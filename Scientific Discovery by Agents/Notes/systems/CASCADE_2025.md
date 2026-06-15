# CASCADE 2025

## 基本信息
- **论文**: CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution
- **作者**: Xu Huang, Junwu Chen, Yuxing Fei, Zhuohan Li, Philippe Schwaller, Gerbrand Ceder
- **年份**: 2025
- **来源**: arXiv:2512.23880
- **关键词**: skill-evolution, scientific-agents, materials-science, chemistry, self-evolving-agent

## 核心思想
CASCADE 关注科学智能体对固定工具和脆弱工具生成的依赖。作者认为科学 agent 不应只调用预设工具，而应能够通过持续学习和自我反思形成可复用、可共享的 executable skills。

## 方法细节
CASCADE 通过 web search、code extraction、introspection 和 knowledge graph exploration 等 meta-skills，帮助 agent 学会外部工具并把知识固化为可复用技能。系统强调 memory consolidation、人机协作和技能共享，使 agentic harness 可以随任务经验持续演化。

## 关键结果
论文在 SciSkillBench 的 116 个材料科学和化学研究任务上评估，报告 GPT-5 配合 CASCADE 达到 93.3% success rate，而无演化机制时为 35.4%。作者还展示了计算分析、自主实验和论文复现应用。

## 局限性
CASCADE 的核心是 skill / harness evolution，不是完整的科学发现闭环。它更适合作为多智能体科研工作流的基础设施支撑，而不是单独作为严格 ASD 系统。

## 核心贡献
CASCADE 的核心贡献是将科学 agent 的能力增长从一次性工具调用推进到累计式技能创造和演化。

## 与综述的关联
该工作适合放入 `X0-Y5-Z1/Z3/Z4/Z5/Z7/Z8`。它是 harness / capability evolution 的关键支撑，可与 STELLA、SciToolAgent、EvoScientist 和 Science Earth 对照。

## 原文核对与分类复核
- **原文核对**：原文提出 Cumulative Agentic Skill Creation through Autonomous Development and Evolution，强调从 LLM + tool use 走向 LLM + skill acquisition。
- **机制判断**：它通过 continuous learning、web search、code extraction、memory utilization 和 self-reflection 形成可复用技能。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y5` 正确；`Z1,Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合支撑 skills / harness evolution，但不应作为多智能体主案例。

## 深读补充（按 MARS 标准）

### 研究问题
CASCADE 关注 LLM agents 依赖预定义工具、难以持续适应复杂科学任务的问题。

### 系统架构 / 工作流
系统通过 continuous learning 和 self-reflection 两类 meta-skills 让 agent 学习外部工具、提取代码、使用记忆、探索知识图谱，并将经验固化为可复用 skill。

### 关键机制
核心是 cumulative agentic skill creation。演化对象是技能、工具使用方式和任务解决 harness，而不是单个科学发现结果。

### 实验验证与证据
原文在 SciSkillBench 的材料科学和化学任务上评估，报告 evolution mechanisms 显著提高任务成功率。

### 局限性补充
它是科学 agent 技能基础设施，不是完整 ASD 系统。技能生成质量、错误技能污染和安全边界需要独立治理。

### XYZ 分类逐项解释
- `X0`：不是显式多智能体。
- `Y5`：skill / harness evolution 是核心。
- `Z1,Z3,Z4,Z5,Z7,Z8`：覆盖知识、工具/方案、执行、分析、验证和迭代。

### 综述写作用法
适合第 8 章基础设施，也支撑第 5 章 harness evolution。
