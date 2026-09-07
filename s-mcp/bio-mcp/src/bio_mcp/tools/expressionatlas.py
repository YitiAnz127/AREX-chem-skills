"""Expression Atlas 基因表达查询工具。

Expression Atlas是EBI的基因表达知识库，包含不同条件和组织中的基因表达数据。
工具：
  - expression_atlas_gene: 查找与某基因相关的表达实验（诚实版）
  - expression_atlas_experiment: 按关键词搜索表达实验
"""
from __future__ import annotations

from bio_mcp.core.expressionatlas import ExpressionAtlasClient

_client: ExpressionAtlasClient | None = None


def _get_client() -> ExpressionAtlasClient:
    global _client
    if _client is None:
        _client = ExpressionAtlasClient()
    return _client


def register(server):
    """注册Expression Atlas工具到MCP服务器"""

    @server.tool("expression_atlas_gene", description="Find Expression Atlas experiments relevant to a gene. Public REST no longer exposes numeric per-gene expression values; this returns experiments whose description/species match the gene (e.g. TP53, ENSG00000141510), where expression can be viewed. 查找与基因相关的表达实验：输入基因 ID 或符号（TP53/ENSG00000141510）与可选物种，返回匹配的表达实验列表。公开 REST 已不提供单基因数值表达量端点，此处诚实返回相关实验供进一步查看。")
    def expression_atlas_gene_tool(gene_id: str, species: str = "homo sapiens") -> str:
        """查找基因相关表达实验。"""
        client = _get_client()
        result = client.gene_expression(gene_id, species)
        return _format_result(result)

    @server.tool("expression_atlas_experiment", description="Search Expression Atlas experiments by keyword. Input: search term (cancer, tissue, disease). Output: matching experiments with conditions, species, and data availability. 按关键词搜索表达实验：输入搜索词（cancer/tissue/TP53），返回匹配实验列表，包含物种、实验类型与样本数，用于数据发现。")
    def expression_atlas_experiment_tool(term: str) -> str:
        """搜索表达实验。"""
        client = _get_client()
        result = client.experiment_search(term)
        return _format_result(result)


def _format_result(result: dict) -> str:
    """格式化查询结果为字符串。"""
    if "error" in result:
        return f"Expression Atlas查询错误: {result['error']}"

    experiments = result.get("experiments", [])
    total = result.get("total_matches", 0)

    if not experiments:
        subject = result.get("gene_id") or result.get("search_term", "")
        return f"未找到 Expression Atlas 实验（查询词：{subject}）。"

    title = "基因相关实验" if "gene_id" in result else "实验搜索结果"
    lines = [
        f"# Expression Atlas {title}",
        "",
        f"匹配实验数：{total}（显示前 {len(experiments)} 条）",
        "",
    ]

    for e in experiments[:10]:
        acc = e.get("experimentAccession", "N/A")
        desc = e.get("experimentDescription", "")
        species = e.get("species", "")
        etype = e.get("experimentType", "")
        n_assays = e.get("numberOfAssays", "")

        lines.append(f"### {acc}")
        if desc:
            lines.append(f"- 描述：{desc[:200]}")
        if species:
            lines.append(f"- 物种：{species}")
        if etype:
            lines.append(f"- 类型：{etype}")
        if n_assays:
            lines.append(f"- 样本数：{n_assays}")
        lines.append(f"- 链接：https://www.ebi.ac.uk/gxa/experiments/{acc}")
        lines.append("")

    if result.get("note"):
        lines.append(f"诚实说明 / Honest note: {result['note']}")
    lines.append("")
    lines.append("来源：Expression Atlas（EBI 基因表达知识库）。")
    return "\n".join(lines)
