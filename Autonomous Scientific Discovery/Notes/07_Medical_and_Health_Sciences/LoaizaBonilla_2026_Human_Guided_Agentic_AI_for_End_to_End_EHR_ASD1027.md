# Human-Guided Agentic AI for End-to-End EHR Research: Sequential Antibody-Drug Conjugate Pathways in Breast Cancer

**论文信息**

- ID：ASD-1027
- 标题：Human-Guided Agentic AI for End-to-End EHR Research: Sequential Antibody-Drug Conjugate Pathways in Breast Cancer
- 作者：Arturo Loaiza-Bonilla; Christos Colovos; Daniel Kim; James M. Grichnik; Kritika Singh; Paolo Tarantino
- 年份：2026
- 来源 / venue：medRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.10.13.26365479
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1027.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/LoaizaBonilla_2026_Human_Guided_Agentic_AI_for_End_to_End_EHR_ASD1027.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 临床研究对象为乳腺癌患者ADC药物序贯订单的真实世界EHR分析。 | Full text, local TXT line 37；核验TXT行号 37 | sequential sacituzumab govitecan (SG) and trastuzumab deruxtecan (T-DXd) orders in breast cancer | 高（一手正文；非独立复现） |
| 多步科研流程 | Agent支持从队列构建到分析、质控、文献检索及报告的连续研究任务。 | Full text, local TXT line 40；核验TXT行号 40 | cohort construction, executable statistical analysis, data-quality checks, literature retrieval, and reporting | 高（一手正文；非独立复现） |
| Agent能力 | 多Agent系统由人类研究者监督和引导。 | Full text, local TXT line 36；核验TXT行号 36 | multi-agent artificial intelligence (AI) system governed by Human-Guided Orchestration | 高（一手正文；非独立复现） |
| 验证结果 | 实际队列含106名患者，并报告药物订单间隔的描述统计。 | Full text, local TXT line 46；核验TXT行号 46 | The workflow identified 106 patients | 高（一手正文；非独立复现） |
| 限制与边界 | 作者明确声明订单不证明实际给药或疾病进展，分析未作调整。 | Full text, local TXT line 44；核验TXT行号 44 | Analyses were descriptive and unadjusted; orders did not confirm administration or progression | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文展示研究者引导的多Agent EHR研究流程，结合临床问题规范、队列构建、可执行统计分析、数据质量检查、文献检索和报告生成。案例关注乳腺癌患者两种抗体药物偶联物T-DXd与SG的治疗顺序，系统从EHR识别106例患者，其中73例先开立T-DXd、33例先开立SG。该回顾性路径分析说明协作流程可执行，但处方记录不等于实际给药，也不能推断药物疗效差异。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。科学目标是研究乳腺癌ADC治疗路径，基于具体EHR队列。
  - 原文位置：Full text, local TXT line 37；核验TXT行号 37；引文：sequential sacituzumab govitecan (SG) and trastuzumab deruxtecan (T-DXd) orders in breast cancer
- 多步行动过程：yes。工作流串联队列构建、数据质控、统计分析、检索及报告。
  - 原文位置：Full text, local TXT line 40；核验TXT行号 40；引文：cohort construction, executable statistical analysis, data-quality checks, literature retrieval, and reporting
- 至少一种Agent能力：yes。Muse Spark及多Agent团队在HGO下执行任务并接受研究者裁决。
  - 原文位置：Full text, local TXT line 36；核验TXT行号 36；引文：multi-agent artificial intelligence (AI) system governed by Human-Guided Orchestration
- 明确科研流程角色：yes。该Agent承担临床研究分析支持角色；论文同时限定了EHR订单证据边界。
  - 原文位置：Full text, local TXT line 46；核验TXT行号 46；引文：The workflow identified 106 patients

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.02.05 肿瘤学；07.03.08 医学信息学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.01临床数据研究；结果是治疗路径描述和Agent工作流示范，不是两种ADC疗效或因果优劣证据。

### 2.3 容易混淆的边界

归入06.01临床数据研究；结果是治疗路径描述和Agent工作流示范，不是两种ADC疗效或因果优劣证据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

研究采用人类引导的Symbiotic Agent Teaming执行EHR研究：研究者给出问题和规范，Agent团队编译成可执行分析、运行数据质量检查、检索文献并生成报告，人工保留决策控制。

### 3.3 自主能力

Muse Spark及多Agent团队在HGO下执行任务并接受研究者裁决。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是展示人类引导多Agent如何从临床问题推进到EHR队列、分析、证据检索和报告，强调研究者与Agent的协作。

### 4.2 系统流程与组件

工作流分析乳腺癌患者先后使用trastuzumab deruxtecan（T-DXd）和sacituzumab govitecan（SG）的治疗路径；从EHR构建队列、比较给药顺序并使用文献检索和临床分析工具解释结果。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者按既有EHR数据质量原则评估工作流，并报告识别的106例患者：73例T-DXd先开立、33例SG先开立。验证是回顾性EHR队列分析和流程执行展示。

### 5.2 基线、指标与结果

研究识别两种ADC的真实世界开立顺序分布，为描述后续治疗路径提供案例；订单状态不等同于实际给药，分析结果不能直接解释为药效或优劣比较。

### 5.3 科学贡献与证据强度

贡献是展示人类引导多Agent如何从临床问题推进到EHR队列、分析、证据检索和报告，强调研究者与Agent的协作。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较完全自动运行的EHRAgent，本文突出研究者给定分析规范并保留人为控制；与单纯EHR问答不同，它执行队列构建和可运行统计分析。

## 7. 局限性与风险

样本量和单一乳腺癌ADC问题限制推广；EHR开立记录可能包括未实际接受的治疗，残余混杂、缺失记录及编码差异会影响结论。

## 8. 对综述写作的价值

可用于讨论人类引导EHR研究Agent的队列分析流程及电子病历记录对临床解释的限制。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

研究者引导的Agent团队从EHR构建乳腺癌队列并分析T-DXd和SG的开立顺序，共识别106例患者。结果描述真实世界治疗路径，不代表实际接受治疗或两药疗效比较。

### 9.2 速记版 pipeline

工作流分析乳腺癌患者先后使用trastuzumab deruxtecan（T-DXd）和sacituzumab govitecan（SG）的治疗路径；从EHR构建队列、比较给药顺序并使用文献检索和临床分析工具解释结果。

### 9.3 标注字段汇总

```text
paper_id=ASD-1027
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.02.05;07.03.08
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | EHR队列可由记录核对 | “sequential sacituzumab govitecan (SG) and trastuzumab deruxtecan (T-DXd) orders” · L36 |
| 验证强度 | V2 计算/仿真/回顾性 | 回顾性EHR数据分析 | “The workflow identified 106 patients” · L24 |
| 系统自主性 | L2 闭环执行者 | Agent执行端到端EHR研究流程 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
