# Nazeri et al. 2026 - RAISE: a self-driving laboratory for interfacial property formulation discovery

**论文信息**
- 标题：RAISE: a self-driving laboratory for interfacial property formulation discovery
- 作者：Nazeri et al.
- 年份：2026
- 来源 / venue：Digital Discovery
- DOI / arXiv / URL：https://doi.org/10.1039/d5dd00531k
- PDF / 本地文件路径：本轮未归档本地 PDF；已直接核对官方 RSC 文章 HTML full text
- 论文类型：研究论文 / self-driving laboratory
- 当前状态：已读（本轮按一手全文重审）；主列表流程状态仍可保持 `to_read`
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 官方 RSC HTML full text | 系统是面向 formulation discovery 的 autonomous closed-loop laboratory | 高 |
| 科学对象归类 | `04` | 官方 RSC HTML full text | 论文直接围绕 interfacial-property formulation、surface wettability 等具体材料 / 配方对象做目标导向优化 | 高 |
| 方法流程 | 闭环 SDL | 官方 RSC HTML full text | 从用户目标出发，自动提出、测试并更新 formulation 候选 | 高 |
| 验证方式 | 真实闭环材料 / 配方发现 | 官方 RSC HTML full text | 不是 Crossref 摘要层面的系统叙事，而是有明确 paper-level 实验与闭环发现过程 | 高 |
| 边界判断 | 不转 `01.04` | 官方 RSC HTML full text | 核心对象是具体 interfacial formulation discovery，不是通用科研 Agent 平台 | 高 |

## 0. 摘要翻译

RAISE 是一个围绕界面性质配方发现的自驱动实验室系统，目标是根据用户定义的界面性质要求自动搜索和优化 formulation。与旧 note 的 Crossref-only 读法不同，本轮已直接核对官方 RSC 全文，因此可以稳定确认本文属于 `04` 材料科学对象覆盖，而不是薄证据状态下的暂存条目。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：面向明确材料发现目标，具有任务规划、实验执行、结果读出与闭环反馈
- 判定置信度：高

## 2. 科学领域归类

- scientific_object_modules：`04`
- object_coverage_mode：`single_module`
- has_concrete_object_experiments：`yes`
- general_method_bucket：`none`
- primary_module_for_filing：`04`
- first_hand_sources_checked：official RSC article HTML full text
- classification_evidence_source_level：`first_hand_full_text`
- source_limited：`no`
- safety_access_status：`none`
- boundary_type：`direct_landing`
- confidence：`high`
- 归类理由：官方 RSC 全文直接报告了面向 tailored interfacial property / wettability targets 的 autonomous formulation discovery，这是明确的材料 / 配方优化对象覆盖。
- 边界说明：虽与 `03` 化学模块存在相邻关系，但当前论文的稳定对象是 formulation 及其界面性质表现，按 adjudication 保持单模块 `04` 即可，不扩写更细分支或跨模块。

## 3. Agent 系统与科研流程角色

- Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
- 科研流程角色：experimental_design; experiment_execution; data_analysis; evidence_assessment_and_validation; end_to_end_research_automation
- 自主能力要点：候选配方生成、自动实验执行、界面性质读出、闭环更新

## 4. 方法设计

系统把 formulation discovery 转化为目标导向的闭环搜索任务，根据界面性质读出更新下一轮候选。对当前分类最关键的是，论文研究对象始终是具体 formulation 与 interfacial-property target，而非抽象科研平台本身。

## 5. 实验与验证

- 验证方式：closed-loop laboratory experimentation
- 关键对象：interfacial formulations; surface wettability targets
- 关键结果：实现 autonomous closed-loop formulation discovery，并围绕具体性质目标进行优化
- 证据强度：`first_hand_full_text`

## 6. 与已有工作的关系

RAISE 应作为材料科学中的 self-driving laboratory 代表样本使用，而不再保留旧的 Crossref 摘要级保守表述。它和通用 `01.04` 科研 Agent 的区别在于：本文的对象、目标和验证都牢固地落在材料 / 配方层面。

## 7. 局限性与风险

- 本轮未新增本地 PDF 归档，仅核对官方 RSC HTML full text。
- adjudication 只批准 `04`，因此本 note 不主动扩展到 `03` 或更细子类。

## 8. 对综述写作的价值

- 可放入章节：`04` 材料科学相关章节
- 可支撑论点：自驱动实验室已经在配方与界面性质优化上形成明确材料对象覆盖
- 适合用法：材料 SDL / formulation discovery 的正例

## 9. 总结

### 9.1 一句话概括

RAISE 是一个由官方全文直接支撑的 `04` 材料科学自驱配方发现系统，而不再是 Crossref-only 的保守暂存样本。

### 9.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：04
object_coverage_mode：single_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：04
first_hand_sources_checked：official RSC article HTML full text
classification_evidence_source_level：first_hand_full_text
local_pdf_archived_this_round：no
source_limited：no
safety_access_status：none
boundary_type：direct_landing
confidence：high
推荐引用强度：core
```
