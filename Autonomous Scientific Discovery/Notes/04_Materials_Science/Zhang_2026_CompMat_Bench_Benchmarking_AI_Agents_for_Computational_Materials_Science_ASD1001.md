# CompMat-Bench: Benchmarking AI Agents for Computational Materials Science

**论文信息**

- ID：ASD-1001
- 标题：CompMat-Bench: Benchmarking AI Agents for Computational Materials Science
- 作者：Chenmu Zhang; Levi Felix; Jun-Jie Zhang; Xingfu Li; Xuelian Jiang; Tao Jiang; Subhendu Mishra; Xixi Qin; Boris Yakobson
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.00636
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1001.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Zhang_2026_CompMat_Bench_Benchmarking_AI_Agents_for_Computational_Materials_Science_ASD1001.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | CompMat-Bench从近期计算材料论文提取94项任务，要求Agent完成通向科学目标的研究步骤。为避免重复昂贵模拟，基准事先复现研究步骤，将输入准备和输出分析作为可评分任务，并以固定规则和地面真值评分。评估设置涵盖单任务及关联工作流、完整或简化方法指导。 | 摘要；TXT第292行；核验TXT行号 292 | Evaluating AI agents on scientific research tasks is constrained by the time and resources required for the underlying experiments or calculations. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第297行；核验TXT行号 297 | We introduce CompMat-Bench, a benchmark of 94 tasks derived from recently published computational materials studies, each asking agents to complete a step toward achieving the study’s scientific goal. | 高（一手正文；非独立复现） |
| Agent能力与行动 | CompMat-Bench: Benchmarking AI Agents for Computational Materials Science。系统角色与能力：基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第311行；核验TXT行号 311 | Both longer workflows and reduced guidance can limit agent performance, but in different ways for different agents: they lower the pass rates of the weaker agents, whereas the strongest agent falls only when a long workflow is combined with reduced guidance. | 高（一手正文；非独立复现） |
| 验证与结果 | 在94项任务完整指导的单任务条件下，三类LLM Agent通过率为66.0–90.4%。较长工作流或减少指导会降低部分Agent表现；失败分析发现多数错误属于科学推理错误，而非软件操作错误。 | 摘要；TXT第303行；核验TXT行号 303 | The reproduced inputs and results serve as ground truth for grading agents with fixed rules, without an LLM judge. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 支持综述讨论基于真实已发表研究步骤的可复现评测，以及科学错误与软件错误的区分。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第294行；核验TXT行号 294 | In computational materials research, repeating the same expensive simulations across agents and trials can make evaluation impractical. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

CompMat-Bench从近期计算材料论文提取94项任务，要求Agent完成通向科学目标的研究步骤。为避免重复昂贵模拟，基准事先复现研究步骤，将输入准备和输出分析作为可评分任务，并以固定规则和地面真值评分。评估设置涵盖单任务及关联工作流、完整或简化方法指导。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。CompMat-Bench从近期计算材料论文提取94项任务，要求Agent完成通向科学目标的研究步骤。为避免重复昂贵模拟，基准事先复现研究步骤，将输入准备和输出分析作为可评分任务，并以固定规则和地面真值评分。评估设置涵盖单任务及关联工作流、完整或简化方法指导。
  - 原文位置：摘要；TXT第292行；核验TXT行号 292；引文：Evaluating AI agents on scientific research tasks is constrained by the time and resources required for the underlying experiments or calculations.
- 多步行动过程：yes。基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第297行；核验TXT行号 297；引文：We introduce CompMat-Bench, a benchmark of 94 tasks derived from recently published computational materials studies, each asking agents to complete a step toward achieving the study’s scientific goal.
- 至少一种Agent能力：yes。CompMat-Bench: Benchmarking AI Agents for Computational Materials Science。系统角色与能力：基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第311行；核验TXT行号 311；引文：Both longer workflows and reduced guidance can limit agent performance, but in different ways for different agents: they lower the pass rates of the weaker agents, whereas the strongest agent falls only when a long workflow is combined with reduced guidance.
- 明确科研流程角色：yes。在94项任务完整指导的单任务条件下，三类LLM Agent通过率为66.0–90.4%。较长工作流或减少指导会降低部分Agent表现；失败分析发现多数错误属于科学推理错误，而非软件操作错误。
  - 原文位置：摘要；TXT第303行；核验TXT行号 303；引文：The reproduced inputs and results serve as ground truth for grading agents with fixed rules, without an LLM judge.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.01 材料基础；04.02 结构材料与无机材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是计算材料科学研究步骤和Agent基准，归04.01/04.02。基准评价能力，不是Agent本身完成新材料发现。

### 2.3 容易混淆的边界

对象是计算材料科学研究步骤和Agent基准，归04.01/04.02。基准评价能力，不是Agent本身完成新材料发现。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

CompMat-Bench: Benchmarking AI Agents for Computational Materials Science。系统角色与能力：基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

CompMat-Bench: Benchmarking AI Agents for Computational Materials Science。系统角色与能力：基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

支持综述讨论基于真实已发表研究步骤的可复现评测，以及科学错误与软件错误的区分。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

在94项任务完整指导的单任务条件下，三类LLM Agent通过率为66.0–90.4%。较长工作流或减少指导会降低部分Agent表现；失败分析发现多数错误属于科学推理错误，而非软件操作错误。

### 5.2 基线、指标与结果

在94项任务完整指导的单任务条件下，三类LLM Agent通过率为66.0–90.4%。较长工作流或减少指导会降低部分Agent表现；失败分析发现多数错误属于科学推理错误，而非软件操作错误。

### 5.3 科学贡献与证据强度

支持综述讨论基于真实已发表研究步骤的可复现评测，以及科学错误与软件错误的区分。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文与已有AI科学家/材料基准相关，选择已发表计算材料研究中的真实步骤，并以预计算结果和固定规则减少重复昂贵模拟及LLM裁判偏差。

## 7. 局限性与风险

作者及读者可确认的适用边界：基准预先复现昂贵模拟，并主要考核输入准备和输出分析步骤；因此不能替代真实长周期、含物理执行的端到端发现评估。

## 8. 对综述写作的价值

支持综述讨论基于真实已发表研究步骤的可复现评测，以及科学错误与软件错误的区分。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

CompMat-Bench从近期计算材料论文提取94项任务，要求Agent完成通向科学目标的研究步骤。

### 9.2 速记版 pipeline

基准提供科学任务、已有模拟输出和方法信息，Agent准备计算输入或分析结果；因昂贵模拟已预先执行，评测时不必重新运行。固定规则基于复现结果评分，比较不同Agent在单任务、长工作流及不同指导条件下的表现。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-1001
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.01;04.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.04` 材料计算与材料信息学；二级：`04.01`。
- 原文位置：PDF p.1。
- 判定：94个计算材料任务的执行和复现评估，归材料计算。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
