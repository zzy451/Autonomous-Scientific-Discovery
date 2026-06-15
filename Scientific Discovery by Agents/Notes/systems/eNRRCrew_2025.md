# eNRRCrew 2025

## 基本信息

- **论文**: eNRRCrew: A Multi-Agent System for Electrocatalyst Recommendation in Electrochemical Nitrogen Reduction
- **年份**: 2025
- **来源**: National Science Review, DOI: 10.1093/nsr/nwaf372
- **系统名称**: eNRRCrew
- **关键词**: electrocatalyst recommendation, eNRR, orchestrator, GraphRAG, yield predictor, FE predictor

## 摘要要点

eNRRCrew 面向 electrochemical nitrogen reduction reaction (eNRR) 催化剂推荐。系统由 orchestrator 动态分配 yield predictor、faradaic efficiency predictor、GraphRAG retriever、CSV handler / code execution agent 等专门 agents，用于检索文献、分析 structure-activity relationships 并推荐候选 electrocatalysts。

## 方法动机

eNRR 催化剂发现需要从文献和实验数据中提取复杂结构-性能关系。单个 LLM 难以同时完成文献 grounding、数据处理、性能预测和候选推荐。eNRRCrew 的思路是用 orchestrator 调度多个预测和检索 agents，将催化剂推荐变成可分解的 agent workflow。

## 方法设计

流程包括：

1. 用户提出 eNRR 催化剂查询或优化目标。
2. Orchestrator 解析任务并选择需要的 specialist agents。
3. GraphRAG retriever 检索相关文献、材料和反应信息。
4. Yield predictor 和 FE predictor 评估候选催化剂性能。
5. CSV / code agent 处理结构化数据和计算分析。
6. 系统汇总 SAR 分析、性能预测和推荐理由。

这里的 `X4` 来自 orchestrator 的动态分配；`Y2` 来自候选推荐和性能比较。

## 实验与结果

论文展示系统可从文献和数据中分析 eNRR 催化剂，并推荐潜在候选。它强调 multi-agent + GraphRAG + predictive agents 对材料/催化文献分析的作用。

## 局限性

- 执行层主要是数据和模型分析，不应强标 `Z3/Z4`。
- 推荐结果仍需实验验证。
- 预测器的训练数据和 domain coverage 会影响推荐可靠性。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | orchestrator 动态分配多个预测、检索和代码 agents |
| Y | `Y2` | 推荐候选催化剂并预测/比较性能 |
| Z | `Z1,Z2,Z5,Z7,Z8` | 覆盖文献数据库、候选推荐、结果分析、证据验证和可扩展迭代 |

## 对综述的价值

eNRRCrew 补强材料/催化方向的 `X4-Y2`，说明层级式多智能体可用于科学文献数据挖掘和候选推荐，而不一定需要进入机器人实验。

