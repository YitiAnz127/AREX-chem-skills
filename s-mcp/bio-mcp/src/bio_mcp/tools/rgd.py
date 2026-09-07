"""RGD 大鼠基因组学数据库查询工具。

RGD (Rat Genome Database) 是大鼠模式生物数据库。
工具：
  - rgd_gene_symbol: 按基因符号获取大鼠基因信息
  - rgd_search: 按关键词搜索大鼠基因
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.rgd import RGDClient

_client: RGDClient | None = None


def _get_client() -> RGDClient:
    global _client
    if _client is None:
        _client = RGDClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="rgd_gene_symbol",
        description=(
            "Get rat gene by gene symbol. "
            "按基因符号获取大鼠基因信息：输入大鼠基因符号"
            "（如 Brca1/Tp53），返回基因名称、符号、染色体位置、"
            "功能注释与别名，用于大鼠遗传学研究。"
        ),
    )
    def rgd_gene_symbol_tool(
        symbol: str
    ) -> str:
        """查询大鼠基因。

        Args:
            symbol: 大鼠基因符号（Brca1/Tp53等）
        """
        client = _get_client()
        result = client.gene_by_symbol(symbol)
        return _format_gene_result(result)

    @server.tool(
        name="rgd_search",
        description=(
            "Search rat genes by keyword. "
            "按关键词搜索大鼠基因：输入搜索词"
            "（基因名、功能或符号），返回匹配基因列表，"
            "包含基因符号、名称与 RGD ID，用于基因发现。"
        ),
    )
    def rgd_search_tool(
        term: str
    ) -> str:
        """搜索大鼠基因。

        Args:
            term: 搜索关键词
        """
        client = _get_client()
        result = client.gene_search(term)
        return _format_search_result(result)


def _format_gene_result(result: dict) -> str:
    """格式化基因查询结果。"""
    if "error" in result:
        return f"RGD查询错误: {result['error']}"

    symbol = result.get("symbol", "")
    data = result.get("data")

    if not data:
        return f"未找到大鼠基因「{symbol}」。"

    lines = [
        f"# RGD 大鼠基因",
        f"",
        f"- **基因符号 / Symbol**: {symbol}",
        f""
    ]

    if isinstance(data, dict):
        name = data.get("name") or data.get("full_name")
        rgd_id = data.get("rgd_id") or data.get("id")
        location = data.get("chromosome") or data.get("location")

        if name:
            lines.append(f"- **基因名称 / Name**: {name}")
        if rgd_id:
            lines.append(f"- **RGD ID**: {rgd_id}")
        if location:
            lines.append(f"- **染色体位置 / Location**: {location}")

        for key, value in data.items()[:8]:
            if key not in ("name", "full_name", "rgd_id", "id",
                          "chromosome", "location", "symbol") and value:
                lines.append(f"- **{key}**: {value}")

    lines.append("")
    lines.append("来源：RGD（大鼠基因组学数据库）。")
    return "\n".join(lines)


def _format_search_result(result: dict) -> str:
    """格式化搜索结果。"""
    if "error" in result:
        return f"RGD搜索错误: {result['error']}"

    search_term = result.get("search_term", "")
    results = result.get("results", [])

    if not results:
        return f"未找到与「{search_term}」相关的基因。"

    lines = [
        f"# RGD 搜索结果",
        f"",
        f"搜索词：{search_term}",
        f"结果数：{len(results)}",
        f""
    ]

    for item in results[:10]:
        symbol = item.get("symbol") or item.get("name", "N/A")
        name = item.get("name") or item.get("full_name", "")
        rgd_id = item.get("rgd_id") or item.get("id", "")

        lines.append(f"- **{symbol}**")
        if name:
            lines.append(f"  名称：{name}")
        if rgd_id:
            lines.append(f"  RGD ID：{rgd_id}")

    if len(results) > 10:
        lines.append(f"- ...（共 {len(results)} 条结果）")

    lines.append("")
    lines.append("来源：RGD（大鼠基因组学数据库）。")
    return "\n".join(lines)
