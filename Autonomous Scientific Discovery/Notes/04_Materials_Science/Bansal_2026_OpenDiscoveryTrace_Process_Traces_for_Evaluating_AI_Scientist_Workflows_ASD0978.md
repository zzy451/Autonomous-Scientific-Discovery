# OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows

**论文信息**

- ID：ASD-0978
- 标题：OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows
- 作者：Aayam Bansal; Keertan Balaji
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.09203
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0978.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Bansal_2026_OpenDiscoveryTrace_Process_Traces_for_Evaluating_AI_Scientist_Workflows_ASD0978.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | OpenDiscoveryTrace发布558条AI科学家完整轨迹，覆盖124项药物、材料、基因组和科学文献任务。每步记录思考、工具调用、观察、错误、修订触发与自报信心，供过程级审计。作者对多种前沿及开放模型开展试点评估，显示相近任务成功率可能掩盖不同错误数量和类型，并定义多项基准任务及传统机器学习基线。 | 摘要；TXT第233行；核验TXT行号 233 | Existing benchmarks for autonomous AI scientists evaluate only final outputs—generated code, hypotheses, or papers—yet discard the reasoning process by which those outputs were obtained. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。 | 摘要；TXT第233行；核验TXT行号 233 | We present OpenDiscoveryTrace, a public dataset of 558 complete AI scientific agent trajectories that captures how models reason, not just what they produce. | 高（一手正文；非独立复现） |
| Agent能力与行动 | OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows。系统角色与能力：该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。 | 摘要；TXT第233行；核验TXT行号 233 | Each trajectory records a structured 9-field-per-step trace—including thoughts, tool calls, observations, errors, revision triggers, and self-reported confidence—as models execute 124 scientific tasks spanning drug discovery, materials science, genomics, and scientific literature analysis. | 高（一手正文；非独立复现） |
| 验证与结果 | 作者以363条轨迹作试点分析，三个模型成功率相近，但自报置信度与校准表现不同；不能把成功率相近解释为过程可靠性相同。 | 摘要；TXT第233行；核验TXT行号 233 | all three frontier models achieve comparable success rates | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 支撑综述讨论过程日志如何揭示仅看最终答案无法发现的Agent错误及治理问题。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第233行；核验TXT行号 233 | We define five benchmark tasks with baselines from logistic regression, random forests, LSTM, and Transformer models. The dataset, trace schema, agent harness, and benchmark definitions are publicly available under CC-BY-4.0 to support research on process-level evaluation, scientific agent auditing, and AI governance. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

OpenDiscoveryTrace发布558条AI科学家完整轨迹，覆盖124项药物、材料、基因组和科学文献任务。每步记录思考、工具调用、观察、错误、修订触发与自报信心，供过程级审计。作者对多种前沿及开放模型开展试点评估，显示相近任务成功率可能掩盖不同错误数量和类型，并定义多项基准任务及传统机器学习基线。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。OpenDiscoveryTrace发布558条AI科学家完整轨迹，覆盖124项药物、材料、基因组和科学文献任务。每步记录思考、工具调用、观察、错误、修订触发与自报信心，供过程级审计。作者对多种前沿及开放模型开展试点评估，显示相近任务成功率可能掩盖不同错误数量和类型，并定义多项基准任务及传统机器学习基线。
  - 原文位置：摘要；TXT第233行；核验TXT行号 233；引文：Existing benchmarks for autonomous AI scientists evaluate only final outputs—generated code, hypotheses, or papers—yet discard the reasoning process by which those outputs were obtained.
- 多步行动过程：yes。该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。
  - 原文位置：摘要；TXT第233行；核验TXT行号 233；引文：We present OpenDiscoveryTrace, a public dataset of 558 complete AI scientific agent trajectories that captures how models reason, not just what they produce.
- 至少一种Agent能力：yes。OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows。系统角色与能力：该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。
  - 原文位置：摘要；TXT第233行；核验TXT行号 233；引文：Each trajectory records a structured 9-field-per-step trace—including thoughts, tool calls, observations, errors, revision triggers, and self-reported confidence—as models execute 124 scientific tasks spanning drug discovery, materials science, genomics, and scientific literature analysis.
- 明确科研流程角色：yes。以558条轨迹及124项任务构建数据集；试点分析使用363条经LLM评判轨迹。作者报告前沿模型成功率相近（84–89%），但错误率与错误类型存在差异；五类基准与逻辑回归、随机森林、LSTM和Transformer比较。
  - 原文位置：摘要；TXT第233行；核验TXT行号 233；引文：Each trajectory records a structured 9-field-per-step trace—including thoughts, tool calls, observations, errors, revision triggers, and self-reported confidence—as models execute 124 scientific tasks spanning drug discovery, materials science, genomics, and scientific literature analysis. The dataset covers seven models: three frontier (GPT-5.4, Claude Opus 4.6, Gemini 3.1 Pro; 124 trajectories each, fully balanced across domains and difficulty levels) and four open-weight (Qwen2.5-7B, Mistral-

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04;06;07;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.02 结构材料与无机材料；04.04 能源、电子与器件材料；06.03.01 基因组学；07.04.01 药物发现；11.07 科学系统与知识生产研究
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是AI科学家工作流及其评估数据；药物、材料、基因组等是轨迹覆盖领域，不意味着本文本身在每个领域执行新发现。建议保留04及数据/工作流评估相关分类，跨模块分类需主控按对象政策裁决。

### 2.3 容易混淆的边界

对象是AI科学家工作流及其评估数据；药物、材料、基因组等是轨迹覆盖领域，不意味着本文本身在每个领域执行新发现。建议保留04及数据/工作流评估相关分类，跨模块分类需主控按对象政策裁决。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows。系统角色与能力：该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。

### 3.3 自主能力

OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows。系统角色与能力：该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

支撑综述讨论过程日志如何揭示仅看最终答案无法发现的Agent错误及治理问题。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以558条轨迹及124项任务构建数据集；试点分析使用363条经LLM评判轨迹。作者报告前沿模型成功率相近（84–89%），但错误率与错误类型存在差异；五类基准与逻辑回归、随机森林、LSTM和Transformer比较。

### 5.2 基线、指标与结果

以558条轨迹及124项任务构建数据集；试点分析使用363条经LLM评判轨迹。作者报告前沿模型成功率相近（84–89%），但错误率与错误类型存在差异；五类基准与逻辑回归、随机森林、LSTM和Transformer比较。

### 5.3 科学贡献与证据强度

支撑综述讨论过程日志如何揭示仅看最终答案无法发现的Agent错误及治理问题。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文针对只比较最终代码、假设或论文的AI Scientist基准，补充过程轨迹层评估；并与既有科研Agent任务集和传统轨迹预测/错误分类基线比较。

## 7. 局限性与风险

作者及读者可确认的适用边界：数据集试点评估主要使用经LLM评判的部分轨迹；模型、任务域和工具脚手架覆盖并不均衡，作者指出后续需要扩展开放模型及工具任务。

## 8. 对综述写作的价值

支撑综述讨论过程日志如何揭示仅看最终答案无法发现的Agent错误及治理问题。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

OpenDiscoveryTrace发布558条AI科学家完整轨迹，覆盖124项药物、材料、基因组和科学文献任务。

### 9.2 速记版 pipeline

该工作以科学任务、模型执行轨迹及结构化步骤字段为输入，组织不同模型运行任务并收集过程记录；轨迹被整理为统一数据集，再由标注/模型评判流程用于轨迹预测、错误定位、主张核验和过程质量评分等任务。输出是可审计数据集、schema、harness和基准定义，而不是新的自然科学结论。

### 9.3 标注字段汇总

```text
paper_id=ASD-0978
inclusion_status=to_read
scientific_object_modules=04;06;07;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.02;04.04;06.03.01;07.04.01;11.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.02.02` 合金材料；二级：`04.02`。
- 原文位置：PDF pp.9,11,12 materials-science traces; Appendix materials task prompts。
- 判定：当前04.02结构/无机材料下，HEA成分及晶体结构设计任务明确命中合金材料；保留其他材料任务为多候选，不因process-trace定位取消对象证据。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
