# Xiang et al. 2025 - SciReplicate-Bench

**论文信息**
- 标题：SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers
- 作者：Xiang et al.
- 年份：2025
- 来源 / venue：COLM 2025 / arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2504.00255
- PDF / 本地文件路径：临时读取 `ASD-0100_SciReplicate-Bench.pdf`；未写入项目 Reference_PDF
- 论文类型：benchmark / dual-agent framework
- 当前状态：已读 / 已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

Evidence level: full-text (arXiv PDF full text; COLM 2025 publication status from PDF first page).

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，提出 Sci-Reproducer dual-agent 框架并评测 agent-driven reproduction | 摘要；Introduction；Sec. 3 | Paper Agent 解释算法，Coding Agent 生成代码 | 高 |
| 科学对象归类 | `01.04` 科研智能系统 / 科研复现 benchmark | 摘要；Table 1；Sec. 3 | benchmark 面向从论文复现算法代码的科研能力 | 高 |
| 方法流程 | 论文理解 - 推理图 - 代码生成 - 测试执行 | Abstract；Sec. 3；metrics | 使用 reasoning graph accuracy 与 test pass rate 评估 | 高 |
| 实验验证 | 100 tasks from 36 NLP papers | Abstract；Sec. 3 | benchmark 从 2024 NLP papers 构建，含 repository context 和 reference implementation | 高 |
| 科学贡献 | 科研算法复现 benchmark 与双 Agent baseline | Abstract；Contributions | 揭示 LLM 能理解算法但代码实现仍困难 | 高 |

## 0. 摘要翻译

SciReplicate-Bench 评估 LLM 从近期 NLP 论文算法描述中生成复现代码的能力。benchmark 包含来自 36 篇 2024 年 NLP 论文的 100 个任务，要求模型理解论文中的算法描述、结合论文和代码库上下文，生成可运行实现。作者提出 Sci-Reproducer 双 Agent 框架，由 Paper Agent 理解算法、Coding Agent 实现代码，并引入 reasoning graph accuracy 与 test pass rate 等指标。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：论文不仅是 benchmark，还提出双 Agent 框架执行算法理解和代码实现，且任务是科研论文复现。
- 判定置信度：高。
- 是否面向明确科研目标：是，提高科研可复现性和算法复现能力。
- 是否具有多步行动过程：是，论文理解、信息抽取、代码生成、测试执行。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分。
  - 工具调用：是，代码生成与测试执行环境。
  - 反馈迭代：框架细节需复核，但 benchmark 强调 agent-driven task execution。
  - 自主决策：中。
  - 多 Agent 协作：是，Paper Agent + Coding Agent。
- 在科研流程中承担的明确角色：论文理解者、算法复现者、科研代码实现者、评测对象。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，是科研复现 benchmark 和 Agent 框架。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：不完全缺少；代码生成有测试验证，但是否多轮修复需进一步复核。
- 若排除，排除理由：不适用。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`01` 形式、信息与计算科学。
- 二级类：`01.04` 科研智能系统与 Autonomous Scientific Discovery。
- 三级类：agent-driven algorithmic reproduction。
- 四级专题：Agent-driven scientific reproduction benchmark。
- 四级专题是否为新增：是，主清单已有新增标记。
- 归类理由：研究对象是科研论文算法复现能力和科研智能评测，不是 NLP 任务本身。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：论文算法描述、代码库上下文、reference implementation、reasoning graph。
- 最终科学问题：LLM/Agent 能否从论文自动复现算法实现。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：归 `01.04` 是因为对象是通用科研复现能力，而不是因为用了 LLM。

### 2.3 容易混淆的边界

- 可能误归类到：NLP 或软件工程 benchmark。
- 最终判定：`01.04`。
- 判定理由：benchmark 服务于科学论文复现和科研 Agent 能力评估。
- 是否需要二次复核：低。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：部分。
- Tool-using Agent：是。
- Retrieval-augmented Agent：部分，使用论文和文献上下文。
- Multi-Agent System：是，dual-agent。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：否。
- Hybrid Agent：是。
- 其他：algorithmic reproduction agents。

### 3.2 科研流程角色

- 文献检索与阅读：阅读论文和引用上下文。
- 知识抽取与组织：核心。
- 科学问题提出：否。
- 假设生成：否。
- 实验设计：否。
- 仿真建模：否。
- 工具调用与代码执行：核心。
- 实验执行：代码测试执行。
- 数据分析：评测分析。
- 结果解释：reasoning graph。
- 证据评估与验证：核心。
- 论文写作：否。
- 端到端科研流程自动化：局部，算法复现环节。

### 3.3 自主能力

- 任务分解：中。
- 计划生成：中。
- 工具调用：强。
- 记忆与状态维护：中。
- 反馈迭代：中，需复核具体实现。
- 自主决策：中。
- 多 Agent 协作：强。
- 环境交互：代码库和测试环境。
- 闭环实验：代码验证闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：否。
- 实验驱动：否。
- 仿真驱动：否。
- 多模态：否。
- 多尺度建模：否。
- 高通量筛选：否。
- 知识图谱：reasoning graph 评测。
- 数字孪生：否。
- 机器人平台：否。
- 其他：reproducibility benchmark。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：将论文算法描述转成可运行代码是科研复现和科学发现加速的瓶颈。
- 现有科研流程或方法的痛点：通用代码 benchmark 不要求深入理解论文算法，论文描述常不完整或分散。
- 核心假设或直觉：把论文理解和代码实现分给两个 Agent，并用 reasoning graph 衡量理解质量，可更细致评估科研复现能力。

### 4.2 系统流程

1. 输入：目标算法描述、原论文、引用文献上下文、repository context。
2. 任务分解 / 规划：Paper Agent 解释算法逻辑；Coding Agent 规划实现。
3. 工具、数据库、模型或实验平台调用：读取代码库、生成代码、运行测试。
4. 中间结果反馈：reasoning graph 和 test cases 提供评测信号。
5. 决策或迭代：根据框架实现生成最终代码；多轮细节需复核。
6. 输出：算法复现代码、reasoning graph、测试结果。

### 4.3 系统组件

- Agent 核心：Paper Agent、Coding Agent。
- 工具 / API / 数据库：论文 PDF/LaTeX、引用文献、代码库、测试用例。
- 记忆或状态模块：任务上下文和 reasoning graph。
- 规划器：Paper/Coding agent 内部规划。
- 评估器 / verifier：reasoning graph accuracy、test pass rate、CodeBLEU。
- 人类反馈或专家介入：benchmark 标注构建阶段。
- 实验平台或仿真环境：代码执行环境。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：核心。
- 仿真验证：否。
- 高通量计算：否。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：benchmark 标注由科学家/人工完成。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：100 tasks from 36 NLP papers published in 2024。
- 任务设置：给算法描述、literature context、repository context，生成代码并通过测试。
- 对比基线：多种 LLM / coding agents；具体结果需复核表格。
- 评价指标：reasoning graph accuracy、test pass rate、CodeBLEU。
- 关键结果：LLM 算法理解强于实际实现；论文描述缺失或不一致是复现失败的重要原因。
- 是否有消融实验：有一定模型/输入比较。
- 是否有失败案例或负结果：有，缺失实现细节和论文/代码不一致导致失败。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：否，贡献是 benchmark 和复现 Agent。
- 科学贡献是否经过验证：通过 benchmark 评测。
- 贡献强度判断：中。
- 科学贡献类型：benchmark / 系统平台 / 科研复现能力评测。
- 证据强度：benchmark。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：关注科学论文算法复现能力，而非特定科学预测任务。
- 与已有 Agent / 科研智能系统的区别：提供专门 benchmark 和 reasoning graph metric。
- 与同一科学领域其他 Agent 文献的关系：与 ResearchCodeAgent 互补；前者是 benchmark + dual-agent，后者是方法 codification 系统。
- 主要创新点：从真实论文构造代码复现任务，并区分算法理解和实现正确性。

## 7. 局限性与风险

- Agent 自主性不足：作为 benchmark 和 baseline 框架，闭环修复能力可能有限。
- 科学验证不足：只验证算法复现，不验证新科学发现。
- 泛化性不足：NLP 论文为主。
- 工具链依赖：依赖开源 repository 和测试用例。
- 数据泄漏或 benchmark 偏差：2024 论文降低但不能完全消除污染风险。
- 成本、可复现性或安全风险：自动复现代码可能产生看似正确但科学意义错误的实现。

## 8. 对综述写作的价值

- 可放入哪个章节：科研智能系统 benchmark；科研复现 Agent；代码执行型 Agent。
- 可支撑哪个论点：科学 Agent 评估需要同时衡量“理解科学文本”和“产生可执行证据”的能力。
- 可用于哪个表格或图：benchmark 对比表；科学复现 pipeline 图。
- 适合作为代表性案例吗：适合作为 benchmark 代表。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：Table 1；Sec. 3；metrics section。
- 需要与哪些论文并列比较：ResearchCodeAgent、SciCode、MLE-Bench、MLAgentBench、CodeScientist。

## 9. 总结

### 9.1 一句话概括

评测 Agent 从论文复现算法代码的 benchmark。

### 9.2 速记版 pipeline

1. 从论文抽取算法任务。
2. Paper Agent 理解算法。
3. Coding Agent 生成实现。
4. 用 reasoning graph 评估理解。
5. 用测试和 CodeBLEU 评估代码。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01 形式、信息与计算科学
二级类：01.04
三级类：科研算法复现 / scientific coding benchmark
四级专题：Agent-driven scientific reproduction benchmark
Agent 类型：LLM Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：文献检索与阅读; 知识抽取与组织; 工具调用与代码执行; 证据评估与验证
自主能力：任务分解; 计划生成; 工具调用; 多 Agent 协作; 环境交互
验证方式：benchmark
交叉属性：计算驱动; 知识图谱(reasoning graph)
科学贡献类型：benchmark; 系统平台
证据强度：benchmark
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
