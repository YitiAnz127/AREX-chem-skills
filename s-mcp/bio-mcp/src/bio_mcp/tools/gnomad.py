"""gnomAD 人群变异频率与基因约束工具。

gnomAD（Broad Institute）是人群等位基因频率与基因约束的行业标准数据库，
广泛用于变异解读、孟德尔随机化工具变量质量控制与共定位先验。
工具：
  - gnomad_variant_lookup: 按 rsID 或 chr-pos-ref-alt 查询人群分层频率
  - gnomad_gene_constraint: 按基因符号查询 pLI / LOEUF 等约束指标
"""
from __future__ import annotations

import json
import re
from typing import Any

from bio_mcp.core.gnomad import GnomADClient

_client: GnomADClient | None = None

_RS_PATTERN = re.compile(r"^rs\d+$", re.IGNORECASE)
_POS_PATTERN = re.compile(r"^\d+-\d+-[ACGTN]+-[ACGTN]+$", re.IGNORECASE)

# 人群分层常用字段名（gnomAD v4 populations.id）
_POP_CN = {
    "eas": "东亚 (East Asian)",
    "sas": "南亚 (South Asian)",
    "afr": "非洲 (African)",
    "amr": "美洲 (Admixed American)",
    "eur": "欧洲 (European)",
    "mid": "中东 (Middle Eastern)",
}


def _get_client() -> GnomADClient:
    global _client
    if _client is None:
        _client = GnomADClient()
    return _client


def _extract_errors(data: dict[str, Any]) -> list[str]:
    return [e.get("message", "") for e in (data.get("errors") or [])]


def _format_freq(entry: dict[str, Any] | None) -> str:
    """把 exome/genome 频率块格式化为可读字符串。"""
    if not entry:
        return "无数据"
    parts = [f"AF={entry.get('af'):.6f}" if entry.get("af") is not None else "AF=无"]
    parts.append(f"AC={entry.get('ac', 0)}/AN={entry.get('an', 0)}")
    parts.append(f"纯合={entry.get('homozygote_count', 0)}")
    faf95 = entry.get("faf95") or {}
    if faf95:
        parts.append(
            f"faf95_max={faf95.get('popmax')} ({faf95.get('popmax_population')})"
        )
    pops = entry.get("populations") or []
    pop_parts = []
    for p in pops:
        pid = p.get("id", "")
        label = _POP_CN.get(pid, pid)
        ac, an = p.get("ac", 0), p.get("an", 0)
        af = ac / an if an else None
        af_s = f"{af:.6f}" if af is not None else "无"
        pop_parts.append(f"{label}: {af_s}")
    if pop_parts:
        parts.append("人群: " + ", ".join(pop_parts))
    return "; ".join(parts)


def _format_variant(result: dict[str, Any]) -> str:
    data = result.get("data") or {}
    errors = _extract_errors(data)
    if errors:
        return f"查询失败: {'; '.join(errors)}"
    variant = (data.get("data") or {}).get("variant")
    if not variant:
        return f"未找到该变异（dataset={result.get('dataset')}），请核对 ID 或换用其他数据集。"
    lines = [
        f"# gnomAD 变异频率 / Variant Frequency",
        f"变异: {variant.get('variant_id')} · rsID: {', '.join(variant.get('rsids') or []) or '无'}",
        f"位置: chr{variant.get('chrom')}:{variant.get('pos')} {variant.get('ref')}>{variant.get('alt')} · dataset={result.get('dataset')}",
        "",
        "## 外显子组 / Exome",
        _format_freq(variant.get("exome")),
        "",
        "## 全基因组 / Genome",
        _format_freq(variant.get("genome")),
        "",
        "说明: AF 为人群等位基因频率，用于评估变异稀有程度；faf95/faf99 为过滤等位基因频率。",
    ]
    return "\n".join(lines)


def _format_constraint(result: dict[str, Any]) -> str:
    data = result.get("data") or {}
    errors = _extract_errors(data)
    if errors:
        return f"查询失败: {'; '.join(errors)}"
    gene = (data.get("data") or {}).get("gene")
    if not gene:
        return f"未找到该基因（symbol={result.get('gene_symbol')}，reference_genome={result.get('reference_genome')}）。"
    c = gene.get("gnomad_constraint") or {}
    lines = [
        f"# gnomAD 基因约束 / Gene Constraint",
        f"基因: {gene.get('symbol')} ({gene.get('gene_id')})",
        "",
        "## gnomAD 约束指标",
        f"pLI = {c.get('pLI')}  （pLI>0.9 提示强烈纯合无效不耐受）",
        f"LOEUF(oe_lof_upper) = {c.get('oe_lof_upper')}  （越低越不耐受，<0.35 常见于单倍剂量不足敏感基因）",
        f"oe_lof = {c.get('oe_lof')} · oe_mis = {c.get('oe_mis')} · oe_mis_upper = {c.get('oe_mis_upper')}",
        f"syn_z = {c.get('syn_z')} · mis_z = {c.get('mis_z')} · lof_z = {c.get('lof_z')}",
        "",
        "说明: 以上指标来自 gnomAD v4 基因约束表，用于评估基因对功能丧失/错义变异的耐受性。",
    ]
    return "\n".join(lines)


def register(server: Any) -> None:
    @server.tool(
        name="gnomad_variant_lookup",
        description=(
            "Look up population allele frequency for a variant in gnomAD. "
            "按 rsID 或 chr-pos-ref-alt 查询 gnomAD 人群等位基因频率（外显子组/全基因组，"
            "含东亚等各人群分层、纯合计数与 faf95/faf99），用于变异稀有度评估、"
            "孟德尔随机化工具变量质量控制等。用法：gnomad_variant_lookup('rs1800562') 或 "
            "gnomad_variant_lookup('6-26092913-G-A')。"
        ),
    )
    def gnomad_variant_lookup_tool(variant: str, dataset: str = "gnomad_r4") -> str:
        """查询 gnomAD 变异人群频率。"""
        client = _get_client()
        vid = variant.strip()
        if _RS_PATTERN.match(vid) or not _POS_PATTERN.match(vid):
            resolved = client.resolve_rsid(vid, dataset)
            data = resolved.get("data") or {}
            hits = ((data.get("data") or {}).get("variant_search") or [])
            if hits:
                vid = hits[0].get("variant_id") or vid
        result = client.variant_by_id(vid, dataset)
        return _format_variant(result)

    @server.tool(
        name="gnomad_gene_constraint",
        description=(
            "Look up gene constraint metrics (pLI / LOEUF) from gnomAD. "
            "按基因符号查询 gnomAD v4 基因约束指标（pLI、LOEUF/oe_lof_upper、oe_mis 等），"
            "用于判断基因对功能丧失/错义变异的耐受性，辅助致病性评估。"
            "用法：gnomad_gene_constraint('HFE')。"
        ),
    )
    def gnomad_gene_constraint_tool(
        gene_symbol: str, reference_genome: str = "GRCh38"
    ) -> str:
        """查询 gnomAD 基因约束指标。"""
        client = _get_client()
        result = client.gene_constraint(gene_symbol, reference_genome)
        return _format_constraint(result)
