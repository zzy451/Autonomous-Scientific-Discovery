# SciDER 2026

## 基本信息

- **论文**: SciDER: Scientific Data-centric End-to-end Researcher
- **年份**: 2026
- **来源**: arXiv:2603.01421
- **系统名称**: SciDER
- **关键词**: scientific data, end-to-end researcher, multi-agent, evolutionary idea search, data analysis, experimentation, critic

## 一句话总结

SciDER 是一个 data-centric end-to-end scientific researcher，使用多个 specialized sub-agents 覆盖 ideation、data analysis、experimentation 和 critic，并在 idea generation 阶段引入 Evolutionary Idea Search。

## 研究问题

许多科学 agent 系统停留在文献综述或假设生成，而没有把数据分析、实验执行和批评反馈串成完整工作流。SciDER 的问题意识是：能否让系统围绕科学数据完成从想法提出到实验分析再到批评修正的端到端过程。

## 系统架构

SciDER 包含多个 specialized sub-agents：

| 角色 | 作用 |
|---|---|
| Ideation agent | 生成研究想法，并通过 Evolutionary Idea Search 改进 |
| Data analysis agent | 处理和解释科学数据 |
| Experimentation agent | 设计并执行实验/计算尝试 |
| Critic agent | 评价结果、指出问题并触发修正 |

这个结构是典型 `X2: 固定角色多智能体`，但其 Y 轴重点不是普通反思，而是 idea/artifact evolution。

## 关键机制

### Evolutionary Idea Search

SciDER 的关键贡献是把 idea generation 视为可演化 artifact。想法不是一次性生成，而是在多角色反馈下被选择、修订和推进到实验环节。

### Data-centric workflow

与纯文献或纯写作系统不同，SciDER 把数据分析作为工作流中心，使候选想法必须接受数据和实验反馈。

## XYZ 分类

建议分类为：

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | ideation、data analysis、experimentation、critic 等固定角色 |
| Y | `Y4` | Evolutionary Idea Search 支撑 artifact evolution |
| Z | `Z2,Z3,Z4,Z5,Z7,Z8` | 覆盖想法生成、实验/代码设计、执行、分析、验证和迭代 |

建议作为 **严格 ASD 候选**：若深读确认其任务确实产生可验证科学结果，可列入严格 ASD；否则列为 ASD 相关系统。

## 对综述的价值

SciDER 能补 `X2-Y4-Z3/Z5` 等稀疏坐标，使固定角色多智能体中的 evolution 不只来自 Virtual Lab 和 EvoSci，而是扩展到 data-centric end-to-end discovery。

## 局限性

- 是否具有真实发现贡献，需要结合任务和实验结果判断。
- 如果主要是 benchmark 数据任务，则应避免夸大为全自动科学家。
- 报告/论文写作能力尚需深读确认，暂不标 `Z6`。

