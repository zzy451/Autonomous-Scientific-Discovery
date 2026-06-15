# XYZ evidence batch 1: core ASD papers

> 核对原则：优先使用 arXiv、期刊 DOI/论文页、OpenReview 等一手来源；英文原文只摘短句/短语，每篇合计控制在短句级，分类解释用中文转述。

| 文献 | 坐标 | 原文位置 | 原文短句/短语 | 支撑的坐标 | 解释 | 来源 |
|---|---|---|---|---|---|---|
| Agent_Laboratory_2024 | X2-Y1-Z1,Z2,Z3,Z4,Z5,Z6,Z7 | arXiv 摘要 | “autonomous LLM-based framework” | X2/Y1 | 论文把系统定义为自主 LLM agent 框架；结合论文中的 PhD/Postdoc/Engineer/Reviewer 等角色，可支撑固定角色多 agent 与反思/反馈式改进。 | https://arxiv.org/abs/2501.04227 |
| Agent_Laboratory_2024 | X2-Y1-Z1,Z2,Z3,Z4,Z5,Z6,Z7 | arXiv 摘要 | “literature review, experimentation, and report writing” | Z1/Z3/Z4/Z5/Z6/Z7 | 三阶段覆盖文献综述、实验执行和论文产出；摘要还说明生成 code repository 和 research report，可支撑系统覆盖科研流程。 | https://arxiv.org/abs/2501.04227 |
| AI_Scientist_Nature_2026 | X0-Y3-Z2,Z3,Z4,Z5,Z6,Z7,Z8 | Nature 摘要/Main | “complex agentic system” | X0/Y3 | Nature 版明确把 The AI Scientist 置于 agentic system 中，并用 agentic/tree search 扩展实验探索；但当前证据不足以证明显式多智能体组织，因此从显式多智能体分布中移出。 | https://www.nature.com/articles/s41586-026-10265-5 |
| AI_Scientist_Nature_2026 | X0-Y3-Z2,Z3,Z4,Z5,Z6,Z7,Z8 | Nature Main | “ideation, literature search, experiment planning and implementation, result analysis, manuscript writing, and peer review” | Z2/Z3/Z4/Z5/Z6/Z7/Z8 | 这句话直接列出从想法、实验计划/实现、结果分析、写作到同行评审的全流程覆盖，支持端到端 ASD baseline 坐标。 | https://www.nature.com/articles/s41586-026-10265-5 |
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

## 无法找到一手证据或证据薄弱

- 未发现完全无法定位一手来源的条目；15 篇均找到 arXiv、DOI、Nature/Matter/npj 页面或 OpenReview 之一。
- 证据相对薄弱、需在综述正文中谨慎措辞：Kosmos_2025、EvoScientist_2026、MAESTRO_2026、MOFGen_2025、PriM_2025、Science_Earth_2026、AScience_ASCollab_2025、SAGA_2025 主要依赖 arXiv/预印本或 workshop 版本，部分结论尚需同行评议或独立复现。
- AScience_ASCollab_2025 的 Z7 是“peer review/专家评价 + 明确承认 wet-lab validation remains indispensable”，不能写成已经完成湿实验验证。
- Robin_2026、CoScientist_2026 的生物医学结果属于早期体外/机制验证或 lab-in-the-loop，不应写成临床有效性或完全机器人闭环。
