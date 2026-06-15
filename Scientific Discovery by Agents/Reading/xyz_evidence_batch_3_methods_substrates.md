# XYZ evidence batch 3: methods/substrates

说明：本表优先使用一手来源（arXiv、Nature、ACL Anthology）。每篇至少给出 1 条支撑 X/Y 的方法或对象证据，1 条支撑 Z/系统覆盖的证据；英文原文只保留短句或短语，其余用中文解释。

| 文献 | 坐标 | 原文位置 | 原文短句/短语 | 支撑的坐标 | 解释 | 来源 |
|---|---|---|---|---|---|---|
| EvoSci_2026 | X2-Y4-Z1,Z2,Z7,Z8 | Sec. 3.2 Task Decomposition and Team Collaboration | `collaborative research process` | X2-Y4 | 原文说明 Prime Researcher 将探索分解为背景调查、问题分析、idea generation 与迭代 refinement 等任务，并用 CrewAI 组织团队，支撑“多智能体协作的研究想法/发现流程”。 | [arXiv HTML](https://arxiv.org/html/2605.24018v1) |
| EvoSci_2026 | X2-Y4-Z1,Z2,Z7,Z8 | Sec. 3.3-4.1 Research Idea Evaluation | `reviewer agent` | Z1,Z2,Z7,Z8 | 系统含研究任务分解、种子想法生成、进化迭代、评审/元评审和 tournament 排名；这些模块覆盖生成、迭代优化、评价与系统化记录。 | [arXiv HTML](https://arxiv.org/html/2605.24018v1) |
| Instrument_Agents_2026 | X2-Y5-Z1,Z3,Z4,Z5,Z7,Z8 | Nature abstract / opening summary | `operates complex scientific instrumentation` | X2-Y5 | 论文直接说开发并 benchmark 一个 multi-agent framework 操作两类真实科学设施，支撑“多智能体 + 物理科学仪器/实验设施”坐标。 | [Nature](https://www.nature.com/articles/s41524-026-02005-0) |
| Instrument_Agents_2026 | X2-Y5-Z1,Z3,Z4,Z5,Z7,Z8 | Nature lines 91-93, 172 | `learn on the job` | Z1,Z3,Z4,Z5,Z7,Z8 | 系统能编排多步实验、解释多模态数据、协作人类研究者，并通过专家指导/交互记忆学习；覆盖工具/仪器执行、数据解释、人机协作、评价可靠性。 | [Nature](https://www.nature.com/articles/s41524-026-02005-0) |
| MAGenIdeas_2026 | X2-Y2-Z1,Z2,Z7,Z8 | arXiv abstract | `generate, evaluate, and refine research ideas` | X2-Y2 | 摘要称其将组合创新理论、迭代知识搜索与 LLM 多智能体系统结合，用于研究想法生成；当前证据强支撑多候选生成、评价和 refinement，但不足以归为树/轨迹搜索。 | [arXiv abstract](https://arxiv.org/abs/2604.20548) |
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
| MOSAIC_Chemical_Synthesis_2026 | X0-Y2-Z1,Z3,Z7 | Nature abstract | `specialized chemical experts` | X0-Y2 | Nature 摘要称 MOSAIC 训练 2,498 个化学专家模型并利用数百万反应协议；这更像专家化合成能力 substrate / protocol prediction，而不是显式 agent workflow。 | [Nature](https://www.nature.com/articles/s41586-026-10131-4) |
| MOSAIC_Chemical_Synthesis_2026 | X0-Y2-Z1,Z3,Z7 | Nature abstract | `reproducible and executable experimental protocols` | Z1,Z3,Z7 | 系统基于反应协议知识输出可执行实验 protocol、confidence metrics，并有 71% 成功率和 35+ 新化合物实验验证；但不宜写成自主长程闭环执行。 | [Nature](https://www.nature.com/articles/s41586-026-10131-4) |
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

## 证据薄弱或需复核

| 文献 | 问题 | 当前处理 |
|---|---|---|
| MAGenIdeas_2026 | 浏览器未取得 arXiv HTML/PDF 正文，只取得 arXiv 摘要页；摘要信息足以支撑分类，但系统细节证据偏摘要级。 | 使用 arXiv 摘要和其公开代码/数据/demo 声明。 |
| PaperOrchestra_2026 | arXiv HTML 未能打开，主要一手证据来自 arXiv 摘要；ResearchGate 有 PDF 文本镜像但非首选一手。 | 使用 arXiv 摘要；未采用二手新闻/社媒。 |
| LLM_Verifier_2025 | 给定短名“LLM_Verifier_2025”与一手题名不完全一致；本地系统笔记与分类最匹配来源为 OpenReview 论文 *Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers*。 | 按 MAV / multiple verifiers 的 verification substrate 记录为 `X3-Y2-Z7`；不要混用 *The Need for Verification in AI-Driven Scientific Discovery* 的综述证据。 |
| OR_Agent_2026 | 检索到 OR-Agent 与 EvoOR-Agent 两篇相近 OR/agent 论文；给定短名更匹配 OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery。 | 使用 arXiv:2602.13769 的 OR-Agent；未混用 EvoOR-Agent 证据。 |
| ResearchAgent_2025 | 初版 arXiv 为 2024，但 ACL Anthology 正式会议版本为 NAACL 2025。 | 使用 ACL Anthology 2025 PDF 作为正式一手来源。 |
