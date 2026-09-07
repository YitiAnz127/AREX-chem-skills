# Changelog

All notable changes to **BioMCP** are documented here. 记录 BioMCP 的版本变更。

## [0.7.0] - 2026-09-01

### Added 新增
- **gnomAD 人群频率与基因约束 / Population frequency & constraint（Broad）**:
  - `gnomad_variant_lookup` - 按 rsID / chr-pos-ref-alt 查询人群等位基因频率（外显子组/全基因组、人群分层、纯合计数、faf95/faf99）/ population allele frequency with ancestry breakdown
  - `gnomad_gene_constraint` - 按基因符号查询 pLI / LOEUF 等约束指标 / gene constraint metrics
- **GoDMC mQTL / 甲基化 QTL（Genetics of DNA Methylation Consortium）**:
  - `mqtl_snp_lookup` - SNP→CpG mQTL 关联（β/p 值/样本量/队列数）/ SNP-to-CpG mQTL
  - `mqtl_cpg_lookup` - CpG→SNP mQTL 关联 / CpG-to-SNP mQTL
- **EWAS Atlas 表观遗传 / Epigenome-wide association（NGDC/CNCB）**:
  - `ewas_probe_lookup` - 按 CpG 位点查询 EWAS 关联（性状/研究/PMID）/ probe EWAS associations
  - `ewas_gene_lookup` - 按基因符号查询关联的 CpG 探针 / gene→probe EWAS
- **Open Targets 药物靶点 / Drug targets（EMBL-EBI 等）**:
  - `ot_target_info` - 按 Ensembl ID 查询靶点信息（符号/全名/定位/同义词）/ drug target info
  - `ot_target_disease` - 靶点-疾病评分化关联（含新颖性）/ target-disease associations
- **GTEx Portal 组织表达与 eQTL / Tissue expression & eQTL**:
  - `gtex_tissue_expression` - 基因各组织中位表达（TPM，接受基因符号自动解析）/ tissue median expression
  - `gtex_eqtl` - 单组织 eQTL 关联（变异/p 值/效应）/ single-tissue eQTL
- **数据库 38 → 43，工具 73 → 83** / databases 38→43, tools 73→83
- 一致性保障测试：每个注册工具必须出现在 tool_inventory 与智能推荐映射中，防止新增库不被 agent 推荐 / consistency tests: every registered tool must appear in tool_inventory and the intelligent-agent mapping

### Changed 变更
- **智能推荐升级**：新增 METHYLATION 数据类型（CpG 位点自动路由到 mQTL/EWAS 工具）；10 个新工具与 20+ 既有工具进入 TOOL_MAPPING / intelligent agent: new METHYLATION data type + new tool recommendations
- **db_health_check 并发化**：43 个端点线程池并发检查，耗时从串行数十秒降至数秒 / db_health_check now runs concurrently (thread pool)
- **BioHTTP 增强**：修复 max_retries 硬编码 bug、补 408/501/505-511 重试码、退避加 jitter、请求头透传 / BioHTTP: max_retries fix, extra retry codes, jittered backoff, header passthrough
- **core/__init__.py** 补齐 11 个既有客户端导出，另加 5 个新客户端 / core exports completed
- 工具总数常量与说明文档全量同步至 83/43

### Notes 备注
- gnomAD 官方限速 10 QPM，客户端内置节流（6.5s/请求）/ gnomAD rate limit (10 QPM) throttled internally
- GTEx 端点按官方 OpenAPI 实现；部分网络下 gtexportal 偶发 502/SSL 中断，连通性以 `db_health_check` 实时结果为准 / GTEx endpoints implemented per OpenAPI; intermittent 502/SSL from some networks, verify with `db_health_check`
- 4 个新库（gnomAD/GoDMC/EWAS/Open Targets）已对真实 API 端到端验证 / 4 new databases e2e-verified against live APIs

## [0.6.0] - 2026-08-28

### Added 新增
- **QuickGO 基因本体 / Gene Ontology（EBI）**:
  - `go_term_lookup` - 按 GO ID 查询本体术语详情（名称/定义/方面/同义词）/ GO term details by ID
  - `go_term_search` - 按关键词搜索 GO 术语 / GO term keyword search
  - `gene_go_annotation` - 按基因产品 ID 查询 GO 注释（GO ID/方面/证据/PMID）/ GO annotations by gene product
- **GWAS Catalog 遗传关联 / Genome-wide association（EBI）**:
  - `gwas_variant_associations` - 按 rsID 查询变异的 GWAS 关联（性状/p 值/风险频率/效应量）/ variant-trait associations by rsID
  - `gwas_gene_variants` - 按基因查询关联的 GWAS 变异 / GWAS variants by gene
- **数据库 36 → 38，工具 68 → 73** / databases 36→38, tools 68→73
- 全部 5 个新工具已对真实 API 端到端验证 / all 5 new tools e2e-verified against live APIs
- 基因本体与遗传关联覆盖 / new "GO & GWAS" category in tool table

### Changed 变更
- 工具表新增「基因本体与遗传关联 / GO & GWAS」分类

## [0.5.0] - 2026-08-25

### Added 新增
- **智能 Agent 系统 / Intelligent Agent System**:
  - `intelligent_analyze` - 自动数据类型检测和工具推荐 / automated data type detection and tool recommendation
  - `get_analysis_template` - 预构建分析场景模板 / pre-built analysis scenario templates
  - Token 优化 / token optimization: 根据数据类型智能推荐最相关工具，节省 API 调用
  - 多方案支持 / multiple plans: 主方案 + 备选方案，提供意外见解
- **诚实 Agent / Honest Agent**:
  - `db_health_check` - 对全部数据库端点做真实 HTTP 连通性测试 / real connectivity tests
  - `tool_inventory` - 工具清单与验证状态（e2e_verified / best_effort）/ tool inventory & verification status
- **10 个新数据库客户端 / 10 new database clients**:
  - **HGNC** 基因命名 / gene nomenclature: `hgnc_search`、`hgnc_gene_symbol`
  - **BioGRID** 蛋白互作 / interactions: `biogrid_interactions`、`biogrid_gene_interactions`（需 `BIOGRID_ACCESS_KEY`）
  - **NCBI BioSamples** 生物样本 / samples: `biosample_by_id`、`biosample_search`
  - **EBI Expression Atlas** 基因表达 / expression: `expression_atlas_gene`、`expression_atlas_experiment`
  - **UniChem** 化合物 ID 映射 / ID mapping: `unichem_mapping`、`unichem_structure`
  - **ChEBI** 化合物本体 / compound ontology: `chebi_compound`、`chebi_search`
  - **EBI PRIDE** 蛋白质组学 / proteomics: `pride_project`、`pride_search`
  - **FlyBase** 果蝇 / fruit fly: `flybase_gene`、`flybase_search`
  - **WormBase** 线虫 / nematode: `wormbase_gene`、`wormbase_search`
  - **Rat Genome DB** 大鼠 / rat: `rgd_gene_symbol`、`rgd_search`
- **植物数据库 / Plants**（复用 Ensembl REST，覆盖拟南芥/水稻/玉米等）: `plant_gene_lookup`、`plant_species_list`
- **NCBI 测序档案扩展 / NCBI sequencing archive**: `sra_search`（SRA 测序数据）、`bioproject_search`（BioProject 测序项目）
- **数据库 26 → 36，工具 40 → 68** / databases 26→36, tools 40→68

### Changed 变更
- README 更新: 去除 emoji、去 AI 感、全中英双语、无 AI 工具署名 / removed emojis, AI tone, full bilingual, no AI tool attribution
- README 工具表扩充至 68 工具 / tool table expanded to 68 tools
- License: MIT → Dual License (academic MIT + commercial authorization required)
- BioGRID 客户端诚实化: 不再伪造 key，明确要求 `BIOGRID_ACCESS_KEY` / honest key requirement instead of a fake key
- 诚实声明: v0.5 大部分新工具已端到端验证，受限工具如实披露（FlyBase WAF / RGD 超时 / WormBase 尽力而为）/ most new tools e2e verified, restricted ones disclosed
- 单元测试 `EXPECTED_TOOLS` 扩充至 68，全部通过 / unit test covers all 68 tools
- 端点修复 / endpoint fixes (verified against real APIs):
  - ChEBI: `compound_by_id` 改用 EBI Search `chebi/entry/{id}`（旧 CHEBI_ID 字段查询无效）
  - PRIDE: `project_search` 改用 `projects?q={keyword}` 列表端点（该 API 无独立 search 端点）
  - Expression Atlas: 单基因数值表达端点已下线，诚实重构为客户端过滤实验列表，`gene_expression` 返回相关实验
- 新增内置 Skill 4 个: bio-data-to-database（数据→数据库匹配，agent/直连双路径）、bio-analysis、bio-mcp-usage、bio-release
- README 新增「两种使用方式」节：智能 Agent 或单独调用任意工具 / README documents both agent-driven and direct tool-call modes

### Honest note 诚实说明
- 原有 40 个工具（v0.1-0.4）在开发期做过端到端验证。
- v0.5 新增的 28 个工具中，大部分（HGNC、BioSamples、UniChem、ChEBI、PRIDE、WormBase、植物、SRA/BioProject、Expression Atlas 实验检索、智能分析、诚实检查）已用真实数据端到端验证。
- 受限工具如实披露：FlyBase 被 CloudFront WAF 机器人检测拦截（脚本客户端暂无法访问）；Rat Genome DB 在当前网络下超时；WormBase 搜索为尽力而为；BioGRID 需免费注册 key。
- Expression Atlas 的 `expression_atlas_gene` 为诚实版：公开 REST 已不提供单基因数值表达量端点，该工具返回匹配该基因的表达实验列表供进一步查看。

## [0.4.0] - 2026-08-11

### Added 新增
- **7 个新数据库 / 7 new databases**（全部零配置直连 / all zero-config direct access）:
  - **EBI ENA** 欧洲核苷酸档案 / nucleotide archive: `ena_sequence_search` 核酸序列（微生物/病毒/质粒，tax_tree 语法）
  - **EBI MGnify** 微生物组 / microbiome: `microbiome_study_search` 宏基因组研究（细菌/古菌/病毒）
  - **Reactome** 生物通路 / pathways: `reactome_pathway_search`（信号转导/代谢/DNA 修复）
  - **OpenAlex** 学术文献 / scholarly works: `openalex_work_search`（被引/作者/期刊）
  - **LIPID MAPS** 脂质组学 / lipidomics: `lipid_lookup`（名称/分子式/SMILES/DB 交叉引用）
  - **EBI EMDB** 冷冻电镜结构 / cryo-EM: `emdb_structure_lookup`（标题/作者/分辨率/组分）
  - **EBI IntAct** 实验分子互作 / experimental interactions: `intact_interactions`（检测方法/MI-score/文献）
- **数据库 19 → 26，工具 33 → 40** / databases 19→26, tools 33→40
- 全部 7 个新工具均以真实数据端到端验证（40/40 通过）/ all 7 new tools E2E validated with real data

### Changed 变更
- README 工具表新增 文献（OpenAlex）/ 核酸与质粒（ENA）/ 微生物组 / 脂质组学 分类，通路与互作分类补充 Reactome、IntAct
- 架构图与目录结构更新至 26 客户端 / 40 工具

### Note 说明
- 本轮所有新数据库均位于 EBI / Reactome / OpenAlex / LIPID MAPS 等免密钥服务；NCBI 在开发期网络不可达，其既有工具保持 v0.3 已验证状态，NCBI 新扩展（Gene/Protein/SRA）顺延至下一版本

## [0.3.0] - 2026-08-11

### Added 新增
- **4 个新数据库 / 4 new databases**（全部零配置直连 / all zero-config direct access）:
  - **GlyGen** 糖组学 / glycomics: `glycan_lookup` 糖苷结构（组成/质量/IUPAC）、`protein_glycosylation` 蛋白糖基化位点
  - **EBI UniParc** 蛋白序列归档 / protein archive: `uniparc_search`、`uniparc_by_id`（UPI/交叉引用/序列）
  - **EBI Metabolights** 代谢组学 / metabolomics: `metabolomics_study` 研究详情（技术/设计/因子）、`metabolomics_latest` 最新研究
  - **Human Protein Atlas** 蛋白组织图谱 / tissue atlas: `protein_tissue_expression`（组织表达/亚细胞定位）
- **NCBI 新检索能力 / new NCBI search capabilities**:
  - `genome_assembly_search` 基因组组装（微生物/细菌/病毒/真核）/ genome assemblies
  - `dbsnp_search` 遗传变异（rsID/等位基因/临床意义）/ dbSNP variants
  - `plasmid_search` 质粒/载体序列 / plasmid sequences
- **数据库 15 → 19，工具 23 → 33** / databases 15→19, tools 23→33

### Changed 变更
- README 工具表新增 糖组学 / 代谢组学 / 核酸与质粒 / 蛋白图谱 分类
- NCBI 客户端扩展 Assembly / dbSNP / nuccore 三个 esearch 系列方法

### Removed 移除
- DisGeNET（需要 API key，无法零配置直连）/ requires API key

## [0.2.0] - 2026-08-11

### Added 新增
- **8 个新数据库 / 8 new databases**（全部零配置直连 / all zero-config direct access）:
  - EuropePMC 全文文献检索 / full-text literature (`europepmc_search`)
  - AlphaFold DB AI 蛋白结构预测 / AI-predicted protein structures (`alphafold_structure`)
  - ChEMBL 药物活性 / drug bioactivity (`chembl_drug_search`)
  - CELLxGENE 单细胞数据 / single-cell datasets (`cellxgene_search`)
  - UCSC 基因组浏览器 / genome browser (`ucsc_genome_info`)
  - NCBI Taxonomy 物种分类 / species taxonomy (`taxonomy_lookup`)
  - NCBI GEO 基因表达数据集 / expression datasets (`geo_dataset_search`)
- **组合工具 / combined tool**: `gene_full_profile` 多库并发交叉验证 / concurrent multi-DB cross-validation (Ensembl + UniProt + STRING + PubMed)
- **架构 / architecture**: 线程安全 LRU 缓存层 / thread-safe LRU cache layer（`core/cache.py`）
- **项目成熟化 / project maturity**: 双语描述（中英）、`py.typed`、GitHub Actions CI、CHANGELOG

### Changed 变更
- 数据库数量 6 → 15，工具数量 6 → 23 / databases 6→15, tools 6→23
- Enrichr 替换 g:Profiler（大陆直连更稳）/ Enrichr engine (reliable from CN networks)
- KEGG 通路基因解析改用 `get` 端点（修复 400）/ KEGG parsing via `get` endpoint
- Ensembl 同源查询改用 `homology/symbol` 端点 / Ensembl homologs via symbol endpoint

### Removed 移除
- OpenGWAS（2024-05 起强制 API token，无法直连）/ requires token since 2024-05
- SGD（官网 API 已废弃返回 HTML）/ deprecated API

## [0.1.0] - 2026-08-10

### Added 新增
- 首个版本 / initial release：6 工具 / 6 tools
  - PubMed 文献 / `pubmed_search`
  - NCBI 序列 / `ncbi_fetch_sequence`
  - BLAST 同源比对 / `blast_search`
  - PDB 结构 / `pdb_structure_summary`
  - GO/KEGG 富集 / `gene_enrichment`
  - UniProt 注释 / `uniprot_annotate`
- MIT License、双语 README、捐赠二维码 / MIT license, bilingual README, donation QR
