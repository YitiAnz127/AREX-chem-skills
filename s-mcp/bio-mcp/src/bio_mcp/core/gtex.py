"""GTEx Portal v2 客户端：组织特异基因表达与 eQTL。

GTEx（Genotype-Tissue Expression）提供跨 54 个组织的正常组织基因表达
与单组织 eQTL 关联，是组织特异表达与调控研究的金标准资源，免鉴权。
API：REST https://gtexportal.org/api/v2

能力：
  - resolve_gene：接受基因符号或 ENSG ID，符号经 Ensembl REST 解析为 ENSG
  - median_expression：查询基因在全部组织的分位数标准化中位表达（TPM）
  - single_tissue_eqtl：查询基因在指定组织的单组织 eQTL 关联
"""
from __future__ import annotations

import re
from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://gtexportal.org/api/v2"
ENSEMBL_LOOKUP = "https://rest.ensembl.org/lookup/symbol/homo_sapiens"

# GTEx v2 常用组织名（tissueSiteDetailId）
KNOWN_TISSUES = (
    "Whole_Blood", "Muscle_Skeletal", "Lung", "Liver",
    "Heart_Left_Ventricle", "Brain_Cortex", "Adipose_Subcutaneous",
    "Adipose_Visceral_Omentum", "Artery_Aorta", "Artery_Tibial",
    "Skin_Sun_Exposed_Lower_leg", "Thyroid", "Nerve_Tibial",
    "Cells_Cultured_fibroblasts", "Pancreas", "Kidney_Cortex",
)

_ENSG = re.compile(r"^ENSG\d{11}(\.\d+)?$", re.IGNORECASE)


class GTExClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=40.0)
        self._ensembl = BioHTTP(base_url=ENSEMBL_LOOKUP, timeout=30.0)

    def resolve_gene(self, query: str) -> dict[str, Any]:
        """把基因符号/ENSG ID 解析为 gencodeId（ENSG）。

        ENSG 直接返回；符号则调 Ensembl REST 解析。返回带 gencode_id 与 gene_symbol。
        """
        query = query.strip()
        if _ENSG.match(query):
            return {"gencode_id": query, "gene_symbol": None}
        try:
            resp = self._ensembl.get(f"/{query}", headers={"Content-Type": "application/json"})
            data = resp.json()
            if isinstance(data, dict) and data.get("id") and data.get("display_name"):
                return {"gencode_id": data["id"], "gene_symbol": data["display_name"]}
            if isinstance(data, list) and data:
                return {
                    "gencode_id": data[0].get("id"),
                    "gene_symbol": data[0].get("display_name"),
                }
            return {"gencode_id": None, "gene_symbol": None, "error": f"未在人类基因组中解析到基因 {query}"}
        except Exception as e:  # noqa: BLE001
            return {"gencode_id": None, "gene_symbol": None, "error": str(e)}

    def median_expression(self, gencode_id: str) -> dict[str, Any]:
        """查询基因在全部组织的分位数标准化中位表达。"""
        try:
            resp = self._http.get(
                "expression/medianGeneExpression",
                params={"gencodeId": gencode_id, "datasetId": "gtex_v8"},
            )
            return {"gencode_id": gencode_id, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"gencode_id": gencode_id, "error": str(e)}

    def single_tissue_eqtl(self, gencode_id: str, tissue: str) -> dict[str, Any]:
        """查询基因在指定组织的单组织 eQTL。"""
        try:
            resp = self._http.get(
                "association/singleTissueEqtl",
                params={
                    "gencodeId": gencode_id,
                    "tissueSiteDetailId": tissue,
                    "datasetId": "gtex_v8",
                },
            )
            return {"gencode_id": gencode_id, "tissue": tissue, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"gencode_id": gencode_id, "tissue": tissue, "error": str(e)}
