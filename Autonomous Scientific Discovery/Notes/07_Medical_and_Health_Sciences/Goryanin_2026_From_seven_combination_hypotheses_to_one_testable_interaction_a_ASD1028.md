# From seven combination hypotheses to one testable interaction: a gated agentic AI–QSP workflow applied to healthy-ageing interventions

**论文信息**

- ID：ASD-1028
- 标题：From seven combination hypotheses to one testable interaction: a gated agentic AI–QSP workflow applied to healthy-ageing interventions
- 作者：Igor Goryanin; Bob Damms; Irina V. Goryanin
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.29.755460
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1028.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Goryanin_2026_From_seven_combination_hypotheses_to_one_testable_interaction_a_ASD1028.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 本文科学目标是健康老龄化干预组合假设、QSP模型和试验设计；相关工作中的模型benchmark不是本文目标。 | Full text, local TXT line 15；核验TXT行号 15 | We applied this pipeline end to end to healthy-ageing interventions | 高（一手正文；非独立复现） |
| 多步科研流程 | 流程生成组合假设，再经模型构建、可识别性分析和试验设计筛选。 | Full text, local TXT line 20；核验TXT行号 20 | generated seven nutritional combination hypotheses | 高（一手正文；非独立复现） |
| Agent能力 | 科学假设须通过先例、证据、结构完整性及发布门槛。 | Full text, local TXT line 14；核验TXT行号 14 | no hypothesis reaches a report until it clears strict hurdles for precedent, evidence, structural integrity, and release | 高（一手正文；非独立复现） |
| 验证结果 | 虚拟试验检验设计功效，并揭示检测下限对功效和估计的影响。 | Full text, local TXT line 26；核验TXT行号 26 | A 9,000-person virtual trial confirmed the design | 高（一手正文；非独立复现） |
| 限制与边界 | 七个假设中的大量参数缺少数据约束，最终交互仍待真实随机试验验证。 | Full text, local TXT line 22；核验TXT行号 22 | 37 of these were completely unconstrained by available data | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出门控式Agent—QSP工作流，将健康老龄化干预组合假设生成与报告发布分开。工作流以临床试验校准的34状态模型为基础，并先用独立DNA甲基化试验评估模型；模型未通过效应幅度检验后，七个营养组合假设再经过证据、结构和参数可识别性审查，最终仅保留一个可检验交互及其试验设计。研究展示了生成假设的筛选机制，不是干预延寿或改善健康的临床证据。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。科学目标是健康老龄化干预的QSP建模和可检验试验设计；related-work benchmark不是研究目标。
  - 原文位置：Full text, local TXT line 15；核验TXT行号 15；引文：We applied this pipeline end to end to healthy-ageing interventions
- 多步行动过程：yes。流程从多个干预组合假设推进至参数筛选和试验方案。
  - 原文位置：Full text, local TXT line 20；核验TXT行号 20；引文：generated seven nutritional combination hypotheses
- 至少一种Agent能力：yes。先例、证据、模型完整性和发布门槛控制假设晋级。
  - 原文位置：Full text, local TXT line 14；核验TXT行号 14；引文：no hypothesis reaches a report until it clears strict hurdles for precedent, evidence, structural integrity, and release
- 明确科研流程角色：yes。以独立数据、识别性分析及虚拟试验检验模型与设计；并非已证实干预疗效。
  - 原文位置：Full text, local TXT line 26；核验TXT行号 26；引文：A 9,000-person virtual trial confirmed the design

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.03.04 营养科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入健康/衰老干预研究对象模块；属于Agent生成并门控QSP假设的具体应用，单个模型工作流不构成干预有效性的临床证据。

### 2.3 容易混淆的边界

归入健康/衰老干预研究对象模块；属于Agent生成并门控QSP假设的具体应用，单个模型工作流不构成干预有效性的临床证据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

该门控Agent–QSP工作流将假设生成与发表报告分离，依次检查既有证据、模型结构完整性、参数可识别性和释放条件，未通过门槛的组合不进入最终报告。

### 3.3 自主能力

先例、证据、模型完整性和发布门槛控制假设晋级。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把QSP机制模型、证据门槛、参数可识别性和试验设计串成Agent工作流，约束生成式假设过早被表述为结论。

### 4.2 系统流程与组件

应用对象为健康老龄化干预组合。流程以34状态模型为基础，该模型由semaglutide和metformin临床试验校准，并用独立DNA甲基化试验作锁定后评估；Agent先生成7个营养组合假设，再筛选出可检验交互并设计实验。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

研究报告模型校准及独立试验的后验评估，检查参数编码、可识别性和实验设计信息量；以COMBINE/OMEX档案和Python实现支撑可复核性。单一项目运行而非多项目外部验证。

### 5.2 基线、指标与结果

七个组合假设经证据和可识别性门控后仅一个进入可检验交互报告；作者强调模型能够给出可识别参数和实验指标约束下的方案，而不是证明组合已改善健康寿命。

### 5.3 科学贡献与证据强度

贡献是把QSP机制模型、证据门槛、参数可识别性和试验设计串成Agent工作流，约束生成式假设过早被表述为结论。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较只让LLM提出组合方案或直接生成机制模型，本文设置逐级证据与可识别性门控，并将最终输出落到能够区分假设的试验设计。

## 7. 局限性与风险

这是一个团队和单一项目的经验，模型与AgeQSP记录仅覆盖一个项目周期；营养组合和健康老龄化机制仍需实际实验及临床试验验证。

## 8. 对综述写作的价值

可用于比较生成式干预组合假设如何经QSP证据、可识别性与试验设计门槛筛选。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

门控Agent—QSP流程从七个健康老龄化营养组合假设中筛出一个可识别、可实验检验的交互，并提出相应试验设计。模型评估和证据门槛限制了过度推断，但单一项目并未证明干预有效。

### 9.2 速记版 pipeline

应用对象为健康老龄化干预组合。流程以34状态模型为基础，该模型由semaglutide和metformin临床试验校准，并用独立DNA甲基化试验作锁定后评估；Agent先生成7个营养组合假设，再筛选出可检验交互并设计实验。

### 9.3 标注字段汇总

```text
paper_id=ASD-1028
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.03.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O4 需物理检验 | 营养组合假设产生候选干预方案，需真实试验验证健康效果 | “seven nutritional combination hypotheses” · L22 |
| 验证强度 | V2 计算/仿真/回顾性 | 虚拟试验与QSP模型仿真验证设计，无真实人群试验 | “A 9,000-person virtual trial confirmed the design” · L24 |
| 系统自主性 | L2 闭环执行者 | 多步工作流自主筛选假设和可识别性，但目标由人设定 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
