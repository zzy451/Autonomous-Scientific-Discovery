# Castano et al. 2007 - Onboard Autonomous Rover Science

**论文信息**
- 标题：Onboard Autonomous Rover Science
- 作者：Rebecca Castano; Tara Estlin; Dan Gaines; Caroline Chouinard; Ben Bornstein; Robert C. Anderson; Michael Burl; David Thompson; Andres Castano; Michele Judd
- 年份：2007
- 来源 / venue：2007 IEEE Aerospace Conference
- DOI / arXiv / URL：https://doi.org/10.1109/AERO.2007.352700
- PDF / 本地文件路径：`Reference_PDF/10_Aerospace_Marine_and_Transportation_Sciences/Castano_2007_Onboard_Autonomous_Rover_Science.pdf`
- 论文类型：研究论文 / onboard rover mission-science autonomy
- 当前状态：to_read（note 已按 Batch29Partial1 writeback 更新）
- 阅读日期：2026-06-24
- 笔记作者：Codex

## 2026-06-24 Batch29Partial1 writeback / full reaudit

- final supported_modules：`10`
- primary_module_for_filing：`10`
- object_coverage_mode：`single_module`
- final_01_04_bucket：`none`
- source_limited：`no`
- safety_access_status：`accessed_no_safety_issue`
- evidence source level：`first_hand_full_text; official_jpl_pdf_archived_locally_and_checked`
- first-hand source checked：`official JPL PDF checked locally: Reference_PDF/10_Aerospace_Marine_and_Transportation_Sciences/Castano_2007_Onboard_Autonomous_Rover_Science.pdf`；original source `https://ai.jpl.nasa.gov/public/documents/papers/castano-iac07-onboard.pdf`
- note_revision_required：`yes`
- adjudication confidence：`high`
- final_reason：OASIS / FIDO rover mission-science autonomy, planning / scheduling, target assessment, and follow-up imaging are stable class-10 mission-science evidence.

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract | OASIS 在 FIDO rover 上完成 closed-loop opportunistic detection and reaction，并在 ROAMS simulator 中进一步演示。 | 高 |
| `10` 模块证据 | 强支持 | Abstract | 论文明确围绕 rover traverse 中的 onboard autonomous science、planning / scheduling、image prioritization、target selection 与 follow-up imaging。 | 高 |
| 方法流程 | 多步闭环明确 | Abstract | 包括 partial panorama、targets of interest assessment、narrow-angle image collection 等顺序决策环节。 | 高 |
| 验证方式 | 硬件演示 + 仿真 | Abstract | 同时报告 FIDO rover hardware demonstration 与 ROAMS simulation 结果。 | 高 |
| 边界判断 | 不补 `05` | object-first reading | 虽有 rock-property estimation 和 geology sensing，但本轮冻结裁决要求保持 mission-science autonomy 的 `10` 单模块表述。 | 高 |

## 0. 摘要翻译

论文介绍 OASIS 在 NASA JPL 的 FIDO rover 上完成的 onboard autonomous science demonstration。系统实现了 rover traverse 过程中的 closed-loop opportunistic detection and reaction，并新增 planning / scheduling、image prioritization，以及 end-of-traverse partial panorama、目标评估和高价值窄视场 follow-up imaging 等能力。文章也比较了若干 rock-property estimation methods，但在本轮冻结裁决下，最终稳定对象仍是 rover mission-science autonomy，因此维持 `10` 单模块。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确 mission-science 目标、多步决策链、工具调用、感知评估和跟进观测
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未强调
- 在科研流程中承担的明确角色：onboard science analysis、planning / scheduling、target assessment、follow-up observation

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不适用

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`10`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`10`
- 主展示模块一级类：`10` 航空、航天、海洋与交通科学
- 主展示模块二级类：`10.02` onboard rover mission-science autonomy
- 每个模块的对象实验证据：`10` 来自 FIDO rover traverse 中的 closed-loop detection and reaction、planning / scheduling、image prioritization、target assessment、follow-up imaging
- 归类理由：文章最终研究的是 onboard rover science workflow，而不是地质本体研究
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：onboard autonomous rover science workflow
- 最终科学问题：rover 如何在 traverse 中自主发现、排序并跟进高价值科学目标
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：感知算法和 rock-property estimation 只是 autonomy loop 的组成部分，主对象是 mission-science operations

### 2.3 容易混淆的边界

- 可能误归类到：`05`
- 最终判定：保持 `10`
- 判定理由：虽然文章讨论 rock properties 和 geology sensing，但冻结 landing subset 仅接受 `10`，不扩写额外模块
- 多模块覆盖说明：本轮必须遵守 adjudicated row，不新增 `05`
- 01.04 判定说明：不是领域无关 workflow paper
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

- Agent 类型：Planning Agent；Tool-using Agent；Robot / Embodied Agent；Hybrid Agent
- 科研流程角色：experiment_execution；data_analysis；evidence_assessment_and_validation；workflow_orchestration；feedback_iteration
- 自主能力：planning；tool_use；feedback_iteration；autonomous_decision_making；environment_interaction

## 4. 方法设计

- 方法动机：提高 rover 在 traverse 过程中的 onboard scientific responsiveness
- 系统流程：识别目标、排序图像、评估 targets of interest、采集 follow-up narrow-angle imagery，并在硬件与仿真中闭环执行
- 核心组件：OASIS、FIDO rover、ROAMS simulator、planning / scheduling、image prioritization、target-assessment methods

## 5. 实验与验证

- 验证方式：robotic_demonstration；simulation_validation
- 数据与任务：FIDO rover traverse autonomous science demonstration
- 关键结果：系统实现 closed-loop opportunistic detection and reaction，并加入 planning / scheduling 与 target follow-up capabilities
- 证据强度：computationally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是 geology classifier，而是 onboard rover mission-science loop
- 与同领域其他 Agent 文献的关系：是 `Woods 2009`、`Francis 2018 AEGIS` 等 rover autonomy 论文的前期关键锚点
- 主要创新点：在 rover traverse 中实现从感知到 follow-up imaging 的 closed-loop autonomous science

## 7. 局限性与风险

- 文章重点仍是 autonomy capability demonstration，而不是新的行星科学发现
- 虽涉及 rock-property estimation，但本轮 writeback 必须遵循冻结单模块 `10`
- 旧 note 若带有抽象化或边界漂移语言，本次已统一收紧到 `10` mission-science autonomy

## 8. 对综述写作的价值

- 可放入章节：`10` 航天 rover mission-science autonomy
- 可支撑论点：早期 rover science autonomy papers 的稳定对象是 mission-science operations，而非必须展开成额外地球 / 行星地质模块
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

面向 FIDO rover 的 onboard autonomous mission-science 闭环系统。

### 9.2 速记版 pipeline

1. 在 traverse 中感知场景
2. 识别并排序科学机会
3. 规划后续采样 / 成像动作
4. 评估 targets of interest
5. 采集高价值 follow-up data

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：10
覆盖模式：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
Primary module for filing：10
是否进入 01.04 存放区：否
主展示模块一级类：10
主展示模块二级类：10.02
module_assignment_evidence：FIDO rover onboard autonomous science、planning / scheduling、image prioritization、target assessment、follow-up imaging
evidence source level：first_hand_full_text; official_jpl_pdf_archived_locally_and_checked
first_hand_source_checked：official JPL PDF checked locally: Reference_PDF/10_Aerospace_Marine_and_Transportation_Sciences/Castano_2007_Onboard_Autonomous_Rover_Science.pdf
source_limited：no
confidence：high
```
