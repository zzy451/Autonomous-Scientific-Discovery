# Schmidgall and Moor 2025 - AgentRxiv: Towards Collaborative Autonomous Research

**论文信息**
- 标题：AgentRxiv: Towards Collaborative Autonomous Research
- 作者：Samuel Schmidgall, Michael Moor
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2503.18102
- PDF / 本地文件路径：临时阅读 `ASD-0019.pdf` / `ASD-0019.txt`
- 论文类型：通用科研 Agent 协作平台 / 系统论文
- 当前状态：已读，已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，面向自主研究协作的 Agent 平台 | PDF p.1 Abstract/Fig.1；p.2 Introduction | lets LLM agent laboratories upload and retrieve reports；agents autonomously provide research outputs | 高 |
| 科学对象归类 | `01.04` 通用科研 Agent / 科研协作平台 | PDF p.1-3 | collaborative autonomous research；shared preprint server for agent laboratories | 高 |
| 方法流程 | 多个 Agent laboratory 通过共享 archive 迭代改进研究 | PDF Fig.1/Fig.3；method section | upload, retrieve, build upon prior reports | 高 |
| 实验验证 | MATH-500、GPQA、MMLU-Pro、MedQA 等 benchmark | PDF Abstract；results | MATH-500 70.2% to 78.2%；平均跨 benchmark +3.3%；parallel labs 79.8% | 高 |
| 科学贡献 | 让自主 Agent 研究具备累积性和协作性 | PDF contributions | agents build upon discoveries of other agents over time | 高 |

## 0. 摘要翻译

AgentRxiv 针对已有自主科研 Agent 彼此孤立、难以累积前序研究的问题，提出一个供 LLM agent laboratories 上传、检索和复用研究报告的共享平台。作者让 Agent laboratories 发现新的推理和 prompting 技术，发现有访问历史研究的 Agent 在 MATH-500 上从 70.2% 提升到 78.2%，且发现的策略能泛化到 GPQA、MMLU-Pro、MedQA 等 benchmark，平均提升约 3.3%。多个实验室并行协作时也能推动共同目标。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：平台服务于 autonomous agent laboratories；Agent 自主生成、共享并基于研究报告继续实验。
- 判定置信度：高。
- 是否面向明确科研目标：是，目标是发现和改进推理 / prompting 技术，并研究 agentic scientific collaboration。
- 是否具有多步行动过程：是。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是。
  - 工具调用：是，使用 Agent Laboratory、archive、benchmarks。
  - 反馈迭代：是，每代研究基于前序报告。
  - 自主决策：是。
  - 多 Agent 协作：是，多个 agent laboratories 协同。
- 在科研流程中承担的明确角色：研究报告生产者、文献/报告检索者、方法改进者、实验评估者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，是 Agent 协作科研平台。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`01` 形式、信息与计算科学。
- 二级类：`01.04` 科研智能系统与 Autonomous Scientific Discovery。
- 三级类：`01.04.04` 多 Agent 科研协同系统 / `01.04.05` 通用科学发现平台。
- 四级专题：General scientific research-agent systems。
- 四级专题是否为新增：否。
- 归类理由：研究对象是自主科研协作机制和 Agent 研究平台，而非具体自然科学对象。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：Agent 科研协作系统、知识累积机制、推理技术发现。
- 最终科学问题：Agent 是否能像科研共同体一样通过共享成果产生累积改进。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM 和 benchmark 是实现与验证，主贡献是科研智能系统。

### 2.3 容易混淆的边界

- 可能误归类到：`11.07` 科学系统与知识生产研究；`01.02` AI。
- 最终判定：`01.04`。
- 判定理由：论文不是社会科学式研究科研共同体，而是构建通用科研 Agent 平台。
- 是否需要二次复核：否。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，检索共享研究报告。
- Multi-Agent System：是。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：初始方向由人给出；执行可自主。
- Hybrid Agent：是。
- 其他：Agent preprint server / research archive。

### 3.2 科研流程角色

- 文献检索与阅读：是，检索前序 agent reports。
- 知识抽取与组织：是。
- 科学问题提出：部分，人类给方向，Agent 生成方法变体。
- 假设生成：是。
- 实验设计：是。
- 仿真建模：否。
- 工具调用与代码执行：是。
- 实验执行：是，benchmark 实验。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：是。
- 论文写作：是，报告上传。
- 端到端科研流程自动化：是，针对计算研究。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：是，通过 AgentRxiv archive 外部化记忆。
- 反馈迭代：是。
- 自主决策：是。
- 多 Agent 协作：是。
- 环境交互：benchmark、archive、代码环境。
- 闭环实验：计算研究闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：计算实验。
- 仿真驱动：否。
- 多模态：否。
- 多尺度建模：否。
- 高通量筛选：否。
- 知识图谱：弱，主要是报告 archive。
- 数字孪生：否。
- 机器人平台：否。
- 其他：research archive、cumulative science。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：现有自主科研 Agent 可以独立产出研究，但缺少像科学共同体一样持续积累和互相借鉴的机制。
- 现有科研流程或方法的痛点：agent runs isolated，不能系统复用先前发现。
- 核心假设或直觉：共享 preprint server 可以把单次 Agent 实验变成可累积的协作研究过程。

### 4.2 系统流程

1. 输入：人类给定研究方向和详细指令。
2. 任务分解 / 规划：多个 Agent laboratories 确定研究问题、实验和报告结构。
3. 工具、数据库、模型或实验平台调用：使用 Agent Laboratory、benchmark、AgentRxiv archive。
4. 中间结果反馈：读取前序研究报告，提取可复用策略。
5. 决策或迭代：生成新算法/提示技术，继续测试和发布。
6. 输出：agent-authored research reports、改进的推理方法、benchmark 性能提升。

### 4.3 系统组件

- Agent 核心：LLM agent laboratories。
- 工具 / API / 数据库：AgentRxiv server、MATH-500、GPQA、MMLU-Pro、MedQA。
- 记忆或状态模块：共享报告库。
- 规划器：Agent Laboratory workflow。
- 评估器 / verifier：benchmark accuracy。
- 人类反馈或专家介入：人类提供初始研究方向和约束。
- 实验平台或仿真环境：推理 benchmark。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是。
- 仿真验证：否。
- 高通量计算：部分。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：MedQA 是医学 QA benchmark，不是临床数据验证。
- 真实场景部署：原型平台。
- 专家评估：未见主要专家评估。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：MATH-500、GPQA Diamond、MMLU-Pro、MedQA。
- 任务设置：Agent 发现 prompting / reasoning 方法，并通过共享研究报告逐代改进。
- 对比基线：无历史访问的 Agent、baseline gpt-4o mini zero-shot、多模型/多 benchmark 设置。
- 评价指标：accuracy improvement。
- 关键结果：MATH-500 从 70.2% 到 78.2%；跨 benchmark 平均 +3.3%；并行实验到 79.8%。
- 是否有消融实验：是，移除前序研究访问。
- 是否有失败案例或负结果：有，性能提升依赖可访问历史，且泛化幅度有限。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：发现新的 reasoning / prompting 方法，科学对象是 AI / 科研智能系统能力。
- 科学贡献是否经过验证：通过多个 benchmark 验证。
- 贡献强度判断：中。
- 科学贡献类型：系统平台 / 方法发现 / benchmark。
- 证据强度：benchmark。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：研究的是 Agent 科研过程的累积协作，而非单一模型性能。
- 与已有 Agent / 科研智能系统的区别：在 Agent Laboratory 等单体科研流水线之上增加共享记忆和协作平台。
- 与同一科学领域其他 Agent 文献的关系：可作为通用科研 Agent 从 individual lab 到 community collaboration 的代表。
- 主要创新点：agent-native preprint server；跨代研究报告复用；并行 Agent lab 协作。

## 7. 局限性与风险

- Agent 自主性不足：初始研究方向仍由人类给定。
- 科学验证不足：验证集中在推理 benchmark，不等同于真实自然科学发现。
- 泛化性不足：发现的 prompting 方法是否跨任务长期有效仍需更多验证。
- 工具链依赖：依赖 Agent Laboratory 和 archive 格式。
- 数据泄漏或 benchmark 偏差：公开 benchmark 容易被过拟合。
- 成本、可复现性或安全风险：多实验室并行可能放大错误发现和无效报告。

## 8. 对综述写作的价值

- 可放入哪个章节：通用科研 Agent；多 Agent 科研协作；科研知识生产机制。
- 可支撑哪个论点：Autonomous Scientific Discovery 的下一步不是单个 Agent，而是 Agent 之间的累积知识生态。
- 可用于哪个表格或图：Agent collaboration architecture；external memory/archive 对比表。
- 适合作为代表性案例吗：适合。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：PDF p.1 Fig.1；PDF Fig.3；结果 Fig.4-6。
- 需要与哪些论文并列比较：Agent Laboratory、AI Scientist、ResearchAgent、Robin、Dora。

## 9. 总结

### 9.1 一句话概括

Agent 科研共同体原型。

### 9.2 速记版 pipeline

1. 多个 Agent lab 接收共同研究方向。
2. 生成研究报告并上传 AgentRxiv。
3. 后续 Agent 检索前序报告。
4. 基于前序发现改进方法。
5. 在 benchmark 上验证累积提升。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01 形式、信息与计算科学
二级类：01.04 科研智能系统与 Autonomous Scientific Discovery
三级类：01.04.04 / 01.04.05
四级专题：General scientific research-agent systems
Agent 类型：LLM Agent；Planning Agent；Tool-using Agent；Retrieval-augmented Agent；Multi-Agent System；Human-in-the-loop Agent；Hybrid Agent
科研流程角色：文献检索与阅读；知识抽取与组织；假设生成；实验设计；工具调用与代码执行；数据分析；结果解释；证据评估与验证；论文写作
自主能力：任务分解；计划生成；工具调用；记忆与状态维护；反馈迭代；自主决策；多 Agent 协作
验证方式：benchmark
交叉属性：计算驱动；数据驱动；科研报告 archive
科学贡献类型：系统平台；方法发现；benchmark
证据强度：全文 PDF 高
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
