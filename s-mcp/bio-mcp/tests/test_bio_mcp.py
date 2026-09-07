"""BioMCP 单元测试：注册完整性 + 参数校验逻辑（不依赖外部网络）。

真实数据库连通性由 tests/_e2e_smoke.py 覆盖（需网络）。
"""
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pytest


def run(coro):
    """每个用例独立 event loop，避免重入问题。"""
    return asyncio.run(coro)


EXPECTED_TOOLS = {
    # 原有 6
    "pubmed_search",
    "ncbi_fetch_sequence",
    "blast_search",
    "pdb_structure_summary",
    "gene_enrichment",
    "uniprot_annotate",
    # v0.2 新增 10
    "ensembl_gene_lookup",
    "ensembl_homologs",
    "string_interactions",
    "kegg_pathway_search",
    "kegg_pathway_genes",
    "variant_annotate",
    "clinvar_query",
    "protein_domains",
    "compound_info",
    # v0.2 新增 7（开源直连，替换 OpenGWAS）
    "europepmc_search",
    "alphafold_structure",
    "chembl_drug_search",
    "cellxgene_search",
    "ucsc_genome_info",
    "taxonomy_lookup",
    "geo_dataset_search",
    # v0.2 组合工具
    "gene_full_profile",
    # v0.3 新增 10（糖/代谢/病毒/基因组/核酸/质粒/蛋白图谱）
    "glycan_lookup",
    "protein_glycosylation",
    "uniparc_search",
    "uniparc_by_id",
    "metabolomics_study",
    "metabolomics_latest",
    "protein_tissue_expression",
    "genome_assembly_search",
    "dbsnp_search",
    "plasmid_search",
    # v0.4 新增 7（核酸档案/微生物组/通路/文献/脂质/电镜结构/实验互作）
    "ena_sequence_search",
    "microbiome_study_search",
    "reactome_pathway_search",
    "openalex_work_search",
    "lipid_lookup",
    "emdb_structure_lookup",
    "intact_interactions",
    # v0.5 新增：智能 agent / 诚实 agent
    "intelligent_analyze",
    "get_analysis_template",
    "db_health_check",
    "tool_inventory",
    # v0.5 新增：HGNC 基因命名
    "hgnc_search",
    "hgnc_gene_symbol",
    # v0.5 新增：BioGRID 互作（需 key）
    "biogrid_interactions",
    "biogrid_gene_interactions",
    # v0.5 新增：BioSamples 样本
    "biosample_by_id",
    "biosample_search",
    # v0.5 新增：Expression Atlas 表达
    "expression_atlas_gene",
    "expression_atlas_experiment",
    # v0.5 新增：UniChem / ChEBI 化合物
    "unichem_mapping",
    "unichem_structure",
    "chebi_compound",
    "chebi_search",
    # v0.5 新增：PRIDE 蛋白质组学
    "pride_project",
    "pride_search",
    # v0.5 新增：模式生物
    "flybase_gene",
    "flybase_search",
    "wormbase_gene",
    "wormbase_search",
    "rgd_gene_symbol",
    "rgd_search",
    # v0.5 新增：植物 / 测序档案
    "plant_gene_lookup",
    "plant_species_list",
    "sra_search",
    "bioproject_search",
    # v0.6 新增：GO 基因本体（QuickGO）
    "go_term_lookup",
    "go_term_search",
    "gene_go_annotation",
    # v0.6 新增：GWAS Catalog
    "gwas_variant_associations",
    "gwas_gene_variants",
    # v0.7 新增：gnomAD 变异/约束
    "gnomad_variant_lookup",
    "gnomad_gene_constraint",
    # v0.7 新增：GoDMC mQTL
    "mqtl_snp_lookup",
    "mqtl_cpg_lookup",
    # v0.7 新增：EWAS Atlas
    "ewas_probe_lookup",
    "ewas_gene_lookup",
    # v0.7 新增：GTEx 表达/eQTL
    "gtex_tissue_expression",
    "gtex_eqtl",
    # v0.7 新增：Open Targets 靶点-疾病
    "ot_target_info",
    "ot_target_disease",
}


def test_create_server_registers_all_tools():
    from bio_mcp.server import create_server

    server = create_server()

    async def _t():
        return {t.name for t in await server.list_tools()}

    tools = run(_t())
    assert tools == EXPECTED_TOOLS
    assert len(tools) == 83


def test_tool_descriptions_nonempty():
    from bio_mcp.server import create_server

    server = create_server()

    async def _t():
        return {t.name: t.description for t in await server.list_tools()}

    descs = run(_t())
    for name, desc in descs.items():
        assert desc and len(desc) > 10, f"{name} 缺描述"


def test_enrichment_requires_two_genes():
    """校验逻辑：少于 2 个基因直接拒绝。"""
    from bio_mcp.tools.enrichment import register
    from mcp.server.mcpserver import MCPServer

    server = MCPServer(name="t", version="1")
    register(server)

    async def _call():
        return await server.call_tool("gene_enrichment", {"genes": "ONLYONE"})

    res = run(_call())
    text = res.content[0].text if res.content else ""
    assert "至少需要 2 个基因" in text


def test_enrichment_rejects_unknown_library():
    from bio_mcp.tools.enrichment import register
    from mcp.server.mcpserver import MCPServer

    server = MCPServer(name="t", version="1")
    register(server)

    async def _call():
        return await server.call_tool(
            "gene_enrichment", {"genes": "BRCA1,TP53", "library": "NOT_A_LIB"}
        )

    res = run(_call())
    text = res.content[0].text if res.content else ""
    assert "未知基因集库" in text


def test_ncbi_limits_max_ids():
    """max_ids 参数被限制在 1-5。"""
    from bio_mcp.tools.ncbi import register
    from mcp.server.mcpserver import MCPServer

    server = MCPServer(name="t", version="1")
    register(server)

    async def _call():
        return await server.call_tool(
            "ncbi_fetch_sequence", {"query": "TP53", "db": "gene", "max_ids": 99}
        )

    # 不应因 max_ids=99 报错（会被 clamp），走真实网络前 mock 掉
    import bio_mcp.tools.ncbi as ncbi_tool

    orig = ncbi_tool.NCBIClient

    class Fake:
        def esearch(self, db, term, retmax=10, sort=None):
            return {"count": 0, "ids": [], "query": term}

        def close(self):
            pass

    ncbi_tool.NCBIClient = Fake
    try:
        res = run(_call())
    finally:
        ncbi_tool.NCBIClient = orig
    text = res.content[0].text if res.content else ""
    assert "未检索到" in text


def test_all_tools_documented_in_inventory():
    """一致性保障：每个注册工具都必须出现在 tool_inventory 文本中，防止新增库漏文档。"""
    from bio_mcp.server import create_server
    from bio_mcp.tools.honesty import _build_inventory_text

    server = create_server()

    async def _t():
        return {t.name for t in await server.list_tools()}

    tools = run(_t())
    text = _build_inventory_text()
    missing = [
        name
        for name in sorted(tools)
        if re.search(rf"\b{re.escape(name)}\b", text) is None
    ]
    assert not missing, f"以下工具未在 tool_inventory 中列出: {missing}"


def test_intelligence_default_tool_count_matches():
    """DEFAULT_TOTAL_TOOLS 必须与注册工具数一致，防止 token 节省估算失真。"""
    from bio_mcp.server import create_server
    from bio_mcp.tools.intelligence import DEFAULT_TOTAL_TOOLS

    server = create_server()

    async def _t():
        return await server.list_tools()

    tools = run(_t())
    assert len(tools) == DEFAULT_TOTAL_TOOLS, (
        f"intelligence.DEFAULT_TOTAL_TOOLS={DEFAULT_TOTAL_TOOLS} "
        f"与实际注册 {len(tools)} 不一致"
    )


def test_all_tools_in_intelligence_mapping():
    """一致性保障：每个注册工具必须进入智能推荐映射（TOOL_MAPPING），
    或显式标注为 utility/组合工具，防止新增数据库不被智能 agent 推荐。"""
    from bio_mcp.server import create_server
    from bio_mcp.tools.intelligence import RecommendationEngine, UTILITY_TOOLS

    server = create_server()

    async def _t():
        return {t.name for t in await server.list_tools()}

    tools = run(_t())
    mapped = set()
    for tl in RecommendationEngine.TOOL_MAPPING.values():
        mapped.update(tl)
    missing = sorted(tools - mapped - UTILITY_TOOLS)
    assert not missing, (
        f"以下工具未进入智能推荐映射（TOOL_MAPPING/UTILITY_TOOLS）: {missing}"
    )
