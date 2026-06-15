# MLZero 2025

## 基本信息
- **论文**: MLZero: A Multi-Agent System for End-to-end Machine Learning Automation
- **作者**: Haoyang Fang 等
- **年份**: 2025
- **来源**: arXiv:2505.13941
- **关键词**: multi-agent, AutoML, ML-engineering, memory

## 核心思想
MLZero 使用多智能体框架自动化多模态机器学习任务，从原始输入到高质量 ML solution。

## 方法细节
系统使用 cognitive perception、semantic memory 和 episodic memory 支撑代码生成、调试和迭代。

## 关键结果
论文报告 MLZero 在 MLE-Bench Lite 和 multimodal AutoML benchmark 上优于竞争方法。

## 局限性
偏 ML engineering，不直接覆盖科学假设验证。

## 核心贡献
展示多智能体、记忆和端到端 ML 自动化的结合。

## 与综述的关联
适合放入 `X2-Y5-Z3/Z4/Z5/Z7,Z8`，作为 computational discovery harness 证据。

## 原文核对与分类复核
- **原文核对**：本地笔记和题名显示其为 end-to-end machine learning automation 的 multi-agent system，强调 semantic / episodic memory。
- **机制判断**：它更接近 ML 自动化 harness，而不是直接面向某个自然科学问题的完整 ASD。
- **分类复核**：保持 `ASD 相关系统`；`X2` 正确；`Y5` 正确，因为 memory / automation harness 是核心；`Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：作为 harness evolution 和 ML research automation 的支撑材料。

## 深读补充（按 MARS 标准）

### 研究问题
MLZero 面向 end-to-end machine learning automation，关注如何让多个 agents 自动完成数据理解、模型构建、训练和评估。

### 系统架构 / 工作流
系统是 multi-agent AutoML framework，并结合 semantic / episodic memory 保存任务经验和解决策略。

### 关键机制
核心是 memory-enhanced multi-agent automation。记忆让系统能够复用过去经验并改进后续 pipeline。

### 实验验证与证据
原文在 ML 自动化任务上评估 end-to-end pipeline 生成和执行表现。

### 局限性补充
MLZero 支撑 ML research / engineering，不直接处理自然科学假设、实验和因果解释。

### XYZ 分类逐项解释
- `X2`：多智能体 AutoML。
- `Y5`：semantic / episodic memory 属于 harness evolution。
- `Z3,Z4,Z5,Z7,Z8`：覆盖 pipeline 设计、执行、分析、验证和迭代。

### 综述写作用法
适合说明 memory / harness evolution 在自动 ML 科研中的作用。
