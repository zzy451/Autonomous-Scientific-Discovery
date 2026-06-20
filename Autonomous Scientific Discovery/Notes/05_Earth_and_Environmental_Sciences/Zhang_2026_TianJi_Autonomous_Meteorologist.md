# Zhang et al. 2026 - TianJi: An autonomous AI meteorologist for discovering physical mechanisms in atmospheric science

**论文信息**
- 标题：TianJi: An autonomous AI meteorologist for discovering physical mechanisms in atmospheric science
- 作者：Kaikai Zhang; Xiang Wang; Haoluo Zhao; Nan Chen; Mengyang Yu; Jing-Jia Luo; Tao Song; Fan Meng
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2603.27738
- PDF / 本地文件路径：当前笔记基于 arXiv abstract / HTML
- 论文类型：预印本 / autonomous atmospheric-science agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract / HTML | 系统会自主做文献调研、假设生成、WRF 调用与假设验证 | 高 |
| 科学对象归类 | `05.02` | 标题；abstract | 稳定对象是 atmospheric science 中的 physical mechanism discovery | 高 |
| 方法流程 | 两层 agent workflow | HTML | cognitive planning layer + engineering execution layer | 高 |
| 工具调用 | 强 | HTML | 以 WRF 为核心的 meteorology-specific verification engine | 高 |
| 实验验证 | benchmark + simulation | HTML | 在大气动力学场景中实现 zero human intervention，并能自修复错误 | 高 |

## 0. 摘要翻译

论文提出 TianJi，一个自治 AI meteorologist，用于大气科学中的物理机制发现。系统既能自主阅读与生成假设，也能把这些假设交给以 WRF 为中心的多 Agent 验证引擎执行，并对结果进行支持 / 否定判断。作者展示了 TianJi 在多个 atmospheric dynamics 场景中的端到端执行能力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备文献调研、假设提出、模拟器调用、结果判断和错误恢复等典型 Agent 行为
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：文献调研、假设生成、模拟验证、结果解释

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：05
- 二级类：05.02
- 三级类：大气机制发现与气象模拟验证
- 四级专题：autonomous atmospheric-mechanism discovery agents
- 四级专题是否为新增：否
- 归类理由：任务、模拟器和验证对象都锚定 atmospheric science
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：atmospheric science physical mechanisms
- 最终科学问题：如何自主提出并验证大气科学中的物理机制假设
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：WRF 与气象任务只是对对象的具体落实，稳定主类仍由大气科学对象决定

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 05.02
- 判定理由：模拟器、假设类型和验证场景都深度绑定气象 / 大气动力学
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：AI meteorologist

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：否
- 仿真建模：是
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
- 仿真驱动：是
- 多模态：否
- 多尺度建模：部分是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：WRF-centric verification workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：大气科学中的机制发现需要从文献、假设到模拟验证的长链条组织
- 现有科研流程或方法的痛点：人工设计和验证假设成本高，错误恢复困难
- 核心假设或直觉：如果把认知规划与工程执行分层，自治系统能更稳地完成气象机制发现

### 4.2 系统流程

1. 输入：大气科学问题
2. 任务分解 / 规划：认知层完成文献调研与假设生成
3. 工具、数据库、模型或实验平台调用：工程层调用 WRF 等模拟工具
4. 中间结果反馈：记录运行状态并自动修复部分错误
5. 决策或迭代：判断假设是否被支持并继续修正
6. 输出：机制结论与验证结果

### 4.3 系统组件

- Agent 核心：TianJi
- 工具 / API / 数据库：WRF-centered verification engine
- 记忆或状态模块：任务与执行状态
- 规划器：meta-planner + worker agents
- 评估器 / verifier：hypothesis support evaluation
- 人类反馈或专家介入：有限
- 实验平台或仿真环境：atmospheric simulation environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：多类 atmospheric dynamics 场景
- 任务设置：假设生成与 WRF-based verification
- 对比基线：非自治或弱自治流程
- 评价指标：端到端完成度、错误恢复、假设判断质量
- 关键结果：部分复杂场景中可实现 zero human intervention
- 是否有消融实验：摘要级信息有限
- 是否有失败案例或负结果：作者承认长时 climate 与多圈层问题仍弱

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：偏机制发现流程与验证组织
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：knowledge_discovery
- 证据强度：中高

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：从预测扩展到机制发现与验证
- 与已有 Agent / 科研智能系统的区别：强调 meteorology-specific verification engine
- 与同一科学领域其他 Agent 文献的关系：可与 ClimAgent、EarthLink 构成 climate / atmosphere 三角样本
- 主要创新点：把文献到 WRF 验证的长链条压成自治气象研究流程

## 7. 局限性与风险

- Agent 自主性不足：场景仍偏短时中尺度动力过程
- 科学验证不足：对长期 climate 与多圈层耦合外推较弱
- 泛化性不足：验证场景仍有限
- 工具链依赖：高度依赖 WRF 和气象模拟栈
- 数据泄漏或 benchmark 偏差：更细评测设计仍需全文复核
- 成本、可复现性或安全风险：模拟成本较高

## 8. 对综述写作的价值

- 可放入哪个章节：地球与环境科学中的大气机制发现 Agent
- 可支撑哪个论点：Agent 不只做预测，也能承担机制提出与验证
- 可用于哪个表格或图：大气科学 Agent 功能分解表
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：两层架构图与 WRF 验证流程
- 需要与哪些论文并列比较：ASD-0623、ASD-0633

## 9. 总结

### 9.1 一句话概括

自治气象 Agent 用 WRF 驱动大气机制假设的提出与验证。

### 9.2 速记版 pipeline

1. 读文献并生成假设  
2. 拆解验证任务  
3. 调 WRF 等工具执行  
4. 判断假设并修正

### 9.3 标注字段汇总

```text
是否纳入：是
主类：05
二级类：05.02
三级类：大气机制发现与气象模拟验证
四级专题：autonomous atmospheric-mechanism discovery agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; hypothesis_generation; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; simulation_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：knowledge_discovery
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
