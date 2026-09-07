# AREX-Skill 项目结构分析（面向“壳子移植”）

> 分析目的：本项目（AREX-Skill）是一个“技能蒸馏 / 技能库 + 可编程 Agent 运行时”的完整工程。
> 目标是剥离出**可复用的“壳子”**（产品结构/运行时框架/工具链），移植到其他领域复用。
> 本文以“产品结构”为主线，逐层拆解部件、功能与结构。

---

## 1. 项目定位（它是什么）

AREX-Skill（DisCo）把 GitHub 仓库 / 论文中的 **“操作知识”** 蒸馏成 Agent 可读、可执行的 **Skill**，
并由一个**可编程编码 Agent 运行时**（DisCo）负责路由、加载、执行、验证这些 Skill。

一句话：**“知识蒸馏成 Skill + Agent 运行时消费 Skill”** 的双层产品。

- 核心产物：Skill（自包含、Agent 可读、可执行的操作知识单元）
- 核心运行时：DisCo（基于 Pi 开源 Agent 工具包改造）
- 数据规模：1,000 个仓库、5,000+ Skill、20 个研究领域、178 个包族

---

## 2. 顶层目录结构（产品的分层骨架）

```text
AREX-Skill/
├── README.md / README.zh-CN.md      # 项目入口与介绍
├── CONTRIBUTING.md(_CN)             # 贡献规范
├── LICENSE                          # Apache 2.0（库级）
├── assets/                          # 图片素材（hero/method/results/library 示意图）
├── docs/                            # 架构与使用文档（架构、安装、工作流、元技能、目录等）
├── skills/                          # ★ 知识层：AREX-Skill 技能库（运行期集合）
├── scripts/                         # 安装/发布脚本（installer、release）
├── cli/                             # ★ 运行时层：DisCo CLI / SDK（npm 包 @arex-skill/disco）
└── examples/                        # 端到端使用示例（Creator / Researcher 工作流产物）
```

**产品的两层核心：**
- `skills/` —— **内容层**（数据/知识资产）
- `cli/` —— **机制层**（引擎/运行时/工具链）

这两者解耦，正是“壳子”可移植的关键：**壳子 = cli/（机制层）+ scripts/（构建流水线）+ skills 的目录约定（内容契约）**。

---

## 3. 机制层：`cli/`（DisCo 运行时）—— 移植的重点“壳子”

`cli/` 是唯一可发布的 npm 包 `@arex-skill/disco`，本质是 **Pi（earendil-works/pi v0.83.0）编码 Agent 的深度改造版**。
它自带一个完整的 Agent 运行时（LLM 统一接口、Agent 循环、终端 UI、编码 Agent CLI、SDK）。

### 3.1 源码树结构

```text
cli/
├── package.json                 # 唯一发布包 @arex-skill/disco（bin: disco; main/index; exports）
├── npm-shrinkwrap.json          # 锁定依赖
├── tsconfig.*.json / vitest.config.ts
├── docs/                        # 运行时文档（sdk/rpc/skills/extensions/sessions/providers…）
├── examples/                    # SDK 示例 + extensions 示例（大量扩展插件示例）
├── scripts/                     # 资产复制、上游溯源校验、包内容校验
└── packages/
    └── coding-agent/            # ★ 核心运行时源码（来自 Pi 的移植子树）
        ├── src/
        ├── test/
        └── UPSTREAM_*.json/md   # 上游溯源清单（可审计）
```

### 3.2 `src/` 运行时模块划分（按功能）

| 模块 | 目录 | 功能 |
| --- | --- | --- |
| 入口 | `src/cli.ts` `src/main.ts` `src/index.ts` `src/rpc-entry.ts` | CLI/包/SDK/RPC 四种入口 |
| CLI 参数与启动 | `src/cli/` | args、config-selector、project-trust、startup-ui、session-picker、repo-skills、file-processor、initial-message、list-models |
| 核心会话引擎 | `src/core/` | agent-session、agent-session-runtime、会话管理、事件总线、消息、提示词模板 |
| 模型层 | `src/core/model-*` | model-config/registry/resolver/runtime、models-store、provider-composer、remote-catalog |
| 工具集 | `src/core/tools/` | bash、edit、read、write、find、grep、ls、truncate 等编码 Agent 内建工具 |
| 扩展机制 | `src/core/extensions/` | extensions loader/runner/wrapper/types —— 插件系统（核心可复用机制） |
| OAuth/鉴权 | `src/core/oauth/` | anthropic、openai-codex、openrouter、device-code、pkce 等 |
| 会话压缩/导出 | `src/core/compaction/`、`src/core/export-html/` | 上下文压缩、HTML 会话导出 |
| 包管理 | `src/core/package-manager.ts` | Skill/扩展/提示词/主题包安装 |
| 技能系统 | `src/core/skills.ts` | Skill 发现、加载、注册、模型可见性（含 disable-model-invocation）|
| **DisCo 专有层** | `src/disco/` | ★ 与 Pi 差异最大、最值得移植的部分（见 3.3）|
| 交互 UI | `src/modes/interactive/` | TUI 组件（会话、模型、主题、Skill 选择器等）|
| 其他模式 | `src/modes/print-mode.ts`、`src/modes/rpc/` | 打印模式、RPC 模式 |
| 工具函数 | `src/utils/` | git、shell、image、frontmatter、paths 等 |

### 3.3 DisCo 专有层 `src/disco/` —— 项目“灵魂”，也是移植核心价值

这是本项目在 Pi 之上新增的部分，包含：

1. **`src/disco/skills/`** —— 内建的 Creator 元技能（工作流技能），即“蒸馏流水线本身写成 Skill”：
   - `distill-ml-knowledge/`（蒸馏总入口）
   - `create-repo-skill/`、`verify-repo-skill/`、`prepare-repo-skill-env/`
   - `refresh-repo-skill/`、`extend-repo-skill/`
   - `import-repo-skills-to-agent/`（跨 Agent 导出）
   - `repo-skills-router/`（路由技能）
   - 论文蒸馏组：`create-paper-skills/`、`paper-skills-distiller/`、`plan-paper-skill-modules/`、
     `create-paper-module-skill/`、`prepare-paper-recovery-env/`、`recover-paper-result/`、`analyze-paper-recovery/`
   - `design-meta-skill/`、`workflow-authoring/`
2. **`src/disco/dynamic-workflows/`** —— 动态工作流引擎（workflow-manager、workflow、agent、deep-research、model-routing、run-persistence、structured-output 等）
3. **`src/disco/modes/`** —— Creator/Researcher 双角色模式（prompts、skill-policy、types）
4. **DisCo 导入/路由/事务**（在 `src/disco/` 根）：
   - `import_repo_skill`、`import_operating_skill_graph`、`import_meta_skill`
   - `build_repo_skills_collection`、`update_repo_skills_router`、`export_repo_skills_to_agent`
   - `with_import_lock`（带锁的原子导入事务）、`repo-skill-license-contract`、`skill-role-contracts`

> **移植启示**：`src/disco/skills/` 的“工作流即 Skill”设计 + `with_import_lock` 事务式导入 +
> 双角色（Creator/Researcher）过滤，是本项目最具普适性的“壳”骨架。

---

## 4. 知识层：`skills/`（AREX-Skill 技能库）

```text
skills/
├── README.md
├── repositories/
│   ├── repo-skills/             # ★ 1,000 个仓库技能根（31,191 个文件）
│   │   ├── repository-index.jsonl
│   │   └── <skill-id>/
│   │       ├── SKILL.md
│   │       ├── sub-skills/      # 分层子技能
│   │       ├── references/      # 佐证/溯源
│   │       └── scripts/         # 可执行助手
│   └── repo-skills-router/      # ★ 路由技能（area→family→repo 渐进式下钻）
│       ├── SKILL.md
│       └── references/{areas,families,index}/
└── task-oriented/               # 基准任务专用技能（FrontierCS/PaperBench/PassNet）
```

### 4.1 单个技能的标准“产品形态”

```text
skill/
├── SKILL.md                # 首个被读文件：作用域、路由、工作流、校验
├── references/             # 聚焦的指令 + 来源溯源（repo-provenance.md、repo-routing-metadata.json、troubleshooting.md）
├── sub-skills/<area>/SKILL.md   # 更深层任务专用指导（渐进式披露）
└── scripts/                # 小型可执行助手/诊断/预检（如 vllm_skill_doctor.py）
```

**SKILL.md frontmatter 关键字段：**
- `name`、`description`（决定模型是否自动选择）
- `disable-model-invocation: true`（隐藏根技能，避免撑爆上下文）
- `metadata.disco-role: operating|meta|shared`（决定在 Researcher/Creator 哪种模式可用）
- `license`（每个技能独立授权）

### 4.2 路由设计（渐进式披露，关键机制）

```text
请求 → area(领域) → family(族) → repository(仓库根) → sub-skill(子技能)
```

- 路由器 `repo-skills-router` 模型可见；普通仓库技能默认隐藏（`disable-model-invocation`）。
- 机器可读索引（`references/index/`）：`taxonomy.json`（20 领域 178 族）、`repositories.jsonl`、`assignments.jsonl` —— 是路由的**单一事实源**。
- 导入/更新用结构化元数据生成路由页，**不手工编辑 Markdown**。

### 4.3 部署作用域（移植时可直接复用）

| 作用域 | 位置 | 适用 |
| --- | --- | --- |
| 项目级 | `<project>/.agents/skills/<id>/` | 绑定单任务/单环境，不确定复用 |
| 托管级 | `~/.disco/agent/skills/<id>/` | 自包含、可溯源、跨项目复用 |
| 仓库集 | `~/.disco/agent/skills/repositories/{repo-skills, repo-skills-router}/` | 仓库技能专用 |

---

## 5. 构建/流水线层：`scripts/`（蒸馏与发布的“工厂”）

```text
scripts/
├── install-disco.sh / install-disco.ps1     # 托管安装器（curl/PowerShell）
├── prepare-disco-release-assets.py          # 打包发布资产
├── reset-disco-home.sh                      # 重置 ~/.disco
├── build-from-source-link.sh                # 源码构建/链接冒烟
└── dev/
    ├── deprecate-legacy-disco-npm.sh
    └── release-disco-npm.py                 # npm 发布
```

- `cli/scripts/`：`copy-assets.mjs`、`upstream-provenance.mjs`（上游溯源校验）、`verify-package.mjs`、`verify-rpiv-todo-contract.mjs`
- 发布门禁（`cli/package.json` 的 `prepublishOnly`）：溯源校验 → typecheck → 测试 → 构建 → 包校验。

---

## 6. 文档层：`docs/`

- `architecture.md`（架构，双角色/路由/部署/单一事实源）
- `disco-meta-skills.md` / `disco-workflows.md`（Creator 工作流与元技能目录）
- `installation.md`、`refreshing-repo-skills.md`
- `repository-catalog.md`、`imported-repo-skills.md`（目录清单）
- 中英双语均有（`.zh.md`）

---

## 7. 示例层：`examples/`（端到端“成品”样例）

- `researcher/`：Researcher 模式真实产物（vLLM vs SGLang 基准对比：命令、工作负载、结果、版本、报告）
- `creator/repo-to-skills/`：Creator 把 huggingface_hub 仓库蒸馏成完整技能图 + 全部验证工件（test-cases/review/evidence）
- `creator/paper-to-skills/`：论文蒸馏配置模板
- `cli/examples/`：SDK 示例（01–13）+ 大量扩展插件示例

---

## 8. “壳子”可复用部件清单（移植到其他领域）

移植时按“依赖自低到高、可独立抽取”排序：

| 层 | 可移植部件 | 说明 |
| --- | --- | --- |
| **A. 可编程 Agent 运行时** | `cli/packages/coding-agent/src/` | 完整编码 Agent：会话引擎、工具集、扩展插件系统、OAuth、模型层、TUI/RPC/打印模式、SDK |
| **B. 插件/扩展机制** | `src/core/extensions/` + `cli/examples/extensions/` | 高度可复用的事件总线 + 扩展加载/运行/包装 |
| **C. 技能系统** | `src/core/skills.ts` + `frontmatter` 契约 | Skill 发现、注册、模型可见性、角色过滤 |
| **D. 包管理器** | `src/core/package-manager.ts` | 安装 Skill/扩展/提示词/主题包 |
| **E. 工作流即 Skill** | `src/disco/skills/` | Creator/Researcher 元技能模式（把流程写成 Skill）|
| **F. 事务式导入** | `src/disco/*.ts`（with_import_lock 等）| 原子、可回滚的图形导入/路由更新 |
| **G. 渐进式路由** | `repo-skills-router` + 索引 | area→family→repo→sub-skill 下钻，避免上下文爆炸 |
| **H. 技能内容契约** | `SKILL.md / references / sub-skills / scripts` 目录约定 | 与具体领域无关，可直接作为新领域的内容规范 |
| **I. 蒸馏流水线** | `src/disco/skills/`（create/verify/refresh/extend）| 把仓库/论文/知识源蒸馏成技能的方法论（可改造目标领域）|
| **J. 安装/发布** | `scripts/`（installer、release、provenance）| 多平台安装器 + 可审计发布门禁 |

---

## 9. 移植要点与建议（供后续决策）

1. **壳与内容已解耦**：`cli/`（机制）与 `skills/`（内容）分离，移植只需搬机制层 + 重新定义内容契约与领域路由。
2. **优先抽取**：A（运行时）+ B（扩展）+ C（技能系统）+ G（路由）是“通用壳”；E/F/I（蒸馏流水线）是针对“知识→技能”的领域化部分，需按新领域改造。
3. **领域替换点**（新领域需要重写的部分）：
   - 技能内容（`skills/repositories/repo-skills/<id>/`）
   - 路由 taxonomy（`taxonomy.json`：20 领域/178 族 → 新领域分类）
   - Creator 蒸馏的“证据源”类型（当前是 GitHub 仓库/论文 → 新领域知识源）
   - `repo-routing-metadata.json` 的 schema（repo_id/skill_id/assignments → 新领域身份）
4. **角色模型可直接复用**：Creator（造技能）/ Researcher（用技能）双角色 + `meta/operating/shared` 角色过滤，是通用产品结构。
5. **注意依赖约束**：运行时基于 Pi v0.83.0（pinned 依赖 `pi-agent-core/pi-ai/pi-tui`），Node >= 22.19.0；许可证方面库为 Apache-2.0、CLI 包为 MIT，逐技能独立授权，移植前需核对。

---

## 10. 结语

AREX-Skill 的“壳子”本质 = **“可编程 Agent 运行时 + 技能发现/路由系统 + 知识蒸馏流水线 + 事务式导入”** 的组合，
其产品结构高度模块化、机制与内容解耦。将其移植到其他领域时，**机制层（cli/ + 技能系统 + 路由）几乎可以原样复用，
只需替换内容层（技能图）与领域路由分类，并改造蒸馏流水线的“证据源”适配新领域知识**。
