# Pandey et al. 2025 - OpenFOAMGPT: a RAG-augmented LLM agent for OpenFOAM-based computational fluid dynamics

**论文信息**
- 标题：OpenFOAMGPT: a RAG-augmented LLM agent for OpenFOAM-based computational fluid dynamics
- 作者：Pandey et al.
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2501.06327
- PDF / 本地文件路径：本轮基于 arXiv 摘要页；未保存本地 PDF
- 论文类型：系统论文 / CFD workflow agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 面向 OpenFOAM 的 RAG-augmented LLM agent，带迭代纠错回路 | 高 |
| 科学对象归类 | `09.01` | arXiv abstract | 对象是 CFD 建模与仿真工作流，而非通用科研平台 | 高 |
| 方法流程 | RAG + case setup + correction | arXiv abstract | 自动处理 case setup、模型调整与代码翻译 | 高 |
| 实验验证 | simulation / benchmark | arXiv abstract | 涵盖多类 CFD cases 和 turbulence-model tasks | 高 |
| 边界判断 | 不应归 `01.04` | arXiv abstract | 任务与知识源都深度绑定 CFD 工程对象 | 高 |

## 0. 摘要翻译

OpenFOAMGPT 把 LLM Agent 和 RAG 结合起来，面向 OpenFOAM 的 CFD 建模、修改和代码迁移任务。系统不仅检索知识，还能自动处理 case setup、边界条件修改、模型替换和迭代纠错。由于演示与评估始终绑定具体 CFD 工程问题，因此主类应稳定放在工程科学。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：明确科研目标、多步工具调用、迭代纠错与工程仿真角色
- 判定置信度：高
- 在科研流程中承担的明确角色：simulation_modeling；tool_use_and_code_execution
- 是否仍需进一步全文复核：需要，用于增强 core-strength 判断

## 2. 科学领域归类

- 一级类：09
- 二级类：09.01
- 三级类：CFD / engineering simulation workflows
- 四级专题：CFD workflow agents
- 最终科学研究对象：CFD 仿真建模与案例配置
- 最终科学问题：如何让 Agent 更自主地组织 OpenFOAM 仿真工作流
- 容易混淆的边界：`01.04`
- 最终判定：保留 `09.01`
- 判定理由：演示与评估都绑定具体 CFD 工程对象，而不是通用 scientific-agent platform

## 3. Agent 系统与科研流程角色

- Agent 类型标签：LLM Agent；Retrieval-augmented Agent；Tool-using Agent
- 科研流程角色：simulation_modeling；tool_use_and_code_execution
- 自主能力：planning；tool_use；feedback_iteration
- 交叉属性标签：computation_driven；simulation_driven

## 4. 方法设计

1. 接收 CFD 建模任务。
2. builder / RAG 模块检索已有设置与知识。
3. 生成或修改 OpenFOAM case。
4. 执行并根据错误进行迭代修正。
5. 输出更可用的仿真工作流结果。

## 5. 实验与验证

- 验证方式：benchmark；simulation_validation
- 数据、任务与指标：多种 CFD case、湍流模型调整与代码翻译任务
- 关键结果：支持多类 OpenFOAM 工作流自动化
- 科学贡献类型：system_platform；analysis
- 证据强度：high_primary_abstract

## 6. 与已有工作的关系

- 与一般 LLM coding assistant 不同，它深度绑定 OpenFOAM 工程环境。
- 与通用 scientific workflow platform 不同，这里对象是具体 CFD 工程仿真。
- 可与 FEM、mechanics、structural analysis agents 共同构成 `09.01` 仿真子群。

## 7. 局限性与风险

- 当前更多体现 workflow automation，而不是强发现性科学贡献。
- 风险主要是 core-strength，而不是主类风险。
- 后续可补更复杂工业场景的全文证据。

## 8. 对综述写作的价值

- 适合放入工程仿真 / CFD agents 小节。
- 可支持“RAG agent 开始嵌入复杂工程仿真生态”这一论点。
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

RAG-augmented Agent 被用于 OpenFOAM CFD 工作流。

### 9.2 速记版 pipeline

1. 输入 CFD 任务
2. 检索已有案例
3. 生成/修改仿真配置
4. 执行并纠错
5. 输出 CFD 结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：09
二级类：09.01
三级类：CFD / engineering simulation workflows
四级专题：CFD workflow agents
Agent 类型：LLM Agent; Retrieval-augmented Agent; Tool-using Agent
科研流程角色：simulation_modeling; tool_use_and_code_execution
自主能力：planning; tool_use; feedback_iteration
验证方式：benchmark; simulation_validation
交叉属性：computation_driven; simulation_driven
科学贡献类型：system_platform; analysis
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
