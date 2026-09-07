"""WormBase 客户端：线虫遗传学和基因组学数据库。

WormBase是秀丽隐杆线虫模式生物数据库。
API：https://rest.wormbase.org/，免鉴权。
参考：https://rest.wormbase.org/
"""
from __future__ import annotations

from typing import Any, Optional

from bio_mcp.core.http import BioHTTP

BASE = "https://rest.wormbase.org"


class WormBaseClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def gene_by_id(self, gene_id: str) -> dict[str, Any]:
        """按基因ID获取线虫基因信息。

        gene_id：WormBase基因ID（WBGene00000001）或基因名。
        使用现行 widget 端点：/rest/widget/gene/{id}/overview
        """
        try:
            resp = self._http.get(f"rest/widget/gene/{gene_id}/overview")
            data = resp.json() if resp.status_code == 200 else None
            if data and isinstance(data, dict):
                fields = data.get("fields", {})
                name = (fields.get("name") or {}).get("data") or {}
                return {
                    "gene_id": gene_id,
                    "symbol": (name or {}).get("label", ""),
                    "sequence_name": (fields.get("sequence_name") or {}).get("data", ""),
                    "locus_name": (fields.get("locus_name") or {}).get("data", ""),
                    "concise_description": (
                        (fields.get("concise_description") or {}).get("data") or {}
                    ).get("text", ""),
                    "classification": (
                        (fields.get("classification") or {}).get("data") or {}
                    ).get("prose_description", ""),
                    "taxonomy": (fields.get("taxonomy") or {}).get("data", {}),
                    "other_names": (fields.get("other_names") or {}).get("data", []),
                    "data": fields,
                    "status": resp.status_code
                }
            return {"gene_id": gene_id, "data": None, "status": resp.status_code}
        except Exception as e:
            return {"gene_id": gene_id, "data": None, "error": str(e)}

    def gene_search(self, term: str) -> dict[str, Any]:
        """按关键词搜索线虫基因（尽力而为）。

        term：搜索关键词（基因名/功能等）
        注：WormBase REST 公开搜索端点已变动，本方法为 best-effort，
        优先尝试按基因名解析到 WBGene 再取 overview。
        """
        try:
            resp = self._http.get(f"rest/widget/gene/{term}/overview")
            data = resp.json() if resp.status_code == 200 else None
            if data and isinstance(data, dict):
                widget = data.get("widget", data)
                return {
                    "search_term": term,
                    "results": [{
                        "id": widget.get("gene", {}).get("id", term),
                        "label": widget.get("gene", {}).get("label", term),
                        "data": widget.get("data", {})
                    }],
                    "status": resp.status_code
                }
            return {
                "search_term": term,
                "results": [],
                "status": resp.status_code,
                "note": "WormBase 公开搜索端点已变动，未解析到该名称的基因。"
            }
        except Exception as e:
            return {"search_term": term, "results": [], "error": str(e)}

    def close(self) -> None:
        self._http.close()