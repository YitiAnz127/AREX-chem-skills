"""QuickGO 基因本体工具。

Gene Ontology（GO）是描述基因产物功能的标准化本体，分为
生物学过程（biological_process）/ 分子功能（molecular_function）/ 细胞组分（cellular_component）三方面。
工具：
  - go_term_lookup: 按 GO ID 查询本体术语详情
  - go_term_search: 按关键词搜索 GO 术语
  - gene_go_annotation: 按基因产品 ID 查询 GO 注释
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.quickgo import QuickGOClient

_client: QuickGOClient | None = None

ASPECT_CN = {
    "biological_process": "生物学过程",
    "molecular_function": "分子功能",
    "cellular_component": "细胞组分",
}


def _get_client() -> QuickGOClient:
    global _client
    if _client is None:
        _client = QuickGOClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="go_term_lookup",
        description=(
            "Look up a Gene Ontology term by GO ID. "
            "按 GO 编号查询基因本体（GO）术语详情：输入 GO ID"
            "（如 GO:0006915），返回术语名称、所属方面（生物学过程/"
            "分子功能/细胞组分）、定义与同义词，用于理解基因功能注释含义。"
        ),
    )
    def go_term_lookup_tool(go_id: str) -> str:
        """查询 GO 术语详情。

        Args:
            go_id: GO 编号（如 GO:0006915）
        """
        client = _get_client()
        result = client.term_by_id(go_id)
        return _format_term_result(result)

    @server.tool(
        name="go_term_search",
        description=(
            "Search Gene Ontology terms by keyword. "
            "按关键词搜索基因本体（GO）术语：输入英文关键词"
            "（如 apoptosis / kinase / membrane），返回匹配的 GO 术语列表，"
            "含编号、名称与所属方面，用于功能注释与富集分析。"
        ),
    )
    def go_term_search_tool(keyword: str, limit: int = 10) -> str:
        """搜索 GO 术语。

        Args:
            keyword: 搜索关键词
            limit: 返回条数（1-25）
        """
        client = _get_client()
        result = client.term_search(keyword, min(limit, 25))
        return _format_search_result(result)

    @server.tool(
        name="gene_go_annotation",
        description=(
            "Get GO annotations for a gene product. "
            "按基因产品 ID 查询其基因本体（GO）注释：输入如 "
            "UniProtKB:P04637（TP53），返回该基因的 GO 注释列表"
            "（GO ID、方面、限定词与证据），用于功能理解与富集分析。"
        ),
    )
    def gene_go_annotation_tool(
        gene_product_id: str,
        aspect: str = "",
        limit: int = 20,
    ) -> str:
        """查询基因的 GO 注释。

        Args:
            gene_product_id: 基因产品 ID（如 UniProtKB:P04637）
            aspect: 可选过滤方面（biological_process/molecular_function/cellular_component）
            limit: 返回条数（1-50）
        """
        client = _get_client()
        valid_aspects = {"", "biological_process", "molecular_function", "cellular_component"}
        if aspect not in valid_aspects:
            return f"未知方面「{aspect}」，可选：biological_process / molecular_function / cellular_component"
        result = client.gene_annotations(gene_product_id, aspect, min(limit, 50))
        return _format_annotation_result(result)


def _format_term_result(result: dict) -> str:
    """格式化 GO 术语详情。"""
    if "error" in result:
        return f"QuickGO 查询错误: {result['error']}"

    data = result.get("data") or {}
    results = data.get("results") or []
    if not results:
        return f"未找到 GO 术语「{result['go_id']}」。"
    r = results[0]

    lines = [
        f"# GO 术语",
        f"",
        f"- **GO ID**: {r.get('id', '')}",
        f"- **名称 / Name**: {r.get('name', '')}",
    ]
    aspect = r.get("aspect", "")
    if aspect:
        lines.append(f"- **方面 / Aspect**: {aspect}（{ASPECT_CN.get(aspect, '')}）")
    if r.get("isObsolete"):
        lines.append(f"- **状态 / Status**: ⚠️ 已废弃（obsolete）")
    definition = (r.get("definition") or {}).get("text", "")
    if definition:
        lines.append(f"- **定义 / Definition**: {definition[:400]}")
    synonyms = [s.get("name") for s in (r.get("synonyms") or []) if s.get("name")]
    if synonyms:
        lines.append(f"- **同义词 / Synonyms**: {', '.join(synonyms[:6])}")
    children = r.get("children") or []
    if children:
        lines.append(f"- **子术语数 / Children**: {len(children)}")

    lines.append("")
    lines.append("来源：QuickGO（EBI 基因本体服务）。")
    return "\n".join(lines)


def _format_search_result(result: dict) -> str:
    """格式化 GO 术语搜索结果。"""
    if "error" in result:
        return f"QuickGO 搜索错误: {result['error']}"

    keyword = result.get("keyword", "")
    data = result.get("data") or {}
    hits = data.get("numberOfHits", 0)
    results = data.get("results") or []

    if not results:
        return f"未找到与「{keyword}」相关的 GO 术语。"

    lines = [
        f"# GO 术语搜索结果",
        f"",
        f"关键词：{keyword}",
        f"总命中：{hits}",
        f"",
    ]

    for r in results[:15]:
        aspect = r.get("aspect", "")
        obsolete = " ⚠️" if r.get("isObsolete") else ""
        lines.append(
            f"- **{r.get('id', '')}** {r.get('name', '')} · {aspect}{obsolete}"
        )

    if len(results) > 15:
        lines.append(f"- ...（共 {hits} 条，展示前 15 条）")

    lines.append("")
    lines.append("来源：QuickGO（EBI 基因本体服务）。")
    return "\n".join(lines)


def _format_annotation_result(result: dict) -> str:
    """格式化基因 GO 注释。"""
    if "error" in result:
        return f"QuickGO 注释查询错误: {result['error']}"

    gene_id = result.get("gene_id", "")
    data = result.get("data") or {}
    total = data.get("numberOfHits", 0)
    annotations = data.get("results") or []

    if not annotations:
        return f"未找到基因「{gene_id}」的 GO 注释。"

    # 统计方面分布
    from collections import Counter

    aspect_counts = Counter(a.get("goAspect", "?") for a in annotations)
    aspect_summary = "、".join(
        f"{ASPECT_CN.get(k, k)} {v}" for k, v in aspect_counts.items()
    )

    lines = [
        f"# 基因 GO 注释",
        f"",
        f"基因产品：{gene_id}",
        f"注释总数：{total}（本页 {len(annotations)}）",
        f"方面分布：{aspect_summary}",
        f"",
    ]

    for a in annotations[:30]:
        go_id = a.get("goId", "")
        aspect = a.get("goAspect", "")
        qualifier = a.get("qualifier", "")
        evidence = a.get("evidenceCode", "")
        symbol = a.get("symbol", "")
        refs = a.get("reference", "") or ""
        ref_short = refs[:60] if refs else ""
        q_str = f" ({qualifier})" if qualifier and qualifier != "involved_in" else ""
        lines.append(
            f"- **{go_id}** · {ASPECT_CN.get(aspect, aspect)} · 证据 {evidence}{q_str}"
            + (f" · {symbol}" if symbol else "")
        )
        if ref_short:
            lines.append(f"  来源: {ref_short}")

    if len(annotations) > 30:
        lines.append(f"- ...（还有 {total - 30} 条，可通过 limit 或 aspect 精简）")

    lines.append("")
    lines.append("注：注释接口不返回术语名称，可用 go_term_lookup 查具体 GO ID 的含义。")
    lines.append("来源：QuickGO（EBI 基因本体服务）。")
    return "\n".join(lines)
