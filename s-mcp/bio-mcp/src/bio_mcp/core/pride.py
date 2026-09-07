"""PRIDE 客户端：蛋白质组学数据仓库。

PRIDE是EBI的质谱分析蛋白质组学数据库。
API：https://www.ebi.ac.uk/pride/ws/archive/v3/，免鉴权。
参考：https://www.ebi.ac.uk/pride/markdownpage/prideapi
"""
from __future__ import annotations

from typing import Any, Optional

from bio_mcp.core.http import BioHTTP

BASE = "https://www.ebi.ac.uk/pride/ws/archive/v3"


def _names(items: Any) -> list[str]:
    """从 PRIDE v3 的 CvParam 对象列表里提取 name 字符串。"""
    names: list[str] = []
    if not isinstance(items, list):
        return names
    for item in items:
        if isinstance(item, dict) and item.get("name"):
            names.append(item["name"])
        elif isinstance(item, str) and item:
            names.append(item)
    return names


class PRIDEClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def project_by_id(self, project_id: str) -> dict[str, Any]:
        """按项目ID获取蛋白质组学项目信息。

        project_id：PXD项目ID（PXD000001）
        """
        try:
            resp = self._http.get(f"projects/{project_id}")
            return {
                "project_id": project_id,
                "data": resp.json() if resp.status_code == 200 else None,
                "status": resp.status_code
            }
        except Exception as e:
            return {"project_id": project_id, "data": None, "error": str(e)}

    def project_search(self, keyword: str, limit: int = 10) -> dict[str, Any]:
        """按关键词搜索蛋白质组学项目。

        keyword：搜索关键词（cancer/human/tissue等）
        使用 PRIDE archive v3 的列表端点 projects?q={keyword}（该 API 无独立 search 端点）。
        """
        try:
            resp = self._http.get(
                "projects",
                params={"q": keyword, "pageSize": limit}
            )
            data = resp.json() if resp.status_code == 200 else []
            results: list[dict[str, Any]] = []
            if isinstance(data, list):
                for p in data[:limit]:
                    results.append(
                        {
                            "accession": p.get("accession", ""),
                            "title": (p.get("title") or "").strip(),
                            "description": (p.get("projectDescription") or "").strip()[:300],
                            "organisms": _names(p.get("organisms")),
                            "diseases": _names(p.get("diseases")),
                            "submission_date": p.get("submissionDate", ""),
                            "doi": p.get("doi", ""),
                        }
                    )
            return {"keyword": keyword, "results": results, "status": resp.status_code}
        except Exception as e:
            return {"keyword": keyword, "results": [], "error": str(e)}

    def close(self) -> None:
        self._http.close()