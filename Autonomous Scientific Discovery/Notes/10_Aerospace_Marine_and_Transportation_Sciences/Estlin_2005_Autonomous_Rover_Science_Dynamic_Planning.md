# Estlin et al. 2005 - Enabling Autonomous Rover Science Through Dynamic Planning and Scheduling

**论文信息**
- 标题：Enabling Autonomous Rover Science Through Dynamic Planning and Scheduling
- 作者：Tara Estlin; Trey Smith; David Wettergreen; Steve Chien; Rebecca Castano; et al.
- 年份：2005
- 来源 / venue：IEEE Aerospace Conference
- DOI / arXiv / URL：https://ai.jpl.nasa.gov/public/documents/papers/estlin-ieeeaero2005-EnablingAutonomous.pdf
- PDF / 本地文件路径：当前笔记基于 JPL official PDF
- 论文类型：研究论文 / dynamic-planning rover science
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## Round-2 Relaxed Multi-Module Update (2026-06-21)

- `scientific_object_modules`: `10`
- `object_coverage_mode`: `single_module`
- `primary_module_for_filing`: `10`
- `general_method_bucket`: `none`
- `first_hand_sources_checked`: official JPL PDF `estlin-ieeeaero2005-EnablingAutonomous.pdf`
- `classification_evidence_source_level`: `first_hand_full_text`
- `note_revision_required`: `no`

This note no longer treats the record as a live `10 / 05` boundary question. The official full text is strong enough to keep the paper in `10` only: its stable object is onboard rover mission-science planning and scheduling, including science alerts, target insertion, resource-aware replanning, and opportunistic science handling. The paper does mention Mars and science targets, but it does not report an independent planetary-environment, geology, or Earth-and-environment-style object study strong enough to add `05` under the current relaxed rule.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 官方 PDF 摘要与引言 | 接收 science and engineering goals，生成 plan，并在新机会或故障下 re-plan | 高 |
| 科学对象归类 | `10.02` | CLEaR/OASIS 描述 | 对象是 rover mission-science autonomy，而不是火星 geology 本体 | 高 |
| 方法流程 | 多步闭环 | 功能列表 | initial plan creation、execution、monitoring、dynamic modification、optimization、science alerts | 高 |
| 反馈驱动自主决策 | 明确存在 | science alerts 描述 | onboard data analysis 触发新目标后系统可重规划并追加科学动作 | 高 |
| 实验验证 | 仿真 + rover hardware | 测试部分 | 在模拟与真实 rover hardware 上处理机会科学事件并完成自主运行 | 高 |

## 0. 摘要翻译

论文研究如何把动态规划与调度部署到火星车 onboard，使其围绕 science goals 自主调整活动。系统既能执行地面给定的科学目标，也能响应 onboard data analysis 发现的新目标，在资源、时间与路径不确定性下持续重规划。核心对象是 rover mission-science autonomy，而非行星自然过程本体。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科学目标、多步执行与监控、反馈触发重规划、自主决策与环境交互
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：实验执行、数据分析、任务编排、反馈迭代

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：dynamic-planning rover science
- 四级专题：dynamic-planning rover science agents
- 四级专题是否为新增：否
- 归类理由：论文的稳定对象是航天任务中的 onboard science planning and scheduling
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：rover onboard mission-science planning workflow
- 最终科学问题：如何在火星车上基于 science alerts 动态重规划科学任务
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：planning / scheduling 是手段，最终对象仍是 mission-science autonomy

### 2.3 容易混淆的边界

- 可能误归类到：05
- 最终判定：保持 10.02
- 判定理由：论文不是研究火星 geology，而是 rover 如何自主做科学决策
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：dynamic planning mission-science agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：部分是
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：部分是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：onboard planning and scheduling

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：让 rover 能在通信延迟与不确定条件下自主抓住科学机会
- 现有科研流程或方法的痛点：传统命令序列缺少对新科学机会的即时响应
- 核心假设或直觉：dynamic planning + onboard science alerts 能提升 mission science return

### 4.2 系统流程

1. 输入：science and engineering goals
2. 任务分解 / 规划：CLEaR 生成初始计划
3. 工具、数据库、模型或实验平台调用：execution、monitoring、constraint maintenance、science alerts
4. 中间结果反馈：OASIS 提供 onboard data analysis 与 new opportunities
5. 决策或迭代：re-plan、modify path、insert new science actions
6. 输出：更新后的 rover mission-science plan

### 4.3 系统组件

- Agent 核心：CLEaR + OASIS
- 工具 / API / 数据库：planning / scheduling stack、onboard data analysis
- 记忆或状态模块：constraint maintenance、plan state
- 规划器：有
- 评估器 / verifier：monitoring 与 opportunity handling
- 人类反馈或专家介入：初始 goals 由地面提供
- 实验平台或仿真环境：simulations + rover hardware

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：是
- 高通量计算：否
- 机器人实验：是
- 湿实验：否
- 临床数据：否
- 真实场景部署：部分是
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：science alerts 与 rover mission tasks
- 任务设置：opportunistic science event handling
- 对比基线：静态计划执行
- 评价指标：机会科学事件处理成功、自主运行距离与任务完成
- 关键结果：系统在模拟和真实 rover hardware 上完成自主运行与机会科学处理
- 是否有消融实验：当前笔记未细化
- 是否有失败案例或负结果：当前笔记未细化

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是 mission-science autonomy capability
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / mission-science planning
- 证据强度：仿真支持 + 机器人实验

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态路径规划，而是围绕科学回报的动态任务 Agent
- 与已有 Agent / 科研智能系统的区别：较早系统化地把 planning and scheduling 接入 onboard science loop
- 与同一科学领域其他 Agent 文献的关系：是 OASIS / AEGIS 谱系的重要早期 anchor
- 主要创新点：science alerts 驱动的 dynamic replanning

## 7. 局限性与风险

- Agent 自主性不足：受 mission constraints 限制
- 科学验证不足：更偏 autonomy 机制而非直接科学新发现
- 泛化性不足：以 rover missions 为主
- 工具链依赖：planning/scheduling stack 强依赖
- 数据泄漏或 benchmark 偏差：不是主要风险
- 成本、可复现性或安全风险：真实任务落地仍需高验证成本

## 8. 对综述写作的价值

- 可放入哪个章节：10 航天科学中的 rover planning agents
- 可支撑哪个论点：mission-science autonomy 的关键能力之一是动态重规划
- 可用于哪个表格或图：rover autonomy 历史谱系图
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：功能列表与 science alerts 描述
- 需要与哪些论文并列比较：ASD-0691；ASD-0696；ASD-0713

## 9. 总结

### 9.1 一句话概括

围绕 science alerts 动态重规划的 rover mission-science Agent。

### 9.2 速记版 pipeline

1. 接收科学与工程目标
2. 生成初始计划
3. 监控执行与约束
4. 接收 science alerts 并重规划
5. 更新 rover 科学任务

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：10
二级类：10.02
三级类：dynamic-planning rover science
四级专题：dynamic-planning rover science agents
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：data_analysis; workflow_orchestration; feedback_iteration; autonomous_decision_making
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：simulation_validation; robotic_experiment
交叉属性：computation_driven; data_driven; experiment_driven; robotic_platform
科学贡献类型：system_platform
证据强度：high_primary_pdf
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
