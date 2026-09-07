"""ChEBI 客户端：化学生物学实体数据库。

ChEBI是EBI的化学实体生物学兴趣数据库。
API：通过EBI Search REST API，免鉴权。
参考：https://www.ebi.ac.uk/chebi/
"""
from __future__ import annotations

from typing import Any, Optional

from bio_mcp.core.http import BioHTTP

BASE = "https://www.ebi.ac.uk"


class CHEBIClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def compound_by_id(self, chebi_id: str) -> dict[str, Any]:
        """按ChEBI ID查询化合物信息。

        chebi_id：ChEBI ID（CHEBI:15377）
        使用 EBI Search 的 entry 端点（https://www.ebi.ac.uk/ebisearch/ws/rest/chebi/entry/{id}）。
        """
        try:
            resp = self._http.get(
                f"ebisearch/ws/rest/chebi/entry/{chebi_id}",
                params={"format": "json", "fields": "acc,id,name,description"}
            )
            data = resp.json() if resp.status_code == 200 else None
            entry = None
            if data and isinstance(data, dict):
                entries = data.get("entries") or []
                if entries:
                    e = entries[0]
                    fields = e.get("fields", {}) or {}
                    name = (fields.get("name") or [""])[0]
                    description = (fields.get("description") or [""])[0]
                    entry = {
                        "acc": e.get("acc", chebi_id),
                        "id": e.get("id", ""),
                        "name": name,
                        "description": description,
                    }
            return {"chebi_id": chebi_id, "data": entry, "status": resp.status_code}
        except Exception as e:
            return {"chebi_id": chebi_id, "data": None, "error": str(e)}

    def compound_search(self, name: str, limit: int = 10) -> dict[str, Any]:
        """按化合物名称搜索ChEBI。

        name：化合物名称（ATP/glucose等）
        使用 EBI Search 关键词检索，取前 limit 条并带出名称字段。
        """
        try:
            resp = self._http.get(
                "ebisearch/ws/rest/chebi",
                params={
                    "query": name,
                    "format": "json",
                    "fields": "acc,id,name",
                    "size": limit,
                }
            )
            data = resp.json() if resp.status_code == 200 else {}
            results: list[dict[str, Any]] = []
            hit_count = 0
            if data and isinstance(data, dict):
                hit_count = int(data.get("hitCount", 0))
                for e in data.get("entries") or []:
                    fields = e.get("fields", {}) or {}
                    results.append(
                        {
                            "acc": e.get("acc", ""),
                            "id": e.get("id", ""),
                            "name": (fields.get("name") or [""])[0],
                        }
                    )
            return {
                "search_term": name,
                "hit_count": hit_count,
                "results": results,
                "status": resp.status_code,
            }
        except Exception as e:
            return {"search_term": name, "hit_count": 0, "results": [], "error": str(e)}

    def close(self) -> None:
        self._http.close()