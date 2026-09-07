"""HTTP 基础客户端：超时、重试、限速、缓存，统一错误处理。"""
from __future__ import annotations

import logging
import random
import threading
import time
from typing import Any, Optional

import httpx

logger = logging.getLogger("bio_mcp")

# NCBI 官方要求：请求间隔 ≥3 秒，且需提供联系方式
NCBI_RATE_LIMIT_SECONDS = 3.0
NCBI_TOOL = "BioMCP"
NCBI_EMAIL = "qgeng1465@users.noreply.github.com"

# 值得重试的状态码：429 限速 + 5xx 服务端错误
_RETRYABLE_STATUS = (408, 429, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511)


class BioHTTPError(RuntimeError):
    """带 HTTP 状态码的请求错误。"""

    def __init__(self, message: str, status_code: Optional[int] = None, url: str = ""):
        super().__init__(message)
        self.status_code = status_code
        self.url = url


class BioHTTP:
    """可复用的 HTTP 客户端：重试 + 退避 + 可配置限速。

    线程安全：限速状态与并发用锁保护；多个线程共享同一实例时仍保持正确节流。
    """

    def __init__(
        self,
        base_url: str = "",
        timeout: float = 30.0,
        max_retries: int = 3,
        rate_limit: float = 0.0,
        headers: Optional[dict[str, str]] = None,
        follow_redirects: bool = True,
        verify: bool = True,
        max_connections: int = 10,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self._rate_limit = rate_limit
        self._max_retries = max(1, int(max_retries))
        self._lock = threading.Lock()
        self._last_request = 0.0
        merged_headers = {
            "User-Agent": (
                f"{NCBI_TOOL} (zero-config bioinformatics MCP server; "
                f"contact: {NCBI_EMAIL})"
            )
        }
        if headers:
            merged_headers.update(headers)
        self._client = httpx.Client(
            timeout=timeout,
            follow_redirects=follow_redirects,
            headers=merged_headers,
            http2=False,
            verify=verify,
            limits=httpx.Limits(
                max_connections=max_connections,
                max_keepalive_connections=max_connections,
            ),
        )

    def _throttle(self) -> None:
        if self._rate_limit <= 0:
            return
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_request
            if elapsed < self._rate_limit:
                time.sleep(self._rate_limit - elapsed)
            self._last_request = time.monotonic()

    def _backoff(self, attempt: int) -> float:
        """指数退避 + 抖动，避免突发重试同步踩点。"""
        return 1.5 * (attempt + 1) + random.uniform(0, 1.0)

    def request(
        self,
        method: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        json: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        if path.startswith("http://") or path.startswith("https://"):
            url = path
        elif path:
            url = f"{self.base_url}/{path.lstrip('/')}"
        else:
            # 空 path：直接请求 base_url，避免画蛇添足的尾部斜杠（部分服务对 / 敏感）
            url = self.base_url
        last_err: Exception | None = None
        for attempt in range(self._max_retries):
            self._throttle()
            try:
                resp = self._client.request(
                    method,
                    url,
                    params=params,
                    json=json,
                    data=data,
                    files=files,
                    headers=headers,
                )
                if (
                    resp.status_code in _RETRYABLE_STATUS
                    and attempt < self._max_retries - 1
                ):
                    time.sleep(self._backoff(attempt))
                    continue
                resp.raise_for_status()
                return resp
            except (httpx.HTTPStatusError, httpx.TransportError) as e:
                last_err = e
                if attempt < self._max_retries - 1:
                    time.sleep(self._backoff(attempt))
                    continue
                break
        status = getattr(last_err, "response", None)
        code = status.status_code if status is not None else None
        raise BioHTTPError(str(last_err), status_code=code, url=url) from last_err

    def get(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return self.request("GET", path, params=params, headers=headers)

    def post(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
        json: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return self.request(
            "POST", path, params=params, json=json, data=data, files=files, headers=headers
        )

    def close(self) -> None:
        self._client.close()
