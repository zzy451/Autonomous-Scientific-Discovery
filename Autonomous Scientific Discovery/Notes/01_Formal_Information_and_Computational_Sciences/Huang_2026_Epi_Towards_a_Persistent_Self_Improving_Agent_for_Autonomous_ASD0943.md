# Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research

**论文信息**

- ID：ASD-0943
- 标题：Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research
- 作者：Yue Huang; Zhangchen Xu; Xiaonan Luo; Zheyuan Liu; Lichi Li; Yiping Wang; Peiyang Song; Eric Gabriel Ramos; Enze Xie; Olexandr Isayev; Paul Liang; Nouha Dziri; Huan Sun; Jianfeng Gao; Ying Liu; Misha Sra; Xiangliang Zhang; Alex Pentland; Zichen Chen
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.24944
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0943.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Huang_2026_Epi_Towards_a_Persistent_Self_Improving_Agent_for_Autonomous_ASD0943.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | Epi是可跨模型会话持续研究的自主Agent，通过持久研究历史、层级记忆、分支探索和独立审查保持连续性，并从实验中积累经验。作者报告其在数学优化等任务中产生120项纪录，包括12个族的20项数值界纪录和8个族的100项构造纪录。 | 本地全文：ASD-0943中与研究目标/科学问题直接相关的原文句子；核验TXT行号 446 | We present Épi, an autonomous research agent that sustains investigations across model sessions and evolves its methods through accumulated experience. Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity, learn from experiments, and explore and revisit alternative approaches. Its experiments run across session boundaries, and a fixed verifier evaluates their outputs. Épi produced 120 record-setting results, comprising 20 numerical bound records across 12 families and 100 construction records across eight families. These include an approximately 84-fold narrower interval for the nn-queens constant and a more than 3.6-million-fold narrower rigorous interval for the quartic Feigenbaum attractor dimension. Exact dual certificates establish that the Cohn–Elkies linear-programming bound cannot be sharp in dimensions 10 and 11. Beyond numerical improvements, Épi gives a computer-assisted proof of Tuza’s conjecture for split graphs with an eight-vertex clique part and at most three triangle-active neighborhood types, with arbitrary multiplicities. We extend this research process to algorithmic coding with Épi-turbo, a lightweight configuration that develops executable solvers for tasks including vehicle routing, scheduling and production planning. On 30 FrontierOR tasks, Épi-turbo achieves a 5.4% higher total benchmark score than Codex at 64% of its model cost, using the same underlying model and reasoning effort. Épi is designed to support human understanding by connecting computational results to explicit methods and mathematical arguments that researchers can examine and build upon. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | Agent跨会话保存研究状态，运行实验并更新经验；采用分支探索和独立验证器检查候选解，再延续或重访研究方向。 | 本地全文：ASD-0943中与多步行动/研究流程直接相关的原文句子；核验TXT行号 446 | Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity, learn from experiments, and explore and revisit alternative approaches. | 高（一手正文；非独立复现） |
| Agent实现与能力 | Epi以持久历史和层级记忆连接不同模型会话，支持研究分支、独立审查及对先前探索路线的重访。 | 本地全文：ASD-0943中与Agent实现与能力直接相关的原文句子；核验TXT行号 520 | Mathematical discovery provides a concrete demonstration of this research process: the agent develops methods whose outputs can be checked as constructions, bounds or proofs. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 作者在数值界和构造任务族中评估，并报告120项纪录：12个族的20项数值界纪录及8个族的100项构造纪录。 | 本地全文：ASD-0943中与实验任务与验证设置直接相关的原文句子；核验TXT行号 446 | Its experiments run across session boundaries, and a fixed verifier evaluates their outputs. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 正文报告120项记录性结果，覆盖数值界和构造问题；应视为所选优化任务上的作者报告，不外推为一般科研能力。 贡献是把跨会话持久记忆、分支实验与独立验证结合，面向长时段自主研究。 | 本地全文中包含该原句的位置；核验TXT行号 446 | Épi produced 120 record-setting results, comprising 20 numerical bound records across 12 families and 100 construction records across eight families. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Epi是可跨模型会话持续研究的自主Agent，通过持久研究历史、层级记忆、分支探索和独立审查保持连续性，并从实验中积累经验。作者报告其在数学优化等任务中产生120项纪录，包括12个族的20项数值界纪录和8个族的100项构造纪录。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。Epi是可跨模型会话持续研究的自主Agent，通过持久研究历史、层级记忆、分支探索和独立审查保持连续性，并从实验中积累经验。作者报告其在数学优化等任务中产生120项纪录，包括12个族的20项数值界纪录和8个族的100项构造纪录。
  - 原文位置：本地全文：ASD-0943中与研究目标/科学问题直接相关的原文句子；核验TXT行号 446；引文：We present Épi, an autonomous research agent that sustains investigations across model sessions and evolves its methods through accumulated experience. Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity, learn from experiments, and explore and revisit alternative approaches. Its experiments run across session boundaries, and a fixed verifier evaluates their outputs. Épi produced 120 record-setting results, comprising 20 numerical bound records across 12 families and 100 construction records across eight families. These include an approximately 84-fold narrower interval for the nn-queens constant and a more than 3.6-million-fold narrower rigorous interval for the quartic Feigenbaum attractor dimension. Exact dual certificates establish that the Cohn–Elkies linear-programming bound cannot be sharp in dimensions 10 and 11. Beyond numerical improvements, Épi gives a computer-assisted proof of Tuza’s conjecture for split graphs with an eight-vertex clique part and at most three triangle-active neighborhood types, with arbitrary multiplicities. We extend this research process to algorithmic coding with Épi-turbo, a lightweight configuration that develops executable solvers for tasks including vehicle routing, scheduling and production planning. On 30 FrontierOR tasks, Épi-turbo achieves a 5.4% higher total benchmark score than Codex at 64% of its model cost, using the same underlying model and reasoning effort. Épi is designed to support human understanding by connecting computational results to explicit methods and mathematical arguments that researchers can examine and build upon.
- 多步行动过程：yes。Agent跨会话保存研究状态，运行实验并更新经验；采用分支探索和独立验证器检查候选解，再延续或重访研究方向。
  - 原文位置：本地全文：ASD-0943中与多步行动/研究流程直接相关的原文句子；核验TXT行号 446；引文：Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity, learn from experiments, and explore and revisit alternative approaches.
- 至少一种Agent能力：yes。Epi以持久历史和层级记忆连接不同模型会话，支持研究分支、独立审查及对先前探索路线的重访。
  - 原文位置：本地全文：ASD-0943中与Agent实现与能力直接相关的原文句子；核验TXT行号 520；引文：Mathematical discovery provides a concrete demonstration of this research process: the agent develops methods whose outputs can be checked as constructions, bounds or proofs.
- 明确科研流程角色：yes。作者在数值界和构造任务族中评估，并报告120项纪录：12个族的20项数值界纪录及8个族的100项构造纪录。
  - 原文位置：本地全文：ASD-0943中与实验任务与验证设置直接相关的原文句子；核验TXT行号 446；引文：Its experiments run across session boundaries, and a fixed verifier evaluates their outputs.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;09;10
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01 数学；09.05.07 水利工程；10.04 交通运输科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01, 09, 10；01.01, 09.05.07, 10.04）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01, 09, 10；01.01, 09.05.07, 10.04）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

Epi以持久历史和层级记忆连接不同模型会话，支持研究分支、独立审查及对先前探索路线的重访。

### 3.3 自主能力

Epi以持久历史和层级记忆连接不同模型会话，支持研究分支、独立审查及对先前探索路线的重访。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把跨会话持久记忆、分支实验与独立验证结合，面向长时段自主研究。

### 4.2 系统流程与组件

Agent跨会话保存研究状态，运行实验并更新经验；采用分支探索和独立验证器检查候选解，再延续或重访研究方向。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者在数值界和构造任务族中评估，并报告120项纪录：12个族的20项数值界纪录及8个族的100项构造纪录。

### 5.2 基线、指标与结果

正文报告120项记录性结果，覆盖数值界和构造问题；应视为所选优化任务上的作者报告，不外推为一般科研能力。

### 5.3 科学贡献与证据强度

贡献是把跨会话持久记忆、分支实验与独立验证结合，面向长时段自主研究。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

成果集中于论文列举的可计算任务族；“record-setting”依赖基准、已有记录和验证器覆盖。

## 8. 对综述写作的价值

可用于综述“Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Epi跨会话积累研究经验，并报告数值界与构造任务中的120项纪录。

### 9.2 速记版 pipeline

Agent跨会话保存研究状态，运行实验并更新经验；采用分支探索和独立验证器检查候选解，再延续或重访研究方向。

### 9.3 标注字段汇总

```text
paper_id=ASD-0943
inclusion_status=to_read
scientific_object_modules=01;09;10
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01;09.05.07;10.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.01.12` 离散数学与组合数学；二级：`01.01`。
- 原文位置：PDF p.2。
- 判定：n皇后、组合构造和Tuza猜想直接支持离散数学；数值区间及动力系统另记数学多标签。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
