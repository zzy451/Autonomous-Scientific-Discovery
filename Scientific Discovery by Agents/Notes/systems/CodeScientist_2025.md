# CodeScientist 2025

## 基本信息
- **论文**: CodeScientist: End-to-End Semi-Automated Scientific Discovery with Code-based Experimentation
- **作者**: Peter Jansen, Oyvind Tafjord, Marissa Radensky, Pao Siangliulue, Tom Hope, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Daniel S. Weld, Peter Clark
- **年份**: 2025
- **来源**: arXiv:2503.22708; ACL Findings 2025
- **关键词**: ASD, code-based-experimentation, genetic-search, replication

## 核心思想
CodeScientist 将代码实验作为科学发现核心产物，使用遗传搜索组合文献和代码块来生成研究想法和实验。

## 方法细节
系统对研究文章和 codeblocks 进行 genetic search，自动构建、运行、分析实验，并进行外部 review、code review 和 replication attempts。

## 关键结果
论文报告系统产生 19 个 potential discoveries，其中 6 个被判断为至少 minimally sound 和 incrementally novel。

## 局限性
主要限于可用代码表达的 agent / virtual environment 领域。

## 核心贡献
把 ASD 从论文生成推进到代码实验、复现和多面验证。

## 与综述的关联
适合放入 `X0-Y4-Z1/Z2/Z3/Z4/Z5/Z6/Z7/Z8`，是 artifact evolution 的核心案例。

## 原文核对与分类复核
- **原文核对**：原文明确自称面向 ASD of software artifacts，并将 ideation 与 experiment construction 建模为 genetic search over research articles and codeblocks。
- **机制判断**：系统自动开展数百个代码实验，并使用 external review、code review、replication attempts 进行多面验证。
- **分类复核**：保持 `严格 ASD`；`X0` 正确，原文主要不是多智能体组织；`Y4` 正确，genetic search 是核心；`Z1-Z8` 全流程标签成立。
- **写作用途**：这是 artifact-level evolution 的核心案例，特别适合对比 AI Scientist 的 paper generation。

## 深读补充（按 MARS 标准）

### 研究问题
CodeScientist 针对 ASD of software artifacts 的两个局限：设计空间过窄，以及自动生成论文/代码常只接受 conference-style review，缺少对代码和复现实验的深入评估。

### 系统架构 / 工作流
系统把 ideation 和 experiment construction 建模为 genetic search over research articles and codeblocks。它自动构造、运行和分析大量代码实验。

### 关键机制
核心是 code-based experimentation 与 genetic search。科学产物不是文本论文，而是可以执行、审查和复现的代码实验。

### 实验验证与证据
原文执行数百个自动实验，返回 19 个 discoveries，其中 6 个被判断为至少 minimally sound 且 incrementally novel，并经过 external review、code review 和 replication attempts。

### 局限性补充
当前主要局限在 agents / virtual environments 等可用代码表达的领域。发现质量仍依赖评价协议和代码块库。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y4`：genetic search 是核心机制。
- `Z1-Z8`：覆盖文献、想法、实验构造、执行、分析、报告、验证和迭代。

### 综述写作用法
是 artifact-level evolution 的核心案例，可与 AI Scientist、AlphaEvolve、ERA 对比。
