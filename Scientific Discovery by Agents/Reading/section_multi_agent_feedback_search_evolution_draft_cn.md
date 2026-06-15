# 多智能体组织与反馈、搜索、演化机制

> 中文综述正文草稿。口径基于 `xyz_explicit_multi_agent_search_evolution_distribution.md` 中去除 `X0` 与 `Y0` 后的 72 篇显式多智能体、且包含反馈/搜索/演化机制的文献。

## 1. 从单一 AI scientist 到多智能体科学工作流

自主科学发现并不是简单地让一个大模型完成更多步骤，而是逐渐表现为一种多智能体工作流系统。科学发现包含文献 grounding、问题形成、假设生成、实验或仿真设计、代码或证明执行、结果分析、报告综合、验证评审和长期迭代等多个阶段；这些阶段遵循不同的证据标准，依赖不同的工具和执行环境，也对应不同的责任边界。因此，单一 agent 很难同时承担生成者、执行者、批评者、验证者和项目管理者的全部角色。72 篇显式多智能体且包含反馈/搜索/演化机制的论文显示，当前 ASD 系统的核心变化并不只是“agent 数量增加”，而是科学劳动、科学能力、科学产物和验证边界被重新组织成可分工、可交接、可复核、可搜索和可演化的工作流。

在这些系统中，多智能体首先体现为固定角色分工。`Agent_Laboratory_2024` 将科研过程组织为文献综述、实验和报告写作等阶段，并引入类似 PhD、Postdoc、Engineer、Reviewer 的角色；`Virtual_Lab_2025` 使用 PI 和 specialist agents 组织纳米抗体设计；`MARS_Materials_2026` 通过 19 个 LLM agents 和 16 个领域工具支撑材料发现闭环；`Robin_2026` 将 literature search、data analysis、候选提出和 lab-in-the-loop 连接起来。这类系统对应 `X2` 或 `X4`：前者强调多个固定角色之间的互补协作，后者强调 supervisor、planner 或 orchestrator 对多个 worker/specialist agents 的层级调度。

第二种“多”是同角色多实例或并行候选。形式化证明、假设生成和验证任务中尤其需要这种组织方式，因为科学搜索空间通常巨大，单一路径容易陷入局部错误。`AlphaProof_Nexus_2026`、`BFS_Prover_V2_2025` 和 `Automatic_Textbook_Formalization_2026` 使用多个 prover、proof workers 或并行 agents 在共享证明环境中探索和提交候选；`LLM_Verifier_2025` 使用多个 verifier models 对候选输出进行并行验证；`AccelMat_2025` 使用多个 critic LLM 对材料假设进行评审。这类 `X3` 系统的价值不在于角色更多，而在于用多实例提高搜索宽度、降低单点判断风险，并形成相对独立的候选比较或验证信号。

第三种“多”是层级式组织。复杂科研任务往往不能简单串联若干角色，而需要上层 agent 进行任务分解、资源调度、错误恢复和证据汇总。`CoScientist_2026` 通过 supervisor/task framework 组织假设生成、辩论、排序和演化；`MARS_Materials_2026`、`MASTER_2025` 和 `Robin_2026` 将材料或药物发现任务拆解为候选提出、计算/实验执行、结果分析与反馈；`DREAMS_2025`、`El_Agente_Q_2025`、`PANGAEA_GPT_2026` 和 `LeanMarathon_2026` 则分别在材料仿真、量子化学、地球科学数据分析和 Lean 形式化证明中体现 central planner、supervisor-worker 或 two-stage orchestrator 的作用。层级结构的核心功能是把开放科学问题转化为可执行子任务，并将局部结果重新聚合为下一步决策。

第四种“多”进一步超出封闭团队，表现为开放能力网络。`Science_Earth_2026` 将科学发现建模为 planet-scale scientific runtime，其中 EACN 支持 capability discovery、competitive bidding、task ownership negotiation、cross-regime adjudication 和 reputation-weighted trust；`ScienceClaw_Infinite_2026` 通过 skill registry、artifact DAG 和 global index 组织分布式科学协作；`SCP_2025` 将工具、模型、数据和物理仪器接入科学上下文协议；`AgentRxiv_2025` 用 shared preprint server 连接多个 agent laboratories；`MACC_2026` 和 `OmniScientist_2025` 则从共享黑板、协作竞争和 human-AI scientist ecosystem 角度讨论开放协作结构。这里的多智能体不再只是一个固定 team，而是开放的 scientific capability network：能力可以被发现、组合、评价和复用，科学任务可以在不同能力节点之间流动。

## 2. 多智能体反馈：从自我修正到证据闭环

多智能体 ASD 的第一类改进机制是反馈与自我修正。`Y1` 系统通常不显式构建搜索树或演化种群，而是在生成结果后通过 critique、reflection、debug、failure detection、rerun 或 reviewer feedback 改进产物。`Agent_Laboratory_2024`、`MAESTRO_2026`、`SparksMatter_2025`、`MLR_Copilot_2024`、`GenoMAS_2025` 和 `TAIS_2024` 都将固定角色协作与反馈修正结合起来：一个 agent 生成研究方案、代码、分析或报告，另一个 agent 或同一工作流中的 reviewer/critic 根据错误、结果或评价信号推动修订。

这类反馈机制的重要性在于，它把科学发现从一次性回答转化为可检查的产物循环。以代码和数据分析系统为例，`IMPROVE_2025` 通过逐组件 refinement 改进 ML pipeline，`MA_LoT_2025` 将 prover、Lean verifier 和 corrector 连接为证明生成-验证-修正循环，`CRISPR_GPT_2026` 使用 planner、executor、tool provider 和 user proxy 支持实验设计、执行、数据分析与 troubleshooting。这里的 feedback 不只是语言层面的“反思”，而是来自编译器、形式验证器、实验约束、工具执行结果、专家评分或人类检查点的外部信号。

多智能体反馈还使 critic/reviewer 不再是装饰性角色。`AgentReview_2024` 和 `Generative_Adversarial_Reviews_2024` 将同行评审过程本身模拟为多角色系统；`PaperOrchestra_2026` 将未结构化研究材料转化为论文手稿，并通过评价 agents 支撑写作质量检查；`ResearchAgent_2025` 使用 reviewing agents 对 problem、method 和 experiment design 进行反馈。虽然这些系统不一定构成完整科学发现闭环，但它们揭示了 ASD 的一个关键边界：科学产物必须经过评审、验证或复核，才能从“看起来合理的 agent output”变成可纳入证据链的 scientific artifact。

## 3. 候选生成与筛选：把假设生成变成受约束搜索

第二类机制是候选生成与筛选，对应 `Y2`。在这类系统中，多智能体不是只生成一个答案，而是产生多个假设、材料、分子、实验方案、论文 idea 或证明候选，再通过 ranking、scoring、review、comparison 或 selection 选择较优候选。`MOFGen_2025` 结合 LLM、扩散结构生成、量子力学筛选和 synthetic-feasibility agents 生成并过滤 MOF 候选；`MOOSE_Chem_2024` 通过 inspiration retrieval、hypothesis generation 和 ranking 组织化学假设发现；`MAGenIdeas_2026` 将 research idea generation 组织为多智能体生成、评价和 refinement；`AI_Researcher_HKU_2025` 和 `ResearchAgent_2025` 则将文献驱动的问题形成、方法设计和评审反馈连接起来。

材料和药物发现是候选生成与筛选最密集的证据区。`AtomAgents_2025`、`Materealize_2026`、`AGAPI_Agents_2025`、`MADD_2025`、`MARS_Materials_2026`、`MASTER_2025` 和 `Robin_2026` 都将候选提出与工具调用、仿真、属性预测、筛选或实验检查结合起来。它们说明，多智能体系统中的假设生成不应被理解为自由文本创意生成，而是一个受约束的候选空间探索过程：候选必须经过物理知识、合成可行性、性能指标、工具输出、专家标准或实验反馈过滤。

这种机制也改变了科学问题形成的性质。传统 LLM-based ideation 往往强调 novelty 或 plausibility，而多智能体候选筛选系统进一步要求候选能够被执行、比较和验证。例如 `AstroAgents_2025` 使用多个角色围绕质谱数据和文献生成生命起源假设，并通过 novelty/plausibility 评价；`AccelMat_2025` 通过多个 critic LLM 从 relevance、novelty、feasibility 和 testability 等维度评估材料假设。由此，科学假设不再只是一个语义上新颖的句子，而是进入后续实验、仿真、证明或评审流程的可操作对象。

## 4. 树搜索、轨迹搜索与多步路径探索

第三类机制是树搜索、MCTS 或 trajectory search，对应 `Y3`。与 `Y2` 的候选列表不同，`Y3` 系统显式保留搜索路径、状态转移或分支结构，使系统能够在多步探索中回溯、扩展和比较不同研究路线。`PriM_2025` 将 principle-inspired multi-agent collaboration 与 MCTS/structured search 结合，用于材料发现中的假设生成、实验验证和反馈更新；`DrugMCTS_2025` 将 RAG、多 agent 协作和 Monte Carlo Tree Search 用于药物重定位候选推理；`PiFlow_2025` 将科学发现表述为 principle-guided structured uncertainty reduction；`KompeteAI_2025` 在 AutoML pipeline 生成中结合 MCTS、候选合并和调试。

形式化证明是树搜索机制最清晰的执行载体之一。`BFS_Prover_V2_2025` 使用 planner 分解 theorem/subgoals，并由并行 prover agents 共享 proof cache 进行 multi-agent tree search；`LeanMarathon_2026` 通过 Blueprinter、Target-Reviewer、Worker 和 Refiner 沿 proof DAG 推进 autoformalization，并用 CI verifier 检查结果；`MOOSE_Chem2_2025` 将细粒度化学假设发现形式化为 hypothesis space 上的 hierarchical search。与普通候选筛选相比，树/轨迹搜索的优势在于它保存了“为什么走到这个结果”的路径信息，使失败节点、部分证明、实验分支或中间候选可以被复用、回退或解释。

这类系统也提示我们：搜索不等同于生成更多答案。科学搜索需要状态表示、扩展策略、评价函数和终止条件。多智能体结构为这些组件提供了自然分工：planner 负责拆解问题，generator 扩展候选，executor 运行代码/证明/仿真，critic 或 verifier 评价节点，manager 决定分支扩展或回退。由此，搜索树本身成为一种 scientific artifact，记录了系统如何在不确定空间中逐步逼近可验证结果。

## 5. 演化式优化：科学研究产物的种群、选择与归档

第四类机制是演化式优化，对应 `Y4`。这类系统通常显式使用 mutation、recombination、population、Elo、tournament、archive、elite selection 或 parallel traces 等机制，优化的对象主要是 scientific research artifacts：假设、idea、算法、代码、数学问题、证明候选、材料方案或实验计划。`CoScientist_2026` 通过生成、辩论、排序和演化组织 biomedical hypothesis tournament；`SciDER_2026` 使用 Evolutionary Idea Search 推进 data-centric discovery；`EvoSci_2026` 将科学 idea 生成、评审、锦标赛和迭代 refinement 组织为 bio-inspired multi-agent discovery framework；`RD_Agent_2025` 通过 Researcher/Developer 双 agent、多条 exploration traces、代码实现和性能反馈推进数据科学研发。

在数学与形式化场景中，`AlphaProof_Nexus_2026` 使用多个 prover/rating agents、population database 和 Lean-based verification 推动证明搜索；`Code2Math_2026` 使用 evolution 与 verification 阶段将已有数学问题演化为更复杂变体。材料和生物方向中，`Virtual_Lab_2025` 通过多轮 mutation、weighted score 和 top-candidate selection 优化 nanobody candidates；`OR_Agent_2026` 和 `GeoEvolve_2025` 则将算法发现或地理空间模型发现组织为层级式演化搜索。

演化机制的关键贡献是把科学研究产物从单个结果变成一个可管理的 population。每个候选都可以被执行、评分、比较、变异、淘汰或归档。多智能体系统在这里承担不同功能：generator 产生变体，critic/rater 评估质量，executor 运行代码或实验，archive 记录历史，manager 决定保留或扩展哪些分支。相比单轮 generate-and-rank，演化式工作流更适合开放空间中的长期探索，因为它能积累失败分支和中间结果，并通过选择压力逐渐提高候选质量。

## 6. Harness 与能力演化：从产物优化到工作流自更新

前四类机制主要作用于科学研究产物，而 `Y5` 指向另一类更深的演化对象：agentic harness。这里被更新的不只是 hypothesis、code、proof 或 experiment plan，而是生成、路由、执行、记忆、评分、验证和交接这些产物的系统脚手架。`EvoScientist_2026` 通过 Researcher、Engineer、Evolution Manager 和 persistent memory 改进 research strategies；`Kosmos_2025` 通过 structured world model 在 data-analysis agent 与 literature-search agent 之间共享状态，并生成 evidence-linked reports；`SciAgents_2024` 强调 multi-agent graph reasoning 与 in-situ learning；`Instrument_Agents_2026` 将 on-the-job learning 和 interaction memory 引入真实科学仪器操作。

层级式 harness evolution 还体现在 `TopoMAS_2025`、`Mimosa_2026`、`Mozi_2026`、`SAGA_2025` 和 `Claw_AI_Lab_2026` 等系统中。`TopoMAS_2025` 将拓扑材料检索、理论推理、结构生成和 first-principles validation 编排为材料发现 pipeline，并通过 self-evolving knowledge graph 更新系统知识；`Mimosa_2026` 自动合成 task-specific multi-agent workflows，并使用 judge feedback 与执行日志改进 workflow；`Mozi_2026` 用 supervisor-worker control plane 和 composable stateful skill graphs 治理药物发现流程；`SAGA_2025` 通过外层 goal-evolving agents 更新目标和 scoring functions，内层执行 solution optimization。这些系统说明，ASD 中的演化不应被狭义理解为候选产物变异，而应包括 workflow topology、memory、skill graph、tool chain、objective function 和 validation gates 的更新。

开放能力网络进一步扩展了 harness evolution 的范围。`Science_Earth_2026` 中的 EACN 将 capability discovery、task bidding、cross-regime adjudication 和 reputation-weighted trust 作为运行时协议；`ScienceClaw_Infinite_2026` 通过 300+ scientific skills、artifact DAG、persistent memory 和 global index 组织分布式发现；`SCP_2025` 通过 protocol/hub/servers 连接工具、模型、数据和物理仪器；`AgentRxiv_2025` 通过 shared preprint server 让多个 agent laboratories 上传、检索并基于彼此报告迭代。这里的演化对象已经从某个团队内部的工作流扩展为开放科学能力网络本身：能力如何注册、发现、评价、复用和获得信任，成为 ASD 是否能长期运行的关键。

## 7. 组织形态与演化机制的耦合

多智能体组织形态与反馈/搜索/演化机制并不是两个独立维度，而是相互耦合的系统设计选择。固定角色多智能体 `X2` 最常见，适合支撑反思修正、候选生成、树搜索和 harness memory 等多类机制；同角色多实例 `X3` 更适合并行证明、验证和候选评审；层级式多智能体 `X4` 适合复杂任务分解、工具执行和跨阶段调度；开放能力网络 `X5` 则适合讨论长期协作、能力发现、声誉更新、产物交换和跨证据标准裁决。

这种耦合关系解释了为什么 ASD 不能只按应用领域分类。材料发现、药物发现、数学证明、科学写作、地球科学数据分析和自动机器学习看似属于不同领域，但它们共享类似的系统问题：如何拆解任务，如何生成候选，如何让候选进入执行环境，如何获得反馈，如何比较与筛选，如何记录失败和中间状态，如何通过验证门槛把输出提升为可信科学产物。多智能体提供组织结构，反馈/搜索/演化提供改进动力，验证与人类检查点则提供科学边界。

因此，本节的核心结论是：自主科学发现中的 multi-agent 不是“多个 agent 聊天”，search/evolution 也不是泛化的自我改进口号。更准确地说，多智能体 ASD 是一种工作流级组织原则：它把异质角色、同类实例、层级调度和开放能力网络连接起来；反馈、搜索与演化则在这个组织结构中不断改进两类对象，一类是科学研究产物，另一类是产生、执行和验证这些产物的 agentic harness。只有当这两类改进都被验证、记录并置于人类或实验室检查点之下，agent 输出才可能成为可信的 autonomous scientific discovery 结果。

