# Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents

**论文信息**

- ID：ASD-0971
- 标题：Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents
- 作者：Youran Sun; Xingyu Ren; Chugang Yi; Kejia Zhang; Di Wu; Yingkang Cao; Allen Zhou; Jianping Ye; Suying Liu; Jiaxuan Guo; Jianda Du; Weicheng Ye; Kecheng Liu; Hefan Zhang; Haixin Wang; Jie Xiao; Eric Yang; Haizhao Yang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.21082
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0971.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Sun_2026_Sci_vot_Benchmarking_Principal_Investigator_Judgment_at_Pivotal_Moments_ASD0971.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 基准对象是科研项目关键时点上的人类纠正判断。 | 本地原文 TXT 第631行；核验TXT行号 631 | We introduce SciΠ\Pivot to make these judgments measurable. Its 248 cases from 26 projects pair original LLM plans with human-corrected alternatives reconstructed from completed project histories. The model chooses between them using the project record available before the human intervention, including its code, experimental logs, and progress notes. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | 案例由项目历史重建，并让模型基于干预前记录比较两种计划。 | 本地原文 TXT 第1056行；核验TXT行号 1056 | We build cases retrospectively from completed scientific research projects. Each project’s senior researcher supervised it from the initial idea through the final write-up. The full history links human interventions to subsequent investigation and provides evidence of their scientific value. We use this evidence to recover useful corrections, then evaluate them at the earlier decision point. Evaluators see only the earlier project record and two plans and judge which is more likely to advance the scientific question while the outcome is still unknown. Providing the same plans isolates this judgment from generating plausible alternatives. Figure 1 summarizes construction and evaluation. | 高（一手正文；非独立复现） |
| 实验任务与验证 | 研究对跨项目案例标注判断类型，并设置项目记录与仅选项条件。 | 本地原文 TXT 第1124行；核验TXT行号 1124 | The human corrections reveal recurring failures across scientific research projects (Table 3). We name each category after the judgment involved and describe what goes wrong. These judgments range from adapting to experimental results to deciding whether the evidence suffices for a conclusion. The focus category covers experiments that can run correctly yet leave the research question unanswered. For example, changing a cloth’s physical area does not answer how its parameters should change with mesh resolution on the same cloth. The coverage counts and radar scores group cases by these judgments. All 248 cases have a primary judgment label, and some carry secondary labels. Historical-error coding assigns 243 cases a primary error label and up to two secondary labels. Coding uses the original LLM plans and human corrections, without the evaluated responses (Appendix C). | 高（一手正文；非独立复现） |
| 主要结果 | 模型选择任务控制选项顺序、推理强度及可见材料以比较判断能力。 | 本地原文 TXT 第1500行；核验TXT行号 1500 | We evaluate GPT-6 Astra (OpenAI, 2026b), Claude Opus 5 (Anthropic, 2026), Grok 4.6 (xAI, 2026), and GPT-5.6 Sol and Terra (OpenAI, 2026a), abbreviated as Astra, Opus, Grok, Sol, and Terra. In the project condition, the model receives two plans and the project record. We ask it to start with the research idea, proposal, and progress notes, then consult other files as needed. The project record excludes Git history and later project state. Network access and research execution are prohibited. The model returns a choice and an explanation. The options-only condition presents the same plans without the project record. Client details appear in Appendix A. Appendix E gives the exact prompts, all twelve conditions, and available materials. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 评测覆盖理论和计算研究，且明确湿实验不在当前范围内。 | 本地原文 TXT 第1733行；核验TXT行号 1733 | SciΠ\Pivot covers theoretical and computational research using CPUs and GPUs, including simulation and analysis of existing data such as biological images. Wet-lab execution and workflows using specialized commercial scientific software such as COMSOL remain outside this evaluation. The cases test judgments central to PhD research across disciplines, including experiment selection, anomaly diagnosis, and revision of conclusions. Evaluation in other settings would test how these judgments transfer alongside different tools and experimental procedures. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

SciΠvot研究科研Agent运行中的关键PI判断，特别是何时应停止、修正或继续实验。作者从长期自主研究项目中整理人类判断节点，并建立用于模型识别与评估的基准。论文还分析模型能否从人类纠正历史中恢复决策。研究对象是科研决策与研究流程治理，而非某一具体自然科学领域；目前代码为11.07。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是识别真实科学项目中能否推进科学问题的关键判断；基准来源覆盖26个项目和六个科学领域。
  - 原文位置：本地全文TXT第426行；Abstract；来源项目与科研目标；核验TXT行号 426；引文：The benchmark draws on records from six months of research in which senior researchers ran LLM agents on 26 projects across six scientific fields and repeatedly intervened to correct the agents’ research judgments.
- 多步行动过程：yes。多步行动存在于基准来源轨迹：完整项目从研究构想到论文写作，且PI干预与后续调查相连。被测模型只处理一个关键决策，不要求完成全项目。
  - 原文位置：本地全文TXT第1056行；Section 3.1；完整研究历史；核验TXT行号 1056；引文：We build cases retrospectively from completed scientific research projects. Each project’s senior researcher supervised it from the initial idea through the final write-up. The full history links human interventions to subsequent investigation and provides evidence of their scientific value.
- 至少一种Agent能力：yes。作者实际运行科研AutoResearch Agent；全文说明源项目包含计算、仿真和研究记录。客户端只读项目记录并选择方案，科研执行另行评估，故本文证明的是轨迹中的判断任务而非端到端执行。
  - 原文位置：本地全文TXT第589行；Introduction；实际运行科研Agent；核验TXT行号 589；引文：Using frontier models with frontier agentic systems, we ran scientific AutoResearch agents on original, PhD-level projects at scale across disciplines.
- 明确科研流程角色：yes。该判断是指导实验工作流选择下一步的PI角色；项目干预后的调查为人类修正方案提供依据。
  - 原文位置：本地全文TXT第1406行；Section 3.4；科研判断与工作流关系；核验TXT行号 1406；引文：SciΠ\Pivot tests the scientific judgments needed to guide such workflows.

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

- Decision points during scientific research-agent runs; the exact task-domain set needs full-record inspection.

### 2.3 容易混淆的边界

基准来自真实多步AutoResearch项目轨迹，包含代码、实验日志及PI干预，并用后续调查重建参考方案；客户端每题只读上下文并作一次判断。可作为11.07科研决策/研究流程判断 benchmark 纳入，需明确其不评测客户端执行科研或闭环控制。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

多Agent/科研工作流Agent

### 3.2 科研流程角色

科学问题提出；实验设计；工具调用与代码执行；结果分析与验证

研究对象包含AutoResearch Agent项目和人类PI；SciΠvot整理决策历史、恢复关键科学判断，使用模型重演/识别人类纠正。

### 3.3 自主能力

作者实际运行科研AutoResearch Agent；全文说明源项目包含计算、仿真和研究记录。客户端只读项目记录并选择方案，科研执行另行评估，故本文证明的是轨迹中的判断任务而非端到端执行。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科研流程决策基准和人类判断分析是系统/方法贡献；未报告领域科学新发现。

### 4.2 系统流程与组件

输入为数月科研项目轨迹、关键决策及后续结果；标注判断节点及失败模式；构建回溯决策评估；测试模型能否从项目历史识别人类修正并与人类基线比较。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

理论、模拟、计算和已有科学数据分析项目的回顾性轨迹；模型判断与人类PI标注比较；湿实验及专有软件工作流未覆盖。

### 5.2 基线、指标与结果

作者归纳重复、偏焦等科研判断失败模式，并报告模型恢复人类决策的能力存在局限；不是对新自然科学发现的验证。

### 5.3 科学贡献与证据强度

科研流程决策基准和人类判断分析是系统/方法贡献；未报告领域科学新发现。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

补充以任务结果评分的AI Scientist benchmark，关注实验选择、问题聚焦和项目进展等过程判断。

## 7. 局限性与风险

回顾性判断标签受专家解释影响；覆盖以计算研究为主，不含湿实验和部分专业软件；对实际科研质量的因果效应尚未验证。

## 8. 对综述写作的价值

可用于讨论PI判断、科研Agent治理和项目级过程评估。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

以项目轨迹基准研究科研Agent关键决策中的PI判断。

### 9.2 速记版 pipeline

输入为数月科研项目轨迹、关键决策及后续结果；标注判断节点及失败模式；构建回溯决策评估；测试模型能否从项目历史识别人类修正并与人类基线比较。

### 9.3 标注字段汇总

```text
paper_id=ASD-0971
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


## 2026-10-29 三级分类复核

- 归档分类：`11.07.08` 科学方法论；二级：`11.07`。
- 原文位置：PDF pp.3,4,5,8。
- 判定：Concrete experiment/task evidence supports 11.07.08 (科学方法论). Its 248 cases from 26 projects pair original LLM plans with human-corrected alternatives reconstructed from completed project histories; Planning; Adapting; Anomaly awareness; Evidence sufficiency
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
