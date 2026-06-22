# Xian Gao 2025 - ReviewAgents: Bridging the Gap Between Human and AI-Generated Paper Reviews

**论文信息**
- 标题：ReviewAgents: Bridging the Gap Between Human and AI-Generated Paper Reviews
- 作者：Xian Gao; Jiacheng Ruan; Zongyun Zhang; Jingsheng Gao; Ting Liu; Yuzhuo Fu
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2503.08506
- PDF / 本地文件路径：未记录本地归档 PDF；当前笔记基于 arXiv 摘要页等一手来源整理。
- 论文类型：系统论文 / Agent 论文
- 当前状态：已读摘要级证据；主列表当前保持 `to_read`
- 阅读日期：2026-06-18
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 摘要 / 标题 / 方法概览 | 系统面向明确科研目标，并包含多步行动、反馈迭代或多 Agent 协作。 | 高 |
| 科学对象归类 | `11.07` | arXiv 摘要 | 研究对象是 scientific peer review 这一知识生产与评审机制本身，而不是领域无关的通用 research-agent workflow。 | 高 |
| 方法流程 | 多角色审稿工作流成立 | arXiv 摘要 | 系统按人类审稿结构组织摘要概括、相关工作参照、优缺点识别与终评生成，并由多角色、多 LLM reviewer agents 协同完成。 | 高 |
| 实验验证 | ReviewCoT + ReviewBench + human-style review evaluation | arXiv 摘要 | 论文先构建 142k review comments 的 ReviewCoT 数据集，再用 ReviewBench 评测生成审稿意见与人类审稿的差距。 | 高 |
| 边界判断 | 稳定 `11.07`，不属于 `01.04` | arXiv 摘要 / 任务定义 | 本文直接生成和评估 scientific peer review comments，处理的是 scientific knowledge production 中的评审环节，而不是通用科研平台。 | 高 |

## 0. 摘要翻译

论文提出 ReviewAgents，用 LLM reviewer agents 自动生成 scientific peer review comments。作者先构建包含 142k 审稿评论的 ReviewCoT 数据集，让模型学习人类审稿中的论文概括、相关工作参照、优缺点识别与结论生成，再搭建 multi-role、multi-LLM 的审稿框架，并用 ReviewBench 比较其输出与人类审稿之间的差距。就综述归类而言，这篇论文研究的是 scientific peer review 这一知识生产与评审过程本身，应稳定归入 `11.07`，而不是写成通用科研工作流或 `01.04` 方法论文。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕自动 scientific peer review 执行多步审稿流程，具备结构化推理、相关工作参照、反馈式审稿意见生成和多 Agent 协作等 Agent 特征。
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是或部分是
  - 反馈迭代：是
  - 自主决策：是或部分是
  - 多 Agent 协作：是或部分是
- 在科研流程中承担的明确角色：literature_search_and_reading; evidence_assessment_and_validation; result_interpretation

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
- 四级专题：Scientific peer-review agents
- 四级专题是否为新增：否
- 三级类：科学知识生产中的同行评审生成与评估
- 归类理由：按对象优先规则，本文研究的是 scientific peer review comment generation and evaluation，本质上属于 scientific knowledge production 的评审与验证环节，因此稳定归入 `11.07`。
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：scientific peer review generation and evaluation
- 最终科学问题：如何用多角色 LLM reviewer agents 生成更接近人类审稿的、具有结构化推理的 paper reviews，并系统评测其质量。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：项目规则要求按最终研究对象而不是模型实现细节归类。

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `11.07`
- 判定理由：研究对象是 scientific peer review 本身，不是无具体对象的通用科研代理平台。
- 是否需要二次复核：当前分类无需二次复核；后续如补全文只需补强证据细节。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- Agent 类型：LLM Agent; Multi-Agent System; Hybrid Agent

### 3.2 科研流程角色

- 主要角色：literature_search_and_reading; evidence_assessment_and_validation; result_interpretation

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

- 作者为什么提出该 Agent 系统：希望缩小 AI 生成审稿意见与人类审稿之间的质量差距。
- 现有科研流程或方法的痛点：现有自动审稿常给出浅层、缺少结构化推理的一般性评论，难以稳定贴近人类 reviewer judgment。
- 核心假设或直觉：如果让 reviewer agents 学习人类审稿中的结构化 reasoning，并按多角色流程组织评论生成，就能提升审稿质量。

### 4.2 系统流程

1. 输入：待审 scientific paper。
2. 任务分解 / 规划：按人类审稿结构拆成论文概括、相关工作参照、优缺点识别与结论生成等子任务。
3. 工具、数据库、模型或实验平台调用：调用经 ReviewCoT 训练的 reviewer agents，并在多角色、多 LLM 框架中协同生成评论。
4. 中间结果反馈：不同角色的审稿意见互相补充，提升评论覆盖度与推理一致性。
5. 决策或迭代：聚合各角色输出，形成更接近人类 reviewer judgment 的最终 review comments。
6. 输出：结构化 scientific peer review comments，并在 ReviewBench 上进行评测。

### 4.3 系统组件

- Agent 核心：ReviewAgents multi-role, multi-LLM reviewer framework。
- 工具 / API / 数据库：ReviewCoT dataset；relevant-paper-aware training；ReviewBench。
- 记忆或状态模块：以结构化 reviewer reasoning 为主，而不是长期实验状态记忆。
- 规划器：存在，体现在多角色审稿流程编排。
- 评估器 / verifier：ReviewBench 与 human-style review evaluation。
- 人类反馈或专家介入：以人类审稿评论作为训练与评测参照。
- 实验平台或仿真环境：scientific peer review benchmark environment。

## 5. 实验与验证

### 5.1 验证方式

- 当前主要验证：ReviewBench 与 human-style review evaluation

### 5.2 数据、任务与指标

- 数据集 / 实验对象：ReviewCoT（142k review comments）与 ReviewBench。
- 任务设置：针对 scientific paper 生成结构化 reviewer comments，并与人类审稿进行比较。
- 对比基线：以论文原文报告为准。
- 关键结果：ReviewAgents 在 ReviewBench 上缩小了 AI 审稿与人类审稿之间的差距，并优于更强的单体 LLM review generation baselines。
- 是否有消融实验：当前摘要页未细列，后续如补全文可补充。
- 是否有失败案例或负结果：摘要明确仍与 human-generated reviews 存在差距。

### 5.3 科学贡献

- 科学贡献类型：system_platform; peer_review_automation
- 贡献强度判断：中等到较强，取决于论文是平台型还是有直接实验发现。
- 证据强度：medium_metadata_with_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：本文直接研究 scientific peer review，而不是自然科学对象上的预测或发现。
- 与已有 Agent / 科研智能系统的区别：它把审稿任务拆成更接近人类 reviewer reasoning 的多角色结构，而非只生成单轮评论。
- 与同一科学领域其他 Agent 文献的关系：可与其他 `11.07` peer-review agents 一起构成 scientific knowledge production automation 子谱系。
- 主要创新点：ReviewCoT 数据集、relevant-paper-aware reviewer training，以及 multi-role review generation framework。

## 7. 局限性与风险

- Agent 自主性不足：部分论文仍依赖人工设定问题、工具或实验执行。
- 科学验证不足：当前笔记仍主要基于 arXiv 摘要页，尚未把全文页码级证据补入 note。
- 泛化性不足：当前验证集中在 benchmark 式自动审稿场景，跨学科和跨 venue 泛化仍需看全文细节。
- 工具链依赖：强依赖外部工具、检索、执行环境或评价器。
- 数据泄漏或 benchmark 偏差：若以公开 benchmark 为主，则需警惕该风险。
- 成本、可复现性或安全风险：多 Agent 长流程通常带来较高成本和复现负担。

## 8. 对综述写作的价值

- 可放入哪个章节：`11.07` 科学系统与知识生产研究中的 scientific peer review agents。
- 可支撑哪个论点：Agent 已经开始直接介入 scientific peer review 这一知识生产与评审环节，而不是只做通用科研辅助。
- 可用于哪个表格或图：主类代表作表、边界样本表、验证方式对比表。
- 适合作为代表性案例吗：是，但代表性强弱仍受证据强度影响。
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：后续全文笔记补齐。
- 需要与哪些论文并列比较：可与同主类或相邻边界样本并列。

## 9. 总结

### 9.1 一句话概括

用多角色 LLM reviewer agents 生成并评测 scientific peer review comments。

### 9.2 速记版 pipeline

1. 读入待审论文。
2. 按人类审稿结构拆解任务。
3. 多角色 reviewer agents 生成评论。
4. 聚合并评测最终 review。
5. 输出更接近人类的审稿意见。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：科学知识生产中的同行评审生成与评估
四级专题：Scientific peer-review agents
Agent 类型：LLM Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; evidence_assessment_and_validation; result_interpretation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; benchmark_driven
科学贡献类型：system_platform; peer_review_automation
证据强度：medium_metadata_with_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
