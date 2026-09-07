"""BioGRID 客户端：蛋白互作数据库查询。

BioGRID 是一个公共互作数据库，但其 REST API 需要注册获取 access key
（https://thebiogrid.org/login.php），并非真正零配置。

本项目遵循诚实原则：不再假装"免密钥"。若用户未配置 BIOGRID_ACCESS_KEY
环境变量，工具会明确告知需要注册，而不是静默返回空结果或伪造 key。
"""
from __future__ import annotations

import os
from typing import Any, Optional

from bio_mcp.core.http import BioHTTP

BASE = "https://webservice.biogrid.org"


class BioGRIDClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)
        self._accesskey = os.environ.get("BIOGRID_ACCESS_KEY", "").strip()

    @property
    def configured(self) -> bool:
        """是否已配置有效 access key。"""
        return bool(self._accesskey)

    def _require_key(self) -> Optional[str]:
        """返回错误信息；若已配置 key 则返回 None。"""
        if not self._accesskey:
            return (
                "BioGRID 需要注册 access key（非零配置）。"
                "请在 https://thebiogrid.org/login.php 注册，"
                "然后设置环境变量 BIOGRID_ACCESS_KEY 后重试。"
            )
        return None

    def interactions_search(
        self,
        search_name: str,
        search_type: str = "GENES",
    ) -> dict[str, Any]:
        """搜索蛋白互作数据（需 BIOGRID_ACCESS_KEY）。"""
        err = self._require_key()
        if err:
            return {"query": search_name, "results": [], "needs_key": True, "error": err}
        try:
            params = {
                "searchNames": search_name,
                "searchType": search_type,
                "accesskey": self._accesskey,
                "format": "json",
            }
            resp = self._http.get("interactions", params=params)
            return {
                "query": search_name,
                "results": resp.json() if resp.status_code == 200 else [],
                "status": resp.status_code,
            }
        except Exception as e:
            return {"query": search_name, "results": [], "error": str(e)}

    def gene_interactions(
        self,
        gene_symbol: str,
        organism: Optional[int] = None,
    ) -> dict[str, Any]:
        """按基因符号获取互作数据（需 BIOGRID_ACCESS_KEY）。"""
        err = self._require_key()
        if err:
            return {"gene": gene_symbol, "interactions": [], "needs_key": True, "error": err}
        try:
            params = {
                "searchNames": gene_symbol,
                "searchType": "GENES",
                "accesskey": self._accesskey,
                "format": "json",
            }
            if organism:
                params["organism"] = str(organism)
            resp = self._http.get("interactions", params=params)
            return {
                "gene": gene_symbol,
                "interactions": resp.json() if resp.status_code == 200 else [],
                "status": resp.status_code,
            }
        except Exception as e:
            return {"gene": gene_symbol, "interactions": [], "error": str(e)}

    def close(self) -> None:
        self._http.close()