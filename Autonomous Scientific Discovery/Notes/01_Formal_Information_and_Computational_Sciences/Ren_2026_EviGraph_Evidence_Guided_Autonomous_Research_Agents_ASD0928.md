# EviGraph: Evidence-Guided Autonomous Research Agents

**论文信息**

- ID：ASD-0928
- 标题：EviGraph: Evidence-Guided Autonomous Research Agents
- 作者：Zhenjiang Ren; Ruiji Li; Xujing Zhang; Ziliang Pang; Shuo Ren; Jiajun Zhang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.04738
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0928.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Ren_2026_EviGraph_Evidence_Guided_Autonomous_Research_Agents_ASD0928.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | EviGraph 将自主研究过程表示为包含 Problem、Gap、Hypothesis、Experiment、Finding、Claim 节点的类型化证据图，并以图作为Agent执行状态，持续检查证据链缺失、语义错位和结果与主张不一致。作者报告其在 ARC-Bench-ML 的 Overall 得分为 86.45%，并在 NanoResearch-20 上报告主张支持率由最强基线的 27% 提高到 37.85%。 | 本地全文：ASD-0928中与研究目标/科学问题直接相关的原文句子；核验TXT行号 384 | Autonomous research agents can generate hypotheses, execute experiments, and draft manuscripts, yet their outputs often contain unsupported claims and inconsistencies between research questions, experiments, results, and conclusions. We argue that this problem is partly architectural: existing systems organize research as sequential pipelines but do not explicitly maintain or validate the evolving claim–evidence structure across stages. In this paper, we introduce EviGraph, an autonomous research framework that represents the research process as a typed evidence graph containing Problem, Gap, Hypothesis, Experiment, Finding, and Claim nodes. The graph serves as the operational state of the agent rather than a post-hoc record. EviGraph inspects evidence chains for missing dependencies, semantic misalignment, and result–claim inconsistencies, localizes the earliest weak node, and regenerates its affected downstream subgraph. Graph checkpointing prevents unsuccessful repairs from corrupting previously validated evidence. Manuscripts are generated only after every retained claim is grounded in a validated evidence chain. Experiments on ARC-Bench-ML and NanoResearch-20 show that EviGraph outperforms the compared end-to-end research-agent baselines in overall research performance, improves Claim Support Rate by 40.19% over the strongest baseline, and achieves 87.73% Experimental Data Consistency. These results demonstrate the value of explicit evidence-state maintenance for reliable autonomous research. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统将研究流程各阶段写入类型化证据图，检查缺失依赖、语义错配及结果—主张不一致，并据此修订下游研究产物。 | 本地全文：ASD-0928中与多步行动/研究流程直接相关的原文句子；核验TXT行号 385 | EviGraph inspects evidence chains for missing dependencies, semantic misalignment, and result–claim inconsistencies, localizes the earliest weak node, and regenerates its affected downstream subgraph. | 高（一手正文；非独立复现） |
| Agent实现与能力 | EviGraph 是证据图驱动的自主研究框架，图节点记录问题、缺口、假设、实验、发现和主张，Agent据此检测并修复薄弱证据链。 | 本地全文：ASD-0928中与Agent实现与能力直接相关的原文句子；核验TXT行号 385 | In this paper, we introduce EviGraph, an autonomous research framework that represents the research process as a typed evidence graph containing Problem, Gap, Hypothesis, Experiment, Finding, and Claim nodes. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 作者在 ARC-Bench-ML 和 NanoResearch-20 上评估，比较总体分数、研究质量维度及 Claim Support Rate。 | 本地全文：ASD-0928中与实验任务与验证设置直接相关的原文句子；核验TXT行号 386 | Experiments on ARC-Bench-ML and NanoResearch-20 show that EviGraph outperforms the compared end-to-end research-agent baselines in overall research performance, improves Claim Support Rate by 40.19% over the strongest baseline, and achieves 87.73% Experimental Data Consistency. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 正文报告 ARC-Bench-ML Overall 为 86.45%；NanoResearch-20 的 Claim Support Rate 从最强基线 27% 提升至 37.85%。 工作贡献是把主张—证据结构作为Agent运行状态，用于跨研究阶段验证；学科对象主要是机器学习研究任务。 | 本地全文中包含该原句的位置；核验TXT行号 464 | EviGraph achieves an Overall score of 86.45% on ARC-Bench-ML and obtains the strongest Novelty, Performance, and Writing scores among the compared systems on NanoResearch-20. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

EviGraph 将自主研究过程表示为包含 Problem、Gap、Hypothesis、Experiment、Finding、Claim 节点的类型化证据图，并以图作为Agent执行状态，持续检查证据链缺失、语义错位和结果与主张不一致。作者报告其在 ARC-Bench-ML 的 Overall 得分为 86.45%，并在 NanoResearch-20 上报告主张支持率由最强基线的 27% 提高到 37.85%。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。EviGraph 将自主研究过程表示为包含 Problem、Gap、Hypothesis、Experiment、Finding、Claim 节点的类型化证据图，并以图作为Agent执行状态，持续检查证据链缺失、语义错位和结果与主张不一致。作者报告其在 ARC-Bench-ML 的 Overall 得分为 86.45%，并在 NanoResearch-20 上报告主张支持率由最强基线的 27% 提高到 37.85%。
  - 原文位置：本地全文：ASD-0928中与研究目标/科学问题直接相关的原文句子；核验TXT行号 384；引文：Autonomous research agents can generate hypotheses, execute experiments, and draft manuscripts, yet their outputs often contain unsupported claims and inconsistencies between research questions, experiments, results, and conclusions. We argue that this problem is partly architectural: existing systems organize research as sequential pipelines but do not explicitly maintain or validate the evolving claim–evidence structure across stages. In this paper, we introduce EviGraph, an autonomous research framework that represents the research process as a typed evidence graph containing Problem, Gap, Hypothesis, Experiment, Finding, and Claim nodes. The graph serves as the operational state of the agent rather than a post-hoc record. EviGraph inspects evidence chains for missing dependencies, semantic misalignment, and result–claim inconsistencies, localizes the earliest weak node, and regenerates its affected downstream subgraph. Graph checkpointing prevents unsuccessful repairs from corrupting previously validated evidence. Manuscripts are generated only after every retained claim is grounded in a validated evidence chain. Experiments on ARC-Bench-ML and NanoResearch-20 show that EviGraph outperforms the compared end-to-end research-agent baselines in overall research performance, improves Claim Support Rate by 40.19% over the strongest baseline, and achieves 87.73% Experimental Data Consistency. These results demonstrate the value of explicit evidence-state maintenance for reliable autonomous research.
- 多步行动过程：yes。系统将研究流程各阶段写入类型化证据图，检查缺失依赖、语义错配及结果—主张不一致，并据此修订下游研究产物。
  - 原文位置：本地全文：ASD-0928中与多步行动/研究流程直接相关的原文句子；核验TXT行号 385；引文：EviGraph inspects evidence chains for missing dependencies, semantic misalignment, and result–claim inconsistencies, localizes the earliest weak node, and regenerates its affected downstream subgraph.
- 至少一种Agent能力：yes。EviGraph 是证据图驱动的自主研究框架，图节点记录问题、缺口、假设、实验、发现和主张，Agent据此检测并修复薄弱证据链。
  - 原文位置：本地全文：ASD-0928中与Agent实现与能力直接相关的原文句子；核验TXT行号 385；引文：In this paper, we introduce EviGraph, an autonomous research framework that represents the research process as a typed evidence graph containing Problem, Gap, Hypothesis, Experiment, Finding, and Claim nodes.
- 明确科研流程角色：yes。作者在 ARC-Bench-ML 和 NanoResearch-20 上评估，比较总体分数、研究质量维度及 Claim Support Rate。
  - 原文位置：本地全文：ASD-0928中与实验任务与验证设置直接相关的原文句子；核验TXT行号 386；引文：Experiments on ARC-Bench-ML and NanoResearch-20 show that EviGraph outperforms the compared end-to-end research-agent baselines in overall research performance, improves Claim Support Rate by 40.19% over the strongest baseline, and achieves 87.73% Experimental Data Consistency.

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

EviGraph 是证据图驱动的自主研究框架，图节点记录问题、缺口、假设、实验、发现和主张，Agent据此检测并修复薄弱证据链。

### 3.3 自主能力

EviGraph 是证据图驱动的自主研究框架，图节点记录问题、缺口、假设、实验、发现和主张，Agent据此检测并修复薄弱证据链。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

工作贡献是把主张—证据结构作为Agent运行状态，用于跨研究阶段验证；学科对象主要是机器学习研究任务。

### 4.2 系统流程与组件

系统将研究流程各阶段写入类型化证据图，检查缺失依赖、语义错配及结果—主张不一致，并据此修订下游研究产物。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者在 ARC-Bench-ML 和 NanoResearch-20 上评估，比较总体分数、研究质量维度及 Claim Support Rate。

### 5.2 基线、指标与结果

正文报告 ARC-Bench-ML Overall 为 86.45%；NanoResearch-20 的 Claim Support Rate 从最强基线 27% 提升至 37.85%。

### 5.3 科学贡献与证据强度

工作贡献是把主张—证据结构作为Agent运行状态，用于跨研究阶段验证；学科对象主要是机器学习研究任务。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“EviGraph: Evidence-Guided Autonomous Research Agents”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

报告的基准分数受任务集和评分器约束；证据图减少内部不一致并不自动证明发现具有外部科学效度。

## 8. 对综述写作的价值

可用于综述“EviGraph: Evidence-Guided Autonomous Research Agents”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

EviGraph 用类型化证据图跟踪科研主张与证据，并报告基准成绩及主张支持率提升。

### 9.2 速记版 pipeline

系统将研究流程各阶段写入类型化证据图，检查缺失依赖、语义错配及结果—主张不一致，并据此修订下游研究产物。

### 9.3 标注字段汇总

```text
paper_id=ASD-0928
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
| 问题开放度 | O2 既定基准 | 在ARC-Bench-ML和NanoResearch-20基准上评估，任务预先定义 | “Experiments on ARC-Bench-ML and NanoResearch-20” · L42 |
| 验证强度 | V1 基准/内部评测 | 使用Claim Support Rate和Experimental Data Consistency等指标评分 | “improves Claim Support Rate by 40.19% over the strongest baseline” · L42 |
| 系统自主性 | L2 闭环执行者 | Agent自主执行研究并检查证据链，在人给定目标内迭代多步 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
