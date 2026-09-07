"""HGNC 基因命名查询工具。

HGNC (HUGO Gene Nomenclature Committee) 负责人类基因的标准命名。
工具：
  - hgnc_search: 搜索人类基因命名信息
  - hgnc_gene_symbol: 按符号获取详细基因信息
"""
from __future__ import annotations

from bio_mcp.core.hgnc import HGNCClient
from bio_mcp.core.cache import cached

_client: HGNCClient | None = None


def _get_client() -> HGNCClient:
    global _client
    if _client is None:
        _client = HGNCClient()
    return _client


def register(server):
    """注册HGNC工具到MCP服务器"""

    @server.tool("hgnc_search", description="Search human gene nomenclature by symbol or name. Input: gene symbol (BRCA1) or name keyword. Output: HGNC gene information with approved symbols, names, and aliases.")
    def hgnc_search_tool(query: str) -> str:
        """Search HGNC gene nomenclature."""
        client = _get_client()
        result = client.gene_search(query)
        return _format_result(result)

    @server.tool("hgnc_gene_symbol", description="Get detailed human gene information by HGNC approved symbol. Input: gene symbol (BRCA1, TP53). Output: Complete gene nomenclature data including aliases, chromosomal location, and previous symbols.")
    def hgnc_gene_symbol_tool(symbol: str) -> str:
        """Get HGNC gene by symbol."""
        client = _get_client()
        result = client.gene_by_symbol(symbol)
        return _format_result(result)


def _format_result(result: dict) -> str:
    """格式化查询结果为字符串。"""
    if "error" in result:
        return f"HGNC查询错误: {result['error']}"

    if not result.get("results") and not result.get("data"):
        return f"未找到HGNC数据: {result.get('query', result.get('symbol', ''))}"

    if "results" in result:
        results = result["results"]
        if isinstance(results, list) and len(results) > 0:
            first = results[0]
            return f"""HGNC基因信息: {result.get('query', '')}

- 基因符号: {first.get('symbol', 'N/A')}
- 基因名称: {first.get('name', 'N/A')}
- HGNC ID: {first.get('hgnc_id', 'N/A')}
- 染色体位置: {first.get('chromosome', 'N/A')}
- 别名: {', '.join(first.get('alias_symbol', [])[:5])}
- 前用符号: {', '.join(first.get('prev_symbol', [])[:5])}
- 基因家族: {first.get('gene_family', 'N/A')}
- 审批日期: {first.get('date_approved', 'N/A')}

共找到 {len(results)} 条相关结果。"""

    if "data" in result:
        data = result["data"]
        if isinstance(data, dict):
            return f"""HGNC基因详细信息: {result.get('symbol', '')}

- 基因符号: {data.get('symbol', 'N/A')}
- 基因名称: {data.get('name', 'N/A')}
- HGNC ID: {data.get('hgnc_id', 'N/A')}
- 染色体位置: {data.get('chromosome', 'N/A')}
- 别名: {', '.join(data.get('alias_symbol', [])[:5])}
- 前用符号: {', '.join(data.get('prev_symbol', [])[:5])}
- 基因家族: {data.get('gene_family', 'N/A')}
- 审批日期: {data.get('date_approved', 'N/A')}"""

    return str(result)