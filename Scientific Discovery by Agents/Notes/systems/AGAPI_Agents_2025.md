# AGAPI Agents 2025

## 基本信息

- **论文**: AGAPI Agents: Automated Materials Discovery through Agentic API Orchestration
- **年份**: 2025
- **来源**: arXiv / materials informatics preprint
- **系统名称**: AGAPI Agents
- **关键词**: materials APIs, agent planner, executor, summarizer, inverse design, diffraction analysis

## 摘要要点

AGAPI Agents 面向材料信息学和材料发现工具调用。系统采用 Agent-Planner-Executor-Summarizer 架构，统一 20+ materials APIs，支持多步检索、预测、优化、衍射分析和 inverse design。它的关键价值在于把分散材料 API 组织成层级式 agentic workflow。

## 方法动机

材料研究者经常需要同时访问结构数据库、性质预测模型、仿真工具和分析 API。普通 LLM 可以写调用代码，但难以保证多步工具链正确、可解释和可恢复。AGAPI Agents 的目标是让 agent 根据材料问题自动选择和编排 API。

## 方法设计

流程包括：

1. 用户提出材料检索、预测、优化或逆向设计需求。
2. Agent/Planner 解析任务并生成多步 API 调用计划。
3. Executor 调用材料数据库、预测模型、衍射分析或优化接口。
4. 系统根据中间结果调整后续 API 调用。
5. Summarizer 汇总结果、候选和证据。
6. 用户可检查候选、预测结果和工具链输出。

其层级性来自 Planner/Executor/Summarizer 的任务分解和工具调度。

## 实验与结果

论文展示系统可完成多种材料 API 任务，包括检索、性质预测、优化、XRD/结构分析和 inverse design。它补的是工具/执行编排能力，而不是单独新材料的湿实验发现。

## 局限性

- 依赖外部 API 的覆盖、稳定性和准确性。
- 多步 API 调用可能产生错误传播。
- 候选材料的真实合成和性能仍需实验或更高保真计算验证。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | Agent-Planner-Executor-Summarizer 架构体现层级调度 |
| Y | `Y2` | 多个候选、预测和优化结果经过比较筛选 |
| Z | `Z1,Z2,Z3,Z4,Z5,Z7` | 覆盖检索、候选设计、工具执行、分析和验证；长期记忆更新、失败分支复用或持续 discovery loop 证据不足，故不标 `Z8` |

## 对综述的价值

AGAPI Agents 可用于说明 multi-agent ASD 的 execution substrate 不只包括机器人实验，也包括工具/API 编排。它适合第 4 章 coordination protocol 和第 6 章 code/tool substrate。
