"""智能数据推荐agent系统 - Intelligent Data Recommendation Agent System

这个系统通过分析用户的原始数据，智能推荐最适合的数据库和分析方案，
目的是节省token使用，并提供用户可能没想到的insights。
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import re
import json

# 未显式传入工具总数时的回退值。生产路径（intelligent_analyze 工具）在注册时
# 通过 server.list_tools() 取真实总数；此常量仅作为直接 API 调用的安全回退，
# 发布时与 EXPECTED_TOOLS 保持一致。
DEFAULT_TOTAL_TOOLS = 83

# 组合/工具性工具：不参与数据类型映射推荐（agent/honesty/组合/参考查询）。
# 一致性测试保证：每个注册工具要么在 TOOL_MAPPING，要么在此清单中。
UTILITY_TOOLS = frozenset({
    "intelligent_analyze", "get_analysis_template",  # 智能 agent
    "db_health_check", "tool_inventory",  # 诚实 agent
    "crosscheck", "gene_full_profile",  # 组合工具
    "go_term_lookup", "go_term_search",  # 本体参考查询
    "ucsc_genome_info",  # 基因组浏览器信息查询
})


class DataType(Enum):
    """支持的数据类型"""
    GENE_NAME = "gene_name"  # 基因名称 (BRCA1, TP53)
    GENE_ID = "gene_id"  # 基因ID (ENSG00000141510, P04637)
    PROTEIN_NAME = "protein_name"  # 蛋白质名称
    PROTEIN_ID = "protein_id"  # 蛋白质ID
    SEQUENCE = "sequence"  # 序列数据 (DNA/Protein)
    VARIANT = "variant"  # 变异数据 (chr13:g.32911145G>A)
    METHYLATION = "methylation"  # 甲基化位点 (cg05575921, mQTL/EWAS)
    COMPOUND = "compound"  # 化合物 (药物名称)
    PATHWAY = "pathway"  # 通路名称
    DISEASE = "disease"  # 疾病名称
    LITERATURE_QUERY = "literature_query"  # 文献查询
    STRUCTURE_ID = "structure_id"  # 结构ID (PDB, EMDB)
    MICROBIOME = "microbiome"  # 微生物组相关
    SINGLE_CELL = "single_cell"  # 单细胞数据
    GLYCANS = "glycans"  # 糖组学
    METABOLOMICS = "metabolomics"  # 代谢组学
    LIPIDOMICS = "lipidomics"  # 脂质组学
    PROTEOMICS = "proteomics"  # 蛋白质组学
    MODEL_ORGANISM = "model_organism"  # 模式生物
    PLASMID = "plasmid"  # 质粒数据
    BIOSAMPLE = "biosample"  # 生物样本
    PLANT = "plant"  # 植物基因
    SEQUENCE_READ = "sequence_read"  # 测序数据（SRA/BioProject）
    UNKNOWN = "unknown"


class AnalysisGoal(Enum):
    """分析目标"""
    BASIC_INFO = "basic_info"  # 基础信息获取
    FUNCTIONAL_ANALYSIS = "functional_analysis"  # 功能分析
    STRUCTURAL_ANALYSIS = "structural_analysis"  # 结构分析
    PATHWAY_ANALYSIS = "pathway_analysis"  # 通路分析
    INTERACTION_ANALYSIS = "interaction_analysis"  # 互作分析
    ENRICHMENT_ANALYSIS = "enrichment_analysis"  # 富集分析
    LITERATURE_REVIEW = "literature_review"  # 文献综述
    CLINICAL_INTERPRETATION = "clinical_interpretation"  # 临床解读
    DRUG_DISCOVERY = "drug_discovery"  # 药物发现
    COMPARATIVE_ANALYSIS = "comparative_analysis"  # 比较分析
    MULTI_OMICS = "multi_omics"  # 多组学整合


@dataclass
class AnalysisPlan:
    """分析方案"""
    plan_id: str
    description: str
    recommended_tools: List[str]
    expected_results: List[str]
    token_efficiency: str  # high/medium/low
    confidence: float  # 0-1
    alternative_plans: List['AnalysisPlan']
    insights: List[str]  # 用户可能没想到的insights
    execution_order: List[str]  # 工具调用顺序


@dataclass
class DataCharacteristics:
    """数据特征"""
    primary_type: DataType
    secondary_types: List[DataType]
    confidence_scores: Dict[DataType, float]
    metadata: Dict[str, Any]


class DataAnalyzer:
    """数据类型分析器"""

    # 基因名称模式
    GENE_PATTERNS = [
        r'^[A-Z][A-Z0-9]{3,9}$',  # 常见基因命名模式 (BRCA1, TP53, EGFR)
        r'^[A-Z][A-Za-z0-9]{1,20}$',  # 较长的基因名
    ]

    # 基因ID模式
    GENE_ID_PATTERNS = [
        r'^ENSG\d{11}$',  # Ensembl基因ID
        r'^ENSP\d{11}$',  # Ensembl蛋白ID
        r'^[A-Z0-9]{6}$',  # UniProt ID
        r'^NM_\d+\.\d+$',  # RefSeq mRNA ID
        r'^NP_\d+\.\d+$',  # RefSeq蛋白ID
    ]

    # 变异模式
    VARIANT_PATTERNS = [
        r'^chr\d+:[gc]\.\d+[A-Z]>[A-Z]$',  # HGVS格式
        r'^rs\d+$',  # dbSNP ID
        r'^\d+:\d+-$',  # 简单位置格式
    ]

    # 甲基化位点模式（Illumina 450K/EPIC 探针 ID，如 cg14380065）
    METHYLATION_PATTERNS = [
        r'^cg\d+$',
        r'^ch\.\d+\.[A-Za-z]+$',
    ]

    # 结构ID模式
    STRUCTURE_ID_PATTERNS = [
        r'^\d[A-Z0-9]{3}$',  # PDB ID
        r'^EMD-\d{4}$',  # EMDB ID
    ]

    # 化合物模式
    COMPOUND_PATTERNS = [
        r'^CID\d+$',  # PubChem CID
        r'^CHEMBL\d+$',  # ChEMBL ID
    ]

    @classmethod
    def analyze_input(cls, user_input: str) -> DataCharacteristics:
        """分析用户输入，识别数据类型"""
        user_input = user_input.strip()
        primary_type = DataType.UNKNOWN
        secondary_types = []
        confidence_scores = {}

        # 检查基因ID
        for pattern in cls.GENE_ID_PATTERNS:
            if re.match(pattern, user_input, re.IGNORECASE):
                primary_type = DataType.GENE_ID
                confidence_scores[DataType.GENE_ID] = 0.95
                break

        # 检查基因名称
        if primary_type == DataType.UNKNOWN:
            for pattern in cls.GENE_PATTERNS:
                if re.match(pattern, user_input):
                    primary_type = DataType.GENE_NAME
                    confidence_scores[DataType.GENE_NAME] = 0.85
                    break

        # 检查变异数据
        if primary_type == DataType.UNKNOWN:
            for pattern in cls.VARIANT_PATTERNS:
                if re.match(pattern, user_input, re.IGNORECASE):
                    primary_type = DataType.VARIANT
                    confidence_scores[DataType.VARIANT] = 0.90
                    break

        # 检查甲基化位点（CpG）
        if primary_type == DataType.UNKNOWN:
            for pattern in cls.METHYLATION_PATTERNS:
                if re.match(pattern, user_input, re.IGNORECASE):
                    primary_type = DataType.METHYLATION
                    confidence_scores[DataType.METHYLATION] = 0.95
                    break

        # 检查结构ID
        if primary_type == DataType.UNKNOWN:
            for pattern in cls.STRUCTURE_ID_PATTERNS:
                if re.match(pattern, user_input, re.IGNORECASE):
                    primary_type = DataType.STRUCTURE_ID
                    confidence_scores[DataType.STRUCTURE_ID] = 0.95
                    break

        # 检查化合物
        if primary_type == DataType.UNKNOWN:
            for pattern in cls.COMPOUND_PATTERNS:
                if re.match(pattern, user_input, re.IGNORECASE):
                    primary_type = DataType.COMPOUND
                    confidence_scores[DataType.COMPOUND] = 0.90
                    break

        # 检查序列数据
        if primary_type == DataType.UNKNOWN:
            if cls._is_sequence(user_input):
                primary_type = DataType.SEQUENCE
                confidence_scores[DataType.SEQUENCE] = 0.95

        # 检查关键词
        keywords = cls._extract_keywords(user_input.lower())
        if "pathway" in keywords or "通路" in user_input:
            secondary_types.append(DataType.PATHWAY)
            confidence_scores[DataType.PATHWAY] = 0.70
        if "disease" in keywords or "疾病" in user_input or "癌症" in user_input:
            secondary_types.append(DataType.DISEASE)
            confidence_scores[DataType.DISEASE] = 0.75
        if "literature" in keywords or "文献" in user_input or "pubmed" in keywords:
            secondary_types.append(DataType.LITERATURE_QUERY)
            confidence_scores[DataType.LITERATURE_QUERY] = 0.80

        return DataCharacteristics(
            primary_type=primary_type,
            secondary_types=secondary_types,
            confidence_scores=confidence_scores,
            metadata={"raw_input": user_input, "keywords": keywords}
        )

    @classmethod
    def _is_sequence(cls, text: str) -> bool:
        """判断是否为序列数据"""
        # DNA序列 (A,T,G,C)
        dna_chars = set('ATGCNatgcn')
        # 蛋白序列 (20种氨基酸)
        protein_chars = set('ACDEFGHIKLMNPQRSTVWYacdefghiklmnpqrstvwy')

        # 去除空格和数字
        clean_text = re.sub(r'[\s\d]', '', text)
        if len(clean_text) < 10:
            return False

        # 检查是否为DNA序列
        dna_ratio = sum(1 for c in clean_text if c in dna_chars) / len(clean_text)
        if dna_ratio > 0.8:
            return True

        # 检查是否为蛋白序列
        protein_ratio = sum(1 for c in clean_text if c in protein_chars) / len(clean_text)
        if protein_ratio > 0.7:
            return True

        return False

    @classmethod
    def _extract_keywords(cls, text: str) -> List[str]:
        """提取关键词"""
        common_words = {'the', 'is', 'at', 'which', 'on', 'and', 'or', 'for', 'with', 'about'}
        words = re.findall(r'\b\w+\b', text)
        return [w for w in words if w not in common_words and len(w) > 2]


class RecommendationEngine:
    """智能推荐引擎"""

    # 数据类型到工具的映射
    TOOL_MAPPING = {
        DataType.GENE_NAME: [
            "uniprot_annotate", "ensembl_gene_lookup", "string_interactions",
            "gene_enrichment", "gene_full_profile", "pubmed_search",
            "hgnc_search", "biogrid_interactions", "expression_atlas_gene",
            "ensembl_homologs", "protein_domains", "intact_interactions",
            "biogrid_gene_interactions", "expression_atlas_experiment",
            "gene_go_annotation", "gwas_gene_variants", "gnomad_gene_constraint",
            "gtex_tissue_expression", "gtex_eqtl", "ot_target_info",
            "ot_target_disease", "ewas_gene_lookup"
        ],
        DataType.GENE_ID: [
            "uniprot_annotate", "ensembl_gene_lookup", "alphafold_structure",
            "protein_tissue_expression", "string_interactions", "gene_full_profile",
            "hgnc_gene_symbol", "expression_atlas_gene",
            "ensembl_homologs", "protein_domains", "expression_atlas_experiment",
            "gene_go_annotation", "gnomad_gene_constraint", "gtex_tissue_expression",
            "ot_target_info"
        ],
        DataType.SEQUENCE: [
            "ncbi_fetch_sequence", "blast_search", "taxonomy_lookup",
            "uniparc_search", "uniparc_by_id"
        ],
        DataType.VARIANT: [
            "variant_annotate", "clinvar_query", "dbsnp_search",
            "gnomad_variant_lookup", "mqtl_snp_lookup", "gwas_variant_associations",
            "gtex_eqtl"
        ],
        DataType.METHYLATION: [
            "mqtl_snp_lookup", "mqtl_cpg_lookup", "ewas_probe_lookup",
            "ewas_gene_lookup"
        ],
        DataType.COMPOUND: [
            "compound_info", "chembl_drug_search", "unichem_mapping",
            "chebi_compound", "chebi_search", "unichem_structure"
        ],
        DataType.STRUCTURE_ID: [
            "pdb_structure_summary", "alphafold_structure", "emdb_structure_lookup"
        ],
        DataType.PATHWAY: [
            "kegg_pathway_search", "reactome_pathway_search", "kegg_pathway_genes"
        ],
        DataType.LITERATURE_QUERY: [
            "pubmed_search", "europepmc_search", "openalex_work_search"
        ],
        DataType.MICROBIOME: [
            "microbiome_study_search", "genome_assembly_search", "ena_sequence_search",
            "sra_search", "bioproject_search"
        ],
        DataType.SINGLE_CELL: [
            "cellxgene_search"
        ],
        DataType.GLYCANS: [
            "glycan_lookup", "protein_glycosylation"
        ],
        DataType.METABOLOMICS: [
            "metabolomics_study", "metabolomics_latest"
        ],
        DataType.LIPIDOMICS: [
            "lipid_lookup"
        ],
        DataType.PROTEOMICS: [
            "pride_project", "pride_search"
        ],
        DataType.MODEL_ORGANISM: [
            "flybase_gene", "flybase_search", "wormbase_gene", "wormbase_search",
            "rgd_gene_symbol", "rgd_search"
        ],
        DataType.PLASMID: [
            "plasmid_search", "biosample_by_id", "sra_search"
        ],
        DataType.BIOSAMPLE: [
            "biosample_by_id", "biosample_search"
        ],
        DataType.PLANT: [
            "plant_gene_lookup", "plant_species_list"
        ],
        DataType.SEQUENCE_READ: [
            "sra_search", "bioproject_search", "geo_dataset_search"
        ]
    }

    # 每个注册工具都必须在 TOOL_MAPPING 或 UTILITY_TOOLS 中（由一致性测试兜底）

    @classmethod
    def generate_recommendations(cls, data_chars: DataCharacteristics,
                                goal: Optional[AnalysisGoal] = None) -> List[AnalysisPlan]:
        """生成分析方案推荐"""
        primary_tools = cls.TOOL_MAPPING.get(data_chars.primary_type, [])

        # 基于分析目标优化工具选择
        if goal:
            primary_tools = cls._optimize_for_goal(primary_tools, goal, data_chars)

        # 生成主方案
        primary_plan = cls._create_primary_plan(data_chars, primary_tools, goal)

        # 生成备选方案
        alternative_plans = cls._create_alternative_plans(data_chars, goal)

        return [primary_plan] + alternative_plans

    @classmethod
    def _optimize_for_goal(cls, tools: List[str], goal: AnalysisGoal,
                          data_chars: DataCharacteristics) -> List[str]:
        """根据分析目标优化工具选择"""
        goal_tool_mapping = {
            AnalysisGoal.BASIC_INFO: ["uniprot_annotate", "ensembl_gene_lookup", "pubmed_search"],
            AnalysisGoal.FUNCTIONAL_ANALYSIS: ["uniprot_annotate", "protein_domains", "gene_enrichment"],
            AnalysisGoal.STRUCTURAL_ANALYSIS: ["pdb_structure_summary", "alphafold_structure", "emdb_structure_lookup"],
            AnalysisGoal.PATHWAY_ANALYSIS: ["kegg_pathway_search", "reactome_pathway_search", "kegg_pathway_genes"],
            AnalysisGoal.INTERACTION_ANALYSIS: ["string_interactions", "intact_interactions"],
            AnalysisGoal.ENRICHMENT_ANALYSIS: ["gene_enrichment", "kegg_pathway_search"],
            AnalysisGoal.LITERATURE_REVIEW: ["pubmed_search", "europepmc_search", "openalex_work_search"],
            AnalysisGoal.CLINICAL_INTERPRETATION: ["variant_annotate", "clinvar_query", "protein_tissue_expression"],
            AnalysisGoal.DRUG_DISCOVERY: ["chembl_drug_search", "compound_info", "string_interactions"],
            AnalysisGoal.MULTI_OMICS: ["gene_full_profile", "cellxgene_search", "metabolomics_study"]
        }

        goal_tools = goal_tool_mapping.get(goal, [])
        # 优先使用与目标匹配的工具
        prioritized_tools = [t for t in goal_tools if t in tools]
        # 添加其他相关工具
        prioritized_tools.extend([t for t in tools if t not in prioritized_tools])

        return prioritized_tools[:10]  # 限制工具数量以节省token

    @classmethod
    def _create_primary_plan(cls, data_chars: DataCharacteristics,
                            tools: List[str], goal: Optional[AnalysisGoal]) -> AnalysisPlan:
        """创建主分析方案"""
        insights = cls._generate_insights(data_chars, goal)
        expected_results = cls._predict_results(data_chars, tools, goal)

        return AnalysisPlan(
            plan_id="primary",
            description=f"针对{data_chars.primary_type.value}类型数据的主要分析方案",
            recommended_tools=tools[:6],  # 限制工具数量
            expected_results=expected_results,
            token_efficiency="high",
            confidence=data_chars.confidence_scores.get(data_chars.primary_type, 0.8),
            alternative_plans=[],
            insights=insights,
            execution_order=cls._optimize_execution_order(tools[:6])
        )

    @classmethod
    def _create_alternative_plans(cls, data_chars: DataCharacteristics,
                                  goal: Optional[AnalysisGoal]) -> List[AnalysisPlan]:
        """创建备选方案"""
        plans = []

        # 方案1: 跨库验证方案
        if data_chars.primary_type in [DataType.GENE_NAME, DataType.GENE_ID]:
            plans.append(AnalysisPlan(
                plan_id="cross_validation",
                description="跨库验证方案，使用多个数据库交叉验证结果",
                recommended_tools=["gene_full_profile", "uniprot_annotate", "ensembl_gene_lookup"],
                expected_results=["跨库一致的结果", "数据质量评估", "置信度评分"],
                token_efficiency="medium",
                confidence=0.85,
                alternative_plans=[],
                insights=["跨库验证可以提高结果可靠性", "不同数据库可能有不同的更新周期"],
                execution_order=["gene_full_profile", "uniprot_annotate", "ensembl_gene_lookup"]
            ))

        # 方案2: 文献辅助方案
        plans.append(AnalysisPlan(
            plan_id="literature_assisted",
            description="结合文献分析的综合方案",
            recommended_tools=["pubmed_search", "europepmc_search"] +
                            (["gene_enrichment"] if data_chars.primary_type in [DataType.GENE_NAME, DataType.GENE_ID] else []),
            expected_results=["相关研究文献", "研究热点分析", "引用关系网络"],
            token_efficiency="medium",
            confidence=0.75,
            alternative_plans=[],
            insights=["文献分析可以发现研究趋势", "高引用文献通常更可靠"],
            execution_order=["pubmed_search", "europepmc_search", "gene_enrichment"]
        ))

        return plans

    @classmethod
    def _generate_insights(cls, data_chars: DataCharacteristics,
                          goal: Optional[AnalysisGoal]) -> List[str]:
        """生成用户可能没想到的insights"""
        insights = []

        # 基于数据类型的insights
        if data_chars.primary_type == DataType.GENE_NAME:
            insights.extend([
                "建议检查基因的物种特异性，不同物种的同一基因可能功能不同",
                "考虑该基因在不同发育阶段或组织中的表达差异",
                "可以探索该基因在疾病状态下的异常表达模式"
            ])
        elif data_chars.primary_type == DataType.SEQUENCE:
            insights.extend([
                "序列同源性分析可以揭示进化关系和功能保守性",
                "考虑序列中的结构域和motif，它们可能决定蛋白功能",
                "序列变异可能影响蛋白的稳定性或互作能力"
            ])
        elif data_chars.primary_type == DataType.VARIANT:
            insights.extend([
                "变异的功能影响需要结合蛋白结构位置来评估",
                "同一变异在不同人群中的频率可能差异很大",
                "考虑变异的连锁不平衡模式"
            ])

        # 基于分析目标的insights
        if goal == AnalysisGoal.DRUG_DISCOVERY:
            insights.extend([
                "药物靶点的可药性评估很重要，不是所有蛋白都适合作为药物靶点",
                "考虑靶点在不同组织中的表达，避免副作用",
                "评估靶点的结构与已知药物靶点的相似性"
            ])
        elif goal == AnalysisGoal.MULTI_OMICS:
            insights.extend([
                "多组学数据整合时要注意不同数据的批次效应",
                "时间序列数据可以揭示动态变化过程",
                "考虑样本间的异质性，避免过度概括"
            ])

        return insights[:8]  # 限制insights数量

    @classmethod
    def _predict_results(cls, data_chars: DataCharacteristics,
                       tools: List[str], goal: Optional[AnalysisGoal]) -> List[str]:
        """预测分析结果"""
        results = []

        tool_results = {
            "uniprot_annotate": ["蛋白基本信息", "功能描述", "亚细胞定位"],
            "ensembl_gene_lookup": ["基因组位置", "转录本信息", "同源基因"],
            "string_interactions": ["蛋白互作网络", "互作置信度", "功能关联"],
            "gene_enrichment": ["GO富集分析", "KEGG通路", "Reactome通路"],
            "pubmed_search": ["相关文献", "引用数量", "研究趋势"],
            "pdb_structure_summary": ["结构信息", "分辨率", "实验方法"],
            "alphafold_structure": ["预测结构", "置信度评分", "结构域"],
            "variant_annotate": ["变异注释", "功能预测", "临床意义"],
            "chembl_drug_search": ["药物活性", "靶点信息", "IC50/Ki值"]
        }

        for tool in tools[:5]:  # 限制预测数量
            if tool in tool_results:
                results.extend(tool_results[tool])

        return results[:15]  # 限制结果数量

    @classmethod
    def _optimize_execution_order(cls, tools: List[str]) -> List[str]:
        """优化工具执行顺序以提高效率"""
        # 优先级映射
        priority = {
            "gene_full_profile": 1,  # 综合工具优先
            "uniprot_annotate": 2,
            "ensembl_gene_lookup": 2,
            "pubmed_search": 3,
            "string_interactions": 4,
            "gene_enrichment": 5
        }

        return sorted(tools, key=lambda x: priority.get(x, 999))


class IntelligentAgent:
    """智能数据推荐Agent"""

    def __init__(self, total_tools: Optional[int] = None):
        self.data_analyzer = DataAnalyzer()
        self.recommendation_engine = RecommendationEngine()
        self.total_tools = total_tools

    def analyze_and_recommend(self, user_input: str,
                            goal: Optional[str] = None) -> Dict[str, Any]:
        """分析用户输入并推荐方案"""

        # 分析数据类型
        data_chars = self.data_analyzer.analyze_input(user_input)

        # 解析分析目标
        analysis_goal = self._parse_goal(goal) if goal else None

        # 生成推荐方案
        plans = self.recommendation_engine.generate_recommendations(
            data_chars, analysis_goal
        )

        # 构建响应
        response = {
            "data_analysis": {
                "primary_type": data_chars.primary_type.value,
                "secondary_types": [t.value for t in data_chars.secondary_types],
                "confidence": {k.value: v for k, v in data_chars.confidence_scores.items()},
                "metadata": data_chars.metadata
            },
            "recommended_plans": [
                {
                    "plan_id": plan.plan_id,
                    "description": plan.description,
                    "recommended_tools": plan.recommended_tools,
                    "expected_results": plan.expected_results,
                    "token_efficiency": plan.token_efficiency,
                    "confidence": plan.confidence,
                    "insights": plan.insights,
                    "execution_order": plan.execution_order
                }
                for plan in plans
            ],
            "token_optimization": {
                "primary_tools_count": len(plans[0].recommended_tools),
                "estimated_token_saving": f"约{self._estimate_token_saving(plans)}%",
                "recommendation": "先执行主方案，如需更多结果再考虑备选方案"
            },
            "next_steps": [
                f"1. 数据类型识别为: {data_chars.primary_type.value}",
                f"2. 建议使用 {len(plans[0].recommended_tools)} 个核心工具",
                "3. 按推荐顺序执行工具调用",
                "4. 根据结果评估是否需要备选方案"
            ]
        }

        return response

    def _parse_goal(self, goal_str: str) -> Optional[AnalysisGoal]:
        """解析分析目标"""
        goal_mapping = {
            "basic": AnalysisGoal.BASIC_INFO,
            "function": AnalysisGoal.FUNCTIONAL_ANALYSIS,
            "structure": AnalysisGoal.STRUCTURAL_ANALYSIS,
            "pathway": AnalysisGoal.PATHWAY_ANALYSIS,
            "interaction": AnalysisGoal.INTERACTION_ANALYSIS,
            "enrichment": AnalysisGoal.ENRICHMENT_ANALYSIS,
            "literature": AnalysisGoal.LITERATURE_REVIEW,
            "clinical": AnalysisGoal.CLINICAL_INTERPRETATION,
            "drug": AnalysisGoal.DRUG_DISCOVERY,
            "comparative": AnalysisGoal.COMPARATIVE_ANALYSIS,
            "multi_omics": AnalysisGoal.MULTI_OMICS
        }
        return goal_mapping.get(goal_str.lower())

    def _estimate_token_saving(self, plans: List[AnalysisPlan]) -> int:
        """估算token节省百分比"""
        # 与穷举所有工具相比的节省比例
        primary_tools = len(plans[0].recommended_tools)
        all_possible_tools = self.total_tools or DEFAULT_TOTAL_TOOLS
        saving = ((all_possible_tools - primary_tools) / all_possible_tools) * 100
        return round(saving)


def analyze_input_data(
    user_input: str,
    analysis_goal: Optional[str] = None,
    total_tools: Optional[int] = None,
) -> str:
    """主入口函数：分析用户输入并生成推荐方案

    Args:
        user_input: 用户的原始数据或查询
        analysis_goal: 可选的分析目标 (basic/function/structure/pathway等)
        total_tools: 当前注册的工具总数（用于 token 节省估算；缺省用回退值）

    Returns:
        JSON格式的推荐方案
    """
    agent = IntelligentAgent(total_tools=total_tools)
    result = agent.analyze_and_recommend(user_input, analysis_goal)
    return json.dumps(result, ensure_ascii=False, indent=2)


# MCP工具注册
def register(server):
    """注册智能推荐工具到MCP服务器"""

    @server.tool("intelligent_analyze", description="智能分析生物数据并推荐最佳分析方案，节省token使用。输入：数据字符串，可选分析目标。输出：数据类型识别、推荐工具、预期结果、insights等。")
    async def intelligent_analyze_tool(user_input: str, analysis_goal: Optional[str] = None) -> str:
        """智能分析生物数据并推荐最佳分析方案"""
        tools = await server.list_tools()
        return analyze_input_data(user_input, analysis_goal, total_tools=len(tools))

    @server.tool("get_analysis_template", description="获取常见分析场景的模板方案。输入：场景类型(基因研究/药物发现/疾病分析等)。输出：模板化的分析流程和工具列表。")
    def get_analysis_template_tool(scenario: str) -> str:
        """获取分析场景模板"""
        templates = {
            "基因研究": {
                "scenario": "基因功能研究",
                "recommended_workflow": [
                    "1. 使用 uniprot_annotate 获取蛋白基础信息",
                    "2. 使用 ensembl_gene_lookup 获取基因组信息",
                    "3. 使用 string_interactions 分析蛋白互作网络",
                    "4. 使用 gene_enrichment 进行富集分析",
                    "5. 使用 pubmed_search 查阅相关文献"
                ],
                "expected_outcomes": [
                    "蛋白功能和定位信息",
                    "基因组位置和同源性分析",
                    "互作伙伴和通路信息",
                    "GO/KEGG富集结果",
                    "相关研究文献"
                ],
                "token_efficiency": "high"
            },
            "药物发现": {
                "scenario": "药物靶点发现和验证",
                "recommended_workflow": [
                    "1. 使用 uniprot_annotate 分析靶点蛋白",
                    "2. 使用 pdb_structure_summary 获取结构信息",
                    "3. 使用 chembl_drug_search 查找已知药物",
                    "4. 使用 compound_info 分析化合物特性",
                    "5. 使用 variant_annotate 评估变异影响"
                ],
                "expected_outcomes": [
                    "靶点蛋白详细注释",
                    "3D结构和药物结合位点",
                    "已知药物活性和选择性",
                    "化合物ADMET特性",
                    "变异对药物反应的影响"
                ],
                "token_efficiency": "medium"
            }
        }

        template = templates.get(scenario, {
            "scenario": "通用分析",
            "recommended_workflow": ["建议使用 intelligent_analyze 工具进行定制化分析"],
            "expected_outcomes": ["根据具体数据类型定制"],
            "token_efficiency": "high"
        })

        return json.dumps(template, ensure_ascii=False, indent=2)