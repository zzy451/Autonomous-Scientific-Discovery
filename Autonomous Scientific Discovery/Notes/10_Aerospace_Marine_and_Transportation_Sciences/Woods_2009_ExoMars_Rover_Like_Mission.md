# Woods et al. 2009 - Autonomous science for an ExoMars Rover-like mission

**论文信息**
- 标题：Autonomous science for an ExoMars Rover-like mission
- 作者：Mark Woods; Andy Shaw; Dave Barnes; David Ernest Price; Derek Long; Derek Pullan
- 年份：2009
- 来源 / venue：Journal of Field Robotics
- DOI / arXiv / URL：https://doi.org/10.1002/rob.20289
- PDF / 本地文件路径：`Reference_PDF/10_Aerospace_Marine_and_Transportation_Sciences/Woods_2009_ExoMars_Rover_Like_Mission.pdf`
- 论文类型：研究论文 / rover mission-science autonomy system
- 当前状态：to_read（note 已按 Batch29Partial1 writeback 更新）
- 阅读日期：2026-06-24
- 笔记作者：Codex

## 2026-06-24 Batch29Partial1 writeback / full reaudit

- final supported_modules：`05;10`
- primary_module_for_filing：`10`
- object_coverage_mode：`multi_module`
- final_01_04_bucket：`none`
- source_limited：`no`
- safety_access_status：`accessed_no_safety_issue`
- evidence source level：`first_hand_full_text; repository_pdf_archived_locally_and_checked; publisher_abstract_checked`
- first-hand source checked：`repository PDF checked locally: Reference_PDF/10_Aerospace_Marine_and_Transportation_Sciences/Woods_2009_ExoMars_Rover_Like_Mission.pdf`；original repository source `https://pure.aber.ac.uk/ws/files/99154/fulltext.pdf`；Wiley abstract cross-checked
- note_revision_required：`yes`
- adjudication confidence：`medium`
- final_reason：Mission-science rover autonomy is primary (`10`), while geological-feature scoring and field-science assessment provide explicit additional `05` evidence.

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Introduction | 论文为 ExoMars-like mission 设计 autonomous, opportunistic science concept，包含 science target selection 与 active data acquisition。 | 高 |
| `10` 模块证据 | 强支持 | Introduction | 核心目标是提高 rover mission science return，在 representative robotic platform 上演示 autonomous science concept。 | 高 |
| `05` 模块证据 | 支持 | 方法部分 | scientific autonomy 方法明确建立在 human geological field practice 之上，并对 complex geological features 做识别、分类、关联和尺度重评估。 | 中高 |
| 验证方式 | 机器人平台演示 + assessment methodology | Introduction；方法部分 | 论文强调 autonomous science assessment methodology，并在 ExoMars rover-like platform 上集成多项 autonomy components。 | 中高 |
| 边界判断 | `10` 为主，显式补记 `05` | object-first reading | 文章主轴不是行星地质本体研究，而是 mission-science autonomy；但 geological-feature assessment 不是仅仅背景叙事，足以触发 `05` 共覆盖。 | 中高 |

## 0. 摘要翻译

论文面向 ExoMars Rover-like mission 讨论 autonomous science，指出仅依赖地面指挥会降低科学探索响应速度和 science return，因此需要在 rover 平台上部署 science target selection 与 active data acquisition 的自主系统。作者在代表性 robotic platform 上演示了 autonomous opportunistic science concept，并进一步提出一种基于 terrestrial geological field practice 的 autonomous science assessment methodology。由此，本轮冻结裁决将该文写为 `05;10`：`10` 表示 mission-science rover autonomy 主对象，`05` 表示明确存在的 geological field-science object coverage。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确科学任务目标，具有多步 target selection、active data acquisition、自主评估与响应流程
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未强调
- 在科研流程中承担的明确角色：mission-science planning、target selection、data acquisition、field-science assessment

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不适用

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`05;10`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`10`
- 主展示模块一级类：`10` 航空、航天、海洋与交通科学
- 主展示模块二级类：`10.02` rover mission-science autonomy
- 其他覆盖模块及对应层级路径：`05` geological field-science assessment
- 每个模块的对象实验证据：
  - `10`：science return、science target selection、active data acquisition、representative robotic platform
  - `05`：human geological field practice、complex geological feature recognition / classification / association、autonomous target identification with additional data analysis
- 归类理由：论文的主对象是 ExoMars-like rover mission-science autonomy，但 geological assessment 不是纯背景，构成明确 field-science object coverage
- 归类置信度：中

### 2.2 对象优先判定

- 最终科学研究对象：ExoMars rover-like mission autonomy 与其中的 geological field-science target assessment
- 最终科学问题：如何在 rover mission 中实现 opportunistic science、提高 science return，并以 geological practice 指导自主评估
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：机器人 / autonomy stack 只是实现形式，分类事实来自 mission-science object 与 geological field-science object

### 2.3 容易混淆的边界

- 可能误归类到：仅保留 `10`，或只看 planetary geology 而压到 `05`
- 最终判定：`10` 为主，显式补记 `05`
- 判定理由：mission-science autonomy 是稳定主轴；但文中对 geological feature assessment 与 field-practice methodology 的投入足以支持 `05`
- 多模块覆盖说明：保留 `10` 作为 filing convenience，不覆盖 `05` 共覆盖事实
- 01.04 判定说明：不是领域无关 scientific workflow
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

- Agent 类型：Planning Agent；Tool-using Agent；Robot / Embodied Agent；Hybrid Agent
- 科研流程角色：experimental_design；experiment_execution；data_analysis；evidence_assessment_and_validation；workflow_orchestration
- 自主能力：planning；tool_use；feedback_iteration；autonomous_decision_making；environment_interaction

## 4. 方法设计

- 方法动机：降低通信延迟和人工监督对 rover mission science responsiveness 的限制
- 系统流程：在 rover-like platform 上执行 science target selection、active data acquisition、opportunistic response 和 autonomous science assessment
- 核心组件：rover autonomy components、science target-selection mechanism、field-science assessment methodology、additional data-acquisition loop

## 5. 实验与验证

- 验证方式：robotic_demonstration；methodology_assessment
- 数据与任务：ExoMars rover-like mission task；autonomous opportunistic science；geological feature evaluation
- 关键结果：系统在 representative robotic platform 上演示 autonomous opportunistic science concept，并提出面向 geological assessment 的自主评价方法
- 证据强度：simulation_supported

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 geology classifier，而是 mission-science rover autonomy system
- 与同领域其他 Agent 文献的关系：可与 `Castano 2007 OASIS`、`Francis 2018 AEGIS` 等构成 rover autonomy lineage
- 主要创新点：将 rover mission autonomy 与 geological field-practice-based science assessment 紧密耦合

## 7. 局限性与风险

- 主体仍是 platform / mission concept demonstration，不是直接新的行星地质发现
- `05` 证据来自 geological assessment methodology，而非独立地球科学 benchmark 体系，因此整体置信度保持 `medium`
- 旧 note 若只保留 `10`，本次已按冻结裁决显式补写 `05`

## 8. 对综述写作的价值

- 可放入章节：`10` mission-science rover autonomy，并在 `05/10` 边界表中列为代表例
- 可支撑论点：mission-science autonomy papers 可以同时包含 field-science object coverage，不必强迫写成单模块
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

一个以 ExoMars rover mission-science autonomy 为主、并显式包含 geological field-science assessment 的早期自主科学系统。

### 9.2 速记版 pipeline

1. 识别 mission science opportunity
2. 自主选取科学目标
3. 主动获取补充数据
4. 依据 geological practice 评估目标
5. 提升 rover science return

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：05;10
覆盖模式：multi_module
是否具有具体科学对象实验：是
general_method_bucket：none
Primary module for filing：10
是否进入 01.04 存放区：否
主展示模块一级类：10
主展示模块二级类：10.02
其他覆盖模块及对应层级路径：05 geological field-science assessment
module_assignment_evidence：10 来自 science return / target selection / active data acquisition 的 rover mission object；05 来自 geological feature recognition、classification 与 field-practice-based assessment
multi_module_object_coverage_note：保持 10 为 primary filing，但显式写回 geological field-science 带来的 05 共覆盖
evidence source level：first_hand_full_text; repository_pdf_archived_locally_and_checked; publisher_abstract_checked
first_hand_source_checked：repository PDF checked locally: Reference_PDF/10_Aerospace_Marine_and_Transportation_Sciences/Woods_2009_ExoMars_Rover_Like_Mission.pdf
source_limited：no
confidence：medium
```
