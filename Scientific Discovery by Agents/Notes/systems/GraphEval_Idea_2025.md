# GraphEval Idea 2025

## 基本信息
- **论文**: GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation
- **作者**: Tao Feng, Yihang Sun, Jiaxuan You
- **年份**: 2025
- **来源**: arXiv:2503.12600; ICLR 2025
- **关键词**: idea-evaluation, graph-based-evaluation, novelty-detection

## 核心思想
GraphEval 将复杂研究想法分解为 viewpoint graph，以提升 idea evaluation 的稳定性。

## 方法细节
系统用小模型抽取 viewpoint nodes，再构建图并通过 label propagation 或 GNN 传播评价信号。

## 关键结果
论文报告 GraphEval 在两个数据集上至少提升 14% F1，并能检测 plagiarized ideas。

## 局限性
只评估想法，不生成或执行科学实验。

## 核心贡献
为科学 idea evaluation 提供结构化图表示。

## 与综述的关联
适合放入 `X0-Y2-Z2,Z7`。

## 原文核对与分类复核
- **原文核对**：原文提出 lightweight graph-based LLM framework for idea evaluation。
- **机制判断**：它支撑候选科学想法评价，而不是完整 ASD。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y2` 正确；`Z2,Z7` 正确。
- **写作用途**：适合放在 idea evaluation / candidate selection 小节。

## 深读补充（按 MARS 标准）

### 研究问题
GraphEval 关注 scientific idea evaluation 缺少轻量、结构化和可解释评估框架的问题。

### 系统架构 / 工作流
系统用 graph-based LLM framework 对 idea 进行结构化评价，帮助判断候选想法质量。

### 关键机制
核心是 graph-structured evaluation。它支撑候选筛选，而不是生成完整研究闭环。

### 实验验证与证据
原文在 idea evaluation 任务上评估框架有效性，作为 idea generation 系统的评价补充。

### 局限性补充
GraphEval 评价的是想法，不保证实验可行性和真实发现价值。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y2`：候选 idea evaluation。
- `Z2,Z7`：覆盖想法和验证/评价。

### 综述写作用法
适合第 7 章评价指标，也可放在 candidate selection 支撑材料。
