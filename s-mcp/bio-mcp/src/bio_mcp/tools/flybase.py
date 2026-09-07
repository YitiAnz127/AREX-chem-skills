"""FlyBase 果蝇遗传学数据库查询工具。

FlyBase是果蝇模式生物数据库，提供全面的基因组学数据。
工具：
  - flybase_gene: 按基因ID获取果蝇基因信息
  - flybase_search: 按关键词搜索果蝇基因
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.flybase import FlyBaseClient

_client: FlyBaseClient | None = None


def _get_client() -> FlyBaseClient:
    global _client
    if _client is None:
        _client = FlyBaseClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="flybase_gene",
        description=(
            "Get Drosophila gene by FlyBase ID. "
            "按 FlyBase ID 获取果蝇基因信息：输入果蝇基因编号"
            "（如 FBgn0000015），返回基因名称、符号、染色体位置、"
            "功能注释与别名，用于果蝇遗传学研究。"
        ),
    )
    def flybase_gene_tool(
        gene_id: str
    ) -> str:
        """查询果蝇基因。

        Args:
            gene_id: FlyBase基因ID（FBgn0000015）
        """
        client = _get_client()
        result = client.gene_by_id(gene_id)
        return _format_gene_result(result)

    @server.tool(
        name="flybase_search",
        description=(
            "Search Drosophila genes by keyword. "
            "按关键词搜索果蝇基因：输入搜索词"
            "（基因名、功能或符号），返回匹配基因列表，"
            "包含基因 ID、符号与名称，用于基因发现。"
        ),
    )
    def flybase_search_tool(
        term: str
    ) -> str:
        """搜索果蝇基因。

        Args:
            term: 搜索关键词
        """
        client = _get_client()
        result = client.gene_search(term)
        return _format_search_result(result)


def _format_gene_result(result: dict) -> str:
    """格式化基因查询结果。"""
    if "error" in result:
        return f"FlyBase查询错误: {result['error']}"

    gene_id = result.get("gene_id", "")
    data = result.get("data")

    if not data:
        return f"未找到 FlyBase 基因「{gene_id}」。"

    lines = [
        f"# FlyBase 果蝇基因",
        f"",
        f"- **基因ID / Gene ID**: {gene_id}",
        f""
    ]

    if isinstance(data, dict):
        symbol = data.get("symbol") or data.get("primarySymbol")
        name = data.get("name") or data.get("fullName")
        location = data.get("chromosome_location") or data.get("location")

        if symbol:
            lines.append(f"- **基因符号 / Symbol**: {symbol}")
        if name:
            lines.append(f"- **基因名称 / Name**: {name}")
        if location:
            lines.append(f"- **染色体位置 / Location**: {location}")

        for key, value in data.items()[:8]:
            if key not in ("symbol", "primarySymbol", "name", "fullName",
                          "chromosome_location", "location") and value:
                lines.append(f"- **{key}**: {value}")

    lines.append("")
    lines.append("来源：FlyBase（果蝇遗传学与基因组学数据库）。")
    return "\n".join(lines)


def _format_search_result(result: dict) -> str:
    """格式化搜索结果。"""
    if "error" in result:
        return f"FlyBase搜索错误: {result['error']}"

    search_term = result.get("search_term", "")
    results = result.get("results", [])

    if not results:
        return f"未找到与「{search_term}」相关的基因。"

    lines = [
        f"# FlyBase 搜索结果",
        f"",
        f"搜索词：{search_term}",
        f"结果数：{len(results)}",
        f""
    ]

    for item in results[:10]:
        gene_id = item.get("gene_id") or item.get("id", "N/A")
        symbol = item.get("symbol") or item.get("primarySymbol", "N/A")
        name = item.get("name") or item.get("fullName", "")

        lines.append(f"- **{gene_id}**: {symbol}")
        if name:
            lines.append(f"  名称：{name}")

    if len(results) > 10:
        lines.append(f"- ...（共 {len(results)} 条结果）")

    lines.append("")
    lines.append("来源：FlyBase（果蝇遗传学与基因组学数据库）。")
    return "\n".join(lines)
