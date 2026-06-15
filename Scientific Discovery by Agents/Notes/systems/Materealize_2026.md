# Materealize 2026

## 基本信息

- **论文**: Materealize: A Multi-Agent Framework for Inorganic Materials Discovery
- **年份**: 2026
- **来源**: arXiv / materials discovery preprint
- **系统名称**: Materealize
- **关键词**: inorganic materials, multi-agent deliberation, tool orchestration, synthesis route, mechanism hypothesis

## 摘要要点

Materealize 面向无机材料发现，使用多智能体 deliberation 与工具编排来生成候选材料、合成路线和机制解释。系统结合文献/知识检索、材料设计推理、工具调用和专家式讨论，目标是把材料发现从单次文本生成推进到可检查、可执行的候选设计流程。

## 方法动机

无机材料发现需要同时考虑组成、结构、性质、合成可行性和物理机制。单个 LLM 很容易给出泛泛建议，而材料专家通常需要多视角讨论。Materealize 的直觉是用多个领域视角/工具角色进行 deliberation，通过外部工具和物理约束筛选候选。

## 方法设计

流程包括：

1. 输入目标性质、材料类别或应用需求。
2. 文献/知识 agent 检索相关材料体系和设计规则。
3. 设计 agents 生成候选组成、结构或替代策略。
4. 合成/机制 agents 提出合成路线和可能物理机制。
5. 工具 agents 调用数据库、预测模型或计算工具进行初步筛选。
6. 多 agents 通过 deliberation 比较候选，输出推荐材料、证据和下一步实验/计算建议。

系统的核心是多角色讨论和候选筛选，而不是显式 MCTS 或遗传算法。

## 实验与结果

论文展示 Materealize 能在无机材料场景中提出候选、合成路线和机制解释，并通过工具或文献/物理证据支持判断。它补强材料发现中固定角色多智能体 + 候选筛选的证据。

## 局限性

- 不宜强标为论文/报告生成系统，因此当前不标 `Z6`。
- 真实材料发现仍需要高保真计算、合成和表征验证。
- deliberation 的质量依赖角色 prompt、工具准确性和证据 grounding。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | 固定领域视角/工具角色构成 deliberation team |
| Y | `Y2` | 生成候选材料、合成路线和机制解释，并通过工具/讨论筛选 |
| Z | `Z1,Z2,Z3,Z4,Z5,Z7,Z8` | 覆盖文献、候选设计、工具执行、诊断、验证和迭代 |

## 对综述的价值

Materealize 可用于说明材料发现是当前严格 ASD 系统的密集证据区，也能支撑“多智能体的多”包括多领域视角和多工具能力。

