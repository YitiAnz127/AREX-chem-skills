"""GWAS Catalog 客户端：全基因组关联研究（GWAS）数据查询。

GWAS Catalog 是 EMBL-EBI 托管的变异-性状关联数据库，免鉴权。
API：https://www.ebi.ac.uk/gwas/rest/api/
参考：https://www.ebi.ac.uk/gwas/rest/api/docs

能力：
  - variant_associations：按 rsID 查询该变异的 GWAS 关联（含 p 值/风险频率）
  - association_efo_traits：按关联自链获取 EFO 性状标签
  - gene_variants：按基因查询关联的 GWAS 变异（rsID）
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://www.ebi.ac.uk/gwas/rest/api"


class GWASCatalogClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def variant_associations(self, rsid: str) -> dict[str, Any]:
        """按 rsID 查询变异的 GWAS 关联。

        rsid：dbSNP 编号（如 'rs73229090'）
        返回 associations 列表，每个关联含 pvalueMantissa/Exponent、
        riskFrequency、snpType、loci 等字段；trait 需经 association_efo_traits 获取。
        """
        try:
            resp = self._http.get(
                "associations/search/findByRsId", params={"rsId": rsid}
            )
            data = resp.json()
            associations = (data.get("_embedded") or {}).get("associations", [])
            return {
                "rsid": rsid,
                "associations": associations,
                "total": len(associations),
                "status": resp.status_code,
            }
        except Exception as e:  # noqa: BLE001
            return {"rsid": rsid, "error": str(e)}

    def association_efo_traits(self, association_url: str) -> list[str]:
        """按关联的自链 URL 获取 EFO 性状标签。"""
        try:
            resp = self._http.get(association_url)
            data = resp.json()
            traits = (data.get("_embedded") or {}).get("efoTraits", [])
            return [t.get("trait") for t in traits if t.get("trait")]
        except Exception:  # noqa: BLE001
            return []

    def gene_variants(self, gene: str, limit: int = 20) -> dict[str, Any]:
        """按基因查询关联的 GWAS 变异。

        gene：基因符号（如 'TP53'）
        """
        try:
            resp = self._http.get(
                "singleNucleotidePolymorphisms/search/findByGene",
                params={"geneName": gene, "page": 0, "size": min(limit, 50)},
            )
            data = resp.json()
            snps = (data.get("_embedded") or {}).get(
                "singleNucleotidePolymorphisms", []
            )
            total = data.get("page", {}).get("totalElements", len(snps))
            return {
                "gene": gene,
                "snps": snps,
                "total": total,
                "status": resp.status_code,
            }
        except Exception as e:  # noqa: BLE001
            return {"gene": gene, "error": str(e)}

    def close(self) -> None:
        self._http.close()
