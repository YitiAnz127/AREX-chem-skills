"""QuickGO 客户端：基因本体（Gene Ontology）查询服务。

QuickGO 是 EMBL-EBI 的基因本体注释与本体查询服务，免鉴权。
API：https://www.ebi.ac.uk/QuickGO/services/
参考：https://www.ebi.ac.uk/QuickGO/api/

能力：
  - term_by_id：按 GO ID 查询本体 term 详情（名称/定义/方面/同义词）
  - term_search：按关键词搜索 GO term
  - gene_annotations：按基因产品 ID（如 UniProtKB:P04637）查询 GO 注释
    （注意：注释接口不返回 goName，需结合 term_by_id 获取术语名称）
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://www.ebi.ac.uk/QuickGO/services"


class QuickGOClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def term_by_id(self, go_id: str) -> dict[str, Any]:
        """按 GO ID 查询 term 详情。

        go_id：GO 编号（如 'GO:0006915'）
        """
        try:
            resp = self._http.get(f"ontology/go/terms/{go_id}")
            return {"go_id": go_id, "data": resp.json(), "status": resp.status_code}
        except Exception as e:  # noqa: BLE001
            return {"go_id": go_id, "error": str(e)}

    def term_search(self, keyword: str, limit: int = 10) -> dict[str, Any]:
        """按关键词搜索 GO term。

        keyword：搜索词（支持英文关键词或 GO 编号）
        """
        try:
            resp = self._http.get(
                "ontology/go/search", params={"query": keyword, "limit": min(limit, 25)}
            )
            return {"keyword": keyword, "data": resp.json(), "status": resp.status_code}
        except Exception as e:  # noqa: BLE001
            return {"keyword": keyword, "error": str(e)}

    def gene_annotations(
        self, gene_product_id: str, aspect: str = "", limit: int = 20
    ) -> dict[str, Any]:
        """按基因产品 ID 查询 GO 注释。

        gene_product_id：基因产品标识（如 'UniProtKB:P04637' / 'MGI:...'）
        aspect：可选过滤，'biological_process' / 'molecular_function' / 'cellular_component'
        """
        params: dict[str, Any] = {"geneProductId": gene_product_id, "limit": min(limit, 50)}
        if aspect:
            params["aspect"] = aspect
        try:
            resp = self._http.get("annotation/search", params=params)
            return {
                "gene_id": gene_product_id,
                "data": resp.json(),
                "status": resp.status_code,
            }
        except Exception as e:  # noqa: BLE001
            return {"gene_id": gene_product_id, "error": str(e)}

    def close(self) -> None:
        self._http.close()
