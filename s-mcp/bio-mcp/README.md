# BioMCP — 生物信息学 MCP 服务器 / Bioinformatics MCP Server

**BioMCP** is an open-source **MCP server** that connects any AI assistant directly to **43 open bioinformatics databases** — zero config, no API keys. Literature, sequences, BLAST, structures, enrichment, annotations, genomes, interactions, pathways, variants, population frequencies, methylation QTLs, tissue expression, drug targets, compounds, single-cell, glycomics, metabolomics, lipidomics, microbiome, plants, model organisms, proteomics and more.

BioMCP 是一个开源的 **MCP 服务器**，让任意 AI 助手**零配置直连 43 个公开生物数据库**——文献、序列、比对、结构、富集、注释、基因组、互作、通路、变异、人群频率、甲基化 QTL、表观遗传、组织表达、药物靶点、化合物、单细胞、糖组学、代谢组学、脂质组学、微生物组、植物、模式生物、蛋白质组学等全流程。

[![MCP](https://img.shields.io/badge/MCP-Server-7c5cff?style=flat-square)](https://modelcontextprotocol.io)
[![PyPI](https://img.shields.io/pypi/v/biomcp-server?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/biomcp-server/)
[![Tools](https://img.shields.io/badge/Tools-83-0ea5e9?style=flat-square)](https://github.com/qgeng1465/bio-mcp)
[![Databases](https://img.shields.io/badge/Databases-43-22c55e?style=flat-square)](https://github.com/qgeng1465/bio-mcp)
[![Python](https://img.shields.io/badge/Python-3.10%2B-2ea44f?style=flat-square)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Dual%20License-blue?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-win%20%7C%20mac%20%7C%20linux-lightgrey?style=flat-square)](https://github.com/qgeng1465/bio-mcp)

---

## 特性 / Features

**标准 MCP 协议** / Standard MCP protocol — Based on official MCP SDK with stdio transport, compatible with all MCP clients
基于官方 MCP SDK，stdio 传输，兼容所有 MCP 客户端

**83 个工具 · 43 个数据库** / 83 tools · 43 databases — Covers literature → sequences → structures → functions → interactions → pathways → variants → population frequency → methylation → tissue expression → drug targets → drugs → single-cell → glycomics → metabolomics → lipidomics → microbiome → plants → model organisms → proteomics → intelligent analysis
覆盖文献→序列→结构→功能→互作→通路→变异→人群频率→甲基化→组织表达→药物靶点→药物→单细胞→糖组学→代谢组学→脂质组学→微生物组→植物→模式生物→蛋白质组学→智能分析全流程

**零配置使用** / Zero-config — `pip install biomcp-server` one command, no database setup, no API keys required
`pip install biomcp-server` 一条命令，无需数据库、无需密钥

**数据公开权威** / Authoritative public data — All from official APIs: NCBI / RCSB / UniProt / Ensembl / EBI / STRING / KEGG / GlyGen / Reactome / OpenAlex, etc.
全部来自 NCBI / RCSB / UniProt / Ensembl / EBI / STRING / KEGG / GlyGen / Reactome / OpenAlex 等官方 API

**智能限速** / Smart rate-limiting — Built-in NCBI 3 seconds/request rate limiting with retry backoff, respects academic API standards
内置 NCBI 3 秒/请求限速与重试退避，遵守学术 API 规范

**跨库交叉验证** / Cross-database validation — `gene_full_profile` concurrently queries 4 databases, `intelligent_analyze` auto-detects data types and recommends optimal analysis plans
`gene_full_profile` 一次并发查询 4 个数据库，`intelligent_analyze` 自动检测数据类型并推荐最佳分析方案

**中英双语** / Bilingual — Tool descriptions and documentation in both languages, domestic network reachable (adapted Enrichr as g:Profiler alternative)
命令描述与文档双语，国内网络可达（已适配 Enrichr 替代 g:Profiler）

**智能 Agent 系统** / Intelligent Agent System — Auto-analyzes input data, recommends optimal tools, saves tokens, provides unexpected insights
自动分析输入数据，推荐最佳工具，节省 token，提供意外见解

**诚实 Agent** / Honest Agent — `db_health_check` runs real connectivity tests on all endpoints, `tool_inventory` reports which tools are end-to-end verified vs best-effort
`db_health_check` 对全部端点做真实连通性检查，`tool_inventory` 如实报告哪些工具已端到端验证、哪些为尽力而为，不做乐观假设

---

## 安装 / Install

```bash
# 1. 安装（需要 Python 3.10+）/ Install (Python 3.10+)
pip install biomcp-server

# 2. 启动（stdio 模式，供 MCP 客户端调用）/ Run in stdio mode
bio-mcp
```

### 手动安装（源码）/ Install from source

```bash
git clone https://github.com/qgeng1465/bio-mcp.git
cd bio-mcp
pip install .
# 或开发模式 / or dev mode
pip install -e ".[test]"
```

---

## 快速开始 / Quick Start

Register BioMCP in any MCP-compatible AI assistant / IDE (Cursor / VS Code / MCP clients, etc.):
在任何支持 MCP 的 AI 助手 / IDE 中注册 BioMCP（Cursor / VS Code / 各类 MCP 客户端等）：

```json
{
  "mcpServers": {
    "bio-mcp": {
      "command": "bio-mcp"
    }
  }
}
```

Then just ask in conversation:
然后在对话中直接使用：

```
查询 BRCA1 相关的最新文献 / 查 CRISPR 领域的高被引论文
下载 CYP2D6 的蛋白序列 / 检索大肠杆菌的核酸序列
对这段 DNA 做 BLAST：ATGC...
查 PDB 1CRN 的结构 / AlphaFold 预测 P04637 / EMDB 电镜结构 EMD-1234
分析基因列表 BRCA1,TP53,EGFR,ATM,RAD51 的富集
查 apoptosis 通路 / 查 TP53 的实验互作网络
查糖苷 G00051MO 的结构 / P04637 的糖基化 / 查脂质 LMFA01030001
检索肠道微生物组研究 / 检索大肠杆菌的基因组组装 / 查 pET-28a 质粒
查 BRCA1 在人体组织中的表达
查 rs1800562 的人群等位基因频率 / HFE 基因的 gnomAD 约束指标
查 rs6602381 的 mQTL 关联 / cg05575921 的表观遗传关联
查 TP53 在肝脏的 eQTL / 查 TP53 的药物靶点-疾病关联
查拟南芥基因 AT1G01010 / 查线虫基因 WBGene00000001
检索人血浆蛋白质组学项目 PXD000001 / 查 TP53 的 HGNC 基因符号
搜索乳腺癌的 SRA 测序数据 / 查 aspirin 在 UniChem 的 ID 映射
对 BRCA1 做一个多库综合分析报告
使用智能分析：TP53 基因的功能分析
获取基因研究的分析模板
检查当前哪些数据库可达（诚实检查）
```

---

## 工具 / Tools（83）

### 智能分析 / Intelligent Analysis
| 工具 | 功能 / Function | 说明 / Description |
|---|---|---|
| `intelligent_analyze` | 智能数据分析和工具推荐 / Intelligent data analysis and tool recommendation | 自动检测数据类型，推荐最佳分析方案，节省 token 使用 |
| `get_analysis_template` | 获取分析场景模板 / Get analysis scenario templates | 预构建的基因研究、药物发现等分析流程 |

### 文献 / Literature
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `pubmed_search` | PubMed 文献检索（标题/作者/期刊/PMID/DOI）/ literature search | NCBI E-utilities |
| `europepmc_search` | 全文文献检索（含 OA 全文）/ full-text + open-access | Europe PMC (EBI) |
| `openalex_work_search` | 全球学术著作检索（被引/作者/期刊）/ scholarly works search | OpenAlex |

### 序列与比对 / Sequence & Alignment
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `ncbi_fetch_sequence` | 下载核酸/蛋白序列（FASTA/GenBank）/ fetch sequences | NCBI E-utilities |
| `blast_search` | DNA/蛋白同源 BLAST，返回 top hits / homology search | NCBI BLAST |
| `taxonomy_lookup` | 物种分类查询（学名/谱系）/ species taxonomy | NCBI Taxonomy |
| `geo_dataset_search` | 基因表达数据集检索 / expression dataset search | NCBI GEO |
| `uniparc_search` | 蛋白序列归档检索（UPI/交叉引用）/ protein archive search | EBI UniParc |
| `uniparc_by_id` | UniParc 记录详情（序列/全部交叉引用）/ record by UPI ID | EBI UniParc |

### 结构 / Structure
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `pdb_structure_summary` | 实验结构查询（分辨率/方法/链序列）/ experimental structures | RCSB PDB |
| `alphafold_structure` | AI 预测结构（pLDDT 置信度）/ AI-predicted structures | AlphaFold DB (EBI) |
| `emdb_structure_lookup` | 冷冻电镜结构（标题/作者/分辨率/组分）/ cryo-EM structures | EBI EMDB |

### 蛋白功能 / Protein Function
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `uniprot_annotate` | 蛋白注释（名称/基因/功能/GO）/ protein annotations | UniProt |
| `protein_domains` | 蛋白结构域/家族/位点 / structural domains | InterPro (EBI) |

### 基因命名 / Gene Nomenclature
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `hgnc_search` | 基因符号/别名搜索 / gene symbol search | HGNC |
| `hgnc_gene_symbol` | 标准基因符号与别名查询 / canonical symbol & aliases | HGNC |

### 通路与互作 / Pathways & Interactions
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `gene_enrichment` | GO/KEGG/Reactome 富集分析 / enrichment analysis | Enrichr |
| `kegg_pathway_search` | KEGG 通路搜索 / pathway search | KEGG |
| `kegg_pathway_genes` | 通路包含的基因列表 / genes in a pathway | KEGG |
| `reactome_pathway_search` | 生物通路检索（信号转导/代谢/DNA修复）/ pathway search | Reactome |
| `string_interactions` | 蛋白互作网络（预测）/ protein interaction network | STRING-db |
| `intact_interactions` | 实验分子互作（检测方法/证据）/ experimental interactions | EBI IntAct |
| `ensembl_gene_lookup` | 基因定位（GRCh38 坐标）/ gene lookup | Ensembl |
| `ensembl_homologs` | 同源基因（直系/旁系）/ homologous genes | Ensembl Compara |
| `biogrid_interactions` | 蛋白互作（需 BIOGRID_ACCESS_KEY）/ interactions | BioGRID |
| `biogrid_gene_interactions` | 基因级互作检索（需 BIOGRID_ACCESS_KEY）/ gene interactions | BioGRID |

### 基因组与组装 / Genome & Assembly
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `ucsc_genome_info` | 基因组组装与注释轨道 / genome assemblies | UCSC Genome Browser |
| `genome_assembly_search` | 基因组组装检索（细菌/病毒/真核）/ genome assemblies | NCBI Assembly |

### 变异与临床 / Variants & Clinical
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `variant_annotate` | 变异注释（频率/功能预测/临床意义）/ variant annotation | MyVariant.info |
| `clinvar_query` | ClinVar 临床变异分类 / clinical variant classification | NCBI ClinVar |
| `dbsnp_search` | dbSNP 遗传变异检索（rsID/等位基因/临床意义）/ variant search | NCBI dbSNP |

### 基因本体与遗传关联 / GO & GWAS
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `go_term_lookup` | GO 术语详情（定义/方面/同义词）/ GO term details | QuickGO (EBI) |
| `go_term_search` | GO 术语关键词搜索 / GO term search | QuickGO (EBI) |
| `gene_go_annotation` | 基因 GO 功能注释（证据/PMID）/ GO annotations by gene | QuickGO (EBI) |
| `gwas_variant_associations` | 变异 GWAS 关联（性状/p值/效应）/ variant-trait associations | GWAS Catalog (EBI) |
| `gwas_gene_variants` | 基因关联的 GWAS 变异 / GWAS variants by gene | GWAS Catalog (EBI) |

### 人群频率与基因约束 / Population Frequency & Constraint
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `gnomad_variant_lookup` | gnomAD 人群等位基因频率（外显子组/全基因组、人群分层、faf95/faf99）/ allele frequency | gnomAD (Broad) |
| `gnomad_gene_constraint` | 基因约束指标（pLI / LOEUF）/ gene constraint metrics | gnomAD (Broad) |

### 甲基化 QTL 与表观遗传 / Methylation QTL & Epigenetics
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `mqtl_snp_lookup` | SNP→CpG mQTL 关联（β/p值/队列数）/ SNP-to-CpG mQTL | GoDMC |
| `mqtl_cpg_lookup` | CpG→SNP mQTL 关联 / CpG-to-SNP mQTL | GoDMC |
| `ewas_probe_lookup` | CpG 位点的 EWAS 关联（性状/研究/PMID）/ probe EWAS associations | EWAS Atlas (NGDC) |
| `ewas_gene_lookup` | 基因关联的 CpG 探针与 EWAS 性状 / gene→probe EWAS | EWAS Atlas (NGDC) |

### 组织表达与药物靶点 / Tissue Expression & Drug Targets
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `gtex_tissue_expression` | 基因在各组织的分位数标准化中位表达（TPM）/ tissue median expression | GTEx Portal |
| `gtex_eqtl` | 单组织 eQTL 关联（变异/p值/效应）/ single-tissue eQTL | GTEx Portal |
| `ot_target_info` | 药物靶点信息（符号/定位/同义词）/ drug target info | Open Targets |
| `ot_target_disease` | 靶点-疾病评分化关联（含新颖性）/ target-disease associations | Open Targets |

### 化合物与药物 / Compounds & Drugs
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `compound_info` | 化合物信息（SMILES/分子式/InChIKey）/ compound info | PubChem |
| `chembl_drug_search` | 药物活性与靶点（IC50/Ki）/ drug bioactivity & targets | ChEMBL (EBI) |
| `unichem_mapping` | 化合物 ID 跨库映射（按 InChIKey）/ ID mapping by InChIKey | UniChem (EBI) |
| `unichem_structure` | 化合物跨库引用详情（按 InChIKey）/ cross-refs by InChIKey | UniChem (EBI) |
| `chebi_compound` | ChEBI 化合物详情（本体/关系）/ compound details | ChEBI (EBI) |
| `chebi_search` | ChEBI 化合物全文搜索 / compound search | ChEBI (EBI) |

### 核酸与质粒 / Nucleic Acid & Plasmids
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `plasmid_search` | 质粒/载体序列检索（名称/宿主/长度）/ plasmid search | NCBI nuccore |
| `ena_sequence_search` | 欧洲核苷酸档案序列（微生物/病毒/质粒）/ nucleotide sequences | EBI ENA |

### 微生物组 / Microbiome
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `microbiome_study_search` | 微生物组宏基因组研究（宿主/栖息地）/ metagenomics studies | EBI MGnify |

### 单细胞 / Single-Cell
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `cellxgene_search` | 单细胞数据集检索（含类器官/肿瘤图谱）/ single-cell datasets | CELLxGENE (CZ) |

### 糖组学 / Glycomics
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `glycan_lookup` | 糖苷结构详情（组成/质量/IUPAC）/ glycan structure | GlyGen (GlyTouCan) |
| `protein_glycosylation` | 蛋白糖基化位点与糖修饰 / protein glycosylation | GlyGen |

### 代谢组学 / Metabolomics
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `metabolomics_study` | 代谢组学研究详情（技术/设计/因子）/ study details | EBI Metabolights |
| `metabolomics_latest` | 最新代谢组学研究列表 / latest studies | EBI Metabolights |

### 脂质组学 / Lipidomics
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `lipid_lookup` | 脂质结构查询（名称/分子式/SMILES/DB交叉引用）/ lipid structure | LIPID MAPS |

### 蛋白图谱 / Protein Atlas
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `protein_tissue_expression` | 蛋白组织表达与亚细胞定位 / tissue expression | Human Protein Atlas |

### 样本与表达 / Samples & Expression
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `biosample_by_id` | 生物样本详情（属性/来源）/ sample details | NCBI BioSamples |
| `biosample_search` | 生物样本检索 / sample search | NCBI BioSamples |
| `expression_atlas_gene` | 基因相关表达实验（诚实版）/ gene-related experiments | EBI Expression Atlas |
| `expression_atlas_experiment` | 表达实验检索（关键词/物种）/ experiment search | EBI Expression Atlas |

### 蛋白质组学 / Proteomics
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `pride_project` | 质谱项目详情（仪器/肽段/蛋白）/ project details | EBI PRIDE |
| `pride_search` | 蛋白质组学项目检索 / project search | EBI PRIDE |

### 模式生物 / Model Organisms
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `flybase_gene` | 果蝇基因详情（FBgn）/ fly gene details | FlyBase |
| `flybase_search` | 果蝇基因搜索 / fly gene search | FlyBase |
| `wormbase_gene` | 线虫基因详情（WBGene）/ worm gene details | WormBase |
| `wormbase_search` | 线虫基因搜索 / worm gene search | WormBase |
| `rgd_gene_symbol` | 大鼠基因标准符号与注释 / rat gene symbol | Rat Genome DB |
| `rgd_search` | 大鼠基因搜索 / rat gene search | Rat Genome DB |

### 植物 / Plants
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `plant_gene_lookup` | 植物基因查询（拟南芥/水稻/玉米等）/ plant gene lookup | Ensembl Plants |
| `plant_species_list` | 支持的植物物种列表 / supported plant species | Ensembl Plants |

### 测序档案 / Sequencing Archive
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `sra_search` | 测序数据检索（RNA-seq/WGS/ATAC-seq）/ sequence read archive | NCBI SRA |
| `bioproject_search` | 测序项目检索（样本/研究设计）/ BioProject search | NCBI BioProject |

### 诚实检查 / Honesty
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `db_health_check` | 真实连通性检查：逐库 HTTP 测试，如实报告可达/不可达 / real connectivity test | 全部数据库 |
| `tool_inventory` | 工具清单与验证状态（e2e_verified / best_effort）/ tool inventory & status | 全部工具 |

### 组合分析 / Combined
| 工具 | 功能 / Function | 数据源 / Source |
|---|---|---|
| `gene_full_profile` | **多库交叉验证**：一次并发查 Ensembl+UniProt+STRING+PubMed / combined report | 4 个数据库 |

---

## 示例输出 / Example Output

**智能分析**（Intelligent Analysis）
```
输入: "TP53"
分析目标: "function"

输出:
{
  "data_analysis": {
    "primary_type": "gene_name",
    "confidence": {"gene_name": 0.85}
  },
  "recommended_plans": [
    {
      "plan_id": "primary",
      "recommended_tools": [
        "uniprot_annotate",
        "protein_domains",
        "gene_enrichment",
        "string_interactions"
      ],
      "expected_results": [
        "蛋白基本信息",
        "结构域和家族",
        "GO富集分析",
        "蛋白互作网络"
      ],
      "token_efficiency": "high",
      "insights": [
        "建议检查基因的物种特异性",
        "考虑该基因在不同组织中的表达差异",
        "可以探索该基因在疾病状态下的异常表达"
      ]
    }
  ]
}
```

**gene_full_profile**（组合工具 / combined tool）
```
基因综合分析：TP53 (homo_sapiens)

- Ensembl ENSG00000141510 · chr17:7668402-7687550 · protein_coding · tumor protein p53
- UniProt P04637 · Cellular tumor antigen p53 · Homo sapiens · 393 aa · Multifunctional transcription factor...
- STRING 互作伙伴: MDM2(0.999), TP53BP1(0.996), EP300(0.986), ...
- PubMed 文献: 74,021 篇

综合来自 Ensembl / UniProt / STRING / PubMed 的交叉验证。
```

---

## 两种使用方式：智能 Agent 或直接调用 / Two Ways to Use: Agent or Direct

BioMCP 同时支持两种使用方式，可按需选择。 / Two usage modes are available:

**方式一：用智能 Agent 与 Skill（省 token）/ Mode 1 — Intelligent agent + skills (token-saving)**
- 直接提问 `intelligent_analyze(input, goal)`，由 agent 判断数据类型、推荐数据库、给出预期结果与洞察，并只调用必要的工具。
- 或使用仓库内置 Skill（bio-data-to-database / bio-analysis / bio-mcp-usage），自动走「分类 → 推荐 → 交叉验证 → 诚实报告」流程。
- 适合：不确定数据能做什么、想省 token、需要洞察的场景。

**方式二：单独调用任意工具（完全手动）/ Mode 2 — Call any tool directly (fully manual)**
- 不经过 agent，直接调用任意单个工具，如 `pubmed_search(term="BRCA1")`、`blast_search(...)`、`uniprot_annotate(gene="TP53")`。
- 适合：数据与目标明确、已有查询计划、不想引入 agent 判断的场景。
- 工具本身与 agent 用的是同一套：`tool_inventory` 可查看全部 83 个工具与验证状态，`db_health_check` 可确认当前网络可达性。

> 两种方式等价且互通：agent 最终也是调用这些工具；手动调用得到的结果完全相同。

---

## 架构 / Architecture

```
Client Layer / 客户端层
┌──────────────────────────────────────────────┐
│                 MCP Client                   │
│   (Any MCP-compatible AI assistant / IDE)     │
└──────────────────────┬───────────────────────┘
                       │  stdio (JSON-RPC 2.0)
Server Layer / 服务器层
┌──────────────────────▼───────────────────────┐
│              bio-mcp server                   │
│  ┌────────────────────────────────────────┐  │
│  │  tools/  (83 MCP tools / 83 工具)      │  │
│  │  intelligent · honesty · pubmed · ncbi │  │
│  │  blast · pdb · uniprot · enrichment ·  │  │
│  │  ensembl · string · kegg · variant ·   │  │
│  │  interpro · pubchem · chembl ·         │  │
│  │  europepmc · alphafold · cellxgene ·   │  │
│  │  ucsc · taxonomy · geo · glygen ·      │  │
│  │  uniparc · metabolights · proteinatlas │  │
│  │  assembly · dbsnp · plasmid · ena ·    │  │
│  │  mgnify · reactome · openalex · lipid  │  │
│  │  emdb · intact · crosscheck · hgnc ·   │  │
│  │  biogrid · biosamples · expression ·   │  │
│  │  unichem · chebi · pride · flybase ·   │  │
│  │  wormbase · rgd · plants · gnomad ·    │  │
│  │  godmc · ewas · gtex · opentargets     │  │
│  └────────────────────┬───────────────────┘  │
│  ┌────────────────────▼───────────────────┐  │
│  │  core/  (42 client modules · 43 DBs)     │  │
│  │  BioHTTP: retry/backoff/rate-limit/      │  │
│  │  LRUCache: thread-safe caching          │  │
│  └────────────────────┬───────────────────┘  │
└───────────────────────┼──────────────────────┘
Database Layer / 数据库层
        ┌───────┬───────┼───────┬───────┬────────────┐
     ┌──▼──┐ ┌──▼──┐ ┌──▼──┐ ┌──▼──┐ ┌──▼──┐ ┌─────▼─────┐
     │NCBI │ │RCSB │ │Uni  │ │Ens  │ │STRING│ │Enrichr   │
     │     │ │PDB  │ │Prot │ │embl │ │     │ │... 共43库 │
     └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └───────────┘
```

### 为什么用 Enrichr 而不是 g:Profiler？

g:Profiler（爱沙尼亚）在国内网络下常不可达；Enrichr（Ma'ayan Lab）国内可达且提供 GO/KEGG/Reactome/WikiPathways 等数百个基因集库。BioMCP 默认采用 Enrichr，保证开箱即用。

### 为什么 OpenGWAS / DisGeNET 被排除？

OpenGWAS 从 2024-05 起强制要求 API token；DisGeNET 也需 API key，均无法零配置直连，故不包含。收录的数据库中，除 BioGRID 需要 `BIOGRID_ACCESS_KEY` 环境变量外，其余 42 个均为开放免密钥 API。BioGRID 之所以保留，是因为其注册即可免费获得 key，且互作数据对蛋白网络分析价值高。

---

## 目录结构 / Project Structure

```
bio-mcp/
├── src/bio_mcp/
│   ├── server.py            # MCP server 入口（装配 83 个工具）
│   ├── core/                # 42 个客户端模块覆盖 43 库
│   │   ├── http.py          #   BioHTTP：重试/退避/限速/超时
│   │   ├── cache.py         #   LRUCache：线程安全缓存层
│   │   ├── ncbi.py          #   NCBI E-utilities + BLAST + Assembly + dbSNP + SRA/BioProject/BioSamples
│   │   ├── rcsb.py          #   RCSB PDB
│   │   ├── uniprot.py       #   UniProt REST
│   │   ├── enrichr.py       #   Enrichr 富集
│   │   ├── ensembl.py       #   Ensembl 基因/同源/植物
│   │   ├── stringdb.py      #   STRING 互作
│   │   ├── kegg.py          #   KEGG 通路
│   │   ├── myvariant.py     #   MyVariant 变异
│   │   ├── interpro.py      #   InterPro 结构域
│   │   ├── pubchem.py       #   PubChem 化合物
│   │   ├── europepmc.py     #   Europe PMC 文献
│   │   ├── alphafold.py     #   AlphaFold 结构
│   │   ├── chembl.py        #   ChEMBL 药物
│   │   ├── cellxgene.py     #   CELLxGENE 单细胞
│   │   ├── ucsc.py          #   UCSC 基因组
│   │   ├── glygen.py        #   GlyGen 糖组学
│   │   ├── uniparc.py       #   UniParc 蛋白序列归档
│   │   ├── metabolights.py  #   Metabolights 代谢组学
│   │   ├── proteinatlas.py  #   Human Protein Atlas
│   │   ├── ena.py           #   EBI ENA 核酸档案
│   │   ├── mgnify.py        #   EBI MGnify 微生物组
│   │   ├── reactome.py      #   Reactome 通路
│   │   ├── openalex.py      #   OpenAlex 文献
│   │   ├── lipidmaps.py     #   LIPID MAPS 脂质
│   │   ├── emdb.py          #   EBI EMDB 电镜结构
│   │   ├── intact.py        #   EBI IntAct 实验互作
│   │   ├── hgnc.py          #   HGNC 基因命名
│   │   ├── biogrid.py       #   BioGRID 互作（需 key）
│   │   ├── expressionatlas.py # EBI Expression Atlas
│   │   ├── unichem.py       #   UniChem 化合物 ID 映射
│   │   ├── chebi.py         #   ChEBI 化合物本体
│   │   ├── pride.py         #   EBI PRIDE 蛋白质组学
│   │   ├── flybase.py       #   FlyBase 果蝇
│   │   ├── wormbase.py      #   WormBase 线虫
│   │   ├── rgd.py           #   Rat Genome DB 大鼠
│   │   ├── gnomad.py        #   gnomAD 人群频率/基因约束
│   │   ├── godmc.py         #   GoDMC mQTL
│   │   ├── ewas.py          #   EWAS Atlas 表观遗传
│   │   ├── gtex.py          #   GTEx 组织表达/eQTL
│   │   └── opentargets.py   #   Open Targets 药物靶点
│   └── tools/               # 83 个 MCP 工具定义
│       ├── intelligence.py  #   智能分析系统
│       ├── honesty.py       #   诚实 agent（连通性检查/工具清单）
│       ├── plants.py        #   植物基因工具
│       ├── pubmed.py · ncbi.py · blast.py · pdb.py
│       ├── uniprot.py · enrichment.py · ensembl.py
│       ├── stringdb.py · kegg.py · variant.py
│       ├── interpro.py · pubchem.py · europepmc.py
│       ├── alphafold.py · chembl.py · cellxgene.py
│       ├── ucsc.py · ncbi_extra.py · glygen.py
│       ├── uniparc.py · metabolights.py · proteinatlas.py
│       ├── ena.py · mgnify.py · reactome.py · openalex.py
│       ├── lipidmaps.py · emdb.py · intact.py · crosscheck.py
│       ├── hgnc.py · biogrid.py · biosamples.py
│       ├── expressionatlas.py · unichem.py · chebi.py
│       ├── pride.py · flybase.py · wormbase.py · rgd.py
│       ├── gnomad.py · godmc.py · ewas.py · gtex.py
│       └── opentargets.py
├── tests/                   # 单元测试（不依赖网络）
├── examples/                # 客户端配置与快速开始
├── .github/workflows/       # CI（GitHub Actions）
└── pyproject.toml
```

---

## 测试 / Testing

```bash
# 单元测试（离线，不依赖网络）/ offline unit tests
python -m pytest tests/ -v
```

**诚实声明 / Honest note on verification status：**

- 原有 40 个工具（v0.1-0.4）在开发期对真实公开数据库做过端到端验证。
- v0.5 新增的 28 个工具中，大部分（HGNC、BioSamples、UniChem、ChEBI、PRIDE、WormBase、植物、SRA/BioProject、Expression Atlas 实验检索、智能分析与诚实检查）已在开发期用真实数据端到端验证。
- v0.6 新增的 5 个工具（QuickGO 3 个、GWAS Catalog 2 个）已对真实 API 端到端验证。
- v0.7 新增的 10 个工具（gnomAD 2、GoDMC 2、EWAS 2、Open Targets 2 已对真实 API 端到端验证；GTEx 2 已按 OpenAPI 实现并做结构校验，当前网络下 gtexportal 端点偶发 502/SSL 中断，连通性以 `db_health_check` 实时结果为准）。
- 受限工具如实披露：FlyBase 被 CloudFront WAF 机器人检测拦截（脚本客户端无法访问）；Rat Genome DB 在当前网络下超时；WormBase 搜索为尽力而为；BioGRID 需 API key。
- Expression Atlas 的 `expression_atlas_gene` 为诚实版：公开 REST 已不提供单基因数值表达量端点，该工具返回匹配该基因的实验列表供进一步查看。
- 如需确认当前环境下某数据库是否可达，先调用 `db_health_check`；对关键结论请结合专业工具与原始数据复核。

> The original 40 tools (v0.1-0.4) were end-to-end validated during development. Most of the 28 tools added in v0.5 were validated against real data during development. The 5 tools added in v0.6 (QuickGO ×3, GWAS Catalog ×2) were e2e-validated against live APIs. The 10 tools added in v0.7 (gnomAD ×2, GoDMC ×2, EWAS ×2, Open Targets ×2) were e2e-validated against live APIs; GTEx ×2 were implemented per OpenAPI with structural checks — the gtexportal endpoints intermittently return 502/SSL errors from some networks, so verify with `db_health_check`. Restricted tools are disclosed honestly: FlyBase is blocked by CloudFront WAF bot detection; Rat Genome DB timed out in the current network; WormBase search is best-effort; BioGRID needs an API key. `expression_atlas_gene` is an honest version — the public REST no longer exposes numeric per-gene expression values, so it returns matching experiments instead. Run `db_health_check` to confirm endpoint reachability before relying on a specific database.

---

## License

BioMCP uses a **dual licensing model** / BioMCP 采用**双重授权模式**：

- **Academic Use / 学术使用**：MIT License for educational, research, and personal non-commercial use
  教育、研究和个人非商业使用采用 MIT 许可

- **Commercial Use / 商业使用**：Requires separate commercial license for business integration, revenue generation, or SaaS deployment
  业务集成、创收或 SaaS 部署需要单独的商业许可

For commercial licensing inquiries / 商业许可咨询：https://github.com/qgeng1465

---

## Roadmap / 路线图

- 批量对比分析（多条序列/多基因批量富集）/ Batch comparative analysis
- 虚拟细胞 / 类器官数据接口（多组学整合）/ Virtual cell & organoid data interfaces
- 更多数据库支持（MGI/ZFIN/Xenbase 等模式生物、更多植物基因组）/ More database support
- 高级智能分析功能（多agent协同）/ Advanced intelligent analysis (multi-agent collaboration)
- P1/P2 候选数据库：EVA 变异档案、cBioPortal 癌症基因组、GDC 癌症数据、BioMart、SIGNOR 信号网络、SGD 酵母、BioStudies、CTD 比较毒理基因组学、WikiPathways、Complex Portal、HCA 人类细胞图谱、MGI/AllianceMine（免 key 端点优先接入）/ Candidate databases: EVA, cBioPortal, GDC, BioMart, SIGNOR, SGD, BioStudies, CTD, WikiPathways, Complex Portal, HCA, MGI/AllianceMine
- HTTP/2 + 响应缓存 + 并发请求优化，缩短多库交叉验证的等待时间 / HTTP/2, response caching, concurrent requests to speed up cross-database validation

---

## Disclaimer / 免责声明

本工具**仅用于学习研究及个人合理使用** / For educational research and personal reasonable use only.

- 查询结果来自公开数据库原始数据，不保证完全准确，请结合专业工具与原始数据复核。
  Query results come from public database raw data and are not guaranteed to be completely accurate; please verify with professional tools and original data.

- 请遵守各数据库使用条款（NCBI 要求 ≥3 秒/请求并提供联系方式，本项目已内置）。
  Please comply with database usage terms (NCBI requires ≥3 seconds/request with contact info, already built-in).

- 涉及临床/药物/医疗决策时，请咨询专业人士。使用本工具产生的任何风险与法律责任由使用者自行承担。
  For clinical/drug/medical decisions, please consult professionals. Users assume all risks and liabilities.

---

## Support / 支持

If BioMCP helps you, consider supporting the project to keep it updated.

如果 BioMCP 帮到了你，欢迎支持项目，让我有动力持续更新。

<img src="assets/donate.png" alt="赞赏码 / Donation QR" width="200">

---

## Citation / 引用

If you use BioMCP in your research or publication, please cite:
如果您在研究或出版物中使用了 BioMCP，请引用：

```bibtex
@software{bio_mcp_2026,
  title={BioMCP: A Zero-Config MCP Server for Bioinformatics Databases},
  author={qgeng1465},
  year={2026},
  url={https://github.com/qgeng1465/bio-mcp}
}
```

---

License © 2026 qgeng1465