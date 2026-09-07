---
name: bio-mcp-usage
description: How to query the 43 BioMCP databases effectively — tool selection per data type, NCBI rate limits, honest verification. Use whenever a task involves literature search, sequences, structures, enrichment, interactions, compounds, omics data, or the intelligent_analyze agent.
---

# BioMCP Usage Guide / BioMCP 使用指南

This skill explains how to use BioMCP tools correctly and honestly. 本 skill 说明如何正确、诚实地使用 BioMCP 工具。

## Workflow / 工作流

1. **Detect the data type first** 先判断数据类型 → call `intelligent_analyze(input, goal)` to get a recommended plan + expected results + insights. Let the agent pick tools and save tokens.
2. **Verify before trusting** 使用前先确认 → if unsure an endpoint is reachable, call `db_health_check`; for critical conclusions, cross-check with `tool_inventory` to know which tools are e2e verified vs best-effort.
3. **Prefer the specialized tool** 优先专用工具 → e.g. a UniProt ID goes to `uniprot_annotate`, not to general literature search.

## Tool selection by data type / 按数据类型选工具

| Input 输入 | Recommended tools 推荐工具 |
|---|---|
| Gene symbol 基因符号 | `uniprot_annotate`, `ensembl_gene_lookup`, `hgnc_gene_symbol`, `gene_enrichment`, `string_interactions`, `gene_full_profile` |
| Protein ID 蛋白 ID | `uniprot_annotate`, `protein_domains`, `alphafold_structure` |
| DNA/protein sequence 序列 | `blast_search`, `ncbi_fetch_sequence` |
| Variant 变异 | `variant_annotate`, `dbsnp_search`, `clinvar_query` |
| Compound/drug 化合物/药物 | `compound_info`, `chembl_drug_search`, `unichem_mapping`, `chebi_compound` |
| Pathway 通路 | `reactome_pathway_search`, `kegg_pathway_search` |
| Disease 疾病 | `europepmc_search`, `pubmed_search`, `openalex_work_search` |
| Plant gene 植物基因 | `plant_gene_lookup` (species name, e.g. `arabidopsis`) |
| Model organism 模式生物 | `flybase_gene`, `wormbase_gene`, `rgd_gene_symbol` |
| Sequencing data 测序数据 | `sra_search`, `bioproject_search`, `biosample_search` |
| Proteomics 蛋白质组学 | `pride_search`, `pride_project` |
| Microbiome 微生物组 | `microbiome_study_search` |
| Single-cell 单细胞 | `cellxgene_search` |
| Lipid/metabolite/glycan 脂质/代谢物/糖 | `lipid_lookup`, `metabolomics_study`, `glycan_lookup` |
| Batch gene list 基因列表 | `gene_enrichment` (≥2 genes) |

## Rules 规则

- **NCBI rate limit**: ≥3 s between E-utilities requests. When a query needs several NCBI calls, expect delays; do not time out impatiently.
  NCBI 限速：两次 E-utilities 请求间隔 ≥3 秒，多查询需耐心等待。
- **`gene_enrichment`** requires ≥2 genes; unknown library names are rejected. 至少 2 个基因，未知基因集库会被拒绝。
- **BioGRID** needs `BIOGRID_ACCESS_KEY`; without it returns an honest error, do not invent results. 需要 key，无 key 时如实报错。
- **Honesty**: report results as retrieved from the public APIs. Do not fabricate database entries, citation counts, or IDs. 如实报告 API 返回结果，不得编造。
- **`gene_full_profile`** queries Ensembl + UniProt + STRING + PubMed concurrently — a fast way to cross-validate one gene. 跨 4 库交叉验证。
- **BLAST queries** can take 30-60 s; set expectations accordingly. BLAST 可能需要 30-60 秒。
