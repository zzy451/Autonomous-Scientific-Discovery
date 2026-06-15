# MASTER 2025

## 基本信息
- **论文**: Hierarchical Multi-agent Large Language Model Reasoning for Autonomous Functional Materials Discovery
- **作者**: Samuel Rothfarb, Megan C. Davis, Ivana Matanovic, Baikun Li, Edward F. Holby, Wilton J. M. Kort-Kamp
- **年份**: 2025
- **来源**: arXiv:2512.13930
- **关键词**: materials-discovery, hierarchical-multi-agent, atomistic-simulation, active-learning, scientific-reasoning

## 核心思想
MASTER 关注材料发现中的科学推理问题。许多自动化方法只是在大空间中盲目采样或执行程序任务，而 MASTER 试图让 LLM reasoning agents 指导 atomistic simulation 的选择、执行和解释。

## 方法细节
MASTER 是一个 active learning framework，系统将自然语言目标转化为 density functional theory workflows，并用高层 reasoning agents 指导发现过程。论文比较 single agent baseline 和三种 multi-agent approaches：peer review、triage-ranking 和 triage-forms。

## 关键结果
在两个化学应用中，reasoning-driven exploration 相比 trial-and-error selection 将所需 atomistic simulations 减少最多 90%。论文还分析 reasoning trajectories，显示系统产生了化学上合理的决策。

## 局限性
MASTER 的验证主要在 atomistic simulation 环境中完成，不等同于完整物理实验室发现。多智能体设置的泛化能力和长期记忆机制仍需进一步验证。

## 核心贡献
MASTER 的核心贡献是把 hierarchical multi-agent reasoning 引入 functional materials discovery，并将 reasoning、simulation 和 candidate selection 连接起来。

## 与综述的关联
该工作适合放入 `X4-Y2-Z2/Z3/Z4/Z5/Z7/Z8`，属于严格 ASD 候选。它补强层级式多智能体在科学仿真发现中的作用。

## 原文核对与分类复核
- **原文核对**：原文提出 MASTER，即 Materials Agents for Simulation and Theory in Electronic-structure Reasoning，使用层级 reasoning agents 设计、执行和解释 atomistic simulations。
- **机制判断**：其多 agent approaches 包括 peer review、triage-ranking 和 triage-forms，用于引导 functional materials discovery。
- **分类复核**：保持 `严格 ASD`；`X4` 正确；`Y2` 正确，因为有候选 triage/ranking；`Z2,Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合说明 hierarchical multi-agent reasoning 如何嵌入仿真发现。

## 深读补充（按 MARS 标准）

### 研究问题
MASTER 关注 functional materials discovery 中自动系统缺少科学推理、难以自主设计和解释 atomistic simulations 的问题。

### 系统架构 / 工作流
系统把自然语言目标转成 DFT workflows，并由 higher-level reasoning agents 通过 hierarchy of strategies 指导发现。策略包括 single-agent baseline、peer review、triage-ranking 和 triage-forms 等多 agent approaches。

### 关键机制
核心是 hierarchical multi-agent reasoning 与 simulation execution。Agents 不只是生成文本，而是指导仿真设计、执行和解释。

### 实验验证与证据
原文在 CO adsorption / functional materials 场景评估系统，比较不同 agent reasoning strategies。

### 局限性补充
系统依赖 DFT workflow 质量、仿真成本和材料任务定义。形式上仍需人类专家判断物理意义。

### XYZ 分类逐项解释
- `X4`：层级 reasoning agents 指导 worker-level simulation。
- `Y2`：triage-ranking 和候选比较支撑候选筛选。
- `Z2,Z3,Z4,Z5,Z7,Z8`：覆盖问题、仿真设计、执行、分析、验证和迭代。

### 综述写作用法
适合说明 hierarchical coordination 如何进入 simulation-based ASD。
