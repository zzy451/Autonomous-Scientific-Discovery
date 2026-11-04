# MedKGent: a large language model agent framework for constructing temporally evolving medical knowledge graph

**论文信息**

- ID：ASD-1030
- 标题：MedKGent: a large language model agent framework for constructing temporally evolving medical knowledge graph
- 作者：Duzhen Zhang; Zixiao Wang; Zhong-Zhi Li; Yahan Yu; Shuncheng Jia; Jiahua Dong; Haotian Xu; Xing Wu; Yingying Zhang; Tielin Zhang; Jie Yang; Xiuying Chen; Le Song
- 年份：2026
- 来源 / venue：npj Digital Medicine
- DOI / arXiv / URL：https://doi.org/10.1038/s41746-026-03058-7
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1030.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Zhang_2026_MedKGent_a_large_language_model_agent_framework_for_constructing_ASD1030.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 科学目标是从医学文献构建具有时间演化能力的医学知识图谱。 | Full text, local TXT line 54；核验TXT行号 54 | temporally evolving medical KGs | 高（一手正文；非独立复现） |
| 多步科研流程 | 系统逐日处理新文献并更新知识图谱。 | Full text, local TXT line 55；核验TXT行号 55 | incrementally constructs a KG daily via two specialized agents | 高（一手正文；非独立复现） |
| Agent能力 | Extractor抽取并评分，Constructor整合知识、强化重复关系和解决冲突。 | Full text, local TXT line 55；核验TXT行号 55 | The Extractor Agent identifies knowledge triples and assigns confidence scores | 高（一手正文；非独立复现） |
| 验证结果 | 作者通过自动和专家评估图谱三元组有效性。 | Full text, local TXT line 59；核验TXT行号 59 | triple-validity rates approaching 90 | 高（一手正文；非独立复现） |
| 限制与边界 | 下游验证为七个医学QA基准中的RAG效用，不代表临床诊疗决策效果。 | Full text, local TXT line 60；核验TXT行号 60 | across seven medical question-answering benchmarks | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出MedKGent，通过Extractor和Constructor两个专用Agent从1975—2023年的逾千万篇PubMed摘要增量构建带时间信息的医学知识图谱。系统提取带置信度的知识三元组，再整合重复信息并处理知识冲突；图谱含156,275个实体和2,971,384条三元组。自动与专家评估的有效率约90%，将图谱用作RAG来源也提升七个医学问答基准表现。图谱抽取错误和问答成绩不能证明临床决策安全或知识覆盖完整。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是组织和更新医学研究知识，科学对象及用途明确。
  - 原文位置：Full text, local TXT line 54；核验TXT行号 54；引文：temporally evolving medical KGs
- 多步行动过程：yes。两个专门Agent连续执行抽取、整合和时间更新。
  - 原文位置：Full text, local TXT line 55；核验TXT行号 55；引文：incrementally constructs a KG daily via two specialized agents
- 至少一种Agent能力：yes。系统具备三元组抽取、置信度评估、图谱构建及冲突处理能力。
  - 原文位置：Full text, local TXT line 55；核验TXT行号 55；引文：The Extractor Agent identifies knowledge triples and assigns confidence scores
- 明确科研流程角色：yes。该角色是医学文献知识工程与检索支持；验证不应扩大为临床决策能力。
  - 原文位置：Full text, local TXT line 59；核验TXT行号 59；引文：triple-validity rates approaching 90

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.03.08 医学信息学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.01医学知识与文献基础设施；研究对象是医学文献知识表示和问答支持，不是临床患者队列或新医学发现验证。

### 2.3 容易混淆的边界

归入06.01医学知识与文献基础设施；研究对象是医学文献知识表示和问答支持，不是临床患者队列或新医学发现验证。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

MedKGent以LLM Agent协同构建随时间演化的医学知识图谱，解析文献中的医学实体和关系、做实体链接与时序组织，再将图谱供RAG检索使用。

### 3.3 自主能力

系统具备三元组抽取、置信度评估、图谱构建及冲突处理能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是提出能够维护时间演化信息的Agent知识图谱构建框架，并评估其对文献知识检索和医学问答的支撑作用。

### 4.2 系统流程与组件

系统从医学文献提取实体/关系，采用语义相似度策略完成实体链接并构建带时间信息的知识图谱；作者评估自动及专家三元组有效性，并在七个医学多选问答数据集上测试图谱作为RAG来源的下游效用。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

论文报告图谱规模、自动/专家质量评估和七个QA基准上的RAG比较；这些结果验证知识组织及检索辅助价值，不等同医学知识图谱中的每条关系都经临床专家确认。

### 5.2 基线、指标与结果

图谱包含156,275个实体和2,971,384条三元组，自动与专家评估的有效率约90%；作为RAG信息源时，七个医学QA数据集的下游表现改善。

### 5.3 科学贡献与证据强度

贡献是提出能够维护时间演化信息的Agent知识图谱构建框架，并评估其对文献知识检索和医学问答的支撑作用。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较静态医学KG，MedKGent显式处理文献知识随时间变化；相较纯RAG文本检索，它先构造结构化实体关系，再供下游系统调用。

## 7. 局限性与风险

自动抽取和实体链接仍会引入错误，近90%有效率说明仍有不可靠三元组；七个QA基准衡量问答效用，不能证明临床决策安全或知识图谱覆盖完整。

## 8. 对综述写作的价值

可用于讨论Agent构建时序医学知识图谱的质量、RAG效用及知识基础设施与临床发现的边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

MedKGent从千万级PubMed摘要构建时序医学知识图谱，并以人工/自动质量评估及七个医学问答基准检验图谱效用。结果支持文献组织和RAG检索价值，仍需关注错误三元组及临床适用边界。

### 9.2 速记版 pipeline

系统从医学文献提取实体/关系，采用语义相似度策略完成实体链接并构建带时间信息的知识图谱；作者评估自动及专家三元组有效性，并在七个医学多选问答数据集上测试图谱作为RAG来源的下游效用。

### 9.3 标注字段汇总

```text
paper_id=ASD-1030
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.03.08
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 从文献构建知识图谱可由数据库核对 | “temporally evolving medical KGs” · L36 |
| 验证强度 | V2 计算/仿真/回顾性 | 自动与专家评估三元组有效性约90% | “triple-validity rates approaching 90” · L42 |
| 系统自主性 | L2 闭环执行者 | 逐日处理新文献并自主更新知识图谱 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
