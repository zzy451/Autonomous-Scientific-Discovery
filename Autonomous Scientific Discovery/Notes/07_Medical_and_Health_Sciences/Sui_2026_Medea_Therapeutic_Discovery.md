# Sui et al. 2026 - Medea: An omics AI agent for therapeutic discovery

**论文信息**
- 标题：Medea: An omics AI agent for therapeutic discovery
- 作者：Sui et al.
- 年份：2026
- 来源 / venue：bioRxiv / PMC
- DOI / arXiv / URL：https://doi.org/10.64898/2026.01.16.696667
- PDF / 本地文件路径：本轮未归档本地 PDF；已直接核对官方 PMC full text，并交叉查看官方项目 / GitHub 线索
- 论文类型：研究论文 / omics therapeutic-discovery Agent
- 当前状态：已读（本轮按一手来源重审）；主列表流程状态仍可保持 `to_read`
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 官方 PMC full text | 系统围绕 omics therapeutic-discovery objective 组织透明多步分析与工具调用 | 高 |
| 科学对象归类 | `06;07`，主归档 `07` | 官方 PMC full text | 直接覆盖 therapeutic target discovery、synthetic lethality、immunotherapy-response prediction，以及 omics / pathway / biological-target analysis | 高 |
| 方法流程 | 多模块 Agent 工作流 | 官方 PMC full text + official project trail | planning、code execution、literature reasoning、consensus 等模块协同 | 高 |
| 工具调用 | 明确 | 官方 PMC full text | 跨 transcriptomics、vulnerability maps、pathway knowledge、ML models 等工具与资源 | 高 |
| 边界判断 | 保持 `06;07`，不再写成 source-limited / pending | 官方 PMC full text | 当前一手全文已经足以稳固支持生命科学与医学健康科学双模块覆盖 | 高 |

## 2026-06-23 stronger-source refresh

```text
scientific_object_modules: 06;07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 07
first_hand_sources_checked: official PMC full text; official project/GitHub trail
classification_evidence_source_level: first_hand_full_text
source_limited: no
safety_access_status: none
boundary_type: direct_landing
confidence: high
module_assignment_evidence: `07` is supported by therapeutic target discovery, synthetic lethality, and immunotherapy-response prediction; `06` is supported by omics, pathway, biological-target, and cellular / molecular analysis tasks.
multi_module_object_coverage_note: The therapeutic endpoint controls primary filing, while the omics / pathway / target-analysis workflow remains concrete life-science object coverage and should be retained as `06`.
```

## 0. 摘要翻译

Medea 是一个面向治疗发现的 omics AI agent。官方 PMC 全文显示，它把规划、代码执行、文献推理与共识整合串成透明的多步流程，并调用多类组学、通路、脆弱性图谱和模型资源，服务于 therapeutic target discovery、synthetic lethality 与 immunotherapy-response prediction 等任务。按本轮更强一手来源复核，本文不是 source-limited 的保守样本，而是可稳定落在 `06;07`、主归档 `07` 的 landed 案例。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：面向明确治疗发现目标，具有多步任务分解、工具调用、证据整合与结果判断
- 判定置信度：高

## 2. 科学领域归类

- scientific_object_modules：`06;07`
- object_coverage_mode：`multi_module`
- has_concrete_object_experiments：`yes`
- general_method_bucket：`none`
- primary_module_for_filing：`07`
- first_hand_sources_checked：official PMC full text; official project/GitHub trail
- classification_evidence_source_level：`first_hand_full_text`
- source_limited：`no`
- safety_access_status：`none`
- boundary_type：`direct_landing`
- confidence：`high`
- 归类理由：官方 PMC 全文直接支撑治疗靶点发现、合成致死推理与免疫治疗响应预测等医学导向任务，同时也明确覆盖 omics / pathway / biological-target 分析，因此需要同时保留 `06` 与 `07`。
- 边界说明：治疗终点控制主归档为 `07`，但生命科学层面的多组学、通路与分子靶点分析并非背景叙事，而是具体对象覆盖，不能删去 `06`。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
- 科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation
- 自主能力要点：任务分解、工具链调用、分析状态维护、跨模块共识整合

## 4. 方法设计

Medea 把治疗发现分析拆成多个可协作模块，围绕组学数据、知识资源与模型进行推理与结果整合。对当前归类而言，关键不只是“它服务于治疗发现”，而是它在全文中同时把生物学对象分析与医学终点任务都写成了 concrete object coverage。

## 5. 实验与验证

- 验证方式：benchmark; high_throughput computation; clinical-data-oriented analysis
- 关键任务：target identification; synthetic lethality; immunotherapy-response prediction
- 关键结果：论文直接报告多类治疗发现与多组学分析任务表现，而非仅停留在平台能力展示
- 证据强度：`first_hand_full_text`

## 6. 与已有工作的关系

Medea 是当前批次中较清晰的 `06;07` 双模块正例。它与只落在 `07` 的治疗发现样本不同，因为本文中的 omics / pathway / target analysis 不是附带背景，而是论文直接验证和汇报的核心对象层任务。

## 7. 局限性与风险

- 本轮未新增本地 PDF 归档，仅核对官方 PMC full text。
- 当前证据未要求扩展到更多模块，故保持 adjudication 批准的 `06;07` 即可。

## 8. 对综述写作的价值

- 可放入章节：`07` 医学与健康科学主章节，并在 `06` 生命科学交叉覆盖处点名
- 可支撑论点：治疗发现 Agent 可以同时覆盖 omics / pathway / biological-target 分析与医学终点任务
- 适合用法：`06;07` multi-module landed 正例

## 9. 总结

### 9.1 一句话概括

Medea 是一个经官方 PMC 全文直接支撑的 `06;07` 多模块治疗发现 Agent，主归档 `07`，不再是 source-limited 或 pending 样本。

### 9.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：06;07
object_coverage_mode：multi_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：07
first_hand_sources_checked：official PMC full text; official project/GitHub trail
classification_evidence_source_level：first_hand_full_text
local_pdf_archived_this_round：no
source_limited：no
safety_access_status：none
boundary_type：direct_landing
confidence：high
推荐引用强度：core
```
