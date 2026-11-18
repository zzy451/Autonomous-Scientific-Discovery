# VortexChat: An agentic framework for autonomous multi-objective integrated photonic design

**论文信息**

- ID：ASD-1044
- 标题：VortexChat: An agentic framework for autonomous multi-objective integrated photonic design
- 作者：Faqian Chong; Yulun Wu; Shilong Li; Andrew Forbes; Hongsheng Chen; Song Han
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.20688
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1044.txt
- PDF / 本地文件路径：Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Chong_2026_VortexChat_An_agentic_framework_for_autonomous_multi_objective_integrated_ASD1044.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 面向集成光子器件的自然语言驱动逆向设计。 | Abstract；核验TXT行号 27 | agentic framework for the autonomous, end-to-end inverse design of integrated photonic devices directly from natural language specifications. | 高（一手正文；非独立复现） |
| Agent流程 | LLM决策Agent编排拓扑生成、梯度优化和全波电磁仿真。 | Abstract；核验TXT行号 29 | large language model (LLM) decision agent with topology generation, gradient-based refinement, and full-wave electromagnetic simulation. | 高（一手正文；非独立复现） |
| 反馈闭环 | 系统依照仿真反馈更新策略，处理多目标约束。 | Abstract；核验TXT行号 32 | update strategies based on feedback | 高（一手正文；非独立复现） |
| Benchmark | Vortex100评估效率、模式纯度和带宽等联合设计要求。 | Abstract；核验TXT行号 33 | Constrained by the absolute metrics of the Vortex100 Benchmark | 高（一手正文；非独立复现） |
| 实物验证 | 制作宽带太赫兹perfect vortex beam multiplexer并测量。 | Abstract；核验TXT行号 36 | we fabricated a broadband terahertz perfect vortex beam multiplexer | 高（一手正文；非独立复现） |
| 实验结果 | 测量验证高效率、高模式纯度和低通道串扰，与全波模拟一致。 | Abstract；核验TXT行号 37 | with measurements confirming high-efficiency operation, high mode purity and low inter-channel crosstalk in agreement with full- wave simulations. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | Vortex100评估集成光子器件设计，且制作并测量太赫兹涡旋光束复用器；光电器件工程代码适配。 | TXT line 36；核验TXT行号 36 | we fabricated a broadband terahertz perfect vortex beam multiplexer, autonomously designed by VortexChat, with measurements confirming high-efficiency operation, high mode purity and low inter-channel crosstalk in agreement with full- wave simulations. These | 高（一手正文；非独立复现） |

## 0. 摘要翻译

VortexChat根据自然语言规格自主设计集成光子器件，以拓扑生成、梯度优化和全波电磁仿真组成反馈闭环。除Vortex100系统评估外，作者制作了宽带太赫兹涡旋光束复用器并测量验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是将自然语言光学规格转为可制造集成光子器件。
  - 原文位置：Abstract；核验TXT行号 27；引文：agentic framework for the autonomous, end-to-end inverse design of integrated photonic devices directly from natural language specifications.
- 多步行动过程：yes。系统分解目标、调用拓扑生成/梯度优化/全波仿真并根据反馈更新。
  - 原文位置：Abstract；核验TXT行号 31；引文：enables the system to iteratively decompose design objectives, orchestrate computational tools, and update strategies based on feedback with minimal human intervention.
- 至少一种Agent能力：yes。通过Vortex100反复迭代并在无human-in-loop情况下满足阈值。
  - 原文位置：Abstract；核验TXT行号 34；引文：VortexChat autonomously generates devices that strictly meet all predefined performance thresholds without any human-in-the-loop.
- 明确科研流程角色：yes。自主进行集成光子器件逆向设计，并制作器件实验验证。
  - 原文位置：Abstract；核验TXT行号 36；引文：we fabricated a broadband terahertz perfect vortex beam multiplexer

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：09
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：09（仅归档，不覆盖其他模块）
- 模块内分类路径：09.08.03 光电器件
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

Vortex100评估集成光子器件设计，且制作并测量太赫兹涡旋光束复用器；光电器件工程代码适配。

### 2.3 容易混淆的边界

Vortex100评估集成光子器件设计，且制作并测量太赫兹涡旋光束复用器；光电器件工程代码适配。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent

### 3.2 科研流程角色

scientific_question_formulation；experimental_design；simulation_modeling；tool_use_and_code_execution；experiment_execution；data_analysis

LLM决策Agent调用拓扑生成器、梯度优化和全波电磁仿真工具，自动执行多目标设计。

### 3.3 自主能力

通过Vortex100反复迭代并在无human-in-loop情况下满足阈值。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献为满足目标约束的光子器件设计及实测；系统贡献为自然语言到器件的闭环工具编排。

### 4.2 系统流程与组件

解析规格；形成结构/性能目标；生成拓扑；仿真并按反馈优化；检查制造约束；输出器件结构并加工测量。 输入光学规格后，决策Agent生成结构拓扑，调用梯度优化和全波电磁仿真，按多目标反馈更新结构；选定方案再加工并测量器件。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

Vortex100 benchmark多目标测试；电磁全波仿真；制作宽带太赫兹器件并测量效率、模式纯度和串扰。

### 5.2 基线、指标与结果

Vortex100整体成功率71%；实验器件的测量确认高效率、高模式纯度、低通道串扰且与模拟一致。

### 5.3 科学贡献与证据强度

科学贡献为满足目标约束的光子器件设计及实测；系统贡献为自然语言到器件的闭环工具编排。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

从仿真型逆向设计扩展到Agent驱动的目标理解、工具选择、反馈优化及实物验证。

## 7. 局限性与风险

Benchmark成功率仍有失败任务；单一器件样机不足以证明普遍可制造性或跨设计族迁移。

## 8. 对综述写作的价值

可作为Agent驱动器件设计、闭环仿真和实物实验验证的代表案例。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

VortexChat闭环设计并实测验证太赫兹光子器件。

### 9.2 速记版 pipeline

解析规格；形成结构/性能目标；生成拓扑；仿真并按反馈优化；检查制造约束；输出器件结构并加工测量。 输入光学规格后，决策Agent生成结构拓扑，调用梯度优化和全波电磁仿真，按多目标反馈更新结构；选定方案再加工并测量器件。

### 9.3 标注字段汇总

```text
paper_id=ASD-1044
inclusion_status=to_read
scientific_object_modules=09
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=09
module_taxonomy_codes=09.08.03
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O4 需物理检验 | 设计需实物验证的光子器件 | “integrated photonic devices” · L38 |
| 验证强度 | V3 物理实验 | 制作太赫兹器件并测量验证性能指标 | “fabricated a broadband terahertz” · L25 |
| 系统自主性 | L2 闭环执行者 | 依据仿真反馈自主更新拓扑和优化策略 | — |

- 强验证（V3–V4）：是
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
