# Experimental Experience Modeling for Autonomous Research

**论文信息**

- ID：ASD-0947
- 标题：Experimental Experience Modeling for Autonomous Research
- 作者：Wei, Wenda; Zhang, Yingchen; Zhang, Ruqing; Guo, Jiafeng; Shi, Daiting; Cheng, Xueqi
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.39392
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0947.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Wenda_2026_Experimental_Experience_Modeling_for_Autonomous_Research_ASD0947.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | Experimental Experience Modeling（EEM）从先前实验轨迹抽取与决策相关的记录，将观察蒸馏为可复用经验并组织进经验库。面临新实验决策时，系统检索适用经验；证据不足时开展针对性pilot，再据观察决定是否投入完整实验。作者使用含25个机器学习研究主题的ARC-Bench评估。 | 本地全文：ASD-0947中与研究目标/科学问题直接相关的原文句子；核验TXT行号 263 | Autonomous research agents can generate hypotheses and conduct experiments, but experimentation remains a major source of computational cost. A fundamental challenge is deciding which experiments are worth running, particularly when prior evidence is insufficient to resolve uncertainty. Yet current research agents lack a systematic way to leverage experimental experience when making such decisions. We introduce Experimental Experience Modeling (EEM), a framework for making informed experimental decisions by acquiring, reusing, and accumulating experimental experience. EEM extracts decision-relevant records from earlier experimental trajectories, distills them into reusable experience, and organizes them in an experience library. For a new experimental decision, EEM retrieves relevant historical experience and assesses whether it provides sufficient support for deciding whether a candidate direction warrants further investment. When historical experience is insufficient, EEM conducts a targeted, low-cost pilot experiment to acquire the missing decision-relevant experience on demand. It then combines this newly acquired experience with retrieved historical experience to determine whether the direction warrants full-scale evaluation, which requires substantial resources. The resulting experimental outcomes are further distilled into reusable experience, allowing the library to continually grow through iterative accumulation. Experiments on autonomous research benchmarks show that EEM improves research performance while reducing model interaction overhead, demonstrating the value of reusing accumulated experience and acquiring additional experience only when needed. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统从实验轨迹抽取记录，蒸馏适用条件及经验关系；新决策时检索相关经验，必要时运行小规模pilot，根据结果决定完整实验投入。 | 本地全文：ASD-0947中与多步行动/研究流程直接相关的原文句子；核验TXT行号 269 | When historical experience is insufficient, EEM conducts a targeted, low-cost pilot experiment to acquire the missing decision-relevant experience on demand. | 高（一手正文；非独立复现） |
| Agent实现与能力 | EEM将既往实验中的条件、结果和投资建议存入经验库，并供后续自主研究Agent检索和决策。 | 本地全文：ASD-0947中与Agent实现与能力直接相关的原文句子；核验TXT行号 267 | EEM extracts decision-relevant records from earlier experimental trajectories, distills them into reusable experience, and organizes them in an experience library. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 作者使用ARC-Bench的25个机器学习研究主题，任务给出研究目标和实验要求，并评估代码开发、执行及研究结果等能力。 | 本地全文：ASD-0947中与实验任务与验证设置直接相关的原文句子；核验TXT行号 361 | We evaluate EEM on the 25 research topics in ARC-Bench (Liu et al., 2026). Compared with AutoResearchClaw (Liu et al., 2026), the strongest evaluated baseline, EEM improves the overall score by 13.1% and result analysis by 31.7%, while reducing average total token consumption by 11.4%. Ablation experiments support the effectiveness of EEM’s design, while experiments across backbone models and repeated runs examine its applicability and performance consistency. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 正文比较引入EEM前后的实验决策和研究表现；结果依赖经验库覆盖度与ARC-Bench任务设置。 方法贡献是把零散实验观察转换为带适用条件的可复用决策知识，用于后续实验投资。 | 本地全文中包含该原句的位置；核验TXT行号 362 | Compared with AutoResearchClaw (Liu et al., 2026), the strongest evaluated baseline, EEM improves the overall score by 13.1% and result analysis by 31.7%, while reducing average total token consumption by 11.4%. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Experimental Experience Modeling（EEM）从先前实验轨迹抽取与决策相关的记录，将观察蒸馏为可复用经验并组织进经验库。面临新实验决策时，系统检索适用经验；证据不足时开展针对性pilot，再据观察决定是否投入完整实验。作者使用含25个机器学习研究主题的ARC-Bench评估。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。Experimental Experience Modeling（EEM）从先前实验轨迹抽取与决策相关的记录，将观察蒸馏为可复用经验并组织进经验库。面临新实验决策时，系统检索适用经验；证据不足时开展针对性pilot，再据观察决定是否投入完整实验。作者使用含25个机器学习研究主题的ARC-Bench评估。
  - 原文位置：本地全文：ASD-0947中与研究目标/科学问题直接相关的原文句子；核验TXT行号 263；引文：Autonomous research agents can generate hypotheses and conduct experiments, but experimentation remains a major source of computational cost. A fundamental challenge is deciding which experiments are worth running, particularly when prior evidence is insufficient to resolve uncertainty. Yet current research agents lack a systematic way to leverage experimental experience when making such decisions. We introduce Experimental Experience Modeling (EEM), a framework for making informed experimental decisions by acquiring, reusing, and accumulating experimental experience. EEM extracts decision-relevant records from earlier experimental trajectories, distills them into reusable experience, and organizes them in an experience library. For a new experimental decision, EEM retrieves relevant historical experience and assesses whether it provides sufficient support for deciding whether a candidate direction warrants further investment. When historical experience is insufficient, EEM conducts a targeted, low-cost pilot experiment to acquire the missing decision-relevant experience on demand. It then combines this newly acquired experience with retrieved historical experience to determine whether the direction warrants full-scale evaluation, which requires substantial resources. The resulting experimental outcomes are further distilled into reusable experience, allowing the library to continually grow through iterative accumulation. Experiments on autonomous research benchmarks show that EEM improves research performance while reducing model interaction overhead, demonstrating the value of reusing accumulated experience and acquiring additional experience only when needed.
- 多步行动过程：yes。系统从实验轨迹抽取记录，蒸馏适用条件及经验关系；新决策时检索相关经验，必要时运行小规模pilot，根据结果决定完整实验投入。
  - 原文位置：本地全文：ASD-0947中与多步行动/研究流程直接相关的原文句子；核验TXT行号 269；引文：When historical experience is insufficient, EEM conducts a targeted, low-cost pilot experiment to acquire the missing decision-relevant experience on demand.
- 至少一种Agent能力：yes。EEM将既往实验中的条件、结果和投资建议存入经验库，并供后续自主研究Agent检索和决策。
  - 原文位置：本地全文：ASD-0947中与Agent实现与能力直接相关的原文句子；核验TXT行号 267；引文：EEM extracts decision-relevant records from earlier experimental trajectories, distills them into reusable experience, and organizes them in an experience library.
- 明确科研流程角色：yes。作者使用ARC-Bench的25个机器学习研究主题，任务给出研究目标和实验要求，并评估代码开发、执行及研究结果等能力。
  - 原文位置：本地全文：ASD-0947中与实验任务与验证设置直接相关的原文句子；核验TXT行号 361；引文：We evaluate EEM on the 25 research topics in ARC-Bench (Liu et al., 2026). Compared with AutoResearchClaw (Liu et al., 2026), the strongest evaluated baseline, EEM improves the overall score by 13.1% and result analysis by 31.7%, while reducing average total token consumption by 11.4%. Ablation experiments support the effectiveness of EEM’s design, while experiments across backbone models and repeated runs examine its applicability and performance consistency.

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

EEM将既往实验中的条件、结果和投资建议存入经验库，并供后续自主研究Agent检索和决策。

### 3.3 自主能力

EEM将既往实验中的条件、结果和投资建议存入经验库，并供后续自主研究Agent检索和决策。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

方法贡献是把零散实验观察转换为带适用条件的可复用决策知识，用于后续实验投资。

### 4.2 系统流程与组件

系统从实验轨迹抽取记录，蒸馏适用条件及经验关系；新决策时检索相关经验，必要时运行小规模pilot，根据结果决定完整实验投入。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者使用ARC-Bench的25个机器学习研究主题，任务给出研究目标和实验要求，并评估代码开发、执行及研究结果等能力。

### 5.2 基线、指标与结果

正文比较引入EEM前后的实验决策和研究表现；结果依赖经验库覆盖度与ARC-Bench任务设置。

### 5.3 科学贡献与证据强度

方法贡献是把零散实验观察转换为带适用条件的可复用决策知识，用于后续实验投资。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Experimental Experience Modeling for Autonomous Research”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

过去经验可能不适用于新任务；蒸馏偏差、检索匹配和pilot范围会影响决策可靠性。

## 8. 对综述写作的价值

可用于综述“Experimental Experience Modeling for Autonomous Research”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

EEM把历史实验经验转成可检索的决策知识，帮助Agent选择后续实验投入。

### 9.2 速记版 pipeline

系统从实验轨迹抽取记录，蒸馏适用条件及经验关系；新决策时检索相关经验，必要时运行小规模pilot，根据结果决定完整实验投入。

### 9.3 标注字段汇总

```text
paper_id=ASD-0947
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
| 问题开放度 | O2 既定基准 | 在ARC-Bench的25个机器学习研究主题上评估 | “25 research topics in ARC-Bench” · L42 |
| 验证强度 | V1 基准/内部评测 | 比较研究表现和token消耗，属基准评测 | “improves the overall score by 13.1%” · L42 |
| 系统自主性 | L2 闭环执行者 | 系统从既往实验抽取经验并用于后续实验决策闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
