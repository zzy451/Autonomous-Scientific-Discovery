# Gongora et al. 2020 - A Bayesian experimental autonomous researcher for mechanical design

## 2026-06-22 archive sync

- Canonical PDF path: no local PDF archived in this round
- First-hand source checked this round: PMC full text
- PDF version: no local PDF; first-hand PMC full text checked
- Source-limited: no
- Final adjudication: `scientific_object_modules=09`; `object_coverage_mode=single_module`; `primary_module_for_filing=09`; `general_method_bucket=none`; `confidence=high`

**论文信息**
- 标题：A Bayesian experimental autonomous researcher for mechanical design
- 作者：Gongora et al.
- 年份：2020
- 来源 / venue：Science Advances
- DOI / arXiv / URL：https://doi.org/10.1126/sciadv.aaz1708
- PDF / 本地文件路径：本轮未归档本地 PDF；已核对 PMC 全文
- First-hand source checked：PMC full text
- PDF version：no local PDF; first-hand PMC full text checked
- Source-limited：no
- 论文类型：研究论文 / autonomous mechanical-design researcher
- 当前状态：confirmed core；已按 2026-06-22 adjudication 同步
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| 来源核对 | 已完成 | PMC full text | 本轮未归档本地 PDF，但已按 PMC 全文完成一手核对；当前记录不属于 `source_limited` | 高 |
| Agent 纳入 | 是 | PMC full text | 系统将 Bayesian optimization 与自动实验结合，自主决定后续实验 | 高 |
| 科学对象归类 | `09` | PMC full text | 研究对象是机械设计与 additive-manufacturing structures 的 toughness 优化 | 高 |
| 方法流程 | 自动实验闭环 | PMC full text | 自动打印、自动测试、模型更新和再选样构成闭环 | 高 |
| 实验验证 | 真实实验 | PMC full text | 相比网格搜索显著减少实验次数，并基于真实打印测试循环优化 | 高 |
| 边界判断 | 不应归 `01.04` | PMC full text | 科学对象是具体机械结构设计，而不是通用 research-agent platform | 高 |

## 0. 摘要翻译

BEAR 将 Bayesian optimization 与高通量自动实验结合起来，用于机械设计问题中的结构 toughness 优化。系统能够自主打印、测试并根据结果决定下一轮实验。由于它直接研究的是机械结构设计对象，因此应稳定放在工程与工业技术科学，而不是通用科研 Agent 类。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多步实验流程、反馈驱动决策与自动实验执行。
- 判定置信度：高
- 在科研流程中承担的明确角色：`experimental_design`; `simulation_modeling`; `data_analysis`; `feedback_iteration`
- 当前来源状态：本轮未归档本地 PDF；已按 PMC 全文完成一手核对。当前记录不属于 `source_limited`。

## 2. 科学领域归类

- scientific_object_modules: `09`
- object_coverage_mode: `single_module`
- general_method_bucket: `none`
- primary_module_for_filing: `09`
- Note path 说明：当前 note 放在 `09` 目录仅是 filing convenience，不是分类 authority。
- 最终科学研究对象：机械结构与 additive manufacturing design optimization
- 最终科学问题：如何通过自主实验系统高效优化机械设计
- 容易混淆的边界：`01.04`
- 最终判定：保持 `09`
- 判定理由：对象是具体工程结构与制造设计，而不是通用科研流程平台。
- 归类置信度：高

## 3. Agent 系统与科研流程角色

- Agent 类型标签：Planning Agent；Hybrid Agent
- 科研流程角色：`experimental_design`; `simulation_modeling`; `data_analysis`; `feedback_iteration`
- 自主能力：`planning`; `feedback_iteration`; `autonomous_decision_making`; `closed_loop_experimentation`
- 交叉属性：`experiment_driven`; `high_throughput_screening`

## 4. 方法设计

1. 系统提出新的机械设计实验点。
2. 自动打印并测试样件。
3. 汇总 toughness 等结果。
4. 更新 BO 模型后选择下一轮实验。
5. 输出更优的机械设计。

## 5. 实验与验证

- 验证方式：`simulation_validation`
- 数据、任务与指标：additive-manufacturing mechanical-design tasks
- 关键结果：以更少实验实现更高效的机械设计搜索
- 科学贡献类型：`experimental_optimization`; `system_platform`
- 证据强度：`experimentally_validated`

## 6. 与已有工作的关系

- 与一般 engineering optimization 不同，这里是自主实验闭环。
- 与通用 `01.04` scientific workflow 不同，对象明确锚定机械结构设计。
- 可与其他 `09` 类工程 Agent 形成对象链条。

## 7. 局限性与风险

- 后续仍可补更细的制造工艺细节。
- 主要风险不在对象模块，而在 `09` 内部更细粒度比较。
- 当前记录已有一手全文支撑，不属于 `source_limited`。

## 8. 对综述写作的价值

- 适合放入工程设计型闭环 Agent 小节。
- 可支撑“Agent 已进入真实机械设计实验闭环”这一论点。
- 推荐引用强度：core

## 9. 总结

### 9.1 一句话概括

自主实验系统通过 BO 优化机械结构设计。

### 9.2 速记版 pipeline

1. 选设计点
2. 自动打印和测试
3. 汇总结果
4. 更新模型
5. 再选下一轮

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：09
object_coverage_mode：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
primary_module_for_filing：09
是否进入 01.04 存放区：否
module_assignment_evidence：mechanical-design optimization and additive-manufacturing structure evaluation remain concrete engineering objects
first_hand_sources_checked：PMC full text
classification_evidence_source_level：first_hand_full_text
Agent 类型：Planning Agent; Hybrid Agent
科研流程角色：experimental_design; simulation_modeling; data_analysis; feedback_iteration
自主能力：planning; feedback_iteration; autonomous_decision_making; closed_loop_experimentation
验证方式：simulation_validation
交叉属性：experiment_driven; high_throughput_screening
科学贡献类型：experimental_optimization; system_platform
证据强度：experimentally_validated
归类置信度：high
纳入置信度：high
推荐引用强度：core
```
