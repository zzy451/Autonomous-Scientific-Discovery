# Ngo and Rahgozar 2026 - Causal-Enhanced AI Agents for Medical Research Screening

**论文信息**
- 标题：Causal-Enhanced AI Agents for Medical Research Screening
- 作者：Duc Ngo; Arya Rahgozar
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2601.02814
- PDF / 本地文件路径：已核对 arXiv PDF 全文
- 论文类型：研究论文 / medical evidence-screening agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | PDF p1 abstract | 系统执行摘要筛选、检索、因果分析与回答生成的多步流程 | 高 |
| 多步工作流 | 是 | PDF p3 Sec. 3.1; p4 Sec. 3.3 | 双 classifier 做 PICOS 判定，CEAI agent 再做 evidence retrieval 与 reasoning | 高 |
| 工具调用 | 是 | PDF p4 Sec. 3.3 | lightRAG、Think tool、knowledge graph 与 causal reasoning 被显式调用 | 高 |
| 科学对象归类 | `07.03` | PDF p5-p6 | 对象是 dementia / exercise 相关医学证据筛选与 health evidence synthesis | 高 |
| `07 / 11.07` 边界 | 不转 `11.07` | PDF p1; p10 Sec. 7 | 它不是研究 scientific knowledge production itself，而是医学 systematic review screening | 高 |
| 验证方式 | benchmark + human evaluation | PDF p5-p6 | 在 234 abstracts 与 10 个问题上比较 vanilla、lightRAG、CausalAgent | 高 |
| 主要风险 | core-strength risk | PDF p10 Sec. 7 | 贡献更偏 medical evidence workflow，而不是强发现型医学结果 | 中高 |

## 0. 摘要翻译

论文提出一个 causal-enhanced medical research screening agent，把知识图谱、lightRAG 检索和因果推理结合起来，用于 systematic review 语境中的医学文献筛选与复杂证据问答。系统先基于 PICOS 标准对摘要做 INCLUDE/EXCLUDE/UNCERTAIN 判定，再用因果增强的检索与推理模块回答医学证据问题。结果表明，在小规模医学证据语料上，causal-enhanced 方案比更简单的 RAG 或 vanilla agents 更有助于 evidence synthesis，但其贡献仍主要停留在 workflow 级支持。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确医学研究筛选任务，具有多步工作流、工具调用、结构化决策与回答生成
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：部分是
- 在科研流程中承担的明确角色：文献筛选、证据评估与验证、结果解释、研究工作流编排

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.03
- 三级类：Evidence-based medical-research screening agents
- 四级专题：Systematic-review screening and causal evidence-synthesis agents
- 四级专题是否为新增：否
- 归类理由：任务稳定落在医学证据筛选与 evidence-based medicine，而不是通用科研知识生产研究
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：dementia / exercise intervention medical evidence
- 最终科学问题：如何让 AI agent 更可靠地完成 systematic review screening 与医学证据整合
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：causal RAG 是方法，研究对象仍是医学证据筛选任务

### 2.3 容易混淆的边界

- 可能误归类到：11.07；01.04
- 最终判定：保持 07.03
- 判定理由：虽然处理的是 scientific literature，但问题空间始终是 health evidence synthesis，而不是 scientific knowledge production itself
- 是否需要二次复核：否，主类边界已稳定

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：部分是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：causal evidence-screening agent

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：部分是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：部分是
- 自主决策：是
- 多 Agent 协作：部分是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：是
- 数字孪生：否
- 机器人平台：否
- 其他：causal evidence integration

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：提升 evidence-based medicine 语境下 automatic screening 与 question answering 的可靠性
- 现有科研流程或方法的痛点：普通 RAG 或 agent 在复杂医学证据筛选中容易缺少因果结构和证据链
- 核心假设或直觉：在检索增强工作流中加入 causal reasoning 能改善医学证据整合质量

### 4.2 系统流程

1. 输入：systematic review screening task 或医学证据问题
2. 任务分解 / 规划：先进行 PICOS-based screening，再进入证据整合
3. 工具、数据库、模型或实验平台调用：lightRAG、knowledge graph、Think tool
4. 中间结果反馈：基于 retrieval 与 causal graph 更新分析
5. 决策或迭代：在证据不足或冲突时继续筛选和推理
6. 输出：医学证据筛选结果与结构化回答

### 4.3 系统组件

- Agent 核心：Causal-Enhanced AI Agent
- 工具 / API / 数据库：lightRAG; causal graph; Think tool
- 记忆或状态模块：retrieval / graph state
- 规划器：screening + reasoning workflow
- 评估器 / verifier：human evaluation
- 人类反馈或专家介入：有
- 实验平台或仿真环境：234 abstracts corpus and evaluation questions

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

- 数据集 / 实验对象：234 abstracts；10 evaluation questions
- 任务设置：medical screening 与 evidence synthesis
- 对比基线：vanilla agent；lightRAG；CausalAgent variants
- 评价指标：screening quality；answer quality；human judgments
- 关键结果：causal-enhanced setup 在复杂医学证据问题上更稳
- 是否有消融实验：部分有
- 是否有失败案例或负结果：规模仍小，跨领域泛化未证实

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏研究流程支持
- 科学贡献是否经过验证：部分是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 解释 / 证据评估
- 证据强度：专家评估

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：强调 systematic review screening 与 causal evidence reasoning，而不是单轮医学问答
- 与已有 Agent / 科研智能系统的区别：把 knowledge graph 与 causal reasoning 明确接到医学 evidence workflow
- 与同一科学领域其他 Agent 文献的关系：可与 DeepER-Med、HealthFlow 构成 `07` 内的 evidence-centered medical agents 子群
- 主要创新点：将 medical screening、retrieval、knowledge graph 与 causal reasoning 组合成可执行 agent workflow

## 7. 局限性与风险

- Agent 自主性不足：仍以 evidence workflow assistant 为主
- 科学验证不足：没有直接对应新的医学发现或临床结论
- 泛化性不足：语料规模和场景仍偏小
- 工具链依赖：对 retrieval 与图结构质量高度敏感
- 数据泄漏或 benchmark 偏差：小样本人工评价存在偏差风险
- 成本、可复现性或安全风险：复杂医疗语境下仍需专家复核

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学中的 evidence-based medical-research agents
- 可支撑哪个论点：处理科学文献不等于 `11.07`；只要对象是医学 evidence workflow，就应留在 `07`
- 可用于哪个表格或图：`07 / 11.07 / 01.04` 边界表
- 适合作为代表性案例吗：适合，特别适合作为边界案例
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：PDF p3 Sec. 3.1；p4 Sec. 3.3；p10 Sec. 7
- 需要与哪些论文并列比较：Wang_2026_DeepER_Med；Zhu_2025_HealthFlow

## 9. 总结

### 9.1 一句话概括

将 causal reasoning 接入医学证据筛选的 research-screening agent。

### 9.2 速记版 pipeline

1. 按 PICOS 筛选医学摘要
2. 构建检索与知识图谱上下文
3. 做因果增强推理
4. 输出 evidence synthesis 结果

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.03
三级类：Evidence-based medical-research screening agents
四级专题：Systematic-review screening and causal evidence-synthesis agents
Agent 类型：LLM Agent; Tool-using Agent; Retrieval-augmented Agent; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; tool_use_and_code_execution; result_interpretation; evidence_assessment_and_validation
自主能力：tool_use; autonomous_decision_making
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; knowledge_graph
科学贡献类型：system_platform; explanation; evidence_assessment
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
