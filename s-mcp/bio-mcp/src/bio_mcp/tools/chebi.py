"""ChEBI 化学生物学实体查询工具。

ChEBI是EBI的化学实体生物学兴趣数据库。
工具：
  - chebi_compound: 按ChEBI ID查询化合物信息
  - chebi_search: 按化合物名称搜索ChEBI
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.chebi import CHEBIClient

_client: CHEBIClient | None = None


def _get_client() -> CHEBIClient:
    global _client
    if _client is None:
        _client = CHEBIClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="chebi_compound",
        description=(
            "Query ChEBI compound by ChEBI ID. "
            "按 ChEBI ID 查询化合物信息：输入 ChEBI 编号（如 CHEBI:15377 ATP），"
            "返回化合物名称、定义、化学属性与交叉引用，用于化学生物学研究。"
        ),
    )
    def chebi_compound_tool(
        chebi_id: str
    ) -> str:
        """查询ChEBI化合物。

        Args:
            chebi_id: ChEBI ID（CHEBI:15377）
        """
        client = _get_client()
        result = client.compound_by_id(chebi_id)
        return _format_compound_result(result)

    @server.tool(
        name="chebi_search",
        description=(
            "Search ChEBI compounds by name or keyword. "
            "按化合物名称搜索 ChEBI：输入化合物名称或关键词（如 ATP/glucose），"
            "返回匹配的化合物列表，包含 ChEBI ID、名称与定义，用于化合物查询。"
        ),
    )
    def chebi_search_tool(
        name: str
    ) -> str:
        """搜索ChEBI化合物。

        Args:
            name: 化合物名称或关键词
        """
        client = _get_client()
        result = client.compound_search(name)
        return _format_search_result(result)


def _format_compound_result(result: dict) -> str:
    """格式化化合物查询结果。"""
    if "error" in result:
        return f"ChEBI查询错误: {result['error']}"

    chebi_id = result.get("chebi_id", "")
    data = result.get("data")

    if not data:
        return f"未找到 ChEBI 化合物「{chebi_id}」。"

    lines = [
        f"# ChEBI 化合物",
        f"",
        f"- **ChEBI ID**: {data.get('acc', chebi_id)}",
    ]

    if isinstance(data, dict):
        name = data.get("name")
        description = data.get("description")

        if name:
            lines.append(f"- **名称 / Name**: {name}")
        if description:
            lines.append(f"- **定义 / Definition**: {description[:400]}")

    lines.append("")
    lines.append("来源：ChEBI（EBI 化学生物学实体数据库，via EBI Search）。")
    return "\n".join(lines)


def _format_search_result(result: dict) -> str:
    """格式化搜索结果。"""
    if "error" in result:
        return f"ChEBI搜索错误: {result['error']}"

    search_term = result.get("search_term", "")
    hit_count = result.get("hit_count", 0)
    results = result.get("results", [])

    if not results:
        return f"未找到与「{search_term}」相关的化合物。"

    lines = [
        f"# ChEBI 搜索结果",
        f"",
        f"搜索词：{search_term}",
        f"命中数：{hit_count}（显示前 {len(results)} 条）",
        f""
    ]

    for item in results[:10]:
        chebi_id = item.get("acc") or item.get("id", "N/A")
        name = item.get("name", "N/A")

        lines.append(f"- **{chebi_id}**: {name}")

    lines.append("")
    lines.append("来源：ChEBI（EBI 化学生物学实体数据库，via EBI Search）。")
    return "\n".join(lines)
