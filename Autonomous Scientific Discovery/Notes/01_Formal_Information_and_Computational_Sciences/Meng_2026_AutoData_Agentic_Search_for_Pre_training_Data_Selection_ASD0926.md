# AutoData: Agentic Search for Pre-training Data Selection

**论文信息**

- ID：ASD-0926
- 标题：AutoData: Agentic Search for Pre-training Data Selection
- 作者：Yan Meng; Dhruv Srikanth; Bingchen Zhao; Zhengyao Jiang; Yuxiang Wu
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.19754
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0926.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Meng_2026_AutoData_Agentic_Search_for_Pre_training_Data_Selection_ASD0926.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | 本文提出 AutoData，以Agent搜索可执行的数据选择函数，用代理模型和留出验证反馈改进预训练语料筛选。作者在 ClimbMix 上评估方法，并报告不同评测设置下的变化；CORE 上的增益未达到统计显著，因此不应概括为对所有数据集都稳定有效。 | 本地全文：ASD-0926中与研究目标/科学问题直接相关的原文句子；核验TXT行号 366 | LLM agents have recently shown promise in automating machine learning engineering by editing model and training code under execution feedback. Data, however, remains largely outside this agentic optimisation loop. We frame pre-training data selection as heuristic engineering over per-document features, i.e., lexical statistics, categorical labels, and perplexity. We introduce AutoData, an agent that searches directly over executable selection algorithms. Unlike prior data mixture methods that optimise weights over a fixed set of domains, AutoData searches a richer program space of scoring, stratification, and stochastic selection rules, discovering feature interactions automatically by iteratively refining algorithms with validation feedback from a proxy model. Within an overnight search, AutoData discovers a selection algorithm that outperforms existing human-designed curation pipelines. Despite being searched only on this small proxy, the discovered recipe transfers to larger scales and improves the downstream metric CORE. These results suggest that data engineering can be treated as an agentic machine learning problem, extending autonomous research from model and training-code optimization to the data. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统以训练语料和验证目标为输入，搜索数据选择函数，使用选出的数据训练代理模型，再依据留出验证表现反馈更新候选函数。 | 本地全文：ASD-0926中与多步行动/研究流程直接相关的原文句子；核验TXT行号 370 | Unlike prior data mixture methods that optimise weights over a fixed set of domains, AutoData searches a richer program space of scoring, stratification, and stochastic selection rules, discovering feature interactions automatically by iteratively refining algorithms with validation feedback from a proxy model. | 高（一手正文；非独立复现） |
| Agent实现与能力 | AutoData 是面向预训练数据选择的Agent系统：生成和迭代可执行筛选函数，训练代理模型，并根据留出验证反馈继续搜索。 | 本地全文：ASD-0926中与Agent实现与能力直接相关的原文句子；核验TXT行号 369 | We introduce AutoData, an agent that searches directly over executable selection algorithms. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 作者在 NVIDIA ClimbMix 语料上开展实验，并报告 CORE 等基准结果；CORE 的增益被作者说明为统计上不显著。 | 本地全文：ASD-0926中与实验任务与验证设置直接相关的原文句子；核验TXT行号 745 | We apply AutoData to NVIDIA’s full ClimbMix corpus (Diao et al., 2025), a 400B-token English pretraining corpus. The corpus contains 6,5426{,}542 training shards, covering N=553,155,584N=553{,}155{,}584 documents. We reserve one shard as a held-out validation set and exclude it from all selection pools. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 论文报告 AutoData 在部分预训练数据选择评测上获得改进；CORE 的结果未达到统计显著，结论应保留这一限定。 科学对象是机器学习预训练数据及其对模型训练表现的影响；方法贡献是将数据筛选规则搜索表述为带验证反馈的Agent优化任务。 | 本地全文中包含该原句的位置；核验TXT行号 1791 | AutoData recipes significantly outperform all four baselines on val-bpb from depth 88 to depth 2020, showing that recipes discovered with a small proxy model can remain effective at larger scales. At depth 2424, however, AutoData performs similarly to the default ClimbMix, indicating a limit to its cross-scale transfer. On the downstream CORE benchmark, AutoData outperforms the baselines at every scale except depth 1616. However, these gains are not statistically significant, possibly because CORE has high variance. The lack of statistically significant improvements on CORE is a limitation of our methodology. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出 AutoData，以Agent搜索可执行的数据选择函数，用代理模型和留出验证反馈改进预训练语料筛选。作者在 ClimbMix 上评估方法，并报告不同评测设置下的变化；CORE 上的增益未达到统计显著，因此不应概括为对所有数据集都稳定有效。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文提出 AutoData，以Agent搜索可执行的数据选择函数，用代理模型和留出验证反馈改进预训练语料筛选。作者在 ClimbMix 上评估方法，并报告不同评测设置下的变化；CORE 上的增益未达到统计显著，因此不应概括为对所有数据集都稳定有效。
  - 原文位置：本地全文：ASD-0926中与研究目标/科学问题直接相关的原文句子；核验TXT行号 366；引文：LLM agents have recently shown promise in automating machine learning engineering by editing model and training code under execution feedback. Data, however, remains largely outside this agentic optimisation loop. We frame pre-training data selection as heuristic engineering over per-document features, i.e., lexical statistics, categorical labels, and perplexity. We introduce AutoData, an agent that searches directly over executable selection algorithms. Unlike prior data mixture methods that optimise weights over a fixed set of domains, AutoData searches a richer program space of scoring, stratification, and stochastic selection rules, discovering feature interactions automatically by iteratively refining algorithms with validation feedback from a proxy model. Within an overnight search, AutoData discovers a selection algorithm that outperforms existing human-designed curation pipelines. Despite being searched only on this small proxy, the discovered recipe transfers to larger scales and improves the downstream metric CORE. These results suggest that data engineering can be treated as an agentic machine learning problem, extending autonomous research from model and training-code optimization to the data.
- 多步行动过程：yes。系统以训练语料和验证目标为输入，搜索数据选择函数，使用选出的数据训练代理模型，再依据留出验证表现反馈更新候选函数。
  - 原文位置：本地全文：ASD-0926中与多步行动/研究流程直接相关的原文句子；核验TXT行号 370；引文：Unlike prior data mixture methods that optimise weights over a fixed set of domains, AutoData searches a richer program space of scoring, stratification, and stochastic selection rules, discovering feature interactions automatically by iteratively refining algorithms with validation feedback from a proxy model.
- 至少一种Agent能力：yes。AutoData 是面向预训练数据选择的Agent系统：生成和迭代可执行筛选函数，训练代理模型，并根据留出验证反馈继续搜索。
  - 原文位置：本地全文：ASD-0926中与Agent实现与能力直接相关的原文句子；核验TXT行号 369；引文：We introduce AutoData, an agent that searches directly over executable selection algorithms.
- 明确科研流程角色：yes。作者在 NVIDIA ClimbMix 语料上开展实验，并报告 CORE 等基准结果；CORE 的增益被作者说明为统计上不显著。
  - 原文位置：本地全文：ASD-0926中与实验任务与验证设置直接相关的原文句子；核验TXT行号 745；引文：We apply AutoData to NVIDIA’s full ClimbMix corpus (Diao et al., 2025), a 400B-token English pretraining corpus. The corpus contains 6,5426{,}542 training shards, covering N=553,155,584N=553{,}155{,}584 documents. We reserve one shard as a held-out validation set and exclude it from all selection pools.

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

AutoData 是面向预训练数据选择的Agent系统：生成和迭代可执行筛选函数，训练代理模型，并根据留出验证反馈继续搜索。

### 3.3 自主能力

AutoData 是面向预训练数据选择的Agent系统：生成和迭代可执行筛选函数，训练代理模型，并根据留出验证反馈继续搜索。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学对象是机器学习预训练数据及其对模型训练表现的影响；方法贡献是将数据筛选规则搜索表述为带验证反馈的Agent优化任务。

### 4.2 系统流程与组件

系统以训练语料和验证目标为输入，搜索数据选择函数，使用选出的数据训练代理模型，再依据留出验证表现反馈更新候选函数。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者在 NVIDIA ClimbMix 语料上开展实验，并报告 CORE 等基准结果；CORE 的增益被作者说明为统计上不显著。

### 5.2 基线、指标与结果

论文报告 AutoData 在部分预训练数据选择评测上获得改进；CORE 的结果未达到统计显著，结论应保留这一限定。

### 5.3 科学贡献与证据强度

科学对象是机器学习预训练数据及其对模型训练表现的影响；方法贡献是将数据筛选规则搜索表述为带验证反馈的Agent优化任务。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“AutoData: Agentic Search for Pre-training Data Selection”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

验证表现依赖所用代理模型、语料和下游评测；CORE 上的非显著结果限制了关于普遍收益的主张。

## 8. 对综述写作的价值

可用于综述“AutoData: Agentic Search for Pre-training Data Selection”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

AutoData 用代理模型的验证反馈搜索预训练数据选择函数。

### 9.2 速记版 pipeline

系统以训练语料和验证目标为输入，搜索数据选择函数，使用选出的数据训练代理模型，再依据留出验证表现反馈更新候选函数。

### 9.3 标注字段汇总

```text
paper_id=ASD-0926
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
| 问题开放度 | O3 新实例 | 搜索预训练数据选择函数并优化语料筛选，答案可由代理模型验证核对 | “searches a richer program space of scoring, stratification, and stochastic selection rules” · L21 |
| 验证强度 | V2 计算/仿真/回顾性 | 在ClimbMix语料上通过代理模型和留出验证评估，但CORE结果未达显著 | “CORE 的增益被作者说明为统计上不显著” · L24 |
| 系统自主性 | L2 闭环执行者 | 系统自主生成数据选择函数、训练代理模型并根据反馈迭代优化 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
