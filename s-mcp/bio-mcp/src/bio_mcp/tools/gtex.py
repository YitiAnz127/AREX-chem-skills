"""GTEx 工具：组织特异表达与 eQTL。

GTEx 提供正常组织中的基因表达与调控（eQTL）数据，用于组织特异性分析：
  工具：
  - gtex_tissue_expression: 基因在各组织的分位数标准化中位表达（TPM）
  - gtex_eqtl: 基因在指定组织的单组织 eQTL 关联
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.gtex import GTExClient

_client: GTExClient | None = None


def _get_client() -> GTExClient:
    global _client
    if _client is None:
        _client = GTExClient()
    return _client


def _tissue_short(tissue_id: str) -> str:
    """把 tissueSiteDetailId 转成更可读的展示名。"""
    return tissue_id.replace("_", " ")


def _format_expression(result: dict[str, Any]) -> str:
    if result.get("error"):
        return f"查询失败: {result['error']}"
    data = result.get("data") or {}
    gene = data.get("gene") or {}
    medians = data.get("medianGeneExpression") or []
    if not medians:
        return f"未检索到基因 {gene.get('gencodeId')} 的组织表达数据。"
    gene_symbol = gene.get("geneSymbol") or result.get("gencode_id")
    # 按表达量降序排序，取前 15
    medians_sorted = sorted(
        medians,
        key=lambda m: (m.get("medianGeneExpression") or m.get("median") or 0),
        reverse=True,
    )
    lines = [
        f"# GTEx 组织特异表达 / Tissue Expression",
        f"基因: {gene_symbol} ({gene.get('gencodeId')}) · 数据: GTEx v8",
        "",
        "| 组织 | 中位表达 (TPM) |",
        "|---|---|",
    ]
    for m in medians_sorted[:15]:
        val = m.get("medianGeneExpression") or m.get("median") or 0
        lines.append(f"| {_tissue_short(m.get('tissueSiteDetailId', '—'))} | {val:.2f} |")
    if len(medians_sorted) > 15:
        lines.append(f"\n（仅显示表达量最高的前 15 个组织，共 {len(medians_sorted)} 个组织）")
    lines.append("")
    lines.append("说明: 表达量为 GTEx 分位数标准化后的中位表达（TPM）。")
    return "\n".join(lines)


def _format_eqtl(result: dict[str, Any]) -> str:
    if result.get("error"):
        return f"查询失败: {result['error']}"
    data = result.get("data") or {}
    assoc = data.get("associations") or []
    if not assoc:
        return (
            f"未检索到基因 {result.get('gencode_id')} 在 "
            f"{_tissue_short(result.get('tissue', ''))} 的 eQTL 关联。"
        )
    lines = [
        f"# GTEx 单组织 eQTL / Single-Tissue eQTL",
        f"基因: {data.get('geneSymbol')} ({data.get('gencodeId')}) · "
        f"组织: {_tissue_short(result.get('tissue', ''))} · 数据: GTEx v8",
        "",
        "| 变异位点 | p 值 | MAF | slope |",
        "|---|---|---|---|",
    ]
    for a in assoc[:15]:
        lines.append(
            f"| {a.get('variantId', '—')} | {a.get('pValue', 1):.2e} "
            f"| {a.get('maf', '—')} | {a.get('slope', '—'):.3f} |"
        )
    if len(assoc) > 15:
        lines.append(f"\n（仅显示前 15 条 eQTL，共 {len(assoc)} 条）")
    lines.append("")
    lines.append("说明: p 值为该组织内变异-基因表达的关联显著性；slope 为效应方向。")
    return "\n".join(lines)


def register(server: Any) -> None:
    @server.tool(
        name="gtex_tissue_expression",
        description=(
            "Look up tissue-specific gene expression from GTEx. "
            "查询基因在 GTEx 各组织中的中位表达（TPM），用于组织特异表达分析。"
            "接受基因符号（如 'TP53'）或 ENSG ID，自动解析。"
            "用法：gtex_tissue_expression('TP53')。"
        ),
    )
    def gtex_tissue_expression_tool(gene: str) -> str:
        """查询基因在各组织的表达。"""
        client = _get_client()
        resolved = client.resolve_gene(gene)
        if resolved.get("error"):
            return f"基因解析失败: {resolved['error']}"
        return _format_expression(client.median_expression(resolved["gencode_id"]))

    @server.tool(
        name="gtex_eqtl",
        description=(
            "Look up single-tissue eQTL from GTEx. "
            "查询基因在指定组织的单组织 eQTL 关联（变异位点、p 值、效应），"
            "用于组织特异调控研究。接受基因符号或 ENSG ID；组织用 GTEx 组织名"
            "（如 'Whole_Blood'、'Liver'）。用法：gtex_eqtl('TP53', 'Whole_Blood')。"
        ),
    )
    def gtex_eqtl_tool(gene: str, tissue: str = "Whole_Blood") -> str:
        """查询基因在指定组织的 eQTL。"""
        client = _get_client()
        resolved = client.resolve_gene(gene)
        if resolved.get("error"):
            return f"基因解析失败: {resolved['error']}"
        return _format_eqtl(client.single_tissue_eqtl(resolved["gencode_id"], tissue.strip()))
