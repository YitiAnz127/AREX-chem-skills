# AREX-Skill 化学/化工/分子/制药 仓库分档下载清单

> **这份文件是给「AI 下载助手」看的。** 按 AREX-Skill 的 design 要求，**把三个档位分别下载到三个不同的文件夹**，并且**按每个仓库的用途判断该 clone 什么**（不是无脑全量拉取）。

---

## 一、给 AI 的操作指引（请先读这段）

**你的任务**：把下面的 57 个仓库按三档下载到**用户指定文件夹**下的三个子文件夹里：

| 档位 | 装入文件夹 | 数量 | clone 策略 |
|------|-----------|------|-----------|
| S 档 · 现成 MCP Server | `<TARGET>/s-mcp/` | 26 | **整仓浅克隆**（MCP server 是可运行程序，需全部源码） |
| S 档 · 现成 Agent-Skills 库 | `<TARGET>/s-skills/` | 11 | **只取技能目录**（sparse-checkout，不夹带示例/模板等无关内容） |
| A 档 · 核心库（供 DisCo 蒸馏） | `<TARGET>/a-libs/` | 20 | **整仓浅克隆源码**（蒸馏器需读源码+文档+示例+测试+配置） |

**AREX-Skill 的 evidence-boundary 思路（为什么这样分）**：AREX 蒸馏技能时，只会把"可操作知识"（源码、文档、示例、测试、配置）纳入，而**排除**生成物、构建输出、vendored 依赖、本地环境、缓存、大工件等无关内容。所以——

- MCP server 要**运行**，必须完整源码 → 整仓。
- Agent-Skills 库本质是"技能集合"，**只需技能目录本身**（`SKILL.md + references/ + scripts/`），不需要库里的教程/模板/训练脚本 → 用 sparse-checkout 只取技能目录。
- 核心库给 DisCo 蒸馏器用，蒸馏器要采样的就是源码组件的 evidence → 整仓源码；这些库的大权重/数据集通常在 git 之外（在 HuggingFace / Release 单独下载），所以 clone 本身不重。

**执行方式（推荐，改动 `<TARGET>` 后可直接运行）**：

```bash
#!/usr/bin/env bash
set -euo pipefail

TARGET="/path/to/你的/目标文件夹"     # ← 改成用户指定的路径

# 整仓浅克隆（MCP server / A 档核心库）
fetch_full() { git clone --depth 1 "$1"; }

# 只取技能目录：探测常见路径，失败回退整仓
fetch_skill() {
  git clone --depth 1 --filter=blob:none --sparse "$1"
  local dir
  dir=$(basename "$1")
  ( cd "$dir" && for d in skills .claude/skills .agents/skills .continuing/skills; do
      if git ls-tree -d HEAD "$d" >/dev/null 2>&1; then
        git sparse-checkout set "$d"; echo "  [skill] $dir <- $d"; return
      fi
    done
    git sparse-checkout disable; echo "  [skill] $dir <- 整仓（未发现技能子目录）" )
}

rm -rf "$TARGET/s-mcp" "$TARGET/s-skills" "$TARGET/a-libs"
mkdir -p "$TARGET/s-mcp" "$TARGET/s-skills" "$TARGET/a-libs"

# ---------- ① S 档 · MCP Server（整仓）→ s-mcp/ ----------
cd "$TARGET/s-mcp"
for r in cyanheads/pubmed-mcp-server Cicatriiz/healthcare-mcp-public patsnap/mcp \
         cyanheads/clinicaltrialsgov-mcp-server variomeanalytics/bioinformatics-agent-skills \
         Augmented-Nature/PubChem-MCP-Server tandemai-inc/rdkit-mcp-server PDBeurope/PDBe-MCP-Servers \
         Augmented-Nature/AlphaFold-MCP-Server longevity-genie/gget-mcp AIB001/PRISM \
         Augmented-Nature/PDB-MCP-Server biocontext-ai/registry \
         Augmented-Nature/Augmented-Nature-UniProt-MCP-Server dovas-net/chimeraX-mcp \
         nickzren/opentargets-mcp Arielbs/rosetta-mcp-server PhelanShao/xtb-mcp-server \
         chemrich/MCPymol jasonkim8652/protein-design-mcp TakumiY235/uniprot-mcp-server \
         dogeplusplus/bio-agents-mcp Augmented-Nature/OpenTargets-MCP-Server \
         openpharma-org/drugbank-mcp-server qgeng1465/bio-mcp cyanheads/pubchem-mcp-server; do
  fetch_full "https://github.com/$r.git"
done

# ---------- ② S 档 · Agent-Skills（只取技能目录）→ s-skills/ ----------
cd "$TARGET/s-skills"
for r in K-Dense-AI/scientific-agent-skills aipoch/medical-research-skills ai4s-research/open-science \
         GPTomics/bioSkills ClawBio/ClawBio beita6969/ScienceClaw \
         jaechang-hits/SciAgent-Skills K-Dense-AI/science-superpowers \
         adaptyvbio/protein-design-skills jinzhezenggroup/computational-chemistry-agent-skills \
         QSong-github/DrugClaw; do
  fetch_skill "https://github.com/$r.git"
done

# ---------- ③ A 档 · 核心库（整仓源码，供蒸馏）→ a-libs/ ----------
cd "$TARGET/a-libs"
for r in rdkit/rdkit openbabel/openbabel datamol-io/datamol openmm/openmm \
         MDAnalysis/mdanalysis mdtraj/mdtraj deepmodeling/deepmd-kit pyscf/pyscf psi4/psi4 \
         gcorso/DiffDock gnina/gnina MolecularAI/aizynthfinder MolecularAI/REINVENT4 \
         molecularsets/moses deepchem/deepchem DeepGraphLearning/torchdrug \
         AstraZeneca/chemicalx mims-harvard/TDC facebookresearch/esm CalebBell/thermo; do
  fetch_full "https://github.com/$r.git"
done

echo "全部完成。请核对：s-mcp/ 应有 26 个，s-skills/ 应有 11 个，a-libs/ 应有 20 个。"
```

**注意事项**：
- `s-skills/` 若整仓回退，属正常（有些库技能目录平铺在根下），已用 `--filter=blob:none` 控制体积。
- 大仓库（`deepchem`、`esm`、`REINVENT4` 等）的模型权重/数据集不在 git 里，clone 不会很大；若用户后续要权重，另从 HuggingFace/Release 下载。
- 完成后向用户汇报：`成功 N / 失败 M`，失败清单列出来。

---

## 二、S 档（37 个）—— 放进 Disco 即插即用

### 2.1 现成 MCP Server（26 个）→ `s-mcp/`，整仓

| # | 仓库名称 | 链接 | clone 策略 |
|---|----------|------|-----------|
| 1 | cyanheads/pubmed-mcp-server | https://github.com/cyanheads/pubmed-mcp-server | 整仓 |
| 2 | Cicatriiz/healthcare-mcp-public | https://github.com/Cicatriiz/healthcare-mcp-public | 整仓 |
| 3 | patsnap/mcp | https://github.com/patsnap/mcp | 整仓 |
| 4 | cyanheads/clinicaltrialsgov-mcp-server | https://github.com/cyanheads/clinicaltrialsgov-mcp-server | 整仓 |
| 5 | variomeanalytics/bioinformatics-agent-skills | https://github.com/variomeanalytics/bioinformatics-agent-skills | 整仓 |
| 6 | Augmented-Nature/PubChem-MCP-Server | https://github.com/Augmented-Nature/PubChem-MCP-Server | 整仓 |
| 7 | tandemai-inc/rdkit-mcp-server | https://github.com/tandemai-inc/rdkit-mcp-server | 整仓 |
| 8 | PDBeurope/PDBe-MCP-Servers | https://github.com/PDBeurope/PDBe-MCP-Servers | 整仓 |
| 9 | Augmented-Nature/AlphaFold-MCP-Server | https://github.com/Augmented-Nature/AlphaFold-MCP-Server | 整仓 |
| 10 | longevity-genie/gget-mcp | https://github.com/longevity-genie/gget-mcp | 整仓 |
| 11 | AIB001/PRISM | https://github.com/AIB001/PRISM | 整仓 |
| 12 | Augmented-Nature/PDB-MCP-Server | https://github.com/Augmented-Nature/PDB-MCP-Server | 整仓 |
| 13 | biocontext-ai/registry | https://github.com/biocontext-ai/registry | 整仓 |
| 14 | Augmented-Nature/Augmented-Nature-UniProt-MCP-Server | https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server | 整仓 |
| 15 | dovas-net/chimeraX-mcp | https://github.com/dovas-net/chimeraX-mcp | 整仓 |
| 16 | nickzren/opentargets-mcp | https://github.com/nickzren/opentargets-mcp | 整仓 |
| 17 | Arielbs/rosetta-mcp-server | https://github.com/Arielbs/rosetta-mcp-server | 整仓 |
| 18 | PhelanShao/xtb-mcp-server | https://github.com/PhelanShao/xtb-mcp-server | 整仓 |
| 19 | chemrich/MCPymol | https://github.com/chemrich/MCPymol | 整仓 |
| 20 | jasonkim8652/protein-design-mcp | https://github.com/jasonkim8652/protein-design-mcp | 整仓 |
| 21 | TakumiY235/uniprot-mcp-server | https://github.com/TakumiY235/uniprot-mcp-server | 整仓 |
| 22 | dogeplusplus/bio-agents-mcp | https://github.com/dogeplusplus/bio-agents-mcp | 整仓 |
| 23 | Augmented-Nature/OpenTargets-MCP-Server | https://github.com/Augmented-Nature/OpenTargets-MCP-Server | 整仓 |
| 24 | openpharma-org/drugbank-mcp-server | https://github.com/openpharma-org/drugbank-mcp-server | 整仓 |
| 25 | qgeng1465/bio-mcp | https://github.com/qgeng1465/bio-mcp | 整仓 |
| 26 | cyanheads/pubchem-mcp-server | https://github.com/cyanheads/pubchem-mcp-server | 整仓 |

### 2.2 现成 Agent-Skills 库（11 个）→ `s-skills/`，只取技能目录

| # | 仓库名称 | 链接 | clone 策略 |
|---|----------|------|-----------|
| 1 | K-Dense-AI/scientific-agent-skills | https://github.com/K-Dense-AI/scientific-agent-skills | 取 `skills/`（自适应，失败回退整仓） |
| 2 | aipoch/medical-research-skills | https://github.com/aipoch/medical-research-skills | 取技能目录（自适应） |
| 3 | ai4s-research/open-science | https://github.com/ai4s-research/open-science | 取技能目录（自适应） |
| 4 | GPTomics/bioSkills | https://github.com/GPTomics/bioSkills | 取技能目录（自适应） |
| 5 | ClawBio/ClawBio | https://github.com/ClawBio/ClawBio | 取技能目录（自适应） |
| 6 | beita6969/ScienceClaw | https://github.com/beita6969/ScienceClaw | 取技能目录（自适应） |
| 7 | jaechang-hits/SciAgent-Skills | https://github.com/jaechang-hits/SciAgent-Skills | 取技能目录（自适应） |
| 8 | K-Dense-AI/science-superpowers | https://github.com/K-Dense-AI/science-superpowers | 取技能目录（自适应） |
| 9 | adaptyvbio/protein-design-skills | https://github.com/adaptyvbio/protein-design-skills | 取技能目录（自适应） |
| 10 | jinzhezenggroup/computational-chemistry-agent-skills | https://github.com/jinzhezenggroup/computational-chemistry-agent-skills | 取技能目录（自适应） |
| 11 | QSong-github/DrugClaw | https://github.com/QSong-github/DrugClaw | 取技能目录（自适应） |

---

## 三、A 档（20 个）—— 核心库，需蒸馏成 skill 图后使用 → `a-libs/`，整仓源码

| # | 仓库名称 | 链接 | clone 策略 |
|---|----------|------|-----------|
| 1 | rdkit/rdkit | https://github.com/rdkit/rdkit | 整仓源码（供蒸馏） |
| 2 | openbabel/openbabel | https://github.com/openbabel/openbabel | 整仓源码 |
| 3 | datamol-io/datamol | https://github.com/datamol-io/datamol | 整仓源码 |
| 4 | openmm/openmm | https://github.com/openmm/openmm | 整仓源码 |
| 5 | MDAnalysis/mdanalysis | https://github.com/MDAnalysis/mdanalysis | 整仓源码 |
| 6 | mdtraj/mdtraj | https://github.com/mdtraj/mdtraj | 整仓源码 |
| 7 | deepmodeling/deepmd-kit | https://github.com/deepmodeling/deepmd-kit | 整仓源码 |
| 8 | pyscf/pyscf | https://github.com/pyscf/pyscf | 整仓源码 |
| 9 | psi4/psi4 | https://github.com/psi4/psi4 | 整仓源码 |
| 10 | gcorso/DiffDock | https://github.com/gcorso/DiffDock | 整仓源码 |
| 11 | gnina/gnina | https://github.com/gnina/gnina | 整仓源码 |
| 12 | MolecularAI/aizynthfinder | https://github.com/MolecularAI/aizynthfinder | 整仓源码 |
| 13 | MolecularAI/REINVENT4 | https://github.com/MolecularAI/REINVENT4 | 整仓源码 |
| 14 | molecularsets/moses | https://github.com/molecularsets/moses | 整仓源码 |
| 15 | deepchem/deepchem | https://github.com/deepchem/deepchem | 整仓源码 |
| 16 | DeepGraphLearning/torchdrug | https://github.com/DeepGraphLearning/torchdrug | 整仓源码 |
| 17 | AstraZeneca/chemicalx | https://github.com/AstraZeneca/chemicalx | 整仓源码 |
| 18 | mims-harvard/TDC | https://github.com/mims-harvard/TDC | 整仓源码 |
| 19 | facebookresearch/esm | https://github.com/facebookresearch/esm | 整仓源码 |
| 20 | CalebBell/thermo | https://github.com/CalebBell/thermo | 整仓源码 |

---

*生成于 AREX-Skill 化学/化工/分子/制药领域可封装性普查。S 档=即插即用（MCP/SKILL），A 档=需 DisCo Creator 蒸馏的核心库。clone 策略遵循 AREX evidence-boundary：MCP 整仓运行、SKILL 只取技能目录、核心库整仓供蒸馏。所有链接由 GitHub 仓库元数据生成。*
