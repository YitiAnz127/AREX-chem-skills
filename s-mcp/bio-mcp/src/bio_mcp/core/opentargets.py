"""Open Targets Platform 客户端：靶点-疾病-遗传学关联。

Open Targets Platform 整合多源证据（遗传学、somatic 突变、药物、文献等），
提供基因/靶点与疾病的评分化关联，免鉴权。
API：GraphQL https://api.platform.opentargets.org/api/v4/graphql

能力：
  - target_info：按 Ensembl 基因 ID 查询靶点信息（符号/名称/类型/基因组定位/同义词）
  - target_disease：查询靶点关联疾病（评分/证据/新颖性）
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://api.platform.opentargets.org/api/v4/graphql"

_TARGET_INFO_QUERY = """
query($id: String!) {
  target(ensemblId: $id) {
    id approvedSymbol approvedName biotype
    synonyms { label }
    genomicLocation { chromosome start end }
  }
}
"""

_TARGET_DISEASE_QUERY = """
query($id: String!, $size: Int!) {
  target(ensemblId: $id) {
    id approvedSymbol
    associatedDiseases(page: { index: 0, size: $size }) {
      count
      rows { score novelty disease { id name } }
    }
  }
}
"""


class OpenTargetsClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=40.0)

    def target_info(self, ensembl_id: str) -> dict[str, Any]:
        """查询靶点基础信息。"""
        try:
            resp = self._http.post(
                "", json={"query": _TARGET_INFO_QUERY, "variables": {"id": ensembl_id}}
            )
            return {"ensembl_id": ensembl_id, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"ensembl_id": ensembl_id, "error": str(e)}

    def target_disease(self, ensembl_id: str, top_n: int = 10) -> dict[str, Any]:
        """查询靶点关联疾病（按评分排序）。"""
        size = min(max(int(top_n), 1), 50)
        try:
            resp = self._http.post(
                "",
                json={
                    "query": _TARGET_DISEASE_QUERY,
                    "variables": {"id": ensembl_id, "size": size},
                },
            )
            return {"ensembl_id": ensembl_id, "top_n": size, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"ensembl_id": ensembl_id, "top_n": size, "error": str(e)}
