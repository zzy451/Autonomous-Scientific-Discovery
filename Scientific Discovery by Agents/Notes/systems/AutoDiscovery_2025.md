# AutoDiscovery 2025

## 基本信息
- **论文**: AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise
- **作者**: Dhruv Agarwal, Bodhisattwa Prasad Majumder, Reece Adamson, Megha Chakravorty, Satvika Reddy Gavireddy, Aditya Parashar, Harshit Surana, Bhavana Dalvi Mishra, Andrew McCallum, Ashish Sabharwal, Peter Clark
- **年份**: 2025
- **来源**: arXiv:2507.00310; NeurIPS 2025
- **关键词**: open-ended-ASD, Bayesian-surprise, MCTS, hypothesis-search

## 核心思想
AutoDiscovery 关注 ASD 中“系统自己知道问什么问题”的问题，用 Bayesian surprise 驱动开放式探索。

## 方法细节
系统用 MCTS 和 progressive widening 搜索 nested hypotheses，并以 surprisal 作为 reward。

## 关键结果
论文在 21 个真实数据集上产生更多被 LLM 和领域专家认为 surprising 的发现。

## 局限性
验证依赖数据驱动任务和专家评估，不覆盖物理实验。

## 核心贡献
把 open-ended ASD 建模为 surprise-guided hypothesis search。

## 与综述的关联
适合放入 `X0-Y3-Z2/Z4/Z5,Z7,Z8`。

## 原文核对与分类复核
- **原文核对**：原文明确提出 open-ended ASD，使用 Bayesian surprise 作为探索奖励，并用 MCTS with progressive widening 搜索 nested hypotheses。
- **机制判断**：该工作直接回应 ASD 不只是回答问题，还要知道该问什么问题。
- **分类复核**：保持 `严格 ASD`；`X0` 正确；`Y3` 正确；`Z2,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合作为“问题形成/开放式探索”维度的核心案例。

## 深读补充（按 MARS 标准）

### 研究问题
AutoDiscovery 关注 ASD 不应只是回答人类给定问题，还应能够决定哪些问题值得探索。

### 系统架构 / 工作流
系统使用 Bayesian surprise 作为探索奖励，并用 MCTS with progressive widening 在 nested hypothesis space 中搜索。

### 关键机制
核心是 open-ended exploration by epistemic shift。系统比较 LLM prior 和实验结果后的 posterior，用 surprise 衡量发现价值。

### 实验验证与证据
原文在 21 个真实数据集上评估，报告在固定预算下产生更多令 LLM 和领域专家感到 surprising 的 discoveries。

### 局限性补充
surprise 不等于科学重要性，且 LLM prior/posterior 可能受模型偏差影响。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y3`：MCTS 是核心。
- `Z2,Z4,Z5,Z7,Z8`：覆盖问题探索、执行、分析、验证和迭代。

### 综述写作用法
是 open-ended ASD 和 problem formulation 的核心案例。
