# KompeteAI 2025

## 基本信息
- **论文**: KompeteAI: Accelerated Autonomous Multi-Agent System for End-to-End Pipeline Generation for Machine Learning Problems
- **作者**: Stepan Kulibaba, Artem Dzhalilov, Roman Pakhomov, Oleg Svidchenko, Alexander Gasnikov, Aleksei Shpilman
- **年份**: 2025
- **来源**: arXiv:2508.10177
- **关键词**: multi-agent, ML-pipeline, AutoML, pipeline-generation

## 核心思想
KompeteAI 面向机器学习问题的 end-to-end pipeline generation。

## 方法细节
系统用多智能体组织数据理解、特征处理、模型选择和实验优化等任务。

## 关键结果
论文展示了 autonomous multi-agent pipeline generation 的可行性。

## 局限性
主要面向 ML pipeline，不直接处理科学发现中的因果解释和实验验证。

## 核心贡献
补充多智能体在 ML 自动建模和 pipeline synthesis 中的证据。

## 与综述的关联
适合放入 `X2-Y3-Z3/Z4/Z5/Z7`，支撑多智能体 pipeline 生成中的 MCTS / trajectory search。

## 原文核对与分类复核
- **原文核对**：原文标题和摘要明确是 autonomous multi-agent pipeline generation，并包含 MCTS、dynamic solution-space exploration、candidate merging、RAG 和 accelerated debugging。
- **机制判断**：它不是简单候选筛选，而是多智能体 + MCTS 的 ML pipeline 搜索系统。
- **分类复核**：已从 `Y2` 修正为 `Y3`；`X2` 保持；`Z3,Z4,Z5,Z7` 保持。
- **写作用途**：可作为多智能体和 trajectory search 结合的代码/ML pipeline 案例。

## 深读补充（按 MARS 标准）

### 研究问题
KompeteAI 关注 ML pipeline generation 中探索空间大、完整执行昂贵、候选方案组合困难的问题。

### 系统架构 / 工作流
系统是 autonomous multi-agent pipeline generation framework，结合 MCTS、RAG、candidate merging、predictive scoring 和 accelerated debugging。

### 关键机制
核心是 MCTS-based dynamic solution-space exploration。它不是简单生成多个 pipeline，而是在搜索树中生成、合并、评估和调试候选方案。

### 实验验证与证据
原文在 MLE-Bench 和 Kompete-bench 上报告优于 RD-agent、AIDE、Ml-Master 等方法。

### 局限性补充
该系统主要面向 ML pipeline，不直接保证科学发现的新颖性或因果有效性。

### XYZ 分类逐项解释
- `X2`：多 agent pipeline generation。
- `Y3`：MCTS 和 trajectory exploration 是核心。
- `Z3,Z4,Z5,Z7`：覆盖 pipeline 设计、执行、分析和验证。

### 综述写作用法
适合说明多智能体和 trajectory search 可以结合在代码/ML pipeline 层。
