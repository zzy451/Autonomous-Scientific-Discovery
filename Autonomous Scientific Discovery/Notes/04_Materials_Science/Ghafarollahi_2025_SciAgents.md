# Ghafarollahi and Buehler 2025 - SciAgents

**论文信息**
- 标题：SciAgents: Automating Scientific Discovery Through Bioinspired Multi-Agent Intelligent Graph Reasoning
- 作者：Alireza Ghafarollahi, Markus J. Buehler
- 年份：2025
- 来源 / venue：Advanced Materials
- DOI / URL：https://doi.org/10.1002/adma.202413523
- 当前状态：candidate；core priority；full-text evidence pending

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract / Advanced Materials page | multi-agent intelligent graph reasoning; autonomous hypothesis generation | 高 |
| 科学对象归类 | `04` 材料科学 | arXiv abstract | case studies in bioinspired materials and materials discovery | 高 |
| 方法机制 | 知识图谱 + LLM + 多 Agent | arXiv abstract | ontological knowledge graphs, LLM suite, data retrieval tools, multi-agent systems | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- Agent 行动闭环：多 Agent 协作、知识图谱推理、假设生成与 refinement。
- 纳入置信度：高。

## 2. 科学领域归类

- 一级类：`04` 材料科学
- 二级类：`04.03` 软物质与功能材料，或 `04.04` 材料发现，待全文确定。
- 四级专题：multi-agent graph reasoning for materials discovery
- 归类理由：虽然系统叫 SciAgents，案例和科学对象主要面向材料发现。

## 3. Agent 系统与科研流程角色

- Agent 类型：Multi-Agent System；Retrieval-augmented Agent；Hybrid Agent。
- 科研流程角色：知识组织、假设生成、结果解释、证据评估。
- 交叉属性：知识图谱、多 Agent、多模态/多源知识整合。

## 4. 方法设计

初步 pipeline：

1. 构建或调用材料/科学概念知识图谱。
2. 多 Agent 读取并检索相关知识。
3. 通过图推理发现跨领域关系。
4. 生成并批判性改进研究假设。
5. 输出材料发现方向或机制解释。

## 5. 实验与验证

- 验证方式：案例研究与假设生成，是否有实验验证需全文复核。
- 科学贡献类型：hypothesis；explanation；system_platform。
- 证据强度：暂定 simulation_supported / expert_confirmed，待确认。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 可作为材料科学中“多 Agent + 知识图谱 + 假设生成”的代表性案例。
- 需要与 AtomAgents / alloy design PNAS 论文区分。

## 7. 后续精读任务

- 提取 Agent 角色分工。
- 判断是否产生经验证的新材料发现。
- 记录图谱来源、工具和评价方式。
