"""PRIDE 蛋白质组学数据查询工具。

PRIDE是EBI的质谱分析蛋白质组学数据库。
工具：
  - pride_project: 按项目ID获取蛋白质组学项目
  - pride_search: 按关键词搜索蛋白质组学项目
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.pride import PRIDEClient

_client: PRIDEClient | None = None


def _get_client() -> PRIDEClient:
    global _client
    if _client is None:
        _client = PRIDEClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="pride_project",
        description=(
            "Get PRIDE proteomics project by ID. "
            "按项目 ID 获取蛋白质组学项目：输入 PXD 项目编号"
            "（如 PXD000001），返回项目标题、摘要、物种、实验类型与"
            "数据文件，用于蛋白质组学数据获取。"
        ),
    )
    def pride_project_tool(
        project_id: str
    ) -> str:
        """查询PRIDE项目。

        Args:
            project_id: PXD项目ID（PXD000001）
        """
        client = _get_client()
        result = client.project_by_id(project_id)
        return _format_project_result(result)

    @server.tool(
        name="pride_search",
        description=(
            "Search PRIDE proteomics projects by keyword. "
            "按关键词搜索蛋白质组学项目：输入搜索词"
            "（如 cancer/human/tissue），返回匹配项目列表，"
            "包含项目标题、物种与数据访问链接，用于数据发现。"
        ),
    )
    def pride_search_tool(
        keyword: str
    ) -> str:
        """搜索PRIDE项目。

        Args:
            keyword: 搜索关键词
        """
        client = _get_client()
        result = client.project_search(keyword)
        return _format_search_result(result)


def _format_project_result(result: dict) -> str:
    """格式化项目查询结果。"""
    if "error" in result:
        return f"PRIDE查询错误: {result['error']}"

    project_id = result.get("project_id", "")
    data = result.get("data")

    if not data:
        return f"未找到 PRIDE 项目「{project_id}」。"

    lines = [
        f"# PRIDE 蛋白质组学项目",
        f"",
        f"- **项目ID / Accession**: {project_id}",
        f""
    ]

    if isinstance(data, dict):
        title = data.get("title") or data.get("name")
        desc = data.get("projectDescription") or data.get("description") or data.get("abstract")

        if title:
            lines.append(f"- **标题 / Title**: {title}")
        if desc:
            truncated = desc if len(desc) <= 300 else desc[:300] + "..."
            lines.append(f"- **摘要 / Abstract**: {truncated}")

        def _plain(values: Any) -> list[str]:
            out = []
            for v in values or []:
                if isinstance(v, dict):
                    out.append(v.get("name", ""))
                elif v:
                    out.append(str(v))
            return [x for x in out if x]

        organisms = _plain(data.get("organisms"))
        if organisms:
            lines.append(f"- **物种 / Organisms**: {', '.join(organisms[:5])}")
        diseases = _plain(data.get("diseases"))
        if diseases:
            lines.append(f"- **疾病 / Diseases**: {', '.join(diseases[:5])}")
        submission_date = data.get("submissionDate", "")
        if submission_date:
            lines.append(f"- **提交日期 / Submitted**: {submission_date}")
        doi = data.get("doi", "")
        if doi:
            lines.append(f"- **DOI**: {doi}")

    lines.append("")
    lines.append("来源：PRIDE（EBI 质谱分析蛋白质组学数据库）。")
    return "\n".join(lines)


def _format_search_result(result: dict) -> str:
    """格式化搜索结果。"""
    if "error" in result:
        return f"PRIDE搜索错误: {result['error']}"

    keyword = result.get("keyword", "")
    results = result.get("results", [])

    if not results:
        return f"未找到与「{keyword}」相关的项目。"

    lines = [
        f"# PRIDE 搜索结果",
        f"",
        f"搜索词：{keyword}",
        f"结果数：{len(results)}",
        f""
    ]

    for item in results[:10]:
        acc = item.get("accession") or item.get("id", "N/A")
        title = item.get("title") or item.get("name", "N/A")
        organisms = item.get("organisms") or []
        diseases = item.get("diseases") or []

        lines.append(f"- **{acc}**: {title}")
        if organisms:
            lines.append(f"  物种：{', '.join(organisms[:3])}")
        if diseases:
            lines.append(f"  疾病：{', '.join(diseases[:3])}")
        description = item.get("description", "")
        if description:
            lines.append(f"  简介：{description[:120]}")

    if len(results) > 10:
        lines.append(f"- ...（共 {len(results)} 条结果）")

    lines.append("")
    lines.append("来源：PRIDE（EBI 质谱分析蛋白质组学数据库）。")
    return "\n".join(lines)
