# Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket Retrieval

**论文信息**

- ID：ASD-1107
- 标题：Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket Retrieval
- 作者：Min, Junghyun; Uzunalioglu, Huseyin; Trabelsi, Mohamed
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.13073
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1107.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Junghyun_2026_Autonomous_Research_for_Open_Ended_Problems_A_Case_Study_ASD1107.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象 | 电信工单检索提供表示、架构及训练数据生成的开放式机器学习研究任务。 | 全文第291行；核验TXT行号 291 | In this paper, we explore how autonomous research can be adapted to solve open-ended, industry-grade ML problems, by considering a case study: telecom ticket retrieval, an open-ended task with degrees of freedom in representation, architecture, and training data generation. | 高（一手正文；非独立复现） |
| 实验流程 | 每轮提出模型方案、实现并执行实验，再评估和验证改进。 | 全文第340行；核验TXT行号 340 | In each of its iterations, an LLM-powered agent proposes a new ML system design that could improve on the metric (i.e. lower the loss), implements and runs the experiment, before evaluating the system and verifying the improvement. | 高（一手正文；非独立复现） |
| Agent能力 | Agent读取代码库、修改训练或架构参数，运行试验并依据性能反馈行动。 | 全文第469行；核验TXT行号 469 | The agent, a command-line interface tool with an underlying LLM (e.g. Claude Code, Cursor, and Pi), operates through an iterative process: it reads the repository state, modifies training or architecture parameters, runs trials, and evaluates performance. | 高（一手正文；非独立复现） |
| 案例设置 | 作者以电信工单检索案例研究三个研究问题；此句不单独证明人类治理机制。 | 全文第389行；核验TXT行号 389 | To investigate RQs 1-3, we perform a case study on a prime example of an open-ended task: telecom ticket retrieval | 高（一手正文；非独立复现） |
| 作者报告结果 | 作者报告LLM推理并未显著影响下游性能，不能把完整Agent循环自动等同有效改进。 | 全文第1161行；核验TXT行号 1161 | our results demonstrate that LLM reasoning does not substantially affect downstream performance. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

实证研究以电信工单检索为开放式机器学习研究任务，比较自动研究代理如何提出并检验表示、架构及训练数据生成方案。代理在代码库中修改模型和数据处理并运行检索实验，依据验证性能反馈迭代。工业数据来源不改变其ML研究对象与实验性流程。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。实证研究以电信工单检索为开放式机器学习研究任务，比较自动研究代理如何提出并检验表示、架构及训练数据生成方案。代理在代码库中修改模型和数据处理并运行检索实验，依据验证性能反馈迭代。工业数据来源不改变其ML研究对象与实验性流程。
  - 原文位置：全文第291行；核验TXT行号 291；引文：In this paper, we explore how autonomous research can be adapted to solve open-ended, industry-grade ML problems, by considering a case study: telecom ticket retrieval, an open-ended task with degrees of freedom in representation, architecture, and training data generation.
- 多步行动过程：yes。代理在代码修改、运行实验、读取评估反馈后决定后续迭代。
  - 原文位置：全文第340行；核验TXT行号 340；引文：In each of its iterations, an LLM-powered agent proposes a new ML system design that could improve on the metric (i.e. lower the loss), implements and runs the experiment, before evaluating the system and verifying the improvement.
- 至少一种Agent能力：yes。系统能调用代码库、训练/评测任务及持续实验记忆，具备提出方案、执行和分析结果的能力。
  - 原文位置：全文第469行；核验TXT行号 469；引文：The agent, a command-line interface tool with an underlying LLM (e.g. Claude Code, Cursor, and Pi), operates through an iterative process: it reads the repository state, modifies training or architecture parameters, runs trials, and evaluates performance.
- 明确科研流程角色：yes。代理承担机器学习研究中的假设提出、实验执行、模型评估和修订；人工保留范围明确的治理门。
  - 原文位置：全文第389行；核验TXT行号 389；引文：To investigate RQs 1-3, we perform a case study on a prime example of an open-ended task: telecom ticket retrieval

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02.13 机器学习；01.02.15 自然语言处理
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- 电信工单文档检索模型及其架构、表示和训练数据生成策略

### 2.3 容易混淆的边界

实证研究以电信工单检索为开放式机器学习研究任务，比较自动研究代理如何提出并检验表示、架构及训练数据生成方案。代理在代码库中修改模型和数据处理并运行检索实验，依据验证性能反馈迭代。工业数据来源不改变其ML研究对象与实验性流程。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



实证研究以电信工单检索为开放式机器学习研究任务，比较自动研究代理如何提出并检验表示、架构及训练数据生成方案。代理在代码库中修改模型和数据处理并运行检索实验，依据验证性能反馈迭代。工业数据来源不改变其ML研究对象与实验性流程。

### 3.3 自主能力

系统能调用代码库、训练/评测任务及持续实验记忆，具备提出方案、执行和分析结果的能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

对象是电信信息检索应用而非基础科学对象。虽然包含研究循环，Agent科研角色与工业问题求解边界需要主控按纳入规则裁定，故needs_review。

### 4.2 系统流程与组件

实证研究以电信工单检索为开放式机器学习研究任务，比较自动研究代理如何提出并检验表示、架构及训练数据生成方案。代理在代码库中修改模型和数据处理并运行检索实验，依据验证性能反馈迭代。工业数据来源不改变其ML研究对象与实验性流程。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

实证研究以电信工单检索为开放式机器学习研究任务，比较自动研究代理如何提出并检验表示、架构及训练数据生成方案。代理在代码库中修改模型和数据处理并运行检索实验，依据验证性能反馈迭代。工业数据来源不改变其ML研究对象与实验性流程。 结果必须区分离线评估、线上A/B和人工上线决策。

### 5.2 基线、指标与结果

以工单检索任务和领域指标评估不同方案，并讨论开放式目标、数据/系统约束造成的失败与人工介入。

### 5.3 科学贡献与证据强度

对象是电信信息检索应用而非基础科学对象。虽然包含研究循环，Agent科研角色与工业问题求解边界需要主控按纳入规则裁定，故needs_review。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与一般LLM代理、科学工作流自动化及该领域既有基准/模型相关；本文的具体差异见上述任务设计和验证设置。

## 7. 局限性与风险

本文结果受其数据、模拟环境、评测指标和实验预算限制；不得将基准或仿真表现直接外推为真实部署成效。

## 8. 对综述写作的价值

可用于综述讨论该类Agent的研究对象、工作流角色和验证边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

本文以电信工单检索为开放式工业机器学习案例，探讨自主研究系统如何处理搜索空间较大、目标复杂的真实问题。代理围绕检索系统提出方案、编写代码并运行评估，作者分析将端到端自动研究从受限基准迁移到行业问题时的困难。

### 9.2 速记版 pipeline

实证研究以电信工单检索为开放式机器学习研究任务，比较自动研究代理如何提出并检验表示、架构及训练数据生成方案。代理在代码库中修改模型和数据处理并运行检索实验，依据验证性能反馈迭代。工业数据来源不改变其ML研究对象与实验性流程。

### 9.3 标注字段汇总

```text
paper_id=ASD-1107
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02.13;01.02.15
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 电信工单检索改进可由验证数据核对 | “telecom ticket retrieval” · L42 |
| 验证强度 | V2 计算/仿真/回顾性 | 工单数据评估但作者报告效果不显著 | “LLM reasoning does not substantially affect” · L25 |
| 系统自主性 | L2 闭环执行者 | Agent修改架构和数据处理并运行试验 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
