# SR-Scientist 2026

## 基本信息
- **论文**: SR-Scientist: Scientific Equation Discovery With Agentic AI
- **作者**: Shijie Xia, Yuhan Sun, Pengfei Liu
- **年份**: 2026
- **来源**: OpenReview; ICLR 2026 poster
- **关键词**: equation-discovery, agentic-AI, symbolic-regression, tool-use

## 核心思想
SR-Scientist 将 scientific equation discovery 组织为长周期、工具驱动的数据分析和方程评估 agent workflow。

## 方法细节
系统结合 autonomous agent、data analyzer、equation evaluator 和 RL-style training strategy。

## 关键结果
论文提出了可训练的 agentic symbolic regression framework。

## 局限性
任务范围主要是 symbolic regression。

## 核心贡献
展示 equation discovery 可以被构造为 tool-driven scientific agent。

## 与综述的关联
适合放入 `X0-Y1-Z3/Z4/Z5/Z7/Z8`，支撑 agentic equation discovery 中的执行反馈和反思修正。

## 原文核对与分类复核
- **原文核对**：OpenReview 题名为 Scientific Equation Discovery With Agentic AI，重点在 agentic AI 辅助科学方程发现。
- **机制判断**：该系统更适合作为 reflective / feedback-driven equation discovery，而不是明确 tree search。
- **分类复核**：已从 `Y3` 修正为 `Y1`；`X0` 和 `Z3,Z4,Z5,Z7,Z8` 保持。
- **写作用途**：适合放在方程发现和执行反馈修正，不作为 MCTS/tree-search 主证据。

## 深读补充（按 MARS 标准）

### 研究问题
SR-Scientist 关注用 agentic AI 做 scientific equation discovery，即让系统通过数据分析、候选公式实现和反馈修正发现科学规律。

### 系统架构 / 工作流
系统围绕 symbolic regression workflow 组织 LLM / tools，对候选表达式进行生成、执行、评估和修订。

### 关键机制
核心是 agentic feedback loop。它更像执行反馈驱动的反思修正，而不是明确 tree search。

### 实验验证与证据
原文在科学方程发现任务上评估系统发现规律的能力。

### 局限性补充
系统主要限于 symbolic regression 类任务，难以覆盖复杂机制发现和真实实验。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y1`：反馈修正是核心。
- `Z3,Z4,Z5,Z7,Z8`：覆盖公式设计、执行、分析、验证和迭代。

### 综述写作用法
适合 equation discovery 小节，与 LLM-SR、DrSR、EvoSLD 对照。
