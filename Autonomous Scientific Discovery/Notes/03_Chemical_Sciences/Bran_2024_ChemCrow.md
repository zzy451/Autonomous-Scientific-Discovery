# Bran et al. 2024 - Augmenting Large Language Models with Chemistry Tools

**论文信息**
- 标题：Augmenting large language models with chemistry tools
- 作者：Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, Philippe Schwaller
- 年份：2024
- 来源 / venue：Nature Machine Intelligence
- DOI / URL：https://doi.org/10.1038/s42256-024-00832-8
- 当前状态：candidate；core priority；full-text evidence pending

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，工具增强化学 Agent | Nature Machine Intelligence metadata / seed survey ref 24 | LLM augmented with chemistry tools; known as ChemCrow | 高 |
| 科学对象归类 | `03` 化学科学 | title and venue | chemistry tools and chemistry problem solving | 高 |
| 方法机制 | tool-using LLM | title | augmenting LLMs with chemistry tools | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- Agent 行动闭环：工具调用、问题求解、多步化学任务；是否有反馈迭代需全文确认。
- 纳入置信度：高。

## 2. 科学领域归类

- 一级类：`03` 化学科学
- 二级类：`03.04` 分子设计与化学空间探索 / `03.01` 化学信息学
- 四级专题：tool-using chemistry agent
- 归类理由：主对象是化学任务和化学工具链，不按 LLM 工具使用归入 `01`。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Retrieval-augmented Agent。
- 科研流程角色：工具调用、数据查询、结果解释、化学问题求解。
- 自主能力：工具调用、多步行动，反馈迭代待确认。

## 4. 方法设计

初步 pipeline：

1. 用户提出化学问题。
2. LLM Agent 分析任务并选择化学工具。
3. 调用数据库、计算工具或化学工具链。
4. 整合工具输出并生成化学答案。

## 5. 实验与验证

- 验证方式：benchmark / chemistry task evaluation，需全文确认。
- 科学贡献类型：system_platform。
- 证据强度：benchmark_only / computationally_validated，待全文确认。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 可作为 tool-using chemistry agent 的代表性早期高影响工作。
- 需要与 Coscientist 区分：ChemCrow偏工具增强，Coscientist偏自治实验和规划执行。

## 7. 后续精读任务

- 列出 ChemCrow 工具集合。
- 判断其是否满足严格 Agent 行动闭环。
- 补充具体任务和评价指标。
