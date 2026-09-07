"""BioMCP — 生物信息学 MCP 服务器入口。

运行方式：
    python -m bio_mcp.server
    # 或安装后直接
    bio-mcp

启动后作为 stdio MCP server 供任意 MCP 客户端调用。
"""
from __future__ import annotations

import asyncio
import logging
import sys

from mcp.server.mcpserver import MCPServer

from bio_mcp import __version__

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # 非终端环境
    pass

DESCRIPTION = (
    "BioMCP — Bioinformatics MCP Server / 生物信息学 MCP 服务器。"
    "Zero-config direct access to 43 open academic databases / "
    "零配置直连 43 个公开学术数据库：PubMed/EuropePMC/OpenAlex literature、"
    "NCBI sequences/BLAST/Taxonomy/GEO/Assembly/dbSNP、ENA nucleotides、"
    "PDB structures、AlphaFold/EMDB cryo-EM predictions、UniProt annotations、"
    "GO/KEGG enrichment、Ensembl genome & homologs、STRING/IntAct interactions、"
    "KEGG/Reactome pathways、MyVariant/ClinVar variants、InterPro domains、"
    "PubChem/ChEMBL/UniChem/ChEBI compounds、QuickGO GO ontology、"
    "GWAS Catalog associations、gnomAD population frequencies & gene constraint、"
    "GoDMC mQTL、EWAS Atlas epigenetics、GTEx tissue expression/eQTL、"
    "Open Targets target-disease、CELLxGENE single-cell、UCSC genomes、"
    "GlyGen glycobiology、LIPID MAPS lipidomics、UniParc archive、"
    "MGnify microbiome、Metabolights metabolomics、Human Protein Atlas、"
    "PRIDE proteomics、HGNC gene nomenclature、BioGRID interactions、"
    "Expression Atlas gene expression、FlyBase/WormBase/RGD model organisms. "
    "Cross-database validation via gene_full_profile / "
    "支持跨库交叉验证 gene_full_profile。"
    "Intelligent agent for data analysis and tool recommendation, "
    "plus honest agents for connectivity checks / "
    "智能agent系统，自动分析数据类型并推荐最佳分析方案，节省token使用；"
    "诚实agent提供数据库连通性检查与工具可信度清单。"
)

INSTRUCTIONS = (
    "BioMCP lets AI assistants query bioinformatics databases directly, "
    "all zero-config. 让 AI 助手直接访问生物数据库，全部零配置。\n"
    "Common usage / 常见用法：\n"
    "- Literature 文献：pubmed_search('BRCA1 breast cancer') / europepmc_search('BRCA1') / openalex_work_search('CRISPR')\n"
    "- Sequences 序列：ncbi_fetch_sequence('NM_007294.4') / ena_sequence_search('tax_tree(562)')\n"
    "- Homology 比对：blast_search(sequence)\n"
    "- Structure 结构：pdb_structure_summary('1crn') / alphafold_structure('P04637') / emdb_structure_lookup('EMD-1234')\n"
    "- Enrichment 富集：gene_enrichment('BRCA1,TP53,EGFR')\n"
    "- Protein 蛋白：uniprot_annotate('P04637')\n"
    "- Genome 基因组：ensembl_gene_lookup('BRCA1') / genome_assembly_search('Escherichia coli[Organism]')\n"
    "- Pathways 通路：reactome_pathway_search('apoptosis')\n"
    "- Interactions 互作：string_interactions('TP53') / intact_interactions('TP53')\n"
    "- Microbiome 微生物组：microbiome_study_search('gut microbiome')\n"
    "- Variants 变异：variant_annotate('chr13:g.32911145G>A') / dbsnp_search('BRCA1[Gene Name] AND Homo sapiens[Organism]') / gnomad_variant_lookup('rs1800562')\n"
    "- Population & methylation 人群频率与甲基化：gnomad_gene_constraint('HFE') / mqtl_snp_lookup('rs6602381') / ewas_probe_lookup('cg05575921')\n"
    "- Expression & targets 组织表达与药物靶点：gtex_tissue_expression('TP53') / gtex_eqtl('TP53', 'Liver') / ot_target_disease('ENSG00000141510')\n"
    "- Drugs 药物：chembl_drug_search('imatinib')\n"
    "- Glycomics 糖组学：glycan_lookup('G00051MO') / protein_glycosylation('P04637')\n"
    "- Lipidomics 脂质组学：lipid_lookup('LMFA01030001')\n"
    "- Metabolomics 代谢组学：metabolomics_study('MTBLS1')\n"
    "- Protein Atlas 蛋白图谱：protein_tissue_expression('ENSG00000141510')\n"
    "- Plasmids 质粒：plasmid_search('pET-28a[Title]')\n"
    "- Single-cell 单细胞：cellxgene_search('organoid')\n"
    "- Plants 植物：plant_gene_lookup('AT1G01010', 'arabidopsis') / plant_species_list()\n"
    "- Sequencing archive 测序档案：sra_search('BRCA1') / bioproject_search('gut microbiome')\n"
    "- Gene naming 基因命名：hgnc_gene_symbol('TP53') / compound ID 映射：unichem_mapping('aspirin')\n"
    "- GO & GWAS 基因本体与遗传关联：go_term_lookup('GO:0006915') / gene_go_annotation('UniProtKB:P04637') / gwas_variant_associations('rs73229090') / gwas_gene_variants('TP53')\n"
    "- Model organisms 模式生物：flybase_gene('FBgn0000015') / wormbase_gene('WBGene00000001') / rgd_gene_symbol('Brca1')\n"
    "- Proteomics 蛋白质组学：pride_search('human plasma')\n"
    "- Honesty 诚实检查：db_health_check() — real connectivity / tool_inventory() — verification status\n"
    "- Combined report 综合报告：gene_full_profile('BRCA1') — queries 4 DBs concurrently\n"
    "- Intelligent analysis 智能分析：intelligent_analyze('TP53', 'function') — auto-detects data type and recommends optimal tools\n"
    "- Get template 获取模板：get_analysis_template('基因研究') — pre-built analysis workflows\n"
    "Note / 注意：NCBI has a rate limit — be patient with multi-query calls; "
    "always double-check results with specialized tools / NCBI 有限速，"
    "多查询请耐心等待；结果请结合专业工具复核。"
)


def create_server() -> MCPServer:
    """构建并注册全部工具的 MCP server。"""
    from bio_mcp.tools import (
        alphafold,
        blast,
        biosamples,
        biogrid,
        cellxgene,
        chebi,
        chembl,
        crosscheck,
        emdb,
        ena,
        enrichment,
        ensembl,
        europepmc,
        ewas,
        expressionatlas,
        flybase,
        glygen,
        gnomad,
        godmc,
        gtex,
        gwas,
        hgnc,
        honesty,
        intact,
        intelligence,
        interpro,
        kegg,
        lipidmaps,
        metabolights,
        mgnify,
        ncbi,
        ncbi_extra,
        openalex,
        opentargets,
        pdb,
        plants,
        pride,
        proteinatlas,
        pubchem,
        pubmed,
        quickgo,
        reactome,
        rgd,
        stringdb,
        ucsc,
        unichem,
        uniparc,
        uniprot,
        variant,
        wormbase,
    )

    server = MCPServer(
        name="bio-mcp",
        title="BioMCP 生物信息学助手",
        description=DESCRIPTION,
        instructions=INSTRUCTIONS,
        version=__version__,
    )
    pubmed.register(server)
    ncbi.register(server)
    blast.register(server)
    pdb.register(server)
    enrichment.register(server)
    uniprot.register(server)
    ensembl.register(server)
    stringdb.register(server)
    kegg.register(server)
    variant.register(server)
    interpro.register(server)
    pubchem.register(server)
    europepmc.register(server)
    alphafold.register(server)
    chembl.register(server)
    cellxgene.register(server)
    ucsc.register(server)
    ncbi_extra.register(server)
    glygen.register(server)
    uniparc.register(server)
    metabolights.register(server)
    proteinatlas.register(server)
    ena.register(server)
    mgnify.register(server)
    reactome.register(server)
    openalex.register(server)
    lipidmaps.register(server)
    emdb.register(server)
    intact.register(server)
    crosscheck.register(server)
    intelligence.register(server)
    # 新增数据库工具 / New database tools
    hgnc.register(server)
    biogrid.register(server)
    biosamples.register(server)
    expressionatlas.register(server)
    unichem.register(server)
    chebi.register(server)
    pride.register(server)
    flybase.register(server)
    wormbase.register(server)
    rgd.register(server)
    plants.register(server)
    quickgo.register(server)
    gwas.register(server)
    ewas.register(server)
    gnomad.register(server)
    godmc.register(server)
    gtex.register(server)
    opentargets.register(server)
    honesty.register(server)
    return server


def main() -> None:
    logging.basicConfig(level=logging.WARNING)
    server = create_server()
    asyncio.run(server.run_stdio_async())


if __name__ == "__main__":
    main()
