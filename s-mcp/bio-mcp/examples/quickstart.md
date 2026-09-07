# BioMCP 快速入门指南 / Quick Start Guide

## 安装 / Installation

```bash
pip install biomcp-server
```

## 配置 MCP 客户端 / Configure MCP Client

### 方法 1：Cursor / VS Code

1. 打开设置 / Open Settings
2. 搜索 "MCP Servers" / Search "MCP Servers"
3. 添加以下配置 / Add following config:

```json
{
  "mcpServers": {
    "bio-mcp": {
      "command": "bio-mcp"
    }
  }
}
```

### 方法 2：其他支持 MCP 的客户端 / Other MCP-enabled clients

在任一生成式 AI 桌面客户端的 MCP 配置中加入同一份 JSON 即可，配置项相同。其他支持 MCP 的客户端与 Cursor / VS Code 用法一致。

## 使用示例 / Usage Examples

在支持 MCP 的 AI 助手中直接使用 / Use directly in MCP-enabled AI assistants:

### 文献查询 / Literature Search
```
查一下 BRCA1 相关的最新文献
搜索 CRISPR 技术的高被引论文
```

### 基因分析 / Gene Analysis
```
TP53 基因的功能是什么
分析 BRCA1,TP53,EGFR 基因的富集
```

### 蛋白质研究 / Protein Research
```
获取 P04637 蛋白的详细信息
查一下 TP53 的蛋白互作网络
```

### 化合物和药物 / Compounds and Drugs
```
查询 imatinib 的药物活性
阿司匹林的化学结构是什么
```

### 智能分析 / Intelligent Analysis
```
帮我分析一下这个基因：EGFR
智能推荐这个化合物的分析方案：ATP
```

## 支持的数据库 / Supported Databases (43)

**文献 / Literature:** PubMed, Europe PMC, OpenAlex
**序列 / Sequences:** NCBI, BLAST, ENA, UniParc, GEO
**结构 / Structures:** PDB, AlphaFold, EMDB
**功能 / Function:** UniProt, InterPro domains
**基因组 / Genomes:** Ensembl, UCSC, NCBI Assembly
**互作 / Interactions:** STRING, IntAct, BioGRID
**通路 / Pathways:** KEGG, Reactome
**变异 / Variants:** MyVariant, ClinVar, dbSNP, gnomAD（人群频率/基因约束）
**甲基化 / Methylation:** GoDMC mQTL, EWAS Atlas
**组织表达 / Tissue Expression:** GTEx, Human Protein Atlas, Expression Atlas
**药物靶点 / Drug Targets:** Open Targets
**化合物 / Compounds:** PubChem, ChEMBL, UniChem, ChEBI
**单细胞 / Single-cell:** CELLxGENE
**微生物组 / Microbiome:** MGnify
**糖组学 / Glycomics:** GlyGen
**代谢组学 / Metabolomics:** Metabolights
**脂质组学 / Lipidomics:** LIPID MAPS
**蛋白质组学 / Proteomics:** PRIDE
**基因命名 / Gene Nomenclature:** HGNC
**蛋白图谱 / Protein Atlas:** Human Protein Atlas
**质粒 / Plasmids:** NCBI nuccore
**生物样本 / Biosamples:** NCBI BioSamples
**模式生物 / Model Organisms:** FlyBase, WormBase, RGD
**植物 / Plants:** Ensembl Plants (拟南芥/水稻/玉米等)
**测序档案 / Sequencing Archive:** NCBI SRA, BioProject

## 工具总数 / Total Tools: 83（含智能分析与诚实检查）

## 获取帮助 / Get Help

- GitHub: https://github.com/qgeng1465/bio-mcp
- 报告问题 / Report issues: GitHub Issues
- 赞助支持 / Donation: 见 README / See README

## 注意事项 / Notes

- NCBI 有限速 (3秒/请求) / NCBI rate limit (3 sec/request)
- 结果请结合专业工具复核 / Verify with professional tools
- 仅用于学习研究 / For educational research only