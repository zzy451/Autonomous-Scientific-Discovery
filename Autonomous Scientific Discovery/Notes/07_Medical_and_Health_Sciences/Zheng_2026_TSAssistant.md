# Zheng et al. 2026 - TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment

**论文信息**
- 标题：TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment
- 作者：Xiaochen Zheng; Zhiwen Jiang; David Tokar; Yexiang Cheng; Alvaro Serra; Melanie Guerard; Klas Hatje; Tatyana Doktorova
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.23938
- PDF / 本地文件路径：当前笔记基于 arXiv abstract + arXiv HTML v3
- 论文类型：研究论文 / target-safety assessment multi-agent system
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract; arXiv HTML v3 | 有 Research / Synthesis subagents、memory、programmatic enforcement、HITL refinement | 高 |
| 科学对象归类 | `07 / 07.04` | abstract; evaluation | 研究对象是 therapeutic-target safety liabilities 与 preclinical safety assessment | 高 |
| 方法流程 | 结构化证据整合工作流 | main text | 以预定义 report schema 组织多域 biomedical evidence synthesis | 高 |
| 实验验证 | 35 drug targets + 22-target ortholog benchmark | arXiv HTML v3 | claim-level self-consistency、grounding、HITL refinement 都围绕 target safety task 展开 | 高 |
| 边界判断 | 不应移入 `11.07` 或 `01.04` | abstract + discussion | 它不是研究 scientific knowledge production itself，而是用科学证据评估 biomedical targets | 高 |
| 核心风险 | 更偏 core-strength risk | discussion | 更像 target safety report drafting + evidence synthesis + expert refinement，而非强 ASD 发现闭环 | 中高 |

## 0. 摘要翻译

论文提出 TSAssistant，一个面向 therapeutic target safety assessment 的 human-in-the-loop agentic framework。系统把遗传、转录组、同源性、药理和临床证据的检索、整合和带引用写作拆给多个专职 subagents，再由 synthesis 层整合成结构化报告，并允许专家按 section 做定向修订。其核心不是研究科学知识生产本身，而是服务于药物发现早期的 target safety evaluation。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 架构、工具调用、记忆、协调、反馈修订和 HITL refinement
- 判定置信度：高
- 是否面向明确科研目标：是，面向 target safety assessment
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：证据检索、证据整合、结果解释、安全评估、报告生成

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：
- 四级专题：Automated target-safety-assessment agents
- 四级专题是否为新增：否
- 归类理由：最终研究对象是药物发现早期的 target safety / preclinical safety assessment
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：therapeutic-target safety liabilities
- 最终科学问题：如何自动化整合多域生物医学证据以评估 target safety
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：agentic framework 只是组织形式，主对象仍是生物医药安全评估任务

### 2.3 容易混淆的边界

- 可能误归类到：11.07；01.04
- 最终判定：保持 `07 / 07.04`
- 判定理由：系统不是研究 scientific knowledge production itself，而是用证据服务于 target safety
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：Biomedical evidence-synthesis agents

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：preclinical safety assessment

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：target safety assessment 需要跨多类生物医学证据源做结构化综合，人工成本高且一致性差
- 现有科研流程或方法的痛点：传统流程依赖专家手工整合遗传、转录组、药理和临床证据
- 核心假设或直觉：若把领域技能拆给 research/synthesis subagents，再用程序化钩子约束输出，可提高可审计性和稳定性

### 4.2 系统流程

1. 输入：待评估的 therapeutic target
2. 任务分解 / 规划：按预定义 schema 拆成多个证据域
3. 工具、数据库、模型或实验平台调用：检索遗传、转录组、同源性、药理和临床证据
4. 中间结果反馈：citation validation、grounding 和 section-level review 回流
5. 决策或迭代：research/synthesis agents 更新内容并接受 HITL refinement
6. 输出：结构化 target safety report

### 4.3 系统组件

- Agent 核心：Research Subagents + Synthesis Subagents + Orchestrator
- 工具 / API / 数据库：biomedical evidence sources and validation hooks
- 记忆或状态模块：persistent memory store
- 规划器：orchestrator
- 评估器 / verifier：citation validation、claim-level consistency、section-level refinement
- 人类反馈或专家介入：是，section-level HITL refinement
- 实验平台或仿真环境：35 drug targets benchmark

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：是
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：35 drug targets；22-target ortholog benchmark
- 任务设置：target safety assessment and report generation
- 对比基线：人工参考与内部 consistency / grounding 检查
- 评价指标：ortholog matching、sentence grounding、HITL refinement improvement
- 关键结果：135 sequences 审查、86 exact matches；HITL refinement 净提升显著
- 是否有消融实验：有子任务评估
- 是否有失败案例或负结果：仍需人类保留最终判断权

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是 evidence-synthesis system innovation
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 证据整合
- 证据强度：专家确认

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是简单 biomedical QA，而是多域 target safety evidence synthesis workflow
- 与已有 Agent / 科研智能系统的区别：高度 domain-specialized，并强调 programmatic enforcement 与 HITL refinement
- 与同一科学领域其他 Agent 文献的关系：是 `07 / 11.07 / 01.04` 边界中较稳定的 `07.04` 样本
- 主要创新点：把 TSA 流程拆成多 subagents，并用可审计 schema 和验证钩子固定下来

## 7. 局限性与风险

- Agent 自主性不足：最终决策仍依赖专家
- 科学验证不足：更像 evidence synthesis + report drafting，而非强新发现
- 泛化性不足：集中于 target safety task
- 工具链依赖：强依赖多种证据源与验证钩子
- 数据泄漏或 benchmark 偏差：target benchmark 与人工参考可能带来任务定制偏差
- 成本、可复现性或安全风险：真实药物研发环境仍需严格监管控制

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学 / drug discovery and safety agents
- 可支撑哪个论点：科学证据整合服务于生物医药对象时，不应误归到 `11.07`
- 可用于哪个表格或图：`07 / 11.07 / 01.04` 边界表；target safety agents 表
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：schema、ortholog benchmark、HITL refinement
- 需要与哪些论文并列比较：其他 biomedical evidence-synthesis agents

## 9. 总结

### 9.1 一句话概括

面向药物靶点安全评估的 HITL 多 Agent 系统。

### 9.2 速记版 pipeline

1. 读入待评估靶点
2. 分派多域证据检索
3. 汇总并写成结构化报告
4. 做 grounding 与一致性检查
5. 接受专家定向修订

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：
四级专题：Automated target-safety-assessment agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; paper_writing; workflow_orchestration
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; clinical_data; expert_evaluation
交叉属性：computation_driven; data_driven; multiscale_modeling
科学贡献类型：system_platform
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
