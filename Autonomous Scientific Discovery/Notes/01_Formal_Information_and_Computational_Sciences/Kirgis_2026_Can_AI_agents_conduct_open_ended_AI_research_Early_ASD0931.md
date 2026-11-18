# Can AI agents conduct open-ended AI research? Early evidence from two case studies

**论文信息**

- ID：ASD-0931
- 标题：Can AI agents conduct open-ended AI research? Early evidence from two case studies
- 作者：Peter Kirgis; Sayash Kapoor; Andrew Schwartz; Stephan Rabanser; David Africa; Konstantinos Voudouris; Viet Nguyen; Toby Pilditch; Magda Dubois; Harry Coppock; Cozmin Ududec; Nitya Nadgir; Matilda Orona; Tilman Bayer; Derrick Chan-Sew; Yue Ling; Abhishek Shetty; Helen Toner; Gillian Hadfield; Seth Lazar; Steve Newman; Shoshannah Tekofsky; Rishi Bommasani; Arvind Narayanan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.27191
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0931.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Kirgis_2026_Can_AI_agents_conduct_open_ended_AI_research_Early_ASD0931.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | 本文以 shadow evaluation 评估Agent能否完成开放式AI研究：给Agent未发表高质量论文的核心研究问题，隐藏原论文结果，并由原作者评判输出。研究对两篇未发表 NeurIPS 2026 投稿开展测试，提供前沿Agent六天和数千美元预算。作者发现Agent能够完成必要的工程工作，但未能产出达到顶级机器学习会议水平的原创研究。 | 本地全文：ASD-0931中与研究目标/科学问题直接相关的原文句子；核验TXT行号 406 | Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a third way to measure progress towards AI R&D automation. An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper’s original authors grade its output. We call these shadow evaluations. We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute. The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors. We identify five recurring failure modes: poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift. A robustness check with a second model and scaffold reproduced these failures. We release the expert reviews, survey responses, agent repositories, and logs. Our results provide early evidence that today’s agents can do the engineering of AI research, but struggle with critical parts of the research lifecycle. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 从两篇未发表 NeurIPS 2026 论文提取核心问题，隐藏结果后交由Agent独立研究；Agent获得六天及数千美元资源，原作者评估结果。 | 本地全文：ASD-0931中与多步行动/研究流程直接相关的原文句子；核验TXT行号 406 | An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper’s original authors grade its output. | 高（一手正文；非独立复现） |
| Agent实现与能力 | 论文比较前沿通用Agent执行开放式研究问题的表现，shadow evaluation由原论文作者评估Agent产出。 | 本地全文：ASD-0931中与Agent实现与能力直接相关的原文句子；核验TXT行号 406 | We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 评估采用两项真实研究问题的案例研究，由原创论文作者检查Agent产出，关注研究判断、原创性与最终质量。 | 本地全文：ASD-0931中与实验任务与验证设置直接相关的原文句子；核验TXT行号 681 | Our key finding was that while agents could solve the engineering problems necessary to do the research, they failed to produce original research at the caliber of a top ML conference (see Table 1 for details). | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者报告Agent能处理完成研究所需的工程问题，但未产出达到顶级ML会议水准的原创研究；论文进一步指出研究判断仍是薄弱环节。 核心贡献是提出由原作者评价隐藏结果研究问题的 shadow evaluation，并提供开放式AI研究能力的早期实证。 | 本地全文中包含该原句的位置；核验TXT行号 681 | Our key finding was that while agents could solve the engineering problems necessary to do the research, they failed to produce original research at the caliber of a top ML conference (see Table 1 for details). Our main takeaways: | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文以 shadow evaluation 评估Agent能否完成开放式AI研究：给Agent未发表高质量论文的核心研究问题，隐藏原论文结果，并由原作者评判输出。研究对两篇未发表 NeurIPS 2026 投稿开展测试，提供前沿Agent六天和数千美元预算。作者发现Agent能够完成必要的工程工作，但未能产出达到顶级机器学习会议水平的原创研究。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文以 shadow evaluation 评估Agent能否完成开放式AI研究：给Agent未发表高质量论文的核心研究问题，隐藏原论文结果，并由原作者评判输出。研究对两篇未发表 NeurIPS 2026 投稿开展测试，提供前沿Agent六天和数千美元预算。作者发现Agent能够完成必要的工程工作，但未能产出达到顶级机器学习会议水平的原创研究。
  - 原文位置：本地全文：ASD-0931中与研究目标/科学问题直接相关的原文句子；核验TXT行号 406；引文：Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a third way to measure progress towards AI R&D automation. An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper’s original authors grade its output. We call these shadow evaluations. We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute. The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors. We identify five recurring failure modes: poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift. A robustness check with a second model and scaffold reproduced these failures. We release the expert reviews, survey responses, agent repositories, and logs. Our results provide early evidence that today’s agents can do the engineering of AI research, but struggle with critical parts of the research lifecycle.
- 多步行动过程：yes。从两篇未发表 NeurIPS 2026 论文提取核心问题，隐藏结果后交由Agent独立研究；Agent获得六天及数千美元资源，原作者评估结果。
  - 原文位置：本地全文：ASD-0931中与多步行动/研究流程直接相关的原文句子；核验TXT行号 406；引文：An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper’s original authors grade its output.
- 至少一种Agent能力：yes。论文比较前沿通用Agent执行开放式研究问题的表现，shadow evaluation由原论文作者评估Agent产出。
  - 原文位置：本地全文：ASD-0931中与Agent实现与能力直接相关的原文句子；核验TXT行号 406；引文：We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute.
- 明确科研流程角色：yes。评估采用两项真实研究问题的案例研究，由原创论文作者检查Agent产出，关注研究判断、原创性与最终质量。
  - 原文位置：本地全文：ASD-0931中与实验任务与验证设置直接相关的原文句子；核验TXT行号 681；引文：Our key finding was that while agents could solve the engineering problems necessary to do the research, they failed to produce original research at the caliber of a top ML conference (see Table 1 for details).

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

论文比较前沿通用Agent执行开放式研究问题的表现，shadow evaluation由原论文作者评估Agent产出。

### 3.3 自主能力

论文比较前沿通用Agent执行开放式研究问题的表现，shadow evaluation由原论文作者评估Agent产出。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

核心贡献是提出由原作者评价隐藏结果研究问题的 shadow evaluation，并提供开放式AI研究能力的早期实证。

### 4.2 系统流程与组件

从两篇未发表 NeurIPS 2026 论文提取核心问题，隐藏结果后交由Agent独立研究；Agent获得六天及数千美元资源，原作者评估结果。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评估采用两项真实研究问题的案例研究，由原创论文作者检查Agent产出，关注研究判断、原创性与最终质量。

### 5.2 基线、指标与结果

作者报告Agent能处理完成研究所需的工程问题，但未产出达到顶级ML会议水准的原创研究；论文进一步指出研究判断仍是薄弱环节。

### 5.3 科学贡献与证据强度

核心贡献是提出由原作者评价隐藏结果研究问题的 shadow evaluation，并提供开放式AI研究能力的早期实证。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Can AI agents conduct open-ended AI research? Early evidence from two case studies”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

只有两个案例，且来自特定未发表NeurIPS工作；研究预算、Agent配置和原作者评分会限制结论外推。

## 8. 对综述写作的价值

可用于综述“Can AI agents conduct open-ended AI research? Early evidence from two case studies”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

两项shadow evaluation显示，当前Agent能处理工程工作，但尚未展现顶会水准的原创研究。

### 9.2 速记版 pipeline

从两篇未发表 NeurIPS 2026 论文提取核心问题，隐藏结果后交由Agent独立研究；Agent获得六天及数千美元资源，原作者评估结果。

### 9.3 标注字段汇总

```text
paper_id=ASD-0931
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O6 开放科学 | Agent接收未发表论文的开放式研究问题并独立完成研究，答案事先未知 | “central, open-ended research question of a high-quality unpublished paper” · L21 |
| 验证强度 | V1 基准/内部评测 | 由原论文作者评估Agent产出质量，无独立实验验证或正式发表 | “原创论文作者检查Agent产出” · L24 |
| 系统自主性 | L2 闭环执行者 | Agent获得六天和数千美元资源在人给定问题内自主研究，但未达到自主提出问题 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
