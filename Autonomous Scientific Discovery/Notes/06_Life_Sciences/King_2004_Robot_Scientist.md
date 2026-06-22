# King et al. 2004 - Functional genomic hypothesis generation and experimentation by a robot scientist

## 2026-06-22 archive sync

- Canonical PDF path: no local PDF archived in this round
- First-hand source checked this round: Nature article page + PubMed record
- PDF version: no local PDF archived in this round
- Source-limited: no
- Final adjudication: `scientific_object_modules=06`; `object_coverage_mode=single_module`; `primary_module_for_filing=06`; `general_method_bucket=none`; `confidence=high`

**论文信息**
- 标题：Functional genomic hypothesis generation and experimentation by a robot scientist
- 作者：Ross D. King et al.
- 年份：2004
- 来源 / venue：Nature
- DOI / arXiv / URL：https://doi.org/10.1038/nature02236
- PDF / 本地文件路径：本轮未归档本地 PDF
- First-hand source checked：Nature article page；PubMed record
- PDF version：no local PDF archived in this round
- Source-limited：no
- 论文类型：系统论文 / 经典 Robot Scientist
- 当前状态：confirmed core；已按 2026-06-22 adjudication 同步
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| 来源核对 | 已完成 | Nature article page; PubMed | 本轮未归档本地 PDF，但已按 Nature 发表页与 PubMed 一手记录完成核对；当前记录不属于 `source_limited` | 高 |
| Agent 纳入 | 是 | Nature article page | 自动生成假设、设计实验、执行实验并解释结果，形成重复循环 | 高 |
| 多步闭环 | 是 | Nature article page | 明确存在 repeated cycle，不是单次预测 | 高 |
| 科学对象归类 | `06` | Nature article page; PubMed | 研究 yeast gene function、deletion mutants 与芳香族氨基酸合成通路 | 高 |
| 不是 `01.04` | 是 | Nature article page | 有稳定、具体的功能基因组学对象，不是通用 autonomous science 外壳 | 高 |
| 验证方式 | 真实生物实验 / 机器人实验 | Nature article page | 真实 biological experiments 支撑系统完成 hypothesis-test cycle | 中高 |

## 0. 摘要翻译

这是经典 Robot Scientist 论文。系统自动提出解释观察现象的假设，设计检验实验，由实验机器人执行，再解释结果并剔除与数据不符的假设，然后进入下一轮循环。具体应用落在酵母功能基因组学，利用 deletion mutants 与 auxotrophic growth experiments 推断相关基因功能。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：四条最低纳入标准全部满足，而且是具身实验 Agent 的历史锚点。
- 判定置信度：高
- 在科研流程中承担的明确角色：`hypothesis_generation`; `experimental_design`; `experiment_execution`; `evidence_assessment_and_validation`
- 当前来源状态：本轮未归档本地 PDF，但已按 Nature article page 与 PubMed 完成一手核对；当前记录不属于 `source_limited`。

## 2. 科学领域归类

- scientific_object_modules: `06`
- object_coverage_mode: `single_module`
- general_method_bucket: `none`
- primary_module_for_filing: `06`
- Note path 说明：当前 note 放在 `06` 目录仅是 filing convenience，不是分类 authority。
- 最终科学研究对象：酵母基因功能、缺失突变体与代谢通路
- 最终科学问题：如何自动生成并验证 gene-function hypotheses
- 容易混淆的边界：`01.04`
- 最终判定：保持 `06`
- 判定理由：即使它是经典 Robot Scientist，也不能盖过其稳定的生命科学对象证据。
- 归类置信度：高

## 3. Agent 系统与科研流程角色

- Agent 类型标签：Planning Agent；Tool-using Agent；Robot / Embodied Agent；Hybrid Agent
- 科研流程角色：`hypothesis_generation`; `experimental_design`; `experiment_execution`; `evidence_assessment_and_validation`
- 自主能力：`planning`; `tool_use`; `feedback_iteration`; `autonomous_decision_making`; `environment_interaction`; `closed_loop_experimentation`
- 交叉属性：`computation_driven`; `data_driven`; `experiment_driven`; `robotic_platform`

## 4. 方法设计

1. 输入关于基因功能的背景观察与候选假设。
2. 选择最能区分假设的实验。
3. 由实验机器人执行 biological experiments。
4. 解释结果并淘汰不符假设。
5. 继续下一轮 hypothesis-test cycle。

## 5. 实验与验证

- 验证方式：`wet_lab_experiment`; `robotic_experiment`
- 数据、任务与指标：yeast deletion mutants 与相关代谢通路实验
- 关键结果：用真实 biological experiments 支撑自动化 hypothesis-test cycle
- 科学贡献类型：`experimental_discovery`; `system_platform`
- 证据强度：`experimentally_validated`

## 6. 与已有工作的关系

- 这是具身实验 Agent 的历史锚点之一。
- 它不是通用 autonomous science 平台噪声，而是稳定的生命科学对象论文。
- 可作为生命科学方向 Agent 谱系中的早期代表。

## 7. 局限性与风险

- 当前来源核对主要依赖 Nature article page 与 PubMed，后续如需写综述正文，可再补更细页码。
- 适用场景相对集中在特定功能基因组学任务。
- 当前记录已有足够一手证据，不属于 `source_limited`。

## 8. 对综述写作的价值

- 适合放入生命科学 / 历史锚点小节。
- 可支撑“经典 Robot Scientist 不是通用方法桶，而是稳定生命科学对象论文”这一论点。
- 推荐引用强度：core

## 9. 总结

### 9.1 一句话概括

功能基因组学中的经典 Robot Scientist 闭环。

### 9.2 速记版 pipeline

1. 生成基因功能假设
2. 设计区分性实验
3. 机器人执行实验
4. 解释结果并淘汰假设
5. 进入下一轮

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：06
object_coverage_mode：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
primary_module_for_filing：06
是否进入 01.04 存放区：否
module_assignment_evidence：yeast gene-function hypotheses, deletion-mutant experiments, and pathway-level biological validation remain concrete life-science objects
first_hand_sources_checked：Nature article page; PubMed record
classification_evidence_source_level：first_hand_abstract_or_landing_page
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：hypothesis_generation; experimental_design; experiment_execution; evidence_assessment_and_validation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：wet_lab_experiment; robotic_experiment
交叉属性：computation_driven; data_driven; experiment_driven; robotic_platform
科学贡献类型：experimental_discovery; system_platform
证据强度：experimentally_validated
归类置信度：high
纳入置信度：high
推荐引用强度：core
```
