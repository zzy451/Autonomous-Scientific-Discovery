# AgentRxiv 2025

## 基本信息

- **论文**: AgentRxiv: Towards Collaborative Autonomous Research
- **年份**: 2025
- **来源**: arXiv:2503.18102
- **系统名称**: AgentRxiv
- **关键词**: collaborative autonomous research, preprint server, agent laboratories, cumulative knowledge

## 摘要要点

AgentRxiv 关注 autonomous research systems 的一个组织问题：已有 agent workflows 可以独立产出研究，但通常彼此隔离，不能持续吸收其他 agent labs 的结果。论文提出一个面向 LLM agent laboratories 的共享 preprint server，使多个 agent labs 能上传、检索、复用彼此报告，并在共同目标上迭代推进。

## 方法动机

科学发现很少来自单个 Eureka moment，而是许多研究者在共享成果基础上的累积推进。现有 autonomous research agents 多是封闭 pipeline，缺少跨运行、跨实验室的知识共享机制。AgentRxiv 的研究假设是：如果 agent labs 能像人类科研共同体一样发布和检索 preprints，它们可以比孤立 agents 更快改进策略和结果。

## 方法设计

系统流程包括：

1. 多个 agent laboratories 围绕共同研究目标独立运行。
2. 每个 lab 将研究报告上传到 shared preprint server。
3. 后续 agents 在新一轮研究前检索已有报告，吸收 prior research、prompting strategies 或 reasoning techniques。
4. agents 基于已有报告继续实验、修改策略并再次发布。
5. 通过多 lab 共享形成 cumulative research loop。

AgentRxiv 的核心贡献不是单篇报告生成，而是把 report 变成开放协作网络中的记忆节点。

## 实验与结果

论文在 reasoning/prompting technique development 场景中评估系统。作者报告，能访问 prior research 的 agents 相比孤立 agents 在 MATH-500 上有更高提升；多个 laboratories 共享 AgentRxiv 后，整体 accuracy 相对 baseline 有更大相对提升。最佳策略还能迁移到其他 benchmarks。

## 局限性

- 共享 preprint server 不等同于严格 peer review。
- 当前实验更偏 AI reasoning technique discovery，而非自然科学实验发现。
- 结果依赖报告质量、检索质量和 agent 是否能正确吸收 prior work。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X5` | 多个 agent labs 通过共享 preprint server 形成开放协作网络 |
| Y | `Y5` | 研究报告和策略经验在跨实验室网络中累积并影响后续研究 |
| Z | `Z1,Z5,Z6,Z8` | 覆盖检索既有研究、结果吸收、报告发布和长期迭代；不强标 `Z7` |

## 对综述的价值

AgentRxiv 非常适合支撑“scientific reporting 可以成为开放 agentic memory”的观点。它可用于第 4 章开放能力网络和第 5 章 harness/capability evolution，但不应写成已具备 peer-review validation 的严格 ASD 系统。

