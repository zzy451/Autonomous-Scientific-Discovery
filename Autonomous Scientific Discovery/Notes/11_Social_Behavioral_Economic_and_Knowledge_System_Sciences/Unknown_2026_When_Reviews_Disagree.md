# Kumar et al. 2026 - When Reviews Disagree: Fine-Grained Contradiction Analysis in Scientific Peer Reviews

**论文信息**
- 标题：When Reviews Disagree: Fine-Grained Contradiction Analysis in Scientific Peer Reviews
- 作者：Sandeep Kumar; Yash Kamdar; Abid Hossain; Bharti Kumari; Tanik Saikh; Asif Ekbal
- 年份：2026
- 来源 / venue：ACL 2026 / arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.10171
- paper_id：ASD-0768
- 科学对象模块（本轮裁定）：`11`
- Primary module for filing：`11`
- PDF / 本地文件路径：未配置本地 PDF；本轮按 source-limited 写回，仅核对 arXiv 摘要页与现有 note 内容，不补写本地 archive 路径。
- 论文类型：系统论文 / Agent 论文
- 当前状态：已读摘要级一手来源 / 已纳入；source-limited hold preserved
- 阅读日期：2026-06-23
- 本轮写回口径：`modules=11`；`primary=11`；`confidence=high`；`source_limited=yes`；`safety_access_status=none`
- 笔记作者：Codex

## Phase6NoteRevisionR26 source-limited harmonization override - 2026-07-05

- Final classification: `scientific_object_modules=11`; `object_coverage_mode=single_module`; `primary_module_for_filing=11`; `general_method_bucket=none`.
- Source status: authoritative state remains `source_limited=yes`; the current first-hand evidence is the arXiv abstract page only, and no local PDF/archive path is confirmed.
- Override note: preserve the conservative source-limited wording for this note. Do not read this record as local-PDF-backed or first-hand full-text-checked.

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| 一手来源核对 | 已核对 arXiv 摘要页 | arXiv abs page | 已刷新作者元数据，并核对 RevCI、IMPACT、TIDE 与 contradiction-intensity 相关摘要信息。 | 高 |
| PDF / archive 状态 | source-limited；无本地 archive 路径 | 当前 note + arXiv abs page | 本轮未同步本地 PDF 归档，也不补写不存在的 archive 路径。 | 高 |
| Agent 纳入 | 是 | 标题 + 摘要 | 该工作用多步 agent 流程完成 contradiction evidence extraction、deliberation、adjudication 与 intensity scoring。 | 高 |
| 科学对象归类 | `11`，按知识生产子域记作 `11.07` | 摘要 | 研究对象是 scientific peer review disagreement 与 contradiction analysis，而不是通用 research-agent substrate。 | 高 |
| 任务 / 对象覆盖 | contradiction evidence spans、graded disagreement intensity、scientific review adjudication | 摘要 | 任务全部围绕 scientific knowledge production 中的同行评审分歧解析展开。 | 高 |
| 验证总结 | RevCI + IMPACT + TIDE | 摘要 | 结果主张建立在 peer-review contradiction evidence identification 与 intensity agreement 上。 | 中高 |
| 边界判断 | 不进 `01.04`；稳定落在 `11.07` 口径 | 摘要 + 项目规则 | 虽含 structured multi-agent framework 与 deployment distillation，但对象始终是 scientific review disagreement 本身。 | 高 |

## 0. 摘要翻译

论文围绕“contradiction analysis in scientific peer reviews”提出题为《When Reviews Disagree: Fine-Grained Contradiction Analysis in Scientific Peer Reviews》的 Agent 系统，核心是把多步科研行动组织成可迭代工作流，并以 RevCI dataset、IMPACT multi-agent framework 与 deployment-oriented distillation 作为主要验证。当前可得证据已经足以支持其 Agent 纳入判断与对象优先归类，但仍应区分“平台泛化叙事”和“最终科学对象”之间的关系。

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
- 在科研流程中承担的明确角色：evidence_assessment_and_validation; result_interpretation; workflow_orchestration; feedback_iteration

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 科学对象模块：`11`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是；但对象是 scientific peer review disagreement / scientific knowledge production，而非自然科学对象
- 独立 `01.04` 存放区：none
- Primary module for filing：`11`
- Primary module for filing 说明：仅用于当前 note 落盘与展示，不覆盖对象优先的分类事实
- 主展示模块一级类：11
- 主展示模块二级类：11.07 科学系统与知识生产研究
- 主展示模块三级类：scientific peer review contradiction analysis
- 主展示模块四级专题：Contradiction-analysis agents for scientific peer reviews
- 其他覆盖模块及对应层级路径：无
- 每个模块的对象实验证据：RevCI、IMPACT、TIDE 与 contradiction-intensity evaluation 都直接围绕 scientific peer reviews 展开
- 归类理由：按对象优先规则，本文研究的是 scientific peer review 中的冲突证据提取、分歧强度判定与审稿解释，因此应稳定记入 `11`，并按当前项目口径落在 `11.07`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：contradiction analysis in scientific peer reviews
- 最终科学问题：论文试图通过 Agent 系统推进“contradiction analysis in scientific peer reviews”相关研究任务。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：项目规则要求按最终研究对象而不是模型实现细节归类。

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `11`；按知识生产子域写作时使用 `11.07` 口径
- 判定理由：本文虽然提供 structured multi-agent framework、small-model distillation 与 benchmark 叙事，但 benchmark 与输出都在分析 scientific peer review disagreement，本质上是知识生产系统研究，不是无对象通用科研 Agent
- 多模块覆盖说明：无；当前冻结模块仅为 `11`
- 01.04 判定说明：不进入 `01.04`，因为本文直接研究和解释 scientific knowledge production itself
- 是否需要二次复核：否；本轮主要风险是全文未归档带来的 source-limited 风险，而非分类漂移

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent

### 3.2 科研流程角色

- 主要角色：evidence_assessment_and_validation; result_interpretation; workflow_orchestration; feedback_iteration

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

- 作者为什么提出该 Agent 系统：希望用 Agent 化流程提升 contradiction analysis in scientific peer reviews 的研究效率与质量。
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
- 实验平台或仿真环境：按 RevCI dataset、IMPACT multi-agent framework 与 deployment-oriented distillation 使用。

## 5. 实验与验证

### 5.1 验证方式

- 当前主要验证：RevCI dataset、IMPACT multi-agent framework 与 deployment-oriented distillation

### 5.2 数据、任务与指标

- 数据集 / 实验对象：围绕“contradiction analysis in scientific peer reviews”的论文设定。
- 任务设置：多步科研工作流中的检索、生成、分析、评估或写作任务。
- 对比基线：以论文原文报告为准。
- 关键结果：当前可得证据表明论文主要通过 RevCI dataset、IMPACT multi-agent framework 与 deployment-oriented distillation 支撑其核心主张。
- 是否有消融实验：摘要级证据下不稳定，后续需全文补充。
- 是否有失败案例或负结果：摘要级证据通常不足。

### 5.3 科学贡献

- 科学贡献类型：system_platform; peer_review_automation
- 贡献强度判断：中等；核心价值在于把 reviewer contradiction analysis 组织成 evidence-level、多步 adjudication Agent 流程，而不是产生新的自然科学对象发现。
- 证据强度：source-limited，但摘要页已能支撑高置信度的 `11` / `11.07` 归类
- 本轮验证总结：当前足以确认其对象是 scientific peer review contradiction analysis；不足之处主要是尚未归档本地 PDF、暂缺更细粒度实验页码摘录

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：本论文强调多步 Agent 工作流，而不是单次预测模型。
- 与已有 Agent / 科研智能系统的区别：它把研究流程中的多个环节明确组织进同一套 Agent 化闭环。
- 与同一科学领域其他 Agent 文献的关系：可作为该类对象的代表样本，与同类 Agent 系统并列比较。
- 主要创新点：将对象相关研究任务稳定映射为可迭代的 Agent 工作流。

## 7. 局限性与风险

- Agent 自主性不足：部分论文仍依赖人工设定问题、工具或实验执行。
- 科学验证不足：不少记录当前仍以摘要级和 benchmark 级证据为主。
- 泛化性不足：11.07 内部 NLP-task 化样本；对象仍是 scientific review disagreement 本身
- 工具链依赖：强依赖外部工具、检索、执行环境或评价器。
- 数据泄漏或 benchmark 偏差：若以公开 benchmark 为主，则需警惕该风险。
- 成本、可复现性或安全风险：多 Agent 长流程通常带来较高成本和复现负担。

## 8. 对综述写作的价值

- 可放入哪个章节：主类 `11` / `11.07` 对应章节。
- 可支撑哪个论点：Agent 已经能够围绕“contradiction analysis in scientific peer reviews”形成稳定的多步科研工作流。
- 可用于哪个表格或图：主类代表作表、边界样本表、验证方式对比表。
- 适合作为代表性案例吗：是，但代表性强弱仍受证据强度影响。
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：后续全文笔记补齐。
- 需要与哪些论文并列比较：可与同主类或相邻边界样本并列。

## 9. 总结

### 9.1 一句话概括

面向 scientific peer review disagreement 解析的 `11.07` 多 Agent 系统。

### 9.2 速记版 pipeline

1. 接收研究问题或证据。
2. 分解并编排多步科研任务。
3. 调用工具 / 数据 / 检索资源。
4. 基于反馈修正中间结果。
5. 输出更高质量的研究结论或知识生产结果。

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：11
覆盖模式：single_module
是否具有具体科学对象实验：是，但对象是 scientific peer review disagreement / scientific knowledge production
general_method_bucket：none
Primary module for filing：11
是否进入 01.04 存放区：否
主展示模块一级类：11
主展示模块二级类：11.07
主展示模块三级类：scientific peer review contradiction analysis
主展示模块四级专题：Contradiction-analysis agents for scientific peer reviews
其他覆盖模块及对应层级路径：无
module_assignment_evidence：RevCI、IMPACT、TIDE、contradiction-intensity evaluation
multi_module_object_coverage_note：单模块；冻结 landed 结果为 11
first_hand_sources_checked：arXiv abs page
classification_evidence_source_level：source_limited
PDF/archive_status：no_local_archive_path
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent
科研流程角色：evidence_assessment_and_validation; result_interpretation; workflow_orchestration; feedback_iteration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven
科学贡献类型：system_platform; peer_review_automation
证据强度：source_limited
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
