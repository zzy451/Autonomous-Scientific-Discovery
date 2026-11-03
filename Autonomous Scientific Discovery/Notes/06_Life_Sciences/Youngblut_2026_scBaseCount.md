# scBaseCount: An AI agent-curated, standardized, auto-updated single-cell data repository

**论文信息**

- ID：ASD-0901
- 标题：scBaseCount: An AI agent-curated, standardized, auto-updated single-cell data repository
- 作者：Nicholas D. Youngblut; Christopher Carpenter; Arshia Nayebnazar; Abhinav Adduri; Rohan Shah; Chiara Ricci-Tam; Jaanak Prashar; Rajesh Ilango; Noam Teyssier; Silvana Konermann; Patrick D. Hsu; Alexander Dobin; Dave P. Burke; Hani Goodarzi; Yusuf H. Roohani
- 年份：2026
- 来源 / venue：Cell
- DOI / arXiv / URL：https://doi.org/10.1016/j.cell.2026.08.025
- 一手阅读来源：https://www.biorxiv.org/content/early/2025/05/06/2025.02.27.640494.source.xml
- 来源层级：全文
- 阅读版本：bioRxiv v2, 2025-05-06, DOI 10.1101/2025.02.27.640494；与Cell 2026版同一项目的早期全文。资源规模及部分作者/题名有变化，未读到Cell最终全文。
- 阅读版本题名：scBaseCount: an AI agent-curated, uniformly processed, and continually expanding single cell data repository
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/scBaseCount_v2.xml
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 2026出版版身份和研究对象 | Cell DOI 10.1016/j.cell.2026.08.025，题名scBaseCount，对象为单细胞RNA-seq资源。 | Cell/PubMed PMID 42753696摘要及Europe PMC记录 | high |
| 找到同一bioRxiv DOI的v1和v2全文 | DOI 10.1101/2025.02.27.640494；API返回v1（2025-03-04）及v2（2025-05-06）。v2题名scBaseCount，且标注存在早期版本。 | bioRxiv details API及v1/v2 JATS XML首页 | high |
| 全文明确给出层级Agent架构 | SRAgent是基于LangGraph和LLM的层级agentic workflow，使用专门工具检索SRA。 | bioRxiv v2 Results 2.2，SRAgent workflow | high |
| Agent通过多种检索工具发现数据并抽取元数据 | 列出eSearch、eSummary、eFetch、eLink、NCBI HTML scraping、SRA BigQuery、sra-stat和fastq-dump；持续挖掘10X数据并保存organism、tissue、disease、perturbation等元数据。 | bioRxiv v2 Results 2.2及Figure 2A图注 | high |
| 作者实现标准化reads处理环节 | scRecounter用Nextflow处理原始单细胞reads，使用STARsolo比对并自动检测barcode参数，产出统一表达矩阵。 | bioRxiv v2 Figure 2B图注及Methods 5.1 | high |
| 全文报告数据规模与Agent标注核验 | 识别63,892项SRA experiments、重处理30,387项、资源超过2.3亿细胞；自动组织注释与CELLxGENE标签对照多数一致。 | bioRxiv v2 Results 2.1及Figure 1D图注 | high |
| 作者在全文中明确列出项目代码 | 列出SRAgent、scRecounter和scBaseCount_analysis三个ArcInstitute GitHub仓库；旧组织路径目前访问返回404。 | bioRxiv v2 Data and Code Availability 4.2 | high |
| 预印本和出版版存在版本变化 | 预印本正文称资源超过2.3亿细胞、21类生物和72种组织；Cell摘要称超过5.02亿细胞、27类和75种组织。Agent工作流主张一致，不能推断所有实现细节未变。 | bioRxiv v2与Cell 2026摘要比较 | high |

## 0. 摘要翻译

Cell摘要称 scBaseCount 使用 AI agent 发现单细胞数据集、提取元数据并标准化处理，建立覆盖27个生物类群、75种组织、超过5.02亿细胞的资源。统一处理支持跨实验对齐，并可测量内含子、外显子和非编码基因表达。同作者谱系bioRxiv v2全文提供了SRAgent多工具层级工作流的细节。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
同作者谱系bioRxiv v2全文描述SRAgent为基于LangGraph的层级ReAct agent工作流，异步调用多种NCBI/SRA工具发现数据、抽取并统一元数据，持续扩充资源；随后scRecounter标准化处理原始测序数据。Cell摘要沿用Agent发现、元数据提取及标准化处理这一核心主张。预印本更名与资源规模较小，故将其作为相关版本证据并保留版本限制。

### 1.2 排除风险检查

固定代码06.03.04单细胞生物学。对象为单细胞转录组、SRA数据集与跨实验标准化，支持06；虽抽取disease元数据，但无疾病诊断或治疗任务，不分配07。邻近一般数据库/数据工程论文及01.04通用方法；本文有明确生物数据发现、注释与处理中的多步Agent行动，纳入依据充分。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.03.04
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

bioRxiv v2报告SRAgent识别63,892项SRA experiments、43,587个10X文库，整合后识别49,646项并重处理30,387项，形成超过2.3亿细胞资源；自动组织标签与CELLxGENE标签比较多数一致。Cell摘要报告后续扩展至超过5.02亿细胞、27类生物和75种组织。早期量化结果不视作出版版所有性能的直接验证。

### 2.3 容易混淆的边界

固定代码06.03.04单细胞生物学。对象为单细胞转录组、SRA数据集与跨实验标准化，支持06；虽抽取disease元数据，但无疾病诊断或治疗任务，不分配07。邻近一般数据库/数据工程论文及01.04通用方法；本文有明确生物数据发现、注释与处理中的多步Agent行动，纳入依据充分。

## 3. Agent 系统与科研流程角色

同作者谱系bioRxiv v2全文描述SRAgent为基于LangGraph的层级ReAct agent工作流，异步调用多种NCBI/SRA工具发现数据、抽取并统一元数据，持续扩充资源；随后scRecounter标准化处理原始测序数据。Cell摘要沿用Agent发现、元数据提取及标准化处理这一核心主张。预印本更名与资源规模较小，故将其作为相关版本证据并保留版本限制。

科研流程与自主能力以本文实际行动和工具调用为依据：

bioRxiv v2将系统分为相接的两条工作流。SRAgent是基于LangGraph的层级ReAct agent，异步调用eSearch、eSummary、eFetch、eLink、NCBI HTML scraping、SRA BigQuery、sra-stat和fastq-dump，发现公开10X项目、抽取organism/tissue/disease/perturbation等元数据并写入关系数据库。scRecounter使用Nextflow与STARsolo识别化学版本、统一处理reads并生成表达矩阵。

## 4. 方法设计

### 4.1 方法动机与设计

建立单细胞RNA-seq数据资源，并以Agent自动发现SRA项目、统一元数据、支撑后续标准化处理和持续更新。

### 4.2 系统流程与组件

bioRxiv v2将系统分为相接的两条工作流。SRAgent是基于LangGraph的层级ReAct agent，异步调用eSearch、eSummary、eFetch、eLink、NCBI HTML scraping、SRA BigQuery、sra-stat和fastq-dump，发现公开10X项目、抽取organism/tissue/disease/perturbation等元数据并写入关系数据库。scRecounter使用Nextflow与STARsolo识别化学版本、统一处理reads并生成表达矩阵。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

bioRxiv v2报告SRAgent识别63,892项SRA experiments、43,587个10X文库，整合后识别49,646项并重处理30,387项，形成超过2.3亿细胞资源；自动组织标签与CELLxGENE标签比较多数一致。Cell摘要报告后续扩展至超过5.02亿细胞、27类生物和75种组织。早期量化结果不视作出版版所有性能的直接验证。

### 5.2 基线、指标与结果

bioRxiv v2报告SRAgent识别63,892项SRA experiments、43,587个10X文库，整合后识别49,646项并重处理30,387项，形成超过2.3亿细胞资源；自动组织标签与CELLxGENE标签比较多数一致。Cell摘要报告后续扩展至超过5.02亿细胞、27类生物和75种组织。早期量化结果不视作出版版所有性能的直接验证。

### 5.3 科学贡献与证据强度

建立单细胞RNA-seq数据资源，并以Agent自动发现SRA项目、统一元数据、支撑后续标准化处理和持续更新。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与单细胞数据资源整合、SRA元数据整理及自动化组学处理相关。Agent参与具体生物数据发现和注释，scRecounter承担标准化分析流水线。

## 7. 局限性与风险

详细全文来自2025年bioRxiv v2，不是Cell 2026出版版全文；出版版作者表和资源规模有变化，不能假设流程细节完全相同。bioRxiv v1 HTML及v1/v2 JATS XML已取得，PDF请求超时。论文列出的旧ArcInstitute GitHub路径目前返回404。

## 8. 对综述写作的价值

可作为科学数据资源中Agent承担数据库发现、元数据管理和组学处理任务的实例；版本差异应在正式笔记说明。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

自动更新单细胞数据资源

### 9.2 速记版 pipeline

bioRxiv v2将系统分为相接的两条工作流。SRAgent是基于LangGraph的层级ReAct agent，异步调用eSearch、eSummary、eFetch、eLink、NCBI HTML scraping、SRA BigQuery、sra-stat和fastq-dump，发现公开10X项目、抽取organism/tissue/disease/perturbation等元数据并写入关系数据库。scRecounter使用Nextflow与STARsolo识别化学版本、统一处理reads并生成表达矩阵。

### 9.3 标注字段汇总

```text
paper_id=ASD-0901
inclusion_status=included
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.04
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

已阅读同一工作的bioRxiv v2全文，足以核实Agent流程和06.03.04分类；Cell最终正文仍未取得，今后引用出版版的实现或结果细节需再核对。预印本2.3亿细胞与Cell摘要5.02亿细胞分别记录，不混用。


## 2026-10-29 PR剩余差异复核

- 来源深度：`target_preprint_fulltext`。本轮涉及1条差异，其中1条已判定，0条待核。摘要或图注支持的判定不代表全文已逐页核验。

- 原1664行号 `1140`：`retain_current`。Directly retrieved bioRxiv v2 JATS full text verifies hierarchical ReAct SRAgent, asynchronous retrieval tools, continuous discovery of 10X single-cell projects and metadata curation into a database, linked to standardized RNA-seq processing. This settles the narrow agent/classification question under 06.03.04. Final Cell full text remains unverified: 230 million cells and 30,387 entries are v2-specific values and must not be presented as final-publication scale.
  - 位置：bioRxiv v2 Results, Automated single-cell data discovery and annotation using SRAgent；来源：https://doi.org/10.1016/j.cell.2026.08.025

逐条引文、来源文件和限制见 `Coverage_Check/pr1_82_recheck_2026-10-29/final_review.json`。保留现有分类不等于全部分类边界已消除。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/06_Life_Sciences/ASD-0901_scBaseCount_An_AI_agent_curated_standardized_auto_updated_single_cell_data_repository_preprint_v2.pdf`，共14页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://www.biorxiv.org/content/10.1101/2025.02.27.640494v2.full.pdf
- 版本：bioRxiv preprint v2, 2025-05-06; not the Cell 2026 version of record。
- 此次取得的是2025年5月6日bioRxiv v2，不是2026年Cell正式发表版本；实验规模及数据应按对应版本引用。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 从SRA自动识别单细胞数据集并标准化处理，元数据标签可与CELLxGENE等已有资源核对 | “自动组织注释与CELLxGENE标签对照多数一致” · L30 |
| 验证强度 | V2 计算/仿真/回顾性 | Agent标注与已有标签比对，产出统一表达矩阵，属计算处理和回顾性数据整合 | “识别63,892项SRA experiments、重处理30,387项” · L30 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：否
- 置信度：medium；需全文复核：是；争议记录：无
- 复核状态：待专家复核：需全文复核
