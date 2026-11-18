# TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design

**论文信息**

- ID：ASD-1021
- 标题：TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design
- 作者：Sarveswara Rao Vangala; Vishnu Vardhan Kasturi; Navneet Bung; Arijit Roy
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.12.751167
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1021.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Vangala_2026_TRACEDD_A_Tool_grounded_Reasoning_and_Agentic_Coordination_for_ASD1021.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 论文针对靶点验证、结构分析和分子设计等药物发现决策，科学目标明确。 | Full text, local TXT line 8；核验TXT行号 8 | Drug discovery depends on coordinated decisions across target validation | 高（一手正文；非独立复现） |
| 多步科研流程 | 展示从靶点验证到合成规划的端到端步骤，符合多阶段科研行动。 | Full text, local TXT line 17；核验TXT行号 17 | It demonstrates an end-to-end workflow, from target validation to synthesis planning | 高（一手正文；非独立复现） |
| Agent能力 | LLM负责规划、选工具并整合异质输出，工具结果支持后续决策。 | Full text, local TXT line 111；核验TXT行号 111 | LLMs are used to plan tasks, select tools, integrate heterogeneous outputs | 高（一手正文；非独立复现） |
| 验证结果 | 以JAK2案例展示结构检索、缺失结构预测、口袋识别及分子生成。 | Full text, local TXT line 22；核验TXT行号 22 | Using JAK2 as a representative case | 高（一手正文；非独立复现） |
| 限制与边界 | 设计假设依赖已知抑制剂，报告主要为计算设计和排序证据，不能等同实验疗效。 | Full text, local TXT line 25；核验TXT行号 25 | Known JAK2 inhibitors are used to define design hypotheses | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出TRACEDD，以工具优先的多Agent协作支持可解释药物设计，并用JAK2抑制剂作为端到端案例。系统整合靶点文献证据、蛋白结构检索及AlphaFold结构、结合口袋分析、分子生成、对接、预测pIC50和ADMET排序，最后给出合成规划线索。案例展示了可追溯的计算决策链，但未报告大规模靶点基准或湿实验活性测定；候选排序不能证明真实抑制效果。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。科学目标是协调多个药物发现决策，属于明确的分子设计研究。
  - 原文位置：Full text, local TXT line 8；核验TXT行号 8；引文：Drug discovery depends on coordinated decisions across target validation
- 多步行动过程：yes。从靶点验证推进至合成规划，文本描述了连续的研究步骤。
  - 原文位置：Full text, local TXT line 17；核验TXT行号 17；引文：It demonstrates an end-to-end workflow, from target validation to synthesis planning
- 至少一种Agent能力：yes。LLM规划并选择计算工具、整合结果；不是单轮文本生成。
  - 原文位置：Full text, local TXT line 111；核验TXT行号 111；引文：LLMs are used to plan tasks, select tools, integrate heterogeneous outputs
- 明确科研流程角色：yes。Agent承担药物设计研究协作角色，JAK2案例提供实际任务验证。
  - 原文位置：Full text, local TXT line 22；核验TXT行号 22；引文：Using JAK2 as a representative case

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.06 蛋白质科学；07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.02药物发现；保留为计算设计Agent案例，需明确模型排序和案例可行性不构成药效验证或可开发药物证明。

### 2.3 容易混淆的边界

归入06.02药物发现；保留为计算设计Agent案例，需明确模型排序和案例可行性不构成药效验证或可开发药物证明。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

TRACEDD以tool-first的Reason–Act–Observe循环协调药物设计Agent，使用已验证工具而非让LLM直接替代科学计算；围绕JAK2抑制剂案例连接靶点证据、结构分析、候选生成、开发性评估和合成规划。

### 3.3 自主能力

LLM规划并选择计算工具、整合结果；不是单轮文本生成。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把可追溯的科学工具和证据整合进多Agent药物设计链路，以JAK2说明从靶点验证到分子及合成建议的衔接方式。

### 4.2 系统流程与组件

针对JAK2，系统检索并评估靶点依据，获取/核验蛋白结构（包括结构检索及AlphaFold来源），分析结合口袋；随后生成候选分子，进行口袋相互作用/对接、pIC50及ADMET排序，并形成合成可行性建议。各步对缺失或变化的数据显式调整流程。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

证据来自JAK2端到端案例、结构和分子工具输出、文献证据追溯及候选排序；作者以计算模型和显式推理轨迹检查流程。未见大规模靶点基准或湿实验活性测定，因此属于案例级计算验证。

### 5.2 基线、指标与结果

系统产生并排序JAK2候选，结合结构口袋、预测活性与ADMET信息解释设计理由，并给出合成规划线索。结果说明工具编排可形成可审计设计链，不能据预测分数认定候选具有真实抑制活性。

### 5.3 科学贡献与证据强度

贡献是把可追溯的科学工具和证据整合进多Agent药物设计链路，以JAK2说明从靶点验证到分子及合成建议的衔接方式。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相比只做分子生成/对接的SBDD流程，TRACEDD强调靶点证据、结构来源核验、工具调用轨迹和合成规划；其重点是可解释编排，而非提出新的分子生成模型。

## 7. 局限性与风险

主要为单靶点JAK2演示，缺少大规模基准、实验结合/活性验证、药代毒理和合成实测；pIC50、ADMET及对接分数均为模型估计，且检索证据可能有偏差。

## 8. 对综述写作的价值

可用于讨论药物设计Agent中靶点与结构证据、分子计算排序及湿实验确认之间的证据链。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

TRACEDD围绕JAK2案例串联靶点证据、结构与口袋分析、分子设计、对接、pIC50/ADMET排序和合成建议。它展示工具编排和推理轨迹，缺少实验验证及广泛基准，候选药效仍属预测。

### 9.2 速记版 pipeline

针对JAK2，系统检索并评估靶点依据，获取/核验蛋白结构（包括结构检索及AlphaFold来源），分析结合口袋；随后生成候选分子，进行口袋相互作用/对接、pIC50及ADMET排序，并形成合成可行性建议。各步对缺失或变化的数据显式调整流程。

### 9.3 标注字段汇总

```text
paper_id=ASD-1021
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.06;07.04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 候选分子性质可由计算模型预测 | “Using JAK2 as a representative case” · L24 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算对接和ADMET预测 | “Known JAK2 inhibitors are used to define design hypotheses” · L25 |
| 系统自主性 | L2 闭环执行者 | 系统自主协调从靶点到合成的流程 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
