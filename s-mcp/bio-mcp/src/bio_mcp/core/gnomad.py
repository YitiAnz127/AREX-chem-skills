"""gnomAD 客户端：人群变异频率与基因约束。

gnomAD（Genome Aggregation Database, Broad Institute）是人群等位基因频率与
基因约束的行业标准数据库，免鉴权，官方限速 10 QPM。
API：GraphQL https://gnomad.broadinstitute.org/api

能力：
  - variant_by_id：按 chr-pos-ref-alt 查询变异的人群分层频率（exome/genome）
  - resolve_rsid：把 rsID 解析为 chr-pos-ref-alt（经 variant_search）
  - gene_constraint：按基因符号查询 pLI / LOEUF 等基因约束
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://gnomad.broadinstitute.org/api"
# gnomAD 官方限速 10 QPM，留余量设为 6.5s/请求
RATE_LIMIT = 6.5

# 合法数据集枚举（防注入，只接受白名单）
DATASETS = ("gnomad_r4", "gnomad_r4_genomes", "gnomad_r3", "gnomad_r2_1")

_VARIANT_QUERY = """
query($vid: String!, $ds: DatasetId!) {
  variant(variantId: $vid, dataset: $ds) {
    variant_id rsids chrom pos ref alt
    exome { ac an af homozygote_count
      faf95 { popmax popmax_population }
      faf99 { popmax popmax_population }
      populations { id ac an homozygote_count } }
    genome { ac an af homozygote_count
      faf95 { popmax popmax_population }
      faf99 { popmax popmax_population }
      populations { id ac an homozygote_count } }
  }
}
"""

_SEARCH_QUERY = """
query($q: String!, $ds: DatasetId!) {
  variant_search(query: $q, dataset: $ds) { variant_id }
}
"""

_GENE_QUERY = """
query($g: String!, $rg: ReferenceGenomeId!) {
  gene(gene_symbol: $g, reference_genome: $rg) {
    gene_id symbol
    gnomad_constraint {
      pLI oe_lof oe_lof_upper oe_mis oe_mis_upper syn_z mis_z lof_z
    }
  }
}
"""


class GnomADClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=40.0, rate_limit=RATE_LIMIT)

    def _graphql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        resp = self._http.post("", json={"query": query, "variables": variables})
        return resp.json()

    def variant_by_id(
        self, variant_id: str, dataset: str = "gnomad_r4"
    ) -> dict[str, Any]:
        """按 chr-pos-ref-alt 查询变异人群频率。

        variant_id：如 '6-26092913-G-A'（chrom-pos-ref-alt）
        dataset：gnomad_r4 / gnomad_r4_genomes / gnomad_r3 / gnomad_r2_1
        """
        ds = dataset if dataset in DATASETS else "gnomad_r4"
        try:
            data = self._graphql(_VARIANT_QUERY, {"vid": variant_id, "ds": ds})
            return {"variant_id": variant_id, "dataset": ds, "data": data}
        except Exception as e:  # noqa: BLE001
            return {"variant_id": variant_id, "dataset": ds, "error": str(e)}

    def resolve_rsid(self, rsid: str, dataset: str = "gnomad_r4") -> dict[str, Any]:
        """把 rsID 解析为 chr-pos-ref-alt（返回首个匹配）。"""
        ds = dataset if dataset in DATASETS else "gnomad_r4"
        try:
            data = self._graphql(_SEARCH_QUERY, {"q": rsid, "ds": ds})
            return {"rsid": rsid, "dataset": ds, "data": data}
        except Exception as e:  # noqa: BLE001
            return {"rsid": rsid, "dataset": ds, "error": str(e)}

    def gene_constraint(
        self, gene_symbol: str, reference_genome: str = "GRCh38"
    ) -> dict[str, Any]:
        """按基因符号查询 pLI / LOEUF 等约束指标。"""
        rg = reference_genome if reference_genome in ("GRCh38", "GRCh37") else "GRCh38"
        try:
            data = self._graphql(_GENE_QUERY, {"g": gene_symbol, "rg": rg})
            return {"gene_symbol": gene_symbol, "reference_genome": rg, "data": data}
        except Exception as e:  # noqa: BLE001
            return {"gene_symbol": gene_symbol, "reference_genome": rg, "error": str(e)}
