# From Prompt to Pipeline: A Comparative Evaluation of Large Language Model Coding Agents for Reproducible Bioinformatics Pipeline Construction

**论文信息**

- ID：ASD-1025
- 标题：From Prompt to Pipeline: A Comparative Evaluation of Large Language Model Coding Agents for Reproducible Bioinformatics Pipeline Construction
- 作者：Paul R. Munn; Jennifer K. Grenier
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.11.751004
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1025.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Munn_2026_From_Prompt_to_Pipeline_A_Comparative_Evaluation_of_Large_ASD1025.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 具体科研任务是CUT&Tag测序数据的可复现生物信息学分析。 | Full text, local TXT line 32；核验TXT行号 32 | paired-end CUT&Tag data | 高（一手正文；非独立复现） |
| 多步科研流程 | Agent从自然语言任务构建包含多个分析阶段的Nextflow流程。 | Full text, local TXT line 31；核验TXT行号 31 | constructing a Nextflow DSL2 pipeline | 高（一手正文；非独立复现） |
| Agent能力 | 三个编码Agent接收同一详尽提示，并生成实现供执行和检查。 | Full text, local TXT line 34；核验TXT行号 34 | Each system received the same detailed CRAFT-style prompt | 高（一手正文；非独立复现） |
| 验证结果 | 对照手工参考流程后，三套系统均未完全完成指定分析输出。 | Full text, local TXT line 37；核验TXT行号 37 | none fully satisfied the requested analysis | 高（一手正文；非独立复现） |
| 限制与边界 | 作者指出复杂流程仍需专家复核；该研究是科研软件构建评测。 | Full text, local TXT line 45；核验TXT行号 45 | they do not eliminate the need for expert review | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文比较Biomni、Claude Code和Codex三种编码Agent，要求其为paired-end CUT&Tag数据构建可复现的Nextflow DSL2分析流水线。评估检查从质控、比对和peak calling到注释及MultiQC报告的实现、运行和输出质量。Agent能够加速脚手架和文档构建，但完整外观并不保证分析实现正确或符合生物学要求。研究只覆盖一个复杂任务，结论不能推广到所有生物信息工作流。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是构建CUT&Tag生物信息学流程，具有具体组学分析对象。
  - 原文位置：Full text, local TXT line 32；核验TXT行号 32；引文：paired-end CUT&Tag data
- 多步行动过程：yes。任务要求生成并组织多个测序处理、定量和报告阶段。
  - 原文位置：Full text, local TXT line 31；核验TXT行号 31；引文：constructing a Nextflow DSL2 pipeline
- 至少一种Agent能力：yes。编码Agent生成流程实现，随后执行并依据参考实现检查输出。
  - 原文位置：Full text, local TXT line 34；核验TXT行号 34；引文：Each system received the same detailed CRAFT-style prompt
- 明确科研流程角色：yes。Agent在科研软件工程中担任流程构建助手；结果同时显示仍需专家复核。
  - 原文位置：Full text, local TXT line 45；核验TXT行号 45；引文：they do not eliminate the need for expert review

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.01 基因组学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入CUT&Tag表观基因组学数据分析对象模块，同时记录其主要贡献是Agent软件工程评测；不把能生成pipeline等同于发现新生物学结果。

### 2.3 容易混淆的边界

归入CUT&Tag表观基因组学数据分析对象模块，同时记录其主要贡献是Agent软件工程评测；不把能生成pipeline等同于发现新生物学结果。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

作者让Biomni、Claude Code和Codex在同一CUT&Tag任务中构建Nextflow DSL2分析管线，比较编码Agent在软件选择、流程编排、文档和质量控制方面的实际产物。

### 3.3 自主能力

编码Agent生成流程实现，随后执行并依据参考实现检查输出。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是对科学编码Agent是否能产出可复现生物信息流水线作同任务比较，并揭示执行正确性与领域分析恰当性之间的差距。

### 4.2 系统流程与组件

任务要求从paired-end CUT&Tag输入实现分析步骤、运行环境和可解释QC；研究检查生成管线能否执行及输出是否正确，并对提示具体程度和完成质量作比较。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

采用单一复杂CUT&Tag任务，对三种Agent产生的Nextflow管线进行执行、实现审查及结果检查；这是具体组学工作流案例而非跨任务基准。

### 5.2 基线、指标与结果

Agent能快速搭建脚手架、文档和常规组件，但外观完整的管线仍可能有实现或分析选择问题；作者结论是需明确生物问题、参数和QC要求，专家复核不可省略。

### 5.3 科学贡献与证据强度

贡献是对科学编码Agent是否能产出可复现生物信息流水线作同任务比较，并揭示执行正确性与领域分析恰当性之间的差距。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较一般代码生成基准，本文以CUT&Tag生物学工作流作为端到端任务，检查Nextflow执行产物和分析质量，而不只统计代码是否生成。

## 7. 局限性与风险

仅测试一个复杂任务，模型版本、提示词和运行环境会影响结果；样本数据与管线要求不能覆盖RNA-seq、单细胞等其他工作流。

## 8. 对综述写作的价值

可用于比较科学编码Agent生成CUT&Tag管线的执行正确性、领域合理性和可复现性要求。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

三种编码Agent在同一CUT&Tag任务上构建Nextflow流水线，并接受执行与分析产物检查。结果显示Agent可加快常规搭建，却仍会产生实现或领域选择错误；研究范围限于单一任务。

### 9.2 速记版 pipeline

任务要求从paired-end CUT&Tag输入实现分析步骤、运行环境和可解释QC；研究检查生成管线能否执行及输出是否正确，并对提示具体程度和完成质量作比较。

### 9.3 标注字段汇总

```text
paper_id=ASD-1025
inclusion_status=to_read
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 流水线正确性可由测试数据检验 | “paired-end CUT&Tag data” · L36 |
| 验证强度 | V2 计算/仿真/回顾性 | 执行检查和专家审阅 | “none fully satisfied the requested analysis” · L24 |
| 系统自主性 | L1 任务助手 | Agent生成代码但由人审阅 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
