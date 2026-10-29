# Jianmu-Q: Bridging Quantum Field Theory and Quantum Hardware with AI Agents

**论文信息**

- ID：ASD-1069
- 标题：Jianmu-Q: Bridging Quantum Field Theory and Quantum Hardware with AI Agents
- 作者：Wang, Xiaolin; Guo, Xingyu; Li, Jinyang; Li, Tianyin; Wang, Enke; Wang, Lingxiao; Xing, Hongxi
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.21942
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1069.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Xiaolin_2026_Jianmu_Q_Bridging_Quantum_Field_Theory_and_Quantum_Hardware_ASD1069.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象与输入 | 输入为拉格朗日量/格点哈密顿量、外态和可观测量。 | TXT lines 22-25；核验TXT行号 22 | Here we introduce Jianmu-Q, a multi-agent framework that transforms natural-language descriptions of quantum field theories into quantum simulation workflows. Specialized agents handle theoretical formulation, lattice discretization, qubit mapping, and circuit design, while physical consistency checks and independent numerical calculations provide validation throughout the workflow. | 高（一手正文；非独立复现） |
| 多步验证 | 独立验证结合物理一致性、ED/TN和无噪声电路。 | TXT line 350；核验TXT行号 350 | Each agent receives structured input from the preceding stage, and review or | 高（一手正文；非独立复现） |
| Agent架构 | 阶段Agent传递结构化输入并接收复核结果。 | TXT line 131；核验TXT行号 131 | specifications: a Lagrangian or a lattice Hamiltonian, external states, and an observable M [Eq. | 高（一手正文；非独立复现） |
| 硬件角色 | 任务电路交由量子硬件执行。 | TXT line 135；核验TXT行号 135 | steps, independent validation comprises physical-consistency checks, ED and TN references for the same regulated finite-lattice | 高（一手正文；非独立复现） |
| 边界 | 无噪声模拟由确定性运行时执行而非LLM Agent。 | TXT lines 27-31；核验TXT行号 27 | benchmark the framework on three field theories of increasing complexity: the (1 + 1)-dimensional Nambu–Jona-Lasinio and Schwinger models, and a (2+1)-dimensional Z2 gauge theory. Across these systems, noiseless quantum-circuit simulations converge toward independent exact-diagonalization and tensor-network results, while selected circuits are executed on IBM quantum hardware, demon- strating an end-to-end, validation-guided approach to quantum simulation of field theories. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Jianmu-Q以多阶段Agent工作流连接量子场论问题、格点模型、量子比特编码、电路构造与量子硬件。各阶段传递结构化输入，审查和验证结果反馈给相关Agent。论文提出以物理一致性、精确对角化、张量网络及无噪声电路结果作独立交叉核验。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。从量子场论模型和可观测量生成硬件模拟任务。
  - 原文位置：TXT line 131；核验TXT行号 131；引文：specifications: a Lagrangian or a lattice Hamiltonian, external states, and an observable M [Eq.
- 多步行动过程：yes。工作流涵盖模型规整、编码、电路、硬件及独立验证。
  - 原文位置：TXT line 350；核验TXT行号 350；引文：Each agent receives structured input from the preceding stage, and review or
- 至少一种Agent能力：yes。多个阶段Agent传递结构化输入并返回审查/验证结果。
  - 原文位置：TXT line 350；核验TXT行号 350；引文：Each agent receives structured input from the preceding stage, and review or
- 明确科研流程角色：yes。连接QFT问题构造到量子硬件模拟和验证。
  - 原文位置：TXT line 132；核验TXT行号 132；引文：lattice formulation, a model-specific qubit encoding, and task-dependent circuits (state preparation, optional dynamics [dashed],

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02 物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为量子场论数值模拟及量子硬件，属02物理科学/量子信息。

### 2.3 容易混淆的边界

对象为量子场论数值模拟及量子硬件，属02物理科学/量子信息。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

multi_agent

### 3.2 科研流程角色

theory_to_hardware；circuit_generation；validation

多个阶段LLM Agent负责模型到电路的任务；确定性运行时承担无噪声模拟，量子硬件执行目标电路。

### 3.3 自主能力

多个阶段Agent传递结构化输入并返回审查/验证结果。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是从QFT描述到硬件电路的Agent协作接口；科学贡献是具体场论可观测量计算与验证案例。

### 4.2 系统流程与组件

输入拉格朗日量或格点哈密顿量、外态与可观测量；依序构造规整格点模型、模型特定量子编码和制备/演化/测量电路，交硬件执行，再用物理一致性、ED、张量网络及无噪声电路结果交叉验证，并将审核反馈回Agent。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

同一有限格点问题采用物理一致性检查、精确对角化、张量网络参考及无噪声电路结果比较；另涉及硬件执行。

### 5.2 基线、指标与结果

所见原文明确规定多重独立验证链；结果需依具体任务和硬件噪声分别判断。

### 5.3 科学贡献与证据强度

系统贡献是从QFT描述到硬件电路的Agent协作接口；科学贡献是具体场论可观测量计算与验证案例。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

将LLM Agent用于量子场论到量子硬件的流程衔接，结合传统ED/TN数值参考。

## 7. 局限性与风险

- author_stated：本文文本强调当前硬件可行性约束及规整有限格点问题。
- reviewer_inference：Agent生成的电路需依赖独立数值和物理检查，不能把LLM输出本身视为物理证据。

## 8. 对综述写作的价值

适合讨论Agent作为理论到硬件接口，以及确定性工具和独立验证的边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Jianmu-Q用多Agent工作流连接格点QFT问题与量子硬件并设置独立核验。

### 9.2 速记版 pipeline

输入拉格朗日量或格点哈密顿量、外态与可观测量；依序构造规整格点模型、模型特定量子编码和制备/演化/测量电路，交硬件执行，再用物理一致性、ED、张量网络及无噪声电路结果交叉验证，并将审核反馈回Agent。

### 9.3 标注字段汇总

```text
paper_id=ASD-1069
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.14` 粒子物理学；二级：`02.02`。
- 原文位置：PDF p.1。
- 判定：NJL/Schwinger及规范场模型计算，科学对象是量子场论而非量子计算工具。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
