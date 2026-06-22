# Haishuo Fang 2026 - From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent

**论文信息**
- 标题：From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent
- 作者：Haishuo Fang; Yue Feng; Iryna Gurevych
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2606.13349
- PDF / 本地文件路径：未记录本地归档 PDF；当前笔记基于 arXiv 摘要页与论文首页一手来源整理。
- 论文类型：系统论文 / Agent 论文
- 当前状态：已读摘要级证据；主列表当前保持 `to_read`
- 阅读日期：2026-06-18
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 摘要 / 标题 / 方法概览 | 系统面向明确科研目标，并包含多步行动、反馈迭代或多 Agent 协作。 | 高 |
| 科学对象归类 | `11.07` | arXiv 摘要 / 引言 | 研究对象是 scientific peer review 这一知识生产与质量控制机制本身，而不是通用 research-agent workflow。 | 高 |
| 方法流程 | 主动调查式审稿流程成立 | arXiv 摘要 / 引言 | Agent 维护 structured review log，围绕 claims、questions 和 notes 主动导航论文、核对证据并生成最终审稿意见。 | 高 |
| 实验验证 | 五维质量评测 + human evaluation | arXiv 摘要 / 结果 | ProReviewer 在五个质量维度上的平均分最高，并在人工对比中取得最高 win rate。 | 高 |
| 边界判断 | 稳定 `11.07`，不属于 `01.04` | arXiv 摘要 / 引言 | 本文研究的是 scientific peer review 过程本身，且核心贡献是 evidence-grounded review generation，不是通用科研平台。 | 高 |

## 0. 摘要翻译

论文提出 ProReviewer，把 automated scientific peer review 从被动生成评论推进到主动调查证据。作者将审稿过程形式化为 MDP，并让 agent 维护一个 structured review log，用于持续记录 claims、questions 和 notes，再据此决定下一步检查论文的哪个部分、是否回看前文以及如何形成最终 critique。实验表明，ProReviewer 在五个质量维度上的平均分最高，相对 prompt-based frontier LLMs 最多提升 39%，并在 human evaluation 中取得最高 win rate。就综述归类而言，本文处理的是 scientific peer review 这一知识生产与评审机制本身，应稳定归入 `11.07`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕自动 scientific peer review 执行多步主动调查流程，具备规划、证据记录、反馈迭代和可学习决策策略等 Agent 特征。
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是或部分是
  - 反馈迭代：是
  - 自主决策：是或部分是
  - 多 Agent 协作：是或部分是
- 在科研流程中承担的明确角色：evidence_assessment_and_validation; literature_search_and_reading; feedback_iteration; result_interpretation

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：
- 四级专题：Proactive scientific peer-review agents
- 四级专题是否为新增：否
- 三级类：科学知识生产中的调查式同行评审
- 归类理由：按对象优先规则，本文研究的是 scientific peer review 中的主动证据调查与审稿生成，本质上属于 scientific knowledge production 的评审与验证环节，因此稳定归入 `11.07`。
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：investigative scientific peer review
- 最终科学问题：如何让 review agent 像人类 reviewer 一样主动核查论文中的可疑 claim，并据累积证据生成更扎实的 critique。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：项目规则要求按最终研究对象而不是模型实现细节归类。

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `11.07`
- 判定理由：研究对象就是 scientific peer review 行为本身，而不是无具体对象的通用 research-agent platform。
- 是否需要二次复核：当前分类无需二次复核；后续如补全文只需补强页码证据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- Agent 类型：LLM Agent; Planning Agent; Hybrid Agent

### 3.2 科研流程角色

- 主要角色：evidence_assessment_and_validation; literature_search_and_reading; feedback_iteration; result_interpretation

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

- 交叉属性：以 computation_driven 和 benchmark 驱动为主。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：希望让自动审稿从被动生成一般性评论，转向主动调查论文中的可疑 claim 与证据链。
- 现有科研流程或方法的痛点：已有自动审稿往往评论浅、缺少证据支撑，也难以跨 section 发现 claim 与 results 的不一致。
- 核心假设或直觉：如果让 agent 维护 structured review log，并学习何时检查、回看和更新证据，就能得到更像人类 reviewer 的审稿行为。

### 4.2 系统流程

1. 输入：待审 scientific paper。
2. 任务分解 / 规划：agent 根据论文目录和当前证据决定下一步检查哪个 section、提取什么 claim、提出什么 question。
3. 工具、数据库、模型或实验平台调用：在论文内部导航，并维护 structured review log 记录 claims、questions 和 notes。
4. 中间结果反馈：新读取内容会用于核对早先 claim、解决未决问题，或记录新的 inconsistency。
5. 决策或迭代：通过 MDP policy 决定是否继续追查、回看前文或开始撰写最终 review。
6. 输出：evidence-grounded scientific peer review comments。

### 4.3 系统组件

- Agent 核心：ProReviewer review agent。
- 工具 / API / 数据库：structured review log；paper index / section navigation；训练阶段的 version-matched ICLR review corpus。
- 记忆或状态模块：structured review log，是本文最关键的状态设计。
- 规划器：存在，以 MDP policy 决定下一步 investigation action。
- 评估器 / verifier：五维质量评测与 human evaluation。
- 人类反馈或专家介入：human evaluation 用于比较不同系统生成的 reviews。
- 实验平台或仿真环境：scientific peer review benchmark environment。

## 5. 实验与验证

### 5.1 验证方式

- 当前主要验证：五维质量评测与 human evaluation

### 5.2 数据、任务与指标

- 数据集 / 实验对象：version-matched 5K ICLR 2025/2026 paper-review pairs；其中 4K 用于训练，1K ICLR 2026 论文用于测试。
- 任务设置：在 scientific paper 审稿中主动调查可疑 claim，维护 review log，并生成 evidence-grounded review。
- 对比基线：以论文原文报告为准。
- 关键结果：ProReviewer 在五个质量维度上的平均分最高；相对 prompt-based frontier LLMs 最多提升 39%，相对最强 fine-tuned baseline 提升 16%，且 human evaluation win rate 最高。
- 是否有消融实验：当前摘要页未细列，后续如补全文可补充。
- 是否有失败案例或负结果：摘要未系统展开，但明确把主动调查视为对既有浅层自动审稿方法的改进。

### 5.3 科学贡献

- 科学贡献类型：system_platform; peer_review_automation
- 贡献强度判断：中等到较强，取决于论文是平台型还是有直接实验发现。
- 证据强度：medium_metadata_with_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：本文直接研究 scientific peer review，而不是自然科学对象上的发现或预测。
- 与已有 Agent / 科研智能系统的区别：它把自动审稿从固定 pipeline 推进到可学习的主动调查策略，并强调 evidence-grounded critique。
- 与同一科学领域其他 Agent 文献的关系：可作为 `11.07` peer-review agents 中偏 investigation / evidence-tracking 的代表样本。
- 主要创新点：peer review 的 MDP 形式化、structured review log，以及 RL 优化的主动调查式审稿。

## 7. 局限性与风险

- Agent 自主性不足：部分论文仍依赖人工设定问题、工具或实验执行。
- 科学验证不足：当前笔记仍主要基于 arXiv 摘要页与首页，尚未把全文页码级证据完整补入 note。
- 泛化性不足：当前评测集中在 ICLR review 场景，跨 venue 和跨学科泛化仍需看全文细节。
- 工具链依赖：强依赖外部工具、检索、执行环境或评价器。
- 数据泄漏或 benchmark 偏差：若以公开 benchmark 为主，则需警惕该风险。
- 成本、可复现性或安全风险：多 Agent 长流程通常带来较高成本和复现负担。

## 8. 对综述写作的价值

- 可放入哪个章节：`11.07` 科学系统与知识生产研究中的 investigative peer-review agents。
- 可支撑哪个论点：Agent 已经能够直接介入 scientific peer review 的证据核查与 critique 生成，而不只是产出一般性评论。
- 可用于哪个表格或图：主类代表作表、边界样本表、验证方式对比表。
- 适合作为代表性案例吗：是，但代表性强弱仍受证据强度影响。
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：后续全文笔记补齐。
- 需要与哪些论文并列比较：可与同主类或相邻边界样本并列。

## 9. 总结

### 9.1 一句话概括

把自动审稿推进到主动调查证据的 scientific peer-review agent。

### 9.2 速记版 pipeline

1. 读入待审论文。
2. 维护 review log 并追踪 claims。
3. 主动导航 section 核查证据。
4. 迭代更新 questions / notes。
5. 生成有证据支撑的 review。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：科学知识生产中的调查式同行评审
四级专题：Proactive scientific peer-review agents
Agent 类型：LLM Agent; Planning Agent; Hybrid Agent
科研流程角色：evidence_assessment_and_validation; literature_search_and_reading; feedback_iteration; result_interpretation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; benchmark_driven
科学贡献类型：system_platform; peer_review_automation
证据强度：medium_metadata_with_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
