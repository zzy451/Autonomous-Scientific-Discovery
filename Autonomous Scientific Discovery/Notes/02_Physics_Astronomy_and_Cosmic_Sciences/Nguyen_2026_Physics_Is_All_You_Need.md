# Nguyen 2026 - Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software

**论文信息**
- 标题：Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
- 作者：Nhat-Minh Nguyen
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.30353
- PDF / 本地文件路径：`Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Nguyen_2026_Physics_Is_All_You_Need.pdf`
- 论文类型：研究论文 / cosmology scientific-software agent case study
- 当前状态：to_read（note 已按 Batch29Partial1 writeback 更新）
- 阅读日期：2026-06-24
- 笔记作者：Codex

## 2026-06-24 Batch29Partial1 writeback / full reaudit

- final supported_modules：`02`
- primary_module_for_filing：`02`
- object_coverage_mode：`single_module`
- final_01_04_bucket：`none`
- source_limited：`no`
- safety_access_status：`accessed_no_safety_issue`
- evidence source level：`first_hand_full_text; official_arxiv_pdf_archived_locally_and_checked`
- first-hand source checked：`official arXiv PDF checked locally: Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Nguyen_2026_Physics_Is_All_You_Need.pdf`；original source `https://arxiv.org/pdf/2605.30353.pdf`
- note_revision_required：`yes`
- adjudication confidence：`high`
- final_reason：Differentiable one-loop perturbation-theory software for galaxy clustering, validated to about 1% against CLASS-PT, is a direct class-02 physics / cosmology object.

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract | 一个 physicist 监督 AI coding agent，在 12 个工作日和 57 个 sessions 中开发科学软件模块。 | 高 |
| `02` 模块证据 | 支持 | Abstract | 目标是构建用于 galaxy clustering 预测的 differentiable one-loop perturbation theory JAX module，命名为 CLAX-PT。 | 高 |
| 验证方式 | 计算验证 + 专家监督 | Abstract | 模块对 CLASS-PT 达到约 1% 精度，并记录了 15 次 supervision events。 | 高 |
| 方法流程 | 长程多步工作流 | Abstract；正文案例叙述 | 包含 coding、oracle tests、debugging、系数修正、root-cause diagnosis 与 physicist intervention。 | 高 |
| 边界判断 | 不转 `01` 或 `01.04` | object-first reading | 尽管叙事重点是 AI scientific software development，但最终对象是具体 cosmology / galaxy clustering perturbation theory module。 | 高 |

## 0. 摘要翻译

论文以一个定量个案研究讨论 AI coding agent 在物理学家监督下开发科学软件的真实表现。作者用 12 个工作日、57 次 sessions 构建了一个用于 galaxy clustering 预测的 differentiable one-loop perturbation theory JAX 模块 CLAX-PT，并将其与既有 C 语言参考实现 CLASS-PT 对齐到约 1% 精度。文章关注 agent 在科学软件开发中的优势和失败模式，但对象层面仍然是具体宇宙学 / 物理学计算模块。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、长程多步执行、工具调用、oracle test 驱动迭代和专家监督
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 计划生成：部分是
- 工具调用：是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：否
- 在科研流程中承担的明确角色：代码实现、测试迭代、数值修正、科学软件开发与验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不适用

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`02`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`02`
- 主展示模块一级类：`02` 物理学、天文学与宇宙科学
- 主展示模块二级类：`02.02` 宇宙学 / 物理学计算模块
- 每个模块的对象实验证据：`02` 来自 galaxy clustering one-loop perturbation theory、CLAX-PT JAX module 与 CLASS-PT 对照验证
- 归类理由：文章最终服务的是具体宇宙学计算对象，而不是一般 software engineering workflow
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：galaxy clustering 的 one-loop perturbation theory 科学软件模块
- 最终科学问题：AI agent 在物理学家监督下能否可靠构建高精度的宇宙学 / 物理学计算工具
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：coding agent 只是开发方式，真正的对象是 perturbation-theory scientific software

### 2.3 容易混淆的边界

- 可能误归类到：`01` 或独立 `01.04`
- 最终判定：保持 `02`
- 判定理由：galaxy clustering、one-loop perturbation theory、CLASS-PT 对照精度这些证据都直接锚定 class-02 physics / cosmology
- 多模块覆盖说明：冻结 adjudication 不接受额外 `01` 写回
- 01.04 判定说明：并非无对象实验的通用科研 Agent，而是具体物理模块开发个案
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Human-in-the-loop Agent；Hybrid Agent
- 科研流程角色：tool_use_and_code_execution；simulation_modeling；evidence_assessment_and_validation；workflow_orchestration
- 自主能力：task_decomposition；planning；tool_use；feedback_iteration；environment_interaction

## 4. 方法设计

- 方法动机：检验 AI coding agent 在高要求物理学 scientific software 开发中的真实能力边界
- 系统流程：围绕 CLAX-PT 的模块实现、测试、调试、数值对齐与专家干预展开长程迭代
- 核心组件：AI coding agent、JAX scientific software stack、oracle test suites、CLASS-PT reference、physicist supervision

## 5. 实验与验证

- 验证方式：computational_validation；expert_evaluation
- 数据与任务：构建 differentiable one-loop perturbation theory module for galaxy clustering
- 关键结果：对既有参考实现 CLASS-PT 达到约 1% 精度；10 个 supervision events 被 agent 自主解决，剩余失败与 root-cause diagnosis 有关
- 证据强度：computationally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单点模型，而是 AI agent 参与完整 scientific software 开发
- 与同领域其他 Agent 文献的关系：可与 `CFDagent` 等 scientific-software / simulation workflow papers 对照，但对象更稳定落在宇宙学物理
- 主要创新点：把 agent 的 coding、调试与 supervision dynamics 放进具体物理学软件开发案例中量化分析

## 7. 局限性与风险

- 这是 `N=1` 的个案研究，外推性有限
- 主要产出是科学软件模块，不直接对应新的物理发现
- 文章也强调 agent 容易把 symptom reduction 误当作 root-cause resolution
- 旧 note 曾过度强调 “AI scientific software development” 外观；本次写回改为冻结 `02` 单模块表述

## 8. 对综述写作的价值

- 可放入章节：`02` 物理 / 宇宙学 Agent
- 可支撑论点：scientific software agent 只要对象稳定落在具体物理计算模块上，就不应因为 coding 外观被推回 `01.04`
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

物理学家监督下构建 galaxy clustering 扰动理论模块的 AI coding agent 个案研究。

### 9.2 速记版 pipeline

1. 设定 CLAX-PT 开发目标
2. 让 agent 编写和修改 JAX 模块
3. 用 oracle tests 与 CLASS-PT 持续比对
4. 在关键错误处引入 physicist supervision
5. 输出可验证的宇宙学计算模块

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：02
覆盖模式：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
Primary module for filing：02
是否进入 01.04 存放区：否
主展示模块一级类：02
主展示模块二级类：02.02
module_assignment_evidence：galaxy clustering one-loop perturbation theory、CLAX-PT、CLASS-PT 对照到约 1% 精度
evidence source level：first_hand_full_text; official_arxiv_pdf_archived_locally_and_checked
first_hand_source_checked：official arXiv PDF checked locally: Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Nguyen_2026_Physics_Is_All_You_Need.pdf
source_limited：no
confidence：high
```
