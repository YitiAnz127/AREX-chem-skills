"""WormBase 线虫遗传学数据库查询工具。

WormBase是秀丽隐杆线虫模式生物数据库。
工具：
  - wormbase_gene: 按基因ID获取线虫基因信息
  - wormbase_search: 按关键词搜索线虫基因
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.wormbase import WormBaseClient

_client: WormBaseClient | None = None


def _get_client() -> WormBaseClient:
    global _client
    if _client is None:
        _client = WormBaseClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="wormbase_gene",
        description=(
            "Get C. elegans gene by WormBase ID. "
            "按 WormBase ID 获取线虫基因信息：输入线虫基因编号"
            "（如 WBGene00000001），返回基因名称、符号、染色体位置、"
            "功能注释与序列信息，用于线虫生物学研究。"
        ),
    )
    def wormbase_gene_tool(
        gene_id: str
    ) -> str:
        """查询线虫基因。

        Args:
            gene_id: WormBase基因ID（WBGene00000001）
        """
        client = _get_client()
        result = client.gene_by_id(gene_id)
        return _format_gene_result(result)

    @server.tool(
        name="wormbase_search",
        description=(
            "Search C. elegans genes by keyword. "
            "按关键词搜索线虫基因：输入搜索词"
            "（基因名、功能或符号），返回匹配基因列表，"
            "包含基因 ID、符号与名称，用于基因发现。"
        ),
    )
    def wormbase_search_tool(
        term: str
    ) -> str:
        """搜索线虫基因。

        Args:
            term: 搜索关键词
        """
        client = _get_client()
        result = client.gene_search(term)
        return _format_search_result(result)


def _format_gene_result(result: dict) -> str:
    """格式化基因查询结果。"""
    if "error" in result:
        return f"WormBase查询错误: {result['error']}"

    gene_id = result.get("gene_id", "")
    symbol = result.get("symbol", "")
    sequence_name = result.get("sequence_name", "")
    locus_name = result.get("locus_name", "")
    description = result.get("concise_description", "")
    classification = result.get("classification", "")
    taxonomy = result.get("taxonomy", {}) or {}
    other_names = result.get("other_names", []) or []

    if not symbol and not sequence_name:
        return f"未找到 WormBase 基因「{gene_id}」。"

    lines = [
        f"# WormBase 线虫基因",
        f"",
        f"- **基因ID / Gene ID**: {gene_id}",
    ]

    if symbol:
        lines.append(f"- **基因符号 / Symbol**: {symbol}")
    if sequence_name:
        lines.append(f"- **序列名称 / Sequence name**: {sequence_name}")
    if locus_name and locus_name != "not assigned":
        lines.append(f"- **位点名称 / Locus name**: {locus_name}")
    if taxonomy:
        genus = taxonomy.get("genus", "")
        species = taxonomy.get("species", "")
        if genus or species:
            lines.append(f"- **物种 / Species**: {genus} {species}".strip())
    if classification:
        lines.append(f"- **基因类型 / Type**: {classification[:200]}")
    if description:
        lines.append(f"- **功能描述 / Description**: {description[:400]}")
    if other_names:
        lines.append(f"- **别名 / Aliases**: {', '.join(other_names[:8])}")

    lines.append("")
    lines.append("来源：WormBase（线虫遗传学与基因组学数据库）。")
    return "\n".join(lines)


def _format_search_result(result: dict) -> str:
    """格式化搜索结果。"""
    if "error" in result:
        return f"WormBase搜索错误: {result['error']}"

    search_term = result.get("search_term", "")
    results = result.get("results", [])

    if not results:
        return f"未找到与「{search_term}」相关的基因。"

    lines = [
        f"# WormBase 搜索结果",
        f"",
        f"搜索词：{search_term}",
        f"结果数：{len(results)}",
        f""
    ]

    for item in results[:10]:
        gene_id = item.get("gene_id") or item.get("id", "N/A")
        symbol = item.get("symbol") or item.get("name", "N/A")
        name = item.get("name") or item.get("sequence_name", "")

        lines.append(f"- **{gene_id}**: {symbol}")
        if name and name != symbol:
            lines.append(f"  名称：{name}")

    if len(results) > 10:
        lines.append(f"- ...（共 {len(results)} 条结果）")

    lines.append("")
    lines.append("来源：WormBase（线虫遗传学与基因组学数据库）。")
    return "\n".join(lines)
