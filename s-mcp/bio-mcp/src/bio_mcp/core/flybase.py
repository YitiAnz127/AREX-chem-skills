"""FlyBase 客户端：果蝇遗传学和基因组学数据库。

FlyBase是果蝇模式生物数据库，提供全面的基因组学数据。
API：https://api.flybase.org/，免鉴权。
参考：https://flybase.github.io/
"""
from __future__ import annotations

from typing import Any, Optional

from bio_mcp.core.http import BioHTTP

BASE = "https://api.flybase.org/api/v1.0"


class FlyBaseClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def gene_by_id(self, gene_id: str) -> dict[str, Any]:
        """按基因ID获取果蝇基因信息。

        gene_id：FlyBase基因ID（FBgn0000015）
        """
        try:
            resp = self._http.get(f"genes/{gene_id}", params={"format": "json"})
            return {
                "gene_id": gene_id,
                "data": resp.json() if resp.status_code == 200 else None,
                "status": resp.status_code
            }
        except Exception as e:
            return {"gene_id": gene_id, "data": None, "error": str(e)}

    def gene_search(self, term: str) -> dict[str, Any]:
        """按关键词搜索果蝇基因。

        term：搜索关键词（基因名/功能等）
        """
        try:
            resp = self._http.get(
                "genes/search",
                params={"q": term, "format": "json"}
            )
            return {
                "search_term": term,
                "results": resp.json() if resp.status_code == 200 else [],
                "status": resp.status_code
            }
        except Exception as e:
            return {"search_term": term, "results": [], "error": str(e)}

    def close(self) -> None:
        self._http.close()