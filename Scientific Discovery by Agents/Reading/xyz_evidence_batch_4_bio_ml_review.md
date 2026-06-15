# XYZ evidence batch 4: bio / ML review systems

核对原则：优先使用 arXiv、OpenReview、ACL Anthology、项目官方页等一手来源；“原文短句/短语”只保留最短定位短语，避免长段引用。坐标沿用任务给定分类。

| 文献 | 坐标 | 原文位置 | 原文短句/短语 | 支撑的坐标 | 解释 | 来源 |
|---|---|---|---|---|---|---|
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
| AGAPI_Agents_2025 | X4-Y2-Z1,Z2,Z3,Z4,Z5,Z7 | arXiv 摘要 | "twenty materials-science API endpoints" | Z1, Z2, Z3, Z4, Z5, Z7 | 平台统一数据库、仿真、ML 模型，覆盖检索、预测、优化、衍射分析、逆向设计，并与实验数据比较；长期记忆/失败复用证据不足，故不标 Z8。 | https://arxiv.org/abs/2512.11935 |
| AgentRxiv_2025 | X5-Y5-Z1,Z5,Z6,Z8 | arXiv 摘要 | "shared preprint server"; "agent laboratories" | X5, Y5 | AgentRxiv 让多个 LLM agent laboratories 通过共享 preprint server 上传/检索报告，构成开放科研产物网络和跨实验室记忆。 | https://arxiv.org/abs/2503.18102 |
| AgentRxiv_2025 | X5-Y5-Z1,Z5,Z6,Z8 | arXiv 摘要 | "iteratively build on each other's research" | Z1, Z5, Z6, Z8 | 系统以 prior reports 为知识来源，吸收已有结果、发布报告并迭代改进策略；原文不主张 peer-review 式验证，因此不支撑 Z7。 | https://arxiv.org/abs/2503.18102 |
| AutoResearchClaw_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | "structured multi-agent debate"; "cross-run evolution" | X2, Y5 | AutoResearchClaw 由多 agent debate、自愈 executor 和跨运行演化组成，核心是 research harness 的能力积累。 | https://arxiv.org/abs/2605.20025 |
| AutoResearchClaw_2026 | X2-Y5-Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8 | arXiv 摘要 | "self-healing executor"; "verifiable result reporting" | Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8 | 摘要覆盖假设生成、实验失败修复、结果分析、可验证报告、人机协作和跨运行经验沉淀，是本批 Z 覆盖最完整的系统之一。 | https://arxiv.org/abs/2605.20025 |

## 证据薄弱或需谨慎使用

| 文献 | 情况 |
|---|---|
| AGAPI_Agents_2025 | 已找到 arXiv 一手来源；但截至本次核对主要是 2025 年底预印本/平台论文，材料发现成效多来自 API 编排、示例 workflow 和与实验数据比较，不能写成已经完成湿实验闭环发现。 |
| AutoResearchClaw_2026 | 已找到 arXiv 一手来源；论文很新，证据以 ARC-Bench 和系统机制为主，适合作为 automated research harness / workflow evolution 证据，不宜作为单一自然科学发现的强实证。 |
| AgentRxiv_2025 | 一手来源充分；但其 Z 覆盖不包含严格 peer-review validation，主要是共享报告、检索、吸收结果和长期迭代。 |
| Generative_Adversarial_Reviews_2024 | 一手来源充分；但只支撑 review/critic/validation，不支撑完整科学发现闭环。 |
| MLZero_2025 / KompeteAI_2025 / IMPROVE_2025 | 一手来源充分；但它们主要是 AutoML / ML pipeline automation，对科学发现综述应作为计算型 harness 或 ML research automation 证据，而非生物/化学实验发现证据。 |

未发现完全无法定位一手来源的条目。
