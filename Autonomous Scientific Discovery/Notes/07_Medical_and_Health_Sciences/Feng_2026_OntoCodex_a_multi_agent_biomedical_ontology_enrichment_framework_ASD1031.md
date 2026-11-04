# OntoCodex: a multi-agent biomedical ontology enrichment framework

**论文信息**

- ID：ASD-1031
- 标题：OntoCodex: a multi-agent biomedical ontology enrichment framework
- 作者：Jingna Feng; Yue Yu; Aaron Dong; Xinyue Hu; Shuteng Niu; Pengze Li; Yifang Dang; Ahmed Abdelhameed; Jiang Bian; Xiaoqian Jiang; Cui Tao
- 年份：2026
- 来源 / venue：npj Health Systems
- DOI / arXiv / URL：https://doi.org/10.1038/s44401-026-00117-9
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1031.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| Agent目标 | 覆盖卒中、COPD、房颤、骨质疏松和帕金森病的概念增强。 | Abstract；核验TXT行号 1 | including stroke, chronic obstructive pulmonary disease, atrial fibrillation, osteoporosis, and Parkinson’s disease | 高（一手正文；非独立复现） |
| 系统结构 | 由五个协作Agent完成规划、本体读取、检索、标准术语映射和脚本生成。 | Methods / Fig. 1；核验TXT行号 1 | The OntoCodex framework consists of five agents | 高（一手正文；非独立复现） |
| 行动规划 | Algorithm 1规定读取本体、制定计划、检索证据、消歧、生成OWL更新脚本并执行。 | Methods / Algorithm 1；核验TXT行号 1 | Decision Agent formulates enrichment plan based on: | 高（一手正文；非独立复现） |
| 评估数据 | 以MedlinePlus为语料，由两位作者标注概念金标准。 | Evaluation；核验TXT行号 1 | the gold standard was constructed through manual review of MedlinePlus content by two authors | 高（一手正文；非独立复现） |
| 专家一致性 | 第一轮标注一致率为96.74%，讨论后全部达成一致。 | Evaluation；核验TXT行号 1 | the overall agreement reached 96.74%. | 高（一手正文；非独立复现） |
| 结果与限制 | 抽取及用药映射多项优于ChatGPT-4o；实验室检查映射表现较弱。 | Abstract；核验TXT行号 1 | while showing lower performance in laboratory test mapping. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 本体增强评测覆盖卒中、COPD、房颤、骨质疏松和帕金森病等医学对象；07.03.08医学信息学适配。 | TXT line 1；核验TXT行号 1 | five chronic diseases, including stroke, chronic obstructive pulmonary disease, atrial fibrillation, osteoporosis, and Parkinson’s disease. Compared with baseline ChatGPT-4o, OntoCodex improved concept extraction across most domains, achieving higher precision | 高（一手正文；非独立复现） |

## 0. 摘要翻译

OntoCodex提出五Agent医学本体增强工作流，从医学语料抽取概念、映射标准术语，并生成OWL更新脚本。系统在五类慢性病的MCC-CDO概念增强任务中与ChatGPT-4o比较，报告多数抽取域表现改善，并验证了生成本体结构。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是把五类慢性疾病概念整合到MCC-CDO医学本体。
  - 原文位置：Abstract；核验TXT行号 1；引文：We evaluated OntoCodex using a ChatGPT-4o–powered implementation to enrich concepts across five chronic diseases
- 多步行动过程：yes。流程包括解析、规划、检索、术语映射、人工审核、代码生成和执行。
  - 原文位置：Methods / Algorithm 1；核验TXT行号 1；引文：The overall inter-agent workflow is illustrated in Fig. 1 , and the detailed operational logic of the framework is summarized in Algorithm 1 .
- 至少一种Agent能力：yes。决策Agent解析需求并规划、分派子任务。
  - 原文位置：Methods / Fig. 1；核验TXT行号 1；引文：a decision agent that analyzes the requirements and decides the tasks and the plan of actions for each agent
- 明确科研流程角色：yes。系统承担医学概念抽取、标准化及本体工程任务。
  - 原文位置：Abstract；核验TXT行号 1；引文：successfully enriched the MCC-CDO with new concepts and annotations without errors.

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

本体增强评测覆盖卒中、COPD、房颤、骨质疏松和帕金森病等医学对象；07.03.08医学信息学适配。

### 2.3 容易混淆的边界

本体增强评测覆盖卒中、COPD、房颤、骨质疏松和帕金森病等医学对象；07.03.08医学信息学适配。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Multi-Agent System；Tool-using Agent；Human-in-the-loop Agent

### 3.2 科研流程角色

knowledge_extraction_and_organization；tool_use_and_code_execution；evidence_assessment_and_validation

ChatGPT-4o驱动的五Agent协作系统，包含决策、本体读取、知识库、术语和脚本生成Agent；歧义由人工审核。

### 3.3 自主能力

决策Agent解析需求并规划、分派子任务。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是临床知识本体组织；系统贡献是多Agent、术语归一与OWL代码生成。

### 4.2 系统流程与组件

输入用户请求、OWL本体、医学语料和标准术语；解析schema并规划；检索候选概念与证据；术语规范化；人审歧义；生成和执行Python/OWL脚本；用Protégé检查。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

MedlinePlus语料；两作者人工标注；评估概念抽取、标准编码映射及OWL结构有效性，并与ChatGPT-4o基线比较。

### 5.2 基线、指标与结果

作者报告多域概念抽取precision、recall和F1总体提升，实验室检验抽取达到完美；用药映射较强、实验室映射较弱；脚本执行无错误。

### 5.3 科学贡献与证据强度

科学贡献是临床知识本体组织；系统贡献是多Agent、术语归一与OWL代码生成。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较单次文本抽取或摘要工具，OntoCodex支持从候选概念到本体结构更新的完整流程。

## 7. 局限性与风险

作者指出实验室检查映射较弱且模糊项需要人工判断。读者风险：验证集中于单一本体和MedlinePlus，不能直接推导临床效益。

## 8. 对综述写作的价值

可支撑医学知识组织、临床语义互操作与Agent辅助本体工程。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

五Agent协作扩展临床医学本体。

### 9.2 速记版 pipeline

输入用户请求、OWL本体、医学语料和标准术语；解析schema并规划；检索候选概念与证据；术语规范化；人审歧义；生成和执行Python/OWL脚本；用Protégé检查。

### 9.3 标注字段汇总

```text
paper_id=ASD-1031
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


## 2026-10-29 PR剩余差异复核

- 来源深度：`verified_official_pdf_fulltext`。本轮涉及1条差异，其中1条已判定，0条待核。摘要或图注支持的判定不代表全文已逐页核验。

- 原1664行号 `1492`：`retain_current`。The 12-page original PDF reports medical-ontology experiments across five chronic diseases, planning/retrieval/normalization/OWL-script stages, decision-agent orchestration and feedback, and a medical knowledge-organization role. These support medical informatics (07.03.08).
  - 位置：PDF p.3 Algorithm 1 / decision agent; p.1 five chronic diseases; p.5 evaluation / gold standard；来源：https://doi.org/10.1038/s44401-026-00117-9

逐条引文、来源文件和限制见 `Coverage_Check/pr1_82_recheck_2026-10-29/final_review.json`。保留现有分类不等于全部分类边界已消除。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 从医学语料抽取概念并映射到既有本体 | “including stroke, chronic obstructive pulmonary disease” · L21 |
| 验证强度 | V2 计算/仿真/回顾性 | 人工标注金标准比较和OWL结构验证 | “manual review of MedlinePlus content” · L24 |
| 系统自主性 | L1 任务助手 | 协调五Agent完成抽取映射和脚本生成 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
