# From quantitative features to imaging signs: agentic AI-driven autonomous discovery in glioblastoma

**论文信息**

- ID：ASD-1013
- 标题：From quantitative features to imaging signs: agentic AI-driven autonomous discovery in glioblastoma
- 作者：Qian Li; Yan Liu; Biao Jiang; Fei Dong
- 年份：2026
- 来源 / venue：npj Digital Medicine
- DOI / arXiv / URL：https://doi.org/10.1038/s41746-026-03331-9
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1013.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Li_2026_From_quantitative_features_to_imaging_signs_agentic_AI_driven_ASD1013.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | 研究问题是将定量形态学特征转化为直观语义影像征象，以改善胶质母细胞瘤与脑转移瘤的鉴别。 | Full text, extracted character offset 571；核验TXT行号 15 | We developed an agentic AI pipeline to autonomously translate quantitative morphological features into semantic signs | 高（一手正文；非独立复现） |
| method or agent workflow | 流水线自主完成描述统计、语义征象转译和可视化，构成从特征到候选征象的连续分析过程。 | Full text, extracted character offset 690；核验TXT行号 16 | The pipeline autonomously performed end-to-end analysis—from descriptive statistical proﬁling and semantic sign translation to visualization | 高（一手正文；非独立复现） |
| evaluation design | 在106例开发队列中发现候选征象，并由两名放射科医师在50例GBM和50例转移瘤外部队列独立验证。 | Full text, extracted character offset 1034；核验TXT行号 20 | Two radiologists independently validated the cauliﬂower sign on an external cohort of 50 GBMs and 50 metastases | 高（一手正文；非独立复现） |
| reported result | 花椰菜征在外部队列区分两类肿瘤的平均AUC为0.75，展示数据驱动征象发现的验证结果。 | Full text, extracted character offset 1147；核验TXT行号 21 | achieving AUCs of 0.73 | 高（一手正文；非独立复现） |
| limitation / boundary | 研究为单中心、单一肿瘤类型且样本有限，且仅测一个AI平台和LLM，需跨数据及模型继续验证。 | Full text, extracted character offset 19399；核验TXT行号 356 | the pipeline was evaluated on a single-center, single-tumor-type dataset with a limited sample size | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文开发Agent流程，将106例幕上胶质母细胞瘤MRI中的定量形态特征转译为可解释的语义影像征象。系统生成八个候选征象，其中三种最稳定；两名放射科医师随后在独立的50例胶质母细胞瘤和50例脑转移瘤队列中评估花椰菜征。外部队列AUC分别为0.73和0.77，提示该征象有一定区分信息。研究仍受单中心开发集、有限样本及需人工验证提示词等因素限制。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文研究从定量影像特征发现可解释征象，并检验其用于GBM与转移瘤鉴别的价值。
  - 原文位置：Full text, extracted character offset 571；核验TXT行号 15；引文：We developed an agentic AI pipeline to autonomously translate quantitative morphological features into semantic signs
- 多步行动过程：yes。Agent流水线连续执行统计画像、语义翻译和可视化，而不是仅生成单次文本回答。
  - 原文位置：Full text, extracted character offset 690；核验TXT行号 16；引文：The pipeline autonomously performed end-to-end analysis—from descriptive statistical proﬁling and semantic sign translation to visualization
- 至少一种Agent能力：yes。系统自主处理形态特征并提出候选影像征象，具备面向影像数据的分析与转译能力。
  - 原文位置：Full text, extracted character offset 690；核验TXT行号 16；引文：The pipeline autonomously performed end-to-end analysis—from descriptive statistical proﬁling and semantic sign translation to visualization
- 明确科研流程角色：yes。该Agent流水线承担征象发现流程，放射科医师进一步对外部队列结果进行独立验证。
  - 原文位置：Full text, extracted character offset 1034；核验TXT行号 20；引文：Two radiologists independently validated the cauliﬂower sign on an external cohort of 50 GBMs and 50 metastases

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.02.05 肿瘤学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.01医学影像与神经肿瘤研究；其科学对象是GBM影像表型，报告的是候选征象及区分性能，不代表Agent独立确证生物学机制。

### 2.3 容易混淆的边界

归入06.01医学影像与神经肿瘤研究；其科学对象是GBM影像表型，报告的是候选征象及区分性能，不代表Agent独立确证生物学机制。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

Agent流程自动从胶质母细胞瘤MRI形态定量特征中归纳候选语义影像征象，完成统计剖析、征象转译和可视化，再由放射科医师审阅并外部验证。

### 3.3 自主能力

系统自主处理形态特征并提出候选影像征象，具备面向影像数据的分析与转译能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是尝试把高维定量形态特征转成临床可交流的语义影像征象，并用独立病例检验一个候选征象。

### 4.2 系统流程与组件

开发集含106例幕上GBM。系统提出八种候选征象，后续重点检验cauliflower征；两名放射科医师在外部队列中区分50例GBM与50例转移瘤，并评估征象判读表现。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

研究包含开发集上的Agent征象生成和独立外部病例验证；两位放射科医师分别标注，报告AUC及置信区间。外部验证体现诊断区分能力，仍属观察性影像研究。

### 5.2 基线、指标与结果

系统产生八个候选征象，其中cauliflower、eggplant和pancake征最稳定；cauliflower征在外部GBM/转移瘤队列的两位医师AUC为0.73和0.77，均值0.75。效果提示有判别信息但并非确定诊断。

### 5.3 科学贡献与证据强度

贡献是尝试把高维定量形态特征转成临床可交流的语义影像征象，并用独立病例检验一个候选征象。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较纯放射组学分类器，本文强调从数值特征生成可解释描述；与传统人工征象发现相比，Agent承担候选归纳，医师和外部队列承担核验。

## 7. 局限性与风险

单中心开发队列且样本量有限，扫描参数等临床因素可能混杂；外部队列只直接验证重点征象，候选生成与临床效用仍需多中心、前瞻性评估。

## 8. 对综述写作的价值

可用于讨论Agent将放射组学数值特征转译成可解释征象，并用外部病例进行临床影像验证的路径。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Agent从胶质母细胞瘤影像的定量特征中提出语义征象，并在独立病例中检验花椰菜征对胶质母细胞瘤和转移瘤的区分能力。观察到的AUC约为0.75，支持候选影像表型的进一步研究，尚不足以作为独立诊断结论。

### 9.2 速记版 pipeline

开发集含106例幕上GBM。系统提出八种候选征象，后续重点检验cauliflower征；两名放射科医师在外部队列中区分50例GBM与50例转移瘤，并评估征象判读表现。

### 9.3 标注字段汇总

```text
paper_id=ASD-1013
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.02.05
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 影像征象发现，答案可由外部放射科医师评估验证 | “两名放射科医师在50例GBM和50例转移瘤外部队列独立验证” · L23 |
| 验证强度 | V2 计算/仿真/回顾性 | 外部队列两位放射科医师标注并报告AUC及置信区间 | “外部队列AUC分别为0.73和0.77” · L29 |
| 系统自主性 | L2 闭环执行者 | 流水线自主完成描述统计、语义征象转译和可视化，构成从特征到候选征象的连续分析 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
