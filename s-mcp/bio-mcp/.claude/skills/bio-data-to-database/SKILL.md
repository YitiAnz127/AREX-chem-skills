---
name: bio-data-to-database
description: Match raw bioinformatics data to the right databases and tools. For each data type gives a ranked list of suitable databases, expected outputs and insights, with two paths — let the intelligent_analyze agent decide, or call the specific tools directly yourself. Use whenever the user asks "what can I do with this data".
---

# Data to Database / 数据 → 数据库匹配

This skill turns raw bio data into a concrete query plan, then offers **two execution paths**: the agent decides and runs it, or you call the specific tools directly. 本 skill 把原始生物数据转化为具体查询方案，并给出**两种执行路径**：由 agent 自动决定并执行，或直接手动调用对应工具。

## Path A — Let the agent decide (token-saving) / 路径 A：让 agent 决定（省 token）

1. Call `intelligent_analyze` with the input + a goal:
   `intelligent_analyze(input="<paste data>", goal="<what you want>")`
2. It returns: detected data type, ranked database/tool options, expected results, and candidate insights — so you (or it) can pick before spending tokens on all databases.
3. Let it call the chosen tools, or run the top 1-2 yourself.

## Path B — Call tools directly (manual) / 路径 B：直接调工具（手动）

Skip the agent; pick from the table below by your data type and call the listed tools one by one. 跳过 agent，按数据类型查下表，逐个调用。

| 数据类型 Data type | 首选数据库 Databases | 直接调用工具 Direct tools | 预期产出 Expected output | 潜在洞察 Insights |
|---|---|---|---|---|
| 基因列表 Genes | HGNC · Ensembl · UniProt | `hgnc_gene_symbol` `ensembl_gene_lookup` `uniprot_annotate` | 标准符号/别名、位置、功能注释 | 基因家族、疾病关联线索 |
| 序列核酸 DNA/RNA | NCBI · ENA | `ncbi_fetch_sequence` `ena_sequence_search` `blast_search` | 序列、注释、同源比对 | 保守区、物种同源 |
| 蛋白质序列 Protein | UniProt · AlphaFold | `uniprot_annotate` `uniparc_search` `alphafold_structure` | 功能/结构域、预测结构 | 突变热点、结构功能域 |
| 变异/SNP Variants | dbSNP · MyVariant · ClinVar | `dbsnp_search` `variant_annotate` `clinvar_query` | 频率、致病性、临床注释 | 有害突变、人群分布 |
| 化合物/药物 Compound | PubChem · ChEBI · UniChem | `compound_info` `chebi_search` `unichem_mapping` (InChIKey) | 属性、本体、跨库 ID | 成药性、多库一致性 |
| 表达谱 Expression | Expression Atlas · GEO | `expression_atlas_experiment` `geo_dataset_search` | 相关实验、差异设计 | 组织特异表达 |
| 通路/互作 Pathways | KEGG · Reactome · STRING | `kegg_pathway_search` `reactome_pathway_search` `string_interactions` | 通路成员、互作网络 | 关键 hub、富集通路 |
| 蛋白质组 Proteomics | PRIDE | `pride_search` `pride_project` | 质谱项目、物种/疾病 | 疾病蛋白证据 |
| 微生物/质粒 Microbe/Plasmid | NCBI SRA · BioProject · nuccore | `sra_search` `bioproject_search` `plasmid_search` | 测序数据、质粒序列 | 菌株比较、载体选择 |
| 植物基因 Plant gene | Ensembl Plants | `plant_gene_lookup` `plant_species_list` | 植物基因/物种 | 作物研究 |
| 模式生物 Model organism | WormBase · FlyBase · RGD | `wormbase_gene` `flybase_gene` `rgd_gene_symbol` | 模式生物基因 | 同源疾病模型 |
| 文献 Literature | PubMed · Europe PMC · OpenAlex | `pubmed_search` `europepmc_search` `openalex_work_search` | 论文、引用 | 领域趋势、方法参考 |

## Honesty rules 诚实规则

- Prefer Path A first: it costs fewer tokens and picks the best fit. 优先路径 A，更省 token 且匹配更准。
- Before relying on a tool for a conclusion, confirm reachability with `db_health_check`; treat `tool_inventory` "best-effort" tools with care. 关键结论前先 `db_health_check` 确认可达性。
- If the agent is not available (no MCP), Path B is a valid alternative: the tools are the same, just called directly. 没有 agent 时路径 B 完全可用。
