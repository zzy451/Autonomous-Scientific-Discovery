# IMPROVE 2025

## 基本信息
- **论文**: IMPROVE: Iterative Model Pipeline Refinement and Optimization Leveraging LLM Experts
- **作者**: Eric Xue, Zeyi Huang, Yuyang Ji, Haohan Wang
- **年份**: 2025
- **来源**: arXiv:2502.18530
- **关键词**: multi-agent, iterative-refinement, ML-pipeline, computer-vision

## 核心思想
IMPROVE 通过逐组件迭代改进来提高 LLM-driven ML pipeline 设计的稳定性和可解释性。

## 方法细节
系统将数据预处理、模型架构和训练配置等部分拆分给专门化 agent / 模块逐步优化。

## 关键结果
论文报告 IMPROVE 在多种视觉分类数据集和 Kaggle 任务上优于基线。

## 局限性
偏 ML 自动化，不是完整科学发现闭环。

## 核心贡献
提出 iterative refinement 作为 LLM-driven ML system 的协调策略。

## 与综述的关联
适合放入 `X2-Y1-Z3/Z4/Z5,Z7,Z8`。

## 原文核对与分类复核
- **原文核对**：原文标题为 Iterative Model Pipeline Refinement and Optimization Leveraging LLM Experts，核心是基于训练反馈逐组件优化 pipeline。
- **机制判断**：重点是 iterative refinement，而不是一次性生成完整 pipeline。
- **分类复核**：保持 `ASD 相关系统`；`X2` 可保留为 LLM experts / agent framework；`Y1` 正确；`Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：支撑“执行反馈驱动的 workflow refinement”。


## 深读补充（按 MARS 标准）

### 研究问题
IMPROVE 关注 LLM agents 一次性优化整个 ML pipeline 时难以定位改进来源、收敛不稳定的问题。

### 系统架构 / 工作流
系统使用 LLM experts 对 pipeline 组件进行逐步 refinement，而不是一次性重写全流程。

### 关键机制
核心是 iterative model pipeline refinement。每次只修改一个组件，并根据训练反馈更新 pipeline。

### 实验验证与证据
原文在不同规模和领域的数据集上评估 object classification pipelines，显示 iterative refinement 优于 zero-shot LLM baseline。

### 局限性补充
IMPROVE 是 ML pipeline 优化系统，不直接覆盖科学假设发现或真实实验验证。

### XYZ 分类逐项解释
- `X2`：LLM experts / agent framework。
- `Y1`：基于反馈的 iterative refinement。
- `Z3,Z4,Z5,Z7,Z8`：覆盖 pipeline 设计、执行、分析、验证和迭代。

### 综述写作用法
适合说明执行反馈如何驱动 workflow refinement。
