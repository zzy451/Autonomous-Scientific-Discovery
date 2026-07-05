# Granda et al. 2018 - Controlling an organic synthesis robot with machine learning to search for new reactivity

## Phase6FollowupR21 Frozen Adjudication

- `paper_id`: `ASD-0734`
- Frozen adjudicated modules: `03`
- `primary_module_for_filing`: `03`
- Canonical local archived PDF: `Reference_PDF/03_Chemical_Sciences/Granda_2018_Organic_Synthesis_Robot_Reactivity.pdf`
- `first_hand_sources_checked`: local archived PDF full text (`Reference_PDF/03_Chemical_Sciences/Granda_2018_Organic_Synthesis_Robot_Reactivity.pdf`)
- `classification_evidence_source_level`: `first_hand_full_text`
- `source_limited`: `no`
- Filing note: note location is filing convenience only and does not override the frozen module-`03` adjudication.

**论文信息**
- 标题：Controlling an organic synthesis robot with machine learning to search for new reactivity
- 作者：Jarosław M. Granda; Liva Donina; Vincenza Dragone; De-Liang Long; Leroy Cronin
- 年份：2018
- 来源 / venue：Nature
- DOI / arXiv / URL：https://doi.org/10.1038/s41586-018-0307-8
- PDF / 本地文件路径：`Reference_PDF/03_Chemical_Sciences/Granda_2018_Organic_Synthesis_Robot_Reactivity.pdf`；本轮已核对本地归档 PDF 全文，对应 DOI `10.1038/s41586-018-0307-8`
- 论文类型：研究论文 / organic-reactivity discovery robot
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| 一手来源与归档状态 | 已核对本地归档 PDF 全文 | local archived PDF full text | 本轮冻结裁决使用 `Reference_PDF/03_Chemical_Sciences/Granda_2018_Organic_Synthesis_Robot_Reactivity.pdf` 作为一手全文来源 | 高 |
| Agent 纳入 | 是 | local archived PDF full text | synthesis robot can perform reactions and analysis, predict reactivity, navigate reaction space, and follow up discoveries | 高 |
| 科学对象归类 | `03.03` | title / Nature abstract / Crossref | 对象是 chemical reaction space 与 new reactivity discovery，而不是 materials property space | 高 |
| 方法流程 | experiments -> real-time analysis -> ML decision -> follow-up | local archived PDF full text | 系统实时用 NMR / IR 反馈驱动决策并探索反应空间 | 高 |
| 边界判断 | 不应改到 `04` | object-first rule | 重点是 reaction combinations 与 new reactions 的发现，不是材料性能优化 | 高 |
| 实验验证 | discovered four reactions | RePEc abstract line 76 | 由机器学习预测后，化学家跟进发现四个反应 | 高 |

## 0. 摘要翻译

这篇论文提出一个有机合成机器人，能够执行化学反应、实时分析实验结果，并在做了少量实验之后预测更多试剂组合的反应性，从而探索化学反应空间。系统利用实时 NMR 和红外光谱结果驱动机器学习决策，并最终导向新的反应发现。由于它的核心对象是有机反应空间和 reactivity discovery，而不是某类材料性能，因此更适合稳定归入 `03.03`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统具有实验执行、实时分析、反馈驱动决策和后续实验选择
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：实验设计、实验执行、结果分析、反应发现

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：03
- 二级类：03.03
- 三级类：organic reactivity discovery / reaction-space exploration
- 四级专题：Autonomous organic-synthesis reactivity-discovery systems
- 四级专题是否为新增：否
- 归类理由：系统直接在化学反应空间中搜索新反应性，科学对象就是 chemical reactivity
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：reaction combinations, reaction space, new chemical reactivity
- 最终科学问题：如何用闭环机器人更高效发现新的有机反应性
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：机器学习和机器人只是手段，稳定对象仍是 chemistry reaction discovery

### 2.3 容易混淆的边界

- 可能误归类到：04
- 最终判定：保持 03.03
- 判定理由：如果终点是量子点、聚合物或功能材料性能优化，应倾向 04；本文终点是 new reactivity discovery
- 是否需要二次复核：需要全文补更细实验细节，但主类稳定

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
- 其他：reaction-space exploration robot

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：是
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：是
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
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：否
- 多模态：是
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：real-time NMR and IR

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：提升 reaction-space exploration 的效率并发现新反应性
- 现有科研流程或方法的痛点：人工探索化学反应空间慢且覆盖有限
- 核心假设或直觉：用少量实验训练的机器学习系统可以引导机器人在高维 reaction space 中快速搜索

### 4.2 系统流程

1. 输入：候选试剂组合与反应空间
2. 任务分解 / 规划：机器人选择待测反应组合
3. 工具、数据库、模型或实验平台调用：执行反应并用 NMR / IR 实时分析
4. 中间结果反馈：将分析结果送回机器学习系统
5. 决策或迭代：预测未测组合的反应性并安排后续实验
6. 输出：new reactions / reactivity discoveries

### 4.3 系统组件

- Agent 核心：organic synthesis robot + machine learning decision module
- 工具 / API / 数据库：real-time NMR, IR spectroscopy
- 记忆或状态模块：tested reaction outcomes
- 规划器：ML-based reactivity prediction
- 评估器 / verifier：real-time reaction analysis
- 人类反馈或专家介入：发现后的 manual chemist follow-up
- 实验平台或仿真环境：organic synthesis robot platform

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：否
- 高通量计算：否
- 机器人实验：是
- 湿实验：是
- 临床数据：否
- 真实场景部署：否
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：about 1,000 reaction combinations
- 任务设置：predicting and exploring reactivity in chemical reaction space
- 对比基线：manual execution and prior published datasets
- 评价指标：reactivity prediction accuracy and downstream discovery value
- 关键结果：在略多于 10% 数据后即可对约 1,000 组合达到 80% 以上准确率，并导向四个反应发现
- 是否有消融实验：当前笔记未展开
- 是否有失败案例或负结果：未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，直接导向新反应发现
- 科学贡献是否经过验证：是
- 贡献强度判断：高
- 科学贡献类型：experimental_discovery; chemical_reactivity_discovery
- 证据强度：high_primary_article

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是离线 reaction prediction，而是闭环机器人探索反应空间
- 与已有 Agent / 科研智能系统的区别：较早期地把实时表征、ML 决策和实验执行打通
- 与同一科学领域其他 Agent 文献的关系：可与 Ha_2023_Robotic_Chemist_Organic_Molecules 及后续 closed-loop chemistry agents 并列
- 主要创新点：用机器人和在线分析主动搜索 new reactivity

## 7. 局限性与风险

- Agent 自主性不足：最终新反应确认仍有人工 follow-up
- 科学验证不足：更细机制解释需要全文补充
- 泛化性不足：对其他 reaction families 的迁移边界需要进一步核实
- 工具链依赖：高度依赖实验机器人与在线表征
- 数据泄漏或 benchmark 偏差：当前证据不足以细评
- 成本、可复现性或安全风险：实验平台复现门槛较高

## 8. 对综述写作的价值

- 可放入哪个章节：03 化学科学中的 autonomous reaction discovery
- 可支撑哪个论点：`03 / 04` 边界应按最终对象判断，反应性发现不应因机器人平台而误归材料类
- 可用于哪个表格或图：`03.03 / 04` 边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：后续读全文补充
- 需要与哪些论文并列比较：Ha_2023_Robotic_Chemist_Organic_Molecules; StriethKalthoff_2024_Organic_Laser_Emitters

## 9. 总结

### 9.1 一句话概括

闭环有机合成机器人在反应空间中搜索并发现新反应性。

### 9.2 速记版 pipeline

1. 选择试剂组合
2. 机器人执行并在线分析
3. 机器学习预测更多组合
4. 跟进发现新反应

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：03
二级类：03.03
三级类：organic reactivity discovery / reaction-space exploration
四级专题：Autonomous organic-synthesis reactivity-discovery systems
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：hypothesis_generation; experimental_design; experiment_execution; data_analysis; evidence_assessment_and_validation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：robotic_experiment; wet_lab_experiment; closed_loop_experiment
交叉属性：computation_driven; data_driven; experiment_driven; multimodal; high_throughput_screening; robotic_platform
科学贡献类型：experimental_discovery; chemical_reactivity_discovery
证据强度：high_primary_article
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
## 2026-06-24 writeback adjudication

- `scientific_object_modules`: `03`
- `object_coverage_mode`: `single_module`
- `primary_module_for_filing`: `03`
- `general_method_bucket`: `none`
- `first_hand_sources_checked`: local archived PDF full text (`Reference_PDF/03_Chemical_Sciences/Granda_2018_Organic_Synthesis_Robot_Reactivity.pdf`)
- `classification_evidence_source_level`: `first_hand_full_text`
- `source_limited`: `no`
- `note_revision_required`: `no`

This writeback keeps the reaction-discovery framing explicit: the robot is used to explore organic reaction space and discover new reactivity, not to optimize a materials-property endpoint.
