# Solovev et al. 2025 - MADD: Multi-Agent Drug Discovery Orchestra

**论文信息**
- 标题：MADD: Multi-Agent Drug Discovery Orchestra
- 作者：Solovev et al.
- 年份：2025
- 来源 / venue：Findings of the Association for Computational Linguistics: EMNLP 2025
- DOI / arXiv / URL：https://doi.org/10.18653/v1/2025.findings-emnlp.367
- PDF / 本地文件路径：当前未保存本地 PDF；本笔记基于 ACL Anthology 官方摘要
- 论文类型：会议论文 / multi-agent drug discovery system
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | ACL Anthology abstract | `MADD` 被明确写成 `a multi-agent system` | 高 |
| 科学对象归类 | `07.04` | ACL Anthology abstract | 直接服务于 `hit identification` 与 `drug design` | 高 |
| 方法流程 | 四个协调 agent | ACL Anthology abstract | 系统从 natural language query 构建并执行 hit identification pipeline | 高 |
| 验证方式 | 七个 drug discovery cases | ACL Anthology abstract | 对七个案例评测，并在五个 biological targets 上发布 hit molecules | 高 |
| 边界判断 | 不转 `01.04` | ACL Anthology abstract | 虽有 orchestration 色彩，但科学对象稳定是早期药物发现 | 高 |

## 0. 摘要翻译

MADD 聚焦早期药物发现中的 hit identification 问题。论文指出，大语言模型让虚拟筛选更高效，但工具复杂度阻碍了湿实验研究者使用。为此，作者提出多 Agent 系统 MADD，它能从自然语言查询构建并执行定制的 hit identification pipeline，并用四个协调 Agent 负责 de novo compound generation 和 screening 的关键子任务。系统在七个药物发现案例上进行评测，在五个生物靶点上产出 hit molecules，并额外发布包含超过三百万化合物 query-molecule pairs 与 docking scores 的新 benchmark。稳定对象明显是 `07.04` 药物发现，而不是通用科研工作流。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：多 Agent 协作、任务分工、自然语言到 pipeline 的执行链条完整
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：pipeline construction、分子生成、筛选、命中识别

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：hit identification / drug discovery
- 四级专题：multi-agent drug discovery orchestration
- 四级专题是否为新增：否
- 归类理由：系统围绕早期药物发现中的 hit identification 和 AI-first drug design 展开
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：drug hit molecules / hit identification pipelines
- 最终科学问题：如何从自然语言需求自动构建并执行药物命中发现流程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：多 Agent orchestration 是方法层，稳定对象仍是药物发现

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 07.04
- 判定理由：摘要持续围绕 drug discovery、biological targets、hit molecules，而非一般科学平台
- 是否需要二次复核：是，可后续补全文看 benchmark 与真实发现权重

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：未见明确证据
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：drug-discovery orchestra

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：否
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：未见明确证据
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：virtual screening

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低早期药物发现工具链的复杂度门槛
- 现有科研流程或方法的痛点：虚拟筛选和药物设计工具太复杂，不利于湿实验研究者直接使用
- 核心假设或直觉：多 Agent 可结合 LLM 可解释性与专用工具精度，自动构建命中发现流程

### 4.2 系统流程

1. 输入：自然语言形式的 drug discovery query
2. 任务分解 / 规划：构建 customized hit identification pipeline
3. 工具、数据库、模型或实验平台调用：四个协调 agent 处理 de novo generation 与 screening 子任务
4. 中间结果反馈：根据筛选结果更新后续步骤
5. 决策或迭代：继续候选生成与评估
6. 输出：hit molecules 与 benchmark data

### 4.3 系统组件

- Agent 核心：MADD
- 工具 / API / 数据库：specialized models and tools for screening
- 记忆或状态模块：pipeline state
- 规划器：natural-language-to-pipeline orchestration
- 评估器 / verifier：七个案例评测与 docking / target-level results
- 人类反馈或专家介入：摘要未展开
- 实验平台或仿真环境：virtual screening / computational pipeline

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：是
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：七个 drug discovery cases，五个 biological targets
- 任务设置：从自然语言构建 hit identification pipelines
- 对比基线：existing LLM-based solutions
- 评价指标：superior performance、identified hit molecules、benchmark release
- 关键结果：在五个 biological targets 上完成 AI-first drug design 并发布 hit molecules
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，发布 identified hit molecules
- 科学贡献是否经过验证：有官方摘要级 benchmark / target-level evidence
- 贡献强度判断：中高
- 科学贡献类型：design / system_platform / benchmark
- 证据强度：主摘要支持，偏计算验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单模型虚拟筛选，而是多 Agent drug discovery pipeline
- 与已有 Agent / 科研智能系统的区别：强调从自然语言到 hit identification 的完整执行
- 与同一科学领域其他 Agent 文献的关系：可与 AgentD、CLADD、GALILEO、Medea 对比
- 主要创新点：把自然语言需求直接编译成多 Agent 药物发现工作流

## 7. 局限性与风险

- Agent 自主性不足：仍需全文确认失败恢复与人工介入情况
- 科学验证不足：官方摘要未显示湿实验层面验证
- 泛化性不足：是否能扩展到更多药物发现阶段仍待全文
- 工具链依赖：依赖 specialized models / screening stack
- 数据泄漏或 benchmark 偏差：benchmark 设计细节仍需全文复核
- 成本、可复现性或安全风险：大规模筛选计算成本较高

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学
- 可支撑哪个论点：药物发现 Agent 正从 assistant 走向 orchestration system
- 可用于哪个表格或图：drug discovery multi-agent systems table
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续补 PDF
- 需要与哪些论文并列比较：Ock 2025、Lee 2025、Jiang 2026、Sui 2026

## 9. 总结

### 9.1 一句话概括

MADD 用四个 Agent 自动编排药物命中发现流程。

### 9.2 速记版 pipeline

1. 接收自然语言药物需求
2. 拆成命中发现子任务
3. 多 Agent 执行生成和筛选
4. 评测多个案例
5. 输出命中分子

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：07
二级类：07.04
三级类：hit identification / drug discovery
四级专题：multi-agent drug discovery orchestration
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; simulation_validation; high_throughput_computation
交叉属性：computation_driven; data_driven; simulation_driven; high_throughput_screening
科学贡献类型：design; system_platform; benchmark
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
