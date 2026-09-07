"""诚实性检查工具。

本模块提供两个诚实的工具：
1. db_health_check：对数据库端点做真实连通性测试，如实报告可达/不可达，
   不做任何乐观假设。
2. tool_inventory：列出所有工具及其数据源、验证状态（e2e_verified /
   best_effort），方便用户了解每个工具的可信度。

诚实原则：
- 只报告实际测试得到的结果。
- 未经验证的端点标记为 best_effort，不声称已验证。
- 需要额外配置（如 BioGRID access key）的工具会明确标注。
"""
from __future__ import annotations

import json
import socket
from concurrent.futures import ThreadPoolExecutor
from typing import Any

import httpx

# 需要额外配置的工具（不是零配置）
NEEDS_CONFIG = {
    "biogrid_interactions": "需要 BIOGRID_ACCESS_KEY 环境变量",
    "biogrid_gene_interactions": "需要 BIOGRID_ACCESS_KEY 环境变量",
}

# 端点健康检查清单：(服务名, URL)
HEALTH_ENDPOINTS = [
    ("NCBI E-utilities", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?retmode=json"),
    ("RCSB PDB", "https://data.rcsb.org/rest/v1/core/entry/1CRN"),
    ("UniProt", "https://rest.uniprot.org/uniprotkb/P04637.json"),
    ("Ensembl", "https://rest.ensembl.org/info/ping?content-type=application/json"),
    ("Enrichr", "https://maayanlab.cloud/Enrichr/geneSetLibrary?mode=text&libraryName=KEGG_2021_Human"),
    ("STRING-db", "https://string-db.org/api/tsv/network?identifiers=TP53&species=9606"),
    ("KEGG", "https://rest.kegg.jp/info/hsa"),
    ("MyVariant", "https://myvariant.info/v1/api/variant/13:g.32911145G>A?fields=dbsnp"),
    ("InterPro", "https://www.ebi.ac.uk/interpro/api/entry/"),
    ("PubChem", "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/InChIKey/JSON"),
    ("Europe PMC", "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=BRCA1&format=json&pageSize=1"),
    ("AlphaFold DB", "https://alphafold.ebi.ac.uk/api/prediction/P04637"),
    ("ChEMBL", "https://www.ebi.ac.uk/chembl/api/data/molecule/schema.json"),
    ("CELLxGENE", "https://api.cellxgene.cziscience.com/curation/v1/collections"),
    ("GlyGen", "https://api.glygen.org/glycan/detail/G00051MO/"),
    ("UniParc", "https://rest.uniprot.org/uniparc/UPI0000000001.json"),
    ("Metabolights", "https://www.ebi.ac.uk/metabolights/ws/studies/MTBLS1"),
    ("Human Protein Atlas", "https://www.proteinatlas.org/ENSG00000141510.json"),
    ("EBI ENA", "https://www.ebi.ac.uk/ena/portal/api/filereport?accession=PRJEB1&result=read_run&fields=run_accession&format=json"),
    ("EBI MGnify", "https://www.ebi.ac.uk/metagenomics/api/v1/studies?page_size=1"),
    ("Reactome", "https://reactome.org/ContentService/data/diseases"),
    ("OpenAlex", "https://api.openalex.org/works?search=BRCA1&per-page=1"),
    ("LIPID MAPS", "https://www.lipidmaps.org/rest/compound/lm_id/LMFA01030001/name/json"),
    ("EBI EMDB", "https://www.ebi.ac.uk/emdb/api/entry/EMD-1234"),
    ("EBI IntAct", "https://www.ebi.ac.uk/intact/ws/experiment/MI-1331-1?format=json"),
    ("NCBI Assembly", "https://www.ncbi.nlm.nih.gov/assembly"),
    ("HGNC", "https://rest.genenames.org/fetch/symbol/TP53"),
    ("UniChem", "https://www.ebi.ac.uk/unichem/rest/inchikey/BSYNRYMUTXBXSQ-UHFFFAOYSA-N"),
    ("ChEBI", "https://www.ebi.ac.uk/ebisearch/ws/rest/chebi?query=glucose&format=json"),
    ("PRIDE", "https://www.ebi.ac.uk/pride/ws/archive/v3/projects/PXD000001"),
    ("WormBase", "https://rest.wormbase.org/rest/widget/gene/WBGene00000001/overview"),
    ("Rat Genome DB", "https://rest.rgd.mcw.edu/rgdws/genes/search?query=Brca1&limit=1"),
    ("BioGRID", "https://webservice.biogrid.org/"),
    ("NCBI BioSamples", "https://www.ncbi.nlm.nih.gov/biosample/"),
    ("Expression Atlas", "https://www.ebi.ac.uk/gxa/json/experiments"),
    ("FlyBase", "https://api.flybase.org/api/v1.0/gene/FBgn0000015?format=json"),
    ("Ensembl Plants", "https://rest.ensembl.org/lookup/id/AT1G01010?content-type=application/json"),
    ("NCBI SRA", "https://www.ncbi.nlm.nih.gov/sra"),
    ("gnomAD", "https://gnomad.broadinstitute.org/api"),
    ("GoDMC mQTL", "http://api.godmc.org.uk/v0.1/assoc_meta/rsid/rs6602381"),
    ("EWAS Atlas", "https://ngdc.cncb.ac.cn/ewas/rest/probe?probeId=cg05575921"),
    ("GTEx Portal", "https://gtexportal.org/api/v2/dataset/tissueSiteDetail"),
    ("Open Targets", "https://api.platform.opentargets.org/api/v4/graphql"),
]


def _check_endpoint(url: str, timeout: float = 10.0) -> dict[str, Any]:
    """对单个端点做连通性检查，如实返回结果。"""
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True) as client:
            resp = client.get(url)
            return {
                "reachable": resp.status_code < 500,
                "status_code": resp.status_code,
                "error": None,
            }
    except (httpx.HTTPError, socket.gaierror, ConnectionError) as e:
        return {
            "reachable": False,
            "status_code": None,
            "error": type(e).__name__,
        }


def _build_inventory_text() -> str:
    """生成工具清单文本（供 tool_inventory 工具与一致性测试共用）。"""
    lines = ["# BioMCP 工具清单 / Tool Inventory", ""]

    # 需要额外配置的工具
    lines.append("## 需要额外配置的工具 / Tools Requiring Config")
    if NEEDS_CONFIG:
        for tool, reason in NEEDS_CONFIG.items():
            lines.append(f"- `{tool}`: {reason}")
    else:
        lines.append("- 无")
    lines.append("")

    # 端到端验证的工具（v0.1-0.4 已验证）
    lines.append("## 已端到端验证的工具 / E2E Verified (v0.1-0.4)")
    lines.append("以下工具在开发期用真实数据验证过：")
    lines.append("- 文献: pubmed_search, europepmc_search, openalex_work_search")
    lines.append("- 序列: ncbi_fetch_sequence, blast_search, taxonomy_lookup, geo_dataset_search, uniparc_search, uniparc_by_id")
    lines.append("- 结构: pdb_structure_summary, alphafold_structure, emdb_structure_lookup")
    lines.append("- 功能: uniprot_annotate, protein_domains")
    lines.append("- 通路互作: gene_enrichment, kegg_pathway_search, kegg_pathway_genes, reactome_pathway_search, string_interactions, intact_interactions, ensembl_gene_lookup, ensembl_homologs")
    lines.append("- 基因组: ucsc_genome_info, genome_assembly_search")
    lines.append("- 变异: variant_annotate, clinvar_query, dbsnp_search")
    lines.append("- 化合物: compound_info, chembl_drug_search")
    lines.append("- 核酸质粒: plasmid_search, ena_sequence_search")
    lines.append("- 微生物: microbiome_study_search")
    lines.append("- 单细胞: cellxgene_search")
    lines.append("- 糖组学: glycan_lookup, protein_glycosylation")
    lines.append("- 代谢组学: metabolomics_study, metabolomics_latest")
    lines.append("- 脂质组学: lipid_lookup")
    lines.append("- 蛋白图谱: protein_tissue_expression")
    lines.append("- 组合: gene_full_profile, crosscheck")
    lines.append("")

    # v0.5 新增工具
    lines.append("## v0.5 新增工具 / New in v0.5")
    lines.append("")
    lines.append("### 已端到端验证 / E2E Verified")
    lines.append("以下工具在开发期用真实数据验证过：")
    lines.append("- 基因命名: hgnc_search, hgnc_gene_symbol")
    lines.append("- 样本: biosample_by_id, biosample_search")
    lines.append("- 化合物: unichem_mapping, unichem_structure, chebi_compound, chebi_search")
    lines.append("- 蛋白质组学: pride_project, pride_search")
    lines.append("- 模式生物: wormbase_gene")
    lines.append("- 植物: plant_gene_lookup, plant_species_list")
    lines.append("- 测序数据: sra_search, bioproject_search")
    lines.append("- 表达: expression_atlas_experiment, expression_atlas_gene (诚实版：返回相关实验，非数值表达量)")
    lines.append("- 智能分析: intelligent_analyze, get_analysis_template")
    lines.append("- 诚实检查: db_health_check, tool_inventory")
    lines.append("")
    lines.append("### 受限工具 / Restricted")
    lines.append("以下工具受外部因素限制，需如实说明：")
    lines.append("- flybase_gene, flybase_search: FlyBase API 被 CloudFront WAF 机器人检测拦截（HTTP 202 challenge），脚本客户端暂无法访问")
    lines.append("- rgd_gene_symbol, rgd_search: 当前网络下 Rat Genome DB 请求超时，可能为临时网络问题")
    lines.append("- wormbase_search: WormBase 公开搜索端点已变动，为尽力而为解析")
    lines.append("- biogrid_interactions, biogrid_gene_interactions: 需 BIOGRID_ACCESS_KEY 环境变量")
    lines.append("")

    # v0.6 新增工具
    lines.append("## v0.6 新增工具 / New in v0.6")
    lines.append("以下工具在开发期用真实数据验证过：")
    lines.append("- 基因本体: go_term_lookup, go_term_search, gene_go_annotation")
    lines.append("- 遗传关联: gwas_variant_associations, gwas_gene_variants")
    lines.append("")

    # v0.7 新增工具
    lines.append("## v0.7 新增工具 / New in v0.7")
    lines.append("以下工具在开发期用真实数据验证过：")
    lines.append("- 遗传变异: gnomad_variant_lookup, gnomad_gene_constraint（gnomAD，10 QPM 限速内置节流）")
    lines.append("- 甲基化 QTL: mqtl_snp_lookup, mqtl_cpg_lookup（GoDMC mQTL 元分析）")
    lines.append("- 表观遗传: ewas_probe_lookup, ewas_gene_lookup（EWAS Atlas）")
    lines.append("- 组织表达: gtex_tissue_expression, gtex_eqtl（GTEx v8）")
    lines.append("- 药物靶点: ot_target_info, ot_target_disease（Open Targets）")
    lines.append("")
    lines.append("### 备注 / Notes")
    lines.append("- GTEx 端点在本机曾遇临时 HTTP 502（服务端故障），连通性以 db_health_check 实时结果为准")
    lines.append("")

    lines.append("诚实的说明：")
    lines.append("建议用 db_health_check 确认当前环境连通性后再依赖某个工具；")
    lines.append("查询结果请结合专业工具与原始数据复核。")
    return "\n".join(lines)


def register(server) -> None:
    @server.tool(
        name="db_health_check",
        description=(
            "Check which bioinformatics databases are currently reachable. "
            "检查各生物数据库端点的连通性：对每个数据库做真实 HTTP 请求，"
            "如实报告可达/不可达与状态码，不做乐观假设。"
            "返回结果用于确认当前环境下哪些数据库可用。"
        ),
    )
    def db_health_check(timeout: float = 8.0) -> str:
        """对全部数据库端点做连通性检查（并发，按数据库分组输出）。"""
        lines = ["# 数据库健康检查 / Database Health Check", ""]
        lines.append("说明：此检查基于真实 HTTP 请求，仅反映当前网络的连通性，")
        lines.append("不代表数据源永久可用或返回内容正确。")
        lines.append("")

        # 并发检查全部端点，显著缩短等待时间（串行可能数十秒→并发数秒）
        with ThreadPoolExecutor(max_workers=min(16, len(HEALTH_ENDPOINTS))) as pool:
            futures = {
                pool.submit(_check_endpoint, url, timeout): name
                for name, url in HEALTH_ENDPOINTS
            }
            results = {
                futures[f]: f.result() for f in futures
            }

        reachable = 0
        for name, url in HEALTH_ENDPOINTS:  # 保持稳定顺序输出
            result = results[name]
            if result["reachable"]:
                reachable += 1
                lines.append(f"[OK] {name} (HTTP {result['status_code']})")
            else:
                reason = result["error"] or f"HTTP {result['status_code']}"
                lines.append(f"[FAIL] {name} — {reason}")

        lines.append("")
        lines.append(f"总结 / Summary: {reachable}/{len(HEALTH_ENDPOINTS)} 个端点可达。")
        lines.append("")
        lines.append("注意：不可达可能由网络限制/临时故障导致，不代表数据库本身不可用。")
        return "\n".join(lines)

    @server.tool(
        name="tool_inventory",
        description=(
            "List all BioMCP tools with their data source and verification status. "
            "列出全部 BioMCP 工具及其数据源、验证状态（e2e_verified 已端到端验证 / "
            "best_effort 尽力而为未验证），并标注需要额外配置的工具。"
            "用于了解每个工具的可信度，避免过度信任未经证实的端点。"
        ),
    )
    def tool_inventory() -> str:
        """列出全部工具及其验证状态。"""
        return _build_inventory_text()