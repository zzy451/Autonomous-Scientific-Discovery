# Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`05`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`04;05`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 04 | 04.02 结构材料与无机材料 | 04.02.03 无机非金属材料 | 已落地 |
| 05 | 05.01 地球科学基础 | 05.01.04 矿物学 | 已落地 |

- 模块04：五种蒙脱石GCMC-MD脱附、含水量和层间距。
  - 证据：PDF 第 [7, 9, 10] 页；原文：two clay sheets, one interlayer region, and two external-surface regions

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0989
- 标题：Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns
- 作者：Yijie Wang; Zhen-Yu Yin; Zhenheng Tang; Xiaowen Chu
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.07637
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0989.txt
- PDF / 本地文件路径：Reference_PDF/05_Earth_and_Environmental_Sciences/Wang_2026_Agent_MD_Selective_LLM_Intervention_with_Event_Driven_Escalation_ASD0989.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | Agent-MD研究LLM在有状态GCMC—MD模拟活动中的介入策略，重点不是让模型持续接管每一步，而是在事件触发时升级给LLM，以平衡计算成本、可控性和科学判断。论文围绕电解质/分子模拟活动考察状态维护、事件检测和Agent升级机制；具体体系、事件阈值和比较结果需以正文为准。 | 摘要；TXT第224行；核验TXT行号 224 | Long-running molecular simulation campaigns require repeated continuation from saved states, provenance-aware progression, adaptive assessment, and occasional interpretation of workflow conditions that cannot be resolved safely by fixed rules. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第224行；核验TXT行号 224 | Here, we present Agent-MD, a framework that places large language model (LLM) reasoning selectively at campaign construction and event-triggered review, while routine simulation, analysis, continuation, archiving, and state progression are handled by a persistent rule-based campaign agent using approved policies and explicit state records. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns。系统角色与能力：模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第224行；核验TXT行号 224 | Routine production required no live reasoning-agent invocation, while one state reached a review boundary; two preserved incidents were subsequently evaluated through blinded reasoning-agent replay, which identified the underlying workflow problems and recommended appropriate follow-up actions. | 高（一手正文；非独立复现） |
| 验证与结果 | 评估不同介入策略下模拟活动的完成、稳定性、资源使用和结果质量；比较对象应包括持续LLM介入及常规自动运行基线。具体样本数值需由结果表核验。 | 摘要；TXT第224行；核验TXT行号 224 | Across 15 system–RH states, the workflow completed 120 segmented simulation cycles with state-specific sampling lengths and provenance-aware restart inheritance. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可支持综述讨论何时需要LLM介入科学模拟，以及用事件驱动降低过度调用。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第224行；核验TXT行号 224 | The simulations also revealed distinct composition-dependent low-RH responses, with Ca-bearing montmorillonite retaining more interlayer water and maintaining a larger basal spacing than the Na- and K-bearing systems, while the highest-charge Na system retained more residual water under dry conditions. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Agent-MD将LLM推理用于长期分子模拟研究的campaign构建与事件触发复核，常规推进由带状态记录的规则Agent完成。实际案例比较五种蒙脱石系统在三个顺序湿度状态下的含水量、层间水分布与基面间距；Agent提出系统矩阵、执行及接受规则，并在批准约束下协同模拟、分析和归档。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。Agent-MD研究LLM在有状态GCMC—MD模拟活动中的介入策略，重点不是让模型持续接管每一步，而是在事件触发时升级给LLM，以平衡计算成本、可控性和科学判断。论文围绕电解质/分子模拟活动考察状态维护、事件检测和Agent升级机制；具体体系、事件阈值和比较结果需以正文为准。
  - 原文位置：摘要；TXT第224行；核验TXT行号 224；引文：Long-running molecular simulation campaigns require repeated continuation from saved states, provenance-aware progression, adaptive assessment, and occasional interpretation of workflow conditions that cannot be resolved safely by fixed rules.
- 多步行动过程：yes。模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第224行；核验TXT行号 224；引文：Here, we present Agent-MD, a framework that places large language model (LLM) reasoning selectively at campaign construction and event-triggered review, while routine simulation, analysis, continuation, archiving, and state progression are handled by a persistent rule-based campaign agent using approved policies and explicit state records.
- 至少一种Agent能力：yes。Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns。系统角色与能力：模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第224行；核验TXT行号 224；引文：Routine production required no live reasoning-agent invocation, while one state reached a review boundary; two preserved incidents were subsequently evaluated through blinded reasoning-agent replay, which identified the underlying workflow problems and recommended appropriate follow-up actions.
- 明确科研流程角色：yes。评估不同介入策略下模拟活动的完成、稳定性、资源使用和结果质量；比较对象应包括持续LLM介入及常规自动运行基线。具体样本数值需由结果表核验。
  - 原文位置：摘要；TXT第224行；核验TXT行号 224；引文：Across 15 system–RH states, the workflow completed 120 segmented simulation cycles with state-specific sampling lengths and provenance-aware restart inheritance.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05;04
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不覆盖其他模块）
- 模块内分类路径：05.01.04 矿物学；04.02 结构材料与无机材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

蒙脱石矿物的水化/脱水、不同阳离子及层电荷、层间含水量和基面间距；同时覆盖地质矿物与无机非金属材料对象。

### 2.3 容易混淆的边界

纳入Agent研究。对象分类按被模拟对象而非GCMC/MD方法决定：实际案例是蒙脱石矿物在湿度变化下的层间水与层片结构响应，具有地质矿物学含义（膨胀土、钻孔稳定性、黏土屏障等），建议05.01.04矿物学为主；同时材料对象证据支持04.02.03无机非金属材料。单纯的分子模拟软件工作流不构成04分类依据；本例的矿物对象结果构成依据。主类建议05，副模块04。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns。系统角色与能力：模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns。系统角色与能力：模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述讨论何时需要LLM介入科学模拟，以及用事件驱动降低过度调用。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评估不同介入策略下模拟活动的完成、稳定性、资源使用和结果质量；比较对象应包括持续LLM介入及常规自动运行基线。具体样本数值需由结果表核验。

### 5.2 基线、指标与结果

评估不同介入策略下模拟活动的完成、稳定性、资源使用和结果质量；比较对象应包括持续LLM介入及常规自动运行基线。具体样本数值需由结果表核验。

### 5.3 科学贡献与证据强度

可支持综述讨论何时需要LLM介入科学模拟，以及用事件驱动降低过度调用。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文与持续LLM控制和规则化分子模拟编排工作相关，采用事件触发LLM审查并由持久规则Agent执行常规状态推进。

## 7. 局限性与风险

作者及读者可确认的适用边界：演示聚焦五种蒙脱石的水汽解吸和三个相对湿度状态；事件规则和策略的外推仍需其他分子体系与更长活动验证。

## 8. 对综述写作的价值

可支持综述讨论何时需要LLM介入科学模拟，以及用事件驱动降低过度调用。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Agent-MD研究LLM在有状态GCMC—MD模拟活动中的介入策略，重点不是让模型持续接管每一步，而是在事件触发时升级给LLM，以平衡计算成本、可控性和科学判断。

### 9.2 速记版 pipeline

模拟引擎执行常规GCMC—MD步骤并保存活动状态；事件检测器识别异常、阶段完成或需人/模型决策的节点，再将摘要状态交给LLM。Agent可提出修复或调整建议，运行器执行后继续模拟，形成事件驱动的选择性介入循环。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0989
inclusion_status=to_read
scientific_object_modules=05;04
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.01.04;04.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 分子模拟结果可由已知方法检验 | “Across 15 system–RH states” · L61 |
| 验证强度 | V2 计算/仿真/回顾性 | 仿真结果与回顾性数据检验 | “The simulations also revealed distinct composition-dependent low-RH responses” · L44 |
| 系统自主性 | L2 闭环执行者 | 事件驱动时升级给LLM决策 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
