# Detailed curation of biological samples and experimental designs for genomics using LLM-supported agentic workflows

**论文信息**

- ID：ASD-1024
- 标题：Detailed curation of biological samples and experimental designs for genomics using LLM-supported agentic workflows
- 作者：Paul Pavlidis; B. Ogan Mancarci; Amanda Maximo; Carlton Yan; Rachel A. Schwartz
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.07.30.741874
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1024.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Pavlidis_2026_Detailed_curation_of_biological_samples_and_experimental_designs_for_ASD1024.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 研究对象是Gemma中人、小鼠和大鼠的转录组研究及其实验元数据。 | Full text, local TXT line 28；核验TXT行号 28 | transcriptomic studies | 高（一手正文；非独立复现） |
| 多步科研流程 | 流程将公开组学数据整理为样本级和实验级注释。 | Full text, local TXT line 30；核验TXT行号 30 | sample- and experiment-level annotations | 高（一手正文；非独立复现） |
| Agent能力 | pipeline将传统程序步骤与LLM策展能力组合，按策展规范生成标注。 | Full text, local TXT line 29；核验TXT行号 29 | uses both traditional (mechanical) and large- language models | 高（一手正文；非独立复现） |
| 验证结果 | 作者比较人工策展表现、成本和速度，并评估500项数据集。 | Full text, local TXT line 33；核验TXT行号 33 | performance is near that of human curators | 高（一手正文；非独立复现） |
| 限制与边界 | 作者仍探索将高风险注释转交人工复核的方法，表明需要质量把关。 | Full text, local TXT line 34；核验TXT行号 34 | triage methods for identifying agent curations that are more likely to contain errors | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文开发LLM支持的策展流程，为Gemma转录组资源整理样本和实验设计元数据，并将字段映射到既定本体。流程处理GEO系列筛选、数据集适用性判断和实验信息抽取；主要分析400个数据集，并在留出的100篇研究上测试。作者将自动策展与人工记录比较，结果接近人工策展水平且成本和速度更有优势。研究限于Gemma/GEO转录组语料，难例仍需人工复核。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。科研目标是整理转录组研究的实验设计和样本元数据。
  - 原文位置：Full text, local TXT line 28；核验TXT行号 28；引文：transcriptomic studies
- 多步行动过程：yes。系统对研究记录进行多层次样本与实验注释，而非回答单一问题。
  - 原文位置：Full text, local TXT line 30；核验TXT行号 30；引文：sample- and experiment-level annotations
- 至少一种Agent能力：yes。自动化工具组合传统处理和LLM，并产出可供质控的策展结果。
  - 原文位置：Full text, local TXT line 29；核验TXT行号 29；引文：uses both traditional (mechanical) and large- language models
- 明确科研流程角色：yes。通过人工基准和500项benchmark研究评估生产就绪度及错误分流。
  - 原文位置：Full text, local TXT line 33；核验TXT行号 33；引文：performance is near that of human curators

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

归入06.03基因组学/转录组学数据研究；成果是数据资源策展自动化，不能误作Agent进行下游机制发现或实验设计验证。

### 2.3 容易混淆的边界

归入06.03基因组学/转录组学数据研究；成果是数据资源策展自动化，不能误作Agent进行下游机制发现或实验设计验证。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

该工作把LLM支持的Agent流程用于Gemma基因组学数据库样本和实验设计策展，从GEO系列发现与筛选开始，抽取样本描述并映射至本体字段，再与人工策展记录比较。

### 3.3 自主能力

自动化工具组合传统处理和LLM，并产出可供质控的策展结果。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是自动化生物样本及实验设计的细粒度整理工作，为大型转录组资源提供可扩展的候选策展流程。

### 4.2 系统流程与组件

主要分析400个数据集，另设100篇研究留出测试；流程涵盖GEO抓取、系列适用性筛选、初步信息提取和实验设计本体标注。研究者人工检查错误并对不同任务的注释/抽取质量评分。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者以人工策展数据作为参照，分别评估样本元数据和实验设计信息提取；测试集按研究留出。评价聚焦策展准确度和工作量可用性，不直接检验下游生物学发现。

### 5.2 基线、指标与结果

系统可处理Gemma中转录组数据再分析所需的系列筛选和元数据标注，并在一系列抽取任务上与现行策展相比较；具体表现随字段和任务难度变化，深度实验设计理解仍需要人工监督。

### 5.3 科学贡献与证据强度

贡献是自动化生物样本及实验设计的细粒度整理工作，为大型转录组资源提供可扩展的候选策展流程。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较只抽取文章关键词或基本样本标签，该研究面向Gemma既有的人工高质量策展和实验设计本体；人工记录既是目标也作为评估参照。

## 7. 局限性与风险

主要数据源和应用场景为Gemma/GEO转录组研究，字段准确依赖论文报告完整性；100项留出集不能代表全部物种、实验类型和文献表达方式。

## 8. 对综述写作的价值

可用于讨论Agent辅助转录组文献策展的人工参照、留出评估和下游生物学用途边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Agent流程自动筛选GEO转录组研究并为Gemma整理样本及实验设计本体字段，以400个数据集和100篇留出研究评估。结果接近人工策展，但文献报告不全和任务类型差异仍要求人工检查。

### 9.2 速记版 pipeline

主要分析400个数据集，另设100篇研究留出测试；流程涵盖GEO抓取、系列适用性筛选、初步信息提取和实验设计本体标注。研究者人工检查错误并对不同任务的注释/抽取质量评分。

### 9.3 标注字段汇总

```text
paper_id=ASD-1024
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
| 问题开放度 | O3 新实例 | 元数据字段可由文献核对 | “transcriptomic studies” · L36 |
| 验证强度 | V2 计算/仿真/回顾性 | 与人工策展记录比对 | “performance is near that of human curators” · L24 |
| 系统自主性 | L1 任务助手 | 系统执行策展任务但人设定规范 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
