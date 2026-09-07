"""Open Targets Platform 工具：靶点-疾病关联。

Open Targets Platform 整合遗传学、somatic、药物与文献等多源证据，
提供基因/靶点与疾病的评分化关联，用于药物靶点评估与疾病机制研究。
工具：
  - ot_target_info: 按 Ensembl 基因 ID 查询靶点信息
  - ot_target_disease: 查询靶点关联疾病（评分排序）
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.opentargets import OpenTargetsClient

_client: OpenTargetsClient | None = None


def _get_client() -> OpenTargetsClient:
    global _client
    if _client is None:
        _client = OpenTargetsClient()
    return _client


def _format_target_info(result: dict[str, Any]) -> str:
    if result.get("error"):
        return f"查询失败: {result['error']}"
    data = result.get("data") or {}
    errors = [e.get("message", "") for e in (data.get("errors") or [])]
    if errors:
        return f"查询失败: {'; '.join(errors)}"
    t = (data.get("data") or {}).get("target")
    if not t:
        return f"未找到该靶点（Ensembl ID: {result.get('ensembl_id')}）。"
    loc = t.get("genomicLocation") or {}
    lines = [
        f"# Open Targets 靶点信息 / Target Info",
        f"符号: {t.get('approvedSymbol')} · ID: {t.get('id')}",
        f"全名: {t.get('approvedName')}",
        f"类型: {t.get('biotype')}",
        f"基因组定位: chr{loc.get('chromosome')}:{loc.get('start')}-{loc.get('end')}",
        "",
    ]
    syns = [s.get("label") for s in (t.get("synonyms") or []) if s.get("label")]
    if syns:
        lines.append(f"同义词: {', '.join(syns[:15])}")
    lines.append("")
    lines.append("说明: 数据来自 Open Targets Platform（多源证据整合）。")
    return "\n".join(lines)


def _format_target_disease(result: dict[str, Any]) -> str:
    if result.get("error"):
        return f"查询失败: {result['error']}"
    data = result.get("data") or {}
    errors = [e.get("message", "") for e in (data.get("errors") or [])]
    if errors:
        return f"查询失败: {'; '.join(errors)}"
    t = (data.get("data") or {}).get("target")
    if not t:
        return f"未找到该靶点（Ensembl ID: {result.get('ensembl_id')}）。"
    ad = t.get("associatedDiseases") or {}
    rows = ad.get("rows") or []
    lines = [
        f"# Open Targets 靶点-疾病关联 / Target-Disease Associations",
        f"靶点: {t.get('approvedSymbol')} ({t.get('id')}) · 共 {ad.get('count', len(rows))} 条关联",
        "",
    ]
    if not rows:
        lines.append("暂无关联疾病。")
        return "\n".join(lines)
    lines.append("| 疾病 | 评分 | 新颖性 |")
    lines.append("|---|---|---|")
    for r in rows[:result.get("top_n", 10)]:
        d = r.get("disease") or {}
        lines.append(
            f"| {d.get('name', '—')} ({d.get('id', '—')}) "
            f"| {r.get('score'):.3f} | {r.get('novelty'):.3f} |"
        )
    lines.append("")
    lines.append("说明: 评分 0-1 综合多源证据，越高关联越强；新颖性为最近被证实的程度。")
    return "\n".join(lines)


def register(server: Any) -> None:
    @server.tool(
        name="ot_target_info",
        description=(
            "Look up drug target information from Open Targets Platform. "
            "按 Ensembl 基因 ID 查询 Open Targets 靶点信息（符号、全名、类型、"
            "基因组定位、同义词），用于药物靶点评估与基因功能研究。"
            "用法：ot_target_info('ENSG00000141510')。"
        ),
    )
    def ot_target_info_tool(ensembl_id: str) -> str:
        """查询靶点信息。"""
        client = _get_client()
        return _format_target_info(client.target_info(ensembl_id.strip()))

    @server.tool(
        name="ot_target_disease",
        description=(
            "Look up disease associations for a drug target from Open Targets Platform. "
            "按 Ensembl 基因 ID 查询 Open Targets 评分化靶点-疾病关联（按评分排序，"
            "含新颖性），用于疾病机制研究与药物靶点选择。用法：ot_target_disease('ENSG00000141510', 10)。"
        ),
    )
    def ot_target_disease_tool(ensembl_id: str, top_n: int = 10) -> str:
        """查询靶点关联疾病。"""
        client = _get_client()
        return _format_target_disease(client.target_disease(ensembl_id.strip(), top_n))
