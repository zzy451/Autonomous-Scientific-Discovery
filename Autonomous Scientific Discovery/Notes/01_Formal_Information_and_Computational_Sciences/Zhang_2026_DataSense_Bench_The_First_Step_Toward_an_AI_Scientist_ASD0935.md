# DataSense-Bench: The First Step Toward an AI Scientist

**论文信息**

- ID：ASD-0935
- 标题：DataSense-Bench: The First Step Toward an AI Scientist
- 作者：Yudi Zhang; Mingyu Cao; Lu Yin; Mykola Pechenizkiy; Shiwei Liu
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.12190
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0935.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Zhang_2026_DataSense_Bench_The_First_Step_Toward_an_AI_Scientist_ASD0935.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | DataSense-Bench研究Agent是否具备数据选择能力，并能预测候选训练数据对模型表现的价值。基准要求Agent为微调小型语言模型选择并排序训练子集，允许检查数据、编写和运行分析代码及模型前向计算。 | 本地全文：ASD-0935中与研究目标/科学问题直接相关的原文句子；核验TXT行号 275 | As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench11 1 Code and Project page. to study this capability through the fundamental problem of data selection and performance forecasting in machine learning. We ask AI agents to select and rank candidate training subsets that can be used to fine-tune a small LLM model. Agents are allowed to inspect the data, write and execute analysis code, and run model forward passes, but can not train the model or access the actual evaluation tasks. We then fine-tune the base model on each selected subset and evaluate its post-training performance under a standardized protocol. We instantiate the benchmark in terminal problem solving and tool use, selecting trajectories from OpenThoughts-Agent and EnvScaler and evaluating on TBLite and BFCL, respectively. We then evaluate the agents along two complementary dimensions: the post-training performance of the top-ranked subset, reflecting the ability to identify high-value training data, and ranking accuracy, reflecting the ability to predict the relative performance of the selected subsets. In our experiments, selection gains over random selection are limited; agents do not reliably rank their selected groups, and ranking ability does not hold consistently across tasks: Astra identifies the best group in all three tool-use runs but in only one of three terminal runs. Analysis of execution traces on both tasks shows that agents often use similar data signals while interpreting their training value differently. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 任务要求对样本或分组预测微调后的下游收益，并按预测分数选择、排序指定数量的训练子集；之后实际微调模型检验预测价值。 | 本地全文：ASD-0935中与多步行动/研究流程直接相关的原文句子；核验TXT行号 280 | We ask AI agents to select and rank candidate training subsets that can be used to fine-tune a small LLM model. | 高（一手正文；非独立复现） |
| Agent实现与能力 | 本文主要提出评测基准，允许受测Agent检查候选样本、编写分析代码并运行模型前向过程，以预测训练数据价值。 | 本地全文：ASD-0935中与Agent实现与能力直接相关的原文句子；核验TXT行号 280 | Agents are allowed to inspect the data, write and execute analysis code, and run model forward passes, but can not train the model or access the actual evaluation tasks. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 基准比较Agent的数据筛选与收益预测，并以实际训练后的下游表现检验排序质量；具体数据和模型设置按任务定义。 | 本地全文：ASD-0935中与实验任务与验证设置直接相关的原文句子；核验TXT行号 4176 | Predict, for every sample in the dataset, its expected value for SFT (how much it would improve the downstream benchmark if trained on), and use that prediction to SELECT n_groups groups of exactly group_size rows each, ordered so that: after training each group with the fixed recipe, benchmark score goes from high to low as the group index goes from 1 to n_groups (group 1 best, group n_groups worst). | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 论文把数据价值预测和子集选择作为核心能力测量；解读结果时需区分预测排名质量与最终微调性能。 贡献是将训练数据选择及效果预估作为AI Scientist能力的基础测试对象，提供可执行代码的评测环境。 | 本地全文中包含该原句的位置；核验TXT行号 280 | We then fine-tune the base model on each selected subset and evaluate its post-training performance under a standardized protocol. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

DataSense-Bench研究Agent是否具备数据选择能力，并能预测候选训练数据对模型表现的价值。基准要求Agent为微调小型语言模型选择并排序训练子集，允许检查数据、编写和运行分析代码及模型前向计算。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。DataSense-Bench研究Agent是否具备数据选择能力，并能预测候选训练数据对模型表现的价值。基准要求Agent为微调小型语言模型选择并排序训练子集，允许检查数据、编写和运行分析代码及模型前向计算。
  - 原文位置：本地全文：ASD-0935中与研究目标/科学问题直接相关的原文句子；核验TXT行号 275；引文：As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench11 1 Code and Project page. to study this capability through the fundamental problem of data selection and performance forecasting in machine learning. We ask AI agents to select and rank candidate training subsets that can be used to fine-tune a small LLM model. Agents are allowed to inspect the data, write and execute analysis code, and run model forward passes, but can not train the model or access the actual evaluation tasks. We then fine-tune the base model on each selected subset and evaluate its post-training performance under a standardized protocol. We instantiate the benchmark in terminal problem solving and tool use, selecting trajectories from OpenThoughts-Agent and EnvScaler and evaluating on TBLite and BFCL, respectively. We then evaluate the agents along two complementary dimensions: the post-training performance of the top-ranked subset, reflecting the ability to identify high-value training data, and ranking accuracy, reflecting the ability to predict the relative performance of the selected subsets. In our experiments, selection gains over random selection are limited; agents do not reliably rank their selected groups, and ranking ability does not hold consistently across tasks: Astra identifies the best group in all three tool-use runs but in only one of three terminal runs. Analysis of execution traces on both tasks shows that agents often use similar data signals while interpreting their training value differently.
- 多步行动过程：yes。任务要求对样本或分组预测微调后的下游收益，并按预测分数选择、排序指定数量的训练子集；之后实际微调模型检验预测价值。
  - 原文位置：本地全文：ASD-0935中与多步行动/研究流程直接相关的原文句子；核验TXT行号 280；引文：We ask AI agents to select and rank candidate training subsets that can be used to fine-tune a small LLM model.
- 至少一种Agent能力：yes。本文主要提出评测基准，允许受测Agent检查候选样本、编写分析代码并运行模型前向过程，以预测训练数据价值。
  - 原文位置：本地全文：ASD-0935中与Agent实现与能力直接相关的原文句子；核验TXT行号 280；引文：Agents are allowed to inspect the data, write and execute analysis code, and run model forward passes, but can not train the model or access the actual evaluation tasks.
- 明确科研流程角色：yes。基准比较Agent的数据筛选与收益预测，并以实际训练后的下游表现检验排序质量；具体数据和模型设置按任务定义。
  - 原文位置：本地全文：ASD-0935中与实验任务与验证设置直接相关的原文句子；核验TXT行号 4176；引文：Predict, for every sample in the dataset, its expected value for SFT (how much it would improve the downstream benchmark if trained on), and use that prediction to SELECT n_groups groups of exactly group_size rows each, ordered so that: after training each group with the fixed recipe, benchmark score goes from high to low as the group index goes from 1 to n_groups (group 1 best, group n_groups worst).

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

本文主要提出评测基准，允许受测Agent检查候选样本、编写分析代码并运行模型前向过程，以预测训练数据价值。

### 3.3 自主能力

本文主要提出评测基准，允许受测Agent检查候选样本、编写分析代码并运行模型前向过程，以预测训练数据价值。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是将训练数据选择及效果预估作为AI Scientist能力的基础测试对象，提供可执行代码的评测环境。

### 4.2 系统流程与组件

任务要求对样本或分组预测微调后的下游收益，并按预测分数选择、排序指定数量的训练子集；之后实际微调模型检验预测价值。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

基准比较Agent的数据筛选与收益预测，并以实际训练后的下游表现检验排序质量；具体数据和模型设置按任务定义。

### 5.2 基线、指标与结果

论文把数据价值预测和子集选择作为核心能力测量；解读结果时需区分预测排名质量与最终微调性能。

### 5.3 科学贡献与证据强度

贡献是将训练数据选择及效果预估作为AI Scientist能力的基础测试对象，提供可执行代码的评测环境。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“DataSense-Bench: The First Step Toward an AI Scientist”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

基准聚焦机器学习数据子集与小模型微调，不能直接代表Agent理解所有数据类型或完整科研流程的能力。

## 8. 对综述写作的价值

可用于综述“DataSense-Bench: The First Step Toward an AI Scientist”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

DataSense-Bench测试Agent能否挑选并排序有助于微调模型的训练数据。

### 9.2 速记版 pipeline

任务要求对样本或分组预测微调后的下游收益，并按预测分数选择、排序指定数量的训练子集；之后实际微调模型检验预测价值。

### 9.3 标注字段汇总

```text
paper_id=ASD-0935
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
| 问题开放度 | O2 既定基准 | 基准要求Agent为固定微调任务选择训练子集，任务预先定义 | “select and rank candidate training subsets” · L38 |
| 验证强度 | V1 基准/内部评测 | 以实际微调后的下游表现检验预测，但仍属基准评测 | “fine-tune the base model on each selected subset” · L36 |
| 系统自主性 | L1 任务助手 | Agent预测数据价值并选择子集，但不自主推进完整研究流程 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
