# Nazeri et al. 2026 - RAISE: a self-driving laboratory for interfacial property formulation discovery

**论文信息**
- 标题：RAISE: a self-driving laboratory for interfacial property formulation discovery
- 作者：Nazeri et al.
- 年份：2026
- 来源 / venue：Digital Discovery
- DOI / arXiv / URL：https://doi.org/10.1039/d5dd00531k
- PDF / 本地文件路径：当前未保存本地 PDF；本笔记基于 Crossref 官方元数据摘要
- 论文类型：研究论文 / self-driving laboratory
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Crossref abstract | 系统被明确描述为 `the first autonomous closed-loop system` | 高 |
| 科学对象归类 | `04.03` | Crossref abstract | 直接把 formulation 与 `surface wettability` 连接起来做目标导向发现 | 高 |
| 方法流程 | 闭环 SDL | Crossref abstract | 从 user-defined goals 出发进行 formulation discovery | 高 |
| 实验验证 | 有真实闭环发现流程 | Crossref abstract | 不是单次预测，而是 autonomous closed-loop discovery | 中高 |
| 边界判断 | 不转 `01.04` | Crossref abstract | 核心对象是 interfacial-property formulation，不是通用科研平台 | 高 |

## 0. 摘要翻译

RAISE 被描述为首个将配方与表面润湿性直接连接起来的自主闭环系统，可根据用户给定目标自动发现新配方。就当前可得官方摘要而言，论文的核心不是一般性的科研 Agent 平台，而是一个围绕界面性质与配方搜索展开的自驱动实验系统。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确科研目标，具有多步闭环流程，并承担实验选择、执行与反馈优化角色
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未见明确证据
- 在科研流程中承担的明确角色：配方搜索、实验决策、闭环优化

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：04
- 二级类：04.03
- 三级类：interfacial-property formulation discovery
- 四级专题：self-driving formulation discovery
- 四级专题是否为新增：否
- 归类理由：直接研究对象是配方及其界面润湿性表现，属于软物质 / 功能材料导向的材料发现问题
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：formulation 与 surface wettability
- 最终科学问题：如何根据目标界面性质自动发现合适配方
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：闭环 Agent 架构只是手段，稳定对象仍是具体材料 / 配方性质

### 2.3 容易混淆的边界

- 可能误归类到：01.04；03
- 最终判定：保留 04.03
- 判定理由：当前证据没有把重点放在通用科研基础设施，也不是以分子反应或合成路线为核心
- 是否需要二次复核：是，后续可补全文确认具体实验平台与材料家族

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：未见明确证据
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：未见明确证据
- Hybrid Agent：是
- 其他：self-driving laboratory

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：是
- 仿真建模：未见明确证据
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：未见明确证据
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未见明确证据
- 环境交互：是
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：否
- 多模态：未见明确证据
- 多尺度建模：否
- 高通量筛选：部分是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：界面润湿性优化

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：把用户目标直接转化为配方发现任务
- 现有科研流程或方法的痛点：界面配方空间大、人工试错慢
- 核心假设或直觉：闭环自主实验系统可以更快逼近目标润湿性配方

### 4.2 系统流程

1. 输入：用户定义的 formulation discovery goal
2. 任务分解 / 规划：选择下一轮候选配方
3. 工具、数据库、模型或实验平台调用：调用自驱动实验平台完成测试
4. 中间结果反馈：根据界面性质结果更新决策
5. 决策或迭代：继续闭环搜索
6. 输出：满足目标表面润湿性的候选配方

### 4.3 系统组件

- Agent 核心：RAISE
- 工具 / API / 数据库：实验执行与性质评估平台
- 记忆或状态模块：闭环搜索状态
- 规划器：未在摘要中展开
- 评估器 / verifier：surface wettability readout
- 人类反馈或专家介入：摘要未展开
- 实验平台或仿真环境：self-driving laboratory

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：否
- 高通量计算：否
- 机器人实验：是
- 湿实验：是
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：interfacial formulations
- 任务设置：从用户目标出发做 surface wettability 导向发现
- 对比基线：摘要未展开
- 评价指标：目标界面性质是否达成
- 关键结果：实现 autonomous closed-loop formulation discovery
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是实现目标导向配方发现
- 科学贡献是否经过验证：有闭环实验系统支撑
- 贡献强度判断：中
- 科学贡献类型：design / system_platform / experimental_discovery
- 证据强度：实验验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是离线预测，而是带执行与反馈的 SDL
- 与已有 Agent / 科研智能系统的区别：围绕界面性质配方发现的具体闭环对象
- 与同一科学领域其他 Agent 文献的关系：可与电解液、聚合物、薄膜等材料 SDL 案例并列
- 主要创新点：把 formulation-discovery 问题明确做成目标导向自主闭环

## 7. 局限性与风险

- Agent 自主性不足：摘要未展开异常处理与人工接管比例
- 科学验证不足：当前只有摘要级证据
- 泛化性不足：是否能迁移到其他性质 / 配方体系仍待确认
- 工具链依赖：依赖具体 SDL 平台
- 数据泄漏或 benchmark 偏差：不是当前主要风险
- 成本、可复现性或安全风险：实验平台复现实作成本可能较高

## 8. 对综述写作的价值

- 可放入哪个章节：04 材料科学
- 可支撑哪个论点：界面配方发现已经出现明确 self-driving laboratory 代表样本
- 可用于哪个表格或图：materials SDL case table
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续补 PDF
- 需要与哪些论文并列比较：电解液发现、聚合物优化、材料模拟 Agent

## 9. 总结

### 9.1 一句话概括

RAISE 用闭环 SDL 自动发现目标界面配方。

### 9.2 速记版 pipeline

1. 输入目标润湿性
2. 选择候选配方
3. 自动实验测试
4. 反馈更新
5. 输出更优配方

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：04
二级类：04.03
三级类：interfacial-property formulation discovery
四级专题：self-driving formulation discovery
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：hypothesis_generation; experimental_design; tool_use_and_code_execution; experiment_execution; data_analysis; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：robotic_experiment; wet_lab_experiment
交叉属性：computation_driven; data_driven; experiment_driven; robotic_platform
科学贡献类型：design; system_platform; experimental_discovery
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
