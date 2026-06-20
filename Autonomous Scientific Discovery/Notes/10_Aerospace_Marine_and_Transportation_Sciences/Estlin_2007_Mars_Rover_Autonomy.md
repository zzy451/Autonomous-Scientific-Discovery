# Estlin et al. 2007 - Increased Mars Rover Autonomy using AI Planning, Scheduling and Execution

**论文信息**
- 标题：Increased Mars Rover Autonomy using AI Planning, Scheduling and Execution
- 作者：Tara Estlin; Daniel Gaines; Rebecca Castano; Benjamin Bornstein; Richard C. Anderson; David R. Thompson; Michael Burl; Steve Chien; Robert C. Anderson
- 年份：2007
- 来源 / venue：IEEE ICRA 2007
- DOI / arXiv / URL：https://doi.org/10.1109/ROBOT.2007.364236
- PDF / 本地文件路径：当前笔记基于 IEEE 会议页摘要与主列表已有一手元数据；本地未保存 PDF
- 论文类型：研究论文 / rover mission-science autonomy
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | title / IEEE abstract / master-list evidence | 论文围绕 AI planning, scheduling, execution 提升 rover autonomy，存在明确多步任务闭环 | 高 |
| 科学对象归类 | `10.02` | title / object-first rule / prior rover lineage | 研究对象是 rover mission-science autonomy，而不是火星地表自然过程本体 | 高 |
| 方法流程 | target discovery -> planning -> dynamic replanning -> execution | abstract / master-list remarks | 系统在 onboard 目标发现后执行机会科学与动态重规划 | 高 |
| 实验验证 | mission-oriented deployment evidence | IEEE metadata / master-list evidence | 属于 mission science operation 方向的高相关验证 | 中高 |
| 边界判断 | 不应改到 `05` | project boundary rule | 只要核心是 rover / spacecraft science autonomy，就应保持在 10，而非按观测对象转入 Earth or natural-process classes | 高 |

## 0. 摘要翻译

这篇论文讨论如何通过 AI planning、scheduling 和 execution 提升火星 rover 的自主性，使其能够围绕科学优先级更自动地安排活动、执行任务，并在 onboard 发现新目标后做动态重规划。论文的核心不是研究火星自然环境本体，而是研究 mission science autonomy，因此应稳定归入 10 类中的 rover / spacecraft science autonomy。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确科研任务、planning/scheduling/execution 行动链、动态重规划和基于科学优先级的自主决策
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未明确
- 在科研流程中承担的明确角色：mission science operation, opportunistic observation, replanning

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：rover mission-science autonomy
- 四级专题：AI planning and execution for rover science autonomy
- 四级专题是否为新增：否
- 归类理由：稳定对象是 rover scientific operations and autonomy，而不是 planetary natural process study
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：onboard rover mission-science workflow
- 最终科学问题：如何让 rover 在远程受限任务环境中更自主地完成科学操作
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：AI planning 和执行框架只是手段，核心对象是 mission-science autonomy

### 2.3 容易混淆的边界

- 可能误归类到：05
- 最终判定：保持 10.02
- 判定理由：若研究焦点是环境过程、地表变化或气候过程，应考虑 05；但本文焦点是 rover 如何自主开展科学任务
- 是否需要二次复核：可进一步读全文补细节，但边界判断已较稳

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：未明确
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：mission-science autonomy agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：部分是
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：部分是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：部分是
- 多模态：未明确
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：planetary rover platform

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低对地面人工连续介入的依赖，提高 mission science return
- 现有科研流程或方法的痛点：行星任务通信延迟高、带宽有限、机会科学事件容易错过
- 核心假设或直觉：如果 rover 能把 onboard 观测、科学优先级和计划执行连成闭环，就能获得更高的科学收益

### 4.2 系统流程

1. 输入：科学优先级、rover 状态与 onboard observation
2. 任务分解 / 规划：根据优先级生成活动安排
3. 工具、数据库、模型或实验平台调用：planning, scheduling, target discovery, execution modules
4. 中间结果反馈：当发现机会目标或状态变化时更新计划
5. 决策或迭代：执行动态重规划
6. 输出：优化后的 rover science activity sequence

### 4.3 系统组件

- Agent 核心：AI planning, scheduling and execution stack
- 工具 / API / 数据库：rover onboard science and operation modules
- 记忆或状态模块：mission state and target priorities
- 规划器：planning and scheduling components
- 评估器 / verifier：science-value prioritization and execution monitoring
- 人类反馈或专家介入：地面科学优先级输入
- 实验平台或仿真环境：Mars rover mission context

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：部分是
- 高通量计算：否
- 机器人实验：是
- 湿实验：否
- 临床数据：否
- 真实场景部署：是
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：rover mission science targets and onboard observations
- 任务设置：activity planning, scheduling, opportunistic science, dynamic replanning
- 对比基线：地面人工主导操作
- 评价指标：science return, follow-up responsiveness, mission-operation autonomy
- 关键结果：系统支持在 mission context 中提升机会科学和活动自主性
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏向 mission-science autonomy 能力提升
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; mission_science_planning
- 证据强度：high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一图像识别模型，而是完整的 mission-science autonomy loop
- 与已有 Agent / 科研智能系统的区别：属于较早期但清晰的 rover science autonomy 代表
- 与同一科学领域其他 Agent 文献的关系：可与 OASIS、AEGIS、ChemCam rover 系列工作形成时间谱系
- 主要创新点：将 onboard target discovery 与 planning/scheduling/execution 紧密耦合

## 7. 局限性与风险

- Agent 自主性不足：具体模块自治边界需要全文补充
- 科学验证不足：当前笔记主要依赖会议摘要和主表证据
- 泛化性不足：多半依赖特定 rover task setting
- 工具链依赖：高度依赖 mission-specific planning stack
- 数据泄漏或 benchmark 偏差：不是主要风险
- 成本、可复现性或安全风险：真实航天任务验证门槛高

## 8. 对综述写作的价值

- 可放入哪个章节：10 航空航天与运输科学中的 rover mission autonomy
- 可支撑哪个论点：搭载在火星 rover 上的科学自治系统应优先看 mission autonomy 对象，而不是按观测环境误归到 Earth/environment 类
- 可用于哪个表格或图：`10.02 / 05` 边界案例表；rover autonomy timeline
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：后续读全文再补
- 需要与哪些论文并列比较：Castano_2007_OASIS_Rover_Science; Estlin_2012_AEGIS_Opportunity_Rover; Francis_2017_AEGIS_ChemCam_MSL

## 9. 总结

### 9.1 一句话概括

AI 规划与执行框架提升火星 rover 的机会科学自主性。

### 9.2 速记版 pipeline

1. 输入科学优先级与 onboard 观测
2. 生成 rover 活动计划
3. 发现新目标后动态重规划
4. 执行并提升 mission science return

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：10
二级类：10.02
三级类：rover mission-science autonomy
四级专题：AI planning and execution for rover science autonomy
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：experiment_execution; tool_use_and_code_execution; data_analysis; evidence_assessment_and_validation; workflow_orchestration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：robotic_experiment; real_world_deployment; mission_operation
交叉属性：computation_driven; data_driven; experiment_driven; robotic_platform
科学贡献类型：system_platform; mission_science_planning
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
