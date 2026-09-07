"""GWAS Catalog 工具：全基因组关联研究数据查询。

GWAS Catalog 收录已发表的变异-性状关联，是遗传关联研究的权威数据库。
工具：
  - gwas_variant_associations: 按 rsID 查询变异的 GWAS 关联（含性状与效应）
  - gwas_gene_variants: 按基因查询关联的 GWAS 变异
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.gwas import GWASCatalogClient

_client: GWASCatalogClient | None = None


def _get_client() -> GWASCatalogClient:
    global _client
    if _client is None:
        _client = GWASCatalogClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="gwas_variant_associations",
        description=(
            "Get GWAS associations for a variant by rsID. "
            "按 rsID 查询变异的全基因组关联（GWAS）关联：输入 dbSNP 编号"
            "（如 rs73229090），返回该变体的关联性状、p 值、风险等位基因"
            "频率与效应量，用于遗传关联解读与孟德尔随机化（MR）研究。"
        ),
    )
    def gwas_variant_associations_tool(rsid: str) -> str:
        """查询变异的 GWAS 关联。

        Args:
            rsid: dbSNP 编号（如 rs73229090）
        """
        client = _get_client()
        result = client.variant_associations(rsid)
        return _format_associations_result(client, result)

    @server.tool(
        name="gwas_gene_variants",
        description=(
            "Get GWAS variants associated with a gene. "
            "按基因查询全基因组关联（GWAS）研究中与该基因关联的变异："
            "输入基因符号（如 TP53），返回关联变异 rsID 列表，"
            "用于基因-变异-疾病关联研究。"
        ),
    )
    def gwas_gene_variants_tool(gene: str, limit: int = 20) -> str:
        """查询基因相关的 GWAS 变异。

        Args:
            gene: 基因符号（如 TP53）
            limit: 返回条数（1-50）
        """
        client = _get_client()
        result = client.gene_variants(gene, min(limit, 50))
        return _format_gene_variants_result(result)


def _format_associations_result(client: GWASCatalogClient, result: dict) -> str:
    """格式化变异 GWAS 关联结果。"""
    if "error" in result:
        return f"GWAS Catalog 查询错误: {result['error']}"

    rsid = result.get("rsid", "")
    associations = result.get("associations", [])

    if not associations:
        return f"未在 GWAS Catalog 中找到「{rsid}」的关联。"

    lines = [
        f"# GWAS 关联：{rsid}",
        f"",
        f"关联总数：{result.get('total', 0)}",
        f"",
    ]

    # 每个关联取 trait（额外请求，限制数量避免过多请求）
    for i, a in enumerate(associations[:8], 1):
        pval = _pvalue(a)
        risk = a.get("riskFrequency", "")
        or_val = a.get("orPerCopyNum", "")
        beta = a.get("betaNum", "")
        beta_dir = a.get("betaDirection", "")
        snp_type = a.get("snpType", "")

        # 获取该关联的 EFO traits
        links = a.get("_links", {})
        traits_url = links.get("efoTraits", {}).get("href", "")
        traits = client.association_efo_traits(traits_url) if traits_url else []

        lines.append(f"### 关联 {i}")
        if traits:
            lines.append(f"- **性状 / Traits**: {', '.join(traits)}")
        lines.append(f"- **p 值 / P-value**: {pval}")
        if risk:
            lines.append(f"- **风险等位基因频率 / Risk freq**: {risk}")
        if or_val:
            lines.append(f"- **OR**: {or_val}")
        if beta:
            lines.append(f"- **效应 β**: {beta}（{beta_dir}）")
        if snp_type:
            lines.append(f"- **SNP 类型**: {snp_type}")

    if len(associations) > 8:
        lines.append(f"- ...（共 {result.get('total', len(associations))} 条关联，展示前 8 条）")

    lines.append("")
    lines.append("来源：GWAS Catalog（EMBL-EBI）。")
    return "\n".join(lines)


def _format_gene_variants_result(result: dict) -> str:
    """格式化基因关联变异结果。"""
    if "error" in result:
        return f"GWAS Catalog 查询错误: {result['error']}"

    gene = result.get("gene", "")
    snps = result.get("snps", [])
    total = result.get("total", 0)

    if not snps:
        return f"未在 GWAS Catalog 中找到与「{gene}」关联的变异。"

    lines = [
        f"# 基因 GWAS 变异：{gene}",
        f"",
        f"总匹配变异数：{total}",
        f"",
    ]

    seen: set[str] = set()
    for s in snps:
        rs_id = s.get("rsId", "")
        if rs_id in seen:
            continue
        seen.add(rs_id)
        risk_allele = s.get("riskAllele", "")
        lines.append(f"- **{rs_id}**" + (f" · 风险等位 {risk_allele}" if risk_allele else ""))

    if total > len(seen):
        lines.append(f"- ...（还有 {total - len(seen)} 个，可用 limit 增加）")

    lines.append("")
    lines.append("来源：GWAS Catalog（EMBL-EBI）。")
    return "\n".join(lines)


def _pvalue(a: dict) -> str:
    """从 mantissa/exponent 组合 p 值。"""
    mant = a.get("pvalueMantissa")
    exp = a.get("pvalueExponent")
    if mant is not None and exp is not None:
        try:
            return f"{mant:.1f} × 10^{exp}"
        except (TypeError, ValueError):
            pass
    if a.get("pvalue"):
        return str(a["pvalue"])
    return "N/A"
