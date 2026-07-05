# Chang et al. 2025 - TreeReview: A Dynamic Tree of Questions Framework for Deep and Efficient LLM-based Scientific Peer Review

**论文信息**
- 标题：TreeReview: A Dynamic Tree of Questions Framework for Deep and Efficient LLM-based Scientific Peer Review
- 作者：Yuan Chang; Ziyue Li; Hengyuan Zhang; Yuanbo Kong; Yanru Wu; Hayden Kwok-Hay So; Zhijiang Guo; Liya Zhu; Ngai Wong
- 年份：2025
- 来源 / venue：arXiv / EMNLP 2025 Main
- DOI / arXiv / URL：https://arxiv.org/abs/2506.07642
- PDF / 本地文件路径：当前笔记基于 arXiv HTML
- 论文类型：研究论文 / scientific peer-review agent framework
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Phase6FollowupR20 Frozen Adjudication

- paper_id: `ASD-0655`
- final_adjudicated_modules: `11`
- primary_module_for_filing: `11`
- canonical_local_pdf: `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Chang_2025_TreeReview.pdf`
- frozen_source_state: `source_limited=no`
- first_hand_pdf_status: local archived PDF sampled in `Phase6FollowupR20`
- superseded_note_wording: any older source-limited or abstract-led phrasing is superseded by this frozen round update
- adjudication_note: preserve the stable scientific-peer-review / `11.07` reading; note location remains filing convenience only

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract / HTML | peer review 被建模为动态提问-回答-聚合流程，存在明确角色分工与 follow-up 机制 | 高 |
| 科学对象归类 | `11.07` | intro / method | 研究对象是 scientific peer review 这一科研评价活动 | 高 |
| 方法流程 | 分层树状推理 | HTML | question tree 组织 peer review，Question Generator 和 Answer Synthesizer 分工协作 | 高 |
| 评测对象 | peer review quality | HTML | 在 ICLR 与 NeurIPS 论文及人类评审上比较 full review generation 与 actionable comments | 高 |
| 边界判断 | 不应归 `01.04` | HTML | benchmark、任务、伦理讨论和评价都围绕 peer review 本身 | 高 |

## 0. 摘要翻译

论文提出 TreeReview，把 scientific peer review 建模成一个动态问题树。系统通过 Question Generator 递归提出关键审稿问题，再由 Answer Synthesizer 综合回答并生成最终 review。作者强调同行评审是 scientific research 的核心质量控制机制，并在 ICLR、NeurIPS 论文及人类评审上验证该框架能以更低 token 成本生成更全面且更接近专家的评审反馈。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在动态 follow-up、角色分工和分阶段推理，不是单轮 review generation
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：部分是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：question generation、answer synthesis、peer-review evaluation

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：scientific peer review automation
- 四级专题：dynamic review-question-tree agents
- 四级专题是否为新增：否
- 归类理由：最终对象是同行评审这一科学评价活动，而不是通用长文本 QA 平台
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：scientific peer review
- 最终科学问题：如何让 Agent 更深、更高效地完成科学论文同行评审
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：question tree 只是方法，稳定对象是 peer review 本身

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 11.07
- 判定理由：评价对象、benchmark、伦理讨论和结果都围绕 scientific peer review
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：否
- Retrieval-augmented Agent：否
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：question-tree review framework

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与知识组织：是
- 科学问题提出：部分是
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：否
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与假设验证：是
- 论文写作：部分是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：否
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：否
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：scholarly evaluation

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：直接一次性生成 review 往往浅、散且成本高
- 现有科研流程或方法的痛点：难以系统展开问题、追问子问题并综合答案
- 核心假设或直觉：若将 scientific paper review 组织成 tree-like reasoning process，可得到更深更稳的评审

### 4.2 系统流程

1. 输入：待审 scientific paper
2. 任务分解 / 规划：Question Generator 构造 review question tree
3. 工具、数据库、模型或实验平台调用：无核心外部工具，主要是递归提问和回答
4. 中间结果反馈：follow-up questions 与 intermediate answers 反馈到树结构
5. 决策或迭代：Answer Synthesizer 聚合并修订最终 review
6. 输出：完整 peer-review report 与 actionable comments

### 4.3 系统组件

- Agent 核心：Question Generator；Answer Synthesizer
- 工具 / API / 数据库：review question tree
- 记忆或状态模块：tree state 与 intermediate answers
- 规划器：hierarchical question decomposition
- 评估器 / verifier：human review alignment metrics
- 人类反馈或专家介入：人类评审作比较基准
- 实验平台或仿真环境：ICLR / NeurIPS peer-review evaluation

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：ICLR 与 NeurIPS 论文及其人类评审
- 任务设置：full review generation 与 actionable feedback generation
- 对比基线：直接 LLM review baselines
- 评价指标：review comprehensiveness、expert alignment、token efficiency
- 关键结果：生成的 review 更全面、更接近专家，同时 token 使用下降约 80%
- 是否有消融实验：当前摘要级笔记未展开
- 是否有失败案例或负结果：当前摘要级笔记未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 peer-review automation framework
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：系统平台 / peer_review_automation
- 证据强度：中高

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：对象是 scholarly evaluation，不是自然科学问题求解
- 与已有 Agent / 科研智能系统的区别：把 peer review 显式建模成树状动态 QA 过程
- 与同一科学领域其他 Agent 文献的关系：可与 APRES、Automating Scientific Evaluation、ReviewGrounder 形成 `11.07` 同群
- 主要创新点：把 scientific review 写成 dynamic tree of questions

## 7. 局限性与风险

- Agent 自主性不足：依赖 LLM 对论文内容的理解质量
- 科学验证不足：主要是 benchmark 与人类评审对照
- 泛化性不足：跨学科审稿标准差异仍需进一步验证
- 工具链依赖：主要依赖问题树设计
- 数据泄漏或 benchmark 偏差：训练数据与 benchmark 重叠风险需持续关注
- 成本、可复现性或安全风险：自动审稿的伦理与误判风险不可忽视
- 是否仍需进一步全文复核：否

## 8. 对综述写作的价值

- 可放入哪个章节：scientific peer review agents
- 可支撑哪个论点：如果系统研究的是 scholarly evaluation itself，应归 `11.07`
- 可用于哪个表格或图：peer-review agents 对照表
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：question tree 架构图与效率对比
- 需要与哪些论文并列比较：ASD-0652、ASD-0855

## 9. 总结

### 9.1 一句话概括

把科学同行评审组织成动态问题树 Agent 流程。

### 9.2 速记版 pipeline

1. 生成审稿主问题
2. 递归展开 follow-up questions
3. 聚合局部回答
4. 生成最终 review

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：scientific peer review automation
四级专题：dynamic review-question-tree agents
Agent 类型：LLM Agent; Planning Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; data_analysis; result_interpretation; evidence_assessment_and_validation; paper_writing; end_to_end_research_automation
自主能力：task_decomposition; planning; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
