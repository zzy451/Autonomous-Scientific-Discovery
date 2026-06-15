# Boiko et al. 2023 - Autonomous Chemical Research with Large Language Models

**论文信息**
- 标题：Autonomous chemical research with large language models
- 作者：Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes
- 年份：2023
- 来源 / venue：Nature
- DOI / URL：https://doi.org/10.1038/s41586-023-06792-0
- 当前状态：candidate；core priority；full-text evidence pending

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Nature article / Semantic Scholar TLDR | Coscientist performs autonomous experimental design and execution across chemical tasks | 高 |
| 科学对象归类 | `03` 化学科学 | Nature title | chemical research and reaction optimization | 高 |
| 验证方式 | 化学实验 / reaction optimization | Nature metadata / Semantic Scholar summary | includes palladium-catalysed cross-coupling optimization | 中 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- 判断依据：大语言模型系统 Coscientist 执行多步化学研究任务，包括实验设计与执行。
- Agent 行动闭环：规划、工具调用、实验设计、部分实验执行和结果反馈，需全文逐页确认。
- 纳入置信度：高。

## 2. 科学领域归类

- 一级类：`03` 化学科学
- 二级类：`03.03` 合成、反应与催化
- 四级专题：LLM-based autonomous chemical research
- 归类理由：最终科学对象是化学实验与反应优化，不归入计算机科学。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Planning Agent；Hybrid Agent。
- 科研流程角色：文献/网络查询、实验设计、工具调用、代码/仪器接口、结果解释。
- 自主能力：任务分解、计划生成、工具调用、反馈迭代、闭环实验。

## 4. 方法设计

初步 pipeline：

1. 接收化学研究目标。
2. LLM 系统规划任务并查询外部知识。
3. 调用化学工具和实验接口。
4. 设计或执行化学实验。
5. 分析结果并输出下一步建议或结论。

## 5. 实验与验证

- 验证方式：化学任务与实验验证。
- 科学贡献类型：system_platform；experimental_discovery / experimental_optimization。
- 证据强度：experimentally_validated，待全文细化。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 是本综述中 LLM-driven autonomous chemical research 的关键高刊案例。
- 可作为“Agent 从工具使用走向实验执行”的代表。

## 7. 后续精读任务

- 补充六类任务的具体内容。
- 补充 palladium-catalysed cross-coupling 结果。
- 记录系统架构、工具、人工介入点和失败模式。
