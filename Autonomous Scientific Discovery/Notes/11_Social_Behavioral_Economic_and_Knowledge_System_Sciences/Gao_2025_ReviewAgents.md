# Gao et al. 2025 - ReviewAgents: Bridging the Gap Between Human and AI-Generated Paper Reviews

**论文信息**
- 标题：ReviewAgents: Bridging the Gap Between Human and AI-Generated Paper Reviews
- 作者：Xian Gao; Jiacheng Ruan; Zongyun Zhang; Jingsheng Gao; Ting Liu; Yuzhuo Fu
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2503.08506
- PDF / 本地文件路径：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Gao_2025_ReviewAgents.pdf`
- 论文类型：系统论文 / scientific peer-review agent paper
- 当前状态：`to_read`
- 阅读日期：2026-07-05
- 笔记作者：Codex

## Phase6FollowupR21 Frozen Adjudication

- Frozen paper id: `ASD-0625`
- Final adjudicated modules: `11`
- `general_method_bucket`: `none`
- Primary module for filing: `11`
- Filing note: 当前目录位置仅用于归档便利，不构成分类依据。
- First-hand source state: 本轮已按本地归档 PDF `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Gao_2025_ReviewAgents.pdf` 进行一手来源确认，不再保留“仅摘要级 / 无本地 PDF”表述。
- Frozen judgment: 该文稳定归入 `11`，对象是 scientific peer review 这一 scientific knowledge production 环节本身；可在展示时放入 `11.07` 语境，但模块事实保持 `11`。

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 本地归档 PDF | 系统围绕自动 scientific peer review 执行多步审稿工作流 | 高 |
| 科学对象归类 | `11` | 本地归档 PDF | 对象是 scientific peer review 与 knowledge production 中的评审机制 | 高 |
| 方法流程 | 多角色审稿工作流成立 | 本地归档 PDF | 系统组织摘要概括、相关工作参照、优缺点识别与终评生成，并由多角色 reviewer agents 协同完成 | 高 |
| 实验验证 | ReviewCoT + ReviewBench + human-style review evaluation | 本地归档 PDF | 论文构建 review comments 数据集并评测 AI review 与人类审稿差距 | 高 |
| 边界判断 | 稳定 `11`，不属于 `01.04` | 本地归档 PDF；对象优先规则 | 处理的是 scientific knowledge production 中的评审环节，而非通用科研平台 | 高 |
| 本地 PDF 状态 | 已确认 | 本地归档路径 | R21 冻结写回包已确认本地归档 PDF | 高 |

## 0. 摘要翻译

本文提出 ReviewAgents，用多角色 LLM reviewer agents 自动生成 scientific peer review comments。作者首先构建包含大规模审稿评论的 ReviewCoT 数据集，让模型学习人类审稿中的摘要概括、相关工作对照、优缺点识别与结论生成，再搭建 multi-role、multi-LLM 的审稿框架，并用 ReviewBench 比较其输出与人类审稿之间的差距。就综述归类而言，该文研究的是 scientific peer review 这一知识生产与评审过程本身，应稳定归入 `11`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕自动 scientific peer review 执行多步审稿流程，具备结构化推理、反馈审稿意见生成和多 Agent 协作等特征
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：计划生成、工具调用、反馈迭代、自主决策、多 Agent 协作
- 在科研流程中承担的明确角色：literature_search_and_reading; evidence_assessment_and_validation; result_interpretation

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 当前排除结论：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`11`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`11`
- Primary module for filing 说明：仅用于归档和展示，不覆盖对象模块事实
- 主展示模块一级类：`11` 社会、行为、经济与知识系统科学
- 主展示语境：`11.07` scientific knowledge production / peer review
- 其他覆盖模块及对应层级路径：无
- 每个模块的对象实验证据：scientific peer review comment generation、review benchmark 与 human-style evaluation 均围绕 scientific knowledge production 的评审环节
- 归类理由：研究对象是 scientific peer review generation and evaluation，本质上属于科学知识生产系统
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：scientific peer review generation and evaluation
- 最终科学问题：如何用多角色 LLM reviewer agents 生成更接近人类审稿的 paper reviews，并系统评测其质量
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：项目规则要求按最终研究对象而非模型实现细节归类

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `11`
- 判定理由：研究对象是 scientific peer review 本身，不是无具体对象的通用 research-agent workflow
- 01.04 判定说明：已有明确知识生产对象、任务与结果，因此 `general_method_bucket=none`
- 是否需要二次复核：当前分类无需二次复核

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent; Multi-Agent System; Hybrid Agent
- 科研流程角色：literature_search_and_reading; evidence_assessment_and_validation; result_interpretation
- 自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
- 交叉属性：computation_driven; benchmark_driven

## 4. 方法设计

### 4.1 方法动机

- 作者希望缩小 AI 生成审稿意见与人类审稿之间的质量差距
- 现有自动审稿常给出浅层、缺少结构化推理的一般性评论

### 4.2 系统流程

1. 读入待审 scientific paper。
2. 按人类审稿结构拆解摘要概括、相关工作参照、优缺点识别与终评生成等任务。
3. 调用 reviewer agents 协同生成评论。
4. 聚合多角色输出。
5. 输出更接近人类审稿的 structured review comments。

## 5. 实验与验证

- 验证方式：benchmark; expert_evaluation
- 数据 / 对象：ReviewCoT；ReviewBench
- 任务设置：针对 scientific paper 生成结构化 reviewer comments，并与人类审稿比较
- 关键结果：ReviewAgents 在 benchmark 上缩小了 AI 审稿与人类审稿之间的差距
- 证据强度判断：当前已是本地 PDF 支撑下的对象分类证据，不再是 abstract-only state

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：本文直接研究 scientific peer review，而不是自然科学对象上的预测或发现
- 与已有 Agent / 科研智能系统的区别：它把审稿任务拆成更接近人类 reviewer reasoning 的多角色结构
- 与同一科学领域其他 Agent 文献的关系：可与其他 `11` 下的 peer-review agents 一起构成 scientific knowledge production automation 子轨
- 主要创新点：ReviewCoT 数据集、relevant-paper-aware reviewer training、multi-role review generation framework

## 7. 局限性与风险

- 当前验证仍以 benchmark 化审稿场景为主，跨学科与跨 venue 泛化仍需细看全文细节
- 若做正文精细引文，后续仍可补页码级摘录
- 当前主要风险是系统强度和外推性展开，而不是 `11` 分类风险

## 8. 对综述写作的价值

- 可放入章节：`11` 社会、行为、经济与知识系统科学中的 scientific peer-review agents
- 可支撑论点：Agent 已经直接进入 scientific peer review 这一知识生产与评审环节，而不只是通用科研辅助
- 可用于表格或图：主类代表作表、边界样本表、验证方式对比表
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

用多角色 reviewer agents 生成并评测 scientific peer review comments。

### 9.2 速记版 pipeline

1. 读入待审论文。
2. 按人类审稿结构拆解任务。
3. 多角色 reviewer agents 生成评论。
4. 聚合并评测最终 review。
5. 输出更接近人类的审稿意见。

### 9.3 标注字段汇总

```text
paper_id: ASD-0625
scientific_object_modules: 11
object_coverage_mode: single_module
primary_module_for_filing: 11
general_method_bucket: none
classification_confidence: high
source_limited: no
safety_access_status: none
first_hand_sources_checked: local archived PDF (`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Gao_2025_ReviewAgents.pdf`); official arXiv record (`https://arxiv.org/abs/2503.08506`)
pdf_archive_status: local archived PDF confirmed
canonical_local_pdf_path: Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Gao_2025_ReviewAgents.pdf
official_pdf_url: https://arxiv.org/pdf/2503.08506
```
