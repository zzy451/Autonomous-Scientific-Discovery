# MacLeod et al. 2020 - Self-driving laboratory for accelerated discovery of thin-film materials

## 2026-06-22 archive sync

- Canonical PDF path: no local PDF archived in this round
- First-hand source checked this round: arXiv full text
- PDF version: no local PDF; first-hand arXiv full text checked
- Source-limited: no
- Final adjudication: `scientific_object_modules=04`; `object_coverage_mode=single_module`; `primary_module_for_filing=04`; `general_method_bucket=none`; `confidence=high`

**论文信息**
- 标题：Self-driving laboratory for accelerated discovery of thin-film materials
- 作者：MacLeod et al.
- 年份：2020
- 来源 / venue：Science Advances
- DOI / arXiv / URL：https://doi.org/10.1126/sciadv.aaz8867
- PDF / 本地文件路径：本轮未归档本地 PDF；已核对 arXiv 全文
- First-hand source checked：arXiv full text
- PDF version：no local PDF; first-hand arXiv full text checked
- Source-limited：no
- 论文类型：研究论文 / self-driving materials lab
- 当前状态：confirmed core；已按 2026-06-22 adjudication 同步
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| 来源核对 | 已完成 | arXiv full text | 本轮未归档本地 PDF，但已按 arXiv 全文完成一手核对；当前记录不属于 `source_limited` | 高 |
| Agent 纳入 | 是 | arXiv full text | 平台 iteratively designs, executes, and learns from experiments in a fully autonomous loop | 高 |
| 科学对象归类 | `04` | arXiv full text | 研究对象是 thin-film materials 及相关 optoelectronic properties | 高 |
| 方法流程 | 自主实验闭环 | arXiv full text | 混料、制膜、表征、建模、选点构成完整循环 | 高 |
| 实验验证 | 真实材料实验 | arXiv full text | Ada / ChemOS / Phoenics 通过真实材料实验完成闭环优化 | 高 |
| 边界判断 | 保持 `04` | arXiv full text | 贡献落在具体薄膜材料发现，而不是通用 orchestration 平台 | 高 |

## 0. 摘要翻译

这篇工作是自驱实验室文献中的经典代表。系统在真实实验环境中自动完成混料、制膜、表征、建模和下一轮实验选择，加速薄膜材料发现。由于对象是具体薄膜材料及其性质，而不是通用科研基础设施，因此应稳定保留在材料科学。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多步实验闭环、自动实验执行、反馈建模与自主决策。
- 判定置信度：高
- 在科研流程中承担的明确角色：`experimental_design`; `experiment_execution`; `data_analysis`; `feedback_iteration`
- 当前来源状态：本轮未归档本地 PDF；已按 arXiv 全文完成一手核对。当前记录不属于 `source_limited`。

## 2. 科学领域归类

- scientific_object_modules: `04`
- object_coverage_mode: `single_module`
- general_method_bucket: `none`
- primary_module_for_filing: `04`
- Note path 说明：当前 note 放在 `04` 目录仅是 filing convenience，不是分类 authority。
- 最终科学研究对象：薄膜材料及其 optical / electronic properties
- 最终科学问题：如何在真实实验环境中自主优化薄膜材料搜索
- 容易混淆的边界：`01.04`
- 最终判定：保持 `04`
- 判定理由：实验与科学贡献都落在具体薄膜材料对象上，而不是通用实验 orchestration。
- 归类置信度：高

## 3. Agent 系统与科研流程角色

- Agent 类型标签：Robot / Embodied Agent；Planning Agent；Hybrid Agent
- 科研流程角色：`experimental_design`; `experiment_execution`; `data_analysis`; `feedback_iteration`
- 自主能力：`planning`; `tool_use`; `feedback_iteration`; `autonomous_decision_making`; `closed_loop_experimentation`
- 交叉属性：`experiment_driven`; `robotic_platform`; `high_throughput_screening`

## 4. 方法设计

1. 系统选择下一批材料实验。
2. 自动混料、制膜和表征。
3. 根据测量结果更新模型。
4. 再次选择更优实验点。
5. 输出更优的薄膜材料候选。

## 5. 实验与验证

- 验证方式：`robotic_experiment`
- 数据、任务与指标：薄膜材料发现与 optoelectronic 性能优化
- 关键结果：形成 fully autonomous loop 并显著加速薄膜材料搜索
- 科学贡献类型：`experimental_optimization`; `system_platform`
- 证据强度：`experimentally_validated`

## 6. 与已有工作的关系

- 是材料类 self-driving labs 的 canonical record。
- 与一般材料信息学不同，这里是完整实验闭环而非离线预测。
- 可作为 `04` 类 confirmed-core 的核心代表样本。

## 7. 局限性与风险

- 后续仍可补更细的材料家族和设备细节。
- 主要风险不在主类，而在后续与其他材料 SDL 的纵向比较。
- 当前记录已有一手全文支撑，不属于 `source_limited`。

## 8. 对综述写作的价值

- 适合放入材料 self-driving laboratory 代表案例部分。
- 可支撑“真实实验闭环已在材料发现中形成稳定范式”这一论点。
- 推荐引用强度：core

## 9. 总结

### 9.1 一句话概括

自驱实验室在真实环境中加速薄膜材料发现。

### 9.2 速记版 pipeline

1. 选实验
2. 自动制备
3. 自动表征
4. 更新模型
5. 再选下一轮

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：04
object_coverage_mode：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
primary_module_for_filing：04
是否进入 01.04 存放区：否
module_assignment_evidence：thin-film materials discovery and property optimization remain concrete materials-object experiments
first_hand_sources_checked：arXiv full text
classification_evidence_source_level：first_hand_full_text
Agent 类型：Robot / Embodied Agent; Planning Agent; Hybrid Agent
科研流程角色：experimental_design; experiment_execution; data_analysis; feedback_iteration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; closed_loop_experimentation
验证方式：robotic_experiment
交叉属性：experiment_driven; robotic_platform; high_throughput_screening
科学贡献类型：experimental_optimization; system_platform
证据强度：experimentally_validated
归类置信度：high
纳入置信度：high
推荐引用强度：core
```
