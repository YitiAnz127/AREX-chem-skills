"""RGD 客户端：大鼠基因组学数据库。

RGD (Rat Genome Database) 是大鼠模式生物数据库。
API：https://rest.rgd.mcw.edu/rgdws，免鉴权。
参考：https://rest.rgd.mcw.edu/rgdws/swagger-ui/index.html
"""
from __future__ import annotations

from typing import Any, Optional

from bio_mcp.core.http import BioHTTP

BASE = "https://rest.rgd.mcw.edu/rgdws"


class RGDClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def gene_by_symbol(self, symbol: str) -> dict[str, Any]:
        """按基因符号获取大鼠基因信息。

        symbol：大鼠基因符号（Brca1/Tp53等）
        """
        try:
            resp = self._http.get(
                "genes/search",
                params={"symbol": symbol, "limit": 10}
            )
            return {
                "symbol": symbol,
                "data": resp.json() if resp.status_code == 200 else None,
                "status": resp.status_code
            }
        except Exception as e:
            return {"symbol": symbol, "data": None, "error": str(e)}

    def gene_search(self, term: str) -> dict[str, Any]:
        """按关键词搜索大鼠基因。

        term：搜索关键词
        """
        try:
            resp = self._http.get(
                "genes/search",
                params={"query": term, "limit": 20}
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