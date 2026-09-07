---
name: bio-analysis
description: Multi-step bioinformatics analysis workflow using BioMCP — data type detection, tool recommendation, cross-database validation, and honest insight generation. Use when the user provides raw bio data (gene list, sequence, variant, compound, IDs) and wants analysis or insights.
---

# Bio-Analysis Workflow / 生物信息分析流程

This skill defines the standard analysis workflow for raw bioinformatics input. 本 skill 定义对原始生物数据输入的标准分析流程。

## Steps 步骤

### 1. Classify the input 分类输入
Call `intelligent_analyze(input, goal)` first. It detects the data type (gene_name, sequence, variant, compound, pathway, disease, lipid, glycan, etc.) and returns:
- `data_analysis.primary_type` — detected type with confidence
- `recommended_plans` — primary + backup plans with tool lists
- `expected_results` — what each tool will produce
- `insights` — non-obvious angles worth checking

Use the plan as the skeleton; do not call every tool blindly. 以推荐方案为骨架，不要盲目调用每个工具。

### 2. Execute the plan 执行方案
For a **gene**, the canonical chain is:
1. `uniprot_annotate` — basic info, function, subcellular location
2. `protein_domains` — domains / families (InterPro)
3. `ensembl_gene_lookup` — genomic coordinates, transcript
4. `gene_enrichment(genes)` — functional enrichment (needs ≥2 genes)
5. `string_interactions` — interaction partners
6. Optional: `gene_full_profile` for the one-stop cross-check

For a **variant**: `variant_annotate` (frequency, prediction, clinical), `dbsnp_search`, `clinvar_query`.
For a **compound**: `compound_info`, `chembl_drug_search`, `unichem_mapping`, `chebi_compound`.
For a **sequence**: `blast_search` (top hits), then follow the top hit's organism.

### 3. Cross-validate 交叉验证
- For critical claims, get the same fact from ≥2 independent databases (e.g. gene coordinates from Ensembl + HGNC; compound ID from PubChem + ChEBI + UniChem).
- If two sources disagree, report both and say which is more authoritative. 若两个来源不一致，如实报告并说明哪个更权威。

### 4. Generate insights 生成见解
Insights should be concrete and actionable, not generic. 见解要具体可操作，不要泛泛而谈。Examples of strong insights:
- Expression / tissue specificity (from `protein_tissue_expression`)
- Pathway crosstalk (Reactome + KEGG overlap)
- Disease associations via literature co-occurrence (PubMed/Europe PMC counts)
- Interaction network hubs (STRING degree)

### 5. Honest reporting 诚实汇报
- Quote numbers exactly as returned by the APIs; add the source database name. 引用 API 返回的确切数字，并注明数据源。
- Mark best-effort tools' results as unverified. 标出 best-effort 工具的未验证状态。
- If a database is unreachable, say so and suggest the alternative plan. 数据库不可达时如实说明并提供备选方案。
- Never invent a database entry, ID, citation count, or association. 绝不编造数据库条目、ID、引用数或关联。
