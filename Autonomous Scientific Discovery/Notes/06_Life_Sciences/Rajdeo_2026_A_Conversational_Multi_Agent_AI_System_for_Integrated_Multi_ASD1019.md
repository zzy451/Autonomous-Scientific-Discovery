# A Conversational Multi-Agent AI System for Integrated Multi-Omics Analysis and Biomedical Discovery

**论文信息**

- ID：ASD-1019
- 标题：A Conversational Multi-Agent AI System for Integrated Multi-Omics Analysis and Biomedical Discovery
- 作者：Pankaj Rajdeo; Shunya Asanuma; Michal Kouril; Peixin Lu; Jichao Chen; Aman Chadha; V. B. Surya Prasath; Bruce J. Aronow; Nathan Salomonis
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.08.08.743577
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1019.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Rajdeo_2026_A_Conversational_Multi_Agent_AI_System_for_Integrated_Multi_ASD1019.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | LungChat针对跨单细胞、空间组学、文献和临床试验的综合分析，支持生物医学发现及药物再利用。 | Full text, extracted character offset 5464；核验TXT行号 72 | In this work, we introduce LungChat, a conversational multi-agent AI system for integrated multi-omics analysis | 高（一手正文；非独立复现） |
| method or agent workflow | Supervisor将自然语言问题分解给专门子Agent，任务覆盖组学分析、文献和临床试验综合以及药物再利用。 | Full text, extracted character offset 5931；核验TXT行号 76 | a supervisor coordinates specialized sub-agents | 高（一手正文；非独立复现） |
| evaluation design | 基准包含100个测试案例，覆盖单步分析、安全与越界拒答、多工具协作和复杂推理，并另做架构消融。 | Full text, extracted character offset 11939；核验TXT行号 157 | test cases across five evaluation tracks | 高（一手正文；非独立复现） |
| reported result | IPF案例中系统优先提出saracatinib，并通过DART作细胞类型层级分析；该药曾进入STOP-IPF临床试验。 | Full text, extracted character offset 1971；核验TXT行号 26 | LungChat independently prioritized saracatinib for IPF through drug-connectivity screening, followed by DART-based cell-type analysis | 高（一手正文；非独立复现） |
| limitation / boundary | 评估主要是单轮查询，作者尚未在长会话中实测其持续上下文能力。 | Full text, extracted character offset 123674；核验TXT行号 2807 | The current evaluation focuses on single-turn queries | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出LungChat对话式多Agent系统，整合肺部单细胞和空间组学分析、专业工具与医学文献检索。作者以100个案例组成的基准评估多类任务，并通过消融检查层级协调和工具选择组件；另以特发性肺纤维化为案例生成整合性机制及治疗假设。基准和案例显示系统可支持迭代多组学分析，但IPF候选假设未由独立实验验证，不能视为治疗结论。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。系统目标是整合多组学与生物医学知识来回答科研问题并支持疾病机制分析和治疗候选发现。
  - 原文位置：Full text, extracted character offset 5464；核验TXT行号 72；引文：In this work, we introduce LungChat, a conversational multi-agent AI system for integrated multi-omics analysis
- 多步行动过程：yes。Supervisor把问题拆解为并行子任务，多个专门Agent调用工具完成跨域分析。
  - 原文位置：Full text, extracted character offset 5931；核验TXT行号 76；引文：a supervisor coordinates specialized sub-agents
- 至少一种Agent能力：yes。系统可调用组学分析和药物再利用工具，并根据方向信息筛选可能逆转疾病表达程序的扰动。
  - 原文位置：Full text, extracted character offset 5931；核验TXT行号 76；引文：a supervisor coordinates specialized sub-agents
- 明确科研流程角色：yes。LungChat直接承担组学分析、证据整合和药物候选优先排序等科研工作。
  - 原文位置：Full text, extracted character offset 5464；核验TXT行号 72；引文：In this work, we introduce LungChat, a conversational multi-agent AI system for integrated multi-omics analysis

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.04 单细胞生物学；07.02.10 呼吸病学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.03组学与疾病机制研究，重点是肺部疾病多组学对象；其分析基准和IPF假设不能作为药效或机制实验证据。

### 2.3 容易混淆的边界

归入06.03组学与疾病机制研究，重点是肺部疾病多组学对象；其分析基准和IPF假设不能作为药效或机制实验证据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

LungChat是对话式多Agent多组学系统，协调单细胞/空间组学分析、专业工具调用和生物医学知识检索，并以状态管理支持逐步分析及用户追问。

### 3.3 自主能力

系统可调用组学分析和药物再利用工具，并根据方向信息筛选可能逆转疾病表达程序的扰动。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是将交互式对话、多组学计算和医学知识检索集成于肺病研究助手，使用户可追踪地迭代提出分析问题。

### 4.2 系统流程与组件

作者在肺部疾病相关多组学任务上评测100个测试案例，覆盖五类评价；进行层级Agent及选择组件消融，并以特发性肺纤维化（IPF）作为整合组学和文献证据的案例。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

验证包括任务基准、消融比较及IPF案例分析。基准检查回答/分析质量，病例研究展示候选疾病机制或治疗假设；未报告独立实验验证这些假设。

### 5.2 基线、指标与结果

系统能够协调不同组学与知识工具生成整合分析；消融用于分辨层级协调和选择机制贡献。IPF案例产出的是供后续检验的机制/治疗线索，不是经实验确认的治疗结论。

### 5.3 科学贡献与证据强度

贡献是将交互式对话、多组学计算和医学知识检索集成于肺病研究助手，使用户可追踪地迭代提出分析问题。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较通用医学问答Agent，LungChat聚焦单细胞及空间组学工具链；相较固定分析管线，它支持对话驱动的跨模态迭代。

## 7. 局限性与风险

100个测试案例和特定肺病领域不能证明跨器官泛化；复杂长上下文可能影响推理，案例生成的机制结论需独立生物实验和专家复核。

## 8. 对综述写作的价值

可用于比较对话式多组学Agent如何组织工具和知识，并将案例假设与机制实验证据区分。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

LungChat协调单细胞/空间组学工具和医学知识检索，支持研究者以对话方式迭代分析肺部疾病。100例基准和IPF案例展示其分析能力，所提出机制与治疗线索仍待实验验证。

### 9.2 速记版 pipeline

作者在肺部疾病相关多组学任务上评测100个测试案例，覆盖五类评价；进行层级Agent及选择组件消融，并以特发性肺纤维化（IPF）作为整合组学和文献证据的案例。

### 9.3 标注字段汇总

```text
paper_id=ASD-1019
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.04;07.02.10
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 多组学分析结论可由数据和文献核对 | “integrated multi-omics analysis” · L42 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算分析和文献已知结论比对 | “LungChat independently prioritized saracatinib for IPF” · L24 |
| 系统自主性 | L2 闭环执行者 | 系统自主协调多Agent执行分析 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
