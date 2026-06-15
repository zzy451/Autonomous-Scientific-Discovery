# 稀疏 XYZ 坐标补齐候选：去除 X0/Y0 后的显式多智能体搜索/演化文献

> 口径：基于 `xyz_explicit_multi_agent_search_evolution_distribution.md` 的当前设置，即去除 `X0` 与 `Y0`，只考虑 `X2/X3/X4/X5` 与 `Y1/Y2/Y3/Y4/Y5`。
> 目的：针对当前只有 1-2 篇文献命中的坐标，给出联网检索得到的候选论文、拟议 XYZ 分类和补齐价值。
> 状态：本文件最初用于候选筛选；其中 9 篇已进入 `xyz_literature_classification_matrix.md` 并新增系统笔记。仍建议在正式正文引用前继续逐篇加深原文核对。

## 0. 已处理状态

已纳入主矩阵和系统笔记的条目：

- `Mimosa_2026`
- `OR_Agent_2026`
- `SciDER_2026`
- `AScience_ASCollab_2025`
- `OmniScientist_2025`
- `SAGA_2025`
- `PANGAEA_GPT_2026`
- `Code2Math_2026`
- `PaperOrchestra_2026`

审计后降为 Y0 / 边界使用：

- `MM_Agent_2025`：已纳入主矩阵，但作为 `X2-Y0-Z2/Z3/Z4/Z5/Z6/Z7` 的数学建模/报告边界案例，不再用于补 `X2-Y1-Z6`。

## 1. 补齐前最需要处理的稀疏区域

补齐前的稀疏不是均匀分布，而是集中在这些区域：

| 稀疏区域 | 补齐前代表 | 问题 |
|---|---|---|
| `X4-Y4-*` | CoScientist_2026 | 层级式多智能体 + 演化式优化几乎只有 Co-Scientist 一个锚点 |
| `X4-Y5-*` | 补齐前缺席 | 层级式多智能体 + harness/workflow evolution 是本文主线，但矩阵中没有显式坐标 |
| `X5-Y5-*` | Science_Earth_2026, MACC_2026 | 开放能力网络/科研生态系统证据太少 |
| `X3-Y3/Y4-*` | MOOSE_Chem2_2025, AlphaProof_Nexus_2026 | 同角色多实例/并行候选的搜索与演化证据偏少 |
| `X2-Y4-*` | EvoSci_2026, Virtual_Lab_2025 | 固定角色多智能体中的 artifact evolution 仍可补强 |
| `*-Z6` | Agent_Laboratory, SparksMatter, CycleResearcher, Kosmos 等少量 | synthesis/reporting 与多智能体搜索/演化结合不足 |

## 2. 高优先级候选

| 候选论文 | 来源 | 拟议分类 | 可补坐标 | 纳入理由 | 需要核对 |
|---|---|---|---|---|---|
| Mimosa Framework: Toward Evolving Multi-Agent Systems for Scientific Research | arXiv:2603.28986 | ASD 相关系统；`X4-Y5-Z3/Z4/Z5/Z7/Z8` | 补齐 `X4-Y5-*` | 明确提出 evolving multi-agent framework，自动生成 task-specific workflow topology，meta-orchestrator 调度 code-generating agents，并用 judge feedback 迭代 refinement；非常适合支撑 harness/workflow evolution | 主要评测在 ScienceAgentBench，是否算严格 ASD 需看任务是否具有真实发现闭环 |
| OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery | arXiv:2602.13769 | ASD 相关系统；`X4-Y4-Z2/Z3/Z4/Z5/Z7/Z8` | `X4-Y4-*` | 以 tree-based workflow 组织 branching hypothesis generation、systematic backtracking 和 evolutionary-systematic ideation；可以与 CoScientist_2026 共同支撑层级多智能体中的 artifact evolution | 应核对其多智能体角色是否足够明确，以及实验场景是否属于科学发现还是优化算法发现 |
| SciDER: Scientific Data-centric End-to-end Researcher | arXiv:2603.01421 | 严格 ASD 候选；`X2-Y4-Z2/Z3/Z4/Z5/Z7/Z8` | `X2-Y4-*` | 四个 specialized sub-agents 覆盖 ideation、data analysis、experimentation 和 critic；ideation agent 使用 Evolutionary Idea Search，能补固定角色多智能体中的 artifact evolution | 需要确认是否包含报告/论文生成，暂不标 `Z6` |
| Hypothesis Hunting with Evolving Networks of Autonomous Scientific Agents / AScience-ASCollab | arXiv:2510.08619 | 严格 ASD 候选；`X5-Y5-Z2/Z4/Z5/Z7/Z8` | `X5-Y5-*`，尤其 `Z4/Z5/Z8` | 将 discovery 建模为 agents、networks 和 evaluation norms 的相互作用；LLM research agents 自组织成 evolving networks，并 peer-review findings，极适合补“开放/演化网络”证据 | X5 是否应定义为 open capability network 还是 evolving agent network，需要与 Science_Earth 口径对齐 |
| OmniScientist: Toward a Co-evolving Ecosystem of Human and AI Scientists | arXiv:2511.16931 | ASD 相关系统；`X5-Y5-Z1/Z2/Z3/Z4/Z6/Z7/Z8` | `X5-Y5-Z1/Z6` 等 | 明确把科学研究建模为 collaborative ecosystem，包含 structured knowledge system、collaborative research protocol、human participation 和 ScienceArena/Elo evaluation；很适合支撑开放科研生态与 peer-review/reporting | 系统是否已有充分实验验证、是否应列入主矩阵还是基础设施/愿景类证据，需要深读 |
| SAGA / Accelerating Scientific Discovery with Autonomous Goal-evolving Agents | arXiv:2512.21782 | 严格 ASD 候选；暂拟 `X4-Y5-Z2/Z3/Z4/Z5/Z7/Z8` | 补齐 `X4-Y5-*` | bi-level architecture 中外层 LLM agents 分析优化结果、提出新 objectives 并转换为 computable scoring functions，内层做 solution optimization；可以补“目标函数/评分函数本身演化”的 harness evolution | X 轴需谨慎：若外层 agents 没有明确多角色组织，可能降为 `X0-Y5` 或 `X2-Y5` |

## 3. 中优先级候选

| 候选论文 | 来源 | 拟议分类 | 可补坐标 | 纳入理由 | 需要核对 |
|---|---|---|---|---|---|
| PANGAEA-GPT / A Hierarchical Multi-Agent System for Autonomous Discovery in Geoscientific Data Archives | arXiv:2602.21351 | ASD 相关系统；`X4-Y1-Z1/Z4/Z5/Z7` | 补齐 `X4-Y1-*` | centralized Supervisor-Worker topology，data-type-aware routing，sandboxed deterministic code execution 和 execution-feedback self-correction；适合补层级多智能体 + 执行反馈 | 它偏数据发现/分析，不一定覆盖 hypothesis generation 或 long-horizon discovery |
| Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration? | arXiv:2603.03202 | ASD 相关系统；`X2-Y4-Z2/Z3/Z4/Z7/Z8` | `X2-Y4-*` | 三 agent 结构：Evolution Agent、Solvability Verification Agent、Difficulty Verification Agent；通过 code execution 演化并验证数学问题产物 | 产物是数学题生成，不是科学发现本身；适合作为 artifact evolution 边界案例 |
| PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing | arXiv:2604.05018 | ASD 相关系统；`X2-Y1-Z1/Z6/Z7` | `X2-Y1-Z6` | 多 agent 将 unconstrained pre-writing materials 转为 LaTeX manuscripts，并包含 literature synthesis 与 automated evaluators；补多智能体 reporting/synthesis | 主要是论文写作，不应作为 ASD 主证据 |
| MM-Agent: LLM as Agents for Real-world Mathematical Modeling Problem | NeurIPS 2025 / OpenReview | ASD 相关系统；`X2-Y0-Z2/Z3/Z4/Z5/Z6/Z7` | 不进入去除 X0/Y0 后的核心分布 | 将数学建模拆成 problem analysis、model formulation、computational solving、report generation 四阶段；可作为 execution-to-reporting 的固定角色多智能体边界证据 | 原文未见明确搜索/演化或自反思机制，不再用于补 `X2-Y1-Z6` |

## 4. 已产生的补齐效果

纳入 9 篇后，矩阵结构已经发生这些改善：

| 稀疏坐标 | 当前文献 | 推荐补充 | 补齐效果 |
|---|---|---|---|
| `X4-Y4-Z2/Z3/Z7/Z8` | CoScientist_2026 | OR-Agent_2026 | 层级式多智能体 + artifact evolution 不再只靠 Co-Scientist |
| `X4-Y5-Z3/Z4/Z5/Z7/Z8` | 0 | Mimosa_2026, SAGA_2025 | 第 5 章 harness/workflow evolution 得到强支撑 |
| `X5-Y5-Z1/Z6` | Science_Earth_2026 / MACC_2026 少量 | OmniScientist_2025, AScience_ASCollab_2025 | 开放科研生态、peer review、reporting 与 capability/evaluation network 更稳 |
| `X2-Y4-Z3/Z5` | Virtual_Lab_2025 | SciDER_2026, Code2Math_2026 | 固定角色多智能体中的 artifact evolution 从 ideation 扩展到 data/code/math artifact |
| `X2-Y1-Z6` | Agent_Laboratory_2024, SparksMatter_2025 | PaperOrchestra_2026 | reporting/synthesis 仍主要依赖少量端到端系统；MM-Agent 审计后降为 Y0 边界案例 |

## 5. 当前不建议优先纳入的相邻工作

- 纯 benchmark 或纯评测，如只评测 scientific reasoning 而没有 workflow/system 设计的论文，不应为了补坐标进入主矩阵。
- 通用 multi-agent RAG、通用 agent architecture search 或通用 self-improvement，如果没有科学任务、科学产物或验证边界，最多作为基础设施背景。
- 纯数学/教育题生成系统应谨慎使用；Code2Math 可以作为 artifact evolution 边界案例，但不应压过 AlphaProof Nexus、OpenAI Unit Distance 等真正数学发现/验证案例。
- `SciAgent: A Unified Multi-Agent System for Generalistic Scientific Reasoning` 不建议纳入当前矩阵：arXiv 页面显示 withdrawn，且其任务更偏科学竞赛推理而非 discovery workflow。
- `MA-LoT` 已作为 ASD 相关系统纳入，但审计后从 `X2-Y3-Z3/Z4/Z7/Z8` 收紧为 `X2-Y1-Z3/Z4/Z7`：它能支撑 prover/verifier 与 Lean feedback 的多代理修正，不应再写成树搜索或长周期发现主证据。

## 6. 来源链接

- Mimosa Framework: https://arxiv.org/abs/2603.28986
- OR-Agent: https://arxiv.org/abs/2602.13769
- SciDER: https://arxiv.org/abs/2603.01421
- AScience / ASCollab: https://arxiv.org/abs/2510.08619
- OmniScientist: https://arxiv.org/abs/2511.16931
- SAGA: https://arxiv.org/abs/2512.21782
- PANGAEA-GPT: https://arxiv.org/abs/2602.21351
- Code2Math: https://arxiv.org/abs/2603.03202
- PaperOrchestra: https://arxiv.org/abs/2604.05018
- MM-Agent: https://openreview.net/forum?id=o8n5oNDsiq

## 7. 2026-06-12 追加补齐后的状态

本轮在 `xyz_literature_classification_matrix.md` 中继续补入材料发现、开放能力网络、形式化证明、药物发现、量子化学、植物表型和自动科研工作流文献，并重新生成 `xyz_cross_distribution.md` 与 `xyz_explicit_multi_agent_search_evolution_distribution.md`。

当前主矩阵共有 133 篇：

| 类型 | 数量 |
|---|---:|
| 严格 ASD 系统 | 41 |
| ASD 相关系统 | 92 |
| 合计 | 133 |

去除 `X0` 和 `Y0` 后，当前显式多智能体搜索/演化文献共有 74 篇，其中严格 ASD 系统 26 篇，ASD 相关系统 48 篇。

新增或修正后最明显的变化：

| 区域 | 新增支撑 |
|---|---|
| `X5-Y5` | ScienceClaw + Infinite、SCP、AgentRxiv，使开放能力网络不再只依赖 Science Earth / OmniScientist / MACC |
| `X4-Y1` | DREAMS、El Agente Q、PANGAEA-GPT，加强层级式多智能体中的执行反馈、错误恢复和自修正；PhenoAssistant 审计后作为 Y0 边界案例 |
| `X4-Y2` | AGAPI-Agents、MADD、eNRRCrew，加强层级式候选生成、工具编排和科学计算/药物发现证据；TopoMAS 审计后移入 `X4-Y5` |
| `X2-Y3` | PriM 重分类为 MCTS 驱动的 `Y3`，并加入 DrugMCTS；MA-LoT 审计后收紧为 `X2-Y1` |
| `X4-Y4` | GeoEvolve 从 `X2-Y4` 调整为 `X4-Y4`，加强层级式代码/模型产物的演化式优化 |
| `X3-Y2 / X4-Y3` | AccelMat、Automatic Textbook Formalization 补充同类 critic / proof worker 并行证据；LeanMarathon 审计后移入 `X4-Y3` |

仍未能补齐到每个坐标 4 篇以上的区域主要集中在：

1. `X3-Y4-*`：目前仍主要依赖 AlphaProof Nexus。若严格要求显式同类 agent 实例，而不是普通 population search，候选很少。
2. `X4-Y3-*` 与 `X4-Y4-*`：LeanMarathon 是当前 `X4-Y3` 的主证据；CoScientist、GeoEvolve 与 OR-Agent 是 `X4-Y4` 主证据，但多数 Z 坐标仍少于 4 篇。
3. `Z6` reporting 相关坐标：`X2-Y2-Z6`、`X2-Y3-Z6`、`X2-Y5-Z6`、`X4-Y5-Z6` 仍偏少，说明自动报告/论文写作不是当前多智能体 ASD 的主证据区。

口径更新：审计后将 `MA-LoT` 从 `X2-Y3` 收紧为 `X2-Y1`，将 `MM_Agent_2025` 和 `PhenoAssistant_2026` 降为 Y0 边界案例；这使核心分布更保守，但更符合当前 XYZ 分类标准。

结论：如果坚持“只列出的坐标都要 >= 4 篇”，当前文献生态还补不齐；更合理的写法是把 `X3-Y4`、`X4-Y4` 和 `Z6` 相关坐标写成 emerging / boundary evidence，而不是强行扩展口径。

