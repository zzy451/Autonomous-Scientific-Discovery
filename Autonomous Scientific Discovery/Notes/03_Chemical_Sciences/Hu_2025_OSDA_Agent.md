# Hu et al. 2025 - OSDA agent: Leveraging large language models for de novo design of organic structure directing agents

**论文信息**
- 标题：OSDA agent: Leveraging large language models for de novo design of organic structure directing agents
- 作者：Hu et al.
- 年份：2025
- 来源 / venue：ICLR / OpenReview
- DOI / URL：https://openreview.net/forum?id=9YNyiCJE3k
- PDF / 本地文件路径：`Reference_PDF/03_Chemical_Sciences/Hu_2025_OSDA_Agent.pdf`
- First-hand source checked：OpenReview 页面；official OpenReview PDF
- PDF version：official OpenReview PDF
- Source-limited：no
- 当前状态：confirmed core；当前落地为 relaxed multi-module `03;04`，主归档模块为 `03`

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| PDF 归档与来源核对 | 已完成 | OpenReview 页面；official PDF | 当前使用官方 OpenReview PDF 作为规范版本 | 高 |
| Agent 纳入 | 是 | 摘要；方法与结果部分 | 系统围绕明确科研目标组织多步设计、评估与反馈迭代流程 | 高 |
| 化学科学覆盖 | `03` | 官方 PDF | 直接设计对象是 organic structure-directing agents 分子家族，化学分子设计属性稳定成立 | 高 |
| 材料科学覆盖 | `04` | 官方 PDF | 论文同时围绕 OSDA-zeolite compatibility、host-guest / binding 与 zeolite-related validation 展开，构成材料对象 add-on 证据 | 高 |
| `01.04` 存放区判断 | `none` | 官方 PDF | 论文包含具体化学与材料对象验证，不是独立通用方法记录 | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- 判断依据：系统包含规划、工具调用、候选生成、评估与反馈迭代等多步研究动作。
- 纳入置信度：高。

## 2. 科学领域归类

- scientific_object_modules：`03;04`
- object_coverage_mode：`multi_module`
- general_method_bucket：`none`
- primary_module_for_filing：`03`
- 归类理由：
  - `03`：直接搜索与优化对象是 OSDA 分子。
  - `04`：zeolite-material compatibility / binding validation 使材料模块覆盖成立。
- 边界说明：主文件夹仍保留在化学目录下，但这只是归档锚点，不应再把该文写成纯 `03` 单模块记录。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Hybrid Agent。
- 科研流程角色：molecular_design；tool_use_and_code_execution；evidence_assessment_and_validation。
- 自主能力：planning；tool_use；feedback_iteration；autonomous_decision_making；multi_agent_collaboration。

## 4. 方法设计

1. 输入研究问题与结构导向剂设计目标。
2. 组织多步候选生成与筛选。
3. 调用外部评估工具与相关知识资源。
4. 根据中间结果迭代修正候选。
5. 输出更优的 OSDA 设计与相关材料适配结论。

## 5. 实验与验证

- 化学对象验证：OSDA 分子设计与相关分子级评估。
- 材料对象验证：OSDA-zeolite compatibility / binding 与 host-guest 相关验证。
- 验证方式：benchmark；simulation_validation；tool-based evaluation。
- 证据强度：first-hand official PDF；source_limited = no。

## 6. 对综述写作的价值

- 可作为 `03/04` 边界中的高质量正例。
- 适合支撑“分子设计锚点仍在化学，但若全文对 zeolite 材料对象给出独立验证，就应接受材料 add-on 模块”的当前政策。
- 推荐引用强度：standard。

## 7. 总结

### 7.1 一句话概括

该 Agent 以 OSDA 分子设计为化学锚点，同时通过 zeolite 适配与结合验证覆盖材料科学对象。

### 7.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：03;04
object_coverage_mode：multi_module
general_method_bucket：none
primary_module_for_filing：03
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：molecular_design; tool_use_and_code_execution; evidence_assessment_and_validation
验证方式：benchmark; simulation_validation
科学贡献类型：design
证据强度：first_hand_full_text
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
