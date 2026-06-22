# Castano et al. 2007 - OASIS: Onboard Autonomous Science Investigation System for Opportunistic Rover Science

**论文信息**
- 标题：OASIS: Onboard Autonomous Science Investigation System for Opportunistic Rover Science
- 作者：Rebecca Castano; Trey Smith; M. D. Judd; Steve Chien; David Wettergreen; Delbert G. Graham
- 年份：2007
- 来源 / venue：Journal of Field Robotics
- DOI / arXiv / URL：https://doi.org/10.1002/rob.20192
- PDF / 本地文件路径：当前笔记基于 JPL official PDF URL（https://ai.jpl.nasa.gov/public/documents/papers/castano-jfr07-oasis.pdf）；未见本地归档 PDF
- 论文类型：研究论文 / rover mission-science autonomy
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | JPL PDF 摘要 | rover 能识别并响应 serendipitous science opportunities，并决定是否追加观测 | 高 |
| 科学对象归类 | `05;10` | JPL PDF 摘要、引言、系统描述 | 论文同时覆盖行星科学目标对象（rocks、clouds、dust devils）与 rover mission-science autonomy | 高 |
| 方法流程 | 多步闭环 | JPL PDF 系统结构与流程 | 图像采集 -> target detection -> feature extraction -> prioritization -> planning/scheduling -> follow-up | 高 |
| 自主决策 | 明确存在 | JPL PDF 中 scientist target signatures 与 novelty detection 描述 | 系统根据科学目标自主优先排序并调整 command sequence | 高 |
| 实验验证 | 真实任务导向 | JPL PDF 的 onboard testing、FIDO、MER infusion 描述 | 模块在真实 mission 场景与飞行软件渗透中测试，并服务实际 mission-science return | 高 |

## 0. 摘要翻译

OASIS 是一个面向行星 rover 的 onboard autonomous science system。它能够在漫游过程中自动分析图像、识别岩石、云和尘卷风等潜在高价值行星科学目标，并结合 planning and scheduling 动态调整后续观测与任务序列，从而提高 mission science return。按当前 relaxed multi-module 口径，这篇论文既覆盖 `10` 侧的 rover mission-science autonomy，也覆盖 `05` 侧的行星表面与大气环境科学目标。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多步行动链、工具/模块调用、反馈迭代与自主决策
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：观测执行、数据分析、任务重规划

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`05`; `10`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：10
- Primary module for filing 说明：主文件仍放在 `10`，因为论文的系统主线是 rover mission-science autonomy；这不覆盖 `05` 的对象事实。
- 主展示模块一级类：10
- 主展示模块二级类：10.02
- 主展示模块三级类：rover mission-science autonomy
- 主展示模块四级专题：opportunistic rover-science agents
- 其他覆盖模块及对应层级路径：`05` -> 行星表面 / 大气环境科学目标（rocks、clouds、dust devils）
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：`10` 来自 onboard planning/scheduling、follow-up targeting、mission infusion；`05` 来自对 rocks、clouds、dust devils 等行星科学目标的识别与追加观测。
- 归类理由：全文既验证 rover 如何自主执行 mission-science 工作流，也明确围绕具体行星科学目标开展检测、排序与后续观测。
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：rover 任务中的机会型行星科学目标识别与后续观测执行
- 最终科学问题：如何让 rover 在任务中自主识别并跟进行星科学高价值目标，同时把这些机会转化为 mission-science actions
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：规划器、视觉模块和发表 venue 都只是手段；实际对象证据同时落在行星科学目标与航天 mission-science autonomy 上

### 2.3 容易混淆的边界

- 可能误归类到：仅 `05`；仅 `10`
- 最终判定：保留 `10` 为 primary filing，同时补记 `05`
- 判定理由：如果只看 autonomy 主线会漏掉论文反复使用的 rocks、clouds、dust devils 等行星科学目标；如果只看行星目标又会漏掉论文关于 onboard planning/scheduling 与 mission-science autonomy 的核心系统贡献。
- 多模块覆盖说明：`10` 负责承载 rover mission-science autonomy，`05` 负责承载被识别和追踪的行星表面 / 大气环境科学目标。
- 01.04 判定说明：不适用；本文有明确具体对象与任务验证。
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
- 其他：onboard mission-science agent

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
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：planetary rover platform

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：让 rover 在有限带宽和高延迟任务中最大化科学回报
- 现有科研流程或方法的痛点：传统 rover 操作过度依赖地面人工判断
- 核心假设或直觉：onboard data analysis + planning/scheduling 可以形成机会科学闭环

### 4.2 系统流程

1. 输入：onboard image / science team target signatures
2. 任务分解 / 规划：识别候选目标与机会事件
3. 工具、数据库、模型或实验平台调用：target detection、feature extraction、novelty detection、planning/scheduling
4. 中间结果反馈：目标优先级与机会事件判断
5. 决策或迭代：动态调整 rover command sequence
6. 输出：追加观测、优先化数据回传与 mission-science actions

### 4.3 系统组件

- Agent 核心：onboard science analysis + planning / scheduling
- 工具 / API / 数据库：image analysis modules、prioritization、novelty detection
- 记忆或状态模块：mission state 与 target priorities
- 规划器：有
- 评估器 / verifier：science-value prioritization
- 人类反馈或专家介入：scientist target signatures
- 实验平台或仿真环境：FIDO rover / MER mission context

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

- 数据集 / 实验对象：rocks、clouds、dust devils 等行星科学目标，以及 FIDO / MER 任务场景中的 rover onboard science workflow
- 任务设置：识别目标、排序、规划、追加观测
- 对比基线：人工主导 mission operations
- 评价指标：目标识别与 follow-up 成功、science return、mission infusion
- 关键结果：在真实 mission 场景中实现 opportunistic science loop，把行星科学目标检测与后续观测决策连成 onboard 闭环
- 是否有消融实验：当前笔记未细化
- 是否有失败案例或负结果：记录了模块特定局限

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献是 mission-science autonomy 能力提升，而不是直接提出新的行星科学规律
- 科学贡献是否经过验证：是
- 贡献强度判断：中强
- 科学贡献类型：系统平台 / mission-science planning
- 证据强度：真实部署

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次 geology / atmospheric image model，而是把具体行星科学目标检测接入 mission-science autonomy loop
- 与已有 Agent / 科研智能系统的区别：较早实现 onboard opportunistic science
- 与同一科学领域其他 Agent 文献的关系：是 OASIS / AEGIS / ChemCam 系列的重要前驱
- 主要创新点：把 science opportunity detection 与 planning/scheduling 连成闭环

## 7. 局限性与风险

- Agent 自主性不足：目标特征与检测模块仍较任务特定
- 科学验证不足：更偏任务 autonomy，而非直接新地学发现
- 泛化性不足：主要在特定 rover mission 场景上验证
- 工具链依赖：依赖 onboard image analysis 与 planning stack
- 数据泄漏或 benchmark 偏差：不是主要风险
- 成本、可复现性或安全风险：真实任务部署需要严格验证

## 8. 对综述写作的价值

- 可放入哪个章节：主放 `10` 航天科学中的 rover mission-science autonomy，并在 `05` 行星环境 / 表面科学目标案例中交叉引用
- 可支撑哪个论点：mission-science agents 早在 LLM 时代之前已形成清晰谱系
- 可用于哪个表格或图：10 类历史锚点时间线
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：系统架构图与 planning/scheduling 说明
- 需要与哪些论文并列比较：ASD-0696；ASD-0697；ASD-0712

## 9. 总结

### 9.1 一句话概括

同时覆盖 rover mission-science autonomy 与行星科学目标识别的机会型 Agent。

### 9.2 速记版 pipeline

1. 采集并分析 onboard 图像
2. 识别候选科学目标
3. 评估优先级与新颖性
4. 动态调整观测与任务序列
5. 提升 rover science return

### 9.3 标注字段汇总

```text
是否纳入：to_read
科学对象模块：05;10
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：10
是否进入 01.04 存放区：否
主展示模块一级类：10
主展示模块二级类：10.02
主展示模块三级类：rover mission-science autonomy
主展示模块四级专题：opportunistic rover-science agents
其他覆盖模块及对应层级路径：05 -> 行星表面 / 大气环境科学目标
module_assignment_evidence：05 来自 rocks、clouds、dust devils 等对象目标；10 来自 onboard planning/scheduling、follow-up targeting、mission infusion
multi_module_object_coverage_note：全文既验证 rover mission-science autonomy，也围绕具体行星科学目标进行识别和后续观测
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：data_analysis; experiment_execution; workflow_orchestration; feedback_iteration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：robotic_experiment; real_world_deployment; expert_evaluation
交叉属性：data_driven; experiment_driven; robotic_platform
科学贡献类型：system_platform
证据强度：high_primary_pdf
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
