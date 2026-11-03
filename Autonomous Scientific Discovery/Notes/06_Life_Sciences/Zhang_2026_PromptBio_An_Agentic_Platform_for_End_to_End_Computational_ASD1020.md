# PromptBio: An Agentic Platform for End-to-End Computational Biomedical Research

**论文信息**

- ID：ASD-1020
- 标题：PromptBio: An Agentic Platform for End-to-End Computational Biomedical Research
- 作者：Minzhe Zhang; Wenhao Gu; Bowei Han; Wenbin Guo; Jiayu Chen; Xiaoyuan Zhou; Yang Leng; Youjia Ma; Kai Li; Junbin Zheng; Hebbar Shishir; Weiying Wang; Aaron Huang; KC Shashidhar; Xiao Yang
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.02.748774
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1020.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Zhang_2026_PromptBio_An_Agentic_Platform_for_End_to_End_Computational_ASD1020.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | PromptBio面向计算生物医学研究，将科研问题转化为可执行且可复查的分析流程。 | Full text, extracted character offset 436；核验TXT行号 9 | translating a scientific question into a reliable workflow | 高（一手正文；非独立复现） |
| method or agent workflow | PromptGenie形成可检查的多步计划，协调专门子Agent和技能，并依据中间证据及结果调整后续步骤。 | Full text, extracted character offset 4732；核验TXT行号 65 | constructs an inspectable multi-step plan, coordinates specialized subagents and reusable skills, and executes analyses in managed computational environments | 高（一手正文；非独立复现） |
| evaluation design | 评估包括端到端生物信息学与深度研究基准、组学及机器学习技能验证，以及假设驱动的调控基因组案例。 | Full text, extracted character offset 1241；核验TXT行号 17 | We evaluate the platform through benchmarks of end-to-end bioinformatics analysis and biomedical deep research, validation of representative omics and machine-learning skills, and a hypothesis-driven regulatory-genomics case study | 高（一手正文；非独立复现） |
| reported result | PromptGenie在比较Agent中取得更高分析准确性及更强证据检索和综合表现；案例整合人类基因组与表观基因组信息研究皮层发育。 | Full text, extracted character offset 1473；核验TXT行号 20 | PromptGenie achieved higher analytical accuracy and stronger evidence retrieval and synthesis than the comparison agents | 高（一手正文；非独立复现） |
| limitation / boundary | 现有结果不能证明平台在所有生物医学领域均有一致表现，也不能证明其可在完全自主研究中运行。 | Full text, extracted character offset 7149；核验TXT行号 91 | they do not establish uniform performance across all biomedical domains or fully autonomous research settings | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文介绍PromptBio计算生物医学平台及其PromptGenie多Agent执行器，可将自然语言目标转成可检查计划，调用分析工具并根据中间结果调整流程。作者通过端到端生物信息和深度学习任务评估平台，并展示人类基因组与表观基因组特征分析皮层发育的案例。结果与既有方法一致，支持平台运行能力；有限任务及单一案例不能证明跨生物医学领域的普遍性能或完全自主发现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。平台目标是把计算生物医学研究问题转化为可执行分析，并通过案例开展调控基因组研究。
  - 原文位置：Full text, extracted character offset 436；核验TXT行号 9；引文：translating a scientific question into a reliable workflow
- 多步行动过程：yes。Agent创建多步计划、协调子Agent和技能，并依据中间结果调整后续步骤。
  - 原文位置：Full text, extracted character offset 4732；核验TXT行号 65；引文：constructs an inspectable multi-step plan, coordinates specialized subagents and reusable skills, and executes analyses in managed computational environments
- 至少一种Agent能力：yes。系统执行数据检索、组学管线、统计和机器学习分析及生成代码等计算任务。
  - 原文位置：Full text, extracted character offset 4732；核验TXT行号 65；引文：constructs an inspectable multi-step plan, coordinates specialized subagents and reusable skills, and executes analyses in managed computational environments
- 明确科研流程角色：yes。PromptBio承担证据检索、计算分析与结果解释等生物医学科研工作环节，并保留人工监督。
  - 原文位置：Full text, extracted character offset 436；核验TXT行号 9；引文：translating a scientific question into a reliable workflow

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

归入相应生物信息学研究对象模块；调控基因组学案例使其超出纯通用工具，但平台基准不证明所有任务具备领域Agent能力。

### 2.3 容易混淆的边界

归入相应生物信息学研究对象模块；调控基因组学案例使其超出纯通用工具，但平台基准不证明所有任务具备领域Agent能力。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

PromptBio通过PromptGenie把自然语言研究目标转为可检查计划，执行托管代码/分析工具，并根据中间证据调整后续步骤；人类保留监督和过程记录。

### 3.3 自主能力

系统执行数据检索、组学管线、统计和机器学习分析及生成代码等计算任务。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是提供带有人类监督和可追踪执行记录的端到端计算生物医学Agent平台，并允许将固定方法、定制分析和外部流程组合。

### 4.2 系统流程与组件

平台以端到端生物信息分析基准和生物医学深度学习任务评测，并展示调控基因组学案例：组合人类基因组与表观基因组特征分析皮层发育。方法执行后检查结果是否与已知方法一致。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者使用多类基准任务和单个基因组学案例，报告流程完成与分析结果；还与固定流程或其他Agent方法比较。结果为计算验证，没有实验扰动验证案例结论。

### 5.2 基线、指标与结果

平台能构建并运行可复现分析流程，案例得到与既有方法一致的结果；论文明确指出这些评测不能确立所有生物医学领域的统一表现，也没有证明完全自主研究能力。

### 5.3 科学贡献与证据强度

贡献是提供带有人类监督和可追踪执行记录的端到端计算生物医学Agent平台，并允许将固定方法、定制分析和外部流程组合。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较只处理生物信息问答或预定义单一管线的工具，PromptBio试图从研究目标规划到执行并适应中间结果；评估覆盖传统分析和机器学习任务。

## 7. 局限性与风险

基准任务与案例覆盖有限，结果一致性不等同于新生物学发现；托管环境、数据库访问和用户监督条件会影响可复现性与泛化。

## 8. 对综述写作的价值

可用于评估研究目标到可检查生物信息流程的平台能力及案例结果的外部验证缺口。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

PromptBio从研究目标规划并执行计算生物医学分析，保留人工监督和可追踪过程，并以调控基因组学案例展示应用。基准结果与已知方法一致，但尚未验证跨领域泛化或实验性新发现。

### 9.2 速记版 pipeline

平台以端到端生物信息分析基准和生物医学深度学习任务评测，并展示调控基因组学案例：组合人类基因组与表观基因组特征分析皮层发育。方法执行后检查结果是否与已知方法一致。

### 9.3 标注字段汇总

```text
paper_id=ASD-1020
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
| 问题开放度 | O2 既定基准 | 在既有生物信息基准上评测 | “benchmarks of end-to-end bioinformatics analysis” · L23 |
| 验证强度 | V1 基准/内部评测 | 基准任务准确性评分 | “PromptGenie achieved higher analytical accuracy” · L24 |
| 系统自主性 | L2 闭环执行者 | 系统自主构建并执行多步计划 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
