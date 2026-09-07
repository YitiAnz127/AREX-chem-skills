# 化学 / 化工 / 分子 / 制药 — Skills 仓库清单

> 筛选自 4018 个检索仓库 / 1581 个领域相关仓库
>
> **500 个去重规则**：每个仓库只归属一个主领域（跨领域重叠为 0），并按各子领域体量比例分配名额，保证 8 大子领域均匀覆盖。语言均为 Python / Jupyter（符合 DisCo 封装前提）。
>
> **封装判定**：✅ = 可直接用 create-repo-skill 一键蒸馏（许可证可再分发）；⚠️ = 需预处理/无明确许可证/教程型，走 paper-skill 或 task-oriented 蒸馏。

## 目录
- [化学 / 化工 / 分子 / 制药 — Skills 仓库清单](#化学--化工--分子--制药--skills-仓库清单)
  - [目录](#目录)
  - [药物发现 drug-discovery  ](#药物发现-drug-discovery--)
  - [量子化学 quantum-chem  ](#量子化学-quantum-chem--)
  - [化学信息学 cheminformatics  ](#化学信息学-cheminformatics--)
  - [材料信息学 materials  ](#材料信息学-materials--)
  - [化学工程 chem-eng  ](#化学工程-chem-eng--)
  - [分子模拟 molecular-sim  ](#分子模拟-molecular-sim--)
  - [制药/ADMET pharma-admet  ](#制药admet-pharma-admet--)
  - [蛋白质-配体 protein-ligand  ](#蛋白质-配体-protein-ligand--)
  - [封装可行性说明](#封装可行性说明)

## 药物发现 drug-discovery  <a id="drugdiscovery"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [DeepGraphLearning/torchdrug](https://github.com/DeepGraphLearning/torchdrug) | 1587 | A powerful and flexible machine learning platform for drug discovery | ✅ |
| [molecularsets/moses](https://github.com/molecularsets/moses) | 988 | Molecular Sets (MOSES): A Benchmarking Platform for Molecular Generation Models | ✅ |
| [NVIDIA-BioNeMo/bionemo-recipes](https://github.com/NVIDIA-BioNeMo/bionemo-recipes) | 852 | BioNeMo Recipes: For building and adapting AI models in drug discovery at scale | ⚠️ |
| [Mariewelt/OpenChem](https://github.com/Mariewelt/OpenChem) | 752 | OpenChem: Deep Learning toolkit for Computational Chemistry and Drug Design Research | ✅ |
| [aurekaresearch/OpenDDE](https://github.com/aurekaresearch/OpenDDE) | 449 | An Open-source Drug Discovery Engine | ✅ |
| [guanjq/targetdiff](https://github.com/guanjq/targetdiff) | 346 | The official implementation of 3D Equivariant Diffusion for Target-Aware Molecule Generation and Affinity Prediction (ICLR 2023) | ⚠️ |
| [MinkaiXu/GeoLDM](https://github.com/MinkaiXu/GeoLDM) | 274 | Geometric Latent Diffusion Models for 3D Molecule Generation | ✅ |
| [Dunni3/FlowMol](https://github.com/Dunni3/FlowMol) | 217 | Mixed continous/categorical flow-matching model for de novo molecule generation. | ✅ |
| [coleygroup/molpal](https://github.com/coleygroup/molpal) | 213 | active learning for accelerated high-throughput virtual screening | ✅ |
| [zjunlp/MolGen](https://github.com/zjunlp/MolGen) | 195 | [ICLR 2024] Domain-Agnostic Molecular Generation with Chemical Feedback | ✅ |
| [wengong-jin/multiobj-rationale](https://github.com/wengong-jin/multiobj-rationale) | 170 | Multi-Objective Molecule Generation using Interpretable Substructures (ICML 2020) | ✅ |
| [LPDI-EPFL/DrugFlow](https://github.com/LPDI-EPFL/DrugFlow) | 166 | Multi-domain Distribution Learning for De Novo Drug Design | ✅ |
| [polaris-hub/polaris](https://github.com/polaris-hub/polaris) | 144 | Foster the development of impactful AI models in drug discovery. | ✅ |
| [kevinid/molecule_generator](https://github.com/kevinid/molecule_generator) | 138 | Code for "Multi-Objective De Novo Drug Design with Conditional Graph Generative Model" (https://arxiv.org/abs/1801.07299) | ✅ |
| [pineappleK/ED2Mol](https://github.com/pineappleK/ED2Mol) | 136 | Electron-density-informed effective and reliable de novo molecular design and optimization with ED2Mol | ✅ |
| [aamini/chemprop](https://github.com/aamini/chemprop) | 136 | Fast and scalable uncertainty quantification for neural molecular property prediction, accelerated optimization, and guided virtual screening. | ✅ |
| [MolecularAI/DockStream](https://github.com/MolecularAI/DockStream) | 136 | DockStream: A Docking Wrapper to Enhance De Novo Molecular Design | ✅ |
| [prasadseemakurthi/Deep-Neural-Networks-HealthCare](https://github.com/prasadseemakurthi/Deep-Neural-Networks-HealthCare) | 135 | Tangible and Practical Deep Learning Projects Repository for Healthcare such as Cancer, Drug Discovery, Genomic and More | ✅ |
| [MengwuXiao/GetBox-PyMOL-Plugin](https://github.com/MengwuXiao/GetBox-PyMOL-Plugin) | 127 | A PyMOL Plugin for calculating docking box for LeDock, AutoDock and AutoDock Vina. | ✅ |
| [Acellera/acegen-open](https://github.com/Acellera/acegen-open) | 120 | Language models for drug discovery using torchrl | ✅ |
| [cvignac/MiDi](https://github.com/cvignac/MiDi) | 116 | MiDi: Mixed Graph and 3D Denoising Diffusion for Molecule Generation | ✅ |
| [benstaf/ChemGAN-challenge](https://github.com/benstaf/ChemGAN-challenge) | 115 | Code for the paper: ChemGAN challenge for drug discovery: can AI reproduce natural chemical diversity? arXiv preprint arXiv:1708.08227. | ⚠️ |
| [liugangcode/Graph-DiT](https://github.com/liugangcode/Graph-DiT) | 114 | The code for "Graph Diffusion Transformer for Multi-Conditional Molecular Generation" | ⚠️ |
| [osrf/autodock](https://github.com/osrf/autodock) | 113 | ROS packages for automatic docking | ✅ |
| [SeonghwanSeo/PharmacoNet](https://github.com/SeonghwanSeo/PharmacoNet) | 102 | Official Github for "PharmacoNet: deep learning-guided pharmacophore modeling for ultra-large-scale virtual screening" (Chemical Science) | ✅ |
| [gmh14/data_efficient_grammar](https://github.com/gmh14/data_efficient_grammar) | 101 | [ICLR 2022] Data-Efficient Graph Grammar Learning for Molecular Generation | ✅ |
| [vibudh2209/D2](https://github.com/vibudh2209/D2) | 100 | Speed virtual screening by 50X | ✅ |
| [ohuelab/boltzina](https://github.com/ohuelab/boltzina) | 100 | Boltzina: Efficient and Accurate Virtual Screening via Docking-Guided Binding Prediction with Boltz-2 | ✅ |
| [coleygroup/shepherd](https://github.com/coleygroup/shepherd) | 95 | Training and inference code for ShEPhERD: Diffusing shape, electrostatics, and pharmacophores for bioisosteric drug design [ICLR 2025 oral] | ✅ |
| [coleygroup/pyscreener](https://github.com/coleygroup/pyscreener) | 94 | pythonic interface to virtual screening software | ✅ |
| [acharkq/NExT-Mol](https://github.com/acharkq/NExT-Mol) | 93 | Source code for ICLR2025 paper "NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation". | ⚠️ |
| [durrantlab/gypsum_dl](https://github.com/durrantlab/gypsum_dl) | 86 | Open-source tool to generate 3D-ready small molecules for virtual screening | ✅ |
| [CataAI/PoseX](https://github.com/CataAI/PoseX) | 85 | PoseX: A Molecular Docking Benchmark | ✅ |
| [janash/iqb-2024](https://github.com/janash/iqb-2024) | 82 | Notebooks and environment set up for IQB 2024 workshop - Python for Molecular Docking | ✅ |
| [datamol-io/medchem](https://github.com/datamol-io/medchem) | 78 | Molecular filtering for drug discovery. | ✅ |
| [RMeli/gnina-torch](https://github.com/RMeli/gnina-torch) | 77 | 馃敟 PyTorch implementation of GNINA scoring function for molecular docking | ✅ |
| [OdinZhang/SurfGen](https://github.com/OdinZhang/SurfGen) | 77 | SurfGen: Learning on Topological Surface and Geometric Structure for 3D Molecular Generation | ✅ |
| [awslabs/quantum-computing-exploration-for-drug-discovery-on-aws](https://github.com/awslabs/quantum-computing-exploration-for-drug-discovery-on-aws) | 76 | Deploy a solution to research on drug discovery problems using quantum computing and classical computing resources. | ✅ |
| [stan-his/DeepFMPO](https://github.com/stan-his/DeepFMPO) | 72 | Code accompanying the paper "Deep reinforcement learning for multiparameter optimization in de novo drug design" | ✅ |
| [CSUBioGroup/PGMG](https://github.com/CSUBioGroup/PGMG) | 72 | The official PyTorch implementation of PGMG: A Pharmacophore-Guided Deep Learning Approach for Bioactive Molecule Generation. | ⚠️ |
| [jkwang93/Token-Mol](https://github.com/jkwang93/Token-Mol) | 66 | Token-Mol 1.0锛歵okenized drug design with large language model | ✅ |
| [forlilab/Ringtail](https://github.com/forlilab/Ringtail) | 65 | Package for storage and analysis of virtual screenings run with AutoDock-GPU and AutoDock Vina | ✅ |
| [MIRALab-USTC/AI4Sci-MiCaM](https://github.com/MIRALab-USTC/AI4Sci-MiCaM) | 63 | This is the code of paper "De Novo Molecular Generation via Connection-aware Motif Mining". Zijie Geng, Shufang Xie, Yingce Xia, Lijun Wu, Tao Qin, Jie Wang, Yo… | ⚠️ |
| [elix-tech/kmol](https://github.com/elix-tech/kmol) | 63 | kMoL is a machine learning library for drug discovery and life sciences, with federated learning capabilities. | ✅ |
| [Liu-Group-UF/PropMolFlow](https://github.com/Liu-Group-UF/PropMolFlow) | 62 | SE(3) Equivariant Flow Matching for Property-Guided Molecule Generation. | ✅ |
| [rssrwn/semla-flow](https://github.com/rssrwn/semla-flow) | 61 | Efficient 3D molecular generation with flow-matching and Semla | ✅ |
| [durrantlab/autogrow4](https://github.com/durrantlab/autogrow4) | 58 | AutoGrow4 is an open-source program for semi-automated computer-aided drug discovery. It uses a genetic algorithm to evolve predicted ligands on demand and so i… | ✅ |
| [GRAPH-0/JODO](https://github.com/GRAPH-0/JODO) | 57 | Learning Joint 2D & 3D Diffusion Models for Complete Molecule Generation | ✅ |
| [itWangCode/AI-Drug-Discovery-Design](https://github.com/itWangCode/AI-Drug-Discovery-Design) | 57 | AI drug design | ⚠️ |
| [insilicomedicine/BiAAE](https://github.com/insilicomedicine/BiAAE) | 54 | Molecular Generation for Desired Transcriptome Changes with Adversarial Autoencoders | ✅ |
| [IDEA-XL/InstructMol](https://github.com/IDEA-XL/InstructMol) | 54 | InstructMol: Multi-Modal Integration for Building a Versatile and Reliable Molecular Assistant in Drug Discovery (COLING 2025) | ✅ |
| [uibcdf/OpenPharmacophore](https://github.com/uibcdf/OpenPharmacophore) | 52 | An open library to work with pharmacophores. | ✅ |
| [qiangbo1222/HierDiff](https://github.com/qiangbo1222/HierDiff) | 51 | Implementation of ICML2023 paper : Coarse-to-Fine: a Hierarchical Diffusion Model for Molecule Generation in 3D | ⚠️ |
| [VicFisher/DiffPhore](https://github.com/VicFisher/DiffPhore) | 51 | Knowledge-Guided Diffusion Model for 3D Ligand-Pharmacophore Mapping | ✅ |
| [asapdiscovery/asapdiscovery](https://github.com/asapdiscovery/asapdiscovery) | 49 | Toolkit for open antiviral drug discovery by the ASAP Discovery Consortium | ✅ |
| [itWangCode/AIGC-in-drug-design](https://github.com/itWangCode/AIGC-in-drug-design) | 49 | Application of AIGC in drug design | ⚠️ |
| [sb-ai-lab/MADD](https://github.com/sb-ai-lab/MADD) | 47 | Multi agent system for drug discovery tasks | ⚠️ |
| [GenSI-THUAIR/MolFM](https://github.com/GenSI-THUAIR/MolFM) | 45 | Implementation for NeurIPS 2023 paper "Equivariant Flow Matching with Hybrid Probability Transport for 3D Molecule Generation" | ⚠️ |
| [Wang-Lin-boop/Ouroboros](https://github.com/Wang-Lin-boop/Ouroboros) | 44 | An official implementation of "Directed Chemical Evolution via Navigating Molecular Encoding Space.", which is a foundational model to bridge the gap between re… | ✅ |
| [genedisco/genedisco](https://github.com/genedisco/genedisco) | 43 | GeneDisco is a benchmark suite for evaluating active learning algorithms for experimental design in drug discovery.  | ✅ |
| [hoon-ock/AgentD](https://github.com/hoon-ock/AgentD) | 43 | llm agent for drug discovery | ✅ |
| [molecularmodelinglab/plantain](https://github.com/molecularmodelinglab/plantain) | 42 | Fast and accurate molecular docking with an AI pose scoring function | ✅ |
| [AIDD-LiLab/Apo2Mol](https://github.com/AIDD-LiLab/Apo2Mol) | 41 | Apo2Mol: 3D Molecule Generation via Dynamic Pocket-Aware Diffusion Models | ✅ |
| [HXYfighter/MolRL-MGPT](https://github.com/HXYfighter/MolRL-MGPT) | 41 | NeurIPS 2023 paper: De novo Drug Design using Reinforcement Learning with Multiple GPT Agents | ⚠️ |
| [CMACH508/AlphaDrug](https://github.com/CMACH508/AlphaDrug) | 41 | AlphaDrug: Protein Target Specific De Novo Molecular Generation | ✅ |
| [SeonghwanSeo/RxnFlow](https://github.com/SeonghwanSeo/RxnFlow) | 40 | Synthesis-oriented GFlowNets on a large action space: "Generative Flows on Synthetic Pathway for Drug Design" (ICLR 2025) | ✅ |
| [ppjian19/PhoreGen](https://github.com/ppjian19/PhoreGen) | 40 | PhoreGen: Pharmacophore-Oriented 3D Molecular Generation towards Efficient Feature-Customized Drug Discovery https://www.nature.com/articles/s43588-025-00850-5 | ✅ |
| [CMACH508/KGDiff](https://github.com/CMACH508/KGDiff) | 39 | Towards Explainable Target-Aware Molecule Generation with Knowledge Guidance | ✅ |
| [jostorge/diffusion-hopping](https://github.com/jostorge/diffusion-hopping) | 37 | DiffHopp: A Graph Diffusion Model for Novel Drug Design via Scaffold Hopping | ✅ |
| [TheVisualHub/DrugHunting](https://github.com/TheVisualHub/DrugHunting) | 37 | ?? Cutting-edge automation of computational drug discovery pipelines | ✅ |
| [jacquesboitreaud/OptiMol](https://github.com/jacquesboitreaud/OptiMol) | 36 | Optimization of binding affinities in chemical space for drug discovery | ⚠️ |
| [shukai1997/VSDS-VD](https://github.com/shukai1997/VSDS-VD) | 36 | benchmarking AI-powered docking methods from the perspective of virtual screening | ✅ |
| [ci-lab-cz/crem-dock](https://github.com/ci-lab-cz/crem-dock) | 36 | CReM-dock: generation of chemically reasonable molecules guided by molecular docking | ✅ |
| [longlongman/DESERT](https://github.com/longlongman/DESERT) | 35 | Zero-Shot 3D Drug Design by Sketching and Generating (NeurIPS 2022) | ⚠️ |
| [davidbuterez/mf-pcba](https://github.com/davidbuterez/mf-pcba) | 35 | Source code accompanying the 'MF-PCBA: Multi-fidelity high-throughput screening benchmarks for drug discovery and machine learning' paper | ✅ |
| [ci-lab-cz/pharmd](https://github.com/ci-lab-cz/pharmd) | 35 | MD pharmacophores and virtual screening | ✅ |
| [CRIPAC-DIG/tgm-dlm](https://github.com/CRIPAC-DIG/tgm-dlm) | 34 | Code for AAAI24 paper Text-Guided Molecule Generation with Diffusion Language Model  | ⚠️ |
| [AstraZeneca/kgem-in-drug-discovery](https://github.com/AstraZeneca/kgem-in-drug-discovery) | 34 | Code to accompany the "Understanding the Performance of Knowledge Graph Embeddings in Drug Discovery" manuscript (Artificial Intelligence in the Life Sciences, … | ✅ |
| [bjing2016/scalar-fields](https://github.com/bjing2016/scalar-fields) | 34 | Equivariant Scalar Fields for Molecular Docking with Fast Fourier Transforms | ✅ |
| [aretasg/dockit](https://github.com/aretasg/dockit) | 33 | High-throughput molecular docking with multiple targets and ligands using Vina series engines | ✅ |
| [grisoniFr/scaffold_hopping_whales](https://github.com/grisoniFr/scaffold_hopping_whales) | 33 | Code to perform scaffold hopping and virtual screening using WHALES descriptors. | ✅ |
| [pgniewko/forward_forward_vhts](https://github.com/pgniewko/forward_forward_vhts) | 33 | The Forward-Forward Algorithm for Drug Discovery | ✅ |
| [bio-hpc/metascreener](https://github.com/bio-hpc/metascreener) | 32 | Collection of scripts that integrates docking, virtual screening, similarity and molecular modeling programs. | ✅ |
| [andreirekesh/SynCoGen](https://github.com/andreirekesh/SynCoGen) | 32 | Synthesizable 3D Molecule Generation via Joint Reaction and Coordinate Modeling | ⚠️ |
| [purnawanpp/Docking-4ieh](https://github.com/purnawanpp/Docking-4ieh) | 32 |  Docking Tutorial Using Autodock Vina version 1.2.3 (2021) and AutoDock-GPU Version 1.5.3 | ⚠️ |
| [CCBatIIT/AlGDock](https://github.com/CCBatIIT/AlGDock) | 32 | Molecular docking with Alchemical Interaction Grids | ✅ |
| [atomicarchitects/symphony](https://github.com/atomicarchitects/symphony) | 30 | [ICLR'24] Symphony: Symmetry-Equivariant Point-Centered Spherical Harmonics for Molecule Generation | ✅ |
| [jaechanglim/molecule-generator](https://github.com/jaechanglim/molecule-generator) | 29 | Tensorflow implementation of Generating Focussed Molecule Libraries for Drug Discovery with Recurrent Neural Networks | ⚠️ |
| [yazdanimehdi/DeepDrugDomain](https://github.com/yazdanimehdi/DeepDrugDomain) | 29 | DeepDrugDomain: A versatile Python toolkit for streamlined preprocessing and accurate prediction of drug-target interactions and binding affinities, leveraging … | ✅ |
| [SMU-CATCO/SmartCADD](https://github.com/SMU-CATCO/SmartCADD) | 29 |  SmartCADD is an open-source virtual screening platform that combines deep learning, computer-aided drug design (CADD), and quantum mechanics methodologies with… | ⚠️ |
| [DevSlem/Mol-AIR](https://github.com/DevSlem/Mol-AIR) | 29 | Molecular Reinforcement Learning with Adaptive Intrinsic Reward for Goal-directed Molecular Generation. | ⚠️ |
| [rochoa85/dockECR](https://github.com/rochoa85/dockECR) | 28 | dockECR: open consensus docking and ranking protocol for virtual screening of small molecules | ✅ |
| [D4-course/EDM](https://github.com/D4-course/EDM) | 28 | EDM: E(3) Equivariant Diffusion Model for Molecule Generation in 3D | ⚠️ |
| [Sbolivar16/MolecularDocking](https://github.com/Sbolivar16/MolecularDocking) | 28 | Tools for molecular Docking | ✅ |
| [UCL/Open_Docking_Lab_Handbook](https://github.com/UCL/Open_Docking_Lab_Handbook) | 28 | A place to store and edit the lab handbook for UCL courses that involve the use of open source tools in molecular docking. | ⚠️ |
| [drug2ways/drug2ways](https://github.com/drug2ways/drug2ways) | 28 | A Python package for drug discovery by analyzing causal paths on multiscale networks | ✅ |
| [carlosinator/tabasco](https://github.com/carlosinator/tabasco) | 28 | A Fast, Simplified Model for Molecular Generation with Improved Physical Quality | ✅ |
| [aqlaboratory/QuickBind](https://github.com/aqlaboratory/QuickBind) | 26 | A Light-Weight And Interpretable Molecular Docking Model | ✅ |
| [quantaosun/notebook](https://github.com/quantaosun/notebook) | 26 | My first ever repository, some notebooks useful, others sucks. Topics include file format conversion with obabel, docking with Auto Dock, MD with Charmm GUI and… | ✅ |

---

## 量子化学 quantum-chem  <a id="quantumchem"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [bayesian-optimization/BayesianOptimization](https://github.com/bayesian-optimization/BayesianOptimization) | 8704 | A Python implementation of global optimization with gaussian processes. | ✅ |
| [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane) | 3453 | PennyLane is an open-source quantum software platform for quantum computing, quantum machine learning, and quantum chemistry. Create meaningful quantum algorith… | ✅ |
| [pyscf/pyscf](https://github.com/pyscf/pyscf) | 1666 | Python module for quantum chemistry | ✅ |
| [retentioneering/retentioneering-tools](https://github.com/retentioneering/retentioneering-tools) | 918 | Python toolkit, MCP server, and agent skills for reproducible, auditable clickstream and event log analytics. Helps AI agents, data scientists and analysts buil… | ✅ |
| [lrjconan/LanczosNetwork](https://github.com/lrjconan/LanczosNetwork) | 317 | Lanczos Network, Graph Neural Networks, Deep Graph Convolutional Networks, Deep Learning on Graph Structured Data, QM8 Quantum Chemistry Benchmark, ICLR 2019 | ✅ |
| [thuijskens/bayesian-optimization](https://github.com/thuijskens/bayesian-optimization) | 316 | Python code for bayesian optimization using Gaussian processes | ⚠️ |
| [sayantann11/all-classification-templetes-for-ML](https://github.com/sayantann11/all-classification-templetes-for-ML) | 298 | Classification - Machine Learning This is ‘Classification’ tutorial which is a part of the Machine Learning course offered by Simplilearn. We will learn Classif… | ⚠️ |
| [quantumlib/OpenFermion-Cirq](https://github.com/quantumlib/OpenFermion-Cirq) | 295 | Quantum circuits for simulations of quantum chemistry and materials. | ✅ |
| [zjunlp/Mol-Instructions](https://github.com/zjunlp/Mol-Instructions) | 294 | [ICLR 2024] Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models | ✅ |
| [molyswu/hand_detection](https://github.com/molyswu/hand_detection) | 279 | using Neural Networks (SSD) on Tensorflow.  This repo documents steps and scripts used to train a hand detector using Tensorflow (Object Detection API). As with… | ⚠️ |
| [abusufyanvu/6S191_MIT_DeepLearning](https://github.com/abusufyanvu/6S191_MIT_DeepLearning) | 262 | MIT Introduction to Deep Learning (6.S191) Instructors: Alexander Amini and Ava Soleimany Course Information Summary Prerequisites Schedule Lectures Labs, Final… | ⚠️ |
| [brain-research/mpnn](https://github.com/brain-research/mpnn) | 239 | Open source implementation of "Neural Message Passing for Quantum Chemistry" | ✅ |
| [antarys-ai/python](https://github.com/antarys-ai/python) | 232 | Python client for Antarys vector database, optimized for large-scale vector operations with built-in caching, parallel processing, and dimension validation. | ✅ |
| [MolSSI/QCEngine](https://github.com/MolSSI/QCEngine) | 211 | Quantum chemistry program executor and IO standardizer (QCSchema). | ✅ |
| [MolSSI-BSE/basis_set_exchange](https://github.com/MolSSI-BSE/basis_set_exchange) | 202 | A repository for quantum chemistry basis sets | ✅ |
| [MolSSI/QCElemental](https://github.com/MolSSI/QCElemental) | 201 | Periodic table, physical constants, and molecule parsing for quantum chemistry. | ✅ |
| [relf/EGObox](https://github.com/relf/EGObox) | 184 | Efficient global optimization toolbox in Rust: bayesian optimization, mixture of gaussian processes, sampling methods  | ✅ |
| [truongnmt/multi-task-learning](https://github.com/truongnmt/multi-task-learning) | 179 | Multi-task learning smile detection, age and gender classification on GENKI4k, IMDB-Wiki dataset. | ✅ |
| [MolSSI/QCFractal](https://github.com/MolSSI/QCFractal) | 168 | A distributed compute and database platform for quantum chemistry.  | ✅ |
| [BEAM-Labs/FoldBench](https://github.com/BEAM-Labs/FoldBench) | 150 | FoldBench is a low-homology benchmark spanning proteins, nucleic acids, ligands, and six major interaction types, enabling assessments that were previously infe… | ✅ |
| [SMTG-Bham/ShakeNBreak](https://github.com/SMTG-Bham/ShakeNBreak) | 131 | Defect structure-searching employing chemically-guided bond distortions | ✅ |
| [ifding/graph-neural-networks](https://github.com/ifding/graph-neural-networks) | 131 | Graph Neural Networks for Quantum Chemistry | ⚠️ |
| [zaixizhang/MGSSL](https://github.com/zaixizhang/MGSSL) | 129 | Official implementation of NeurIPS'21 paper"Motif-based Graph Self-Supervised Learning for Molecular Property Prediction" | ✅ |
| [diffqc/dqc](https://github.com/diffqc/dqc) | 123 | Differentiable Quantum Chemistry (only Differentiable Density Functional Theory and Hartree Fock at the moment) | ✅ |
| [OneSavieLabs/Bastet](https://github.com/OneSavieLabs/Bastet) | 122 | Bastet is a comprehensive dataset of common smart contract vulnerabilities in DeFi along with an AI-driven automated detection process to enhance vulnerability … | ✅ |
| [XanaduAI/GradDFT](https://github.com/XanaduAI/GradDFT) | 113 | GradDFT is a JAX-based library enabling the differentiable design and experimentation of exchange-correlation functionals using machine learning techniques. | ✅ |
| [RuiShu/nn-bayesian-optimization](https://github.com/RuiShu/nn-bayesian-optimization) | 108 | We use a modified neural network instead of Gaussian process for Bayesian optimization. | ✅ |
| [MolSSI/QCSchema](https://github.com/MolSSI/QCSchema) | 106 | A Schema for Quantum Chemistry | ✅ |
| [google-research/hyperbo](https://github.com/google-research/hyperbo) | 105 | Pre-trained Gaussian processes for Bayesian optimization | ✅ |
| [mala-project/mala](https://github.com/mala-project/mala) | 101 | Materials Learning Algorithms. A framework for machine learning materials properties from first-principles data. | ✅ |
| [DS4SD/MolGrapher](https://github.com/DS4SD/MolGrapher) | 100 | [ICCV 23] MolGrapher: Graph-based Visual Recognition of Chemical Structures | ✅ |
| [polizzilab/LASErMPNN](https://github.com/polizzilab/LASErMPNN) | 87 | All-Atom (Including Hydrogen!) Ligand-Conditioned Protein Sequence Design & Sidechain Packing GNN | ✅ |
| [hongyehu/PyClifford](https://github.com/hongyehu/PyClifford) | 86 | An intuitive programming package for simulating and analyzing Clifford-dominated circuits, quantum measurement, and stabilizer states with applications to many-… | ✅ |
| [shuaigroup/Renormalizer](https://github.com/shuaigroup/Renormalizer) | 77 | Quantum dynamics package based on tensor network states | ✅ |
| [DS4SD/PatCID](https://github.com/DS4SD/PatCID) | 74 | [Nat. Commun.] PatCID: an open-access dataset of chemical structures in patent documents | ✅ |
| [fiquant/marketsimulator](https://github.com/fiquant/marketsimulator) | 73 | The project simulates a generic agent based	market model. The aim is to explore intimately, by simulation, the process of price formation and the market microst… | ⚠️ |
| [Merck/matcher](https://github.com/Merck/matcher) | 71 | Matcher is a tool for understanding how chemical structure optimization problems have been solved. Matcher enables deep control over searching structure/activit… | ✅ |
| [rigetti/forest-openfermion](https://github.com/rigetti/forest-openfermion) | 71 | OpenFermion quantum chemistry plugin for @rigetti Forest. | ✅ |
| [ChiCheng45/Gaussium](https://github.com/ChiCheng45/Gaussium) | 69 | A Quantum Chemistry program written in Python 3 supporting RHF, UHF, TDHF, CIS, MP2, DFT, CCSD and CCSD(T) methods. | ⚠️ |
| [davpoolechem/JuliaChem.jl](https://github.com/davpoolechem/JuliaChem.jl) | 68 | A research-grade quantum chemistry program written in Julia | ✅ |
| [CrawfordGroup/pycc](https://github.com/CrawfordGroup/pycc) | 68 | PyCC is a simple, Python-based, reference implementation of the coupled cluster method of ab initio quantum chemistry. | ✅ |
| [manhph2211/ViOCR](https://github.com/manhph2211/ViOCR) | 66 | This is our solution dealing with BKAI challenge :smile:  | ⚠️ |
| [Kohulan/ChemAudit](https://github.com/Kohulan/ChemAudit) | 64 | ChemAudit helps researchers validate, standardize, and assess the quality of chemical structures before using them in machine learning models or chemical databa… | ✅ |
| [theochem/ModelHamiltonian](https://github.com/theochem/ModelHamiltonian) | 61 | Generate 1- and 2-electron integrals so that molecular quantum chemistry software can be used for model Hamiltonians. | ✅ |
| [Liu-group/AutoSolvate](https://github.com/Liu-group/AutoSolvate) | 58 | Automated workflow for generating quantum chemistry calculation of explicitly solvated molecules | ✅ |
| [aqreed/solarpy](https://github.com/aqreed/solarpy) | 58 | Solar radiation model for flight dynamics. Based on Duffie & Beckman "Solar energy thermal processes" (1974) | ✅ |
| [fevangelista/Course-QuantumChemistryLab](https://github.com/fevangelista/Course-QuantumChemistryLab) | 57 | Course material for an undergraduate quantum chemistry lab class | ⚠️ |
| [alan-turing-institute/mogp-emulator](https://github.com/alan-turing-institute/mogp-emulator) | 55 | Package for fitting Gaussian Process Emulators to multiple output computer simulation results. | ✅ |
| [jeanwsr/awesome-qc-courses](https://github.com/jeanwsr/awesome-qc-courses) | 54 | Quantum Chemistry course resources available on github and other platforms | ⚠️ |
| [VincentGranville/Point-Processes](https://github.com/VincentGranville/Point-Processes) | 54 | This repository contains the material (datasets, code, videos, spreadsheets) related to my book Stochastic Processes and Simulations - A Machine Learning Perspe… | ⚠️ |
| [reymond-group/CASP-and-dataset-performance](https://github.com/reymond-group/CASP-and-dataset-performance) | 49 | Source code and documentation of a computer assisted synthesis planning (CASP) tool used for the analysis of reaction datasets. | ✅ |
| [qmatter-labs/symmer](https://github.com/qmatter-labs/symmer) | 48 | An efficient Python-based framework for implementing qubit subspace methods, reducing the resource requirements for near-term quantum simulations. | ✅ |
| [tomdbar/naqs-for-quantum-chemistry](https://github.com/tomdbar/naqs-for-quantum-chemistry) | 46 | Supporting code for "Autoregressive neural-network wavefunctions for ab initio quantum chemistry". | ✅ |
| [lowdanie/hartree-fock-solver](https://github.com/lowdanie/hartree-fock-solver) | 44 | A quantum chemisty library in jax. | ✅ |
| [ecust-hc/ScaffoldGVAE](https://github.com/ecust-hc/ScaffoldGVAE) | 44 | ScaffoldGVAE: A Variational Autoencoder Based on Multi-View Graph Neural Networks for Scaffold Generation and Scaffold Hopping of Drug Molecules | ✅ |
| [Lzcstan/DrugLAMP](https://github.com/Lzcstan/DrugLAMP) | 42 | A PyTorch-based system for highly accurate drug-target interaction predictions utilizing multi-modal large language models to discern structural affinities in d… | ⚠️ |
| [HySonLab/Protein_Redesign](https://github.com/HySonLab/Protein_Redesign) | 40 | ProteinReDiff: Complex-based ligand-binding proteins redesign by equivariant diffusion-based generative models | ✅ |
| [pyvandenbussche/transformers-ner](https://github.com/pyvandenbussche/transformers-ner) | 40 | Experiment on NER task using Huggingface state-of-the-art Transformers Natural Language Models library | ✅ |
| [AstraZeneca/StarGazer](https://github.com/AstraZeneca/StarGazer) | 40 | StarGazer is a tool designed for rapidly assessing drug repositioning opportunities. It combines multi-source, multi-omics data with a novel target prioritizati… | ✅ |
| [Frank-LIU-520/DeepMoleNet](https://github.com/Frank-LIU-520/DeepMoleNet) | 39 | Deep learning for molecules quantum chemistry properties prediction | ✅ |
| [masa-ue/SVDD](https://github.com/masa-ue/SVDD) | 39 | Derivative-Free Guidance in Diffusion Models with Soft Value-Based Decoding. For controlled generation in DNA, RNA, proteins, molecules (+ images)  | ⚠️ |
| [Hwoo-Kim/DeepBioisostere](https://github.com/Hwoo-Kim/DeepBioisostere) | 38 | Deep Learning-based Bioisosteric Replacements for Optimization of Multiple Molecular Properties | ✅ |
| [GQCG/GQCP](https://github.com/GQCG/GQCP) | 37 | The Ghent Quantum Chemistry Package for electronic structure calculations | ✅ |
| [LCY02/ABT-MPNN](https://github.com/LCY02/ABT-MPNN) | 37 | An atom-bond transformer-based message passing neural network for molecular property prediction. | ✅ |
| [HeewoongNoh/Retrieval-Retro](https://github.com/HeewoongNoh/Retrieval-Retro) | 37 | The official source code for [2024 NeurIPS] "Retrieval-Retro: Retrieval-based Inorganic Retrosynthesis with Expert Knowledge" | ⚠️ |
| [robashaw/basisopt](https://github.com/robashaw/basisopt) | 36 | Basis set optimization library for quantum chemistry | ✅ |
| [JieZheng-ShanghaiTech/KG4SL](https://github.com/JieZheng-ShanghaiTech/KG4SL) | 35 | Synthetic lethality (SL) is a promising gold mine for the discovery of anti-cancer drug targets. KG4SL is the first graph neural network (GNN)-based model that … | ✅ |
| [coleygroup/rxn-ebm](https://github.com/coleygroup/rxn-ebm) | 34 | Energy-based modeling of chemical reactions | ✅ |
| [ajz34/PyCrawfordProgProj](https://github.com/ajz34/PyCrawfordProgProj) | 33 | Crawford's Quantum Chemistry Exercises by Python approach | ✅ |
| [sirmarcel/cmlkit](https://github.com/sirmarcel/cmlkit) | 33 | tools for machine learning in condensed matter physics and quantum chemistry | ✅ |
| [kilicogluh/lbd-covid](https://github.com/kilicogluh/lbd-covid) | 32 | Drug repurposing for COVID-19 using literature-based discovery | ⚠️ |
| [anny0316/Drug3D-Net](https://github.com/anny0316/Drug3D-Net) | 32 | A Spatial-temporal Gated Attention Module for Molecular Property Prediction Based on Molecular Geometry | ✅ |
| [MedicineBiology-AI/EEG-DTI](https://github.com/MedicineBiology-AI/EEG-DTI) | 31 | An end-to-end heterogeneous graph representation learning-based framework for drug-target interaction prediction | ⚠️ |
| [wzxxxx/Knowledge-based-BERT](https://github.com/wzxxxx/Knowledge-based-BERT) | 31 | K-BERT for molecular property prediction. | ⚠️ |
| [azaz9026/Medicine-Recommendation-System](https://github.com/azaz9026/Medicine-Recommendation-System) | 30 | A Medicine Recommendation System in machine learning (ML) is a software application designed to assist healthcare professionals and patients in selecting the mo… | ⚠️ |
| [pyscf/properties](https://github.com/pyscf/properties) | 29 | Molecular and crystal electromagnetic properties | ✅ |
| [patonlab/Sterimol](https://github.com/patonlab/Sterimol) | 28 | Calculate Sterimol Parameters from Sructure Input/Output Files | ✅ |
| [sandbox-quantum/Tangelo-Examples](https://github.com/sandbox-quantum/Tangelo-Examples) | 28 | Tutorial notebooks and example scripts made with Tangelo. Any Tangelo user can suggest content and  showcase their work, either by pushing on this repo or linki… | ✅ |
| [MihailBogojeski/ml-dft](https://github.com/MihailBogojeski/ml-dft) | 28 | A package for density functional approximation using machine learning. | ✅ |
| [MahaThafar/Drug-Target-Interaction-Prediciton-Method](https://github.com/MahaThafar/Drug-Target-Interaction-Prediciton-Method) | 27 | This repository provides an implementation of the DTiGEMSplus tool, a network-based method for computational Drug-Target Interaction prediction using graph embe… | ⚠️ |
| [rajkstats/PharmAssistAI](https://github.com/rajkstats/PharmAssistAI) | 26 | An innovative application designed to help pharmacists and pharmacy students quickly research FDA-approved drugs by retrieving relevant information from drug la… | ⚠️ |
| [SUSYUSTC/stc_qc_paper](https://github.com/SUSYUSTC/stc_qc_paper) | 25 | Repo for paper: stochastic tensor contraction for quantum chemistry | ✅ |
| [fork123aniket/Molecule-Graph-Generation](https://github.com/fork123aniket/Molecule-Graph-Generation) | 25 | Molecule Graph Generation using Graph Convolutional Networks-based Variational Graph AutoEncoders (VGAE) in PyTorch | ✅ |
| [sciai-lab/structures25](https://github.com/sciai-lab/structures25) | 25 | STRUCTURES25 - Machine-learning OF-DFT implementation using equivariant graph neural networks (JACS 2025). | ✅ |
| [RamAIbot/Womanium-Quantum-Drug-Discovery](https://github.com/RamAIbot/Womanium-Quantum-Drug-Discovery) | 23 | The project outlines using Bioinformatics, AI and Quantum Machine Learning to find Acetylcholinesterase (AChE) inhibitors as targets in Alzheimer’s disease (AD)… | ⚠️ |
| [jingxuyy/PDATC-NCPMKL](https://github.com/jingxuyy/PDATC-NCPMKL) | 23 | PDATC-NCPMKL: Predicting drug鈥檚 Anatomical Therapeutic Chemical (ATC) codes based on network consistency projection and multiple kernel learning In this study, … | ⚠️ |
| [phanisaikamal/Smart-Augmented-Glasses-Hackthon-4.0-](https://github.com/phanisaikamal/Smart-Augmented-Glasses-Hackthon-4.0-) | 21 | Smart Glasses for Police Force, a wearable augmented reality glasses with applications in security, medical and industrial field applications such as remote mon… | ⚠️ |
| [HICAI-ZJU/GS-Meta](https://github.com/HICAI-ZJU/GS-Meta) | 20 | Code and Data for the paper: Graph Sampling-based Meta-Learning for Molecular Property Prediction [IJCAI2023] | ✅ |
| [GONGSHUKAI/USPTO_LLM](https://github.com/GONGSHUKAI/USPTO_LLM) | 20 | [WWW 25] USPTO-LLM: A Large Language Model-Assisted Information-enriched Chemical Reaction Dataset | ✅ |
| [CalebBell/chemical-metadata](https://github.com/CalebBell/chemical-metadata) | 20 | Project to create a curated chemical metadata (structures, names, synonyms, formulas) database under git revision control based on existing databases with minim… | ✅ |
| [saramasarone/enrich_omics](https://github.com/saramasarone/enrich_omics) | 20 | A python package to explore pathways, diseases and drugs associated to a list of targets (genes, proteins, etc) | ✅ |
| [OdinZhang/ECloudGen_old](https://github.com/OdinZhang/ECloudGen_old) | 19 | ECloudGen: Leverage Quantum Physics to Scale Chemical Space for Structure-based Molecular Design | ⚠️ |
| [1JELC1/DFT-ChemDescriptors](https://github.com/1JELC1/DFT-ChemDescriptors) | 19 | A comprehensive tool that automates the extraction of global and local cDFT descriptors using Multiwfn. | ✅ |
| [MrZQAQ/MCANet](https://github.com/MrZQAQ/MCANet) | 17 | Source code of paper: "MCANet: Shared-weight-based MultiheadCrossAttention network for drug-target interaction prediction" | ✅ |
| [deepmodeling/dftio](https://github.com/deepmodeling/dftio) | 16 | dftio is to assist machine learning communities to transcript DFT output into a format that is easy to read or used by machine learning models. | ✅ |
| [DS4SD/MolDepictor](https://github.com/DS4SD/MolDepictor) | 16 | [ICCV 23] MolGrapher: Graph-based Visual Recognition of Chemical Structures | ✅ |
| [DrrDom/spci](https://github.com/DrrDom/spci) | 16 | Tool for mining structure-property relationships from chemical datasets | ⚠️ |
| [mengmeng34/GraphormerDTI](https://github.com/mengmeng34/GraphormerDTI) | 16 | A graph transformer-based approach for drug-target interaction prediction | ⚠️ |
| [rxn4chemistry/rxn-reaction-preprocessing](https://github.com/rxn4chemistry/rxn-reaction-preprocessing) | 16 | Preprocessing of datasets of chemical reactions: standardization, filtering, augmentation, tokenization, etc. | ✅ |
| [Satya3720/Rock-Identification-Using-Deep-Convolution-Neural-Network](https://github.com/Satya3720/Rock-Identification-Using-Deep-Convolution-Neural-Network) | 16 | Rocks are a fundamental component of Earth. The automatic identification of rock type in the field would aid geological surveying, education, and automatic mapp… | ⚠️ |
| [zhichunguo/GraSeq](https://github.com/zhichunguo/GraSeq) | 15 | GraSeq: Graph and Sequence Fusion Learning for Molecular Property Prediction. In CIKM 2020. | ⚠️ |
| [ML4BM-Lab/GeNNius](https://github.com/ML4BM-Lab/GeNNius) | 15 | GeNNius: An ultrafast drug-target interaction inference method based on graph neural networks | ✅ |
| [NSLab-CUK/S-CGIB](https://github.com/NSLab-CUK/S-CGIB) | 15 | Subgraph-conditioned Graph Information Bottleneck (S-CGIB) is a novel architecture for pre-training Graph Neural Networks in molecular property prediction and d… | ✅ |
| [ohuelab/npgpt](https://github.com/ohuelab/npgpt) | 15 | NPGPT: Natural Product-Like Compound Generation with GPT-based Chemical Language Models | ✅ |
| [duaibeom/chemOCR](https://github.com/duaibeom/chemOCR) | 15 | DB-based Optical Chemical Structure Recognition | ✅ |
| [arhamshah/SolubilityPrediction](https://github.com/arhamshah/SolubilityPrediction) | 14 | A web based application predicts water solubility of any given chemical compound known or unknown | ⚠️ |
| [GenSI-THUAIR/Retro-R1](https://github.com/GenSI-THUAIR/Retro-R1) | 14 | Implementation for NeurIPS 2025 paper "Retro-R1: LLM-based Agentic Retrosynthesis" | ✅ |
| [emadalibrahim/Fusion-Cycle](https://github.com/emadalibrahim/Fusion-Cycle) | 14 | Solubility calculation based on enthalpy of fusion, melting point, and activity coefficient predictions. | ⚠️ |
| [chao1224/SGNN-EBM](https://github.com/chao1224/SGNN-EBM) | 14 | Structured Multi-task Learning for Molecular Property Prediction, AISTATS'22 (https://proceedings.mlr.press/v151/liu22e.html) | ✅ |
| [julschleinitz/NiCOlit](https://github.com/julschleinitz/NiCOlit) | 14 | Repository for the featurization of the NiCOlit reaction dataset and machine learning model training for yield prediction | ✅ |
| [jules-leguy/BBOMol](https://github.com/jules-leguy/BBOMol) | 14 | Surrogate-based black-box optimization method for molecular properties | ✅ |

---

## 化学信息学 cheminformatics  <a id="cheminformatics"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [PatWalters/practical_cheminformatics_tutorials](https://github.com/PatWalters/practical_cheminformatics_tutorials) | 1305 | Practical Cheminformatics Tutorials | ✅ |
| [lightaime/deep_gcns_torch](https://github.com/lightaime/deep_gcns_torch) | 1187 | Pytorch Repo for DeepGCNs (ICCV'2019 Oral, TPAMI'2021), DeeperGCN (arXiv'2020) and GNN1000(ICML'2021): https://www.deepgcns.org | ✅ |
| [MolecularAI/aizynthfinder](https://github.com/MolecularAI/aizynthfinder) | 888 | A tool for retrosynthetic planning | ✅ |
| [awslabs/dgl-lifesci](https://github.com/awslabs/dgl-lifesci) | 809 | Python package for graph neural networks in chemistry and biology | ✅ |
| [LPDI-EPFL/masif](https://github.com/LPDI-EPFL/masif) | 774 | MaSIF- Molecular surface interaction fingerprints. Geometric deep learning to decipher patterns in molecular surfaces. | ✅ |
| [wengong-jin/icml18-jtnn](https://github.com/wengong-jin/icml18-jtnn) | 566 | Junction Tree Variational Autoencoder for Molecular Graph Generation (ICML 2018) | ✅ |
| [datamol-io/datamol](https://github.com/datamol-io/datamol) | 548 | Molecular Processing Made Easy. | ✅ |
| [mcs07/PubChemPy](https://github.com/mcs07/PubChemPy) | 514 | Python wrapper for the PubChem PUG REST API. | ✅ |
| [wengong-jin/hgraph2graph](https://github.com/wengong-jin/hgraph2graph) | 444 | Hierarchical Generation of Molecular Graphs using Structural Motifs | ✅ |
| [experimental-design/bofire](https://github.com/experimental-design/bofire) | 408 | Experimental design and (multi-objective) bayesian optimization. | ✅ |
| [MLCIL/scikit-fingerprints](https://github.com/MLCIL/scikit-fingerprints) | 392 | Scikit-learn compatible library for molecular fingerprints and chemoinformatics | ✅ |
| [rxn4chemistry/rxnmapper](https://github.com/rxn4chemistry/rxnmapper) | 382 | RXNMapper: Unsupervised attention-guided atom-mapping. Code complementing our Science Advances publication on "Extraction of organic chemistry grammar from unsu… | ✅ |
| [MolecularAI/Reinvent](https://github.com/MolecularAI/Reinvent) | 377 | （无简介） | ✅ |
| [qinheming/BIoClaw](https://github.com/qinheming/BIoClaw) | 376 | （无简介） | ✅ |
| [microsoft/molecule-generation](https://github.com/microsoft/molecule-generation) | 328 | Implementation of MoLeR: a generative model of molecular graphs which supports scaffold-constrained generation | ✅ |
| [AtomFlow-AI/MoleCode](https://github.com/AtomFlow-AI/MoleCode) | 299 | Molecode presents molecules as code and enables LLMs to operate and reason on chemistry directly. | ✅ |
| [samoturk/mol2vec](https://github.com/samoturk/mol2vec) | 293 | Mol2vec - an unsupervised machine learning approach to learn vector representations of molecular substructures | ✅ |
| [whyzhow/Kaggle-NeurIPS---Open-Polymer-Prediction-2025-Silver-Algorithm-Overview](https://github.com/whyzhow/Kaggle-NeurIPS---Open-Polymer-Prediction-2025-Silver-Algorithm-Overview) | 292 | An improved and reproducible implementation of a Silver Medal Kaggle NeurIPS Open Polymer Prediction solution, featuring SMILES canonicalization, molecular desc… | ⚠️ |
| [wjm41/molplotly](https://github.com/wjm41/molplotly) | 263 | add-on to plotly which show molecule images on mouseover! | ✅ |
| [cbouy/mols2grid](https://github.com/cbouy/mols2grid) | 257 | Interactive molecule viewer for 2D structures | ✅ |
| [EBjerrum/SMILES-enumeration](https://github.com/EBjerrum/SMILES-enumeration) | 249 | SMILES enumeration for QSAR modelling using LSTM recurrent neural networks | ✅ |
| [ecrl/padelpy](https://github.com/ecrl/padelpy) | 233 | Python API for PaDEL-Descriptor molecular descriptor and fingerprint calculation | ✅ |
| [XinhaoLi74/SmilesPE](https://github.com/XinhaoLi74/SmilesPE) | 225 | SMILES Pair Encoding: A data-driven substructure representation of chemicals | ✅ |
| [matteoferla/Fragmenstein](https://github.com/matteoferla/Fragmenstein) | 207 | Merging, linking and placing compounds by stitching bound compounds together like a reanimated corpse | ✅ |
| [UCLCheminformatics/ScaffoldGraph](https://github.com/UCLCheminformatics/ScaffoldGraph) | 202 | ScaffoldGraph is an open-source cheminformatics library, built using RDKit and NetworkX, for the generation and analysis of scaffold networks and scaffold trees… | ✅ |
| [patrickfuller/blender-chemicals](https://github.com/patrickfuller/blender-chemicals) | 200 | Draws chemicals in Blender using common input formats (smiles, molfiles, cif files, etc.) | ✅ |
| [isayevlab/Auto3D_pkg](https://github.com/isayevlab/Auto3D_pkg) | 196 | Auto3D generates low-energy conformers from SMILES/SDF | ✅ |
| [mcs07/MolVS](https://github.com/mcs07/MolVS) | 188 | Molecule Validation and Standardization | ✅ |
| [MolecularAI/ReinventCommunity](https://github.com/MolecularAI/ReinventCommunity) | 180 | （无简介） | ✅ |
| [HFooladi/GNNs-For-Chemists](https://github.com/HFooladi/GNNs-For-Chemists) | 179 | Implementations of different GNNs from scratch for chemists | ✅ |
| [chembl/FPSim2](https://github.com/chembl/FPSim2) | 176 | Simple package for fast molecular similarity searches | ✅ |
| [Global-Chem/global-chem](https://github.com/Global-Chem/global-chem) | 174 | A Knowledge Graph of Common Chemical Names to their Molecular Definition | ✅ |
| [pckroon/pysmiles](https://github.com/pckroon/pysmiles) | 164 | A lightweight python-only library for reading and writing SMILES strings | ✅ |
| [mcsorkun/ChemPlot](https://github.com/mcsorkun/ChemPlot) | 155 | A python package for chemical space visualization. | ✅ |
| [baoilleach/deepsmiles](https://github.com/baoilleach/deepsmiles) | 146 | DeepSMILES - A variant of SMILES for use in machine-learning | ✅ |
| [keiserlab/e3fp](https://github.com/keiserlab/e3fp) | 144 | 3D molecular fingerprints  | ✅ |
| [kuelumbus/rdkit-pypi](https://github.com/kuelumbus/rdkit-pypi) | 138 | 鈿涳笍 RDKit Python Wheels on PyPI. 馃捇 pip install rdkit | ✅ |
| [mcs07/CIRpy](https://github.com/mcs07/CIRpy) | 137 | Python wrapper for the NCI Chemical Identifier Resolver (CIR) | ✅ |
| [mqcomplab/bitbirch](https://github.com/mqcomplab/bitbirch) | 132 | BitBIRCH clustering algorithm | ✅ |
| [gadsbyfly/PyBioMed](https://github.com/gadsbyfly/PyBioMed) | 122 | machine learning, molecular descriptor | ✅ |
| [HUBioDataLab/SELFormer](https://github.com/HUBioDataLab/SELFormer) | 117 | SELFormer: Molecular Representation Learning via SELFIES Language Models | ⚠️ |
| [volkamerlab/opencadd](https://github.com/volkamerlab/opencadd) | 111 | A Python library for structural cheminformatics | ✅ |
| [reymond-group/mhfp](https://github.com/reymond-group/mhfp) | 98 | Molecular MHFP fingerprints for cheminformatics applications | ✅ |
| [CDDLeiden/QSPRpred](https://github.com/CDDLeiden/QSPRpred) | 95 | A tool for creating Quantitative Structure Property/Activity Relationship (QSPR/QSAR) models. | ✅ |
| [undeadpixel/reinvent-randomized](https://github.com/undeadpixel/reinvent-randomized) | 93 | Recurrent Neural Network using randomized SMILES strings to generate molecules | ✅ |
| [cinfony/cinfony](https://github.com/cinfony/cinfony) | 89 | Simplified and standard interface to a number of cheminformatics toolkits | ✅ |
| [mcocdawc/chemcoord](https://github.com/mcocdawc/chemcoord) | 88 | A python module for manipulating cartesian and internal coordinates. | ✅ |
| [coleygroup/Graph2SMILES](https://github.com/coleygroup/Graph2SMILES) | 71 | （无简介） | ✅ |
| [yangnianzu0515/MoleRec](https://github.com/yangnianzu0515/MoleRec) | 69 | The official implementation of our paper "MoleRec: Combinatorial Drug Recommendation with Substructure-Aware Molecular Representation Learning" (TheWebConf 2023… | ✅ |
| [O-Schilter/Clipboard-to-SMILES-Converter](https://github.com/O-Schilter/Clipboard-to-SMILES-Converter) | 66 | Converts clipboard content to smiles and much more | ✅ |
| [akensert/molgraph](https://github.com/akensert/molgraph) | 65 | Graph neural networks for molecular machine learning: Implemented and compatible with TensorFlow and Keras. | ✅ |
| [crcollins/molml](https://github.com/crcollins/molml) | 62 | A library to interface molecules and machine learning. | ✅ |
| [yvquanli/TrimNet](https://github.com/yvquanli/TrimNet) | 59 | Code for paper "TrimNet: learning molecular representation from triplet messages for biomedicine " | ✅ |
| [Laboratoire-de-Chemoinformatique/SynPlanner](https://github.com/Laboratoire-de-Chemoinformatique/SynPlanner) | 59 | Computer-aided synthesis planning | ✅ |
| [muCommons/NistChemPy](https://github.com/muCommons/NistChemPy) | 57 | Unofficial Python tools for querying NIST Chemistry WebBook pages and extracting molecular-property records. | ✅ |
| [ManzoorElahi/organic-chemistry-reaction-prediction-using-NMT](https://github.com/ManzoorElahi/organic-chemistry-reaction-prediction-using-NMT) | 57 | organic chemistry reaction prediction using NMT with Attention | ⚠️ |
| [dylanwal/chemistry_drawer](https://github.com/dylanwal/chemistry_drawer) | 56 | Draw molecules with plotly! | ✅ |
| [Bibyutatsu/FastJTNNpy3](https://github.com/Bibyutatsu/FastJTNNpy3) | 55 | AI for discovering 100% valid drug like molecules, a combination of VAE-JTNN and bayesian optimization, an optimized Python 3 Version of Junction Tree Variation… | ✅ |
| [graphcore-research/minimol](https://github.com/graphcore-research/minimol) | 51 | MiniMol is a 10M-parameters molecular fingerprinting model pre-trained on >3300 biological and quantum tasks  | ✅ |
| [rnepal2/Solubility-Prediction-with-Graph-Neural-Networks](https://github.com/rnepal2/Solubility-Prediction-with-Graph-Neural-Networks) | 50 | GNN, GCN, Molecular Solubility, RDKit, Cheminformatics | ✅ |
| [BiomedSciAI/biomed-multi-view](https://github.com/BiomedSciAI/biomed-multi-view) | 46 | This repository contains the implementation of the Multi-view Molecular Embedding with Late Fusion (MMELON) architecture. MMELON combines molecular representati… | ✅ |
| [simonfqy/PADME](https://github.com/simonfqy/PADME) | 43 | This is the repository containing the source code for my Master's thesis research, about predicting drug-target interaction using deep learning. | ✅ |
| [liugangcode/InfoAlign](https://github.com/liugangcode/InfoAlign) | 43 | The code for "Learning Molecular Representation in a Cell" | ⚠️ |
| [seokhokang/graphvae_approx](https://github.com/seokhokang/graphvae_approx) | 42 | Efficient Learning of Non-Autoregressive Graph Variational Autoencoders for Molecular Graph Generation | ⚠️ |
| [YerevaNN/ChemLactica](https://github.com/YerevaNN/ChemLactica) | 37 | Fine-tuning Galactica and Gemma to operate on SMILES. Integrates into a molecular optimization algorithm. | ✅ |
| [ZhaoningYu1996/HM-GNN](https://github.com/ZhaoningYu1996/HM-GNN) | 37 | Official PyTorch implementation of "Molecular Representation Learning via Heterogeneous Motif Graph Neural Networks" | ⚠️ |
| [hcji/DeepEI](https://github.com/hcji/DeepEI) | 35 | Predicting molecular fingerprint from electron?ionization mass spectrum with deep neural networks | ✅ |
| [ecrl/graphchem](https://github.com/ecrl/graphchem) | 34 | Molecular graph neural networks for predicting chemical properties, with a focus on fuels | ✅ |
| [apahl/mol_frame](https://github.com/apahl/mol_frame) | 34 | Chemical Structure Handling for Pandas DataFrames | ✅ |
| [Ishan-Kumar2/Molecular_VAE_Pytorch](https://github.com/Ishan-Kumar2/Molecular_VAE_Pytorch) | 34 | PyTorch implementation of the paper "Automatic Chemical Design Using a Data-Driven Continuous Representation of Molecules" | ⚠️ |
| [gashawmg/Molecular-fingerprints](https://github.com/gashawmg/Molecular-fingerprints) | 31 | Generate molecular fingerprints using RDKit  | ✅ |
| [fllinares/neural_fingerprints_tf](https://github.com/fllinares/neural_fingerprints_tf) | 30 | A TensorFlow implementation of "Convolutional Networks on Graphs for Learning Molecular Fingerprints". | ⚠️ |
| [hustvl/MolSight](https://github.com/hustvl/MolSight) | 29 | [AAAI 2026] MolSight: Optical Chemical Structure Recognition with SMILES Pretraining, Multi-Granularity Learning and Reinforcement Learning | ✅ |
| [compsciencelab/PromptSMILES](https://github.com/compsciencelab/PromptSMILES) | 28 | Scaffold decoration and fragment linking with chemical language models and RL | ✅ |
| [shuix007/HMGNN](https://github.com/shuix007/HMGNN) | 28 | Heterogeneous Molecular Graph Neural Network | ⚠️ |
| [MarkusFerdinandDablander/QSAR-activity-cliff-experiments](https://github.com/MarkusFerdinandDablander/QSAR-activity-cliff-experiments) | 25 | Exploring QSAR Models for Activity-Cliff Prediction | ✅ |
| [qmlcode/qmllib](https://github.com/qmlcode/qmllib) | 25 | Quantum machine learning (QML) molecular representations and core functions | ✅ |
| [sunshy-1/GDiffRetro](https://github.com/sunshy-1/GDiffRetro) | 24 | [AAAI'25] GDiffRetro: Retrosynthesis Prediction with Dual Graph Enhanced Molecular Representation and Diffusion Generation | ✅ |
| [JelfsMaterialsGroup/stko](https://github.com/JelfsMaterialsGroup/stko) | 24 | A collection of molecular optimisers and property calculators for use with stk. | ✅ |
| [K-Dense-AI/rowan-autosearch](https://github.com/K-Dense-AI/rowan-autosearch) | 23 | Agent-driven molecular optimization over chemical space, using Rowan for property scoring and RDKit for constraint-aware candidate design. | ⚠️ |
| [HICAI-ZJU/iMoLD](https://github.com/HICAI-ZJU/iMoLD) | 23 | Official implementation for Learning Invariant Molecular Representation in Latent Discrete Space (NeurIPS 2023) | ✅ |
| [yikunpku/Atomas](https://github.com/yikunpku/Atomas) | 20 | ICLR 2025: We propose Atomas, a hierarchical molecular representation learning framework that jointly learns representations from SMILES strings and text. We de… | ⚠️ |
| [mldlproject/2021-iCYP-MFE](https://github.com/mldlproject/2021-iCYP-MFE) | 18 | Source code and data of the paper entitled "iCYP-MFE: Identifying Human Cytochrome P450 Inhibitors using Multi-task Learning and Molecular Fingerprint-embedded … | ⚠️ |
| [jiaor17/EPT](https://github.com/jiaor17/EPT) | 18 | [Nature Communications] The implementation for the paper "An equivariant pretrained transformer for unified 3D molecular representation learning" | ⚠️ |
| [MLCIL/benchmarking_molecular_models](https://github.com/MLCIL/benchmarking_molecular_models) | 18 | Code for the article "Benchmarking Pretrained Molecular Embedding Models For Molecular Representation Learning" https://arxiv.org/abs/2508.06199 | ⚠️ |
| [NetPharMedGroup/publication_fingerprint](https://github.com/NetPharMedGroup/publication_fingerprint) | 17 | code for Zagidullin et al 2021 "Comparative analysis of molecular fingerprints in prediction of drug combination effects" | ⚠️ |
| [HongxinXiang/IEM](https://github.com/HongxinXiang/IEM) | 17 | An Image-enhanced Molecular Graph Representation Learning Framework (IJCAI 2024) | ✅ |
| [gmarshall33/Optical-Chemical-Structure-Recognition](https://github.com/gmarshall33/Optical-Chemical-Structure-Recognition) | 16 | Input- hand-drawn image of molecule... Output- SMILES format molecule name | ⚠️ |
| [LUOyk1999/Molecular-homology](https://github.com/LUOyk1999/Molecular-homology) | 16 | [NeurIPS 2023] Implementation of "Improving Self-supervised Molecular Representation Learning using Persistent Homology" | ✅ |
| [keiserlab/e3fp-paper](https://github.com/keiserlab/e3fp-paper) | 15 | 3D molecular fingerprints (E3FP) paper repo | ✅ |
| [yuewan2/MolMCL](https://github.com/yuewan2/MolMCL) | 15 | The official repository for "Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation" | ✅ |
| [darjacvetkovic/HSP-predictions](https://github.com/darjacvetkovic/HSP-predictions) | 14 | XGBoost and GNN training and models for prediction of Hansen solubility parameters | ✅ |
| [MunibaFaiza/cheminformatics](https://github.com/MunibaFaiza/cheminformatics) | 13 | Perform operations on chemical structures using Python. | ✅ |
| [jeffrichardchemistry/molbokeh](https://github.com/jeffrichardchemistry/molbokeh) | 13 | A new python package to visualize molecules in dots hover | ✅ |

---

## 材料信息学 materials  <a id="materials"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [janosh/pymatviz](https://github.com/janosh/pymatviz) | 333 | A toolkit for visualizations in materials informatics. | ✅ |
| [sp8rks/MaterialsInformatics](https://github.com/sp8rks/MaterialsInformatics) | 250 | MSE5540/6640 Materials Informatics course at the University of Utah. Learn how data science tools are revolutionizing materials science! | ✅ |
| [anthony-wang/BestPractices](https://github.com/anthony-wang/BestPractices) | 205 | Things that you should (and should not) do in your Materials Informatics research. | ✅ |
| [hachmannlab/chemml](https://github.com/hachmannlab/chemml) | 180 | ChemML is a machine learning and informatics program suite for the chemical and materials sciences. | ✅ |
| [jiaor17/DiffCSP](https://github.com/jiaor17/DiffCSP) | 179 | [NeurIPS 2023] The implementation for the paper "Crystal Structure Prediction by Joint Equivariant Diffusion" | ✅ |
| [yoshida-lab/XenonPy](https://github.com/yoshida-lab/XenonPy) | 159 | XenonPy is a Python Software for Materials Informatics | ✅ |
| [Tomoki-YAMASHITA/CrySPY](https://github.com/Tomoki-YAMASHITA/CrySPY) | 154 | CrySPY is a crystal structure prediction tool written in Python. | ✅ |
| [argonne-lcf/ChemGraph](https://github.com/argonne-lcf/ChemGraph) | 151 | Agentic framework for computational chemistry and materials science workflows | ✅ |
| [deepmodeling/CrystalFormer](https://github.com/deepmodeling/CrystalFormer) | 151 | A Foundation Model for Crystal Structure Generation and Prediction | ✅ |
| [lrcfmd/ipcsp](https://github.com/lrcfmd/ipcsp) | 48 | Integer Programming encoding for Crystal Structure Prediction with classic and quantum computing bindings | ✅ |
| [szl666/CSLLM](https://github.com/szl666/CSLLM) | 44 | An LLM system for the ultra-accurate (TPR=98.8%) prediction of the synthesizability and precursors of crystal structures | ✅ |
| [nguyen-group/GNNOpt](https://github.com/nguyen-group/GNNOpt) | 34 | Universal Ensemble-Embedding Graph Neural Network for Direct Prediction of Optical Spectra from Crystal Structures | ✅ |
| [the-matter-lab/clari](https://github.com/the-matter-lab/clari) | 34 | Fast Organic Crystal Structure Prediction with Unit Cell Flow Matching | ✅ |
| [EmperorJia/EquiCSP](https://github.com/EmperorJia/EquiCSP) | 31 | Equivariant Diffusion for Crystal Structure Prediction (ICML 2024) | ✅ |
| [BattModels/electrodep](https://github.com/BattModels/electrodep) | 24 | MOOSE Application for simulation of electrodeposition in Li-ion batteries | ✅ |
| [learningmatter-mit/HiTPoly](https://github.com/learningmatter-mit/HiTPoly) | 23 | A platform for setting up high throughput polymer electrolyte MD simulations. | ✅ |
| [atomisticnet/ml-catalysis](https://github.com/atomisticnet/ml-catalysis) | 20 | Machine Learning for Catalysis | ✅ |
| [dembart/intro-to-materials-informatics](https://github.com/dembart/intro-to-materials-informatics) | 20 | Introduction to Materials Informatics course at the Skolkovo Institute of Science and Technology | ✅ |
| [itakigawa/ml-catalysis](https://github.com/itakigawa/ml-catalysis) | 20 | Machine Learning for Catalyst Design and Discovery | ⚠️ |
| [blokhin/materials-informatics-tutorial](https://github.com/blokhin/materials-informatics-tutorial) | 19 | A quick tutorial for modern materials science, should the reader be not familiar with it and just wishing to crack the data | ✅ |
| [tilde-lab/tilde](https://github.com/tilde-lab/tilde) | 18 | Materials informatics framework for ab initio data repositories | ✅ |
| [usccolumbia/cspbenchmark](https://github.com/usccolumbia/cspbenchmark) | 15 | Benchmark of crystal structure prediction algorithms | ✅ |
| [GLAD-RUC/DAO](https://github.com/GLAD-RUC/DAO) | 14 | [Nature Communications] Official code for "Siamese Foundation Models for Crystal Structure Prediction". | ✅ |
| [Teoroo-CMC/GroPoB](https://github.com/Teoroo-CMC/GroPoB) | 14 | Building MD simulations for polymer electrolyte system | ⚠️ |
| [sadmanomee/ParetoCSP](https://github.com/sadmanomee/ParetoCSP) | 13 | Crystal structure prediction using neural network potential and age-fitness Pareto genetic algorithm | ⚠️ |
| [usccolumbia/CSPBenchMetrics](https://github.com/usccolumbia/CSPBenchMetrics) | 13 | Benchmark metrics for crystal structure prediction | ✅ |
| [Liu-Group-UF/MolCrystalFlow](https://github.com/Liu-Group-UF/MolCrystalFlow) | 13 | Molecular Crystal Structure Prediction with Flow Matching | ✅ |
| [learningmatter-mit/atom_by_atom](https://github.com/learningmatter-mit/atom_by_atom) | 12 | Atom-by-atom design of metal oxide catalysts for the oxygen evolution reaction with Machine Learning | ⚠️ |
| [adaptive-intelligent-robotics/QD4CSP](https://github.com/adaptive-intelligent-robotics/QD4CSP) | 12 | Application of MAP-Elites algorithm for crystal structure prediction | ⚠️ |
| [polbeni/PyMCSP](https://github.com/polbeni/PyMCSP) | 12 | A Python and Machine Learning methods implementation for Crystal Structure Prediction and Diffraction Study | ✅ |
| [Tosykie/CrySPR](https://github.com/Tosykie/CrySPR) | 11 | A Python interface for implementation of crystal structure pre-relaxation and prediction using machine-learning inter-atomic potentials. | ✅ |
| [atomisticnet/gibbsml](https://github.com/atomisticnet/gibbsml) | 10 | Prediction of reaction free energies with machine learning | ✅ |
| [jol-jol/neural-network-design-of-HEA](https://github.com/jol-jol/neural-network-design-of-HEA) | 9 | This is the repository of the code and data needed for reproducing the results of the paper "Neural Network-Assisted Development of High-Entropy Alloy Catalysts… | ⚠️ |
| [frcnt/om-diff](https://github.com/frcnt/om-diff) | 9 | OM-Diff: Inverse-design of organometallic catalysts with guided equivariant denoising diffusion | ✅ |
| [ai-naymul/ATS-Catalyst](https://github.com/ai-naymul/ATS-Catalyst) | 9 | ATS Catalyst is an innovative platform designed to empower job seekers and streamline the hiring process. Leveraging advanced AI technologies, our suite of tool… | ⚠️ |
| [TsumiNa/ShotgunCSP](https://github.com/TsumiNa/ShotgunCSP) | 9 | A Python package designed to solve the crystal structure prediction (CSP) problem using a non-iterative, single-shot screening framework. | ✅ |
| [MaterSim/HTOCSP](https://github.com/MaterSim/HTOCSP) | 8 | A public framework for automated High-throughput Organic Crystal Structure Prediction | ✅ |
| [ohuelab/CatDRX](https://github.com/ohuelab/CatDRX) | 8 | CatDRX: Reaction-Conditioned Generative Model for Catalyst Design and Optimization | ✅ |
| [catalystforyou/RetroRanker](https://github.com/catalystforyou/RetroRanker) | 7 | RetroRanker, a ranking model built upon the graph neural network to mitigate the frequency bias in predictions of existing retrosynthesis models through re-rank… | ⚠️ |
| [timcrose/Genarris](https://github.com/timcrose/Genarris) | 7 | Generation of molecular crystal structures and robust workflows for polymorph prediction | ✅ |
| [nkuhuxu/eNRRCrew](https://github.com/nkuhuxu/eNRRCrew) | 6 | eNRRCrew: Accelerating eNRR catalyst Design through Multi-Agent Collaboration and Automated Structure-Activity Analysis | ✅ |
| [Materials-Informatics-Laboratory/Catalyst](https://github.com/Materials-Informatics-Laboratory/Catalyst) | 6 | Generalized machine learning training and analysis software. Designed for atomistic simulations, applicable everywhere.  | ✅ |
| [tldr-group/2ManyScales](https://github.com/tldr-group/2ManyScales) | 5 | Simulation of 1D electrolyte system using PyBaMM framework | ⚠️ |
| [shyuep/miworkshop](https://github.com/shyuep/miworkshop) | 5 | Materials for Workshop on Materials Informatics | ✅ |
| [pwvbutler/CSP-AL](https://github.com/pwvbutler/CSP-AL) | 4 | Implementation of active learning strategies for training machine learned potentials, primarily intended for use with crystal structure prediction data | ✅ |
| [zzz-sl/ESNet](https://github.com/zzz-sl/ESNet) | 4 | ESNet: A Dual-Modal Joint Framework of Elemental Composition and Crystal Structure for Material Properties Prediction | ✅ |
| [tccdem/PNcsp](https://github.com/tccdem/PNcsp) | 4 | Crystal structure prediction via similarity in the Mendeleev's Periodic Number representation | ⚠️ |
| [zhubonan/disp](https://github.com/zhubonan/disp) | 4 | Distribute and manage crystal structure prediction workloads | ✅ |
| [Long1Corn/Complex_Gen](https://github.com/Long1Corn/Complex_Gen) | 4 | Complex_Gen for transition metal homogeneous catalyst design | ✅ |
| [nim-hrkn/mi_knime_tutorial](https://github.com/nim-hrkn/mi_knime_tutorial) | 3 | materials informatics tutorial with KNIME | ✅ |
| [WardLT/ternary-semiconductors-mhm](https://github.com/WardLT/ternary-semiconductors-mhm) | 3 | Scripts from a paper on discovering ternary semiconductors with machine learning and crystal structure prediction | ⚠️ |
| [aaburakhia/polymer-property-prediction](https://github.com/aaburakhia/polymer-property-prediction) | 3 | A Materials Informatics project to predict key polymer properties using XGBoost. Includes an end-to-end MLOps pipeline and a live interactive demo deployed on H… | ✅ |

---

## 化学工程 chem-eng  <a id="chemeng"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [oemof/tespy](https://github.com/oemof/tespy) | 412 | Thermal Engineering Systems in Python (TESPy). This package provides a powerful simulation toolkit for thermodynamic modeling of thermal engineering plants such… | ✅ |
| [CalebBell/ht](https://github.com/CalebBell/ht) | 250 |  Heat transfer component of Chemical Engineering Design Library (ChEDL) | ✅ |
| [wigging/chemics](https://github.com/wigging/chemics) | 209 | A Python package for chemical engineering | ✅ |
| [jckantor/CBE20255](https://github.com/jckantor/CBE20255) | 198 | Introduction to Chemical Engineering Analysis | ✅ |
| [edgarsmdn/MLCE_book](https://github.com/edgarsmdn/MLCE_book) | 134 | Hands-on material for a Machine Learning in Chemical Engineering course | ✅ |
| [ReactionMechanismGenerator/ReactionMechanismSimulator.jl](https://github.com/ReactionMechanismGenerator/ReactionMechanismSimulator.jl) | 95 | The amazing Reaction Mechanism Simulator for simulating large chemical kinetic mechanisms | ✅ |
| [kyleniemeyer/computational-thermo](https://github.com/kyleniemeyer/computational-thermo) | 76 | This is a collection of examples in computational thermodynamics. | ✅ |
| [hkaneko1985/dcekit](https://github.com/hkaneko1985/dcekit) | 75 | DCEKit (Data Chemical Engineering toolKit) | ✅ |
| [portyanikhin/pyfluids](https://github.com/portyanikhin/pyfluids) | 69 | CoolProp wrapper for Python | ✅ |
| [amvro23/essentials-ChEng](https://github.com/amvro23/essentials-ChEng) | 57 | A repository with examples on essential knowledge of chemical engineering.  | ✅ |
| [lollcat/DistillationTrain-Gym](https://github.com/lollcat/DistillationTrain-Gym) | 44 | Deep reinforcement learning for design of distillation column trains (chemical engineering process synthesis) | ⚠️ |
| [lollcat/RL-Process-Design](https://github.com/lollcat/RL-Process-Design) | 41 | Deep reinforcement learning for design of chemical engineering processes | ⚠️ |
| [emedd33/Reinforcement-Learning-in-Process-Control](https://github.com/emedd33/Reinforcement-Learning-in-Process-Control) | 39 | Master thesis spring 2019. Template to be futher used by the department of chemical engineering at NTNU,  | ✅ |
| [jonathanxavier/sim42](https://github.com/jonathanxavier/sim42) | 39 | Simulator42 is an open source process simulator project with the goal of providing an affordable and accessible chemical process simulator to the chemical engin… | ⚠️ |
| [ipqa-research/ugropy](https://github.com/ipqa-research/ugropy) | 36 | A Python library designed to swiftly and effortlessly obtain the UNIFAC-like groups from molecules by their names and subsequently integrate them into inputs fo… | ✅ |
| [jon85p/pyENL](https://github.com/jon85p/pyENL) | 32 | Cross-platform engineering nonlinear equations systems solver [Under construction ??] | ✅ |
| [emelborp/Process-Identification-and-PID-Tuning-with-Deep-Learning](https://github.com/emelborp/Process-Identification-and-PID-Tuning-with-Deep-Learning) | 30 | A program that can do Process Identification and PID Tuning by using Deep Learning designed for people studying and researching chemical engineering. | ⚠️ |
| [pycalphad/scheil](https://github.com/pycalphad/scheil) | 30 | A Scheil-Gulliver simulation tool using pycalphad. | ✅ |
| [hamidrezanorouzi/numericalMethods](https://github.com/hamidrezanorouzi/numericalMethods) | 30 | Learn essential numerical methods for chemical engineering applications with practical Python and MATLAB examples. | ⚠️ |
| [jkitchin/s20-06681](https://github.com/jkitchin/s20-06681) | 28 | Data science and machine learning in chemical engineering | ⚠️ |
| [HugoMVale/polykin](https://github.com/HugoMVale/polykin) | 23 | A Python library for polymerization kinetics and related chemical engineering calculations. | ✅ |
| [jkitchin/f18-06623](https://github.com/jkitchin/f18-06623) | 22 | Fall 2018 - Mathematical Modeling of Chemical Engineering Processes | ⚠️ |
| [j-jith/pythermophy](https://github.com/j-jith/pythermophy) | 21 | Python module for predicting density, heat capacities and speed of sound of pure fluids using Peng-Robinson, (Soave-)Redlich-Kwong and Lee-Kesler equations of s… | ✅ |
| [killingbear999/chemical-reactor-foundation-model](https://github.com/killingbear999/chemical-reactor-foundation-model) | 20 | [Chemical Engineering Research and Design] This work serves as a first step to develop a foundation model for generic chemical reactor modeling (meta-learning u… | ⚠️ |
| [lollcat/Aspen-RL](https://github.com/lollcat/Aspen-RL) | 20 | Reinforcement learning for chemical engineering process design with Aspen Simulator.  | ✅ |
| [OptiMaL-PSE-Lab/Imperial-ML4CE-Course](https://github.com/OptiMaL-PSE-Lab/Imperial-ML4CE-Course) | 20 | Imperial Chemical Engineering Machine Learning Course | ⚠️ |
| [Ahmedhassan676/Python4ChemicalEngineers](https://github.com/Ahmedhassan676/Python4ChemicalEngineers) | 19 | Notebooks to demonstrate some uses of Python in Chemical Engineering | ⚠️ |
| [rwest/CHME4510](https://github.com/rwest/CHME4510) | 18 | Materials for my undergraduate course on Chemical Engineering Kinetics and Reactor Design at Northeastern University | ⚠️ |
| [ZacharyKahn16/Chemical_Engineering_Reactor_Design](https://github.com/ZacharyKahn16/Chemical_Engineering_Reactor_Design) | 17 | Mass and energy differential analysis for a Packed Bed Reactor (PBR) to produce the fuel additive MMH. This design was completed for my Chemical Engineering Cap… | ⚠️ |
| [PSORLab/Chemical_Engineering_Analysis_Notebooks](https://github.com/PSORLab/Chemical_Engineering_Analysis_Notebooks) | 16 | Literate Programming Examples for Chemical Engineering Analysis | ✅ |
| [OptiMaL-PSE-Lab/REINFORCE-PSE](https://github.com/OptiMaL-PSE-Lab/REINFORCE-PSE) | 16 | Reinforcement learning for batch bioprocess optimization (Computers & Chemical Engineering, 2020) | ✅ |
| [process-intelligence-research/ChemEngKG_kgtool](https://github.com/process-intelligence-research/ChemEngKG_kgtool) | 15 | ython package for accessing the Chemical Engineering Knowledge Graph (ChemEngKG) | ✅ |
| [holland202/principia-artificialis](https://github.com/holland202/principia-artificialis) | 15 | An open research program exploring the mathematics of artificial thought: information geometry, topology, dynamical systems, and thermodynamics applied to AI in… | ✅ |
| [akshay7837/ChemCal](https://github.com/akshay7837/ChemCal) | 14 | Chemical engineering calculations as Jupyter notebook | ⚠️ |
| [sshtomar/Chemical-Engineering](https://github.com/sshtomar/Chemical-Engineering) | 13 | This repository contains Chemical Engineering projects. | ⚠️ |
| [Franco-Pretorius/Python-Tutorial](https://github.com/Franco-Pretorius/Python-Tutorial) | 12 | This is a short introduction to data analysis in Jupyter notebooks for chemical engineering students. | ⚠️ |
| [jkitchin/s17-06364](https://github.com/jkitchin/s17-06364) | 12 | Spring 2017 Chemical and Reaction Engineering | ⚠️ |
| [saadtony/ChemPy](https://github.com/saadtony/ChemPy) | 12 | Introductory Python notes from the Chemical Engineering Department at the University of Utah | ✅ |
| [jkitchin/s24-06642](https://github.com/jkitchin/s24-06642) | 12 | Spring 2024 - Data Science and Machine Learning in Chemical Engineering | ✅ |
| [bacchin/chemical_engineering_python](https://github.com/bacchin/chemical_engineering_python) | 12 | Python code for chemical engineering : master classes and research | ⚠️ |
| [a-urq/ecape-parcel-py](https://github.com/a-urq/ecape-parcel-py) | 11 | A simple Python package that computes ECAPE values and parcel paths. Also includes irreversible adiabatic parcels, which are significantly different and more ac… | ✅ |
| [varma666/ProcessPi](https://github.com/varma666/ProcessPi) | 10 | Python toolkit for chemical engineering simulations, equipment design, and unit conversions | ✅ |
| [pysg/pyther](https://github.com/pysg/pyther) | 10 | python to thermodynamics | ✅ |
| [andr1976/dwsim-paper](https://github.com/andr1976/dwsim-paper) | 10 | Supplementary material and information  | ✅ |

---

## 分子模拟 molecular-sim  <a id="molecularsim"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [jax-md/jax-md](https://github.com/jax-md/jax-md) | 1459 | Differentiable, Hardware Accelerated, Molecular Dynamics | ✅ |
| [mdtraj/mdtraj](https://github.com/mdtraj/mdtraj) | 731 | An open library for the analysis of molecular dynamics trajectories | ✅ |
| [torchmd/torchmd](https://github.com/torchmd/torchmd) | 718 | End-To-End Molecular Dynamics (MD) Engine using PyTorch | ✅ |
| [materialyzeai/maml](https://github.com/materialyzeai/maml) | 466 | Python for Materials Machine Learning, Materials Descriptors, Machine Learning Force Fields, Deep Learning, etc. | ✅ |
| [choderalab/openmmtools](https://github.com/choderalab/openmmtools) | 340 | A batteries-included toolkit for the GPU-accelerated OpenMM molecular simulation engine. | ✅ |
| [jewettaij/moltemplate](https://github.com/jewettaij/moltemplate) | 322 | A general cross-platform tool for preparing simulations of molecules and complex molecular assemblies | ✅ |
| [MDIL-SNU/SevenNet](https://github.com/MDIL-SNU/SevenNet) | 272 | SevenNet - a graph neural network interatomic potential package supporting efficient multi-GPU parallel molecular dynamics simulations. | ✅ |
| [ur-whitelab/MDCrow](https://github.com/ur-whitelab/MDCrow) | 245 | Molecular dynamics simulations with an LLM agent | ✅ |
| [general-molecular-simulations/so3lr](https://github.com/general-molecular-simulations/so3lr) | 231 | SO3krates and Universal Pairwise Force Field for Molecular Simulation | ✅ |
| [shirtsgroup/InterMol](https://github.com/shirtsgroup/InterMol) | 230 | Conversion tool for molecular simulations | ✅ |
| [bjing2016/mdgen](https://github.com/bjing2016/mdgen) | 228 | Generative modeling of molecular dynamics trajectories | ✅ |
| [paduagroup/fftool](https://github.com/paduagroup/fftool) | 207 | Tool to build force field input files for molecular simulation | ✅ |
| [markovmodel/deeptime](https://github.com/markovmodel/deeptime) | 189 | Deep learning meets molecular dynamics. | ✅ |
| [torchmd/mdgrad](https://github.com/torchmd/mdgrad) | 188 | Pytorch differentiable molecular dynamics  | ✅ |
| [Autodesk/molecular-design-toolkit](https://github.com/Autodesk/molecular-design-toolkit) | 174 | Notebook-integrated tools for molecular simulation and visualization | ✅ |
| [peteboyd/lammps_interface](https://github.com/peteboyd/lammps_interface) | 170 | automatic generation of LAMMPS input files for molecular dynamics simulations of MOFs | ✅ |
| [mqcomplab/MDANCE](https://github.com/mqcomplab/MDANCE) | 147 | MDANCE: Hyper-efficient tools to process molecular dynamics simulations. | ✅ |
| [dptech-corp/Uni-GBSA](https://github.com/dptech-corp/Uni-GBSA) | 147 | An automatic workflow to perform MM/GB(PB)SA calculations from force field building, and structure optimization to free energy calculation.  | ✅ |
| [abelcarreras/DynaPhoPy](https://github.com/abelcarreras/DynaPhoPy) | 143 | Phonon anharmonicity analysis from molecular dynamics | ✅ |
| [thorben-frank/mlff](https://github.com/thorben-frank/mlff) | 138 | Build neural networks for machine learning force fields with JAX | ✅ |
| [aai-research-lab/FastMDXplora](https://github.com/aai-research-lab/FastMDXplora) | 132 | Software for automated molecular dynamics exploration | ✅ |
| [kyonofx/MDsim](https://github.com/kyonofx/MDsim) | 115 | [TMLR 2023] Training and simulating MD with ML force fields | ✅ |
| [IBM/controlled-peptide-generation](https://github.com/IBM/controlled-peptide-generation) | 108 | source code for https://arxiv.org/abs/2005.11248 "Accelerating Antimicrobial Discovery with Controllable Deep Generative Models and Molecular Dynamics" | ✅ |
| [qubekit/QUBEKit](https://github.com/qubekit/QUBEKit) | 107 |   Quantum Mechanical Bespoke Force Field Derivation Toolkit | ✅ |
| [isayevlab/aimnetcentral](https://github.com/isayevlab/aimnetcentral) | 107 | AIMNet2: Fast and accurate machine-learned interatomic potential for molecular dynamics simulations | ✅ |
| [deepmodeling/reacnetgenerator](https://github.com/deepmodeling/reacnetgenerator) | 103 | an automatic reaction network generator for reactive molecular dynamics simulation | ✅ |
| [mushroomfire/mdapy](https://github.com/mushroomfire/mdapy) | 103 | A simple and fast python library to handle the data generated from molecular dynamics simulations | ✅ |
| [OUnke/SpookyNet](https://github.com/OUnke/SpookyNet) | 88 | Reference implementation of "SpookyNet: Learning force fields with electronic degrees of freedom and nonlocal effects" | ✅ |
| [kinisi-dev/kinisi](https://github.com/kinisi-dev/kinisi) | 88 | A Python package for estimating diffusion properties from molecular dynamics simulations. | ✅ |
| [txie-93/gdynet](https://github.com/txie-93/gdynet) | 84 | Unsupervised learning of atomic scale dynamics from molecular dynamics. | ✅ |
| [mosdef-hub/gmso](https://github.com/mosdef-hub/gmso) | 73 | Flexible storage of chemical topology for molecular simulation | ✅ |
| [ACEsuit/mace-tutorials](https://github.com/ACEsuit/mace-tutorials) | 73 | Collection of tutorials to use the MACE machine learning force field. | ✅ |
| [zetayue/MXMNet](https://github.com/zetayue/MXMNet) | 72 | Source code for "Molecular Mechanics-Driven Graph Neural Network with Multiplex Graph for Molecular Structures" (NeurIPS 2020 Workshop) | ✅ |
| [wells-wood-research/drMD](https://github.com/wells-wood-research/drMD) | 72 | Molecular Dynamics for Experimentalists | ✅ |
| [microsoft/timewarp](https://github.com/microsoft/timewarp) | 68 | Timewarp is a research project using deep learning to accelerate molecular dynamics simulation.  | ✅ |
| [Probe-Particle/ppafm](https://github.com/Probe-Particle/ppafm) | 67 | Classical force field model for simulating atomic force microscopy images. | ✅ |
| [AISciLab/ProtMMLM](https://github.com/AISciLab/ProtMMLM) | 67 | Code for the paper "MDFoundation: Molecular Dynamics Trajectory-aware Foundation Model for Peptide Discovery with Missing Modalities" | ⚠️ |
| [coarse-graining/cgnet](https://github.com/coarse-graining/cgnet) | 65 | learning coarse-grained force fields | ✅ |
| [shirtsgroup/physical_validation](https://github.com/shirtsgroup/physical_validation) | 65 | Physical validation of molecular simulations | ✅ |
| [TheVisualHub/RoyalMD](https://github.com/TheVisualHub/RoyalMD) | 64 | ?? A lightweight molecular dynamics pipeline for running protein simulations on portable hardware | ✅ |
| [juexinwang/NRI-MD](https://github.com/juexinwang/NRI-MD) | 60 | Neural relational inference for molecular dynamics simulations | ✅ |
| [lab-cosmo/flashmd](https://github.com/lab-cosmo/flashmd) | 57 | A universal ML model to predict molecular dynamics trajectories with long time steps | ✅ |
| [dspoel/Toy-MD](https://github.com/dspoel/Toy-MD) | 57 | Python code for learning Molecular Dynamics simulations | ✅ |
| [psipred/cgdms](https://github.com/psipred/cgdms) | 56 | Differentiable molecular simulation of proteins with a coarse-grained potential | ✅ |
| [svats73/mdml](https://github.com/svats73/mdml) | 55 | mdml: Deep Learning for Molecular Simulations | ✅ |
| [CSIprinceton/workshop-july-2022](https://github.com/CSIprinceton/workshop-july-2022) | 52 | Deep Modeling for Molecular Simulation, two-day virtual workshop, July 7-8, 2022 | ⚠️ |

---

## 制药/ADMET pharma-admet  <a id="pharmaadmet"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [NVIDIA-BioNeMo/KERMT](https://github.com/NVIDIA-BioNeMo/KERMT) | 98 | KERMT is a pretrained graph neural network model for molecular property prediction. | ✅ |
| [architkaila/Fine-Tuning-LLMs-for-Medical-Entity-Extraction](https://github.com/architkaila/Fine-Tuning-LLMs-for-Medical-Entity-Extraction) | 91 | Exploring the potential of fine-tuning Large Language Models (LLMs) like Llama2 and StableLM for medical entity extraction. This project focuses on adapting the… | ✅ |
| [kevinkawchak/LLMs-Pharmaceutical](https://github.com/kevinkawchak/LLMs-Pharmaceutical) | 79 | Oncology Trial Innovation | ✅ |
| [jcchan23/GraphSol](https://github.com/jcchan23/GraphSol) | 77 | Code of our JC paper: "Structure-aware protein solubility prediction from sequence through graph convolutional network and predicted contact map" | ✅ |
| [mims-harvard/Madrigal](https://github.com/mims-harvard/Madrigal) | 45 | Madrigal: Multimodal AI predicts clinical outcomes of drug combinations from preclinical data | ✅ |
| [sameerkhurana10/DSOL_rv0.2](https://github.com/sameerkhurana10/DSOL_rv0.2) | 41 | deep protein solubility prediction | ✅ |
| [devalab/CIGIN](https://github.com/devalab/CIGIN) | 37 | AAAI 2020: Chemically Interpretable Graph Interaction Network for Prediction of Pharmacokinetic Properties of Drug-like Molecules | ✅ |
| [fastdatascience/drug_named_entity_recognition](https://github.com/fastdatascience/drug_named_entity_recognition) | 34 | （无简介） | ✅ |
| [CS207-AP/Inventory-Management](https://github.com/CS207-AP/Inventory-Management) | 32 | An inventory management software for a pharmaceutical vendor. | ✅ |
| [Steffothefisher/Adavid](https://github.com/Steffothefisher/Adavid) | 27 | Adavid is auditor-monitoring tool helping against fraud in pharmaceutical industry | ✅ |
| [jwoongkim11/QA-RAG](https://github.com/jwoongkim11/QA-RAG) | 25 | Code for the paper, From RAG to QA-RAG: Integrating Generative AI for Pharmaceutical Regulatory Compliance Process | ✅ |
| [sssingh/pharmaceutical-sales-analysis-powerbi](https://github.com/sssingh/pharmaceutical-sales-analysis-powerbi) | 24 | A PowerBI dashboard to analyze raw sales data from a multinational pharmaceutical manufacturing company and get insights into the performance of the sales team,… | ⚠️ |
| [PKPDAI/PKDocClassifier](https://github.com/PKPDAI/PKDocClassifier) | 21 | Binary classifier to identify scientific publications reporting pharmacokinetic parameters estimated in vivo | ✅ |
| [jameslu01/Neural_PK](https://github.com/jameslu01/Neural_PK) | 20 | Neural-ODE for Pharmacokinetics Modeling  | ✅ |
| [DavAug/chi](https://github.com/DavAug/chi) | 17 | Chi is an open source Python package which is designed for PKPD modelling and model-informed precision dosing (MIPD). | ✅ |
| [crowsonkb/pharmacokinetics](https://github.com/crowsonkb/pharmacokinetics) | 15 | A Flask web application to calculate and plot drug concentration over time. | ✅ |
| [ADicksonLab/OpenRXN](https://github.com/ADicksonLab/OpenRXN) | 13 | A free, open-source tool for modeling chemical reaction networks in Python | ✅ |
| [VizuaraAI/pharma-slm](https://github.com/VizuaraAI/pharma-slm) | 12 | From-scratch ~350M pharmaceutical Small Language Model — full reproducible pipeline, every experiment, GPU/cost breakdown, and a live demo (chat + MCQ). | ⚠️ |
| [Ianphorsman/RxClassAPIWrapper](https://github.com/Ianphorsman/RxClassAPIWrapper) | 12 | Python wrapper for RxClass API with helper functions to lookup: indications, contraindications, pharmacology, pharmacokinetics, chemical names, therapeutic clas… | ✅ |
| [zhekaiTong/Thin_Obj_Bin_Picking](https://github.com/zhekaiTong/Thin_Obj_Bin_Picking) | 12 | A ROS package for autonomous thin objects bin picking, specifically pharmaceutical blister packs, with UR10 robotic arm and Robotiq 2-Finger 140mm Adaptive Para… | ⚠️ |
| [interestng/medkit](https://github.com/interestng/medkit) | 12 | Unified Python SDK for OpenFDA, PubMed, and ClinicalTrials.gov with clinical intelligence, interaction detection, and research tools. | ✅ |
| [Shane-Neeley/DrugMarket](https://github.com/Shane-Neeley/DrugMarket) | 12 | Collect and analyze data related to clinical trials of publicly listed biotech and pharmaceutical stocks. This is intended to give a clinical pipeline and finan… | ✅ |
| [blakeaw/pysb-pkpd](https://github.com/blakeaw/pysb-pkpd) | 11 | PySB add-on providing domain-specific macros and models for empirical and mechanistic PK/PD modeling. | ✅ |
| [ELDERGARLIC/Online-Pharmacy-Microservice](https://github.com/ELDERGARLIC/Online-Pharmacy-Microservice) | 11 | This project is built using Python and FastAPI, offering a modern and efficient solution for managing an online pharmacy platform.  With a focus on scalability,… | ⚠️ |
| [neo4j-product-examples/demo-supply_chain](https://github.com/neo4j-product-examples/demo-supply_chain) | 11 | Scalable AI agent built with Google Cloud’s Agent Development Kit (ADK) and deployed on Cloud Run, integrated with Neo4j to analyze pharmaceutical supply chains… | ✅ |
| [CodeWithCharan/PharmaQuery](https://github.com/CodeWithCharan/PharmaQuery) | 10 | Pharmaceutical Insight Retrieval System designed to help users gain meaningful insights from research papers and documents in the pharmaceutical domain. | ✅ |
| [fangxintao/SciMind](https://github.com/fangxintao/SciMind) | 10 | SciMind: A Multimodal Mixture-of-Experts Model for Advancing Pharmaceutical Sciences | ⚠️ |
| [alofgran/Drug-Price-Prediction](https://github.com/alofgran/Drug-Price-Prediction) | 10 | Pharmaceutical Drug Price Predictor | ⚠️ |
| [MahdiNavaei/pharmaceutical-supply-chain-agentic-ai](https://github.com/MahdiNavaei/pharmaceutical-supply-chain-agentic-ai) | 9 | AI-powered pharmaceutical supply chain management using LangGraph agents, OpenAI GPT-4, and optimization algorithms. | ⚠️ |
| [groverlab/candycodes](https://github.com/groverlab/candycodes) | 9 | CandyCodes: Simple universally unique edible identifiers for confirming the authenticity of pharmaceuticals | ✅ |
| [alexrd/pk](https://github.com/alexrd/pk) | 9 | Simple pharmacokinetics script in Python | ⚠️ |
| [SCrownJ/FGNNSol](https://github.com/SCrownJ/FGNNSol) | 9 | Protein Solubility Prediction Using Fused Graph Convolutional Networks and Improved Attention Networks with AlphaFold3-Derived Features | ⚠️ |
| [peytoncchen/PK-Py](https://github.com/peytoncchen/PK-Py) | 9 | Stanford Appel Lab - Study Pharmacokinetics Project: Pharmacokinetic data modeling and visualization tool. Primary usage for drug delivery studies. Python suppo… | ✅ |
| [ToxMCP/pbpk-mcp](https://github.com/ToxMCP/pbpk-mcp) | 8 | MCP server for PBPK modeling workflows (simulation control + PK analytics). | ✅ |
| [jajsmith/COVID19NonPharmaceuticalInterventions](https://github.com/jajsmith/COVID19NonPharmaceuticalInterventions) | 8 | Gathered data and analysis on Non-Pharmaceutical Interventions related to COVID-19 Pandemic | ⚠️ |
| [JacksonBurns/chemeleon_aqueous_solubility](https://github.com/JacksonBurns/chemeleon_aqueous_solubility) | 7 | CheMeleon Kinetic Solubility Prediction | ✅ |

---

## 蛋白质-配体 protein-ligand  <a id="proteinligand"></a>

| 仓库 | ⭐ | 简介 | 封装 |
|---|---|---|---|
| [luwei0917/DynamicBind](https://github.com/luwei0917/DynamicBind) | 307 | repo for DynamicBind: Predicting ligand-specific protein-ligand complex structure with a deep equivariant generative model | ✅ |
| [thinng/GraphDTA](https://github.com/thinng/GraphDTA) | 307 | GraphDTA: Predicting drug-target binding affinity with graph neural networks | ⚠️ |
| [hkmztrk/DeepDTA](https://github.com/hkmztrk/DeepDTA) | 305 | Source code for "DeepDTA: deep drug-target binding affinity prediction" | ⚠️ |
| [Intelligent-Drug-Discovery-Lab/SurfDock](https://github.com/Intelligent-Drug-Discovery-Lab/SurfDock) | 255 | SurfDock is a Surface-Informed Diffusion Generative Model for Reliable and Accurate Protein-ligand Complex Prediction | ✅ |
| [kexinhuang12345/MolTrans](https://github.com/kexinhuang12345/MolTrans) | 242 | MolTrans: Molecular Interaction Transformer for Drug Target Interaction Prediction (Bioinformatics) | ✅ |
| [patrickbryant1/Umol](https://github.com/patrickbryant1/Umol) | 241 | Protein-ligand structure prediction | ⚠️ |
| [zaixizhang/PocketGen](https://github.com/zaixizhang/PocketGen) | 228 | PocketGen (Nature Machine Intelligence 24): Generating Full-Atom Ligand-Binding Protein Pockets | ✅ |
| [jiaxianyan/BioMiner](https://github.com/jiaxianyan/BioMiner) | 96 | A Multi-modal System for Automated Mining of Protein-Ligand Bioactivity Data from Literature | ✅ |
| [KexinZhangResearch/PhysDock](https://github.com/KexinZhangResearch/PhysDock) | 93 | Physics-Guided All-Atom Diffusion Model for Accurate Protein-Ligand Complex Prediction | ✅ |
| [jonfunk21/ProteusAI](https://github.com/jonfunk21/ProteusAI) | 87 | ProteusAI is a library for the machine learning driven engineering of proteins. The library enables workflows from protein structure prediction, prediction of m… | ✅ |
| [camlab-ethz/GEMS](https://github.com/camlab-ethz/GEMS) | 84 | Protein-Ligand Binding Affinity Prediction with GNN and Transfer Learning From Protein Language Models | ✅ |
| [KailiWang1/DeepDTAF](https://github.com/KailiWang1/DeepDTAF) | 77 |  a deep learning architecture for protein-ligand binding affinity prediction | ✅ |
| [YangLing0818/IPDiff](https://github.com/YangLing0818/IPDiff) | 61 | [ICLR 2024] Protein-Ligand Interaction Prior for Binding-aware 3D Molecule Diffusion Models | ✅ |
| [lucidrains/neural-plexer-pytorch](https://github.com/lucidrains/neural-plexer-pytorch) | 52 | Implementation of Nvidia's NeuralPlexer, for end-to-end differentiable design of functional small-molecules and ligand-binding proteins, in Pytorch | ✅ |
| [jivankandel/PUResNet](https://github.com/jivankandel/PUResNet) | 52 | Predicting protein-ligand binding sites using deep convolutional neural network | ⚠️ |
| [chao1224/NeuralMD](https://github.com/chao1224/NeuralMD) | 51 | NeuralMD for Protein-ligand Binding Simulation, Nature Communicaitons 2025 https://www.nature.com/articles/s41467-025-67808-z | ⚠️ |
| [WeilabMSU/TopoFormer](https://github.com/WeilabMSU/TopoFormer) | 46 | Topological transformer for protein-ligand complex interaction prediction. | ✅ |
| [yvquanli/GLAM](https://github.com/yvquanli/GLAM) | 41 | Code for "An adaptive graph learning method for automated molecular interactions and properties predictions". | ✅ |

---

## 封装可行性说明

- **✅ 直接封装**：可 pip/conda/uv 安装的 Python 包，有 importable 模块 + API/CLI/examples 证据，许可证为 MIT/Apache/BSD/LGPL/MPL 等可再分发。
- **⚠️ 需预处理**：one/缺许可证（可再分发性不明）、教程/Notebook/数据集、或强 copyleft（GPL/AGPL，可蒸馏但必须保留源许可证）。
- 跨领域仓库（如既是药物发现又是量子化学）不在本 500 清单中，以确保去重。


