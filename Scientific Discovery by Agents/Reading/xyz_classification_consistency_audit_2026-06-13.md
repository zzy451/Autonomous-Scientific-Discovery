# XYZ classification consistency audit: explicit multi-agent + search/evolution set

> 核对日期：2026-06-13  
> 核对对象：`xyz_explicit_multi_agent_search_evolution_distribution.md` 中 74 篇 `X2/X3/X4/X5` 且 `Y1-Y5` 的论文。  
> 核对依据：逐篇原文定位证据、`Notes/systems/` 深读笔记，以及少量一手来源复核。  
> 执行状态：用户确认后，已按本审计建议更新 `xyz_literature_classification_matrix.md`，并重新生成 `xyz_cross_distribution.md` 与 `xyz_explicit_multi_agent_search_evolution_distribution.md`。去除 `X0/Y0` 后的显式多智能体搜索/演化集合由 74 篇更新为 72 篇，其中严格 ASD 系统 25 篇，ASD 相关系统 47 篇。

## 总体判断

当前 74 篇的分类整体可以支撑综述写作，尤其是材料发现、代码/证明执行、自动评审、开放能力网络几个证据区已经比较稳。  
但从“显式多智能体 + 搜索/演化”这个严格口径看，仍有少数条目存在三类问题：

1. **X 轴过宽**：有些系统是 agentic / multi-model / expert ensemble，但原文证据不足以证明“显式多智能体组织”。
2. **Y 轴过强**：有些系统只有 iterative generation / evaluation，不一定达到 `Y3` tree/trajectory search 或 `Y5` harness evolution。
3. **Z 轴过满**：有些系统覆盖工具/API/报告/评审，但没有足够证据支持 `Z8` long-horizon iteration 或真实实验闭环。

## 已直接修订的条目

| 文献 | 当前分类 | 建议分类 | 主要理由 | 处理建议 |
|---|---|---|---|---|
| `AI_Scientist_Nature_2026` | `X2-Y3-Z2,Z3,Z4,Z5,Z6,Z7,Z8` | `X0-Y3-Z2,Z3,Z4,Z5,Z6,Z7,Z8` | 当前定位证据是 "complex agentic system" 和 agentic/tree search，足以支撑 `Y3` 和全流程 `Z`，但不足以支撑显式多智能体组织。multi-model 编排、automated reviewer、tree-search node 不等于固定角色 multi-agent team。 | 已从显式多智能体分布表中移出，保留为 ASD 核心 baseline。 |
| `MOSAIC_Chemical_Synthesis_2026` | `X2-Y5-Z3,Z4,Z7,Z8` | `X0-Y2-Z1,Z3,Z7` | 原文核心是 2,498 个 specialized chemical experts 和 protocol generation，不是典型 agent workflow；`Y5` 也偏强，因为专家集合并未在任务中发生 workflow/skill/memory evolution。 | 已从显式 multi-agent search/evolution 集合中移出，正文作为“专家化科学能力/合成协议 substrate”引用。 |
| `MAGenIdeas_2026` | `X2-Y3-Z1,Z2,Z7,Z8` | `X2-Y2-Z1,Z2,Z7,Z8` | 证据显示 multi-agent iterative planning/search、generate/evaluate/refine ideas，强支撑 `X2` 和 `Y2`；但当前 `Y3` 定义要求 tree search / MCTS / trajectory search，摘要级证据不足。 | 已降为 `Y2`。 |
| `AGAPI_Agents_2025` | `X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8` | `X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7` | Agent-Planner-Executor-Summarizer 和 API 编排支持 `X4/Y2`，检索、预测、优化、执行、分析和与实验数据比较支持 `Z1-Z5/Z7`；但当前证据不足以说明长期发现循环、失败复用或持续记忆更新。 | 已删除 `Z8`，作为 tool/API orchestration substrate 使用。 |

## 已修正的证据问题

| 文献 | 问题 | 修正 |
|---|---|---|
| `LLM_Verifier_2025` | 主证据表此前混用了 *The Need for Verification in AI-Driven Scientific Discovery* 的 arXiv 综述证据；但本地笔记和分类实际对应 OpenReview 论文 *Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers*。 | 已在主证据文件与 batch 3 中改为 OpenReview / MAV 证据。分类 `X3-Y2-Z7` 可保留：multiple verifiers 支撑 `X3`，candidate evaluation/selection 支撑 `Y2`，verification 支撑 `Z7`。 |

## 可保留但正文必须降调的条目

| 文献 | 当前分类判断 | 写作边界 |
|---|---|---|
| `PaperOrchestra_2026` | `X2-Y1-Z1,Z6,Z7` 可保留 | 只支撑 reporting / synthesis / manuscript evaluation，不支撑完整 scientific discovery loop。 |
| `AgentReview_2024`、`Generative_Adversarial_Reviews_2024` | `X2-Y1-Z7` 可保留 | 它们是 review / validation substrate，不是发现系统。 |
| `BioAgents_2025` | `X2-Y1-Z1,Z5,Z7` 可保留但偏弱 | `Y1` 应写成有限 self-evaluation / reprocess / troubleshooting，不要写成强闭环自我改进。 |
| `AccelMat_2025` | `X3-Y2-Z2,Z3,Z7` 可保留 | 主要是 hypothesis generation + multi-LLM critics；`Z3` 应解释为实验/设计指向，不要写成执行闭环。 |
| `CycleResearcher_2024` | `X2-Y5-Z1,Z2,Z3,Z6,Z7,Z8` 可保留 | `Y5` 来自 research-review cycle 和 preference training；但科学有效性主要由模拟/自动评审衡量。 |
| `OmniScientist_2025`、`MACC_2026`、`AScience_ASCollab_2025` | `X5-Y5` 可保留 | 更偏开放科研生态、制度架构或协作网络，不宜作为单篇实证发现闭环。 |
| `AutoResearchClaw_2026`、`Claw_AI_Lab_2026`、`ScienceClaw_Infinite_2026` | 当前分类可保留 | 多为新近预印本/平台系统，正文应作为 harness / workflow / ecosystem evidence，而不是成熟自然科学发现结果。 |

## 当前强支撑条目

以下条目的 `X/Y/Z` 坐标与证据匹配度较高，可作为正文主证据优先使用：

- 材料/化学发现主证据：`MARS_Materials_2026`、`MASTER_2025`、`MOFGen_2025`、`Robin_2026`、`Virtual_Lab_2025`、`TopoMAS_2025`、`DREAMS_2025`、`El_Agente_Q_2025`。
- search/evolution 主证据：`CoScientist_2026`、`SciDER_2026`、`EvoSci_2026`、`RD_Agent_2025`、`GeoEvolve_2025`、`OR_Agent_2026`、`AlphaProof_Nexus_2026`。
- formal proof / verification 主证据：`BFS_Prover_V2_2025`、`LeanMarathon_2026`、`Automatic_Textbook_Formalization_2026`、`MA_LoT_2025`、`LLM_Verifier_2025`。
- open capability network 主证据：`Science_Earth_2026`、`ScienceClaw_Infinite_2026`、`SCP_2025`、`AgentRxiv_2025`、`MACC_2026`。
- instrument / physical execution substrate：`Instrument_Agents_2026`、`MARS_Materials_2026`、`Virtual_Lab_2025`、`CRISPR_GPT_2026`。

## 本次已完成

1. 已在 `xyz_literature_classification_matrix.md` 中修改对应条目。
2. 已重新生成 `xyz_cross_distribution.md` 与 `xyz_explicit_multi_agent_search_evolution_distribution.md`。
3. 已更新统计：显式多智能体搜索/演化集合为 72 篇，严格 ASD 系统 25 篇，ASD 相关系统 47 篇。
4. 已同步修正相关 batch 证据和系统笔记，避免后续写作时误用旧坐标。
