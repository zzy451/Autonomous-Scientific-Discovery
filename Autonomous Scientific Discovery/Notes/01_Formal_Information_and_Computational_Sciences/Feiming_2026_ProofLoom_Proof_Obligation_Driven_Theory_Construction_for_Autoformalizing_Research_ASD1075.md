# ProofLoom: Proof-Obligation-Driven Theory Construction for Autoformalizing Research-Level Stochastic Optimization

**论文信息**

- ID：ASD-1075
- 标题：ProofLoom: Proof-Obligation-Driven Theory Construction for Autoformalizing Research-Level Stochastic Optimization
- 作者：Wang, Feiming; Li, Daibo; Yuan, Kun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.34960
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1075.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Feiming_2026_ProofLoom_Proof_Obligation_Driven_Theory_Construction_for_Autoformalizing_Research_ASD1075.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象 | 研究级随机优化及其收敛证明。 | TXT line 611；核验TXT行号 611 | We introduce ProofLoom, a fully automated LLM-agent system for Proof-Obligation-Driven Theory Construction. | 高（一手正文；非独立复现） |
| 输入 | 使用已发表算法、目标定理和原证明。 | TXT line 677；核验TXT行号 677 | Open obligations in the target proof determine which definitions, interfaces, and lemmas to reuse or construct next, driving the joint development of the model, supporting theory, and proof plans. | 高（一手正文；非独立复现） |
| 方法 | 证明义务决定后续定义和引理开发。 | TXT lines 1332-1338；核验TXT行号 1332 | We evaluate ProofLoom on fifteen optimization tasks and examine the mathematical infrastructure produced across 33 algorithm developments. The benchmark contains ten algorithms from Lan’s monograph (Lan, 2020) (FOML) and five research-paper algorithms: AMSGrad, STORM, SPIDER, PAGE, and Sharpness-Aware Minimization (SAM). The research-paper tasks cover online regret bounds, convergence guarantees for stochastic and finite-sum nonconvex optimization, and PAC-Bayes generalization bounds. | 高（一手正文；非独立复现） |
| 验证 | Lean检查形式证明，研究实验涉及多个公开算法。 | TXT lines 1840-1843；核验TXT行号 1840 | Source findings. Across the full audit, formalization identifies 28 independent discrepancies affecting 22 developments. They include incorrect formulas, proof gaps, and algorithm–analysis mismatches. Appendix B records their locations, evidence, and repair scopes. | 高（一手正文；非独立复现） |
| 贡献 | 对公开来源差异进行核查并维护形式化证据。 | TXT lines 1967-1975；核验TXT行号 1967 | Semantic review relies on LLM judgments; repeated errors can shift assumptions or conclusions away from the source. Construction, semantic checks, and audit records require additional model calls and Lean checks; research-level formalization can take hours. Our evaluation covers textbook and research-paper tasks in stochastic optimization. Prompts and control flow were initially developed on a small FOML subset, with infrastructure bugs fixed in subsequent iterations. reconstruct and prove use source proofs to identify intermediate obligations. Applicability to more abstract domains and less detailed proofs requires further evaluation. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

ProofLoom是面向随机优化研究的自动化LLM Agent系统，以证明义务驱动算法模型、数学基础设施和证明计划协同构造。系统从已发表算法、目标定理和源证明出发，按开放义务决定后续定义、接口和引理；证明停滞时诊断原因并调整模型或证明路线，最终以Lean检查证明。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。将研究级随机优化算法与收敛证明形式化。
  - 原文位置：TXT line 677；核验TXT行号 677；引文：Given a published algorithm, its target theorem, and its source proof, ProofLoom autonomously constructs the Lean algorithm model and develops the mathematical infrastructure required to complete the proof.
- 多步行动过程：yes。证明义务驱动定义、接口、引理和证明计划迭代。
  - 原文位置：TXT line 677；核验TXT行号 677；引文：Open obligations in the target proof determine which definitions, interfaces, and lemmas to reuse or construct next, driving the joint development of the model, supporting theory, and proof plans.
- 至少一种Agent能力：yes。Agent自动构建Lean模型并诊断证明停滞原因。
  - 原文位置：TXT line 677；核验TXT行号 677；引文：When proof construction stalls, ProofLoom diagnoses the cause using the source proof, the current Lean state, and prior proof attempts, then autonomously selects and executes the next steps: proving a missing fact, revising the proof route, or reconstructing the Lean model.
- 明确科研流程角色：yes。承担理论算法模型构造和形式证明开发。
  - 原文位置：TXT line 611；核验TXT行号 611；引文：Formalizing research-level stochastic optimization in Lean requires a Lean model of the algorithm and domain theory that connects foundational libraries to its convergence proof.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01 数学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为随机优化理论及形式证明，归入01数学理论。

### 2.3 容易混淆的边界

对象为随机优化理论及形式证明，归入01数学理论。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

formal_theory_agent

### 3.2 科研流程角色

theory_construction；proof_generation

LLM Agent与Lean 4证明助手协作，维护算法模型、领域理论、证明依赖和义务状态。

### 3.3 自主能力

Agent自动构建Lean模型并诊断证明停滞原因。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是随机优化算法和证明的形式化结果及源文献差异核查；系统贡献是证明义务驱动的模型—证明协同构造。

### 4.2 系统流程与组件

输入已发表算法、目标定理和原证明；系统先构造Lean算法模型，生成目标定理开放义务，再依据义务复用或新增定义、接口和引理；证明失败时诊断模型或证明缺口并调整路线，Lean内核核验最终证明。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

使用随机优化研究算法和定理案例，以Lean编译/内核检查为形式正确性验证，并分析证明义务驱动过程及停滞恢复。

### 5.2 基线、指标与结果

作者报告系统对研究级随机优化进行全自动形式化，并在出版来源中发现经核验差异。

### 5.3 科学贡献与证据强度

科学贡献是随机优化算法和证明的形式化结果及源文献差异核查；系统贡献是证明义务驱动的模型—证明协同构造。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

结合LLM数学推理与Lean形式证明，扩展从单次定理证明到算法模型和基础理论共同演化。

## 7. 局限性与风险

- author_stated：论文专设局限讨论，指出研究级形式化受源证明压缩及模型修订影响；须以原文Limitations具体范围为准。
- reviewer_inference：形式证明正确不自动证明所形式化算法模型忠实表达原论文意图。

## 8. 对综述写作的价值

适合讨论科研Agent如何以未完成证明义务驱动理论建模，而非只生成最终证明。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ProofLoom以开放证明义务驱动随机优化算法模型与Lean证明共同发展。

### 9.2 速记版 pipeline

输入已发表算法、目标定理和原证明；系统先构造Lean算法模型，生成目标定理开放义务，再依据义务复用或新增定义、接口和引理；证明失败时诊断模型或证明缺口并调整路线，Lean内核核验最终证明。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1075
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 随机优化证明可由Lean形式验证 | “fifteen optimization tasks” · L23 |
| 验证强度 | V2 计算/仿真/回顾性 | Lean类型检查器验证形式证明，发现源文献差异 | “formalization identifies 28 independent discrepancies” · L24 |
| 系统自主性 | L2 闭环执行者 | 证明义务驱动Agent自主构造定义和证明 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
