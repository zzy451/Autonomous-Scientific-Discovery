# 第 4/5 章写作桥接备忘：从 XYZ 矩阵到正文论证

> 目的：把 `xyz_literature_classification_matrix.md` 与 `xyz_explicit_multi_agent_search_evolution_distribution.md` 中的 74 篇显式多智能体搜索/演化文献，转化为第 4 章 multi-agent organization 与第 5 章 evolution/search mechanisms 的正文写作抓手。
> 本备忘只服务于当前综述主线：multi-agent 是 ASD 的组织原则，evolution/search 是嵌入多智能体工作流中的优化机制。

## 1. 总体写作判断

去除 X0 和 Y0 后，显式多智能体且包含搜索/演化机制的文献共有 74 篇，其中严格 ASD 系统 26 篇，ASD 相关系统 48 篇。这个分布支持一个很清楚的写法：

1. 第 4 章应以 X 轴为骨架，解释科学劳动、科学能力、科学产物和验证边界如何被组织成多智能体工作流。
2. 第 5 章应以 Y 轴为骨架，但始终回扣第 4 章的组织形态，解释搜索/演化如何改进 artifact 或 harness。
3. Z 轴不应单独变成应用领域清单，而应作为每个系统覆盖的 scientific discovery phase，用来说明角色、产物和验证边界落在流程的哪一段。
4. X2 是当前证据最密集的区域，适合承担第 4 章主体；X3/X4/X5 数量较少，但概念价值高，适合承担“多”的扩展定义。
5. X0 系统不能作为第 4 章主证据，但可以在第 5/6/7 章作为 artifact search、execution substrate 和 verification boundary 的机制支撑。

一句话主张：

> Multi-agent ASD is not merely a larger number of agents, but a workflow-level organization of roles, parallel instances, hierarchy, capabilities, evidence standards, and open scientific capability networks.

## 2. 第 4 章：Multi-Agent Organization 的正文骨架

第 4 章建议按“多”的组织形式展开，而不是按学科领域展开。

| 小节 | 核心问题 | 主证据 | 写作重点 |
|---|---|---|---|
| 4.1 Role decomposition | 科学劳动为什么需要拆成不同角色？ | Agent_Laboratory_2024, Virtual_Lab_2025, Robin_2026, ResearchAgent_2025, SparksMatter_2025 | planner、literature、hypothesis、critic、executor、analyst、reviewer、PI 等角色如何形成可交接链条 |
| 4.2 Coordination and handoff | 多角色如何交换中间产物？ | Kosmos_2025, Robin_2026, MARS_Materials_2026, MOFGen_2025, Agent_Laboratory_2024 | artifact handoff、shared state、project memory、evidence-linked reports |
| 4.3 Critique, review, and conflict | 为什么 critic/reviewer 不是装饰性角色？ | AgentReview_2024, Generative_Adversarial_Reviews_2024, LLM_Verifier_2025, ResearchAgent_2025, SparksMatter_2025 | 批评、复核、分歧暴露和 round-robin verification 如何降低无证据输出 |
| 4.4 Parallel instances | 同角色多实例带来什么？ | AlphaProof_Nexus_2026, MOOSE_Chem2_2025, LLM_Verifier_2025 | 多 prover、多 verifier、多候选假设不是“多角色”，而是 search breadth 和 independent checking |
| 4.5 Hierarchical management | 为什么需要 supervisor/manager？ | CoScientist_2026, MARS_Materials_2026, MASTER_2025, MatSciAgent_2026 | 层级调度把复杂科研任务拆成可执行子任务，并连接工具、仿真和实验 |
| 4.6 Open capability networks | 多智能体如何超出固定团队？ | Science_Earth_2026, MACC_2026, MOSAIC_Chemical_Synthesis_2026 | capability discovery、task bidding、reputation/trust、cross-regime adjudication |
| 4.7 Human and lab checkpoints | 人类和实验室为何仍在闭环内？ | Robin_2026, MARS_Materials_2026, Curie_2025, CRISPR_GPT_2026, OpenAI_Unit_Distance_2026 | human/lab checkpoint 是科学责任与真实世界验证边界，不是自动化不足的临时补丁 |

本章的关键转折：

> The relevant unit of analysis is not an isolated LLM agent, but a coordinated workflow in which agents produce, inspect, execute, revise, and promote scientific artifacts under different evidence standards.

## 3. 第 5 章：Evolution/Search 作为嵌入式机制

第 5 章不应写成“演化智能体综述”。它应写成多智能体工作流中的优化机制，并区分两个演化对象：scientific research artifacts 与 agentic harness。

| 小节 | 演化/搜索对象 | 主证据 | 写作重点 |
|---|---|---|---|
| 5.1 Candidate generation and selection | hypothesis, idea, experiment plan | CoScientist_2026, Robin_2026, MOOSE_Chem_2024, ResearchAgent_2025, PriM_2025 | 多候选生成、排序、专家/agent 评审如何把假设生成变成受约束搜索 |
| 5.2 Tree and trajectory search | hypothesis paths, code paths, notebook trajectories | AI_Scientist_Nature_2026, MOOSE_Chem2_2025, PiFlow_2025, KompeteAI_2025 | search tree / trajectory 不只是生成更多结果，而是保存可回溯的决策路径 |
| 5.3 Evolutionary artifact optimization | code, proof, idea, paper draft | Virtual_Lab_2025, AlphaProof_Nexus_2026, EvoSci_2026 | mutation、selection、population、rating agents 和 archive 如何改进科学产物 |
| 5.4 Harness and capability evolution | workflow, memory, skill, capability network | Science_Earth_2026, Kosmos_2025, EvoScientist_2026, SciAgents_2024, Instrument_Agents_2026 | workflow、memory、skill、tool chain、capability registry 和 trust/reputation 的更新 |
| 5.5 Boundary cases outside this slice | multi-agent organization without explicit evolution | DrugAgent_2024, MatSciAgent_2026, MM_Agent_2025, PhenoAssistant_2026 | 这些 Y0 案例不进入去除 X0/Y0 后的交叉分布，但可在正文边界讨论中说明多智能体组织与搜索/演化不是同义词 |

第 5 章建议反复使用的对比：

| 对比 | 作用 |
|---|---|
| CoScientist_2026 vs Robin_2026 | 一个突出 hypothesis tournament/evolution，一个突出 lab-in-the-loop 候选、实验和再提案 |
| AlphaProof_Nexus_2026 vs MOOSE_Chem2_2025 | 一个在形式证明中使用多 prover/rating 和 population，一个在化学假设中使用 ensemble/repeated instances 与 hierarchical search |
| Science_Earth_2026 vs Kosmos_2025 | 一个代表开放能力网络和 reputation-weighted trust，一个代表长周期 world model、memory 和 evidence-linked reporting |
| Virtual_Lab_2025 vs Agent_Laboratory_2024 | 一个更适合讲 mutation-selection pipeline，一个更适合讲固定科研角色与端到端工作流 |
| DrugAgent_2024/MatSciAgent_2026/MM_Agent_2025/PhenoAssistant_2026 vs CoScientist_2026/MARS_Materials_2026 | 前者说明“有多智能体但未必有搜索”，后者说明层级多智能体如何与候选筛选或演化闭环结合 |

## 4. 可直接进入正文的论证段落草稿

第 4 章开头可以这样写：

> In autonomous scientific discovery, multi-agent organization is not simply a strategy for scaling up LLM calls. It is a workflow-level response to the heterogeneity of scientific labor. Literature grounding, hypothesis formation, experimental design, execution, analysis, verification, and reporting obey different epistemic norms and often require different tools, memories, and accountability boundaries. Explicit multi-agent systems therefore decompose scientific work into specialized roles, parallel candidate generators or reviewers, hierarchical supervisors, and in the most open case, capability networks that can discover, recruit, and evaluate scientific capabilities.

第 5 章开头可以这样写：

> Search and evolution enter this picture as mechanisms inside multi-agent scientific workflows rather than as a separate theme. The evolving object may be a scientific research artifact, such as a hypothesis, proof sketch, executable code, notebook trajectory, experiment plan, or manuscript draft. It may also be the agentic harness that generates and validates those artifacts, including role assignment, tool chains, memory, scoring functions, verifiers, promotion gates, and capability registries. This distinction prevents evolutionary ASD from collapsing into either generic optimization or vague claims about self-improving agents.

## 5. 写作时应避免的偏移

- 不要把材料、化学、生物、数学、代码系统按应用领域平铺；这些领域应作为执行载体和验证边界的例子。
- 不要把 X0 系统写成第 4 章主证据；它们适合支撑第 5 章的 artifact search 和第 6/7 章的 execution/verification。
- 不要把 Y5 泛化为所有 self-improvement；只有 workflow、skill、memory、agent capability 或 open capability network 本身发生更新时，才用 harness/capability evolution。
- 不要让 review/reporting 系统主导全文；Z6 数量少，且不是本文最强证据。
- 不要把 human-in-the-loop 写成“未完全自动化”的缺陷；在 ASD 中它也是验证边界、责任归因和科学治理的一部分。

