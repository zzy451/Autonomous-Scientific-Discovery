# XYZ 文献分类矩阵：严格 ASD 系统与 ASD 相关系统

> 目的：只保留两类文献：**严格 ASD 系统**与**ASD 相关系统**。  
> 严格 ASD 系统：直接证明 autonomous scientific discovery 已经出现多智能体、搜索/演化或闭环发现工作流。  
> ASD 相关系统：不完整覆盖科学发现全流程，但支撑文献、代码、实验、验证、审稿等关键环节。  
> 本文件不再纳入纯综述、纯 benchmark、纯 memory/skill 机制、纯治理原则或一般 agent 基础设施；这些材料仍可在其他章节作为背景和边界支撑。

## 坐标轴定义

### X 轴：Multi-Agent 组织形态

| 编码 | 含义 |
|---|---|
| X0 | 非显式多智能体：单 agent、单模型、单项系统或普通模块化 pipeline |
| X2 | 固定角色多智能体：多个明确角色，如 researcher、critic、coder、reviewer、PI、analyst |
| X3 | 同角色多实例 / 并行候选：多个 hypothesis agents、prover agents、reviewers 并行探索或评判 |
| X4 | 层级式多智能体：coordinator / manager / supervisor 调度多个 worker agents |
| X5 | 开放能力网络：不只是固定团队，而是开放 scientific capability network，如 Science Earth / EACN |

### Y 轴：演化 / 搜索机制

| 编码 | 含义 |
|---|---|
| Y0 | 无明显搜索/演化机制 |
| Y1 | 反思 / 自我修正：生成后 critique、revise、reflect、debug 或 failure detection |
| Y2 | 候选生成与筛选：生成多个候选并排序、打分、评审、比较或选择 |
| Y3 | 树搜索 / MCTS / trajectory search：系统性搜索假设、代码、notebook 或证明路径 |
| Y4 | 演化式优化：mutation、recombination、population、Elo、tournament、archive |
| Y5 | harness / capability evolution：workflow、skill、memory、agent 能力或开放能力网络本身发生更新 |

### Z 轴：自主科学研究发现流程

| 编码 | 阶段 | 含义 |
|---|---|---|
| Z1 | Knowledge Grounding / Literature Review | 文献检索、证据 grounding、知识整理 |
| Z2 | Problem Formulation / Hypothesis Generation | 问题发现、假设生成、idea generation |
| Z3 | Experiment / Simulation / Code / Proof Design | 实验设计、仿真设计、代码方案、证明草图 |
| Z4 | Execution | 代码执行、工具调用、实验执行、证明尝试、机器人实验 |
| Z5 | Result Analysis | 数据分析、结果解释、错误诊断 |
| Z6 | Synthesis / Reporting | 报告生成、论文写作、知识综合 |
| Z7 | Verification / Validation / Review | 引用验证、代码复现、形式证明、人类专家审查、物理实验验证 |
| Z8 | Iteration / Long-Horizon Discovery | 长周期项目管理、失败分支复用、持续演化、世界模型更新 |

## 1. 严格 ASD 系统

| 文献 | X | Y | Z | 分类理由 |
|---|---:|---:|---|---|
| AFION_Plasmonic_SDL_2025 | X0 | Y3 | Z3,Z4,Z5,Z7,Z8 | plasmonic self-driving lab，在线表征与多目标实验搜索 |
| Agent_Laboratory_2024 | X2 | Y1 | Z1,Z2,Z3,Z4,Z5,Z6,Z7 | 固定科研角色团队，覆盖文献、实验、写作和评审 |
| AI_Scientist_2024 | X0 | Y4 | Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | 端到端机器学习研究自动化，包含 archive/open-ended iteration |
| AI_Scientist_Nature_2026 | X0 | Y3 | Z2,Z3,Z4,Z5,Z6,Z7,Z8 | agentic tree search 支撑端到端 AI research automation；多模型/自动评审证据不足以归为显式多智能体 |
| ALab_2023 | X0 | Y3 | Z3,Z4,Z5,Z7,Z8 | 材料合成 self-driving lab，真实实验闭环和路线更新 |
| AlphaEvolve_2025 | X0 | Y4 | Z3,Z4,Z7,Z8 | 面向可执行代码/算法产物的 generate-test-refine 与演化式优化 |
| AlphaProof_Nexus_2026 | X3 | Y4 | Z3,Z4,Z7,Z8 | 多 prover / rating agents、population database 与 Lean 验证 |
| Coscientist_2023 | X0 | Y2 | Z3,Z4,Z7 | LLM planner 连接化学实验自动化接口，支撑实验设计与执行 |
| CoScientist_2026 | X4 | Y4 | Z1,Z2,Z3,Z7,Z8 | Supervisor 调度专门 agents，Elo tournament 与 hypothesis evolution |
| ERA_2026 | X0 | Y3 | Z2,Z3,Z4,Z7,Z8 | empirical scientific software 的 LLM rewriting、tree search、sandbox scoring |
| EvoScientist_2026 | X2 | Y5 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | Researcher、Engineer、Evolution Manager 多角色系统，通过 ideation / experimentation memory 推进 harness evolution |
| Kosmos_2025 | X2 | Y5 | Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | 多角色科研组织、world model、长周期状态和证据链接报告 |
| MAESTRO_2026 | X2 | Y1 | Z2,Z3,Z4,Z5,Z7,Z8 | 多智能体催化剂设计循环，通过反思、设计历史和 in-context learning 改进候选 |
| MARS_Materials_2026 | X4 | Y2 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | 19 个 LLM agents、16 个领域工具和机器人实验平台组成材料发现闭环 |
| MASTER_2025 | X4 | Y2 | Z2,Z3,Z4,Z5,Z7,Z8 | hierarchical multi-agent reasoning 指导 atomistic simulation 和 functional materials discovery |
| MOFGen_2025 | X2 | Y2 | Z2,Z3,Z4,Z5,Z7,Z8 | LLM、diffusion model、quantum mechanical agents 和 synthetic-feasibility agents 协同发现 MOF |
| PriM_2025 | X2 | Y3 | Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | principle-inspired multi-agent material discovery，包含 Literature/Hypothesis/Experiment/Optimizer/Analysis agents 与 MCTS 驱动的实验反馈搜索 |
| Rainbow_Perovskite_2025 | X0 | Y3 | Z3,Z4,Z5,Z7,Z8 | 多机器人材料实验与多目标 Bayesian optimization |
| Robin_2026 | X4 | Y2 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | Robin 编排 Crow、Falcon、Finch 等专门 agents，lab-in-the-loop 覆盖候选、实验、分析和再提案 |
| RoboChem_Flex_2026 | X0 | Y3 | Z3,Z4,Z5,Z7,Z8 | 模块化 self-driving lab 与 Bayesian optimization 闭环 |
| Robot_Scientist_2004 | X0 | Y3 | Z2,Z3,Z4,Z5,Z7,Z8 | hypothesis -> experiment -> knowledge update 的早期自动发现闭环 |
| Science_Earth_2026 | X5 | Y5 | Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | EACN、capability discovery、task bidding、cross-regime adjudication |
| AScience_ASCollab_2025 | X5 | Y5 | Z2,Z4,Z5,Z7,Z8 | evolving networks of autonomous scientific agents，支撑假设 hunting、协作网络和 peer-review 式评价 |
| SAGA_2025 | X4 | Y5 | Z2,Z3,Z4,Z5,Z7,Z8 | goal-evolving agents 通过外层目标/评分函数更新和内层 solution optimization 推进 discovery loop |
| SciDER_2026 | X2 | Y4 | Z2,Z3,Z4,Z5,Z7,Z8 | ideation、data analysis、experimentation、critic 多角色系统，使用 Evolutionary Idea Search 推进 data-centric discovery |
| AutoDiscovery_2025 | X0 | Y3 | Z2,Z4,Z5,Z7,Z8 | 以 Bayesian surprise 和 MCTS 驱动开放式科学发现，支撑问题探索、执行、分析和迭代 |
| CodeScientist_2025 | X0 | Y4 | Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | 以代码实验、遗传搜索、外部复查和复现实验组织端到端科学发现 |
| CycleResearcher_2024 | X2 | Y5 | Z1,Z2,Z3,Z6,Z7,Z8 | researcher / reviewer 循环推动自动研究、自动评审和下一轮修订 |
| EvoSLD_2025 | X0 | Y4 | Z3,Z4,Z5,Z7,Z8 | LLM 引导的演化式 neural scaling law discovery，产物为可执行/可评估规律 |
| LLM_SR_2024 | X0 | Y4 | Z3,Z4,Z5,Z7,Z8 | LLM-guided evolutionary program search，用于科学方程和符号规律发现 |
| ProtAgents_2024 | X2 | Y2 | Z1,Z3,Z4,Z5,Z7 | 多智能体结合物理知识和机器学习，支撑蛋白质设计、评估和验证 |
| SciAgents_2024 | X2 | Y5 | Z1,Z2,Z3,Z5,Z7,Z8 | multi-agent graph reasoning 与 in-situ learning 生成并改进材料科学假设 |
| SparksMatter_2025 | X2 | Y1 | Z1,Z2,Z3,Z5,Z6,Z7,Z8 | 多智能体材料推理系统，通过物理知识、批评和修订支持无机材料发现 |
| SR_Scientist_2026 | X0 | Y1 | Z3,Z4,Z5,Z7,Z8 | agentic symbolic regression / equation discovery，通过工具驱动数据分析、公式实现、评估反馈和修订发现方程 |
| TianJi_2026 | X0 | Y3 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | 文献、假设、数值实验、物理解释组成仿真发现 workflow |
| Virtual_Lab_2025 | X2 | Y4 | Z1,Z2,Z3,Z5,Z7,Z8 | PI、specialist、critic 多角色会议与 mutation-selection pipeline |

| AtomAgents_2025 | X2 | Y2 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | physics-aware 多模态多智能体系统，结合知识检索、LAMMPS 仿真、代码执行和结果分析，用于合金设计与假设验证 |
| DREAMS_2025 | X4 | Y1 | Z3,Z4,Z5,Z7,Z8 | central LLM planner 调度结构生成、DFT 收敛、HPC scheduling 和 error-handling agents，反思式重规划支撑材料仿真 |
| Materealize_2026 | X2 | Y2 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | 多智能体 deliberation 与工具编排支撑无机材料候选设计、合成路线、机制假设、工具执行和文献/物理验证 |
| ScienceClaw_Infinite_2026 | X5 | Y5 | Z1,Z3,Z4,Z5,Z6,Z7,Z8 | decentralized agents、300+ skill registry、artifact DAG、global index 和 discourse layer 形成开放科学能力/产物交换生态 |
| TopoMAS_2025 | X4 | Y5 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | hierarchical multi-agent framework 覆盖拓扑材料检索、理论推理、结构生成、DFT validation，并通过动态知识图谱更新支撑 memory / harness evolution |

## 2. ASD 相关系统

| 文献 | 支撑环节 | X | Y | Z | 分类理由 |
|---|---|---:|---:|---|---|
| Adaptive_AI_Decision_Interface_2025 | 实验/分析/验证 | X0 | Y2 | Z3,Z5,Z7 | 人机材料发现界面，支撑候选比较、决策和人类检查点 |
| AI_Researcher_HKU_2025 | 文献/假设/写作 | X2 | Y2 | Z1,Z2,Z3,Z6,Z7 | research agent 与 paper agent 分工，候选想法到论文生成 |
| Autonomous_Materials_Computation_2025 | 材料计算/执行/验证 | X0 | Y1 | Z1,Z3,Z4,Z5,Z7 | 面向第一性原理材料计算的 agentic framework，支撑可靠参数选择、执行和验证 |
| AutoSurvey_2024 | 文献/综合 | X0 | Y1 | Z1,Z6,Z7 | 自动综述和文献综合，支撑 knowledge grounding 与 reporting |
| BioAgents_2025 | 文献/分析/验证 | X2 | Y1 | Z1,Z5,Z7 | Scientific Reports 多智能体生物信息分析系统，支撑固定角色协作、结果分析和验证 |
| BioMedAgent_2026 | 工具/分析/验证 | X0 | Y1 | Z1,Z3,Z4,Z5,Z7 | 生物医学工具调用与分析 agent |
| Causal_Hypothesis_LLM_2025 | 假设/验证 | X0 | Y2 | Z2,Z7 | 因果假设生成与专家/数据验证 |
| CellVoyager_2026 | 执行/分析/综合 | X0 | Y1 | Z4,Z5,Z6,Z7 | 计算生物数据分析 agent，支撑 notebook/data-analysis 修正 |
| Climate_Self_Evolving_Agent_2025 | 仿真/分析/迭代 | X0 | Y5 | Z3,Z4,Z5,Z8 | 气候科学 agent 通过失败反馈更新分析策略 |
| CRISPR_GPT_2026 | 实验设计/执行/验证 | X2 | Y1 | Z3,Z4,Z5,Z7 | Planner、Executor、Tool provider、User proxy 的固定角色协议 workflow |
| CASCADE_2025 | 技能/harness 演化 | X0 | Y5 | Z1,Z3,Z4,Z5,Z7,Z8 | 科学 agent 通过 autonomous skill creation 和 evolution 积累可复用技能 |
| DatawiseAgent_2025 | 执行/分析/报告 | X0 | Y1 | Z4,Z5,Z6 | notebook cells 逐步生成、执行、debug 和修正 |
| Deep_Research_2026 | 交互式科研工作流 | X2 | Y5 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | planning、data analysis、literature search、novelty detection agents 与 persistent world state |
| EvoSci_2026 | 文献/假设/评审/迭代 | X2 | Y4 | Z1,Z2,Z7,Z8 | bio-inspired multi-agent scientific discovery framework，支撑群体生成、评审、选择和科学想法演化 |
| FlowPIE_2026 | 文献/假设/迭代 | X0 | Y4 | Z1,Z2,Z7,Z8 | flow-guided literature exploration 与 test-time idea evolution，支撑科学想法产物的演化式优化 |
| GeneAgent_2025 | 文献/工具/分析 | X0 | Y1 | Z1,Z3,Z4,Z5,Z7 | 基因/生物信息工具链 agent |
| Graph2Idea_2026 | 文献/假设/验证 | X0 | Y2 | Z1,Z2,Z7 | graph-structured literature context 支撑 retrieval-augmented scientific idea generation |
| GPT_Researcher_2024 | 文献/报告 | X0 | Y1 | Z1,Z6,Z7 | 自动检索、综合和报告生成 |
| EvoGens_2026 | 文献/假设/迭代 | X0 | Y4 | Z1,Z2,Z7,Z8 | population-based evolutionary search，用 mutation、crossover、selection 改进 scientific ideas |
| Instrument_Agents_2026 | 仪器/执行/分析/验证/迭代 | X2 | Y5 | Z1,Z3,Z4,Z5,Z7,Z8 | 多智能体科学仪器操作系统，通过 on-the-job learning 和记忆更新支撑 harness / capability evolution |
| Jupiter_Notebook_Agent_2025 | 代码/notebook 搜索 | X0 | Y3 | Z3,Z4,Z5,Z8 | notebook trajectory 的 value-guided search |
| MAGenIdeas_2026 | 文献/假设/评审/迭代 | X2 | Y2 | Z1,Z2,Z7,Z8 | combinatorial innovation 与 multi-agent generate/evaluate/refine，用于研究想法生成和筛选；当前证据不足以归为树/轨迹搜索 |
| MatSciAgent_2026 | 文献/仿真/执行/分析/验证 | X4 | Y0 | Z1,Z3,Z4,Z5,Z7 | master agent 调度 task-specific materials agents，支撑层级式多任务材料计算工作流，但原文没有明确搜索/演化机制 |
| Mimosa_2026 | evolving multi-agent research workflow | X4 | Y5 | Z3,Z4,Z5,Z7,Z8 | meta-orchestrator 生成 task-specific workflow topology，并通过 judge feedback 改进多智能体 harness |
| OR_Agent_2026 | 自动算法发现 | X4 | Y4 | Z2,Z3,Z4,Z5,Z7,Z8 | tree-based workflow 结合 branching hypothesis generation、backtracking 和 evolutionary-systematic ideation |
| OmniScientist_2025 | 开放科研生态 | X5 | Y5 | Z1,Z2,Z3,Z4,Z6,Z7,Z8 | human-AI scientists 协作生态、structured knowledge system、collaborative protocol 与 ScienceArena/Elo evaluation |
| PANGAEA_GPT_2026 | 地球科学数据发现 | X4 | Y1 | Z1,Z4,Z5,Z7 | Supervisor-Worker 层级结构、data-type-aware routing 和 sandboxed code execution 支撑地球科学数据分析 |
| Code2Math_2026 | 数学产物演化 | X2 | Y4 | Z2,Z3,Z4,Z7,Z8 | Evolution Agent、Solvability Verification Agent 和 Difficulty Verification Agent 通过代码执行演化数学问题 artifact |
| PaperOrchestra_2026 | 论文写作/综合 | X2 | Y1 | Z1,Z6,Z7 | 多智能体将 pre-writing materials 转为 LaTeX manuscript，并通过文献综合和自动评价支持 reporting |
| MC_NEST_2025 | 假设搜索 | X0 | Y3 | Z2,Z8 | Monte Carlo / tree search over hypotheses |
| Medea_2026 | 文献/假设/验证 | X0 | Y2 | Z1,Z2,Z7 | 生物医学候选生成和筛选 |
| MOSAIC_Chemical_Synthesis_2026 | 实验/能力组合 | X0 | Y2 | Z1,Z3,Z7 | specialized chemical experts 与 protocol generation 支撑化学合成能力 substrate；不是显式 agent workflow，也不构成自主长程闭环 |
| MACC_2026 | 开放协作/竞争架构 | X5 | Y5 | Z2,Z3,Z6,Z7,Z8 | multi-agent collaborative competition，黑板式共享空间和制度化科学探索架构 |
| OpenAI_Unit_Distance_2026 | 假设/证明/验证 | X0 | Y2 | Z2,Z3,Z7 | AI 生成数学反例，依赖人类数学验证 |
| Paper2Code_2025 | 文献到代码 | X0 | Y1 | Z1,Z3,Z4,Z7 | 从论文到代码的 pipeline，支撑 executable artifact |
| PiFlow_2025 | 多智能体原则引导探索 | X2 | Y3 | Z1,Z2,Z3,Z5,Z7,Z8 | principle-aware multi-agent collaboration，将科学发现建模为 structured uncertainty reduction |
| ResearchAgent_2025 | 文献/假设/审查 | X2 | Y2 | Z1,Z2,Z6,Z7 | ReviewingAgents 对 problem、method、experiment design 进行反馈筛选 |
| SciNav_2026 | 科学代码搜索 | X0 | Y3 | Z3,Z4,Z5,Z8 | scientific coding solution 的 top-K search 与执行反馈 |
| SciToolAgent_2025 | 文献/工具/执行/验证 | X0 | Y5 | Z1,Z3,Z4,Z5,Z7 | 科学工具图谱、chain-of-tools planning 和失败后重规划 |
| SPARK_Cancer_Pathology_2026 | 假设/编码/分析/验证 | X0 | Y2 | Z2,Z3,Z4,Z5,Z7 | 病理场景中的概念、参数、编码和验证链条 |
| STELLA_2025 | 工具/harness 演化 | X0 | Y5 | Z3,Z4,Z5,Z8 | Dynamic Tool Ocean、Tool Creation Agent、template library |
| AgentReview_2024 | 审稿/评审 | X2 | Y1 | Z7 | reviewer、author、area-chair simulation，支撑多角色评审 |
| Reviewer2_2024 | 审稿/错误识别 | X0 | Y1 | Z7 | 审稿意见生成与错误识别 |
| ReviewerGPT_2023 | 审稿/反馈 | X0 | Y1 | Z7 | 自动审稿反馈，支撑 critic / reviewer 角色 |
| LLM_Verifier_2025 | 验证 | X3 | Y2 | Z7 | 多 verifier / round-robin selection 和验证机制 |
| OpenScholar_2025 | 文献/引用验证 | X0 | Y1 | Z1,Z6,Z7 | 文献支持、引用验证和 grounding |
| SafeScientist_2025 | 安全验证 | X0 | Y0 | Z3,Z4,Z7 | 科学任务安全边界、防御机制和风险评估 |
| SPOT_A_2025 | 失败检测/安全 | X0 | Y1 | Z7 | co-scientist failure detection，支撑输出检查 |
| MOOSE_Chem_2024 | 化学假设生成 | X2 | Y2 | Z1,Z2,Z7 | 多智能体 inspiration retrieval、hypothesis generation 与候选 ranking |
| MOOSE_Chem2_2025 | 细粒度化学假设 | X3 | Y3 | Z1,Z2,Z3,Z7 | hierarchical search 与 LLM ensemble / repeated instances，用于细粒度、可执行化学假设发现 |
| HypER_2025 | 文献假设/证据链 | X0 | Y1 | Z1,Z2,Z7 | provenance-grounded hypothesis generation，强调证据链和可追踪性 |
| Open_Domain_Hypotheses_2023 | 开放域假设生成 | X0 | Y1 | Z1,Z2,Z7 | 开放域科学假设生成，支撑 ASD 早期问题形成与 grounding |
| Curie_2025 | 自动实验/严谨性 | X2 | Y1 | Z2,Z3,Z4,Z5,Z7 | 多智能体实验系统强调 inter-agent / intra-agent rigor 与实验检查 |
| GenoMAS_2025 | 基因表达分析 | X2 | Y1 | Z1,Z3,Z4,Z5,Z7,Z8 | 六智能体代码驱动基因表达分析，覆盖执行、分析和迭代 |
| TAIS_2024 | 基因表达发现 | X2 | Y1 | Z1,Z3,Z4,Z5,Z7 | AI-made scientist team 支撑基因表达数据分析和发现 |
| DrugAgent_2024 | 药物发现编程 | X2 | Y0 | Z1,Z3,Z4,Z5,Z7 | Planner 与 Instructor 多智能体协作用于药物发现 ML 编程，但原文没有明确搜索/演化机制 |
| MLZero_2025 | ML 自动化 | X2 | Y5 | Z3,Z4,Z5,Z7,Z8 | 多智能体 AutoML，结合 semantic / episodic memory 支撑 harness evolution |
| MLR_Copilot_2024 | ML 研究自动化 | X2 | Y1 | Z1,Z2,Z3,Z4,Z5,Z7,Z8 | IdeaAgent 与 ExperimentAgent 支撑机器学习研究问题、实验和验证 |
| AIDE_2025 | 代码搜索 | X0 | Y3 | Z3,Z4,Z5,Z7,Z8 | code-space tree search，支撑代码产物生成、执行、评分和迭代 |
| KompeteAI_2025 | ML pipeline | X2 | Y3 | Z3,Z4,Z5,Z7 | 多智能体 ML pipeline 生成，核心包含 MCTS、候选合并、RAG 扩展和加速调试 |
| IMPROVE_2025 | pipeline refinement | X2 | Y1 | Z3,Z4,Z5,Z7,Z8 | 多智能体/迭代式模型 pipeline refinement，支撑执行后修订 |
| DS_Agent_2024 | 数据科学 | X0 | Y5 | Z3,Z4,Z5,Z7,Z8 | case-based reasoning 和 memory 支撑自动数据科学 workflow/harness 改进 |
| DrSR_2025 | 方程发现 | X0 | Y1 | Z3,Z4,Z5,Z7,Z8 | reflective equation discovery，支撑符号回归中的反思修正 |
| Nova_2024 | idea generation | X0 | Y3 | Z1,Z2,Z7,Z8 | iterative planning/search 用于科学 idea generation 和新颖性检查 |
| Scideator_2024 | human-LLM ideation | X0 | Y2 | Z1,Z2,Z7 | facet recombination 与 novelty checking，支撑人机科学创意生成 |
| Sparks_of_Science_2025 | structured hypothesis data | X0 | Y2 | Z1,Z2,Z7 | 结构化论文数据驱动 hypothesis generation 和 idea evaluation |
| Generative_Adversarial_Reviews_2024 | review agents | X2 | Y1 | Z7 | reviewer personas 与 meta-reviewer，支撑多智能体审稿和批评 |
| DeepReview_2025 | structured review | X0 | Y1 | Z7 | evidence-based paper review，支撑科学输出审查 |
| AstroAgents_2025 | astrobiology hypothesis | X2 | Y2 | Z1,Z2,Z5,Z7 | 八智能体质谱数据分析和天体生物学假设生成 |
| VirSci_2024 | virtual scientists | X2 | Y1 | Z1,Z2,Z7,Z8 | virtual scientists 多智能体系统，支撑科学想法生成和迭代 |
| GraphEval_Idea_2025 | idea evaluation | X0 | Y2 | Z2,Z7 | 图结构 idea evaluation，支撑候选科学想法筛选 |
| ToolUniverse_2025 | tool ecosystem | X0 | Y5 | Z1,Z3,Z4,Z5,Z7,Z8 | 大规模科学工具生态，支撑 AI scientist 的工具调用和能力扩展 |
| TxAgent_2025 | therapeutic tool-use reasoning | X0 | Y1 | Z1,Z3,Z4,Z5,Z7 | 面向治疗学的工具调用和推理 agent，支撑生物医学发现关键环节 |

| AGAPI_Agents_2025 | 材料 API/工具编排 | X4 | Y2 | Z1,Z2,Z3,Z4,Z5,Z7 | Agent-Planner-Executor-Summarizer 架构统一 20+ materials APIs，支持多步检索、预测、优化、衍射分析和逆向设计；长期迭代证据不足，故不标 Z8 |

| AgentRxiv_2025 | 开放科研协作/预印本 | X5 | Y5 | Z1,Z5,Z6,Z8 | agent laboratories 通过共享 preprint server 上传、检索和迭代彼此研究，体现开放科研产物网络；原文不强调 peer-review 式验证，故不标 Z7 |

| AutoResearchClaw_2026 | 自动研究/写作/验证 | X2 | Y5 | Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | structured multi-agent debate、自愈 executor、verifiable reporting 与 cross-run evolution 支撑从想法到论文的研究循环 |

| Claw_AI_Lab_2026 | 自动研究实验室/harness | X4 | Y5 | Z2,Z3,Z4,Z5,Z6,Z7,Z8 | hierarchical multi-agent research lab，五层研究流程、Claw-Code Harness、artifact inspection 与 rollback/resume 使研究 harness 可控可迭代 |

| eNRRCrew_2025 | 催化剂文献/分析/推荐 | X4 | Y2 | Z1,Z2,Z5,Z7,Z8 | orchestrator 动态分配 yield predictor、FE predictor、GraphRAG retriever、CSV handler / code execution agent，推荐 eNRR 电催化剂候选并分析 SAR |

| MADD_2025 | 药物发现/命中筛选 | X4 | Y2 | Z3,Z4,Z5,Z7 | Decomposer、Orchestrator、Summarizer 等代理构建并执行 hit-identification pipeline，支持生成、筛选和 docking/ML 评价 |

| MM_Agent_2025 | 数学建模/报告 | X2 | Y0 | Z2,Z3,Z4,Z5,Z6,Z7 | 多阶段数学建模 agent 将开放问题拆解为建模、计算求解、结果分析和报告生成；原文主要是阶段化工作流，未见显式反思/搜索/演化机制 |

| Mozi_2026 | 药物发现治理/harness | X4 | Y5 | Z2,Z3,Z4,Z5,Z7,Z8 | supervisor-worker control plane 与 stateful skill graphs 共同治理药物发现长流程，支撑反思式重规划、数据契约和 HITL 检查点 |

| SCP_2025 | 开放科学协议/能力网络 | X5 | Y5 | Z1,Z3,Z4,Z5,Z7,Z8 | Science Context Protocol 连接工具、模型、数据和物理仪器，Hub + federated servers 支撑跨机构 agent-driven science |

| DrugMCTS_2025 | 药物重定位/MCTS | X2 | Y3 | Z1,Z2,Z5,Z7,Z8 | 五个 specialized agents 结合 RAG 与 Monte Carlo Tree Search，支撑药物重定位中的结构化候选推理、选择和反馈搜索 |

| RD_Agent_2025 | 数据科学研发/代码执行 | X2 | Y4 | Z2,Z3,Z4,Z5,Z7,Z8 | Researcher 与 Developer 双代理通过并行 exploration traces、idea generation、代码实现和性能反馈合并推进数据驱动研发演化 |
| GeoEvolve_2025 | 地理空间模型发现 | X4 | Y4 | Z1,Z3,Z4,Z5,Z7,Z8 | outer agentic controller 评估 global elites 并查询 GeoKnowRAG，内层 code evolver 生成/变异候选，形成层级式演化搜索 |
| El_Agente_Q_2025 | 量子化学工作流 | X4 | Y1 | Z3,Z4,Z5,Z7,Z8 | hierarchical multi-agent cognitive architecture 支撑任务分解、工具选择、执行、post-analysis、文件提交和 in situ debugging |
| PhenoAssistant_2026 | 植物表型分析 | X4 | Y0 | Z3,Z4,Z5,Z7 | central manager / LLM orchestrates curated toolkit、vision model zoo、coding/data-visualization agents 和表型分析工具；原文未给出明确搜索/演化或自反思机制 |

| AccelMat_2025 | 材料假设/同类评审 | X3 | Y2 | Z2,Z3,Z7 | goal-driven hypothesis generator 产生材料候选假设，并由 GPT-4o、Claude、Gemini 等同类 critic ensemble 评价其 relevance、novelty 和 feasibility |
| BFS_Prover_V2_2025 | 形式化证明/tree search | X3 | Y3 | Z3,Z4,Z7,Z8 | planner-enhanced multi-agent tree search 将定理分解为子目标，由并行 prover agents 共享 proof cache 协作完成 Lean 证明 |
| LeanMarathon_2026 | 研究数学 autoformalization | X4 | Y3 | Z3,Z4,Z7,Z8 | two-stage orchestrator 协调 construct/audit/prove/repair agents，并按 proof DAG 叶节点并行推进 CI-gated proof search |
| Automatic_Textbook_Formalization_2026 | 大规模形式化/并行 agents | X3 | Y2 | Z3,Z4,Z7,Z8 | 30K Claude agents 并行协作 formalize 500+ 页代数组合教材，多个同类子代理在共享代码库中提交、审查和合并 Lean 产物 |
| MA_LoT_2025 | Lean 证明/多代理验证反馈 | X2 | Y1 | Z3,Z4,Z7 | prover / verifier 或 Lean-feedback 协作增强形式化定理证明；原文主要强调多代理 Long-CoT 与形式验证反馈，而非显式树搜索 |

## 3. 统计汇总

### 3.1 文献类型数量

| 类型 | 数量 |
|---|---:|
| 严格 ASD 系统 | 41 |
| ASD 相关系统 | 92 |
| 合计 | 133 |

### 3.2 X 轴分布

| X 坐标 | 数量 | 代表性文献 |
|---|---:|---|
| X0 | 57 | AFION_Plasmonic_SDL_2025, AI_Scientist_2024, AI_Scientist_Nature_2026, ALab_2023, AlphaEvolve_2025 |
| X2 | 43 | Agent_Laboratory_2024, EvoScientist_2026, Kosmos_2025, MAESTRO_2026, MOFGen_2025 |
| X3 | 6 | AlphaProof_Nexus_2026, LLM_Verifier_2025, MOOSE_Chem2_2025, AccelMat_2025, BFS_Prover_V2_2025 |
| X4 | 20 | CoScientist_2026, MARS_Materials_2026, MASTER_2025, Robin_2026, SAGA_2025 |
| X5 | 7 | Science_Earth_2026, AScience_ASCollab_2025, ScienceClaw_Infinite_2026, OmniScientist_2025, MACC_2026 |

说明：当前严格/相关 ASD 系统中，X0 数量仍然较多，说明不少系统仍是单 agent、单 pipeline 或 SDL/代码搜索系统；本文差异化主线应重点解释 X2-X5 中多智能体组织如何改变 ASD。

### 3.3 Y 轴分布

| Y 坐标 | 数量 | 代表性文献 |
|---|---:|---|
| Y0 | 5 | MatSciAgent_2026, SafeScientist_2025, DrugAgent_2024, MM_Agent_2025, PhenoAssistant_2026 |
| Y1 | 36 | Agent_Laboratory_2024, MAESTRO_2026, SparksMatter_2025, SR_Scientist_2026, DREAMS_2025 |
| Y2 | 29 | Coscientist_2023, MARS_Materials_2026, MASTER_2025, MOFGen_2025, Robin_2026 |
| Y3 | 21 | AFION_Plasmonic_SDL_2025, AI_Scientist_Nature_2026, ALab_2023, ERA_2026, PriM_2025 |
| Y4 | 16 | AI_Scientist_2024, AlphaEvolve_2025, AlphaProof_Nexus_2026, CoScientist_2026, SciDER_2026 |
| Y5 | 26 | EvoScientist_2026, Kosmos_2025, Science_Earth_2026, AScience_ASCollab_2025, SAGA_2025 |

说明：Y3-Y4 是科学研究产物搜索/演化的主证据区；Y5 支撑 harness / capability evolution 作为本文第二层机制。Y0 在显式多智能体搜索/演化分布中应被排除，只保留为组织形态边界样本。

### 3.4 Z 轴分布

Z 轴允许多标签，因此总数会超过文献总数。

| Z 坐标 | 数量 | 说明 |
|---|---:|---|
| Z1 | 68 | 知识 grounding / 文献综述 |
| Z2 | 67 | 问题形成 / 假设生成 |
| Z3 | 95 | 实验、仿真、代码或证明设计 |
| Z4 | 87 | 执行：代码、工具、实验、证明或机器人操作 |
| Z5 | 85 | 结果分析 / 错误诊断 |
| Z6 | 24 | 综合 / 报告 / 论文写作 |
| Z7 | 126 | 验证 / validation / review |
| Z8 | 79 | 迭代 / 长周期发现 |

说明：Z7 覆盖最多，说明当前 ASD 文献非常依赖验证、评审和人类/实验室检查点。Z3-Z4 也很强，说明执行型产物正在成为自主科学发现的重要载体。Z6 仍相对较少，说明论文写作和综合不是本文最应突出的主线。
