"""BioSamples 生物样本查询工具。

BioSamples是NCBI的样本描述数据库，记录样本的元数据信息。
通过 NCBI E-utilities（db=biosample）零配置直连。
工具：
  - biosample_by_id: 按样本ID获取样本元数据
  - biosample_search: 按关键词搜索样本
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.ncbi import NCBIClient

_client: NCBIClient | None = None


def _get_client() -> NCBIClient:
    global _client
    if _client is None:
        _client = NCBIClient()
    return _client


def register(server):
    """注册BioSamples工具到MCP服务器"""

    @server.tool("biosample_by_id", description="Get biological sample metadata by sample ID. Input: sample ID (SAMN00000001, SAMEA123456). Output: sample accession, title, organism, status. 按样本ID获取生物样本元数据（通过 NCBI E-utilities）。")
    def biosample_by_id_tool(sample_id: str) -> str:
        """Get BioSample by ID."""
        client = _get_client()
        result = client.biosample_search(sample_id, retmax=1)
        return _format_result(result)

    @server.tool("biosample_search", description="Search biological samples by keywords. Input: search term (human[Organism], cancer, tissue:lung). Output: list of matching samples with metadata. 按关键词搜索生物样本（通过 NCBI E-utilities）。")
    def biosample_search_tool(term: str) -> str:
        """Search BioSamples."""
        client = _get_client()
        result = client.biosample_search(term, retmax=5)
        return _format_result(result)


def _format_result(result: dict) -> str:
    """格式化查询结果为字符串。"""
    if "error" in result:
        return f"BioSamples查询错误: {result['error']}"

    samples = result.get("samples", [])

    if not samples:
        query = result.get("count")
        return f"未找到BioSample记录（命中数: {result.get('count', 0)}）。"

    lines = [f"# BioSample 检索结果 / BioSample Search Results", f""]
    lines.append(f"- **总命中数 / Total hits**: {result.get('count', 0)}")
    lines.append("")

    for s in samples[:5]:
        lines.append(f"### {s.get('accession', 'N/A')}")
        lines.append(f"- 标题 / Title: {s.get('title', 'N/A')}")
        lines.append(f"- 物种 / Organism: {s.get('organism', 'N/A')}")
        lines.append(f"- 状态 / Status: {s.get('status', 'N/A')}")
        lines.append(f"- 发布日期 / Date: {s.get('date', 'N/A')}")
        lines.append("")

    lines.append("来源：NCBI BioSample（E-utilities）。")
    return "\n".join(lines)
