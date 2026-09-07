"""HGNC 客户端：人类基因命名委员会数据库查询。

HGNC（HUGO Gene Nomenclature Committee）负责人类基因的标准命名。
API：https://rest.genenames.org/，免鉴权，支持JSON和XML格式。
参考：https://www.genenames.org/help/rest/
"""
from __future__ import annotations

from typing import Any, Optional

from bio_mcp.core.http import BioHTTP

BASE = "https://rest.genenames.org"


class HGNCClient:
    def __init__(self) -> None:
        # HGNC REST 需 Accept: application/json 头才会返回 JSON（否则返回 XML）
        self._http = BioHTTP(
            base_url=BASE,
            timeout=20.0,
            headers={"Accept": "application/json"},
        )

    def gene_search(self, query: str) -> dict[str, Any]:
        """按基因符号或名称搜索HGNC基因信息。

        query 示例：
          BRCA1           基因符号
          TP53            基因符号
          breast cancer   基因名称关键词
        """
        try:
            # 使用fetch端点搜索
            resp = self._http.get(f"fetch/search/{query}")
            return {
                "query": query,
                "results": resp.json() if resp.status_code == 200 else [],
                "status": resp.status_code
            }
        except Exception as e:
            return {"query": query, "results": [], "error": str(e)}

    def gene_by_symbol(self, symbol: str) -> dict[str, Any]:
        """按基因符号获取详细信息。

        symbol 示例：
          BRCA1           基因符号（标准格式）
          TP53            基因符号
        """
        try:
            # 使用symbol端点获取特定基因信息
            resp = self._http.get(f"fetch/symbol/{symbol}")
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, dict) and "response" in data:
                    docs = data["response"].get("docs", [])
                    if docs:
                        return {"symbol": symbol, "data": docs[0]}
                return {"symbol": symbol, "data": data}
            return {"symbol": symbol, "error": f"Status {resp.status_code}"}
        except Exception as e:
            return {"symbol": symbol, "error": str(e)}

    def close(self) -> None:
        self._http.close()