# Euler: Towards Human-Centered Multi-Agent Mathematical Discovery

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`01`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 01 | 01.01 数学 | 01.01.12 离散数学与组合数学 | 已落地 |

- 模块11：数学档案和provenance服务证明探索，独立验证是软件集成测试，没有科学证据理论或科研共同体的对象研究。
  - 证据：PDF 第 [15, 18, 19] 页；原文：The visualizations preserve source-linked records of investigations conducted across earlier workflow versions, including accepted dependencies, unresolved steps, and changes of approach.

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1080
- 标题：Euler: Towards Human-Centered Multi-Agent Mathematical Discovery
- 作者：Chen, Qiuyu; Wang, Qi; Xu, Liang; Jin, Xin; Xie, Baao; Zeng, Wenjun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.19864
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1080.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Qiuyu_2026_Euler_Towards_Human_Centered_Multi_Agent_Mathematical_Discovery_ASD1080.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标 | 建立人本数学研究系统。 | TXT line 305；核验TXT行号 305 | We present Euler, a human-centered mathematical research system built around a shared, structured representation of the research process. | 高（一手正文；非独立复现） |
| 研究表示 | 图结构记录陈述、假设、依赖、失败和验证证据。 | TXT line 350；核验TXT行号 350 | During execution, agents use the current unresolved problems and their dependencies to select tasks, retrieve relevant prior results and failures, and coordinate further reasoning. | 高（一手正文；非独立复现） |
| Agent行动 | Agent基于未解决问题与历史结果分配后续任务。 | TXT line 357；核验TXT行号 357 | A researcher can follow the premises of a conclusion, inspect an abandoned route, or ask agents about a specific mathematical step. | 高（一手正文；非独立复现） |
| 人类介入 | 研究者能追踪结论前提并询问步骤。 | TXT line 1999；核验TXT行号 1999 | At commit ea505c7, the repository’s GitHub Actions workflow completed its offline tests on Python 3.10 and Python 3.13 with 1,352 passing tests and two skips in each environment. | 高（一手正文；非独立复现） |
| 案例验证 | 论文以三个数学研究案例展示系统能力。 | TXT line 2210；核验TXT行号 2210 | Several research questions remain. The usefulness of the representation depends on the quality of the proposed routes, the accuracy of scope assignments, and the ability to retrieve the relevant dependencies and failures. LLM proof review h | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Euler是以人为中心的多Agent数学研究系统，使用共享研究图记录数学陈述、假设、证明依赖、备选路径、失败尝试和验证证据。Agent基于未解问题及依赖选择任务、检索先前结果并跨会话继续推理；研究者可检查证明路线、追问步骤或分支探索。论文以三个数学研究案例展示系统。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。面向数学研究过程的持续探索和结果验证。
  - 原文位置：TXT line 305；核验TXT行号 305；引文：We present Euler, a human-centered mathematical research system built around a shared, structured representation of the research process.
- 多步行动过程：yes。研究图管理问题、依赖、失败路径和验证证据，支持跨会话推进。
  - 原文位置：TXT line 350；核验TXT行号 350；引文：During execution, agents use the current unresolved problems and their dependencies to select tasks, retrieve relevant prior results and failures, and coordinate further reasoning.
- 至少一种Agent能力：yes。Agent基于未解决问题和依赖选择任务并协调推理。
  - 原文位置：TXT line 350；核验TXT行号 350；引文：During execution, agents use the current unresolved problems and their dependencies to select tasks, retrieve relevant prior results and failures, and coordinate further reasoning.
- 明确科研流程角色：yes。人类可检查论证、追问步骤并选择分支继续探索。
  - 原文位置：TXT line 357；核验TXT行号 357；引文：A researcher can follow the premises of a conclusion, inspect an abandoned route, or ask agents about a specific mathematical step.

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

对象为数学发现工作流和具体数学研究案例，归入01数学。

### 2.3 容易混淆的边界

对象为数学发现工作流和具体数学研究案例，归入01数学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

human_centered_multi_agent

### 3.2 科研流程角色

mathematical_discovery；proof_review；persistent_research

多Agent共享研究图和已接纳事实图；保留团队状态及先前尝试，研究者可回看并从保存节点恢复对话。

### 3.3 自主能力

Agent基于未解决问题和依赖选择任务并协调推理。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献取决于三个案例的具体数学结果；系统贡献是共享结构化研究表示、持久上下文及人类可追溯交互。

### 4.2 系统流程与组件

研究者指定数学目标和团队；Agent读取相关命题、依赖、先前尝试及证据后分工，提出结果经对应验证器检查并关联回研究图；共享状态支持后续会话继续、回看失败路线和探索替代分支。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

三个数学研究案例及软件验证；研究图/事实图记录声明范围与检查证据。

### 5.2 基线、指标与结果

论文展示跨会话、可追踪的数学研究工作流；案例支持系统功能，不构成统一数学能力基准。

### 5.3 科学贡献与证据强度

科学贡献取决于三个案例的具体数学结果；系统贡献是共享结构化研究表示、持久上下文及人类可追溯交互。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

在Fact Graph架构上区分研究探索图和经验证接纳的结果图。

## 7. 局限性与风险

- author_stated：论文指出长程研究易碎片化、无支持主张可能传播，系统以图结构应对。
- reviewer_inference：三个案例展示系统可用性，但不能量化多Agent相对于单Agent的科学增益。

## 8. 对综述写作的价值

可用于讨论以可追溯研究状态和人类参与为中心的多Agent数学发现。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Euler以共享研究图支持可追溯的人机协作数学探索。

### 9.2 速记版 pipeline

研究者指定数学目标和团队；Agent读取相关命题、依赖、先前尝试及证据后分工，提出结果经对应验证器检查并关联回研究图；共享状态支持后续会话继续、回看失败路线和探索替代分支。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1080
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
| 问题开放度 | O5 开放数学 | 数学研究案例探索事先未知的证明路径，可由形式化检验 | “三个数学研究案例” · L47 |
| 验证强度 | V1 基准/内部评测 | 案例支持系统功能，不构成统一数学能力基准 | “案例支持系统功能，不构成统一数学能力基准” · L123 |
| 系统自主性 | L2 闭环执行者 | Agent基于未解问题及依赖自主选择任务并跨会话推理 | — |

- 强验证（V3–V4）：否
- 置信度：medium；需全文复核：是；争议记录：无
- 复核状态：待专家复核：需全文复核
