# 新增文献 XYZ 分类审计记录（2026-06-12）

> 目的：核对近期补入 `xyz_literature_classification_matrix.md` 的文献是否符合当前 XYZ 分类标准，尤其避免把普通多阶段 pipeline 误标为搜索/演化机制，或把共享平台误标为验证/评审闭环。

## 审计口径

- X 轴只标注系统的主导多智能体组织形态：固定角色、多实例并行、层级调度或开放能力网络。
- Y 轴优先标注最能代表系统差异化的反馈/搜索/演化机制。
- `Y1-Y4` 主要对应 scientific research artifacts 的反思、筛选、搜索或演化。
- `Y5` 只用于 workflow、skill、memory、agent capability、tool/capability network 等 harness/capability 层更新。
- 没有明确反思、搜索、候选筛选或演化机制的显式多智能体系统，应保守标为 `Y0`。
- Z 轴只标注原文有较强证据支撑的科学发现阶段；复现支持、共享平台或结果展示不自动等同于 `Z7` 或 `Z8`。

## 已修正条目

| 文献 | 原分类 | 修正后分类 | 修正理由 |
|---|---|---|---|
| `Materealize_2026` | `X2-Y2-Z1/Z2/Z3/Z4/Z5/Z6/Z7/Z8` | `X2-Y2-Z1/Z2/Z3/Z4/Z5/Z7/Z8` | 原文支撑候选设计、合成规划、工具执行和验证，但不宜强标为报告/论文生成系统，移除 `Z6`。 |
| `TopoMAS_2025` | `X4-Y2-Z1/Z2/Z3/Z4/Z5/Z7/Z8` | `X4-Y5-Z1/Z2/Z3/Z4/Z5/Z7/Z8` | 动态知识图谱和 memory 更新会改变后续检索/推理环境，主机制更接近 harness / memory evolution。 |
| `AgentRxiv_2025` | `X5-Y5-Z1/Z5/Z6/Z7/Z8` | `X5-Y5-Z1/Z5/Z6/Z8` | 共享 preprint server 支撑开放科研产物网络，但本身不等同于 peer-review / validation，移除 `Z7`。 |
| `eNRRCrew_2025` | `X2-Y2-Z1/Z2/Z5/Z7/Z8` | `X4-Y2-Z1/Z2/Z5/Z7/Z8` | orchestrator 动态分配 yield predictor、FE predictor、GraphRAG retriever、CSV/code agents，层级调度证据强于固定平行角色。 |
| `MM_Agent_2025` | `X2-Y1-Z2/Z3/Z4/Z5/Z6/Z7` | `X2-Y0-Z2/Z3/Z4/Z5/Z6/Z7` | 系统主要是阶段化数学建模与报告工作流，未见明确 reflection/search/evolution 机制。 |
| `GeoEvolve_2025` | `X2-Y4-Z1/Z3/Z4/Z5/Z7/Z8` | `X4-Y4-Z1/Z3/Z4/Z5/Z7/Z8` | outer agentic controller + inner code evolver 构成两层演化搜索组织，层级性是核心证据。 |
| `PhenoAssistant_2026` | `X4-Y1-Z3/Z4/Z5/Z7/Z8` | `X4-Y0-Z3/Z4/Z5/Z7` | central manager 编排工具和分析 agents，但未见明确反思/搜索/演化；复现支持也不等同于长周期 discovery iteration。 |
| `LeanMarathon_2026` | `X3-Y3-Z3/Z4/Z7/Z8` | `X4-Y3-Z3/Z4/Z7/Z8` | two-stage orchestrator 协调 construct/audit/prove/repair agents，并沿 proof DAG 调度子任务，层级调度强于同类实例口径。 |
| `MA_LoT_2025` | `X2-Y3-Z3/Z4/Z7/Z8` | `X2-Y1-Z3/Z4/Z7` | 主要证据是 prover/corrector 或 Lean feedback 的多轮修正，不宜强标为 tree/MCTS search；多轮修正保留在 `Y1`，移除 `Z8`。 |

## 保留当前分类的条目

| 文献 | 当前分类 | 保留理由 |
|---|---|---|
| `AtomAgents_2025` | `X2-Y2-Z1/Z2/Z3/Z4/Z5/Z7/Z8` | 固定领域/工具角色协作，生成并筛选材料候选，包含仿真、代码执行和验证。 |
| `DREAMS_2025` | `X4-Y1-Z3/Z4/Z5/Z7/Z8` | central planner 调度结构生成、DFT/HPC/error-handling agents，错误恢复和重规划支撑 `Y1`。 |
| `ScienceClaw_Infinite_2026` | `X5-Y5-Z1/Z3/Z4/Z5/Z6/Z7/Z8` | decentralized agents、skill registry、artifact DAG 和 global index 支撑开放科学能力/产物交换生态。 |
| `AGAPI_Agents_2025` | `X4-Y2-Z1/Z2/Z3/Z4/Z5/Z7/Z8` | Agent-Planner-Executor-Summarizer 架构统一多材料 API，候选/工具链筛选与层级编排证据较强。 |
| `AutoResearchClaw_2026` | `X2-Y5-Z1/Z2/Z3/Z4/Z5/Z6/Z7/Z8` | structured multi-agent debate、自愈 executor 与 cross-run evolution 更偏 harness/capability 层更新。 |
| `Claw_AI_Lab_2026` | `X4-Y5-Z2/Z3/Z4/Z5/Z6/Z7/Z8` | hierarchical research lab、Claw-Code Harness、artifact inspection 与 rollback/resume 支撑可迭代 harness。 |
| `MADD_2025` | `X4-Y2-Z3/Z4/Z5/Z7` | Decomposer/Orchestrator/Summarizer 形成层级药物发现 pipeline，候选筛选和 docking/ML 评价清楚。 |
| `Mozi_2026` | `X4-Y5-Z2/Z3/Z4/Z5/Z7/Z8` | supervisor-worker control plane 与 stateful skill graphs 指向 harness/capability governance。 |
| `SCP_2025` | `X5-Y5-Z1/Z3/Z4/Z5/Z7/Z8` | federated Science Context Protocol 连接工具、模型、数据和仪器，符合开放能力网络。 |
| `DrugMCTS_2025` | `X2-Y3-Z1/Z2/Z5/Z7/Z8` | specialized agents 与 MCTS 结合，适合作为固定角色多智能体中的候选路径搜索证据。 |
| `RD_Agent_2025` | `X2-Y4-Z2/Z3/Z4/Z5/Z7/Z8` | Researcher/Developer 双代理通过 exploration traces、代码实现和性能反馈形成 artifact-level evolution。 |
| `El_Agente_Q_2025` | `X4-Y1-Z3/Z4/Z5/Z7/Z8` | hierarchical cognitive architecture、工具选择、执行、post-analysis 和 in situ debugging 支撑层级反思修正。 |
| `AccelMat_2025` | `X3-Y2-Z2/Z3/Z7` | 同类 critic ensemble 评价材料假设 relevance、novelty、feasibility，适合作为并行候选/评审证据。 |
| `BFS_Prover_V2_2025` | `X3-Y3-Z3/Z4/Z7/Z8` | planner-enhanced multi-agent tree search 与并行 prover agents 共享 proof cache，符合 `X3-Y3`。 |
| `Automatic_Textbook_Formalization_2026` | `X3-Y2-Z3/Z4/Z7/Z8` | 大规模同类 agents 并行 formalize、提交、审查和合并 Lean 产物，符合并行候选/筛选口径。 |

## 审计后的统计影响

| 项目 | 审计后数量 |
|---|---:|
| 主矩阵总文献 | 133 |
| 严格 ASD 系统 | 41 |
| ASD 相关系统 | 92 |
| 去除 `X0` 与 `Y0` 后的显式多智能体搜索/演化文献 | 74 |
| 其中严格 ASD 系统 | 26 |
| 其中 ASD 相关系统 | 48 |

主要变化：

- `MM_Agent_2025` 与 `PhenoAssistant_2026` 从核心分布退出，作为“有多智能体组织但无明确搜索/演化机制”的 `Y0` 边界案例。
- `eNRRCrew_2025`、`GeoEvolve_2025`、`LeanMarathon_2026` 更能支撑层级式多智能体组织，因此从 X2/X3 调入 `X4`。
- `TopoMAS_2025` 从 candidate selection 口径转入 memory / harness evolution 口径，补强 `X4-Y5`。
- `MA_LoT_2025` 从 tree search 收紧为 Lean-feedback 修正，降低了 `X2-Y3` 的过度扩张风险。

## 参考来源

- AtomAgents: https://arxiv.org/abs/2407.10022
- AgentRxiv: https://arxiv.org/abs/2503.18102
- MA-LoT: https://arxiv.org/abs/2503.03205
- PhenoAssistant: https://arxiv.org/abs/2504.19818
- RD-Agent: https://arxiv.org/abs/2505.14738
- GeoEvolve: https://arxiv.org/abs/2509.21593
- eNRRCrew: https://doi.org/10.1093/nsr/nwaf372
- ScienceClaw + Infinite: https://arxiv.org/abs/2603.14312
- Mozi: https://arxiv.org/abs/2603.03655
- LeanMarathon: https://arxiv.org/html/2606.05400v1
