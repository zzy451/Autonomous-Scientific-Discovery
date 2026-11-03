# DynaMate: An Autonomous Agent for Protein-Ligand Molecular Dynamics Simulations

**论文信息**

- ID：ASD-1017
- 标题：DynaMate: An Autonomous Agent for Protein-Ligand Molecular Dynamics Simulations
- 作者：Cassandra Masschelein; Salomé Guilbert; Jeremy Goumaz; Bohdan Naida; Ursula Rothlisberger; Philippe Schwaller
- 年份：2026
- 来源 / venue：Research Square preprint
- DOI / arXiv / URL：https://doi.org/10.21203/rs.3.rs-10243410/v1
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1017.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Masschelein_2026_DynaMate_An_Autonomous_Agent_for_Protein_Ligand_Molecular_Dynamics_ASD1017.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | DynaMate针对蛋白及蛋白-配体系统自动设置和运行分子动力学，并支持结合自由能计算。 | Full text, extracted character offset 2020；核验TXT行号 64 | Here, we present DynaMate, a 21 modular multi-agent framework that autonomously designs and executes com- 22 plete MD workﬂows for both protein and protein-ligand systems | 高（一手正文；非独立复现） |
| method or agent workflow | 框架结合动态工具调用、网络与文献检索、自我纠错，自动完成MD设置及执行。 | Full text, extracted character offset 2277；核验TXT行号 72 | The framework integrates dynamic tool use, web search, literature query via 25 PaperQA, and a self-correcting behavior | 高（一手正文；非独立复现） |
| evaluation design | 评估覆盖15个不同复杂度基准系统，并在827个蛋白及蛋白-配体系统数据集上测试运行成功率。 | 本地原文 TXT 第74行 | We evaluate its performance ﬁrst across 26 ﬁfteen benchmark systems of varying complexity, assessing success rate, eﬃ- 27 ciency, and adaptability. Second, we conﬁrm its robustness by achieving 67% 28 successful executions of MD simulations on a dataset of 827 diverse protein and 29 protein-ligand systems. | 高（一手正文；非独立复现） |
| reported result | 在827个多样系统上，MD模拟成功执行率为67%，并将通常数小时的设置缩短到数分钟。 | 本地原文 TXT 第78行 | Second, we conﬁrm its robustness by achieving 67% 28 successful executions of MD simulations on a dataset of 827 diverse protein and 29 protein-ligand systems. Overall, DynaMate reduces the typical multi-hour setup 30 time to minutes and autonomously resolves common runtime errors through 31 1 iterative reasoning. | 高（一手正文；非独立复现） |
| limitation / boundary | 部分PDB系统会使提供给LLM的工具失败，这些情况需要深层模拟故障诊断和化学或生物推理。 | Full text, extracted character offset 12554；核验TXT行号 336 | the provided tools can fail for some PDB ﬁles. For these biological systems, a 154 deep understanding of the simulation failure mode and chemical or biological reason- 155 ing is required to solve the encountered errors | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文介绍DynaMate，一个用于蛋白及蛋白—配体体系的模块化多Agent分子动力学框架。系统自动设计和执行模拟流程，协调工具调用、作业运行、轨迹分析和MM/PB(GB)SA结合自由能估算；作者在多个复杂度不同的基准体系中考察流程表现，并比较亲和力结果。该工作展示蛋白模拟工作流自动化，但预测精度仍受采样时长、力场和工具限制，计算结果需要实验数据交叉验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是降低蛋白及蛋白-配体分子动力学的技术门槛，并自动运行相关模拟。
  - 原文位置：Full text, extracted character offset 2020；核验TXT行号 64；引文：Here, we present DynaMate, a 21 modular multi-agent framework that autonomously designs and executes com- 22 plete MD workﬂows for both protein and protein-ligand systems
- 多步行动过程：yes。系统需准备结构、设定参数、平衡体系、运行生产模拟并分析结果，是多步计算工作流。
  - 原文位置：Full text, extracted character offset 2277；核验TXT行号 72；引文：The framework integrates dynamic tool use, web search, literature query via 25 PaperQA, and a self-correcting behavior
- 至少一种Agent能力：yes。Agent动态调用工具、检索文献并处理运行错误，具备实际MD任务执行和自我修复能力。
  - 原文位置：Full text, extracted character offset 2277；核验TXT行号 72；引文：The framework integrates dynamic tool use, web search, literature query via 25 PaperQA, and a self-correcting behavior
- 明确科研流程角色：yes。DynaMate承担生物分子模拟及结合亲和力分析的计算科研执行环节。
  - 原文位置：Full text, extracted character offset 2020；核验TXT行号 64；引文：Here, we present DynaMate, a 21 modular multi-agent framework that autonomously designs and executes com- 22 plete MD workﬂows for both protein and protein-ligand systems

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.06 蛋白质科学；07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.02蛋白质结构与药物发现相关计算；研究对象是分子动力学体系及亲和力估算，未提供新药实验验证。

### 2.3 容易混淆的边界

归入06.02蛋白质结构与药物发现相关计算；研究对象是分子动力学体系及亲和力估算，未提供新药实验验证。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

DynaMate以模块化多Agent流程规划和执行蛋白/蛋白-配体分子动力学任务，协调系统设置、作业提交、模拟监控、结果分析和出错处理，并可检索相关文献。

### 3.3 自主能力

Agent动态调用工具、检索文献并处理运行错误，具备实际MD任务执行和自我修复能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把分子动力学准备、运行和误差处理做成可由Agent协调的端到端流程，面向蛋白结构动力学和配体亲和力问题。

### 4.2 系统流程与组件

作者在多个不同复杂度的蛋白及蛋白-配体基准体系上运行模拟，考察完整计算设置、轨迹分析和结合自由能估算；工作流调用常规MD工具并处理计算任务状态。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

论文报告26个基准体系的模拟/结合亲和力任务，并比较自动运行结果与参考数据或既有方法；还给出工具限制相关案例。证据是计算基准验证。

### 5.2 基线、指标与结果

DynaMate能够自动组织多种分子动力学流程并对基准体系进行分析；结合自由能等预测的可靠性随体系、模拟时长和力场/工具而变，不能将自动完成等同高精度。

### 5.3 科学贡献与证据强度

贡献是把分子动力学准备、运行和误差处理做成可由Agent协调的端到端流程，面向蛋白结构动力学和配体亲和力问题。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较仅自动生成MD输入或只做轨迹后处理的工具，DynaMate覆盖模拟前后环节；与一般代码Agent相比，它聚焦特定蛋白模拟软件工具链。

## 7. 局限性与风险

计算量、模拟时长、力场与工具可用性限制结果；部分基准体系显露现有工具边界。模拟预测需与实验结合数据或更长采样交叉验证。

## 8. 对综述写作的价值

可用于讨论蛋白分子动力学Agent的流程自动化、基准验证和模拟精度对实验数据的依赖。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

DynaMate自动准备并运行蛋白和蛋白—配体分子动力学模拟，随后分析轨迹并估算结合自由能。基准测试说明Agent能够编排完整计算流程，但其亲和力预测仍受模拟和物理模型误差影响。

### 9.2 速记版 pipeline

作者在多个不同复杂度的蛋白及蛋白-配体基准体系上运行模拟，考察完整计算设置、轨迹分析和结合自由能估算；工作流调用常规MD工具并处理计算任务状态。

### 9.3 标注字段汇总

```text
paper_id=ASD-1017
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.06;07.04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 蛋白配体分子动力学，答案可由模拟轨迹和结合自由能计算验证 | “在827个多样系统上，MD模拟成功执行率为67%” · L24 |
| 验证强度 | V2 计算/仿真/回顾性 | 在26个基准体系报告模拟结合亲和力任务，并比较自动运行结果与参考数据 | “26个基准体系的模拟/结合亲和力任务” · L101 |
| 系统自主性 | L2 闭环执行者 | 框架结合动态工具调用网络与文献检索自我纠错，自动完成MD设置及执行 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
