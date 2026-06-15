# XYZ 交叉分布：严格 ASD 系统与 ASD 相关系统

> 口径：基于 `xyz_literature_classification_matrix.md`，保留严格 ASD 系统与 ASD 相关系统的全部 X/Y/Z 坐标。
> 文献数量：133 篇，其中严格 ASD 系统 41 篇，ASD 相关系统 92 篇。
> 展开方式：一篇文献只有一个 X、一个 Y，但可对应多个 Z；因此同一篇文献可能出现在多个 `Xn-Yn-Zn` 组合下。
> 本表只列出有文献命中的组合，并在每个组合后标注其含义。

## 坐标含义

- `X0`：非显式多智能体 / 单 agent / 普通 pipeline。
- `X2`：固定角色多智能体。
- `X3`：同角色多实例 / 并行候选。
- `X4`：层级式多智能体。
- `X5`：开放能力网络。
- `Y0`：无明显搜索/演化机制。
- `Y1-Y5`：反思、自我修正、候选筛选、搜索、演化优化或 harness/capability evolution。

## 交叉分布

| XYZ 组合 | 组合含义 | 数量 | 对应文献 |
|---|---|---:|---|
| X0-Y0-Z3 | 非显式多智能体 / 单 agent / 普通 pipeline + 无明显搜索/演化机制 + 实验、仿真、代码或证明设计 | 1 | SafeScientist_2025 |
| X0-Y0-Z4 | 非显式多智能体 / 单 agent / 普通 pipeline + 无明显搜索/演化机制 + 执行：代码、工具、实验、证明或机器人操作 | 1 | SafeScientist_2025 |
| X0-Y0-Z7 | 非显式多智能体 / 单 agent / 普通 pipeline + 无明显搜索/演化机制 + 验证 / validation / review | 1 | SafeScientist_2025 |
| X0-Y1-Z1 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 知识 grounding / 文献综述 | 10 | Autonomous_Materials_Computation_2025, AutoSurvey_2024, BioMedAgent_2026, GeneAgent_2025, GPT_Researcher_2024, HypER_2025, Open_Domain_Hypotheses_2023, OpenScholar_2025, Paper2Code_2025, TxAgent_2025 |
| X0-Y1-Z2 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 问题形成 / 假设生成 | 2 | HypER_2025, Open_Domain_Hypotheses_2023 |
| X0-Y1-Z3 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 实验、仿真、代码或证明设计 | 7 | Autonomous_Materials_Computation_2025, BioMedAgent_2026, DrSR_2025, GeneAgent_2025, Paper2Code_2025, SR_Scientist_2026, TxAgent_2025 |
| X0-Y1-Z4 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 执行：代码、工具、实验、证明或机器人操作 | 9 | Autonomous_Materials_Computation_2025, BioMedAgent_2026, CellVoyager_2026, DatawiseAgent_2025, DrSR_2025, GeneAgent_2025, Paper2Code_2025, SR_Scientist_2026, TxAgent_2025 |
| X0-Y1-Z5 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 结果分析 / 错误诊断 | 8 | Autonomous_Materials_Computation_2025, BioMedAgent_2026, CellVoyager_2026, DatawiseAgent_2025, DrSR_2025, GeneAgent_2025, SR_Scientist_2026, TxAgent_2025 |
| X0-Y1-Z6 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 综合 / 报告 / 论文写作 | 5 | AutoSurvey_2024, CellVoyager_2026, DatawiseAgent_2025, GPT_Researcher_2024, OpenScholar_2025 |
| X0-Y1-Z7 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 验证 / validation / review | 17 | Autonomous_Materials_Computation_2025, AutoSurvey_2024, BioMedAgent_2026, CellVoyager_2026, DeepReview_2025, DrSR_2025, GeneAgent_2025, GPT_Researcher_2024, HypER_2025, Open_Domain_Hypotheses_2023, OpenScholar_2025, Paper2Code_2025, Reviewer2_2024, ReviewerGPT_2023, SPOT_A_2025, SR_Scientist_2026, TxAgent_2025 |
| X0-Y1-Z8 | 非显式多智能体 / 单 agent / 普通 pipeline + 反思 / 自我修正 + 迭代 / 长周期发现 | 2 | DrSR_2025, SR_Scientist_2026 |
| X0-Y2-Z1 | 非显式多智能体 / 单 agent / 普通 pipeline + 候选生成与筛选 + 知识 grounding / 文献综述 | 5 | Graph2Idea_2026, Medea_2026, MOSAIC_Chemical_Synthesis_2026, Scideator_2024, Sparks_of_Science_2025 |
| X0-Y2-Z2 | 非显式多智能体 / 单 agent / 普通 pipeline + 候选生成与筛选 + 问题形成 / 假设生成 | 8 | Causal_Hypothesis_LLM_2025, Graph2Idea_2026, GraphEval_Idea_2025, Medea_2026, OpenAI_Unit_Distance_2026, Scideator_2024, SPARK_Cancer_Pathology_2026, Sparks_of_Science_2025 |
| X0-Y2-Z3 | 非显式多智能体 / 单 agent / 普通 pipeline + 候选生成与筛选 + 实验、仿真、代码或证明设计 | 5 | Adaptive_AI_Decision_Interface_2025, Coscientist_2023, MOSAIC_Chemical_Synthesis_2026, OpenAI_Unit_Distance_2026, SPARK_Cancer_Pathology_2026 |
| X0-Y2-Z4 | 非显式多智能体 / 单 agent / 普通 pipeline + 候选生成与筛选 + 执行：代码、工具、实验、证明或机器人操作 | 2 | Coscientist_2023, SPARK_Cancer_Pathology_2026 |
| X0-Y2-Z5 | 非显式多智能体 / 单 agent / 普通 pipeline + 候选生成与筛选 + 结果分析 / 错误诊断 | 2 | Adaptive_AI_Decision_Interface_2025, SPARK_Cancer_Pathology_2026 |
| X0-Y2-Z7 | 非显式多智能体 / 单 agent / 普通 pipeline + 候选生成与筛选 + 验证 / validation / review | 11 | Adaptive_AI_Decision_Interface_2025, Causal_Hypothesis_LLM_2025, Coscientist_2023, Graph2Idea_2026, GraphEval_Idea_2025, Medea_2026, MOSAIC_Chemical_Synthesis_2026, OpenAI_Unit_Distance_2026, Scideator_2024, SPARK_Cancer_Pathology_2026, Sparks_of_Science_2025 |
| X0-Y3-Z1 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 知识 grounding / 文献综述 | 2 | Nova_2024, TianJi_2026 |
| X0-Y3-Z2 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 问题形成 / 假设生成 | 7 | AI_Scientist_Nature_2026, AutoDiscovery_2025, ERA_2026, MC_NEST_2025, Nova_2024, Robot_Scientist_2004, TianJi_2026 |
| X0-Y3-Z3 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 实验、仿真、代码或证明设计 | 11 | AFION_Plasmonic_SDL_2025, AI_Scientist_Nature_2026, AIDE_2025, ALab_2023, ERA_2026, Jupiter_Notebook_Agent_2025, Rainbow_Perovskite_2025, RoboChem_Flex_2026, Robot_Scientist_2004, SciNav_2026, TianJi_2026 |
| X0-Y3-Z4 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 执行：代码、工具、实验、证明或机器人操作 | 12 | AFION_Plasmonic_SDL_2025, AI_Scientist_Nature_2026, AIDE_2025, ALab_2023, AutoDiscovery_2025, ERA_2026, Jupiter_Notebook_Agent_2025, Rainbow_Perovskite_2025, RoboChem_Flex_2026, Robot_Scientist_2004, SciNav_2026, TianJi_2026 |
| X0-Y3-Z5 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 结果分析 / 错误诊断 | 11 | AFION_Plasmonic_SDL_2025, AI_Scientist_Nature_2026, AIDE_2025, ALab_2023, AutoDiscovery_2025, Jupiter_Notebook_Agent_2025, Rainbow_Perovskite_2025, RoboChem_Flex_2026, Robot_Scientist_2004, SciNav_2026, TianJi_2026 |
| X0-Y3-Z6 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 综合 / 报告 / 论文写作 | 1 | AI_Scientist_Nature_2026 |
| X0-Y3-Z7 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 验证 / validation / review | 11 | AFION_Plasmonic_SDL_2025, AI_Scientist_Nature_2026, AIDE_2025, ALab_2023, AutoDiscovery_2025, ERA_2026, Nova_2024, Rainbow_Perovskite_2025, RoboChem_Flex_2026, Robot_Scientist_2004, TianJi_2026 |
| X0-Y3-Z8 | 非显式多智能体 / 单 agent / 普通 pipeline + 树搜索 / MCTS / trajectory search + 迭代 / 长周期发现 | 14 | AFION_Plasmonic_SDL_2025, AI_Scientist_Nature_2026, AIDE_2025, ALab_2023, AutoDiscovery_2025, ERA_2026, Jupiter_Notebook_Agent_2025, MC_NEST_2025, Nova_2024, Rainbow_Perovskite_2025, RoboChem_Flex_2026, Robot_Scientist_2004, SciNav_2026, TianJi_2026 |
| X0-Y4-Z1 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 知识 grounding / 文献综述 | 4 | AI_Scientist_2024, CodeScientist_2025, EvoGens_2026, FlowPIE_2026 |
| X0-Y4-Z2 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 问题形成 / 假设生成 | 4 | AI_Scientist_2024, CodeScientist_2025, EvoGens_2026, FlowPIE_2026 |
| X0-Y4-Z3 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 实验、仿真、代码或证明设计 | 5 | AI_Scientist_2024, AlphaEvolve_2025, CodeScientist_2025, EvoSLD_2025, LLM_SR_2024 |
| X0-Y4-Z4 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 执行：代码、工具、实验、证明或机器人操作 | 5 | AI_Scientist_2024, AlphaEvolve_2025, CodeScientist_2025, EvoSLD_2025, LLM_SR_2024 |
| X0-Y4-Z5 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 结果分析 / 错误诊断 | 4 | AI_Scientist_2024, CodeScientist_2025, EvoSLD_2025, LLM_SR_2024 |
| X0-Y4-Z6 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 综合 / 报告 / 论文写作 | 2 | AI_Scientist_2024, CodeScientist_2025 |
| X0-Y4-Z7 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 验证 / validation / review | 7 | AI_Scientist_2024, AlphaEvolve_2025, CodeScientist_2025, EvoGens_2026, EvoSLD_2025, FlowPIE_2026, LLM_SR_2024 |
| X0-Y4-Z8 | 非显式多智能体 / 单 agent / 普通 pipeline + 演化式优化 + 迭代 / 长周期发现 | 7 | AI_Scientist_2024, AlphaEvolve_2025, CodeScientist_2025, EvoGens_2026, EvoSLD_2025, FlowPIE_2026, LLM_SR_2024 |
| X0-Y5-Z1 | 非显式多智能体 / 单 agent / 普通 pipeline + harness / capability evolution + 知识 grounding / 文献综述 | 3 | CASCADE_2025, SciToolAgent_2025, ToolUniverse_2025 |
| X0-Y5-Z3 | 非显式多智能体 / 单 agent / 普通 pipeline + harness / capability evolution + 实验、仿真、代码或证明设计 | 6 | CASCADE_2025, Climate_Self_Evolving_Agent_2025, DS_Agent_2024, SciToolAgent_2025, STELLA_2025, ToolUniverse_2025 |
| X0-Y5-Z4 | 非显式多智能体 / 单 agent / 普通 pipeline + harness / capability evolution + 执行：代码、工具、实验、证明或机器人操作 | 6 | CASCADE_2025, Climate_Self_Evolving_Agent_2025, DS_Agent_2024, SciToolAgent_2025, STELLA_2025, ToolUniverse_2025 |
| X0-Y5-Z5 | 非显式多智能体 / 单 agent / 普通 pipeline + harness / capability evolution + 结果分析 / 错误诊断 | 6 | CASCADE_2025, Climate_Self_Evolving_Agent_2025, DS_Agent_2024, SciToolAgent_2025, STELLA_2025, ToolUniverse_2025 |
| X0-Y5-Z7 | 非显式多智能体 / 单 agent / 普通 pipeline + harness / capability evolution + 验证 / validation / review | 4 | CASCADE_2025, DS_Agent_2024, SciToolAgent_2025, ToolUniverse_2025 |
| X0-Y5-Z8 | 非显式多智能体 / 单 agent / 普通 pipeline + harness / capability evolution + 迭代 / 长周期发现 | 5 | CASCADE_2025, Climate_Self_Evolving_Agent_2025, DS_Agent_2024, STELLA_2025, ToolUniverse_2025 |
| X2-Y0-Z1 | 固定角色多智能体 + 无明显搜索/演化机制 + 知识 grounding / 文献综述 | 1 | DrugAgent_2024 |
| X2-Y0-Z2 | 固定角色多智能体 + 无明显搜索/演化机制 + 问题形成 / 假设生成 | 1 | MM_Agent_2025 |
| X2-Y0-Z3 | 固定角色多智能体 + 无明显搜索/演化机制 + 实验、仿真、代码或证明设计 | 2 | DrugAgent_2024, MM_Agent_2025 |
| X2-Y0-Z4 | 固定角色多智能体 + 无明显搜索/演化机制 + 执行：代码、工具、实验、证明或机器人操作 | 2 | DrugAgent_2024, MM_Agent_2025 |
| X2-Y0-Z5 | 固定角色多智能体 + 无明显搜索/演化机制 + 结果分析 / 错误诊断 | 2 | DrugAgent_2024, MM_Agent_2025 |
| X2-Y0-Z6 | 固定角色多智能体 + 无明显搜索/演化机制 + 综合 / 报告 / 论文写作 | 1 | MM_Agent_2025 |
| X2-Y0-Z7 | 固定角色多智能体 + 无明显搜索/演化机制 + 验证 / validation / review | 2 | DrugAgent_2024, MM_Agent_2025 |
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
| X4-Y0-Z1 | 层级式多智能体 + 无明显搜索/演化机制 + 知识 grounding / 文献综述 | 1 | MatSciAgent_2026 |
| X4-Y0-Z3 | 层级式多智能体 + 无明显搜索/演化机制 + 实验、仿真、代码或证明设计 | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
| X4-Y0-Z4 | 层级式多智能体 + 无明显搜索/演化机制 + 执行：代码、工具、实验、证明或机器人操作 | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
| X4-Y0-Z5 | 层级式多智能体 + 无明显搜索/演化机制 + 结果分析 / 错误诊断 | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
| X4-Y0-Z7 | 层级式多智能体 + 无明显搜索/演化机制 + 验证 / validation / review | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
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
| X0-Y0-Z3 | 1 | SafeScientist_2025 |
| X0-Y0-Z4 | 1 | SafeScientist_2025 |
| X0-Y0-Z7 | 1 | SafeScientist_2025 |
| X0-Y1-Z2 | 2 | HypER_2025, Open_Domain_Hypotheses_2023 |
| X0-Y1-Z8 | 2 | DrSR_2025, SR_Scientist_2026 |
| X0-Y2-Z4 | 2 | Coscientist_2023, SPARK_Cancer_Pathology_2026 |
| X0-Y2-Z5 | 2 | Adaptive_AI_Decision_Interface_2025, SPARK_Cancer_Pathology_2026 |
| X0-Y3-Z1 | 2 | Nova_2024, TianJi_2026 |
| X0-Y3-Z6 | 1 | AI_Scientist_Nature_2026 |
| X0-Y4-Z6 | 2 | AI_Scientist_2024, CodeScientist_2025 |
| X0-Y5-Z1 | 3 | CASCADE_2025, SciToolAgent_2025, ToolUniverse_2025 |
| X2-Y0-Z1 | 1 | DrugAgent_2024 |
| X2-Y0-Z2 | 1 | MM_Agent_2025 |
| X2-Y0-Z3 | 2 | DrugAgent_2024, MM_Agent_2025 |
| X2-Y0-Z4 | 2 | DrugAgent_2024, MM_Agent_2025 |
| X2-Y0-Z5 | 2 | DrugAgent_2024, MM_Agent_2025 |
| X2-Y0-Z6 | 1 | MM_Agent_2025 |
| X2-Y0-Z7 | 2 | DrugAgent_2024, MM_Agent_2025 |
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
| X4-Y0-Z1 | 1 | MatSciAgent_2026 |
| X4-Y0-Z3 | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
| X4-Y0-Z4 | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
| X4-Y0-Z5 | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
| X4-Y0-Z7 | 2 | MatSciAgent_2026, PhenoAssistant_2026 |
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
