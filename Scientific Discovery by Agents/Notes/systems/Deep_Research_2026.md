# Deep Research 2026

## 基本信息
- **论文**: Rethinking the AI Scientist: Interactive Multi-Agent Workflows for Scientific Discovery
- **作者**: Lukas Weidener, Marko Brkic, Mihailo Jovanovic, Ritvik Singh, Chiara Baccin, Emre Ulgac, Alex Dobrin, Aakaash Meduri
- **年份**: 2026
- **来源**: arXiv:2601.12542
- **关键词**: multi-agent, scientific-discovery, interactive-workflow, persistent-world-state, computational-biology

## 核心思想
这篇论文关注现有 AI scientist 系统的一个限制：很多系统以批处理方式运行，研究者难以在研究循环中实时引导系统。作者提出 Deep Research，将科学调查组织成可交互的多智能体工作流，使研究者可以在几分钟级别的周期内参与和修正系统方向。

## 方法细节
Deep Research 包含 planning、data analysis、literature search、novelty detection 等专门化 agents，并通过 persistent world state 维护跨轮研究上下文。系统支持 semi-autonomous mode 和 fully autonomous mode，前者允许人类在关键节点介入，后者支持较长周期的自动探索。

## 关键结果
论文在 BixBench computational biology benchmark 上评估系统，报告 open response accuracy 达到 48.8%，multiple-choice accuracy 达到 64.5%，相对已有基线有明显提升。

## 局限性
Deep Research 更像交互式科学调查系统，而不是已经完成真实实验验证的端到端发现系统。它强在多智能体组织、快速迭代和研究者参与，但科学产物是否能形成真实发现仍依赖后续验证。

## 核心贡献
Deep Research 的核心贡献是将 AI scientist 从长时间批处理 pipeline 推向 interactive multi-agent scientific workflow。

## 与综述的关联
该工作适合放入 `X2-Y5-Z1/Z2/Z3/Z4/Z5/Z7/Z8`。它补强固定角色多智能体、persistent world state、人类检查点和长周期工作流，是连接 Agent Laboratory、Kosmos 和 EvoScientist 的重要材料。

## 原文核对与分类复核
- **原文核对**：原文提出 Deep Research，一个 interactive multi-agent scientific investigation system，由 planning、data analysis、literature search、novelty detection agents 与 persistent world state 组成。
- **机制判断**：它强调分钟级交互式科学调查、semi-autonomous / fully autonomous 两种模式，以及跨迭代保持 context。
- **分类复核**：保持 `ASD 相关系统`；`X2` 正确；`Y5` 正确，因为 persistent world state 支撑 workflow/harness evolution；`Z1,Z2,Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合说明 AI Scientist 从 batch pipeline 转向 interactive workflow。

## 深读补充（按 MARS 标准）

### 研究问题
Deep Research 反思 AI Scientist 的 batch-processing 形态，认为现有系统往往周期长、交互性弱，不利于研究者实时指导科学探索。

### 系统架构 / 工作流
系统由 planning、data analysis、literature search、novelty detection agents 组成，并通过 persistent world state 维持跨轮次上下文。系统支持 semi-autonomous 和 fully autonomous 两种模式。

### 关键机制
核心机制是 interactive multi-agent workflow 和 persistent world state。它把 AI scientist 从一次性 pipeline 推向可交互、可持续的研究工作台。

### 实验验证与证据
原文在 scientific investigation 场景评估系统，强调分钟级 turnaround 和跨迭代状态保持。

### 局限性补充
交互式系统对状态管理、用户检查点和错误积累更敏感。它更像 ASD workbench，而不是单个领域发现系统。

### XYZ 分类逐项解释
- `X2`：多个专门 agents。
- `Y5`：persistent world state 和 workflow continuity 属于 harness evolution。
- `Z1,Z2,Z3,Z4,Z5,Z7,Z8`：覆盖科学调查的多个阶段。

### 综述写作用法
适合说明 AI Scientist 正从离线 pipeline 走向 interactive multi-agent workflow。
