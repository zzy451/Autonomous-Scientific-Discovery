# XYZ 交叉分布（去除 X0 与 Y0）：显式多智能体搜索/演化组合

> 口径：基于 `xyz_literature_classification_matrix.md`，去除所有 `X0` 文献，并去除所有 `Y0` 文献，只保留 `X2/X3/X4/X5` 与 `Y1/Y2/Y3/Y4/Y5`。
> 文献数量：72 篇，其中严格 ASD 系统 25 篇，ASD 相关系统 47 篇。
> 展开方式：一篇文献只有一个 X、一个 Y，但可对应多个 Z；因此同一篇文献可能出现在多个 `Xn-Yn-Zn` 组合下。
> 本表只列出有文献命中的组合，并在每个组合后标注其含义。

## 坐标含义

本文件只讨论已经去除 `X0` 与 `Y0` 后的坐标。因此，这里的每一篇文献都同时满足两个条件：第一，系统具有显式多智能体组织形态；第二，系统包含某种反馈、搜索、演化或能力更新机制。

### X 轴：Multi-Agent 组织形态

X 轴描述“多智能体中的多”如何被组织起来，即科学劳动、能力和责任如何在多个 agents 之间分配。

| 编码 | 名称 | 含义 | 典型信号 |
|---|---|---|---|
| `X2` | 固定角色多智能体 | 多个明确分工的 agents 协作完成科研任务，例如 researcher、planner、coder、critic、reviewer、executor、analyst | 角色固定、职责互补、通常是封闭团队或工作流 |
| `X3` | 同角色多实例 / 并行候选 | 多个同类 agents 或同类候选并行探索、生成、评审或验证同一类科研产物 | 多个 reviewers、provers、hypothesis agents、parallel workers、candidate branches |
| `X4` | 层级式多智能体 | coordinator、manager、supervisor 或 orchestrator 调度多个 worker / specialist agents | supervisor-worker、lead-agent、manager-worker、central planner、hierarchical routing |
| `X5` | 开放能力网络 | 多智能体不再只是单个封闭团队，而是开放的科学能力、工具、产物、协议或协作网络 | capability network、open agent ecosystem、artifact exchange、shared preprint / skill / tool network |

### Y 轴：反馈、搜索与演化机制

Y 轴描述系统如何让科研产物或 agentic harness 变得更好。`Y1-Y4` 主要作用在 scientific research artifacts 上，例如 hypothesis、idea、code、proof、experiment plan、paper；`Y5` 则作用在 workflow、skill、memory、tool network 或 agent capability 等 harness/capability 层。

| 编码 | 名称 | 含义 | 演化对象 |
|---|---|---|---|
| `Y1` | 反思 / 自我修正 | 系统生成结果后进行 critique、reflection、debug、revise、failure detection 或 rerun | 单个或少量科研产物的质量改进 |
| `Y2` | 候选生成与筛选 | 系统生成多个候选，并通过 ranking、scoring、review、comparison 或 selection 选择较优候选 | hypotheses、ideas、molecules、materials、plans、reviews |
| `Y3` | 树搜索 / MCTS / trajectory search | 系统显式组织搜索树、轨迹、分支或多步路径，探索科研产物的可能空间 | code path、proof path、hypothesis path、experiment trajectory |
| `Y4` | 演化式优化 | 系统使用 mutation、recombination、population、Elo、tournament、archive、elite selection 等机制优化科研产物 | artifact population，如 ideas、algorithms、proofs、code、materials candidates |
| `Y5` | harness / capability evolution | 被更新的不只是科研产物，而是 workflow、skill、memory、agent capability、tool ecosystem 或开放能力网络本身 | agentic harness、capability graph、skill library、memory、workflow topology、open network |

### Z 轴：自主科学发现流程阶段

Z 轴描述系统覆盖科学发现流程中的哪些阶段。一篇文献可以对应多个 Z，因为同一个系统可能同时做文献 grounding、假设生成、实验设计、执行、验证和迭代。

| 编码 | 阶段 | 含义 |
|---|---|---|
| `Z1` | Knowledge Grounding / Literature Review | 文献检索、证据 grounding、知识图谱、上下文构建、已有结果整理 |
| `Z2` | Problem Formulation / Hypothesis Generation | 问题形成、研究问题提出、假设生成、idea generation、candidate proposal |
| `Z3` | Experiment / Simulation / Code / Proof Design | 实验方案、仿真方案、代码方案、工具调用计划、证明草图或形式化计划 |
| `Z4` | Execution | 代码执行、工具调用、仿真运行、实验执行、机器人操作、证明尝试 |
| `Z5` | Result Analysis | 数据分析、结果解释、错误诊断、性能归因、实验/仿真输出分析 |
| `Z6` | Synthesis / Reporting | 报告生成、论文写作、preprint、LaTeX manuscript、研究总结、知识综合 |
| `Z7` | Verification / Validation / Review | 引用验证、代码复现、形式证明、专家评审、实验验证、peer-review 式检查 |
| `Z8` | Iteration / Long-Horizon Discovery | 多轮循环、长周期项目管理、失败分支复用、记忆更新、持续 discovery loop |

### 组合读法

一个坐标 `Xn-Yn-Zn` 可以读作：某类多智能体组织形态，在某类反馈/搜索/演化机制下，覆盖某个科学发现阶段。例如 `X4-Y2-Z4` 表示“层级式多智能体通过候选生成与筛选机制支撑执行阶段”，常见于 supervisor 调度多个工具/实验/仿真 workers 来执行并比较候选方案。

## 交叉分布

| XYZ 组合 | 组合含义 | 数量 | 对应文献 |
|---|---|---:|---|
| X2-Y1-Z1 | 固定角色多智能体 + 反思 / 自我修正 + 知识 grounding / 文献综述 | 8 | Agent_Laboratory_2024, BioAgents_2025, GenoMAS_2025, MLR_Copilot_2024, PaperOrchestra_2026, SparksMatter_2025, TAIS_2024, VirSci_2024 |
| X2-Y1-Z2 | 固定角色多智能体 + 反思 / 自我修正 + 问题形成 / 假设生成 | 6 | Agent_Laboratory_2024, Curie_2025, MAESTRO_2026, MLR_Copilot_2024, SparksMatter_2025, VirSci_2024 |
| X2-Y1-Z3 | 固定角色多智能体 + 反思 / 自我修正 + 实验、仿真、代码或证明设计 | 10 | Agent_Laboratory_2024, CRISPR_GPT_2026, Curie_2025, GenoMAS_2025, IMPROVE_2025, MA_LoT_2025, MAESTRO_2026, MLR_Copilot_2024, SparksMatter_2025, TAIS_2024 |
| X2-Y1-Z4 | 固定角色多智能体 + 反思 / 自我修正 + 执行：代码、工具、实验、证明或机器人操作 | 9 | Agent_Laboratory_2024, CRISPR_GPT_2026, Curie_2025, GenoMAS_2025, IMPROVE_2025, MA_LoT_2025, MAESTRO_2026, MLR_Copilot_2024, TAIS_2024 |
| X2-Y1-Z5 | 固定角色多智能体 + 反思 / 自我修正 + 结果分析 / 错误诊断 | 10 | Agent_Laboratory_2024, BioAgents_2025, CRISPR_GPT_2026, Curie_2025, GenoMAS_2025, IMPROVE_2025, MAESTRO_2026, MLR_Copilot_2024, SparksMatter_2025, TAIS_2024 |
| X2-Y1-Z6 | 固定角色多智能体 + 反思 / 自我修正 + 综合 / 报告 / 论文写作 | 3 | Agent_Laboratory_2024, PaperOrchestra_2026, SparksMatter_2025 |
| X2-Y1-Z7 | 固定角色多智能体 + 反思 / 自我修正 + 验证 / validation / review | 15 | Agent_Laboratory_2024, AgentReview_2024, BioAgents_2025, CRISPR_GPT_2026, Curie_2025, Generative_Adversarial_Reviews_2024, GenoMAS_2025, IMPROVE_2025, MA_LoT_2025, MAESTRO_2026, MLR_Copilot_2024, PaperOrchestra_2026, SparksMatter_2025, TAIS_2024, VirSci_2024 |
| X2-Y1-Z8 | 固定角色多智能体 + 反思 / 自我修正 + 迭代 / 长周期发现 | 6 | GenoMAS_2025, IMPROVE_2025, MAESTRO_2026, MLR_Copilot_2024, SparksMatter_2025, VirSci_2024 |
| X2-Y2-Z1 | 固定角色多智能体 + 候选生成与筛选 + 知识 grounding / 文献综述 | 8 | AI_Researcher_HKU_2025, AstroAgents_2025, AtomAgents_2025, MAGenIdeas_2026, Materealize_2026, MOOSE_Chem_2024, ProtAgents_2024, ResearchAgent_2025 |
| X2-Y2-Z2 | 固定角色多智能体 + 候选生成与筛选 + 问题形成 / 假设生成 | 8 | AI_Researcher_HKU_2025, AstroAgents_2025, AtomAgents_2025, MAGenIdeas_2026, Materealize_2026, MOFGen_2025, MOOSE_Chem_2024, ResearchAgent_2025 |
| X2-Y2-Z3 | 固定角色多智能体 + 候选生成与筛选 + 实验、仿真、代码或证明设计 | 5 | AI_Researcher_HKU_2025, AtomAgents_2025, Materealize_2026, MOFGen_2025, ProtAgents_2024 |
| X2-Y2-Z4 | 固定角色多智能体 + 候选生成与筛选 + 执行：代码、工具、实验、证明或机器人操作 | 4 | AtomAgents_2025, Materealize_2026, MOFGen_2025, ProtAgents_2024 |
| X2-Y2-Z5 | 固定角色多智能体 + 候选生成与筛选 + 结果分析 / 错误诊断 | 5 | AstroAgents_2025, AtomAgents_2025, Materealize_2026, MOFGen_2025, ProtAgents_2024 |
| X2-Y2-Z6 | 固定角色多智能体 + 候选生成与筛选 + 综合 / 报告 / 论文写作 | 2 | AI_Researcher_HKU_2025, ResearchAgent_2025 |
| X2-Y2-Z7 | 固定角色多智能体 + 候选生成与筛选 + 验证 / validation / review | 9 | AI_Researcher_HKU_2025, AstroAgents_2025, AtomAgents_2025, MAGenIdeas_2026, Materealize_2026, MOFGen_2025, MOOSE_Chem_2024, ProtAgents_2024, ResearchAgent_2025 |
| X2-Y2-Z8 | 固定角色多智能体 + 候选生成与筛选 + 迭代 / 长周期发现 | 4 | AtomAgents_2025, MAGenIdeas_2026, Materealize_2026, MOFGen_2025 |
| X2-Y3-Z1 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 知识 grounding / 文献综述 | 3 | DrugMCTS_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z2 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 问题形成 / 假设生成 | 3 | DrugMCTS_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z3 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 实验、仿真、代码或证明设计 | 3 | KompeteAI_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z4 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 执行：代码、工具、实验、证明或机器人操作 | 2 | KompeteAI_2025, PriM_2025 |
| X2-Y3-Z5 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 结果分析 / 错误诊断 | 4 | DrugMCTS_2025, KompeteAI_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z6 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 综合 / 报告 / 论文写作 | 1 | PriM_2025 |
| X2-Y3-Z7 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 验证 / validation / review | 4 | DrugMCTS_2025, KompeteAI_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z8 | 固定角色多智能体 + 树搜索 / MCTS / trajectory search + 迭代 / 长周期发现 | 3 | DrugMCTS_2025, PiFlow_2025, PriM_2025 |
| X2-Y4-Z1 | 固定角色多智能体 + 演化式优化 + 知识 grounding / 文献综述 | 2 | EvoSci_2026, Virtual_Lab_2025 |
| X2-Y4-Z2 | 固定角色多智能体 + 演化式优化 + 问题形成 / 假设生成 | 5 | Code2Math_2026, EvoSci_2026, RD_Agent_2025, SciDER_2026, Virtual_Lab_2025 |
| X2-Y4-Z3 | 固定角色多智能体 + 演化式优化 + 实验、仿真、代码或证明设计 | 4 | Code2Math_2026, RD_Agent_2025, SciDER_2026, Virtual_Lab_2025 |
| X2-Y4-Z4 | 固定角色多智能体 + 演化式优化 + 执行：代码、工具、实验、证明或机器人操作 | 3 | Code2Math_2026, RD_Agent_2025, SciDER_2026 |
| X2-Y4-Z5 | 固定角色多智能体 + 演化式优化 + 结果分析 / 错误诊断 | 3 | RD_Agent_2025, SciDER_2026, Virtual_Lab_2025 |
| X2-Y4-Z7 | 固定角色多智能体 + 演化式优化 + 验证 / validation / review | 5 | Code2Math_2026, EvoSci_2026, RD_Agent_2025, SciDER_2026, Virtual_Lab_2025 |
| X2-Y4-Z8 | 固定角色多智能体 + 演化式优化 + 迭代 / 长周期发现 | 5 | Code2Math_2026, EvoSci_2026, RD_Agent_2025, SciDER_2026, Virtual_Lab_2025 |
| X2-Y5-Z1 | 固定角色多智能体 + harness / capability evolution + 知识 grounding / 文献综述 | 7 | AutoResearchClaw_2026, CycleResearcher_2024, Deep_Research_2026, EvoScientist_2026, Instrument_Agents_2026, Kosmos_2025, SciAgents_2024 |
| X2-Y5-Z2 | 固定角色多智能体 + harness / capability evolution + 问题形成 / 假设生成 | 6 | AutoResearchClaw_2026, CycleResearcher_2024, Deep_Research_2026, EvoScientist_2026, Kosmos_2025, SciAgents_2024 |
| X2-Y5-Z3 | 固定角色多智能体 + harness / capability evolution + 实验、仿真、代码或证明设计 | 8 | AutoResearchClaw_2026, CycleResearcher_2024, Deep_Research_2026, EvoScientist_2026, Instrument_Agents_2026, Kosmos_2025, MLZero_2025, SciAgents_2024 |
| X2-Y5-Z4 | 固定角色多智能体 + harness / capability evolution + 执行：代码、工具、实验、证明或机器人操作 | 6 | AutoResearchClaw_2026, Deep_Research_2026, EvoScientist_2026, Instrument_Agents_2026, Kosmos_2025, MLZero_2025 |
| X2-Y5-Z5 | 固定角色多智能体 + harness / capability evolution + 结果分析 / 错误诊断 | 7 | AutoResearchClaw_2026, Deep_Research_2026, EvoScientist_2026, Instrument_Agents_2026, Kosmos_2025, MLZero_2025, SciAgents_2024 |
| X2-Y5-Z6 | 固定角色多智能体 + harness / capability evolution + 综合 / 报告 / 论文写作 | 3 | AutoResearchClaw_2026, CycleResearcher_2024, Kosmos_2025 |
| X2-Y5-Z7 | 固定角色多智能体 + harness / capability evolution + 验证 / validation / review | 8 | AutoResearchClaw_2026, CycleResearcher_2024, Deep_Research_2026, EvoScientist_2026, Instrument_Agents_2026, Kosmos_2025, MLZero_2025, SciAgents_2024 |
| X2-Y5-Z8 | 固定角色多智能体 + harness / capability evolution + 迭代 / 长周期发现 | 8 | AutoResearchClaw_2026, CycleResearcher_2024, Deep_Research_2026, EvoScientist_2026, Instrument_Agents_2026, Kosmos_2025, MLZero_2025, SciAgents_2024 |
| X3-Y2-Z2 | 同角色多实例 / 并行候选 + 候选生成与筛选 + 问题形成 / 假设生成 | 1 | AccelMat_2025 |
| X3-Y2-Z3 | 同角色多实例 / 并行候选 + 候选生成与筛选 + 实验、仿真、代码或证明设计 | 2 | AccelMat_2025, Automatic_Textbook_Formalization_2026 |
| X3-Y2-Z4 | 同角色多实例 / 并行候选 + 候选生成与筛选 + 执行：代码、工具、实验、证明或机器人操作 | 1 | Automatic_Textbook_Formalization_2026 |
| X3-Y2-Z7 | 同角色多实例 / 并行候选 + 候选生成与筛选 + 验证 / validation / review | 3 | AccelMat_2025, Automatic_Textbook_Formalization_2026, LLM_Verifier_2025 |
| X3-Y2-Z8 | 同角色多实例 / 并行候选 + 候选生成与筛选 + 迭代 / 长周期发现 | 1 | Automatic_Textbook_Formalization_2026 |
| X3-Y3-Z1 | 同角色多实例 / 并行候选 + 树搜索 / MCTS / trajectory search + 知识 grounding / 文献综述 | 1 | MOOSE_Chem2_2025 |
| X3-Y3-Z2 | 同角色多实例 / 并行候选 + 树搜索 / MCTS / trajectory search + 问题形成 / 假设生成 | 1 | MOOSE_Chem2_2025 |
| X3-Y3-Z3 | 同角色多实例 / 并行候选 + 树搜索 / MCTS / trajectory search + 实验、仿真、代码或证明设计 | 2 | BFS_Prover_V2_2025, MOOSE_Chem2_2025 |
| X3-Y3-Z4 | 同角色多实例 / 并行候选 + 树搜索 / MCTS / trajectory search + 执行：代码、工具、实验、证明或机器人操作 | 1 | BFS_Prover_V2_2025 |
| X3-Y3-Z7 | 同角色多实例 / 并行候选 + 树搜索 / MCTS / trajectory search + 验证 / validation / review | 2 | BFS_Prover_V2_2025, MOOSE_Chem2_2025 |
| X3-Y3-Z8 | 同角色多实例 / 并行候选 + 树搜索 / MCTS / trajectory search + 迭代 / 长周期发现 | 1 | BFS_Prover_V2_2025 |
| X3-Y4-Z3 | 同角色多实例 / 并行候选 + 演化式优化 + 实验、仿真、代码或证明设计 | 1 | AlphaProof_Nexus_2026 |
| X3-Y4-Z4 | 同角色多实例 / 并行候选 + 演化式优化 + 执行：代码、工具、实验、证明或机器人操作 | 1 | AlphaProof_Nexus_2026 |
| X3-Y4-Z7 | 同角色多实例 / 并行候选 + 演化式优化 + 验证 / validation / review | 1 | AlphaProof_Nexus_2026 |
| X3-Y4-Z8 | 同角色多实例 / 并行候选 + 演化式优化 + 迭代 / 长周期发现 | 1 | AlphaProof_Nexus_2026 |
| X4-Y1-Z1 | 层级式多智能体 + 反思 / 自我修正 + 知识 grounding / 文献综述 | 1 | PANGAEA_GPT_2026 |
| X4-Y1-Z3 | 层级式多智能体 + 反思 / 自我修正 + 实验、仿真、代码或证明设计 | 2 | DREAMS_2025, El_Agente_Q_2025 |
| X4-Y1-Z4 | 层级式多智能体 + 反思 / 自我修正 + 执行：代码、工具、实验、证明或机器人操作 | 3 | DREAMS_2025, El_Agente_Q_2025, PANGAEA_GPT_2026 |
| X4-Y1-Z5 | 层级式多智能体 + 反思 / 自我修正 + 结果分析 / 错误诊断 | 3 | DREAMS_2025, El_Agente_Q_2025, PANGAEA_GPT_2026 |
| X4-Y1-Z7 | 层级式多智能体 + 反思 / 自我修正 + 验证 / validation / review | 3 | DREAMS_2025, El_Agente_Q_2025, PANGAEA_GPT_2026 |
| X4-Y1-Z8 | 层级式多智能体 + 反思 / 自我修正 + 迭代 / 长周期发现 | 2 | DREAMS_2025, El_Agente_Q_2025 |
| X4-Y2-Z1 | 层级式多智能体 + 候选生成与筛选 + 知识 grounding / 文献综述 | 4 | AGAPI_Agents_2025, eNRRCrew_2025, MARS_Materials_2026, Robin_2026 |
| X4-Y2-Z2 | 层级式多智能体 + 候选生成与筛选 + 问题形成 / 假设生成 | 5 | AGAPI_Agents_2025, eNRRCrew_2025, MARS_Materials_2026, MASTER_2025, Robin_2026 |
| X4-Y2-Z3 | 层级式多智能体 + 候选生成与筛选 + 实验、仿真、代码或证明设计 | 5 | AGAPI_Agents_2025, MADD_2025, MARS_Materials_2026, MASTER_2025, Robin_2026 |
| X4-Y2-Z4 | 层级式多智能体 + 候选生成与筛选 + 执行：代码、工具、实验、证明或机器人操作 | 5 | AGAPI_Agents_2025, MADD_2025, MARS_Materials_2026, MASTER_2025, Robin_2026 |
| X4-Y2-Z5 | 层级式多智能体 + 候选生成与筛选 + 结果分析 / 错误诊断 | 6 | AGAPI_Agents_2025, eNRRCrew_2025, MADD_2025, MARS_Materials_2026, MASTER_2025, Robin_2026 |
| X4-Y2-Z7 | 层级式多智能体 + 候选生成与筛选 + 验证 / validation / review | 6 | AGAPI_Agents_2025, eNRRCrew_2025, MADD_2025, MARS_Materials_2026, MASTER_2025, Robin_2026 |
| X4-Y2-Z8 | 层级式多智能体 + 候选生成与筛选 + 迭代 / 长周期发现 | 4 | eNRRCrew_2025, MARS_Materials_2026, MASTER_2025, Robin_2026 |
| X4-Y3-Z3 | 层级式多智能体 + 树搜索 / MCTS / trajectory search + 实验、仿真、代码或证明设计 | 1 | LeanMarathon_2026 |
| X4-Y3-Z4 | 层级式多智能体 + 树搜索 / MCTS / trajectory search + 执行：代码、工具、实验、证明或机器人操作 | 1 | LeanMarathon_2026 |
| X4-Y3-Z7 | 层级式多智能体 + 树搜索 / MCTS / trajectory search + 验证 / validation / review | 1 | LeanMarathon_2026 |
| X4-Y3-Z8 | 层级式多智能体 + 树搜索 / MCTS / trajectory search + 迭代 / 长周期发现 | 1 | LeanMarathon_2026 |
| X4-Y4-Z1 | 层级式多智能体 + 演化式优化 + 知识 grounding / 文献综述 | 2 | CoScientist_2026, GeoEvolve_2025 |
| X4-Y4-Z2 | 层级式多智能体 + 演化式优化 + 问题形成 / 假设生成 | 2 | CoScientist_2026, OR_Agent_2026 |
| X4-Y4-Z3 | 层级式多智能体 + 演化式优化 + 实验、仿真、代码或证明设计 | 3 | CoScientist_2026, GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z4 | 层级式多智能体 + 演化式优化 + 执行：代码、工具、实验、证明或机器人操作 | 2 | GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z5 | 层级式多智能体 + 演化式优化 + 结果分析 / 错误诊断 | 2 | GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z7 | 层级式多智能体 + 演化式优化 + 验证 / validation / review | 3 | CoScientist_2026, GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z8 | 层级式多智能体 + 演化式优化 + 迭代 / 长周期发现 | 3 | CoScientist_2026, GeoEvolve_2025, OR_Agent_2026 |
| X4-Y5-Z1 | 层级式多智能体 + harness / capability evolution + 知识 grounding / 文献综述 | 1 | TopoMAS_2025 |
| X4-Y5-Z2 | 层级式多智能体 + harness / capability evolution + 问题形成 / 假设生成 | 4 | Claw_AI_Lab_2026, Mozi_2026, SAGA_2025, TopoMAS_2025 |
| X4-Y5-Z3 | 层级式多智能体 + harness / capability evolution + 实验、仿真、代码或证明设计 | 5 | Claw_AI_Lab_2026, Mimosa_2026, Mozi_2026, SAGA_2025, TopoMAS_2025 |
| X4-Y5-Z4 | 层级式多智能体 + harness / capability evolution + 执行：代码、工具、实验、证明或机器人操作 | 5 | Claw_AI_Lab_2026, Mimosa_2026, Mozi_2026, SAGA_2025, TopoMAS_2025 |
| X4-Y5-Z5 | 层级式多智能体 + harness / capability evolution + 结果分析 / 错误诊断 | 5 | Claw_AI_Lab_2026, Mimosa_2026, Mozi_2026, SAGA_2025, TopoMAS_2025 |
| X4-Y5-Z6 | 层级式多智能体 + harness / capability evolution + 综合 / 报告 / 论文写作 | 1 | Claw_AI_Lab_2026 |
| X4-Y5-Z7 | 层级式多智能体 + harness / capability evolution + 验证 / validation / review | 5 | Claw_AI_Lab_2026, Mimosa_2026, Mozi_2026, SAGA_2025, TopoMAS_2025 |
| X4-Y5-Z8 | 层级式多智能体 + harness / capability evolution + 迭代 / 长周期发现 | 5 | Claw_AI_Lab_2026, Mimosa_2026, Mozi_2026, SAGA_2025, TopoMAS_2025 |
| X5-Y5-Z1 | 开放能力网络 + harness / capability evolution + 知识 grounding / 文献综述 | 5 | AgentRxiv_2025, OmniScientist_2025, Science_Earth_2026, ScienceClaw_Infinite_2026, SCP_2025 |
| X5-Y5-Z2 | 开放能力网络 + harness / capability evolution + 问题形成 / 假设生成 | 4 | AScience_ASCollab_2025, MACC_2026, OmniScientist_2025, Science_Earth_2026 |
| X5-Y5-Z3 | 开放能力网络 + harness / capability evolution + 实验、仿真、代码或证明设计 | 5 | MACC_2026, OmniScientist_2025, Science_Earth_2026, ScienceClaw_Infinite_2026, SCP_2025 |
| X5-Y5-Z4 | 开放能力网络 + harness / capability evolution + 执行：代码、工具、实验、证明或机器人操作 | 5 | AScience_ASCollab_2025, OmniScientist_2025, Science_Earth_2026, ScienceClaw_Infinite_2026, SCP_2025 |
| X5-Y5-Z5 | 开放能力网络 + harness / capability evolution + 结果分析 / 错误诊断 | 5 | AgentRxiv_2025, AScience_ASCollab_2025, Science_Earth_2026, ScienceClaw_Infinite_2026, SCP_2025 |
| X5-Y5-Z6 | 开放能力网络 + harness / capability evolution + 综合 / 报告 / 论文写作 | 5 | AgentRxiv_2025, MACC_2026, OmniScientist_2025, Science_Earth_2026, ScienceClaw_Infinite_2026 |
| X5-Y5-Z7 | 开放能力网络 + harness / capability evolution + 验证 / validation / review | 6 | AScience_ASCollab_2025, MACC_2026, OmniScientist_2025, Science_Earth_2026, ScienceClaw_Infinite_2026, SCP_2025 |
| X5-Y5-Z8 | 开放能力网络 + harness / capability evolution + 迭代 / 长周期发现 | 7 | AgentRxiv_2025, AScience_ASCollab_2025, MACC_2026, OmniScientist_2025, Science_Earth_2026, ScienceClaw_Infinite_2026, SCP_2025 |

## 稀疏坐标（数量 < 4）

| XYZ 组合 | 数量 | 对应文献 |
|---|---:|---|
| X2-Y1-Z6 | 3 | Agent_Laboratory_2024, PaperOrchestra_2026, SparksMatter_2025 |
| X2-Y2-Z6 | 2 | AI_Researcher_HKU_2025, ResearchAgent_2025 |
| X2-Y3-Z1 | 3 | DrugMCTS_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z2 | 3 | DrugMCTS_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z3 | 3 | KompeteAI_2025, PiFlow_2025, PriM_2025 |
| X2-Y3-Z4 | 2 | KompeteAI_2025, PriM_2025 |
| X2-Y3-Z6 | 1 | PriM_2025 |
| X2-Y3-Z8 | 3 | DrugMCTS_2025, PiFlow_2025, PriM_2025 |
| X2-Y4-Z1 | 2 | EvoSci_2026, Virtual_Lab_2025 |
| X2-Y4-Z4 | 3 | Code2Math_2026, RD_Agent_2025, SciDER_2026 |
| X2-Y4-Z5 | 3 | RD_Agent_2025, SciDER_2026, Virtual_Lab_2025 |
| X2-Y5-Z6 | 3 | AutoResearchClaw_2026, CycleResearcher_2024, Kosmos_2025 |
| X3-Y2-Z2 | 1 | AccelMat_2025 |
| X3-Y2-Z3 | 2 | AccelMat_2025, Automatic_Textbook_Formalization_2026 |
| X3-Y2-Z4 | 1 | Automatic_Textbook_Formalization_2026 |
| X3-Y2-Z7 | 3 | AccelMat_2025, Automatic_Textbook_Formalization_2026, LLM_Verifier_2025 |
| X3-Y2-Z8 | 1 | Automatic_Textbook_Formalization_2026 |
| X3-Y3-Z1 | 1 | MOOSE_Chem2_2025 |
| X3-Y3-Z2 | 1 | MOOSE_Chem2_2025 |
| X3-Y3-Z3 | 2 | BFS_Prover_V2_2025, MOOSE_Chem2_2025 |
| X3-Y3-Z4 | 1 | BFS_Prover_V2_2025 |
| X3-Y3-Z7 | 2 | BFS_Prover_V2_2025, MOOSE_Chem2_2025 |
| X3-Y3-Z8 | 1 | BFS_Prover_V2_2025 |
| X3-Y4-Z3 | 1 | AlphaProof_Nexus_2026 |
| X3-Y4-Z4 | 1 | AlphaProof_Nexus_2026 |
| X3-Y4-Z7 | 1 | AlphaProof_Nexus_2026 |
| X3-Y4-Z8 | 1 | AlphaProof_Nexus_2026 |
| X4-Y1-Z1 | 1 | PANGAEA_GPT_2026 |
| X4-Y1-Z3 | 2 | DREAMS_2025, El_Agente_Q_2025 |
| X4-Y1-Z4 | 3 | DREAMS_2025, El_Agente_Q_2025, PANGAEA_GPT_2026 |
| X4-Y1-Z5 | 3 | DREAMS_2025, El_Agente_Q_2025, PANGAEA_GPT_2026 |
| X4-Y1-Z7 | 3 | DREAMS_2025, El_Agente_Q_2025, PANGAEA_GPT_2026 |
| X4-Y1-Z8 | 2 | DREAMS_2025, El_Agente_Q_2025 |
| X4-Y3-Z3 | 1 | LeanMarathon_2026 |
| X4-Y3-Z4 | 1 | LeanMarathon_2026 |
| X4-Y3-Z7 | 1 | LeanMarathon_2026 |
| X4-Y3-Z8 | 1 | LeanMarathon_2026 |
| X4-Y4-Z1 | 2 | CoScientist_2026, GeoEvolve_2025 |
| X4-Y4-Z2 | 2 | CoScientist_2026, OR_Agent_2026 |
| X4-Y4-Z3 | 3 | CoScientist_2026, GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z4 | 2 | GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z5 | 2 | GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z7 | 3 | CoScientist_2026, GeoEvolve_2025, OR_Agent_2026 |
| X4-Y4-Z8 | 3 | CoScientist_2026, GeoEvolve_2025, OR_Agent_2026 |
| X4-Y5-Z1 | 1 | TopoMAS_2025 |
| X4-Y5-Z6 | 1 | Claw_AI_Lab_2026 |

## 对综述结构的启发

1. **第 4 章 Multi-Agent Workflow 应主要引用 X2-X5 文献**：固定角色、并行实例、层级调度和开放能力网络分别对应不同的科研劳动组织方式。
2. **第 5 章 Evolution/Search 应主要引用 Y3-Y5 文献**：区分 artifact-level search/evolution 与 harness/capability evolution，避免把演化机制泛化为所有迭代。
3. **稀疏坐标应作为证据边界处理**：若某一坐标长期少于 4 篇，正文中应写成 emerging island 或 boundary case，而不是强行声称已有成熟范式。

## 逐篇原文定位证据

> 说明：本节替换原先偏概括的逐篇证据表。每篇论文至少记录两类证据：一类定位 `X/Y`（多智能体组织形态与反馈/搜索/演化机制），另一类定位 `Z`（科学发现流程覆盖）。`原文位置`优先写到摘要、章节、图注或方法段；若目前只能定位到摘要级证据，会在位置或末尾风险清单中明确标出。英文只保留短句/短语，正文写作时应回到对应来源核对页码、图号或段落。

| 文献 | 坐标 | 原文位置 | 原文短句/短语 | 支撑的坐标 | 解释 | 来源 |
|---|---|---|---|---|---|---|
| Agent_Laboratory_2024 | X2-Y1-Z1,Z2,Z3,Z4,Z5,Z6,Z7 | arXiv 摘要 | “autonomous LLM-based framework” | X2/Y1 | 论文把系统定义为自主 LLM agent 框架；结合论文中的 PhD/Postdoc/Engineer/Reviewer 等角色，可支撑固定角色多 agent 与反思/反馈式改进。 | https://arxiv.org/abs/2501.04227 |
| Agent_Laboratory_2024 | X2-Y1-Z1,Z2,Z3,Z4,Z5,Z6,Z7 | arXiv 摘要 | “literature review, experimentation, and report writing” | Z1/Z3/Z4/Z5/Z6/Z7 | 三阶段覆盖文献综述、实验执行和论文产出；摘要还说明生成 code repository 和 research report，可支撑系统覆盖科研流程。 | https://arxiv.org/abs/2501.04227 |
| AlphaProof_Nexus_2026 | X3-Y4-Z3,Z4,Z7,Z8 | arXiv 方法/系统段 | “full-featured agent” / “coordinated using an evolutionary algorithm” | X3/Y4 | 论文区分 basic/full-featured agent，并说明 subagents 由演化算法协调，支撑带验证器和演化搜索的数学发现 agent。 | https://arxiv.org/html/2605.22763v1 |
| AlphaProof_Nexus_2026 | X3-Y4-Z3,Z4,Z7,Z8 | arXiv 摘要 | “Lean-based verification” / “resolved 9 of 353 open Erdős problems” | Z3/Z4/Z7/Z8 | Lean 反馈和形式验证提供硬验证；9 个 Erdős 问题结果说明系统覆盖证明搜索、执行、验证和跨尝试迭代。 | https://arxiv.org/abs/2605.22763 |
| CoScientist_2026 | X4-Y4-Z1,Z2,Z3,Z7,Z8 | arXiv 摘要 | “multi-agent system built on Gemini 2.0” | X4/Y4 | 摘要明确多 agent；系统通过生成、辩论、排序、演化和 supervisor/task framework 组织 hypothesis tournament，支撑层级/演化式假设系统。 | https://arxiv.org/abs/2502.18864 |
| CoScientist_2026 | X4-Y4-Z1,Z2,Z3,Z7,Z8 | arXiv 摘要 | “generate, debate, and evolve approach” | Z1/Z2/Z3/Z7/Z8 | 该机制把文献证据、假设生成、研究 proposal、实验验证案例与迭代改写连接起来；生物医学验证支撑 Z7。 | https://arxiv.org/abs/2502.18864 |
| EvoScientist_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “evolving multi-agent AI scientist framework” | X2/Y5 | 摘要直接说明 evolving multi-agent；核心不是单次产物优化，而是通过记忆与自演化改进 research strategies。 | https://arxiv.org/abs/2603.08127 |
| EvoScientist_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “idea generation and experimental execution” / “persistent memory and self-evolution” | Z1/Z2/Z3/Z4/Z5/Z7/Z8 | Researcher/Engineer/Evolution Manager 与两类持久记忆连接想法、实验实现、执行反馈和后续策略更新。 | https://arxiv.org/abs/2603.08127 |
| Kosmos_2025 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | “structured world model” | X2/Y5 | Kosmos 用 world model 在 data-analysis agent 与 literature-search agent 间共享状态，支撑跨轮次的 harness/memory evolution。 | https://arxiv.org/abs/2511.02824 |
| Kosmos_2025 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | “literature search, hypothesis generation, and data analysis” | Z1/Z2/Z4/Z5/Z6/Z7/Z8 | 摘要还说报告中 statement 由代码或 primary literature 支撑，覆盖文献、假设、代码分析、报告、可追溯验证和长程迭代。 | https://arxiv.org/abs/2511.02824 |
| MAESTRO_2026 | X2-Y1-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “multiple LLMs with specialized roles” | X2/Y1 | 多个专门角色 LLM 协作发现 ORR 单原子催化剂；Y1 由反思和设计历史驱动，而非显式进化/竞赛。 | https://arxiv.org/abs/2602.21533 |
| MAESTRO_2026 | X2-Y1-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “autonomous design loop” / “reflect on results” | Z2/Z3/Z4/Z5/Z7/Z8 | autonomous design loop 中 agents 推理、改造候选、反思结果并累积历史，支撑设计、执行/计算评估、结果分析和迭代。 | https://arxiv.org/abs/2602.21533 |
| MARS_Materials_2026 | X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | Matter 摘要/Progress and potential | “hierarchical architecture coordinating 19 LLM agents with 16 domain-specific tools” | X4/Y2 | MARS 是层级多 agent + 多工具系统；通过 Scientist/Engineer/Executor/Analyst 等功能组生成并筛选材料方案。 | https://doi.org/10.1016/j.matt.2025.102577 |
| MARS_Materials_2026 | X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | Matter 摘要/Progress and potential | “closed-loop autonomous materials discovery” / “design to synthesis and optimization” | Z1/Z2/Z3/Z4/Z5/Z7/Z8 | 期刊摘要说明机器人实验闭环，覆盖知识检索、方案设计、协议、物理执行、数据解释、验证与下一轮优化。 | https://www.cell.com/matter/abstract/S2590-2385(25)00620-4 |
| MASTER_2025 | X4-Y2-Z2,Z3,Z4,Z5,Z7,Z8 | npj Computational Materials 摘要 | “hierarchical agentic large language model reasoning” | X4/Y2 | MASTER 用层级 agentic reasoning 指导 functional/heterogeneous catalyst discovery，并比较 single-agent、多 agent 和 stochastic baselines。 | https://www.nature.com/articles/s41524-026-02139-1 |
| MASTER_2025 | X4-Y2-Z2,Z3,Z4,Z5,Z7,Z8 | npj Computational Materials 摘要 | “autonomously design, execute, and interpret atomistic simulations” | Z2/Z3/Z4/Z5/Z7/Z8 | 摘要直接说明设计、执行和解释 atomistic simulations；DFT workflow 和 reasoning traces 支撑计算验证与迭代筛选。 | https://www.nature.com/articles/s41524-026-02139-1 |
| MOFGen_2025 | X2-Y2-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “system of Agentic AI comprising interconnected agents” | X2/Y2 | MOFGen 由 LLM、扩散结构生成、量子力学筛选和合成可行性 agents 组成，支撑异构多 agent 候选生成/过滤。 | https://arxiv.org/abs/2504.14110 |
| MOFGen_2025 | X2-Y2-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “high-throughput experiments” / “successful synthesis of five ‘AI-dreamt’ MOFs” | Z2/Z3/Z4/Z5/Z7/Z8 | 系统生成 MOF 组成/结构和 linker，经计算筛选、合成可行性判断与高通量实验验证，支撑材料发现闭环中的 Z 维覆盖。 | https://arxiv.org/abs/2504.14110 |
| PriM_2025 | X2-Y3-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | “language inferential multi-agent system” / “roundtable system of MAS” | X2/Y3 | PriM 是多 agent roundtable；笔记中 Y3 由 Optimizer/MCTS 搜索支撑，摘要也强调原则引导的系统探索。 | https://arxiv.org/abs/2504.08810 |
| PriM_2025 | X2-Y3-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | “automated hypothesis generation with experimental validation” | Z1/Z2/Z3/Z4/Z5/Z6/Z7/Z8 | 摘要把自动假设生成、实验验证、透明 reasoning pathways 接在一起，可支撑设计、验证、报告解释和反馈式探索。 | https://arxiv.org/abs/2504.08810 |
| Robin_2026 | X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | Nature 摘要 | “first multi-agent system” / “literature search agents with data analysis agents” | X4/Y2 | Robin 以 Crow/Falcon/Finch 等 agent 和 judge/ranking 组织药物候选生成与筛选，支撑工程化层级工作流。 | https://www.nature.com/articles/s41586-026-10652-y |
| Robin_2026 | X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | Nature 摘要 | “hypotheses, experimental directions, data analyses” / “iterative lab-in-the-loop framework” | Z1/Z2/Z3/Z4/Z5/Z7/Z8 | 摘要明确覆盖假设、实验方向、数据分析和迭代 lab-in-the-loop；实验由人类执行，但结果反馈进下一轮候选。 | https://www.nature.com/articles/s41586-026-10652-y |
| Science_Earth_2026 | X5-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | “planet-scale scientific runtime” / “collaboration structure emerging from the question itself” | X5/Y5 | Science Earth 把 agent 扩展为开放能力网络；任务所有权、协作结构和证据裁决随问题涌现，支撑 X5/Y5。 | https://arxiv.org/abs/2606.01316 |
| Science_Earth_2026 | X5-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | “simulation cluster, a wet-lab robot, a proof engine, a single-cell pipeline” | Z1/Z2/Z3/Z4/Z5/Z6/Z7/Z8 | 摘要列出异构科学能力，并报告 Kuramoto 与 single-cell live runs；支撑跨证据标准、执行载体、分析、验证和产出层。 | https://arxiv.org/abs/2606.01316 |
| AScience_ASCollab_2025 | X5-Y5-Z2,Z4,Z5,Z7,Z8 | arXiv 摘要 | “interaction of agents, networks, and evaluation norms” | X5/Y5 | AScience/ASCollab 把发现建模为 agent、网络和评价规范的共同演化，符合开放/演化协作网络坐标。 | https://arxiv.org/abs/2510.08619 |
| AScience_ASCollab_2025 | X5-Y5-Z2,Z4,Z5,Z7,Z8 | arXiv 摘要 | “continually producing and peer-reviewing findings” / “wet-lab validation remains indispensable” | Z2/Z4/Z5/Z7/Z8 | 系统持续生成、互评发现并积累结果；作者同时明确湿实验验证不可替代，因此 Z7 证据是评价边界而非已闭环湿实验。 | https://arxiv.org/abs/2510.08619 |
| SAGA_2025 | X4-Y5-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “outer loop of LLM agents” / “proposes new objectives” | X4/Y5 | SAGA 的外层 goal-evolving LLM agents 分析结果并更新目标，内层做优化，支撑层级结构与 harness/objective evolution。 | https://arxiv.org/abs/2512.21782 |
| SAGA_2025 | X4-Y5-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | “converts them into computable scoring functions” / “inner loop performs solution optimization” | Z2/Z3/Z4/Z5/Z7/Z8 | 自然语言目标被转成可计算评分函数，内层优化候选并反馈给外层，覆盖目标/设计、执行、分析、验证代理和迭代。 | https://arxiv.org/abs/2512.21782 |
| SciDER_2026 | X2-Y4-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "four specialized sub-agents"; "Evolutionary Idea Search" | X2; Y4 | ideation、data analysis、experimentation、critic 四类固定子代理支撑 X2；idea search 明确是演化式假设/产物优化，支撑 Y4。 | https://arxiv.org/abs/2603.01421 |
| SciDER_2026 | X2-Y4-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "data analysis with experimental execution" | Z2,Z3,Z4,Z5,Z7,Z8 | 摘要同时说明假设生成、数据分析、可执行代码、实验执行、critic 反馈与自我迭代，覆盖从问题/假设到执行、分析、验证与迭代。 | https://arxiv.org/abs/2603.01421 |
| CycleResearcher_2024 | X2-Y5-Z1,Z2,Z3,Z6,Z7,Z8 | arXiv 摘要 | "CycleResearcher ... CycleReviewer" | X2; Y5 | Researcher 执行研究任务，Reviewer 模拟同行评审并通过强化学习提供迭代反馈，说明固定角色协作与评审驱动的能力/流程演化。 | https://arxiv.org/abs/2411.00816 |
| CycleResearcher_2024 | X2-Y5-Z1,Z2,Z3,Z6,Z7,Z8 | arXiv 摘要 | "literature review and manuscript preparation to peer review" | Z1,Z2,Z3,Z6,Z7,Z8 | 原文把研究-评审-修订作为全周期，覆盖文献、研究构思/方案、写作、评审验证和下一轮 refinement。 | https://arxiv.org/abs/2411.00816 |
| ProtAgents_2024 | X2-Y2-Z1,Z3,Z4,Z5,Z7 | arXiv 摘要 | "multiple AI agents with distinct capabilities" | X2; Y2 | 多个具备不同能力的 agent 协作处理蛋白质设计任务；围绕 de novo protein design 的候选生成/分析支撑 Y2。 | https://arxiv.org/abs/2402.04268 |
| ProtAgents_2024 | X2-Y2-Z1,Z3,Z4,Z5,Z7 | arXiv 摘要 | "knowledge retrieval, protein structure analysis, physics-based simulations" | Z1,Z3,Z4,Z5,Z7 | 原文列出知识检索、结构分析、物理仿真、结果分析，并用 first-principles data / targeted properties 作为验证性支撑。 | https://arxiv.org/abs/2402.04268 |
| SciAgents_2024 | X2-Y5-Z1,Z2,Z3,Z5,Z7,Z8 | arXiv 摘要 | "multi-agent systems with in-situ learning capabilities" | X2; Y5 | 多 agent 与 in-situ learning 明确支撑固定多智能体协作及能力/系统状态在任务中更新。 | https://arxiv.org/abs/2409.05556 |
| SciAgents_2024 | X2-Y5-Z1,Z2,Z3,Z5,Z7,Z8 | arXiv 摘要 | "generates and refines research hypotheses" | Z1,Z2,Z3,Z5,Z7,Z8 | 知识图谱、检索工具、假设生成/改进、机制解释和 critique 支撑知识 grounding、假设、分析、验证建议与迭代。 | https://arxiv.org/abs/2409.05556 |
| SparksMatter_2025 | X2-Y1-Z1,Z2,Z3,Z5,Z6,Z7,Z8 | arXiv 摘要 | "multi-agent AI model"; "critiques and improves" | X2; Y1 | SparksMatter 是多智能体材料推理模型，且原文说会批评并改进自身响应，支撑固定多 agent 与反思/自修正。 | https://arxiv.org/abs/2508.02956 |
| SparksMatter_2025 | X2-Y1-Z1,Z2,Z3,Z5,Z6,Z7,Z8 | arXiv 摘要 | "generating ideas, designing and executing experimental workflows" | Z1,Z2,Z3,Z5,Z6,Z7,Z8 | 摘要还提到研究缺口、候选材料、follow-up validation、DFT/合成表征建议和 final report，覆盖假设、设计/分析、报告、验证与迭代。 | https://arxiv.org/abs/2508.02956 |
| Virtual_Lab_2025 | X2-Y4-Z1,Z2,Z3,Z5,Z7,Z8 | Nature 摘要/方法 | "LLM Principal Investigator agent"; "four rounds of mutation" | X2; Y4 | PI agent 领导多个 scientist agents，是固定科研团队；nanobody pipeline 通过多轮 mutation、weighted score 和 top-candidate selection 推进候选优化。 | https://www.nature.com/articles/s41586-025-09442-9 |
| Virtual_Lab_2025 | X2-Y4-Z1,Z2,Z3,Z5,Z7,Z8 | Nature 摘要 | "designed 92 new nanobodies"; "Experimental validation" | Z1,Z2,Z3,Z5,Z7,Z8 | Virtual Lab 形成计算 nanobody 设计 pipeline，并经实验验证功能性 binders，支撑设计、分析、验证和真实发现迭代。 | https://www.nature.com/articles/s41586-025-09442-9 |
| AtomAgents_2025 | X2-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "multiple AI agents that collaborate autonomously" | X2; Y2 | 多个不同专长 agent 自主协作解决材料设计任务；以 alloy candidate design / property comparison 为核心，支撑候选生成与筛选。 | https://arxiv.org/abs/2407.10022 |
| AtomAgents_2025 | X2-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "knowledge retrieval, multi-modal data integration, physics-based simulations" | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | 原文覆盖知识检索、多模态数据、物理仿真和结果分析，并展示合金设计与性质预测，支撑执行、分析、验证和材料发现迭代。 | https://arxiv.org/abs/2407.10022 |
| DREAMS_2025 | X4-Y1-Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "hierarchical, multi-agent framework"; "error handling" | X4; Y1 | central planner 调度 domain-specific agents，构成层级式多智能体；convergence/error handling 支撑故障检测与反思式修正。 | https://arxiv.org/abs/2507.14267 |
| DREAMS_2025 | X4-Y1-Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "atomistic structure generation, systematic DFT convergence testing" | Z3,Z4,Z5,Z7,Z8 | 原文还列出 HPC scheduling、benchmark validation、CO/Pt puzzle 与长期复杂问题求解，覆盖仿真设计、执行、分析、验证与迭代。 | https://arxiv.org/abs/2507.14267 |
| Materealize_2026 | X2-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "multi-agent debate" | X2; Y2 | thinking mode 使用多智能体 debate 产出更精细的合成推荐，结合候选设计、诊断、redesign 和合成路线推荐支撑候选筛选。 | https://arxiv.org/abs/2601.15743 |
| Materealize_2026 | X2-Y2-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "structure generation, property prediction, synthesizability prediction, and synthesis planning" | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | 原文覆盖结构生成、性质/可合成性预测、合成规划、机制假设、文献比较和 physics-grounded simulations，支撑全材料发现链条。 | https://arxiv.org/abs/2601.15743 |
| ScienceClaw_Infinite_2026 | X5-Y5-Z1,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | "independent agents conduct research without central coordination" | X5; Y5 | 任意 contributor 可部署 agents 到共享生态，独立 agents 通过全局索引、artifact exchange 和 persistent memory 协调，符合开放能力网络与 harness evolution。 | https://arxiv.org/abs/2603.14312 |
| ScienceClaw_Infinite_2026 | X5-Y5-Z1,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | "over 300 interoperable scientific skills"; "artifact DAG" | Z1,Z3,Z4,Z5,Z6,Z7,Z8 | skill registry、工具链、artifact DAG、structured posts、provenance views 和 published finding 覆盖检索/设计、执行、分析、报告、验证与多轮迭代。 | https://arxiv.org/abs/2603.14312 |
| TopoMAS_2025 | X4-Y5-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "orchestrates the entire materials-discovery pipeline"; "self-evolving knowledge graph" | X4; Y5 | TopoMAS 将用户查询、检索、推理、结构生成和验证编排成 pipeline，并把计算结果写回动态知识图谱，支撑层级编排与知识/harness 演化。 | https://arxiv.org/abs/2507.04053 |
| TopoMAS_2025 | X4-Y5-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "multi-source data retrieval"; "first-principles validation" | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | 原文还提到 theoretical inference、crystal-structure generation、computational outcomes 和 continuous knowledge refinement，覆盖材料发现全链条。 | https://arxiv.org/abs/2507.04053 |
| AI_Researcher_HKU_2025 | X2-Y2-Z1,Z2,Z3,Z6,Z7 | arXiv HTML 方法/框架 | "comprehensive multi-agent architecture"; "convergent evaluation" | X2; Y2 | 原文说明 specialized components 协作；idea generation 采用 divergent-convergent discovery，先生成多个方向再按 novelty、soundness、potential 评价筛选。 | https://arxiv.org/html/2505.18705v1 |
| AI_Researcher_HKU_2025 | X2-Y2-Z1,Z2,Z3,Z6,Z7 | arXiv 摘要 | "literature review and hypothesis generation to algorithm implementation" | Z1,Z2,Z3,Z6,Z7 | 摘要还写到 publication-ready manuscript preparation，并用 code review / paper review agents 做验证，支撑文献、假设、实现、写作与评审。 | https://arxiv.org/abs/2505.18705 |
| BioAgents_2025 | X2-Y1-Z1,Z5,Z7 | Scientific Reports 摘要/方法 | "multi-agent system built on small language models" | X2; Y1 | 系统由两个 specialized agents 与 reasoning agent 组成；self-evaluation 低分重处理支撑反思/自修正，但论文也指出重复 refinement 可能收益递减。 | https://www.nature.com/articles/s41598-025-25919-z |
| BioAgents_2025 | X2-Y1-Z1,Z5,Z7 | Scientific Reports 结果/讨论 | "performance comparable to human experts" | Z1,Z5,Z7 | BioAgents 面向 bioinformatics workflows，进行概念基因组学分析、信息缺口识别和专家评分比较，支撑知识/分析与专家式验证。 | https://www.nature.com/articles/s41598-025-25919-z |
| CRISPR_GPT_2026 | X2-Y1-Z3,Z4,Z5,Z7 | Nature Biomedical Engineering 摘要/图 1 附近 | "planning and execution agents"; "task decomposition" | X2; Y1 | Planner、Executor、Tool provider、User proxy 等固定组件协作；系统分解任务、询问澄清并支持 troubleshooting，支撑 X2 与反思/修正式流程。 | https://www.nature.com/articles/s41551-025-01463-z |
| CRISPR_GPT_2026 | X2-Y1-Z3,Z4,Z5,Z7 | Nature Biomedical Engineering 摘要/正文 | "designing guide RNAs"; "analysing data" | Z3,Z4,Z5,Z7 | 原文还列出协议、delivery、validation assays、wet-lab knockout/activation 展示和专家评测，覆盖实验设计、执行、数据分析和验证。 | https://www.nature.com/articles/s41551-025-01463-z |
| Deep_Research_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "specialized agents for planning, data analysis, literature search, and novelty detection" | X2; Y5 | 多个固定专长 agents 通过 persistent world state 统一；world state 跨研究循环保存上下文，支撑能力/状态演化。 | https://arxiv.org/abs/2601.12542 |
| Deep_Research_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "persistent world state"; "iterative research cycles" | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | planning、data analysis、literature search、novelty detection 和 extended investigations 支撑文献、假设/计划、分析/执行、验证与长周期迭代。 | https://arxiv.org/abs/2601.12542 |
| EvoSci_2026 | X2-Y4-Z1,Z2,Z7,Z8 | Sec. 3.2 Task Decomposition and Team Collaboration | `collaborative research process` | X2-Y4 | 原文说明 Prime Researcher 将探索分解为背景调查、问题分析、idea generation 与迭代 refinement 等任务，并用 CrewAI 组织团队，支撑“多智能体协作的研究想法/发现流程”。 | [arXiv HTML](https://arxiv.org/html/2605.24018v1) |
| EvoSci_2026 | X2-Y4-Z1,Z2,Z7,Z8 | Sec. 3.3-4.1 Research Idea Evaluation | `reviewer agent` | Z1,Z2,Z7,Z8 | 系统含研究任务分解、种子想法生成、进化迭代、评审/元评审和 tournament 排名；这些模块覆盖生成、迭代优化、评价与系统化记录。 | [arXiv HTML](https://arxiv.org/html/2605.24018v1) |
| Instrument_Agents_2026 | X2-Y5-Z1,Z3,Z4,Z5,Z7,Z8 | Nature abstract / opening summary | `operates complex scientific instrumentation` | X2-Y5 | 论文直接说开发并 benchmark 一个 multi-agent framework 操作两类真实科学设施，支撑“多智能体 + 物理科学仪器/实验设施”坐标。 | [Nature](https://www.nature.com/articles/s41524-026-02005-0) |
| Instrument_Agents_2026 | X2-Y5-Z1,Z3,Z4,Z5,Z7,Z8 | Nature lines 91-93, 172 | `learn on the job` | Z1,Z3,Z4,Z5,Z7,Z8 | 系统能编排多步实验、解释多模态数据、协作人类研究者，并通过专家指导/交互记忆学习；覆盖工具/仪器执行、数据解释、人机协作、评价可靠性。 | [Nature](https://www.nature.com/articles/s41524-026-02005-0) |
| MAGenIdeas_2026 | X2-Y2-Z1,Z2,Z7,Z8 | arXiv abstract | `generate, evaluate, and refine research ideas` | X2-Y3 | 摘要称其将组合创新理论、迭代知识搜索与 LLM 多智能体系统结合，用于研究想法生成，支撑“多智能体研究 ideation 方法”。 | [arXiv abstract](https://arxiv.org/abs/2604.20548) |
| MAGenIdeas_2026 | X2-Y2-Z1,Z2,Z7,Z8 | arXiv abstract | `iterative knowledge search` | Z1,Z2,Z7,Z8 | 系统通过 repeated interaction 生成、评价、精炼 idea，并在 NLP 域实验中比较 diversity/novelty；另有代码、数据和 demo，支撑生成、迭代、评价与可复核系统输出。 | [arXiv abstract](https://arxiv.org/abs/2604.20548) |
| Mimosa_2026 | X4-Y5-Z3,Z4,Z5,Z7,Z8 | Abstract | `task-specific multi-agent workflows` | X4-Y5 | Mimosa 自动合成任务特定工作流，并用 MCP 动态发现工具，执行计算型科学任务；这支撑“可演化工作流/工具型科研自动化”。 | [arXiv HTML](https://arxiv.org/html/2603.28986v1) |
| Mimosa_2026 | X4-Y5-Z3,Z4,Z5,Z7,Z8 | Abstract; Sec. 3 framework layers | `fully logged execution traces` | Z3,Z4,Z5,Z7,Z8 | 原文列出工具发现、meta-orchestrator、代码生成 agent、LLM judge、执行日志和归档 workflow，覆盖工具调用、执行、评价反馈、审计复现。 | [arXiv HTML](https://arxiv.org/html/2603.28986v1) |
| OR_Agent_2026 | X4-Y4-Z2,Z3,Z4,Z5,Z7,Z8 | Abstract | `structured tree-based workflow` | X4-Y4 | OR-Agent 面向复杂实验环境中的自动探索，把研究组织为树状 hypothesis/workflow，支撑“结构化搜索与算法发现/OR 问题求解”。 | [arXiv HTML](https://arxiv.org/html/2602.13769) |
| OR_Agent_2026 | X4-Y4-Z2,Z3,Z4,Z5,Z7,Z8 | Sec. 2.1 Framework Overview | `Idea Agent` / `Code Agent` / `Experiment Agent` | Z2,Z3,Z4,Z5,Z7,Z8 | 系统含共享 solution database、Lead/Idea/Code/Experiment agents、执行调试、实验摘要、反思与回退机制，覆盖想法、代码、实验、反馈、可检查记录。 | [arXiv HTML](https://arxiv.org/html/2602.13769) |
| OmniScientist_2025 | X5-Y5-Z1,Z2,Z3,Z4,Z6,Z7,Z8 | Abstract | `end-to-end automation` | X5-Y5 | 摘要明确覆盖 data foundation、literature review、research ideation、experiment automation、scientific writing、peer review，支撑最宽的端到端科研生态坐标。 | [arXiv HTML](https://arxiv.org/html/2511.16931v1) |
| OmniScientist_2025 | X5-Y5-Z1,Z2,Z3,Z4,Z6,Z7,Z8 | Abstract; Sec. 5 Evaluation through ScienceArena | `ScienceArena` | Z1,Z2,Z3,Z4,Z6,Z7,Z8 | 系统还包含结构化知识系统、协作协议 OSP、人类参与、开放评价平台与 Elo 排名，因此覆盖知识、协作、实验、写作、评审和评价基础设施。 | [arXiv HTML](https://arxiv.org/html/2511.16931v1) |
| PANGAEA_GPT_2026 | X4-Y1-Z1,Z4,Z5,Z7 | Abstract | `autonomous data discovery and analysis` | X4-Y1 | 论文提出地球科学数据档案中的层级 multi-agent 系统，核心对象是 PANGAEA 等异质数据仓库的数据发现与分析。 | [arXiv HTML](https://arxiv.org/html/2602.21351v1) |
| PANGAEA_GPT_2026 | X4-Y1-Z1,Z4,Z5,Z7 | Abstract; Methods 5.2 | `Supervisor-Worker topology` | Z1,Z4,Z5,Z7 | 架构含 Supervisor-Worker 路由、沙盒确定性代码执行、执行反馈自纠错和多步 workflow，覆盖检索、分析执行、反馈修正与评价。 | [arXiv HTML](https://arxiv.org/html/2602.21351v1) |
| Code2Math_2026 | X2-Y4-Z2,Z3,Z4,Z7,Z8 | Abstract | `autonomously evolve existing math problems` | X2-Y4 | 论文研究 code agents 将已有数学题演化为更复杂变体，支撑“代码智能体 + 数学问题演化/生成”方法坐标。 | [arXiv HTML](https://arxiv.org/html/2603.03202v3) |
| Code2Math_2026 | X2-Y4-Z2,Z3,Z4,Z7,Z8 | Appendix A.1 Experimental Setup Details | `controlled environment` | Z2,Z3,Z4,Z7,Z8 | 多智能体系统包含 evolution 与 verification 阶段，受控 Python 执行环境、工具集、外部 judge 和 solvability/difficulty 检查，支撑生成、执行、验证与复核。 | [arXiv HTML](https://arxiv.org/html/2603.03202v3) |
| PaperOrchestra_2026 | X2-Y1-Z1,Z6,Z7 | arXiv abstract | `automated AI research paper writing` | X2-Y1 | 论文把未结构化研究材料转成论文手稿，方法对象是科研写作而非实验发现，支撑写作/论文生成坐标。 | [arXiv abstract](https://arxiv.org/abs/2604.05018) |
| PaperOrchestra_2026 | X2-Y1-Z1,Z6,Z7 | arXiv abstract | `submission-ready LaTeX manuscripts` | Z1,Z6,Z7 | 摘要说明系统生成完整 LaTeX、文献综合和图表/概念图，并用 PaperWritingBench 与人类 side-by-side 评价，覆盖写作产物与评价。 | [arXiv abstract](https://arxiv.org/abs/2604.05018) |
| MACC_2026 | X5-Y5-Z2,Z3,Z6,Z7,Z8 | Abstract | `blackboard-style shared scientific workspace` | X5-Y5 | MACC 是制度架构而非单一 agent pipeline，用共享科学工作区与激励机制组织多主体科学探索，支撑生态/制度层坐标。 | [arXiv HTML](https://arxiv.org/html/2603.03780v1) |
| MACC_2026 | X5-Y5-Z2,Z3,Z6,Z7,Z8 | Sec. 3.3-3.5 | `open participation platform` | Z2,Z3,Z6,Z7,Z8 | 黑板记录模型、超参、中间结果、复现实验与奖励；开放平台允许异构独立 agent 参与，覆盖协作竞争、复现、评价、制度机制与规模化。 | [arXiv HTML](https://arxiv.org/html/2603.03780v1) |
| PiFlow_2025 | X2-Y3-Z1,Z2,Z3,Z5,Z7,Z8 | Abstract | `structured uncertainty reduction` | X2-Y3 | PiFlow 将自动科学发现表述为由科学原则引导的信息论不确定性缩减，支撑“原则约束的多智能体发现方法”。 | [arXiv HTML](https://arxiv.org/html/2505.15047v4) |
| PiFlow_2025 | X2-Y3-Z1,Z2,Z3,Z5,Z7,Z8 | Abstract; Introduction | `three distinct scientific domains` | Z1,Z2,Z3,Z5,Z7,Z8 | 评估覆盖纳米材料、生物分子、超导候选等三域；摘要还说 plug-and-play、泛化到既有 agent 架构，支撑跨域、协作、实验评价与系统集成。 | [arXiv HTML](https://arxiv.org/html/2505.15047v4) |
| ResearchAgent_2025 | X2-Y2-Z1,Z2,Z6,Z7 | ACL Anthology PDF, Abstract | `automatically defines novel problems` | X2-Y2 | ResearchAgent 从核心论文出发，自动定义问题、提出方法、设计实验，支撑“文献驱动的研究 idea operationalization”坐标。 | [ACL Anthology PDF](https://aclanthology.org/2025.naacl-long.342.pdf) |
| ResearchAgent_2025 | X2-Y2-Z1,Z2,Z6,Z7 | ACL Anthology PDF, Abstract / Fig. 1 | `ReviewingAgents` | Z1,Z2,Z6,Z7 | 系统连接 academic graph 与 entity-centric knowledge store，并用多个 reviewing agents 迭代审稿反馈；覆盖检索知识、idea 迭代、审稿评价与实验设计。 | [ACL Anthology PDF](https://aclanthology.org/2025.naacl-long.342.pdf) |
| AgentReview_2024 | X2-Y1-Z7 | Abstract | `peer review simulation framework` | X2-Y1 | AgentReview 用 LLM agent 模拟同行评审，研究对象明确是 peer review 过程与机制，而不是实验或发现执行。 | [arXiv HTML](https://arxiv.org/html/2406.12708v2) |
| AgentReview_2024 | X2-Y1-Z7 | Sec. 2.2 Review Process Design | `structured, 5-phase pipeline` | Z7 | 系统的 5 阶段 pipeline 包含 reviewer assessment、rebuttal、讨论、meta-review 与 final decision，用于评价/机制分析，故支撑 Z7。 | [arXiv HTML](https://arxiv.org/html/2406.12708v2) |
| LLM_Verifier_2025 | X3-Y2-Z7 | OpenReview Abstract | `scaling the number of verifier models` | X3-Y2 | 该文实际对应 Multi-Agent Verification / MAV：用多个 verifier models 作为 test-time scaling 维度，对候选输出进行多验证器评估与选择，支撑同类多实例验证与候选筛选。 | [OpenReview](https://openreview.net/forum?id=LriQ3NY9uL) |
| LLM_Verifier_2025 | X3-Y2-Z7 | OpenReview Abstract | `combines multiple verifiers to improve performance` | Z7 | MAV 的核心任务是 verification；它不是科学发现生成系统，而是可作为 ASD 中 hypothesis、proof、code 或 report 的多验证器 evidence-closure substrate。 | [OpenReview](https://openreview.net/forum?id=LriQ3NY9uL) |
| MOOSE_Chem_2024 | X2-Y2-Z1,Z2,Z7 | arXiv 摘要 | "multi-agent framework"; "three stages" | X2, Y2 | 原文明确是 LLM 多智能体框架，并把假设发现拆为检索 inspiration、生成 hypothesis、排序 hypothesis 的多阶段候选生成/筛选流程。 | https://arxiv.org/abs/2410.07076 |
| MOOSE_Chem_2024 | X2-Y2-Z1,Z2,Z7 | arXiv 摘要 | "background, inspirations, and hypothesis" | Z1, Z2, Z7 | benchmark 将论文拆成背景、灵感和假设，并用 rediscovery/ranking 评估系统是否找回真实创新点，覆盖知识 grounding、假设生成和评价。 | https://arxiv.org/abs/2410.07076 |
| MOOSE_Chem2_2025 | X3-Y3-Z1,Z2,Z3,Z7 | arXiv 摘要 | "combinatorial optimization problem"; "ensemble" | X3, Y3 | 原文把细粒度假设发现形式化为假设空间上的组合优化，并比较 diverse LLM ensemble 与重复实例，支撑多实例/集成与搜索式机制。 | https://arxiv.org/abs/2505.19209 |
| MOOSE_Chem2_2025 | X3-Y3-Z1,Z2,Z3,Z7 | arXiv 摘要 | "hierarchical search method"; "experimental configurations" | Z1, Z2, Z3, Z7 | 方法从 coarse research directions 逐步补全到实验配置，并在专家标注 benchmark 上评估，覆盖背景、假设、实验细节设计与评价。 | https://arxiv.org/abs/2505.19209 |
| Curie_2025 | X2-Y1-Z2,Z3,Z4,Z5,Z7 | arXiv 摘要 | "intra-agent rigor"; "inter-agent rigor" | X2, Y1 | Curie 用 intra/inter-agent rigor 将可靠性、方法控制和可解释性嵌入实验流程，体现多 agent 检查与修正。 | https://arxiv.org/abs/2502.16069 |
| Curie_2025 | X2-Y1-Z2,Z3,Z4,Z5,Z7 | arXiv 摘要 | "46 questions"; "experimental questions" | Z2, Z3, Z4, Z5, Z7 | 论文构建跨四个计算机科学领域的实验 benchmark，并评估实验问题回答，支撑问题形成、实验设计/执行、结果解释和验证。 | https://arxiv.org/abs/2502.16069 |
| GenoMAS_2025 | X2-Y1-Z1,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "six specialized LLM agents"; "typed message-passing" | X2, Y1 | GenoMAS 明确由六个专门化 LLM agents 通过 typed message passing 与 shared canvas 协作，且包含 revise/backtrack 控制。 | https://arxiv.org/abs/2507.21035 |
| GenoMAS_2025 | X2-Y1-Z1,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "advance, revise, bypass, or backtrack" | Z1, Z3, Z4, Z5, Z7, Z8 | 系统将 gene-expression 任务拆成 Action Units，生成、执行、修订和验证代码，并报告文献支持的 gene-phenotype associations。 | https://arxiv.org/abs/2507.21035 |
| TAIS_2024 | X2-Y1-Z1,Z3,Z4,Z5,Z7 | arXiv 摘要 | "project manager"; "data engineer"; "domain expert" | X2, Y1 | TAIS 以项目经理、数据工程师、领域专家等 LLM 角色协作复现数据科学团队流程，支撑固定角色多智能体和协作修正。 | https://arxiv.org/abs/2402.12391 |
| TAIS_2024 | X2-Y1-Z1,Z3,Z4,Z5,Z7 | arXiv 摘要 | "identifying disease-predictive genes" | Z1, Z3, Z4, Z5, Z7 | 任务聚焦基因表达数据中的疾病预测基因识别，并构建 benchmark 评估效果，覆盖知识、分析设计、执行、结果和验证。 | https://arxiv.org/abs/2402.12391 |
| MLZero_2025 | X2-Y5-Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "multi-agent framework"; "semantic and episodic memory" | X2, Y5 | MLZero 是 LLM 多智能体 AutoML 框架，并用语义/情节记忆增强迭代代码生成，支撑 harness/capability evolution。 | https://arxiv.org/abs/2505.13941 |
| MLZero_2025 | X2-Y5-Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "end-to-end ML automation" | Z3, Z4, Z5, Z7, Z8 | 系统从多模态输入到 ML solution 自动化，包含代码生成、执行、评估和迭代改进，适合作为计算型科研 harness 证据。 | https://arxiv.org/abs/2505.13941 |
| MLR_Copilot_2024 | X2-Y1-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "IdeaAgent"; "ExperimentAgent" | X2, Y1 | 原文给出 IdeaAgent 与 ExperimentAgent 分工，且执行阶段含 human feedback 与 iterative debugging，支撑多 agent 反思修正。 | https://arxiv.org/abs/2408.14033 |
| MLR_Copilot_2024 | X2-Y1-Z1,Z2,Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "research idea generation"; "implementation execution" | Z1, Z2, Z3, Z4, Z5, Z7, Z8 | 框架三阶段覆盖从论文到假设/实验计划、可执行实现、运行调试和任务评估，是 ML research idea-to-execution pipeline。 | https://arxiv.org/abs/2408.14033 |
| KompeteAI_2025 | X2-Y3-Z3,Z4,Z5,Z7 | arXiv 摘要 | "dynamic solution space exploration"; "MCTS" | X2, Y3 | KompeteAI 是 autonomous multi-agent AutoML framework，核心针对 MCTS 局限加入动态搜索与候选合并，支撑树/轨迹搜索。 | https://arxiv.org/abs/2508.10177 |
| KompeteAI_2025 | X2-Y3-Z3,Z4,Z5,Z7 | arXiv 摘要 | "accelerated debugging"; "pipeline evaluation" | Z3, Z4, Z5, Z7 | 系统面向端到端 pipeline 生成，通过预测评分和加速调试减少完整执行成本，并在 MLE-Bench/Kompete-bench 上验证。 | https://arxiv.org/abs/2508.10177 |
| IMPROVE_2025 | X2-Y1-Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "Iterative Refinement"; "one component at a time" | X2, Y1 | IMPROVE 用 LLM agents 进行逐组件迭代改进，而不是一次性改全 pipeline，直接支撑反馈驱动修正。 | https://arxiv.org/abs/2502.18530 |
| IMPROVE_2025 | X2-Y1-Z3,Z4,Z5,Z7,Z8 | arXiv 摘要 | "real training feedback"; "object classification pipelines" | Z3, Z4, Z5, Z7, Z8 | 系统根据训练反馈更新组件，自动化和优化视觉分类 pipeline，并跨数据集评估性能，覆盖设计、执行、分析、验证和迭代。 | https://arxiv.org/abs/2502.18530 |
| Generative_Adversarial_Reviews_2024 | X2-Y1-Z7 | arXiv 摘要 | "Generative Agent Reviewers"; "reviewer personas" | X2, Y1 | GAR 用 LLM-empowered agents 和 reviewer personas 模拟 peer reviewers，属于多角色 critic/review 系统。 | https://arxiv.org/abs/2412.10415 |
| Generative_Adversarial_Reviews_2024 | X2-Y1-Z7 | arXiv 摘要 | "multi-round assessment"; "meta-reviewer" | Z7 | review 过程用外部知识、manuscript graph、多轮评估和 meta-reviewer 汇总，主要支撑 validation/review 坐标。 | https://arxiv.org/abs/2412.10415 |
| AstroAgents_2025 | X2-Y2-Z1,Z2,Z5,Z7 | arXiv 摘要 | "eight collaborative agents" | X2, Y2 | AstroAgents 由 data analyst、planner、domain scientists、accumulator、literature reviewer、critic 等八个协作 agent 组成，用于候选假设生成和筛选。 | https://arxiv.org/abs/2503.23170 |
| AstroAgents_2025 | X2-Y2-Z1,Z2,Z5,Z7 | arXiv 摘要 | "novelty and plausibility" | Z1, Z2, Z5, Z7 | 系统结合质谱数据和用户论文生成生命起源假设，并由专家评估 novelty/plausibility，覆盖文献、假设、数据解释和评价。 | https://arxiv.org/abs/2503.23170 |
| VirSci_2024 | X2-Y1-Z1,Z2,Z7,Z8 | arXiv 摘要；ACL Anthology 页面 | "Virtual Scientists"; "team of agents" | X2, Y1 | VirSci 明确模拟科学团队协作，用多个 virtual scientists 生成、评价和 refine research ideas。 | https://arxiv.org/abs/2410.09403 ; https://aclanthology.org/2025.acl-long.1368/ |
| VirSci_2024 | X2-Y1-Z1,Z2,Z7,Z8 | arXiv 摘要；ACL Anthology 页面 | "generate, evaluate, and refine" | Z1, Z2, Z7, Z8 | 工作覆盖科学想法生成、评价与迭代 refinement；不含真实实验执行，因此 Z 主要停留在知识/idea/review/iteration。 | https://arxiv.org/abs/2410.09403 ; https://aclanthology.org/2025.acl-long.1368/ |
| AGAPI_Agents_2025 | X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7 | arXiv 摘要 | "Agent-Planner-Executor-Summarizer architecture" | X4, Y2 | AGAPI 采用层级式 Agent-Planner-Executor-Summarizer 架构，自动构建和执行多步材料 API workflow，支撑层级编排与候选/工具链筛选。 | https://arxiv.org/abs/2512.11935 |
| AGAPI_Agents_2025 | X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7 | arXiv 摘要 | "twenty materials-science API endpoints" | Z1, Z2, Z3, Z4, Z5, Z7, Z8 | 平台统一数据库、仿真、ML 模型，覆盖检索、预测、优化、衍射分析、逆向设计，并与实验数据比较，支撑广泛系统覆盖。 | https://arxiv.org/abs/2512.11935 |
| AgentRxiv_2025 | X5-Y5-Z1,Z5,Z6,Z8 | arXiv 摘要 | "shared preprint server"; "agent laboratories" | X5, Y5 | AgentRxiv 让多个 LLM agent laboratories 通过共享 preprint server 上传/检索报告，构成开放科研产物网络和跨实验室记忆。 | https://arxiv.org/abs/2503.18102 |
| AgentRxiv_2025 | X5-Y5-Z1,Z5,Z6,Z8 | arXiv 摘要 | "iteratively build on each other's research" | Z1, Z5, Z6, Z8 | 系统以 prior reports 为知识来源，吸收已有结果、发布报告并迭代改进策略；原文不主张 peer-review 式验证，因此不支撑 Z7。 | https://arxiv.org/abs/2503.18102 |
| AutoResearchClaw_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | "structured multi-agent debate"; "cross-run evolution" | X2, Y5 | AutoResearchClaw 由多 agent debate、自愈 executor 和跨运行演化组成，核心是 research harness 的能力积累。 | https://arxiv.org/abs/2605.20025 |
| AutoResearchClaw_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | "self-healing executor"; "verifiable result reporting" | Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8 | 摘要覆盖假设生成、实验失败修复、结果分析、可验证报告、人机协作和跨运行经验沉淀，是本批 Z 覆盖最完整的系统之一。 | https://arxiv.org/abs/2605.20025 |
| Claw_AI_Lab_2026 | X4-Y5-Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv HTML, Abstract/Fig. 1 caption | "five connected layers" | X4 | 论文把自动科研组织为 idea、planning、coding、experimentation、writing 五层，并说明每层有 specialized agents 与 validation loops，支撑层级式多智能体组织。 | https://arxiv.org/abs/2605.22662 |
| Claw_AI_Lab_2026 | X4-Y5-Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv HTML, Introduction; project page pipeline | "Claw-Code Harness"; "runnable code" | Y5; Z2/Z3/Z4/Z5/Z6/Z7/Z8 | Claw-Code Harness 连接本地代码、数据、checkpoint，产出代码、图、日志和论文；官网五层流程覆盖文献/假设、实验设计、代码、GPU 执行、日志分析、写作和 peer review，且 L4 结果反馈到 L1，支撑 harness evolution 和长流程覆盖。 | https://arxiv.org/abs/2605.22662 ; https://clawailab.ai/ |
| eNRRCrew_2025 | X4-Y2-Z1,Z2,Z5,Z7,Z8 | National Science Review, Abstract | "five LLM agents" | X4; Y2 | 原文称 eNRRCrew 是 multi-agent framework，并用五个 LLM agents 支持自然语言交互、推荐、预测、数据分析和文献洞察；结合论文正文的任务分派/工具执行描述，可支撑 orchestrator 式候选推荐与性能比较。 | https://doi.org/10.1093/nsr/nwaf372 |
| eNRRCrew_2025 | X4-Y2-Z1,Z2,Z5,Z7,Z8 | National Science Review, Abstract/Fig. 6 caption | "2321 papers"; "novel catalyst recommendation" | Z1/Z2/Z5/Z7/Z8 | 系统从 2321 篇文献构建数据库，进行 yield/FE 预测、可解释性和聚类分析，并给出 13 个催化剂推荐；正文还提到 MoFeNC 推荐已被实验验证，且平台可扩展到其他电催化域。 | https://doi.org/10.1093/nsr/nwaf372 |
| MADD_2025 | X4-Y2-Z3,Z4,Z5,Z7 | ACL Anthology, Abstract | "four coordinated agents" | X4; Y2 | MADD 明确使用四个协调 agents，从自然语言查询构建并执行 hit-identification pipeline，适合支撑层级/编排式药物发现候选生成与筛选。 | https://aclanthology.org/2025.findings-emnlp.367/ |
| MADD_2025 | X4-Y2-Z3,Z4,Z5,Z7 | ACL Anthology, Abstract | "de novo compound generation and screening" | Z3/Z4/Z5/Z7 | 其任务覆盖分子生成、筛选、预测/评价，并在七个 drug discovery cases、五个 biological targets 和 docking-score benchmark 上评估；因此支撑 in silico 设计、工具执行、结果分析和基准验证。 | https://aclanthology.org/2025.findings-emnlp.367/ |
| Mozi_2026 | X4-Y5-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Sec. 4.2 | "Supervisor-Worker Hierarchical Agent System" | X4; Y5 | Mozi 的 Layer A 明确是 Supervisor-Worker 层级 agent system，Supervisor 做规划、约束监控、动态重规划，并委派给 Research/Computation 等 specialized workers。 | https://arxiv.org/abs/2603.03655 |
| Mozi_2026 | X4-Y5-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Sec. 4.3-4.4 | "Composable Stateful Skill Graphs"; "HITL validation gates" | Y5; Z2/Z3/Z4/Z5/Z7/Z8 | Layer B 将长周期药物发现 workflow 编码为有状态 skill graphs，覆盖 target identification、hit identification、hit-to-lead、lead optimization，并用 HITL gates、provenance、rollback/参数修正支撑验证和长流程治理。 | https://arxiv.org/abs/2603.03655 |
| SCP_2025 | X5-Y5-Z1,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Abstract | "global web of autonomous scientific agents" | X5; Y5 | SCP 是开放协议/平台，目标是把 tools、models、datasets、physical instruments 和 agents 连成跨平台、跨机构的 scientific capability network，而非单个固定团队。 | https://arxiv.org/abs/2512.24189 |
| SCP_2025 | X5-Y5-Z1,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Abstract/Sec. 2.1 | "complete experiment lifecycle"; "1,600+ tool resources" | Z1/Z3/Z4/Z5/Z7/Z8 | 论文称 SCP 管理 registration、planning、execution、monitoring、archival，并提供 1,600+ tool resources；hub 负责 registry、service discovery、task dispatch、provenance 与 reproducibility。 | https://arxiv.org/abs/2512.24189 |
| DrugMCTS_2025 | X2-Y3-Z1,Z2,Z5,Z7,Z8 | arXiv HTML, Abstract/Introduction | "five specialized agents"; "Monte Carlo Tree Search" | X2; Y3 | DrugMCTS 将 RAG、多 agent 协作和 MCTS 结合；五个 specialized agents 分别处理药物/蛋白信息，核心机制是候选推理路径的树搜索。 | https://arxiv.org/abs/2507.07426 |
| DrugMCTS_2025 | X2-Y3-Z1,Z2,Z5,Z7,Z8 | arXiv HTML, Abstract/Experiments | "DrugBank and KIBA datasets" | Z1/Z2/Z5/Z7/Z8 | 系统检索并分析 molecular/protein information，用结构化迭代推理做 drug repurposing 候选决策，并在 DrugBank/KIBA 上以 recall 和 robustness 验证搜索结果。 | https://arxiv.org/abs/2507.07426 |
| RD_Agent_2025 | X2-Y4-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Abstract/Sec. 1 | "dual-agent framework"; "multiple parallel exploration traces" | X2; Y4 | R&D-Agent 明确由 Researcher 和 Developer 双 agent 组成，并支持多条 exploration traces 并行、融合和相互增强，支撑 artifact-level evolution。 | https://arxiv.org/abs/2505.14738 |
| RD_Agent_2025 | X2-Y4-Z2,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Sec. 2-3 | "runnable solution"; "performance feedback" | Z2/Z3/Z4/Z5/Z7/Z8 | Researcher 生成 idea，Developer 实现、调试并运行 solution；系统使用性能/错误反馈、trace fusion 和 MLE-Bench 评估闭环，覆盖想法、代码设计/执行、分析、验证和迭代。 | https://arxiv.org/abs/2505.14738 |
| GeoEvolve_2025 | X4-Y4-Z1,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Abstract | "two nested loops"; "code evolver" | X4; Y4 | GeoEvolve 的内层 code evolver 生成/变异候选算法，外层 agentic controller 评估 global elites 并查询 GeoKnowRAG，构成层级式演化搜索。 | https://arxiv.org/abs/2509.21593 |
| GeoEvolve_2025 | X4-Y4-Z1,Z3,Z4,Z5,Z7,Z8 | arXiv HTML, Abstract/Appendix A.5-A.6 | "spatial interpolation"; "geospatial conformal prediction" | Z1/Z3/Z4/Z5/Z7/Z8 | 系统注入地理知识，自动设计、执行和评估 kriging 与 conformal prediction 算法；报告 RMSE 降低和不确定性估计提升，并在 appendix 总结发现的地理建模知识。 | https://arxiv.org/abs/2509.21593 |
| El_Agente_Q_2025 | X4-Y1-Z3,Z4,Z5,Z7,Z8 | arXiv/Cell Abstract | "LLM-based multi-agent system"; "hierarchical memory framework" | X4; Y1 | El Agente Q 是量子化学 multi-agent system，使用 hierarchical memory 支撑任务分解、工具选择、post-analysis 与文件处理；错误恢复和调试支撑反思/自修正。 | https://arxiv.org/abs/2505.02484 ; https://doi.org/10.1016/j.matt.2025.102263 |
| El_Agente_Q_2025 | X4-Y1-Z3,Z4,Z5,Z7,Z8 | arXiv/Cell Abstract | "quantum chemistry workflows"; "in situ debugging" | Z3/Z4/Z5/Z7/Z8 | 系统从自然语言动态生成并执行量子化学 workflow，包含提交、文件处理、post-analysis、action trace logs、长期多步执行和 in situ debugging。 | https://arxiv.org/abs/2505.02484 ; https://doi.org/10.1016/j.matt.2025.102263 |
| AccelMat_2025 | X3-Y2-Z2,Z3,Z7 | arXiv HTML, Sec. 1/Fig. 1 caption | "multi-LLM Critic system" | X3; Y2 | AccelMat 包含 Hypotheses Generation Agent、多个 critic LLM、summarizer 和 evaluation agent；Fig. 1 显示 GPT-4o、Claude、Gemini 三个 critics 并行评审候选。 | https://arxiv.org/abs/2501.13299 |
| AccelMat_2025 | X3-Y2-Z2,Z3,Z7 | arXiv HTML, Sec. 1/Sec. 6.1 | "20 hypotheses"; "reviewed by three critics" | Z2/Z3/Z7 | 系统面向材料发现/设计目标生成多条假设，并用 alignment、plausibility、novelty、feasibility、testability 等质量指标评审，支撑假设生成、实验/设计指向和专家式验证。 | https://arxiv.org/abs/2501.13299 |
| BFS_Prover_V2_2025 | X3-Y3-Z3,Z4,Z7,Z8 | arXiv HTML, Abstract/Contributions | "parallel prover agents"; "shared proof cache" | X3; Y3 | BFS-Prover-V2 使用 planner 分解 theorem/subgoals，再由一组并行 prover agents 共享 proof cache 进行 multi-agent tree search。 | https://arxiv.org/abs/2509.06493 |
| BFS_Prover_V2_2025 | X3-Y3-Z3,Z4,Z7,Z8 | arXiv HTML, Sec. 2/Experiments | "Lean4"; "MiniF2F and ProofNet" | Z3/Z4/Z7/Z8 | 系统把 Lean4 proof search 形式化为多轮 agent-environment 交互，生成 tactic、调用 Lean compiler 验证，并在 MiniF2F/ProofNet 上报告证明成功率，支撑证明设计、执行、验证和长期训练/推理迭代。 | https://arxiv.org/abs/2509.06493 |
| LeanMarathon_2026 | X4-Y3-Z3,Z4,Z7,Z8 | arXiv HTML, Abstract | "four contract-scoped agents"; "proof DAG" | X4; Y3 | LeanMarathon 的 Blueprinter、Target-Reviewer、Worker、Refiner 四类 agents 由 two-stage orchestrator 协调，并沿 proof DAG 自底向上推进证明。 | https://arxiv.org/abs/2606.05400 |
| LeanMarathon_2026 | X4-Y3-Z3,Z4,Z7,Z8 | arXiv HTML, Abstract/Sec. 2-3 | "CI-gated rounds"; "no sorry" | Z3/Z4/Z7/Z8 | 系统构造 blueprint、审计目标、worker 局部 formalize、Refiner 修复，所有 PR 经 CI verifier；实验中 autonomous runs formalize 七个 target theorems with no sorry。 | https://arxiv.org/abs/2606.05400 |
| Automatic_Textbook_Formalization_2026 | X3-Y2-Z3,Z4,Z7,Z8 | arXiv HTML, Abstract/Sec. 1 | "30K Claude 4.5 Opus agents"; "Pull request review" | X3; Y2 | 该系统用大量同类 Claude agents 在共享代码库中并行工作，并通过版本控制、PR review、merge queue 和 independent reviewers 组织候选提交与筛选。 | https://arxiv.org/abs/2604.03071 |
| Automatic_Textbook_Formalization_2026 | X3-Y2-Z3,Z4,Z7,Z8 | arXiv HTML, Abstract/Fig. 1 caption | "shared code base"; "340 target theorems and definitions" | Z3/Z4/Z7/Z8 | 目标是把 500+ 页教材 formalize 到 Lean，产出 130K 行 Lean code、5900 declarations；Fig. 1 说明最终 340 个目标定义/定理都 present and proved，支撑形式化设计、执行、验证和持续迭代。 | https://arxiv.org/abs/2604.03071 |
| MA_LoT_2025 | X2-Y1-Z3,Z4,Z7 | PMLR Abstract / arXiv Sec. 1-2 | "prover agent"; "corrector agent" | X2; Y1 | MA-LoT 把证明生成和错误分析/修正分给 prover 与 corrector，属于固定异质角色协作；核心不是树搜索，而是 Lean feedback 下的反思修正。 | https://proceedings.mlr.press/v267/wang25cb.html ; https://arxiv.org/abs/2503.03205 |
| MA_LoT_2025 | X2-Y1-Z3,Z4,Z7 | PMLR Abstract / arXiv Sec. 2.3 | "Lean4 verifier"; "iterative refinement" | Z3/Z4/Z7 | Prover 生成 proof draft，Lean evaluator/verifier 检查，corrector 根据错误反馈生成 revised proof，循环至成功或上限；支撑证明设计、执行和形式验证。 | https://proceedings.mlr.press/v267/wang25cb.html ; https://arxiv.org/abs/2503.03205 |

## 原文证据薄弱或需谨慎使用的条目

> 这些条目不是从矩阵中删除，而是在正文中需要保守表述：例如只把它们作为预印本系统、in silico pipeline、评审/验证子系统、形式证明子域或开放协议证据，避免外推为完整湿实验闭环或已被广泛复现的科学发现。

### xyz_evidence_batch_1_core_asd
- 未发现完全无法定位一手来源的条目；15 篇均找到 arXiv、DOI、Nature/Matter/npj 页面或 OpenReview 之一。
- 证据相对薄弱、需在综述正文中谨慎措辞：Kosmos_2025、EvoScientist_2026、MAESTRO_2026、MOFGen_2025、PriM_2025、Science_Earth_2026、AScience_ASCollab_2025、SAGA_2025 主要依赖 arXiv/预印本或 workshop 版本，部分结论尚需同行评议或独立复现。
- AScience_ASCollab_2025 的 Z7 是“peer review/专家评价 + 明确承认 wet-lab validation remains indispensable”，不能写成已经完成湿实验验证。
- Robin_2026、CoScientist_2026 的生物医学结果属于早期体外/机制验证或 lab-in-the-loop，不应写成临床有效性或完全机器人闭环。

### xyz_evidence_batch_2_asd_related
| 文献 | 问题 | 处理建议 |
|---|---|---|
| BioAgents_2025 | `Y1` 证据相对薄弱：原文有 self-evaluation / reprocess 机制，但也明确说重复 refinement 可能降低质量；系统主贡献更偏 bioinformatics analysis 支持。 | 保留 `Y1` 时建议在正文中写成“有限 self-evaluation / troubleshooting”，不要写成强闭环自我改进。 |
| AI_Researcher_HKU_2025 | `Y2` 主要来自 arXiv HTML 方法段的 divergent-convergent idea selection，而不是摘要；需避免只用摘要支撑候选筛选。 | 正文引用时同时引用 3.1.2 idea generation 或 HTML 方法段。 |
| ScienceClaw_Infinite_2026 | 项目名为 ScienceClaw + Infinite，但 arXiv 正式标题是 *Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange*。 | 矩阵可继续用项目短名，但参考文献条目应按 arXiv 正式标题列出。 |
| TopoMAS_2025 | 用户给定题名近似为 “A Hierarchical Multi-Agent System...”，arXiv 正式题名为 *Large Language Model Driven Topological Materials Multiagent System*。 | 矩阵保留 TopoMAS 短名即可；参考文献用正式 arXiv/Wiley 标题。 |
| 全部 15 篇 | 未发现完全无法定位一手来源的论文；均找到了 arXiv、Nature / Scientific Reports 或 DOI 页面。 | 后续若要更严格，可把当前短语证据升级为 PDF 页码/图号级证据。 |

### xyz_evidence_batch_3_methods_substrates
| 文献 | 问题 | 当前处理 |
|---|---|---|
| MAGenIdeas_2026 | 浏览器未取得 arXiv HTML/PDF 正文，只取得 arXiv 摘要页；摘要信息足以支撑分类，但系统细节证据偏摘要级。 | 使用 arXiv 摘要和其公开代码/数据/demo 声明。 |
| PaperOrchestra_2026 | arXiv HTML 未能打开，主要一手证据来自 arXiv 摘要；ResearchGate 有 PDF 文本镜像但非首选一手。 | 使用 arXiv 摘要；未采用二手新闻/社媒。 |
| LLM_Verifier_2025 | 给定短名“LLM_Verifier_2025”与一手题名不完全一致；本地系统笔记与分类最匹配来源为 OpenReview 论文 *Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers*。 | 按 MAV / multiple verifiers 的 verification substrate 记录为 `X3-Y2-Z7`；不要混用 *The Need for Verification in AI-Driven Scientific Discovery* 的综述证据。 |
| OR_Agent_2026 | 检索到 OR-Agent 与 EvoOR-Agent 两篇相近 OR/agent 论文；给定短名更匹配 OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery。 | 使用 arXiv:2602.13769 的 OR-Agent；未混用 EvoOR-Agent 证据。 |
| ResearchAgent_2025 | 初版 arXiv 为 2024，但 ACL Anthology 正式会议版本为 NAACL 2025。 | 使用 ACL Anthology 2025 PDF 作为正式一手来源。 |

### xyz_evidence_batch_4_bio_ml_review
| 文献 | 情况 |
|---|---|
| AGAPI_Agents_2025 | 已找到 arXiv 一手来源；但截至本次核对主要是 2025 年底预印本/平台论文，材料发现成效多来自 API 编排、示例 workflow 和与实验数据比较，不能写成已经完成湿实验闭环发现。 |
| AutoResearchClaw_2026 | 已找到 arXiv 一手来源；论文很新，证据以 ARC-Bench 和系统机制为主，适合作为 automated research harness / workflow evolution 证据，不宜作为单一自然科学发现的强实证。 |
| AgentRxiv_2025 | 一手来源充分；但其 Z 覆盖不包含严格 peer-review validation，主要是共享报告、检索、吸收结果和长期迭代。 |
| Generative_Adversarial_Reviews_2024 | 一手来源充分；但只支撑 review/critic/validation，不支撑完整科学发现闭环。 |
| MLZero_2025 / KompeteAI_2025 / IMPROVE_2025 | 一手来源充分；但它们主要是 AutoML / ML pipeline automation，对科学发现综述应作为计算型 harness 或 ML research automation 证据，而非生物/化学实验发现证据。 |
未发现完全无法定位一手来源的条目。

### xyz_evidence_batch_5_harness_formal_drug
- 未发现完全无法定位一手来源的条目；14 篇均至少有 arXiv、DOI、ACL Anthology、PMLR 或官方项目页等来源。
- `Claw_AI_Lab_2026`：可用 arXiv 与官网，但标题在本地笔记中写作 "A Hierarchical Multi-Agent Research Laboratory"，一手 arXiv 标题为 "An Autonomous Multi-Agent Research Team"；证据更偏系统/平台宣称，科学发现案例仍需保守表述。
- `Mozi_2026`、`SCP_2025`、`GeoEvolve_2025`、`LeanMarathon_2026`、`Automatic_Textbook_Formalization_2026`：主要证据来自 arXiv 预印本，尚未按当前检索结果确认同行评议版本。
- `AccelMat_2025`：一手标题是 "Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents"，`AccelMat` 是框架名而非论文题名；Z 轴应保守限于假设生成、设计指向和评审，不宜写成实验执行闭环。
- `BFS_Prover_V2_2025`：论文题名是 "Scaling up Multi-Turn Off-Policy RL and Multi-Agent Tree Search for LLM Step-Provers"，BFS-Prover-V2 是系统名；其覆盖面限于 Lean 形式证明，不应外推为自然科学实验发现。
- `MADD_2025`、`DrugMCTS_2025`、`Mozi_2026`：药物方向证据多为 in silico pipeline / benchmark / governed workflow；除 eNRRCrew 明确提到推荐催化剂的实验验证外，不宜把这些条目写成已完成湿实验验证的新药发现。
