# Castano et al. 2007 - Onboard Autonomous Rover Science

**论文信息**
- 标题：Onboard Autonomous Rover Science
- 作者：Rebecca Castano; Tara Estlin; Dan Gaines; Caroline Chouinard; Ben Bornstein; Robert C. Anderson; Michael Burl; David Thompson; Andres Castano; Michele Judd
- 年份：2007
- 来源 / venue：2007 IEEE Aerospace Conference
- DOI / arXiv / URL：https://doi.org/10.1109/AERO.2007.352700
- PDF / 本地文件路径：当前无本地 PDF；本 note 基于 DOI metadata、CMU publication page 摘要与 batch13 reviewer evidence packs
- 论文类型：研究论文 / onboard rover mission-science autonomy
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | CMU abstract；reviewer pack | OASIS 在 FIDO rover 上做闭环 opportunistic detection and reaction 演示 | 高 |
| 科学对象归类 | `10 / 10.02` | CMU abstract；DOI metadata | 核心是 onboard rover science autonomy，不是火星环境机理研究 | 高 |
| 方法流程 | 多步任务闭环 | CMU abstract | 包含 planning/scheduling、image prioritization、target assessment、follow-up | 高 |
| 边界判断 | 不移到 `05` | reviewer pack | 岩石分析只是 autonomy loop 内的感知对象，不是论文主对象 | 高 |
| 实验验证 | 硬件演示 + 仿真 | CMU abstract | 在 FIDO rover 和 ROAMS simulator 中测试 | 高 |

## 0. 摘要翻译

论文介绍 OASIS 在 NASA JPL 的 FIDO rover 上完成的车载自主科学演示。系统能够在 rover traverse 过程中闭环识别新的科学机会，做图像优先级排序，在行程末端生成局部全景并评估目标，再采集更高价值的窄视场图像。作者同时报告了硬件演示和 ROAMS 仿真结果，并比较若干岩石属性估计方法，以支持自主岩石分析。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多步行动链条、planning/scheduling、感知分析与后续观测决策
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：onboard science analysis、任务重规划、机会目标跟踪、补充观测执行

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：
- 四级专题：Onboard rover mission-science autonomy systems
- 四级专题是否为新增：否
- 归类理由：最终对象是 rover 如何在任务执行中自主完成科学分析与机会响应
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：onboard autonomous rover science workflow
- 最终科学问题：rover 如何自主发现、排序并跟进科学目标
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：图像分析与 geology scene 只是 autonomy 感知对象，不是最终科学对象

### 2.3 容易混淆的边界

- 可能误归类到：05
- 最终判定：保持 10.02
- 判定理由：若论文研究火星地质或气象过程本身才更偏 `05`；本篇研究的是 mission-science autonomy
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
- 其他：OASIS rover science loop

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
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：opportunistic science

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：提升 rover 在任务执行中的自主科学能力
- 现有科研流程或方法的痛点：过度依赖地面人工决策
- 核心假设或直觉：把感知、优先级排序和 planning/scheduling 连成闭环，可提升 mission-science return

### 4.2 系统流程

1. 输入：traverse 过程中采集的图像与场景
2. 任务分解 / 规划：识别科学机会并评估价值
3. 工具、数据库、模型或实验平台调用：planning/scheduling；感知分析；target assessment
4. 中间结果反馈：根据目标价值更新后续动作
5. 决策或迭代：调整命令序列并追加观测
6. 输出：更高价值的 onboard science actions

### 4.3 系统组件

- Agent 核心：OASIS
- 工具 / API / 数据库：image prioritization；science target assessment；planning/scheduling
- 记忆或状态模块：traverse state
- 规划器：有
- 评估器 / verifier：science value assessment
- 人类反馈或专家介入：有上位任务约束
- 实验平台或仿真环境：FIDO rover；ROAMS simulator

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：是
- 高通量计算：否
- 机器人实验：是
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：FIDO rover onboard science demonstrations
- 任务设置：opportunistic detection and reaction
- 对比基线：人工或非自主流程
- 评价指标：mission-science return 与闭环能力
- 关键结果：实现闭环 opportunistic science
- 是否有消融实验：当前证据不足
- 是否有失败案例或负结果：当前证据不足

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：重点是 rover autonomy 能力
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; mission_science_planning
- 证据强度：high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是地质分析模型，而是完整 onboard mission-science loop
- 与已有 Agent / 科研智能系统的区别：较早实现 rover science closed loop
- 与同一科学领域其他 Agent 文献的关系：是 OASIS / AEGIS / ChemCam 线的重要锚点
- 主要创新点：把 onboard perception、science prioritization 和 planning/scheduling 连成闭环

## 7. 局限性与风险

- Agent 自主性不足：任务目标仍需上位设定
- 科学验证不足：一手证据以摘要为主
- 泛化性不足：依赖特定 rover 平台与场景
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：当前证据不足
- 成本、可复现性或安全风险：仍建议补 IEEE 正式 PDF

## 8. 对综述写作的价值

- 可放入哪个章节：10 航天 rover mission-science autonomy
- 可支撑哪个论点：rover science operations 与 EO-1 Earth science applications 在 `10 / 05` 边界上应分开
- 可用于哪个表格或图：class 10 早期锚点时间线
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续正式 PDF
- 需要与哪些论文并列比较：0852、0854、0858

## 9. 总结

### 9.1 一句话概括

面向 Mars rover onboard science operations 的闭环自主系统。

### 9.2 速记版 pipeline

1. 采集 onboard 场景
2. 识别科学机会
3. 排序高价值目标
4. 调整命令并追加观测
5. 提升 science return

### 9.3 标注字段汇总

```text
是否纳入：是
主类：10
二级类：10.02
三级类：
四级专题：Onboard rover mission-science autonomy systems
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：data_analysis; experiment_execution; workflow_orchestration; feedback_iteration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：robotic_experiment; simulation_validation
交叉属性：data_driven; experiment_driven; simulation_driven; robotic_platform
科学贡献类型：system_platform; mission_science_planning
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```

