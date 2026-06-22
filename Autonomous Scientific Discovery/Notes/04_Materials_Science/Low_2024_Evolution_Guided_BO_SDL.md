# Low 2024 - Evolution-guided Bayesian optimization for constrained multi-objective optimization in self-driving labs

## 2026-06-22 archive sync

- Canonical PDF path: `Reference_PDF/04_Materials_Science/Low_2024_Evolution_Guided_BO_SDL.pdf`
- First-hand source checked this round: local archived full text
- PDF version: archived publisher PDF
- Source-limited: no
- Final adjudication: `scientific_object_modules=04`; `object_coverage_mode=single_module`; `primary_module_for_filing=04`; `general_method_bucket=none`; `confidence=high`

**论文信息**
- 标题：Evolution-guided Bayesian optimization for constrained multi-objective optimization in self-driving labs
- 作者：Andre K. Y. Low et al.
- 年份：2024
- 来源 / venue：npj Computational Materials
- DOI / arXiv / URL：https://doi.org/10.1038/s41524-024-01274-x
- PDF / 本地文件路径：`Reference_PDF/04_Materials_Science/Low_2024_Evolution_Guided_BO_SDL.pdf`
- First-hand source checked：local archived full text
- PDF version：archived publisher PDF
- Source-limited：no
- 论文类型：研究论文 / 自驱实验室优化论文
- 当前状态：confirmed core；已按 2026-06-22 adjudication 同步
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| PDF 归档与来源核对 | 已完成 | local archived full text | 已核对本地归档 PDF；当前记录不属于 `source_limited` | 高 |
| Agent 纳入 | 是 | local archived full text | self-driving lab with closed-loop optimization | 高 |
| 科学对象归类 | `04` | local archived full text | seed-mediated silver nanoparticle synthesis with optical targets | 高 |
| 方法流程 | 多步闭环 | local archived full text | algorithm proposes conditions, lab executes, spectra feed back | 高 |
| 实验验证 | 真实 SDL | local archived full text | custom self-driving lab for AgNP synthesis | 高 |
| 边界判断 | `04` 稳于 `03/01.04` | local archived full text | 终点是 AgNP 材料对象与其光学表现，而不是通用优化框架 | 高 |

## 0. 摘要翻译

论文提出一种 evolution-guided Bayesian optimization 方法，并部署到定制的 self-driving lab 中，用于 seed-mediated silver nanoparticle synthesis 的约束多目标优化。系统闭环优化的直接对象是 AgNP 产物及其光学响应、反应速度与种子消耗，因此按对象优先应保留在 `04`。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：存在算法提议、实验执行、结果回传与闭环更新。
- 判定置信度：高
- 在科研流程中承担的明确角色：`experimental_design`; `simulation_modeling`; `tool_use_and_code_execution`; `experiment_execution`; `data_analysis`; `evidence_assessment_and_validation`
- 当前来源状态：本轮已核对本地归档全文；当前记录不属于 `source_limited`。

## 2. 科学领域归类

- scientific_object_modules: `04`
- object_coverage_mode: `single_module`
- general_method_bucket: `none`
- primary_module_for_filing: `04`
- Note path 说明：当前 note 放在 `04` 目录仅是 filing convenience，不是分类 authority。
- 最终科学研究对象：银纳米颗粒合成及其光学性质优化
- 最终科学问题：如何在约束条件下自动优化 AgNP synthesis outcome
- 容易混淆的边界：`03`; `01.04`
- 最终判定：保持 `04`
- 判定理由：虽然涉及合成条件，但论文真正优化的是 AgNP 材料产物表现，而不是新反应机理或通用 workflow。
- 归类置信度：高

## 3. Agent 系统与科研流程角色

- Agent 类型标签：Planning Agent；Tool-using Agent；Robot / Embodied Agent；Hybrid Agent
- 科研流程角色：`experimental_design`; `simulation_modeling`; `tool_use_and_code_execution`; `experiment_execution`; `data_analysis`; `evidence_assessment_and_validation`
- 自主能力：`planning`; `tool_use`; `memory_or_state_tracking`; `feedback_iteration`; `autonomous_decision_making`; `environment_interaction`; `closed_loop_experimentation`
- 交叉属性：`computation_driven`; `data_driven`; `experiment_driven`; `simulation_driven`; `robotic_platform`

## 4. 方法设计

1. 设定 AgNP 优化目标和约束。
2. BO 提议下一组实验条件。
3. 微流控实验与光谱测量执行实验。
4. 将结果反馈给优化器。
5. 继续闭环搜索更优材料表现。

## 5. 实验与验证

- 验证方式：`simulation_validation`; `robotic_experiment`; `wet_lab_experiment`; `real_world_deployment`
- 数据、任务与指标：silver nanoparticle synthesis under constrained multi-objective optimization
- 关键结果：在 SDL 中实现稳定的 constrained optimization
- 科学贡献类型：`experimental_optimization`
- 证据强度：`experimentally_validated`

## 6. 与已有工作的关系

- 不是离线优化，而是完整的闭环 SDL。
- 可作为 `03/04` 边界样本，展示“涉及合成条件”不等于必须归化学。
- 可与其他 nanoparticle / materials SDL 工作并列比较。

## 7. 局限性与风险

- 对象主要集中在单一 AgNP 场景。
- 主要风险在泛化范围，而不是对象模块误判。
- 当前已有一手全文支撑，不属于 `source_limited`。

## 8. 对综述写作的价值

- 适合放入材料科学中的 nanoparticle SDL 小节。
- 可支撑“03/04 边界应按最终材料对象而不是是否涉及合成条件来判定”的论点。
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

面向银纳米颗粒材料优化的自驱实验室闭环系统。

### 9.2 速记版 pipeline

1. 设定 AgNP 目标
2. BO 提议条件
3. 执行实验
4. 回传光谱结果
5. 继续搜索

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：04
object_coverage_mode：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
primary_module_for_filing：04
是否进入 01.04 存放区：否
module_assignment_evidence：seed-mediated silver nanoparticle synthesis and optical-target optimization remain concrete materials-object experiments
first_hand_sources_checked：local archived full text
classification_evidence_source_level：first_hand_full_text
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：experimental_design; simulation_modeling; tool_use_and_code_execution; experiment_execution; data_analysis; evidence_assessment_and_validation
自主能力：planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：simulation_validation; robotic_experiment; wet_lab_experiment; real_world_deployment
交叉属性：computation_driven; data_driven; experiment_driven; simulation_driven; robotic_platform
科学贡献类型：experimental_optimization
证据强度：experimentally_validated
归类置信度：high
纳入置信度：high
推荐引用强度：standard
```
