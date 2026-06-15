# LLM-SR 2024

## 基本信息
- **论文**: LLM-SR: Scientific Equation Discovery via Programming with Large Language Models
- **作者**: Parshin Shojaee, Kazem Meidani, Shashank Gupta, Amir Barati Farimani, Chandan K. Reddy
- **年份**: 2024
- **来源**: arXiv:2404.18400; ICLR 2025
- **关键词**: equation-discovery, symbolic-regression, evolutionary-search, program-search

## 核心思想
LLM-SR 使用 LLM 的科学先验和代码能力来发现科学方程。

## 方法细节
系统将方程表示为程序 skeleton，由 LLM 提出结构，再通过演化搜索和数据拟合优化参数。

## 关键结果
论文在多个科学领域发现具有物理准确性的方程，优于传统 symbolic regression baseline。

## 局限性
不是多智能体系统，主要覆盖 equation discovery。

## 核心贡献
把科学方程发现转化为 LLM-guided evolutionary program search。

## 与综述的关联
适合放入 `X0-Y4-Z3/Z4/Z5,Z7,Z8`，支撑 artifact-level evolution。

## 原文核对与分类复核
- **原文核对**：原文关注 scientific equation discovery via programming with LLMs；本地笔记进一步记录其将方程表示为程序 skeleton，并结合搜索/拟合。
- **机制判断**：该工作是科学方程这个 artifact 的搜索和优化，不是多智能体系统。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y4` 可保留为 evolutionary / program search；`Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：支撑 scientific artifact evolution，尤其是 equation / symbolic artifact。

## 深读补充（按 MARS 标准）

### 研究问题
LLM-SR 关注科学方程发现中传统 symbolic regression 搜索空间大、缺少科学先验的问题。

### 系统架构 / 工作流
系统把方程发现表示为 programming task：LLM 生成程序/方程结构，搜索和拟合机制进一步优化候选方程。

### 关键机制
核心是 LLM-guided program / evolutionary search。科学产物是可执行、可拟合、可评估的方程程序。

### 实验验证与证据
原文在多个科学领域的方程发现任务中展示优于传统 symbolic regression baseline。

### 局限性补充
系统不是多智能体，也主要适用于可由数据拟合和方程形式表达的科学问题。

### XYZ 分类逐项解释
- `X0`：单 agent / 非显式多智能体。
- `Y4`：演化/程序搜索用于优化方程 artifact。
- `Z3,Z4,Z5,Z7,Z8`：覆盖公式设计、执行、分析、验证和迭代。

### 综述写作用法
适合 artifact evolution 中的 equation / symbolic law discovery。
