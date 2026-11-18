# FormaTheoria: Constructing Large-Scale Lean Theories from Mathematical Literature $-$ Toward the Formalization of the Classification of Finite Simple Groups

**论文信息**

- ID：ASD-1076
- 标题：FormaTheoria: Constructing Large-Scale Lean Theories from Mathematical Literature $-$ Toward the Formalization of the Classification of Finite Simple Groups
- 作者：Nie, Tianjiao; Zhang, Ao; Tang, Yusen; Testa, Damiano; Yau, Shing-Tung; Li, Peng; Zhou, Yuan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.10894
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1076.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Tianjiao_2026_FormaTheoria_Constructing_Large_Scale_Lean_Theories_from_Mathematical_Literature_ASD1076.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象 | 先进数学文献中的大规模理论重构。 | TXT line 574；核验TXT行号 574 | We present FormaTheoria, an end-to-end, AI-assisted workflow that coordinates source acquisition, formalization, proof construction, recursive dependency discovery, independent review, and reconciliation, while preserving provenance and protecting approved declarations. | 高（一手正文；非独立复现） |
| 问题 | 需发现隐含依赖并保持语义忠实。 | TXT line 6239；核验TXT行号 6239 | The workflow combines source retrieval, semantic translation, graph-based proof construction, on-demand dependency discovery, independent review, constrained reconciliation, and human escalation, while maintaining provenance and protecting approved declarations from unsupported downstream changes. | 高（一手正文；非独立复现） |
| 流程 | 从来源采集到独立审查和调和。 | TXT line 6253；核验TXT行号 6253 | Review rejected the first candidate for most PF Part I sections and turned translation into an iterative generate–check–revise process. | 高（一手正文；非独立复现） |
| 验证范围 | 围绕有限单群分类形式化目标组织大型数学理论。 | TXT line 3678；核验TXT行号 3678 | The formalization draws on 15 books and papers, covering 1,037 consulted pages (Table 2). | 高（一手正文；非独立复现） |
| 人机审查 | 工作流明确包含独立审查。 | TXT line 6264；核验TXT行号 6264 | The present study remains a case study of a single large-scale formalization in finite-group theory. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

FormaTheoria面向从异质数学文献构建大规模Lean理论，处理隐含依赖发现、源文缺陷修正、语义保持与跨来源调和。系统协调文献采集、形式化、证明构造、递归依赖发现、独立审查和冲突调和，目标案例指向有限单群分类相关理论。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标为从数学文献重构大规模一致理论。
  - 原文位置：TXT line 6239；核验TXT行号 6239；引文：The workflow combines source retrieval, semantic translation, graph-based proof construction, on-demand dependency discovery, independent review, constrained reconciliation, and human escalation, while maintaining provenance and protecting approved declarations from unsupported downstream changes.
- 多步行动过程：yes。工作流包含来源获取、形式化、证明、依赖发现、独立审查及调和。
  - 原文位置：TXT line 574；核验TXT行号 574；引文：We present FormaTheoria, an end-to-end, AI-assisted workflow that coordinates source acquisition, formalization, proof construction, recursive dependency discovery, independent review, and reconciliation, while preserving provenance and protecting approved declarations.
- 至少一种Agent能力：yes。多个Agent协调文献形式化及交叉审查。
  - 原文位置：TXT line 574；核验TXT行号 574；引文：A shared agent framework supports long-horizon execution through tool use, context compaction, review-gated termination, section-level source context, and dependency-aware batch parallelization.
- 明确科研流程角色：yes。承担有限单群分类相关数学文献到Lean理论的构造。
  - 原文位置：TXT line 574；核验TXT行号 574；引文：This process raises four challenges: discovering implicit dependencies, correcting source defects, preserving semantic fidelity, and reconciling cross-source misalignments.

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

对象是纯数学理论与证明，归入01数学。

### 2.3 容易混淆的边界

对象是纯数学理论与证明，归入01数学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

multi_agent_formalization

### 3.2 科研流程角色

literature_formalization；proof_construction；review

AI辅助多阶段Agent协同来源解析、Lean形式化、依赖发现、证明构造和独立审查，保留来源关联。

### 3.3 自主能力

多个Agent协调文献形式化及交叉审查。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是大型文献形式化的来源追踪与独立审阅流程；数学贡献取决于最终已形式化定理及其范围。

### 4.2 系统流程与组件

输入为异质数学文献；系统获取来源并抽取陈述，Agent构建形式化定义和证明，递归寻找依赖，独立审阅者检查语义及来源一致性，调和冲突后形成可编译理论库。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

通过独立审查、Lean证明构造和跨来源一致性调和验证；目标是有限单群分类相关大规模理论。

### 5.2 基线、指标与结果

作者提出端到端文献到理论工作流；需依正文实证部分核定已形式化规模及完成度。

### 5.3 科学贡献与证据强度

系统贡献是大型文献形式化的来源追踪与独立审阅流程；数学贡献取决于最终已形式化定理及其范围。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

区别于逐条翻译定理，强调依赖、源缺陷和跨文献语义调和。

## 7. 局限性与风险

- author_stated：核心挑战包括隐含依赖、源缺陷、语义保真和跨来源不一致。
- reviewer_inference：系统流程描述不等于有限单群分类整体已形式化完成。

## 8. 对综述写作的价值

适合讨论长程数学形式化Agent的文献来源管理和语义审查。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

FormaTheoria协调文献采集、证明构造和独立审查以构建大规模Lean理论。

### 9.2 速记版 pipeline

输入为异质数学文献；系统获取来源并抽取陈述，Agent构建形式化定义和证明，递归寻找依赖，独立审阅者检查语义及来源一致性，调和冲突后形成可编译理论库。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1076
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
| 问题开放度 | O3 新实例 | 从文献形式化有限群理论，答案可由Lean证明助手机器检验 | “15 books and papers” · L24 |
| 验证强度 | V2 计算/仿真/回顾性 | 独立审查和Lean证明构造，属形式化验证而非新数学发现实验 | “independent review” · L38 |
| 系统自主性 | L2 闭环执行者 | Agent递归发现依赖并迭代生成审查修订，人最终审定 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
