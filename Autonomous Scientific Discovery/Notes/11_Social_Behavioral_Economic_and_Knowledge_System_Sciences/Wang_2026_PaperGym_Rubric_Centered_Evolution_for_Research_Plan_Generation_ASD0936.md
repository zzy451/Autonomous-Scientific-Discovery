# PaperGym: Rubric-Centered Evolution for Research-Plan Generation

**论文信息**

- ID：ASD-0936
- 标题：PaperGym: Rubric-Centered Evolution for Research-Plan Generation
- 作者：Yuhan Wang; Zhengxi Lu; Yuchen Yan; Kaitao Song; Wenqi Zhang; Weiming Lu; Jun Xiao; Yueting Zhuang; Yongliang Shen
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.31119
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0936.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Wang_2026_PaperGym_Rubric_Centered_Evolution_for_Research_Plan_Generation_ASD0936.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | PaperGym将研究论文转化为研究计划生成的训练环境：研究问题由论文目标和背景合成，方法与实验部分转化为评分标准，并以标准反馈驱动计划改进。实验使用PaperGym-20k计算机科学子集，约一万条来自2015至2025年arXiv论文的实例。 | 本地全文：ASD-0936中与研究目标/科学问题直接相关的原文句子；核验TXT行号 385 | Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic. Rubrics extracted from scientific papers can supply the critic. Existing pipelines, however, draw the question and the criteria from the same content, so the reward can be earned by paraphrase. The rubric is further compressed into a single scalar per rollout. We introduce PaperGym, a unified framework that turns each research paper into a complete training environment. PaperGym exploits the structure of a paper: the question is synthesized from the research goal and background, while the criteria are derived from the method and experiments. The criteria span methodological innovation and experimental design, and criterion leakage falls to 3.7%, versus 11.90% to 34.10% in existing datasets. Training uses the rubric twice: first as privileged context for OPSD’s self-teacher, then as the reward for GRPO. Across Qwen3-1.7B/4B/8B, this schedule outperforms supervised fine-tuning, either stage alone, and the reverse ordering, improving five-benchmark averages by +5.6, +5.0, and +4.8 points. With the recipe held fixed, models trained on PaperGym-20k win 58.1% of three-way comparisons, against 28.2% for RubricHub Science. The trained Qwen3-8B reaches 73.48 on ResearchQA, above the far larger Kimi K2.6. We release the pipeline, the 20,000-instance corpus PaperGym-20k, and the benchmarks PaperGym-Innov and PaperGym-Design. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统从论文生成研究问题和计划评价criteria，以方法创新和实验设计等维度形成rubric，再用criterion级反馈迭代训练或改进计划生成Agent。 | 本地全文：ASD-0936中与多步行动/研究流程直接相关的原文句子；核验TXT行号 385 | PaperGym exploits the structure of a paper: the question is synthesized from the research goal and background, while the criteria are derived from the method and experiments. | 高（一手正文；非独立复现） |
| Agent实现与能力 | PaperGym是面向研究计划生成的rubric中心训练框架，将论文问题、方法和实验信息整理成环境与可执行评价标准。 | 本地全文：ASD-0936中与Agent实现与能力直接相关的原文句子；核验TXT行号 385 | We introduce PaperGym, a unified framework that turns each research paper into a complete training environment. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 作者在PaperGym-20k计算机科学子集及文中列出的域内基准上评估；训练集约含一万条2015至2025年arXiv论文实例。 | 本地全文：ASD-0936中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1041 | (1) Training data. We train on the computer-science subset of PaperGym-20k, which comprises ∼\sim10,000 instances derived from arXiv papers published between January 2015 and December 2025. (2) In-domain benchmarks. We construct held-out benchmarks from papers released after January 2026 across three domains (cs, econ, physics), sampling 400 papers per domain with two test instances each: PaperGym-Innov derives the question from Research Goal and Background, uses Research Method as the reference answer, and scores along the innovation dimension; PaperGym-Design additionally incorporates Research Method into the question, uses Experimental Design as the reference answer, and scores along the design dimension (Section D.3). (3) Out-of-domain benchmarks. Generalization is assessed on ResearchQA (Yifei et al., 2025) (750 instances, 10 per field), ResearchPlanGen-ML (Goel et al., 2025) (full test set), and RubricHub Science (Li et al., 2026c) (800 instances). All responses are scored by DeepSeek-V4-Flash via an LLM-as-a-judge protocol that rates rubric coverage per criterion. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 论文比较不同研究计划生成方法的rubric得分和泛化表现；结论限于研究计划质量评测，不等同于实验成功或科学发现。 系统贡献是从论文结构自动生成计划训练环境和标准；科学对象是研究计划与机器学习/计算机科学论文语料。 | 本地全文中包含该原句的位置；核验TXT行号 385 | With the recipe held fixed, models trained on PaperGym-20k win 58.1% of three-way comparisons, against 28.2% for RubricHub Science. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

PaperGym将研究论文转化为研究计划生成的训练环境：研究问题由论文目标和背景合成，方法与实验部分转化为评分标准，并以标准反馈驱动计划改进。实验使用PaperGym-20k计算机科学子集，约一万条来自2015至2025年arXiv论文的实例。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。PaperGym将研究论文转化为研究计划生成的训练环境：研究问题由论文目标和背景合成，方法与实验部分转化为评分标准，并以标准反馈驱动计划改进。实验使用PaperGym-20k计算机科学子集，约一万条来自2015至2025年arXiv论文的实例。
  - 原文位置：本地全文：ASD-0936中与研究目标/科学问题直接相关的原文句子；核验TXT行号 385；引文：Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic. Rubrics extracted from scientific papers can supply the critic. Existing pipelines, however, draw the question and the criteria from the same content, so the reward can be earned by paraphrase. The rubric is further compressed into a single scalar per rollout. We introduce PaperGym, a unified framework that turns each research paper into a complete training environment. PaperGym exploits the structure of a paper: the question is synthesized from the research goal and background, while the criteria are derived from the method and experiments. The criteria span methodological innovation and experimental design, and criterion leakage falls to 3.7%, versus 11.90% to 34.10% in existing datasets. Training uses the rubric twice: first as privileged context for OPSD’s self-teacher, then as the reward for GRPO. Across Qwen3-1.7B/4B/8B, this schedule outperforms supervised fine-tuning, either stage alone, and the reverse ordering, improving five-benchmark averages by +5.6, +5.0, and +4.8 points. With the recipe held fixed, models trained on PaperGym-20k win 58.1% of three-way comparisons, against 28.2% for RubricHub Science. The trained Qwen3-8B reaches 73.48 on ResearchQA, above the far larger Kimi K2.6. We release the pipeline, the 20,000-instance corpus PaperGym-20k, and the benchmarks PaperGym-Innov and PaperGym-Design.
- 多步行动过程：yes。系统从论文生成研究问题和计划评价criteria，以方法创新和实验设计等维度形成rubric，再用criterion级反馈迭代训练或改进计划生成Agent。
  - 原文位置：本地全文：ASD-0936中与多步行动/研究流程直接相关的原文句子；核验TXT行号 385；引文：PaperGym exploits the structure of a paper: the question is synthesized from the research goal and background, while the criteria are derived from the method and experiments.
- 至少一种Agent能力：yes。PaperGym是面向研究计划生成的rubric中心训练框架，将论文问题、方法和实验信息整理成环境与可执行评价标准。
  - 原文位置：本地全文：ASD-0936中与Agent实现与能力直接相关的原文句子；核验TXT行号 385；引文：We introduce PaperGym, a unified framework that turns each research paper into a complete training environment.
- 明确科研流程角色：yes。作者在PaperGym-20k计算机科学子集及文中列出的域内基准上评估；训练集约含一万条2015至2025年arXiv论文实例。
  - 原文位置：本地全文：ASD-0936中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1041；引文：(1) Training data. We train on the computer-science subset of PaperGym-20k, which comprises ∼\sim10,000 instances derived from arXiv papers published between January 2015 and December 2025. (2) In-domain benchmarks. We construct held-out benchmarks from papers released after January 2026 across three domains (cs, econ, physics), sampling 400 papers per domain with two test instances each: PaperGym-Innov derives the question from Research Goal and Background, uses Research Method as the reference answer, and scores along the innovation dimension; PaperGym-Design additionally incorporates Research Method into the question, uses Experimental Design as the reference answer, and scores along the design dimension (Section D.3). (3) Out-of-domain benchmarks. Generalization is assessed on ResearchQA (Yifei et al., 2025) (750 instances, 10 per field), ResearchPlanGen-ML (Goel et al., 2025) (full test set), and RubricHub Science (Li et al., 2026c) (800 instances). All responses are scored by DeepSeek-V4-Flash via an LLM-as-a-judge protocol that rates rubric coverage per criterion.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不覆盖其他模块）
- 模块内分类路径：11.07 科学系统与知识生产研究
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（11；11.07）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（11；11.07）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

PaperGym是面向研究计划生成的rubric中心训练框架，将论文问题、方法和实验信息整理成环境与可执行评价标准。

### 3.3 自主能力

PaperGym是面向研究计划生成的rubric中心训练框架，将论文问题、方法和实验信息整理成环境与可执行评价标准。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是从论文结构自动生成计划训练环境和标准；科学对象是研究计划与机器学习/计算机科学论文语料。

### 4.2 系统流程与组件

系统从论文生成研究问题和计划评价criteria，以方法创新和实验设计等维度形成rubric，再用criterion级反馈迭代训练或改进计划生成Agent。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者在PaperGym-20k计算机科学子集及文中列出的域内基准上评估；训练集约含一万条2015至2025年arXiv论文实例。

### 5.2 基线、指标与结果

论文比较不同研究计划生成方法的rubric得分和泛化表现；结论限于研究计划质量评测，不等同于实验成功或科学发现。

### 5.3 科学贡献与证据强度

系统贡献是从论文结构自动生成计划训练环境和标准；科学对象是研究计划与机器学习/计算机科学论文语料。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“PaperGym: Rubric-Centered Evolution for Research-Plan Generation”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

rubric质量取决于论文信息抽取及标准生成；计划评分不能证明方案可执行或会产生有效科学结果。

## 8. 对综述写作的价值

可用于综述“PaperGym: Rubric-Centered Evolution for Research-Plan Generation”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

PaperGym用论文派生的rubric训练并评价研究计划生成Agent。

### 9.2 速记版 pipeline

系统从论文生成研究问题和计划评价criteria，以方法创新和实验设计等维度形成rubric，再用criterion级反馈迭代训练或改进计划生成Agent。

### 9.3 标注字段汇总

```text
paper_id=ASD-0936
inclusion_status=to_read
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 研究计划生成在既有基准上评测 | “We construct held-out benchmarks from papers released after January 2026” · L42 |
| 验证强度 | V1 基准/内部评测 | LLM-as-judge按rubric标准打分 | “All responses are scored by DeepSeek-V4-Flash via an LLM-as-a-judge protocol” · L42 |
| 系统自主性 | L1 任务助手 | 系统执行研究计划生成任务但不决定研究什么 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
