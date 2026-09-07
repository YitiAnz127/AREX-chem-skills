"""GoDMC mQTL 工具：遗传变异 × DNA 甲基化关联（MR 与共定位的分子层证据）。

GoDMC（Genetics of DNA Methylation Consortium）对 28 个队列做 SNP×CpG mQTL 元分析，
提供"遗传变异 → 甲基化水平"的因果推断中间层数据。
工具：
  - mqtl_snp_lookup: 按 rsID 查询该 SNP 关联的 mQTL（→ CpG 位点）
  - mqtl_cpg_lookup: 按 CpG 位点查询其 mQTL 关联（→ SNP）
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.godmc import GoDMCClient

_client: GoDMCClient | None = None


def _get_client() -> GoDMCClient:
    global _client
    if _client is None:
        _client = GoDMCClient()
    return _client


def _fmt_beta(x: Any) -> str:
    return f"{x:.4f}" if isinstance(x, (int, float)) else "—"


def _format_rows(result: dict[str, Any], direction: str) -> str:
    if result.get("error"):
        return f"查询失败: {result['error']}"
    data = result.get("data") or {}
    rows = data.get("assoc_meta") or []
    if not rows:
        return "未检索到 mQTL 关联。"
    lines = [f"# GoDMC mQTL（{direction}）", f"共 {len(rows)} 条关联：", ""]
    lines.append("| 位点 | beta | pval(mre) | pval(are) | 样本量 | 队列数 | cis/trans |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in rows[:25]:
        pos = r.get("cpg") if direction.startswith("SNP") else r.get("rsid") or r.get("snp")
        lines.append(
            f"| {pos} | {_fmt_beta(r.get('beta_a1'))} | {_fmt_beta(r.get('pval_mre'))} "
            f"| {_fmt_beta(r.get('pval_are'))} | {r.get('samplesize', '—')} "
            f"| {r.get('num_studies', '—')} | {r.get('cistrans', '—')} |"
        )
    if len(rows) > 25:
        lines.append(f"\n（仅显示前 25 条，共 {len(rows)} 条）")
    lines.append("")
    lines.append("说明: pval_mre 为随机效应 meta p 值，pval_are 为固定效应 p 值；")
    lines.append("方向列（direction）表示各队列中效应方向一致性，详见 GoDMC 原文。")
    return "\n".join(lines)


def register(server: Any) -> None:
    @server.tool(
        name="mqtl_snp_lookup",
        description=(
            "Look up SNP-to-CpG methylation QTL associations from GoDMC. "
            "按 rsID 查询该 SNP 的全基因组甲基化数量性状位点（mQTL）关联，"
            "返回关联的 CpG 位点、效应量、p 值与样本量，用于孟德尔随机化的"
            "分子中介层（遗传变异→甲基化）与共定位分析。用法：mqtl_snp_lookup('rs6602381')。"
        ),
    )
    def mqtl_snp_lookup_tool(rsid: str) -> str:
        """查询 SNP 关联的 mQTL（→ CpG 位点）。"""
        client = _get_client()
        return _format_rows(client.assoc_by_rsid(rsid.strip()), "SNP → CpG")

    @server.tool(
        name="mqtl_cpg_lookup",
        description=(
            "Look up CpG-to-SNP methylation QTL associations from GoDMC. "
            "按 CpG 位点（如 cg14380065）查询其遗传变异 mQTL 关联，"
            "返回关联的 SNP、效应量与 p 值，用于反向寻找调控某甲基化位点的"
            "遗传变异（甲基化 MR / 共定位）。用法：mqtl_cpg_lookup('cg14380065')。"
        ),
    )
    def mqtl_cpg_lookup_tool(cpg: str) -> str:
        """查询 CpG 位点的 mQTL 关联（→ SNP）。"""
        client = _get_client()
        return _format_rows(client.assoc_by_cpg(cpg.strip()), "CpG → SNP")
