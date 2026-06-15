# EvoSLD 2025

## 基本信息
- **论文**: Can Language Models Discover Scaling Laws?
- **作者**: Haowei Lin, Xiangyu Wang, Jianzhu Ma, Yitao Liang
- **年份**: 2025
- **来源**: arXiv:2507.21184
- **关键词**: scaling-law, evolutionary-search, symbolic-expression, AI-research

## 核心思想
EvoSLD 用 LLM-guided evolutionary algorithms 自动发现神经网络 scaling laws。

## 方法细节
系统共同演化 symbolic expressions 和 optimization routines，寻找简洁且可泛化的函数形式。

## 关键结果
论文在多个 scaling law 场景中重新发现或超越人类提出的规律。

## 局限性
聚焦 AI research 中的 scaling law discovery。

## 核心贡献
将 scaling law discovery 建模为 LLM-guided evolutionary scientific artifact search。

## 与综述的关联
适合放入 `X0-Y4-Z3/Z4/Z5,Z7,Z8`。

## 原文核对与分类复核
- **原文核对**：arXiv 标题为 Can Language Models Discover Scaling Laws?；本地笔记中的 EvoSLD 是方法/系统名称，用于 neural scaling law discovery。
- **机制判断**：核心是 LLM 引导的 scaling-law artifact 搜索/优化。
- **分类复核**：保持 `严格 ASD` 候选；`X0` 正确；`Y4` 正确；`Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：支撑可执行/可评估 scientific law artifact 的演化发现。


## 深读补充（按 MARS 标准）

### 研究问题
EvoSLD / Can Language Models Discover Scaling Laws? 关注神经网络 scaling laws 是否可以由 LLM 自动发现，而不是由人类手工提出函数形式。

### 系统架构 / 工作流
系统使用 LLM-guided evolutionary process 生成和优化 symbolic expressions / scaling law candidates，并通过数据拟合和评价选择更好的规律。

### 关键机制
核心是 scaling-law artifact evolution。候选函数形式被生成、变异、评估和选择。

### 实验验证与证据
原文在 neural scaling law 场景中重新发现或改进 scaling laws，展示 LLM 对科学规律搜索的作用。

### 局限性补充
领域集中在 AI/ML scaling laws；评价依赖数据拟合和泛化指标，科学解释仍需专家判断。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y4`：演化式优化是核心。
- `Z3,Z4,Z5,Z7,Z8`：覆盖规律设计、执行评估、分析、验证和迭代。

### 综述写作用法
适合说明 scientific laws 也可以作为演化搜索对象。
