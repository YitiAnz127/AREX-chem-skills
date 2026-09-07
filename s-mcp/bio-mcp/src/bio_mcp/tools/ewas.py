"""EWAS Atlas 工具：CpG 位点 × 性状/疾病/暴露 表观关联查询。

EWAS Atlas 收录全基因组表观遗传关联研究，可用于反向验证某个甲基化位点
与性状/暴露（如吸烟、环境暴露）的关联，配合 mQTL 数据做"遗传变异→甲基化→表型"
的因果链证据。
工具：
  - ewas_probe_lookup: 按 CpG 位点查询其 EWAS 关联与相关基因
  - ewas_gene_lookup: 按基因符号查询关联的 CpG 探针与关联
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.ewas import EWASClient

_client: EWASClient | None = None


def _get_client() -> EWASClient:
    global _client
    if _client is None:
        _client = EWASClient()
    return _client


def _fmt_assoc(assoc: dict[str, Any]) -> str:
    pmid = assoc.get("pmid")
    pmid_s = f" (PMID:{pmid})" if pmid else ""
    return (
        f"{assoc.get('trait', '—')} [{assoc.get('correlation', '—')} 相关, "
        f"rank={assoc.get('rank', '—')}, study={assoc.get('studyId', '—')}]{pmid_s}"
    )


def _format_probe(result: dict[str, Any]) -> str:
    if result.get("error"):
        return f"查询失败: {result['error']}"
    data = (result.get("data") or {}).get("data")
    if not data:
        return "未检索到该 CpG 位点。"
    lines = [
        f"# EWAS Atlas CpG 位点 / CpG Probe",
        f"探针: {data.get('probeId')} · chr{data.get('chrHg19')}:{data.get('posHg19')} "
        f"(hg19) · CpG岛: {data.get('cpgIsland') or '—'}",
        "",
    ]
    genes = {t.get("geneName") for t in (data.get("relatedTranscription") or []) if t.get("geneName")}
    lines.append(f"相关基因: {', '.join(sorted(genes)) or '—'}")
    lines.append("")
    assoc = data.get("associationList") or []
    if assoc:
        lines.append(f"## 关联性状 / Trait Associations（{len(assoc)} 条）")
        for a in assoc[:20]:
            lines.append(f"- {_fmt_assoc(a)}")
        if len(assoc) > 20:
            lines.append(f"（仅显示前 20 条，共 {len(assoc)} 条）")
    else:
        lines.append("暂无关联性状记录。")
    lines.append("")
    lines.append("说明: correlation 为甲基化水平与性状的相关方向；数据来自公开 EWAS 研究。")
    return "\n".join(lines)


def _format_gene(result: dict[str, Any]) -> str:
    if result.get("error"):
        return f"查询失败: {result['error']}"
    data = (result.get("data") or {}).get("data")
    probes = (data or {}).get("probeList") or []
    if not probes:
        return f"未检索到基因 {result.get('gene_symbol')} 的关联探针。"
    lines = [
        f"# EWAS Atlas 基因关联 / Gene Associations",
        f"基因: {result.get('gene_symbol')} · 关联 {len(probes)} 个 CpG 探针",
        "",
    ]
    for p in probes[:20]:
        assoc = p.get("associationList") or []
        traits = sorted({a.get("trait") for a in assoc if a.get("trait")})
        lines.append(
            f"- {p.get('probeId')} (chr{p.get('chrHg19')}:{p.get('posHg19')}, "
            f"{p.get('cpgIsland') or '—'}): "
            + (", ".join(traits) if traits else "无关联记录")
        )
    if len(probes) > 20:
        lines.append(f"（仅显示前 20 个探针，共 {len(probes)} 个）")
    lines.append("")
    lines.append("说明: 每个探针列出其已报道的 EWAS 关联性状。")
    return "\n".join(lines)


def register(server: Any) -> None:
    @server.tool(
        name="ewas_probe_lookup",
        description=(
            "Look up EWAS associations for a CpG probe. "
            "按 CpG 位点查询 EWAS Atlas 中该甲基化位点的关联性状/疾病/暴露"
            "（含相关方向、研究编号与 PMID）及相关基因，用于反向验证甲基化位点"
            "与表型的关联。用法：ewas_probe_lookup('cg05575921')。"
        ),
    )
    def ewas_probe_lookup_tool(probe_id: str) -> str:
        """查询 CpG 位点的 EWAS 关联。"""
        client = _get_client()
        return _format_probe(client.probe_lookup(probe_id.strip()))

    @server.tool(
        name="ewas_gene_lookup",
        description=(
            "Look up EWAS CpG probes associated with a gene. "
            "按基因符号查询 EWAS Atlas 中与该基因相关的 CpG 探针及其关联性状，"
            "用于从基因出发了解其甲基化位点的表观遗传关联。用法：ewas_gene_lookup('AHRR')。"
        ),
    )
    def ewas_gene_lookup_tool(gene_symbol: str) -> str:
        """查询基因关联的 CpG 探针。"""
        client = _get_client()
        return _format_gene(client.gene_lookup(gene_symbol.strip()))
