# Unknown 2025 - A virtual platform for automated hybrid organic-enzymatic synthesis planning

**论文信息**
- 标题：A virtual platform for automated hybrid organic-enzymatic synthesis planning
- 作者：Unknown
- 年份：2025
- 来源 / venue：Nature Communications
- DOI / arXiv / URL：https://doi.org/10.1038/s41467-025-65898-3
- PDF / 本地文件路径：未保存本地 PDF；本笔记基于 Nature Communications 正式页面与 reviewer 一手证据
- 论文类型：research paper / chemistry planning agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract / method description | Llama3.1 驱动的 synthesis planning agent 结合多工具 API 执行路线规划 | 高 |
| 科学对象归类 | `03.03` | abstract / case studies | 对象是具体分子、天然产物与其混合有机-酶催化合成路径 | 高 |
| 方法流程 | 多工具路线规划与策略切换 | platform description | 先评估反应可行性，再判断酶反应，再做酶推荐与路径扩展 | 高 |
| 实验验证 | 以计算与案例验证为主 | benchmark / case studies | 主要是路径求解、AUC、Top-k 和天然产物案例，不是湿实验闭环 | 高 |
| 边界判断 | 不应退回 `01.04` | object framing | 虽然平台/API 味道强，但最终被研究和验证的是具体合成对象 | 高 |

## 0. 摘要翻译

论文提出 ChemEnzyRetroPlanner，将有机合成与酶催化路线规划、条件预测、可行性评估、酶反应识别与酶推荐整合在一起，并借助 Llama3.1 代理在纯有机路径失败时自动切换到混合有机-酶催化策略，用于复杂分子和天然产物的合成规划。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确合成规划目标、多步决策、工具调用、策略切换与案例验证
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：合成路线规划、反应可行性评估、酶推荐

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否，但闭环主要体现在规划策略切换而非机器人湿实验
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：03
- 二级类：03.03
- 三级类：
- 四级专题：Hybrid organic-enzymatic synthesis planning
- 四级专题是否为新增：否
- 归类理由：被规划和比较的是具体有机/酶催化合成路线
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：具体分子与天然产物的混合有机-酶催化合成路径
- 最终科学问题：如何更有效地找到可执行的混合有机-酶催化路线
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：Llama3.1 与 API 平台只是手段，研究对象始终是 chemical synthesis

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 03.03
- 判定理由：即使平台味道强，验证对象仍是 concrete chemistry routes
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：synthesis planning agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：部分是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：否
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：enzyme recommendation

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：纯有机 retrosynthesis 对复杂分子常受限，混合有机-酶催化更有潜力
- 现有科研流程或方法的痛点：路线规划与酶步骤推荐仍然割裂
- 核心假设或直觉：通过代理协调多工具与策略切换，可以更有效找到 hybrid routes

### 4.2 系统流程

1. 输入：目标分子或天然产物
2. 任务分解 / 规划：评估是否可用纯有机路径，否则切换 hybrid strategy
3. 工具、数据库、模型或实验平台调用：反应可行性、酶反应识别、酶推荐等模块
4. 中间结果反馈：返回候选路径与评分
5. 决策或迭代：筛选更优合成路径
6. 输出：混合有机-酶催化合成方案

### 4.3 系统组件

- Agent 核心：Llama3.1-based planner
- 工具 / API / 数据库：route planning / enzyme recommendation modules
- 记忆或状态模块：候选路径集合
- 规划器：retrosynthesis search
- 评估器 / verifier：路径求解率、AUC、Top-k
- 人类反馈或专家介入：案例解释中存在
- 实验平台或仿真环境：无机器人平台

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：organic compounds and natural products
- 任务设置：hybrid route planning 与 enzyme recommendation
- 对比基线：现有 retrosynthesis / enzyme tools
- 评价指标：path recovery、AUC、Top-k 等
- 关键结果：能在纯有机路径失败时切换 hybrid strategy，并生成大量候选路径
- 是否有消融实验：部分有
- 是否有失败案例或负结果：未系统展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是路径规划能力提升
- 科学贡献是否经过验证：是，但以计算与案例为主
- 贡献强度判断：中
- 科学贡献类型：system_platform; design
- 证据强度：计算验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次预测，而是多模块协调的合成规划 agent
- 与已有 Agent / 科研智能系统的区别：强调 hybrid organic-enzymatic synthesis
- 与同一科学领域其他 Agent 文献的关系：可作为 chemistry planning agent 的代表样本
- 主要创新点：把酶反应识别与酶推荐更深整合进合成路线规划

## 7. 局限性与风险

- Agent 自主性不足：没有湿实验闭环
- 科学验证不足：相对中等
- 泛化性不足：主要在给定规划任务上验证
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：需要继续关注
- 成本、可复现性或安全风险：依赖模块化工具链质量

## 8. 对综述写作的价值

- 可放入哪个章节：03 化学科学 / synthesis planning agents
- 可支撑哪个论点：平台感很强的路线规划系统，若最终对象是具体化学合成，仍应归 03
- 可用于哪个表格或图：planning-oriented chemistry agents
- 适合作为代表性案例吗：可以
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：abstract、case-study sections
- 需要与哪些论文并列比较：ChemCrow、Chemputer、virtual chemistry agents

## 9. 总结

### 9.1 一句话概括

代理协调多工具规划混合有机-酶催化路线。

### 9.2 速记版 pipeline

1. 输入目标分子
2. 判断纯有机路径是否可行
3. 调用酶反应识别与推荐工具
4. 扩展候选合成路径
5. 输出更优 hybrid route

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：03
二级类：03.03
三级类：
四级专题：Hybrid organic-enzymatic synthesis planning
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; autonomous_decision_making
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：design; system_platform
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```

