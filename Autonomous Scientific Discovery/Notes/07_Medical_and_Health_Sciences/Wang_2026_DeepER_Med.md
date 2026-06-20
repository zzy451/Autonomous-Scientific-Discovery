# Wang et al. 2026 - DeepER-Med: Advancing Deep Evidence-Based Research in Medicine Through Agentic AI

**论文信息**
- 标题：DeepER-Med: Advancing Deep Evidence-Based Research in Medicine Through Agentic AI
- 作者：Zhizheng Wang; Chih-Hsuan Wei; Joey Chan; Robert Leaman; Chi-Ping Day; Chuan Wu; Mark A Knepper; Antolin Serrano Farias; Jordina Rincon-Torroella; Hasan Slika; Betty Tyler; Ryan Huu-Tuan Nguyen; Asmita Indurkar; Mélanie Hébert; Shubo Tian; Lauren He; Noor Naffakh; Aseem Aseem; Nicholas Wan; Emily Y Chew; Tiarnan D L Keenan; Zhiyong Lu
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.15456
- PDF / 本地文件路径：当前笔记基于 arXiv abstract / arXiv API 元数据；尚未完成全文核对
- 论文类型：系统论文 / medical-research agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract | frames deep medical research as an explicit workflow of planning, agentic collaboration, and evidence synthesis | 高 |
| 科学对象归类 | `07` 顶层稳定 | Title; Abstract | 对象是 medicine-centered research、medical questions、clinical cases，而非通用科研平台 | 高 |
| 多步行动流程 | 明确存在 | Abstract | three modules: research planning, agentic collaboration, evidence synthesis | 高 |
| 证据与评估 | expert-level medical scenarios | Abstract | DeepER-MedQA contains 100 expert-level questions from authentic medical research scenarios | 高 |
| 真实场景支持 | 有临床案例 | Abstract | demonstrates practical utility through eight real-world clinical cases, with clinician assessment | 高 |
| 边界判断 | 不应移入 `01.04` | Abstract | 虽然有 deep-research 平台外观，但最终对象与评测都落在医学研究和临床证据支持上 | 高 |

## 0. 摘要翻译

可信性和透明性是 AI 在医疗和生物医学研究中被临床采用的关键。近期的 deep research systems 试图通过把 AI agents 与多跳信息检索、推理和综合结合起来，加速 evidence-grounded scientific discovery，但多数系统缺乏显式可审计的证据评价标准。本文提出 DeepER-Med，一个面向医学的 Deep Evidence-based Research framework。系统把深度医学研究写成一个显式、可检查的 evidence-based generation workflow，由 research planning、agentic collaboration 和 evidence synthesis 三个模块构成。作者还构建了 DeepER-MedQA 数据集，并展示系统在专家级医学研究问题和真实临床案例上的表现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕明确医学研究目标执行多步流程，并包含规划、协作、证据综合与案例支持
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：部分是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：文献检索与阅读、证据评估与验证、结果解释、工作流编排

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：evidence-based medical research agents
- 四级专题：Deep medical research and evidence-synthesis agents
- 四级专题是否为新增：否
- 归类理由：对象是医学研究问题、医学证据综合与临床案例支持，顶层稳定落在医学与健康科学
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：医学研究问题、临床证据与医学研究场景
- 最终科学问题：如何通过 agentic AI 提升 evidence-based medical research 的深度与可靠性
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：deep-research workflow 是手段，最终对象是医学研究本身

### 2.3 容易混淆的边界

- 可能误归类到：01.04；07.03
- 最终判定：顶层保持 07，当前暂保留 07.04
- 判定理由：医学对象已很明确，但二级位点仍有 evidence-based medicine / health research 支持型边界压力
- 是否需要二次复核：需要，主要是二级位点和平台性强度

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：部分是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：Deep evidence-based medical research system

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：部分是
- 实验执行：否
- 数据分析：部分是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：部分是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：部分是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：部分是
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
- 其他：clinical decision-support scenarios

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：现有 deep medical research systems 缺乏显式、可检查的证据评价标准
- 现有科研流程或方法的痛点：复杂医学问题需要更可信、更可审计的 evidence synthesis
- 核心假设或直觉：把 research planning、agentic collaboration、evidence synthesis 写成可检查 workflow，可提升医学研究支持质量

### 4.2 系统流程

1. 输入：医学研究问题或病例问题
2. 任务分解 / 规划：research planning
3. 工具、数据库、模型或实验平台调用：多代理协作检索与整理医学证据
4. 中间结果反馈：证据权重与综合过程可检查
5. 决策或迭代：根据证据综合更新研究结论或支持输出
6. 输出：医学研究结论、临床建议支持或证据综合报告

### 4.3 系统组件

- Agent 核心：planning + collaboration + evidence synthesis modules
- 工具 / API / 数据库：医学研究文献与 DeepER-MedQA 场景
- 记忆或状态模块：工作流状态
- 规划器：有
- 评估器 / verifier：expert manual evaluation; clinician assessment
- 人类反馈或专家介入：有
- 实验平台或仿真环境：医学研究与临床案例环境

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：部分是
- 真实场景部署：部分是
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：DeepER-MedQA；8 个真实临床案例
- 任务设置：expert-level medical research questions
- 对比基线：widely used production-grade platforms
- 评价指标：专家手工评估、多项标准、clinician alignment
- 关键结果：在多个标准上优于 baseline；7/8 clinical cases 与临床建议一致
- 是否有消融实验：当前笔记未确认
- 是否有失败案例或负结果：有 1 个 clinical mismatch case

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：作者声称包括 generation of novel scientific insights，但当前仍偏研究支持系统
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：explanation / system_platform / evidence_assessment
- 证据强度：专家评估 + 临床案例支持

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是一般医学问答，而是显式 evidence-based medical research workflow
- 与已有 Agent / 科研智能系统的区别：强调 inspectable evidence appraisal
- 与同一科学领域其他 Agent 文献的关系：可与 healthcare research agents、clinical reasoning agents 并列
- 主要创新点：在医学研究里把 planning、agentic collaboration 和 evidence synthesis 写成可审计工作流

## 7. 局限性与风险

- Agent 自主性不足：仍主要是研究支持与临床建议支持
- 科学验证不足：是否足以支撑更强 confirmed-core 代表性仍需全文判断
- 泛化性不足：二级类位点仍有 07.03 / 07.04 边界张力
- 工具链依赖：依赖医学文献和专家评估场景
- 数据泄漏或 benchmark 偏差：需全文补核
- 成本、可复现性或安全风险：医学高风险语境下需更谨慎审计

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学中的 evidence-based medical research agents
- 可支撑哪个论点：医学对象足够明确的 workflow Agent 不应被一概归为 01.04
- 可用于哪个表格或图：07 / 01.04 边界表；医学 Agent 证据强度表
- 适合作为代表性案例吗：适合
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：Abstract 中的 module 描述与 clinical cases 结果
- 需要与哪些论文并列比较：HealthFlow、medical reasoning agents

## 9. 总结

### 9.1 一句话概括

面向医学研究证据综合的深度 Agent 工作流。

### 9.2 速记版 pipeline

1. 输入医学研究问题
2. 规划研究任务
3. 多代理协作检索证据
4. 综合并评估证据
5. 输出医学研究支持结论

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：evidence-based medical research agents
四级专题：Deep medical research and evidence-synthesis agents
Agent 类型：LLM Agent; Multi-Agent System; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; result_interpretation; evidence_assessment_and_validation; workflow_orchestration
自主能力：task_decomposition; planning; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：explanation; system_platform; evidence_assessment
证据强度：expert_confirmed
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
