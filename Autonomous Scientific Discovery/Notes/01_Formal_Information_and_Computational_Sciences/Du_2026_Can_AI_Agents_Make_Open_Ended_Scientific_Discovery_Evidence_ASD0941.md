# Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station

**论文信息**

- ID：ASD-0941
- 标题：Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station
- 作者：Wenyu Du; Stephen Chung
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.08927
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0941.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Du_2026_Can_AI_Agents_Make_Open_Ended_Scientific_Discovery_Evidence_ASD0941.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | 本文在开放世界Station环境中研究多Agent能否完成开放式发现，并加入Supervisor机制和周期性Meta Reflection，以支持中间指标不足时的持续探索。作者从三篇近期ICLR oral论文构造任务，向Agent提供核心研究问题并隐藏原结果，同时分析Supervisor与反思机制的消融效果。 | 本地全文：ASD-0941中与研究目标/科学问题直接相关的原文句子；核验TXT行号 416 | Recent AI systems have made rapid progress in scientific discovery when given well-defined metrics, but whether they can autonomously undertake open-ended scientific discovery remains unclear. We investigate AI’s ability to tackle open-ended tasks in Station, an open-world environment in which multiple agents simulate a scientific ecosystem. To tackle challenges specific to open-ended tasks, we propose augmenting Station with two mechanisms: a Supervisor mechanism and periodic Meta Reflection, which encourage persistent exploration even when intermediate metrics are lacking. We construct open-ended tasks from three recent oral papers presented at ICLR. We give agents the main research question studied in each paper while withholding the paper’s results and disabling web access. We then measure how many of the original findings—partitioned into individual criteria—agents rediscover. We find that Station rediscovers 62.7% of the criteria on average, compared with 15.4% for Codex Multiagent-v2 and 14.4–20.6% for AI Scientist-v2. Ablation and behavioral analyses indicate that adding the two mechanisms together improves research coverage and continuity. We further evaluate Station on two open-ended tasks without oracle papers and find that some of the discoveries made by the agents closely match discoveries reported by researchers after the knowledge cutoff date. Together, these results indicate that a suitable environment can enable agents to autonomously make meaningful progress in open-ended scientific discovery. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 任务取自三篇ICLR oral论文，隐藏原论文结果并要求Agent解决其研究问题；对移除Supervisor和Meta Reflection的系统进行多轮消融。 | 本地全文：ASD-0941中与多步行动/研究流程直接相关的原文句子；核验TXT行号 416 | To tackle challenges specific to open-ended tasks, we propose augmenting Station with two mechanisms: a Supervisor mechanism and periodic Meta Reflection, which encourage persistent exploration even when intermediate metrics are lacking. | 高（一手正文；非独立复现） |
| Agent实现与能力 | Station是多Agent模拟科学生态的开放世界环境；Supervisor监督探索方向，Meta Reflection周期性总结进展并调整后续研究。 | 本地全文：ASD-0941中与Agent实现与能力直接相关的原文句子；核验TXT行号 894 | 6.1 Effects of the Supervisor and Meta Reflection To understand the effects of the Supervisor and Meta Reflection, we perform an ablation study by removing both mechanisms and conducting three runs on the emergent-planning task. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 主要评估包括三项研究问题的开放式任务及Supervisor/Meta Reflection消融；评价Agent是否能持续探索并恢复论文相关发现。 | 本地全文：ASD-0941中与实验任务与验证设置直接相关的原文句子；核验TXT行号 416 | We construct open-ended tasks from three recent oral papers presented at ICLR. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者通过消融分析两种机制对开放式任务探索的影响；结论限定于Station环境和三项基于论文的问题。 工作提供开放世界多Agent研究环境，并检验监督和周期性反思对持续探索的作用。 | 本地全文中包含该原句的位置；核验TXT行号 900 | To understand the effects of the Supervisor and Meta Reflection, we perform an ablation study by removing both mechanisms and conducting three runs on the emergent-planning task. Removing the two mechanisms reduces sub-discovery recovery from 75.8% to 57.9%, with a pronounced drop in intervention findings (Fig. 3A). These findings require agents to build on earlier concept-probing results and use the identified representations to causally manipulate the RL agent’s behavior. Examination of the records shows that agents in ablated Station are less likely to build on earlier discoveries and instead concentrate on probing concepts, often failing to connect these observations to the broader research goal. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文在开放世界Station环境中研究多Agent能否完成开放式发现，并加入Supervisor机制和周期性Meta Reflection，以支持中间指标不足时的持续探索。作者从三篇近期ICLR oral论文构造任务，向Agent提供核心研究问题并隐藏原结果，同时分析Supervisor与反思机制的消融效果。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文在开放世界Station环境中研究多Agent能否完成开放式发现，并加入Supervisor机制和周期性Meta Reflection，以支持中间指标不足时的持续探索。作者从三篇近期ICLR oral论文构造任务，向Agent提供核心研究问题并隐藏原结果，同时分析Supervisor与反思机制的消融效果。
  - 原文位置：本地全文：ASD-0941中与研究目标/科学问题直接相关的原文句子；核验TXT行号 416；引文：Recent AI systems have made rapid progress in scientific discovery when given well-defined metrics, but whether they can autonomously undertake open-ended scientific discovery remains unclear. We investigate AI’s ability to tackle open-ended tasks in Station, an open-world environment in which multiple agents simulate a scientific ecosystem. To tackle challenges specific to open-ended tasks, we propose augmenting Station with two mechanisms: a Supervisor mechanism and periodic Meta Reflection, which encourage persistent exploration even when intermediate metrics are lacking. We construct open-ended tasks from three recent oral papers presented at ICLR. We give agents the main research question studied in each paper while withholding the paper’s results and disabling web access. We then measure how many of the original findings—partitioned into individual criteria—agents rediscover. We find that Station rediscovers 62.7% of the criteria on average, compared with 15.4% for Codex Multiagent-v2 and 14.4–20.6% for AI Scientist-v2. Ablation and behavioral analyses indicate that adding the two mechanisms together improves research coverage and continuity. We further evaluate Station on two open-ended tasks without oracle papers and find that some of the discoveries made by the agents closely match discoveries reported by researchers after the knowledge cutoff date. Together, these results indicate that a suitable environment can enable agents to autonomously make meaningful progress in open-ended scientific discovery.
- 多步行动过程：yes。任务取自三篇ICLR oral论文，隐藏原论文结果并要求Agent解决其研究问题；对移除Supervisor和Meta Reflection的系统进行多轮消融。
  - 原文位置：本地全文：ASD-0941中与多步行动/研究流程直接相关的原文句子；核验TXT行号 416；引文：To tackle challenges specific to open-ended tasks, we propose augmenting Station with two mechanisms: a Supervisor mechanism and periodic Meta Reflection, which encourage persistent exploration even when intermediate metrics are lacking.
- 至少一种Agent能力：yes。Station是多Agent模拟科学生态的开放世界环境；Supervisor监督探索方向，Meta Reflection周期性总结进展并调整后续研究。
  - 原文位置：本地全文：ASD-0941中与Agent实现与能力直接相关的原文句子；核验TXT行号 894；引文：6.1 Effects of the Supervisor and Meta Reflection To understand the effects of the Supervisor and Meta Reflection, we perform an ablation study by removing both mechanisms and conducting three runs on the emergent-planning task.
- 明确科研流程角色：yes。主要评估包括三项研究问题的开放式任务及Supervisor/Meta Reflection消融；评价Agent是否能持续探索并恢复论文相关发现。
  - 原文位置：本地全文：ASD-0941中与实验任务与验证设置直接相关的原文句子；核验TXT行号 416；引文：We construct open-ended tasks from three recent oral papers presented at ICLR.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

Station是多Agent模拟科学生态的开放世界环境；Supervisor监督探索方向，Meta Reflection周期性总结进展并调整后续研究。

### 3.3 自主能力

Station是多Agent模拟科学生态的开放世界环境；Supervisor监督探索方向，Meta Reflection周期性总结进展并调整后续研究。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

工作提供开放世界多Agent研究环境，并检验监督和周期性反思对持续探索的作用。

### 4.2 系统流程与组件

任务取自三篇ICLR oral论文，隐藏原论文结果并要求Agent解决其研究问题；对移除Supervisor和Meta Reflection的系统进行多轮消融。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

主要评估包括三项研究问题的开放式任务及Supervisor/Meta Reflection消融；评价Agent是否能持续探索并恢复论文相关发现。

### 5.2 基线、指标与结果

作者通过消融分析两种机制对开放式任务探索的影响；结论限定于Station环境和三项基于论文的问题。

### 5.3 科学贡献与证据强度

工作提供开放世界多Agent研究环境，并检验监督和周期性反思对持续探索的作用。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

任务数量为三项且运行于模拟环境；这类 rediscovery 任务不能等同于产生全新、可外部验证的科学发现。

## 8. 对综述写作的价值

可用于综述“Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Station研究Supervisor和周期性反思如何支持多Agent完成开放式论文问题任务。

### 9.2 速记版 pipeline

任务取自三篇ICLR oral论文，隐藏原论文结果并要求Agent解决其研究问题；对移除Supervisor和Meta Reflection的系统进行多轮消融。

### 9.3 标注字段汇总

```text
paper_id=ASD-0941
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 从三篇ICLR论文构造任务，隐藏结果但问题由人给定 | “three recent oral papers presented at ICLR” · L42 |
| 验证强度 | V1 基准/内部评测 | 评估Agent是否恢复论文发现，属基准评测和消融分析 | “how many of the original findings” · L36 |
| 系统自主性 | L2 闭环执行者 | 多Agent在开放环境中持续探索并由Supervisor监督形成闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
