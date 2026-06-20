# Unknown 2026 - SciDER: Scientific Data-centric End-to-end Researcher

## 2026-06-20 relaxed round-2 P0-D revision

- Prior note status: stale `01.04` wording based on abstract-level evidence and broad benchmark names.
- First-hand source checked: arXiv PDF `2603.01421`, especially Sections II.B, IV, and the qualitative case-study pages.
- Updated scientific_object_modules: `01;02;11`.
- object_coverage_mode: `multi_module`.
- general_method_bucket: `none`.
- primary_module_for_filing: `01`.
- Evidence: AI-Idea-Bench, MLE-Bench, AIRS-Bench, and ML research-execution evaluations support formal / computational science coverage (`01`). AstroVisBench is described and evaluated as an astronomy / astrophysics visualization and specialized API-use benchmark, supporting physics / astronomy coverage (`02`). The end-to-end case study generates a calibrated few-shot knowledge-tracing paper on ASSISTments 2009-2010, with reported educational-learning metrics and discussion, supporting social / behavioral / education-science coverage (`11`).
- Boundary note: the paper also mentions skills spanning biology, ecology, chemistry, materials, physics, social sciences, computer science, and remote sensing, and uses DiscoveryBench / SciCode. These broad labels were not counted as additional modules in this round because the SciDER paper does not expose enough task-level object inventory or result evidence for high-confidence `03`, `04`, `05`, or `06` assignments.

**论文信息**
- 标题：SciDER: Scientific Data-centric End-to-end Researcher
- 作者：Unknown
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2603.01421
- PDF / 本地文件路径：未配置本地 PDF；本 note 基于当前可得摘要级 / 元数据级证据整理。
- 论文类型：系统论文 / Agent 论文
- 当前状态：已读摘要级证据；主列表当前保持 `to_read`
- 阅读日期：2026-06-18
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 摘要 / 标题 / 方法概览 | 系统面向明确科研目标，并包含多步行动、反馈迭代或多 Agent 协作。 | 高 |
| 科学对象归类 | `01` / `01.04` | 摘要 | 最稳定对象是“data-centric end-to-end scientific researcher”，而不是单纯的模型方法或发表 venue。 | 高 |
| 方法流程 | 多步 Agent 工作流成立 | 摘要 / 系统描述 | 论文把检索、生成、分析、评估或写作等环节串成可迭代流程。 | 中高 |
| 实验验证 | 6 benchmarks 与 multimodal data/code execution | 摘要 / 结果概览 | 当前可得证据显示论文主要通过 6 benchmarks 与 multimodal data/code execution 支撑其主张。 | 中高 |
| 边界判断 | 稳定 01.04；更偏 research automation system 而非单纯 data tool | 摘要 / 任务定义 | 当前风险主要集中在边界解释与强度判断，不足以推翻现有主类。 | 中高 |

## 0. 摘要翻译

论文围绕“data-centric end-to-end scientific researcher”提出题为《SciDER: Scientific Data-centric End-to-end Researcher》的 Agent 系统，核心是把多步科研行动组织成可迭代工作流，并以 6 benchmarks 与 multimodal data/code execution 作为主要验证。当前可得证据已经足以支持其 Agent 纳入判断与对象优先归类，但仍应区分“平台泛化叙事”和“最终科学对象”之间的关系。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕科研目标执行多步工作流，并具备规划、工具调用、反馈迭代或多 Agent 协作中的至少一项。
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是或部分是
  - 反馈迭代：是
  - 自主决策：是或部分是
  - 多 Agent 协作：是或部分是
- 在科研流程中承担的明确角色：data_analysis; hypothesis_generation; tool_use_and_code_execution; workflow_orchestration; feedback_iteration

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：01
- 二级类：01.04
- 三级类：
- 四级专题：Data-centric end-to-end scientific-research agents
- 四级专题是否为新增：否
- 归类理由：按对象优先规则，本文最稳定的研究对象是“data-centric end-to-end scientific researcher”，因此当前主类保持为 `01` / `01.04`。
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：data-centric end-to-end scientific researcher
- 最终科学问题：论文试图通过 Agent 系统推进“data-centric end-to-end scientific researcher”相关研究任务。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：项目规则要求按最终研究对象而不是模型实现细节归类。

### 2.3 容易混淆的边界

- 可能误归类到：稳定 01.04；更偏 research automation system 而非单纯 data tool
- 最终判定：保持 `01` / `01.04`
- 判定理由：稳定 01.04；更偏 research automation system 而非单纯 data tool
- 是否需要二次复核：不需要。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent

### 3.2 科研流程角色

- 主要角色：data_analysis; hypothesis_generation; tool_use_and_code_execution; workflow_orchestration; feedback_iteration

### 3.3 自主能力

- 任务分解：是或部分是
- 计划生成：是
- 工具调用：是或部分是
- 记忆与状态维护：中等
- 反馈迭代：是
- 自主决策：是或部分是
- 多 Agent 协作：是或部分是
- 环境交互：中等
- 闭环实验：视论文具体验证而定

### 3.4 交叉属性标签

- 交叉属性：以计算驱动为主；若摘要明示实验或部署，再在正文中单独标注。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：希望用 Agent 化流程提升 data-centric end-to-end scientific researcher 的研究效率与质量。
- 现有科研流程或方法的痛点：传统流程往往分散、手工密集，难以在多步任务中持续反馈迭代。
- 核心假设或直觉：把检索、生成、分析、评估等环节编排成可循环的 Agent 工作流，能够提高研究推进能力。

### 4.2 系统流程

1. 输入：研究问题、数据、文献或任务上下文。
2. 任务分解 / 规划：Agent 进行子任务拆解与流程编排。
3. 工具、数据库、模型或实验平台调用：按需要调用外部资源。
4. 中间结果反馈：根据阶段性结果进行检验、批评或修正。
5. 决策或迭代：保留有效候选并推动下一轮研究动作。
6. 输出：形成更高质量的科研分析、假设、实验建议或知识生产结果。

### 4.3 系统组件

- Agent 核心：多 Agent 或单 Agent 编排系统。
- 工具 / API / 数据库：以论文摘要明示工具链为准。
- 记忆或状态模块：若论文强调长期记忆、工作流状态或证据轨迹，则作为关键组件。
- 规划器：存在或部分存在。
- 评估器 / verifier：存在，用于评分、核验或审查。
- 人类反馈或专家介入：部分论文存在。
- 实验平台或仿真环境：按 6 benchmarks 与 multimodal data/code execution 使用。

## 5. 实验与验证

### 5.1 验证方式

- 当前主要验证：6 benchmarks 与 multimodal data/code execution

### 5.2 数据、任务与指标

- 数据集 / 实验对象：围绕“data-centric end-to-end scientific researcher”的论文设定。
- 任务设置：多步科研工作流中的检索、生成、分析、评估或写作任务。
- 对比基线：以论文原文报告为准。
- 关键结果：当前可得证据表明论文主要通过 6 benchmarks 与 multimodal data/code execution 支撑其核心主张。
- 是否有消融实验：摘要级证据下不稳定，后续需全文补充。
- 是否有失败案例或负结果：摘要级证据通常不足。

### 5.3 科学贡献

- 科学贡献类型：system_platform; general_scientific_research
- 贡献强度判断：中等到较强，取决于论文是平台型还是有直接实验发现。
- 证据强度：high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：本论文强调多步 Agent 工作流，而不是单次预测模型。
- 与已有 Agent / 科研智能系统的区别：它把研究流程中的多个环节明确组织进同一套 Agent 化闭环。
- 与同一科学领域其他 Agent 文献的关系：可作为该类对象的代表样本，与同类 Agent 系统并列比较。
- 主要创新点：将对象相关研究任务稳定映射为可迭代的 Agent 工作流。

## 7. 局限性与风险

- Agent 自主性不足：部分论文仍依赖人工设定问题、工具或实验执行。
- 科学验证不足：不少记录当前仍以摘要级和 benchmark 级证据为主。
- 泛化性不足：稳定 01.04；更偏 research automation system 而非单纯 data tool
- 工具链依赖：强依赖外部工具、检索、执行环境或评价器。
- 数据泄漏或 benchmark 偏差：若以公开 benchmark 为主，则需警惕该风险。
- 成本、可复现性或安全风险：多 Agent 长流程通常带来较高成本和复现负担。

## 8. 对综述写作的价值

- 可放入哪个章节：主类 `01` / `01.04` 对应章节。
- 可支撑哪个论点：Agent 已经能够围绕“data-centric end-to-end scientific researcher”形成稳定的多步科研工作流。
- 可用于哪个表格或图：主类代表作表、边界样本表、验证方式对比表。
- 适合作为代表性案例吗：是，但代表性强弱仍受证据强度影响。
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：后续全文笔记补齐。
- 需要与哪些论文并列比较：可与同主类或相邻边界样本并列。

## 9. 总结

### 9.1 一句话概括

围绕“data-centric end-to-end scientific researcher”组织多步科研工作的 Agent 系统。

### 9.2 速记版 pipeline

1. 接收研究问题或证据。
2. 分解并编排多步科研任务。
3. 调用工具 / 数据 / 检索资源。
4. 基于反馈修正中间结果。
5. 输出更高质量的研究结论或知识生产结果。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01
二级类：01.04
三级类：
四级专题：Data-centric end-to-end scientific-research agents
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent
科研流程角色：data_analysis; hypothesis_generation; tool_use_and_code_execution; workflow_orchestration; feedback_iteration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; computational_validation
交叉属性：computation_driven
科学贡献类型：system_platform; general_scientific_research
证据强度：high_primary_abstract
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
