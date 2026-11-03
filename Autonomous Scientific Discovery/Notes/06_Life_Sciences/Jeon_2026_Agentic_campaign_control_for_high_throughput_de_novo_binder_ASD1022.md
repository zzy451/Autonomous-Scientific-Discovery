# Agentic campaign control for high-throughput de novo binder design

**论文信息**

- ID：ASD-1022
- 标题：Agentic campaign control for high-throughput de novo binder design
- 作者：Minkyu Jeon; Jinyeop Song; Jina Kim; Ellen D. Zhong
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.22.753604
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1022.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Jeon_2026_Agentic_campaign_control_for_high_throughput_de_novo_binder_ASD1022.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 目标是从头设计蛋白结合体，并优化有限计算预算下的方法选择。 | Full text, local TXT line 30；核验TXT行号 30 | de novo protein binder design | 高（一手正文；非独立复现） |
| 多步科研流程 | 在设计campaign中根据累积生成和评估结果持续选择后续路线。 | Full text, local TXT line 10；核验TXT行号 10 | Over the course of a design campaign, T-REX leverages large language model | 高（一手正文；非独立复现） |
| Agent能力 | Agent能够在候选救援、参数探索和有效路线利用间作出适应性决策。 | Full text, local TXT line 11；核验TXT行号 11 | decide whether to rescue promising candidates, explore alternative settings, or exploit productive routes | 高（一手正文；非独立复现） |
| 验证结果 | 七个靶点的评估报告目标依赖的算力分配和结构不同hit产出。 | Full text, local TXT line 13；核验TXT行号 13 | Across seven targets, we find that T-REX adaptively allocates its compute | 高（一手正文；非独立复现） |
| 限制与边界 | 结果是计算指标下的结构不同候选吞吐量，不应解释为湿实验结合验证。 | Full text, local TXT line 14；核验TXT行号 14 | structurally distinct hits compared to all baselines | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出T-REX，使用Agent在de novo蛋白binder设计campaign中协调多个生成模型和结构评价器。面对七个靶点，系统依据累积结果在挽救候选、探索新设置和利用有效路线之间分配有限算力，并由确定性控制器审核和调度动作。按共同的计算筛选标准衡量，T-REX获得最高结构差异命中吞吐。结构阈值命中不等于实验结合，评审也未盲法且未报告一致性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。科学目标是蛋白binder从头设计，直接属于蛋白质工程研究。
  - 原文位置：Full text, local TXT line 30；核验TXT行号 30；引文：de novo protein binder design
- 多步行动过程：yes。campaign按阶段累积结果并据此调度后续计算工作。
  - 原文位置：Full text, local TXT line 10；核验TXT行号 10；引文：Over the course of a design campaign, T-REX leverages large language model
- 至少一种Agent能力：yes。Agent决定救援、探索或利用不同路线，并由确定性控制器校验执行。
  - 原文位置：Full text, local TXT line 11；核验TXT行号 11；引文：decide whether to rescue promising candidates, explore alternative settings, or exploit productive routes
- 明确科研流程角色：yes。系统在多个蛋白靶点上作为计算设计campaign控制器接受评估。
  - 原文位置：Full text, local TXT line 13；核验TXT行号 13；引文：Across seven targets, we find that T-REX adaptively allocates its compute

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.06 蛋白质科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入蛋白质工程/药物发现对象模块；其结果是计算binder设计campaign吞吐，不能与实验确认的de novo结合物数量混同。

### 2.3 容易混淆的边界

归入蛋白质工程/药物发现对象模块；其结果是计算binder设计campaign吞吐，不能与实验确认的de novo结合物数量混同。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

T-REX是binder设计campaign控制器，LLM Agent根据累积结果在rescue、explore、exploit策略间选择；确定性控制器检查动作并调度多个蛋白生成模型和结构评价工具。

### 3.3 自主能力

Agent决定救援、探索或利用不同路线，并由确定性控制器校验执行。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把Agent决策用于高通量蛋白设计资源编排，并以靶点依赖的救援、探索和利用策略比较campaign效率。

### 4.2 系统流程与组件

作者在七个靶点开展高通量de novo binder设计，比较T-REX与固定策略基线；以共同计算筛选标准下每GPU小时产生的TM0.6结构命中数衡量吞吐，并观察不同靶点的资源分配。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评估基于七靶点的计算设计campaign和共同in-silico资格标准，报告结构不同的命中数量及单位算力吞吐；研究未以所有候选的实验结合测定作为主验证。

### 5.2 基线、指标与结果

T-REX按靶点适配计算资源，在七个靶点上获得相较基线更高的结构性命中吞吐；结果表明调度策略有计算优势，但结构筛选命中不等于实验结合binder。

### 5.3 科学贡献与证据强度

贡献是把Agent决策用于高通量蛋白设计资源编排，并以靶点依赖的救援、探索和利用策略比较campaign效率。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较提出单一更强蛋白生成模型，T-REX协调多个现有专用模型和评价器；与静态pipeline相比，它根据累积输出动态改变资源投向。

## 7. 局限性与风险

命中定义依赖in-silico结构阈值和评审标注，未盲法且未评估评审者一致性；实验表达、稳定性和结合验证仍是必要后续步骤。

## 8. 对综述写作的价值

可用于比较Agent对蛋白binder设计campaign的算力调度能力与计算命中、实验结合之间的差异。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

T-REX依据七个靶点的累积设计结果动态分配蛋白生成计算，在统一的计算结构标准下提高不同结构命中的吞吐。其优势属于in-silico campaign效率，binder是否表达和结合仍待实验确认。

### 9.2 速记版 pipeline

作者在七个靶点开展高通量de novo binder设计，比较T-REX与固定策略基线；以共同计算筛选标准下每GPU小时产生的TM0.6结构命中数衡量吞吐，并观察不同靶点的资源分配。

### 9.3 标注字段汇总

```text
paper_id=ASD-1022
inclusion_status=to_read
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.06
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 结合体结构可由计算评估 | “de novo protein binder design” · L21 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算结构评价和筛选 | “structurally distinct hits compared to all baselines” · L25 |
| 系统自主性 | L2 闭环执行者 | Agent自主分配计算资源并选择策略 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
