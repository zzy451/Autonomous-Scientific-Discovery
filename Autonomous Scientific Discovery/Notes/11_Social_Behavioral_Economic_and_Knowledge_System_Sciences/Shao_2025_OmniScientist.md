# Shao et al. 2025 - OmniScientist: Toward a Co-evolving Ecosystem of Human and AI Scientists

**论文信息**
- 标题：OmniScientist: Toward a Co-evolving Ecosystem of Human and AI Scientists
- 作者：Chenyang Shao; Dehao Huang; Yu Li; Keyu Zhao; Weiquan Lin; Yining Zhang; Qingbin Zeng; Zhiyu Chen; Tianxing Li; Yifei Huang; Taozhong Wu; Xinyang Liu; Ruotong Zhao; Mengsheng Zhao; Jiaoyang Li; Xuhua Zhang; Yue Wang; Yuanyi Zhen; Fengli Xu; Yong Li; Tie-Yan Liu
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2511.16931
- PDF / 本地文件路径：当前无本地 PDF；本 note 基于 arXiv 摘要页与 batch12 reviewer evidence pack
- 论文类型：研究论文 / scientific ecosystem agent platform
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract；Reader-C evidence pack | 系统组织多 Agent / 人机协作科学流程 | 高 |
| 科学对象归类 | `11 / 11.07` | arXiv abstract；PDF contents；Reader-C evidence pack | 核心对象是 scientific knowledge production / ecosystem / peer review / attribution | 高 |
| 方法流程 | 多模块科研生态 | Reader-C evidence pack | 包含 literature review、ideation、writing、review、protocol、evaluation platform | 高 |
| 边界判断 | 不移到 01.04 | Reader-C evidence pack | 创新点集中在科学制度、知识网络、贡献归因与评审机制，而非通用 workflow substrate | 高 |
| 实验验证 | benchmark + expert evaluation | Reader-C evidence pack | 评价主要为平台评测、用户投票、Elo ranking 等 | 中高 |

## 0. 摘要翻译

论文认为现有 AI Scientist 过度把科学发现理解成孤立的搜索或优化问题，而忽视科学活动的社会性、协作性与制度性。为此，OmniScientist 将 citation networks、peer review、contribution attribution、human participation、collaboration protocol 与 open evaluation platform 编入 AI scientific workflow，尝试构建一个人类与 AI 科学家共同演化的生态系统。该工作研究的重点不是某个自然科学对象，而是科学知识生产系统本身。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确科研目标、多 Agent / 人机协作、多步流程与平台化反馈机制
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：知识组织、假设生成、工作流编排、论文写作、评审与验证

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
- 四级专题：Co-evolving human-AI scientist ecosystems
- 四级专题是否为新增：否
- 归类理由：论文的主要贡献是把 scientific knowledge production、peer review、attribution 和 open evaluation 本身对象化
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：scientific ecosystem 与 scientific knowledge production
- 最终科学问题：如何构建人类与 AI 科学家共同演化的科学生产与评估系统
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：通用科研平台只是表面，真正对象是科学制度与知识生产机制

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 11.07
- 判定理由：知识网络、贡献归因、peer review、protocolized collaboration 与 ScienceArena 都直接指向 scientific system object
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：scientific ecosystem orchestration

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：是
- 假设生成：是
- 实验设计：部分是
- 仿真建模：否
- 工具调用与代码执行：部分是
- 实验执行：部分是
- 数据分析：部分是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：是
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：是
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
- 其他：science-of-science infrastructure

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：纠正把科学仅视为个体搜索问题的简化叙事
- 现有科研流程或方法的痛点：忽视协作、评审、归因和开放评估
- 核心假设或直觉：只有把科学制度与知识网络纳入 workflow，AI scientist 才更接近真实科研生态

### 4.2 系统流程

1. 输入：研究问题、文献网络与协作机制
2. 任务分解 / 规划：拆分为综述、创意、实验、写作、评审、评价等模块
3. 工具、数据库、模型或实验平台调用：citation networks、protocol、ScienceArena 等
4. 中间结果反馈：通过评审、投票、排序和协作反馈持续修正
5. 决策或迭代：在生态中不断更新贡献与评价
6. 输出：共演化的人机科学生产结果

### 4.3 系统组件

- Agent 核心：OmniScientist ecosystem
- 工具 / API / 数据库：knowledge system；citation networks；ScienceArena；OSP
- 记忆或状态模块：知识网络与贡献轨迹
- 规划器：有
- 评估器 / verifier：peer review 与 open evaluation platform
- 人类反馈或专家介入：有
- 实验平台或仿真环境：platform / evaluation environment

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

- 数据集 / 实验对象：scientific workflow modules and evaluation platform
- 任务设置：platform evaluation、user voting、ranking 与 modular case studies
- 对比基线：现有 AI scientist systems
- 评价指标：Elo ranking、用户评价、协作表现
- 关键结果：展示人机共演化科研生态的系统原型与评估路径
- 是否有消融实验：当前证据不足
- 是否有失败案例或负结果：当前证据不足

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：重点是 scientific ecosystem platform 与 evaluation design
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; scientific_knowledge_production
- 证据强度：high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：它研究的是科学制度和知识生产本身
- 与已有 Agent / 科研智能系统的区别：比一般 01.04 平台更强地对象化了 peer review、contribution attribution 和 open evaluation
- 与同一科学领域其他 Agent 文献的关系：可与 Automating Scientific Evaluation、aiXiv、SciSciGPT 等并列
- 主要创新点：把科学共同体协作与知识生产机制嵌入 AI scientist framework

## 7. 局限性与风险

- Agent 自主性不足：平台中仍有较多人类参与
- 科学验证不足：主要是平台与评价证据，不是强自然科学发现证据
- 泛化性不足：生态是否能在真实科研社区中长期运作仍待验证
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：开放评估和投票机制可能引入偏差
- 成本、可复现性或安全风险：治理复杂度高

## 8. 对综述写作的价值

- 可放入哪个章节：11.07 科学系统与知识生产研究
- 可支撑哪个论点：scientific ecosystem / peer-review / attribution 样本应稳放 11.07，而不是泛泛归 01.04
- 可用于哪个表格或图：11.07 / 01.04 关键边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续补全文后细化
- 需要与哪些论文并列比较：Automating Scientific Evaluation、aiXiv、SciSciGPT

## 9. 总结

### 9.1 一句话概括

面向科学知识生产生态的人机共演化 Agent 平台。

### 9.2 速记版 pipeline

1. 组织文献与知识网络
2. 生成研究与写作流程
3. 引入协作协议和评审
4. 用开放评价持续反馈
5. 输出共演化科研生态结果

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：
四级专题：Co-evolving human-AI scientist ecosystems
Agent 类型：LLM Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：hypothesis_generation; workflow_orchestration; manuscript_drafting; evidence_assessment_and_validation; feedback_iteration; knowledge_extraction_and_organization
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; knowledge_graph
科学贡献类型：system_platform; scientific_knowledge_production
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
