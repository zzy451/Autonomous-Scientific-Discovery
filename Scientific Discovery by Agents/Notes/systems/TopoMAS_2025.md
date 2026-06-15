# TopoMAS 2025

## 基本信息

- **论文**: TopoMAS: A Hierarchical Multi-Agent System for Topological Materials Discovery
- **年份**: 2025
- **来源**: arXiv / materials discovery preprint
- **系统名称**: TopoMAS
- **关键词**: topological materials, hierarchical multi-agent, dynamic knowledge graph, DFT validation, memory evolution

## 摘要要点

TopoMAS 面向拓扑材料发现，将 hierarchical multi-agent framework 与动态知识图谱结合。系统覆盖拓扑材料检索、理论推理、结构生成、DFT validation 和知识图谱更新。当前分类将其标为 `Y5`，因为其关键证据不只是候选筛选，而是动态知识图谱/记忆会改变后续推理和检索环境。

## 方法动机

拓扑材料发现需要跨文献知识、理论约束、结构候选和第一性原理验证。单次候选生成容易忽视领域知识更新。TopoMAS 的动机是把材料知识组织成可更新图谱，并让多智能体在检索、生成、验证和记忆更新之间循环。

## 方法设计

流程包括：

1. literature / knowledge agents 检索并结构化拓扑材料知识。
2. reasoning agents 基于理论约束提出候选结构或材料家族。
3. simulation / validation agents 组织 DFT 或相关计算验证。
4. analysis agents 解释计算结果和拓扑性质。
5. dynamic knowledge graph 更新候选、证据和失败经验。
6. 后续检索和推理使用更新后的图谱。

这个闭环使 memory / knowledge graph 成为可演化 harness，而不是静态 RAG。

## 实验与结果

论文展示 TopoMAS 能组织材料检索、结构生成和 DFT validation，用于发现或评估拓扑材料候选。其结果强调多 agent 协作与动态知识组织对材料 discovery loop 的支撑。

## 局限性

- 真实实验验证仍需材料合成和表征。
- 动态知识图谱的质量取决于抽取、验证和更新策略。
- 目前更适合写作材料发现中的 memory/harness evolution，而非普适开放网络。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | hierarchical multi-agent architecture 和多层协作 |
| Y | `Y5` | dynamic knowledge graph / memory update 改变后续推理环境 |
| Z | `Z1,Z2,Z3,Z4,Z5,Z7,Z8` | 覆盖检索、假设/结构生成、DFT 设计执行、分析、验证和闭环更新 |

## 对综述的价值

TopoMAS 是 `X4-Y5` 的材料发现证据，适合说明 harness/capability evolution 不只存在于软件 agent，也可以表现为科学知识图谱和记忆结构的持续更新。

