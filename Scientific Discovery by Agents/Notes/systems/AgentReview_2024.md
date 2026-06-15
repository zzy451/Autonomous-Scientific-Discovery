# AgentReview 2024

## 基本信息

- **论文**: AgentReview: Exploring Peer Review Dynamics with LLM Agents
- **年份**: 2024
- **来源**: arXiv:2406.12708; EMNLP 2024
- **系统名称**: AgentReview
- **关键词**: peer review simulation, reviewer agents, author agents, area chair agents, review dynamics

## 摘要要点

AgentReview 将学术会议审稿过程建模为一个可控的多智能体仿真环境。系统模拟 reviewer、author 和 area chair 等角色，并允许研究者改变审稿人承诺度、知识水平、意图、匿名性、AC 决策方式等变量，从而观察不同制度设计如何影响评审结果。

这篇论文不是严格 ASD 系统，而是 ASD 的 verification / review substrate：它说明 scientific output 的可信闭环不能只靠生成，还需要 reviewer / author / chair 等角色之间的结构化交互。

## 方法动机

真实 peer review 同时包含论文质量、审稿人能力、审稿动机、作者回应、AC 汇总和会议机制等变量。传统数据分析很难隔离这些因素，因为真实审稿数据隐私敏感、变量不可控。AgentReview 的思路是用 LLM agents 构建可重复、可干预的仿真 testbed，用来研究评审机制本身。

## 方法设计

系统把一次审稿流程拆成多个阶段：

1. 输入论文、会议标准和评审机制设定。
2. 多个 reviewer agents 按给定 persona 和 latent traits 生成评审意见。
3. author agent 可根据审稿意见进行回应或 rebuttal。
4. area chair agent 汇总评审意见、作者回应和机制规则，给出接收/拒绝倾向。
5. 研究者通过改变单一变量进行对照，分析 reviewer commitment、reviewer intention、knowledgeability、AC style、author anonymity 等因素的影响。

这种设计的关键不在于产生一篇新论文，而在于把科学共同体中的 review labor 显式角色化、参数化和可实验化。

## 实验与结果

论文展示了 AgentReview 可以模拟 NLP/ML 会议中常见的审稿流程，并通过变量控制研究不同角色特征对最终决策的影响。它的价值主要是机制分析，而不是在某个 benchmark 上追求最高预测精度。

## 局限性

- LLM agent 的行为不能等同于真实审稿人。
- 仿真结果依赖 prompt、模型版本和角色设定。
- 它研究的是 review dynamics，不覆盖 hypothesis generation、execution 或 lab validation。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | reviewer、author、area chair 是固定异质角色 |
| Y | `Y1` | 核心机制是评审、回应、汇总和反馈修正 |
| Z | `Z7` | 直接支撑 scientific output 的 review / validation 阶段 |

## 对综述的价值

AgentReview 适合作为第 4 章 critique/review role decomposition 的证据，也适合第 7 章说明 ASD 需要把 peer review 式检查纳入可信闭环。它不应作为发现系统主证据，而应作为 verification substrate。

