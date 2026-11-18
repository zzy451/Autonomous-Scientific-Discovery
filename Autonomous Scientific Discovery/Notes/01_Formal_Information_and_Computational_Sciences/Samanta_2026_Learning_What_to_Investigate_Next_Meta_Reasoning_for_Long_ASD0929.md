# Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents

**论文信息**

- ID：ASD-0929
- 标题：Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents
- 作者：Ankur Samanta; Yonathan Efroni; Paul Sajda; Kaveh Hassani; Anirudh Goyal
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.02525
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0929.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Samanta_2026_Learning_What_to_Investigate_Next_Meta_Reasoning_for_Long_ASD0929.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | 本文研究长程研究Agent如何决定下一步调查内容，提出 MIRA 将研究资源分配与具体执行拆开：元推理器选择调查方向并生成工作单，执行器完成工作；MIRA-AC 依据回报预测和策略优化学习选择。实验包含 IMOProofBench、HillClimbBench-RMT 和 HillClimbBench-Loop，并设置输出token匹配的定理证明对照。 | 本地全文：ASD-0929中与研究目标/科学问题直接相关的原文句子；核验TXT行号 552 | Long-horizon research agents must decide both how to investigate and what to investigate next as evidence accumulates. This is hard to learn because such decisions are sparse in long execution traces, and their consequences may emerge several investigations later. We introduce Meta-reasoning for Iterative Research Agents (MIRA), a hierarchical architecture separating research allocation from execution. An outer-loop meta-reasoner curates context from a persistent research record, then writes a work order for the next investigation or ends the episode. A fresh inner-loop executor carries out each work order, making execution part of the transition between meta-reasoning actions. Without policy training, MIRA improves long-horizon inference and allocates additional compute more effectively in theorem proving and open-ended neural-architecture research. Its decision boundaries also provide natural units for credit assignment. At each boundary, we train a generative critic to forecast expected remaining return from partial states, outperforming token-level alternatives. Cross-environment pretraining improves forecasting and adaptation, yielding a transferable prior for valuing partial progress. We use this prior to initialize MIRA-AC, a generative actor–critic jointly trained to forecast remaining return and choose the next investigation, without a separate critic model. MIRA-AC concentrates policy optimization on meta-reasoning decisions, enabling efficient long-horizon reinforcement learning without directly optimizing the longer execution traces they initiate. Training MIRA-AC on the model’s own proxy hill-climbing signals improves gold performance across four autoresearch environments; the actor transfers with cross-environment value initialization. Together, these results show that meta-reasoning can be learned as an explicit policy for directing long-horizon autonomous research. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 元推理器根据当前研究状态分配有限的后续干预，生成窄化工作单；执行器完成指定调查并反馈结果，系统据此更新长期决策。 | 本地全文：ASD-0929中与多步行动/研究流程直接相关的原文句子；核验TXT行号 654 | Figure 1: MIRA separates research allocation from execution. At each research-decision boundary, the outer loop reads the persistent research record HtH_{t} and curates evidence bearing on the most consequential unresolved uncertainty into an observation oto_{t}. It then produces a meta-reasoning action ata_{t}, a complete decision response comprising its reasoning followed by either a work order or a stopping decision. For a work order, a fresh executor carries out the investigation and writes its results back to the persistent record, producing Ht+1H_{t+1}. The next outer-loop observation is then constructed from this updated record; a stopping decision instead terminates the research episode. Thus, each investigation, however long, is represented as one transition at the meta-reasoning level. | 高（一手正文；非独立复现） |
| Agent实现与能力 | MIRA 由选择后续调查的元推理器和执行工作单的Agent组成；MIRA-AC 进一步以回报预测和策略优化训练元决策。 | 本地全文中包含该原句的位置；核验TXT行号 841 | Thus, the unit of control is the research decision: the policy chooses what to investigate or whether to terminate, while the executor determines how a selected investigation is carried out. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 论文在 IMOProofBench 与 HillClimbBench-RMT 测试，并在 HillClimbBench-Loop 上与 Codex 比较；定理证明包含输出token数量匹配的继续生成对照。 | 本地全文：ASD-0929中与实验任务与验证设置直接相关的原文句子；核验TXT行号 2019 | All comparisons in this subsection use frozen model weights. We compare GPT-5.5, Codex, and MIRA. GPT-5.5 uses the task interface directly; Codex operates as one persistent tool-using session; and MIRA assigns each investigation to a fresh Codex inner loop. The Codex and MIRA conditions use the same underlying GPT-5.5 model, Codex harness, and tools, while MIRA adds explicit meta-reasoning and curated context resets. We test the three conditions on IMOProofBench (Luong et al., 2025) and HillClimbBench-RMT, and compare MIRA with Codex on HillClimbBench-Loop. For theorem proving, we also include output-token-matched continuation controls. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 正文以多个基准和案例展示针对性调查可以优于宽泛搜索；例如 bnlearn:057 中，两次干预将结构恢复分数由 0.935 提升至 0.982。 科学贡献是把研究中“下一步该查什么”作为长程资源分配问题；系统贡献是元推理器与执行器分离及其学习方法。 | 本地全文中包含该原句的位置；核验TXT行号 8014 | The reverse pattern appears on bnlearn:057. Untrained MIRA used two interventions to raise its score for recovering which variables affect one another from 0.935 to 0.982, then issued the narrow work order “close the SHD=1 gap by identifying and adding the single missing edge” (B-D009). The executor compared the effects implied by the current graph with the variables affected by each intervention and reported, “Identified and added the single missing edge X15-¿X14 to close the SHD=1 gap” (B-R009). Untrained MIRA therefore reached a gold score of 1.0. MIRA-AC’s reconstruction based on its interventions made substantial progress, but its early searches incurred wall-time failures and later graph-learning methods and exhaustive edge-swap searches concluded that the current SHD=7 graph was “the best achievable” (A-R011). It finished at 0.844. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文研究长程研究Agent如何决定下一步调查内容，提出 MIRA 将研究资源分配与具体执行拆开：元推理器选择调查方向并生成工作单，执行器完成工作；MIRA-AC 依据回报预测和策略优化学习选择。实验包含 IMOProofBench、HillClimbBench-RMT 和 HillClimbBench-Loop，并设置输出token匹配的定理证明对照。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文研究长程研究Agent如何决定下一步调查内容，提出 MIRA 将研究资源分配与具体执行拆开：元推理器选择调查方向并生成工作单，执行器完成工作；MIRA-AC 依据回报预测和策略优化学习选择。实验包含 IMOProofBench、HillClimbBench-RMT 和 HillClimbBench-Loop，并设置输出token匹配的定理证明对照。
  - 原文位置：本地全文：ASD-0929中与研究目标/科学问题直接相关的原文句子；核验TXT行号 552；引文：Long-horizon research agents must decide both how to investigate and what to investigate next as evidence accumulates. This is hard to learn because such decisions are sparse in long execution traces, and their consequences may emerge several investigations later. We introduce Meta-reasoning for Iterative Research Agents (MIRA), a hierarchical architecture separating research allocation from execution. An outer-loop meta-reasoner curates context from a persistent research record, then writes a work order for the next investigation or ends the episode. A fresh inner-loop executor carries out each work order, making execution part of the transition between meta-reasoning actions. Without policy training, MIRA improves long-horizon inference and allocates additional compute more effectively in theorem proving and open-ended neural-architecture research. Its decision boundaries also provide natural units for credit assignment. At each boundary, we train a generative critic to forecast expected remaining return from partial states, outperforming token-level alternatives. Cross-environment pretraining improves forecasting and adaptation, yielding a transferable prior for valuing partial progress. We use this prior to initialize MIRA-AC, a generative actor–critic jointly trained to forecast remaining return and choose the next investigation, without a separate critic model. MIRA-AC concentrates policy optimization on meta-reasoning decisions, enabling efficient long-horizon reinforcement learning without directly optimizing the longer execution traces they initiate. Training MIRA-AC on the model’s own proxy hill-climbing signals improves gold performance across four autoresearch environments; the actor transfers with cross-environment value initialization. Together, these results show that meta-reasoning can be learned as an explicit policy for directing long-horizon autonomous research.
- 多步行动过程：yes。元推理器根据当前研究状态分配有限的后续干预，生成窄化工作单；执行器完成指定调查并反馈结果，系统据此更新长期决策。
  - 原文位置：本地全文：ASD-0929中与多步行动/研究流程直接相关的原文句子；核验TXT行号 654；引文：Figure 1: MIRA separates research allocation from execution. At each research-decision boundary, the outer loop reads the persistent research record HtH_{t} and curates evidence bearing on the most consequential unresolved uncertainty into an observation oto_{t}. It then produces a meta-reasoning action ata_{t}, a complete decision response comprising its reasoning followed by either a work order or a stopping decision. For a work order, a fresh executor carries out the investigation and writes its results back to the persistent record, producing Ht+1H_{t+1}. The next outer-loop observation is then constructed from this updated record; a stopping decision instead terminates the research episode. Thus, each investigation, however long, is represented as one transition at the meta-reasoning level.
- 至少一种Agent能力：yes。MIRA 由选择后续调查的元推理器和执行工作单的Agent组成；MIRA-AC 进一步以回报预测和策略优化训练元决策。
  - 原文位置：本地全文：ASD-0929中与Agent实现与能力直接相关的原文句子；核验TXT行号 841；引文：Thus, the unit of control is the research decision: the policy chooses what to investigate or whether to terminate, while the executor determines how a selected investigation is carried out.
- 明确科研流程角色：yes。论文在 IMOProofBench 与 HillClimbBench-RMT 测试，并在 HillClimbBench-Loop 上与 Codex 比较；定理证明包含输出token数量匹配的继续生成对照。
  - 原文位置：本地全文：ASD-0929中与实验任务与验证设置直接相关的原文句子；核验TXT行号 2019；引文：All comparisons in this subsection use frozen model weights. We compare GPT-5.5, Codex, and MIRA. GPT-5.5 uses the task interface directly; Codex operates as one persistent tool-using session; and MIRA assigns each investigation to a fresh Codex inner loop. The Codex and MIRA conditions use the same underlying GPT-5.5 model, Codex harness, and tools, while MIRA adds explicit meta-reasoning and curated context resets. We test the three conditions on IMOProofBench (Luong et al., 2025) and HillClimbBench-RMT, and compare MIRA with Codex on HillClimbBench-Loop. For theorem proving, we also include output-token-matched continuation controls.

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

MIRA 由选择后续调查的元推理器和执行工作单的Agent组成；MIRA-AC 进一步以回报预测和策略优化训练元决策。

### 3.3 自主能力

MIRA 由选择后续调查的元推理器和执行工作单的Agent组成；MIRA-AC 进一步以回报预测和策略优化训练元决策。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是把研究中“下一步该查什么”作为长程资源分配问题；系统贡献是元推理器与执行器分离及其学习方法。

### 4.2 系统流程与组件

元推理器根据当前研究状态分配有限的后续干预，生成窄化工作单；执行器完成指定调查并反馈结果，系统据此更新长期决策。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

论文在 IMOProofBench 与 HillClimbBench-RMT 测试，并在 HillClimbBench-Loop 上与 Codex 比较；定理证明包含输出token数量匹配的继续生成对照。

### 5.2 基线、指标与结果

正文以多个基准和案例展示针对性调查可以优于宽泛搜索；例如 bnlearn:057 中，两次干预将结构恢复分数由 0.935 提升至 0.982。

### 5.3 科学贡献与证据强度

科学贡献是把研究中“下一步该查什么”作为长程资源分配问题；系统贡献是元推理器与执行器分离及其学习方法。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

结果依赖选定的基准、执行器及回报定义；个别案例不能替代跨任务的总体比较，需按正文实验条件解读。

## 8. 对综述写作的价值

可用于综述“Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

MIRA 学习长程科研Agent应优先调查什么，并以工作单驱动执行器。

### 9.2 速记版 pipeline

元推理器根据当前研究状态分配有限的后续干预，生成窄化工作单；执行器完成指定调查并反馈结果，系统据此更新长期决策。

### 9.3 标注字段汇总

```text
paper_id=ASD-0929
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
| 问题开放度 | O2 既定基准 | 在IMOProofBench和HillClimbBench等预定义基准上评估 | “We test the three conditions on IMOProofBench” · L42 |
| 验证强度 | V1 基准/内部评测 | 以基准任务完成度和结构恢复分数等指标评估 | “two interventions to raise its score for recovering” · L25 |
| 系统自主性 | L2 闭环执行者 | 元推理器自主选择调查方向并生成工作单，执行器完成闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
