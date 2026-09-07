"""BioGRID 蛋白互作查询工具。

BioGRID是一个公共数据库，收录蛋白互作和遗传互作数据。
工具：
  - biogrid_interactions: 搜索蛋白互作数据
  - biogrid_gene_interactions: 按基因符号获取互作
"""
from __future__ import annotations

from bio_mcp.core.biogrid import BioGRIDClient

_client: BioGRIDClient | None = None


def _get_client() -> BioGRIDClient:
    global _client
    if _client is None:
        _client = BioGRIDClient()
    return _client


def register(server):
    """注册BioGRID工具到MCP服务器"""

    @server.tool("biogrid_interactions", description="Search protein interaction data from BioGRID database. Input: gene name or identifier (BRCA1, TP53). Output: protein-protein interactions with experimental evidence and publication references.")
    def biogrid_interactions_tool(search_name: str, search_type: str = "GENES") -> str:
        """Search BioGRID interactions."""
        client = _get_client()
        result = client.interactions_search(search_name, search_type)
        return _format_result(result)

    @server.tool("biogrid_gene_interactions", description="Get protein interactions for a specific gene symbol from BioGRID. Input: gene symbol (TP53), optional organism ID (9606=human). Output: interaction partners with experimental evidence and detection methods.")
    def biogrid_gene_interactions_tool(gene_symbol: str, organism: int = 9606) -> str:
        """Get gene interactions from BioGRID."""
        client = _get_client()
        result = client.gene_interactions(gene_symbol, organism)
        return _format_result(result)


def _format_result(result: dict) -> str:
    """格式化查询结果为字符串。"""
    if result.get("needs_key"):
        return (
            "BioGRID 未配置 access key，无法查询。\n\n"
            f"{result['error']}"
        )
    if "error" in result:
        return f"BioGRID查询错误: {result['error']}"

    if not result.get("results") and not result.get("interactions"):
        return f"未找到BioGRID互作数据: {result.get('query', result.get('gene', ''))}"

    interactions = result.get("results", result.get("interactions", []))
    if not interactions:
        return f"未找到BioGRID互作数据"

    if isinstance(interactions, list) and len(interactions) > 0:
        first = interactions[0]
        return f"""BioGRID蛋白互作信息: {result.get('query', result.get('gene', ''))}

- 互作伙伴A: {first.get('SYSTEMATIC_NAME_A', 'N/A')} ({first.get('OFFICIAL_SYMBOL_A', 'N/A')})
- 互作伙伴B: {first.get('SYSTEMATIC_NAME_B', 'N/A')} ({first.get('OFFICIAL_SYMBOL_B', 'N/A')})
- 实验系统: {first.get('EXPERIMENTAL_SYSTEM', 'N/A')}
- 实验方法: {first.get('EXPERIMENTAL_SYSTEM_TYPE', 'N/A')}
- 证据类型: {first.get('THROUGHPUT', 'N/A')}
- 参考文献: {first.get('PUBMEDID', 'N/A')}
- 生物体: {first.get('ORGANISM_A', 'N/A')} x {first.get('ORGANISM_B', 'N/A')}

共找到 {len(interactions)} 条互作记录。"""

    return str(result)