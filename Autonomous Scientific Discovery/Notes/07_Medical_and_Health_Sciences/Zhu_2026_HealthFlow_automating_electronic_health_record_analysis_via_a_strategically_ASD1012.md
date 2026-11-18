# HealthFlow: automating electronic health record analysis via a strategically self-evolving multi-agent framework

**论文信息**

- ID：ASD-1012
- 标题：HealthFlow: automating electronic health record analysis via a strategically self-evolving multi-agent framework
- 作者：Yinghao Zhu; Zixiang Wang; Yifan Qi; Lei Gu; Dehao Sui; Haoran Hu; Xichen Zhang; Ziyi He; Yasha Wang; Junjun He; Liantao Ma; Lequan Yu
- 年份：2026
- 来源 / venue：npj Digital Medicine
- DOI / arXiv / URL：https://doi.org/10.1038/s41746-026-03097-0
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1012.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | 研究目标是自动完成电子病历数据分析，并在数据集与方法约束下产出有效、可复现的临床研究分析。 | Full text, extracted character offset 516；核验TXT行号 1 | Here we present HealthFlow, a multi-agent framework that converts prior EHR analyses into structured, governed experience for planning under dataset-specific and methodological constraints | 高（一手正文；非独立复现） |
| method or agent workflow | HealthFlow将既往分析整理为方法防护、可复用多步流程、数据集事实和实施指导，并按任务条件写回、检索和更新。 | Full text, extracted character offset 5006；核验TXT行号 1 | These memories are written back, retrieved, and updated over time under governed conditions tied to task family, dataset signature, schema cues, and risk tags | 高（一手正文；非独立复现） |
| evaluation design | 作者在五个基准上覆盖开放式EHR流程编排、可执行分析、医学知识推理和工具增强决策。 | Full text, extracted character offset 9392；核验TXT行号 1 | We evaluated HealthFlow on five benchmarks spanning open-ended EHR workflow orchestration, executable EHR analysis, medical knowledge reasoning, and tool-augmented decision-making | 高（一手正文；非独立复现） |
| reported result | 在EHRFlowBench及四个既有基准中，系统相较强基线更常生成有效临床产物并完成复杂分析流程。 | Full text, extracted character offset 833；核验TXT行号 1 | Across EHRFlowBench and four established benchmarks (MedAgentBoard, MedAgentsBench, HLE, and CureBench), HealthFlow consistently outperforms strong baselines in generating valid clinical artifacts and completing complex EHR analysis pipelines | 高（一手正文；非独立复现） |
| limitation / boundary | 作者指出长期记忆管理以及真实部署和评估仍未解决，限制了对实际临床环境泛化的结论。 | Full text, extracted character offset 26769；核验TXT行号 1 | limitations remain in long-term memory management and real-world deployment and evaluation | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出HealthFlow，以多Agent和受治理的历史分析经验自动执行电子病历数据科学任务，并构建EHRFlowBench。基准任务由51,280篇同行评议论文整理而来，涵盖开放式工作流编排和可执行分析产物；作者还在四个既有医疗Agent基准上比较方法。HealthFlow在所测任务中较强基线更常生成有效分析产物并完成复杂流程。证据来自基准执行，作者指出长期记忆管理及真实部署评估仍待解决。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。系统面向真实电子病历研究分析，目标包括在异质数据和方法约束下形成有效分析产物。
  - 原文位置：Full text, extracted character offset 516；核验TXT行号 1；引文：Here we present HealthFlow, a multi-agent framework that converts prior EHR analyses into structured, governed experience for planning under dataset-specific and methodological constraints
- 多步行动过程：yes。记忆被写回、检索和更新，并服务于后续任务规划，形成跨任务的连续分析步骤。
  - 原文位置：Full text, extracted character offset 5006；核验TXT行号 1；引文：These memories are written back, retrieved, and updated over time under governed conditions tied to task family, dataset signature, schema cues, and risk tags
- 至少一种Agent能力：yes。系统编排代码生成、生物医学资源检索与工具使用，直接支持EHR分析执行。
  - 原文位置：Full text, extracted character offset 516；核验TXT行号 1；引文：Here we present HealthFlow, a multi-agent framework that converts prior EHR analyses into structured, governed experience for planning under dataset-specific and methodological constraints
- 明确科研流程角色：yes。HealthFlow承担队列、特征、建模、可视化和报告等EHR分析流程的自动化。
  - 原文位置：Full text, extracted character offset 516；核验TXT行号 1；引文：Here we present HealthFlow, a multi-agent framework that converts prior EHR analyses into structured, governed experience for planning under dataset-specific and methodological constraints

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

归入06.01健康与医学数据研究；研究对象是EHR分析流程及其有效性，基准优势不能解释为患者结局改善或临床获益。

### 2.3 容易混淆的边界

归入06.01健康与医学数据研究；研究对象是EHR分析流程及其有效性，基准优势不能解释为患者结局改善或临床获益。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

HealthFlow把既有EHR分析转成受治理的结构化经验，供多Agent规划时检索并遵守数据集和方法约束；它面向完整健康数据分析产物，而非医学问答。

### 3.3 自主能力

系统编排代码生成、生物医学资源检索与工具使用，直接支持EHR分析执行。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把历史EHR分析转化为约束感知的可复用经验，并建立覆盖端到端分析的EHRFlowBench。

### 4.2 系统流程与组件

系统从用户分析任务形成计划，调用代码生成、执行、检索和数据资源工具，复用相似历史分析模式；完成后检查分析产物有效性并按错误修正。EHRFlowBench由51,280篇论文衍生任务，并与四个既有基准共同评测。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

五类基准涵盖开放式EHR工作流编排及可执行分析任务，比较强基线的临床分析产物有效性和流程完成情况；验证是基准/计算执行，没有前瞻性临床部署验证。

### 5.2 基线、指标与结果

论文报告HealthFlow在EHRFlowBench及MedAgentBoard、MedAgentsBench、HLE、CureBench上总体优于强基线，支持受治理经验复用改善流程鲁棒性的结论。性能结论限于所用数据、硬件和任务定义。

### 5.3 科学贡献与证据强度

贡献是把历史EHR分析转化为约束感知的可复用经验，并建立覆盖端到端分析的EHRFlowBench。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与能回答临床问题或执行孤立工具调用的医疗Agent相比，HealthFlow处理从规划到有效分析产物的多步骤数据科学流程，并使用先例经验约束执行。

## 7. 局限性与风险

基准中的任务来源与人工整理方式会影响代表性；真实机构的权限、数据质量和部署流程尚未被这些离线评测覆盖。作者指出长期记忆管理和真实部署/评估仍待解决。

## 8. 对综述写作的价值

可用于比较医疗数据科学Agent对EHR全流程分析产物的支持及历史经验复用的作用。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

HealthFlow检索结构化的既往EHR分析经验来规划、执行并检查新的临床数据分析任务。它在EHRFlowBench及四个已有基准上优于比较方法，但当前证据主要是离线基准结果，尚未证明真实临床部署效益。

### 9.2 速记版 pipeline

系统从用户分析任务形成计划，调用代码生成、执行、检索和数据资源工具，复用相似历史分析模式；完成后检查分析产物有效性并按错误修正。EHRFlowBench由51,280篇论文衍生任务，并与四个既有基准共同评测。

### 9.3 标注字段汇总

```text
paper_id=ASD-1012
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
| 问题开放度 | O2 既定基准 | 在预定义EHR分析基准上评测 | “five benchmarks spanning open-ended EHR workflow orchestration” · L23 |
| 验证强度 | V1 基准/内部评测 | 基准任务完成度和产物有效性评分 | “HealthFlow consistently outperforms strong baselines in generating valid clinical artifacts” · L24 |
| 系统自主性 | L2 闭环执行者 | 系统自主执行多步EHR分析流程 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
