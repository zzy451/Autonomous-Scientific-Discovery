# GenoMAS 2025

## 基本信息
- **论文**: GenoMAS: A Multi-Agent Framework for Scientific Discovery via Code-Driven Gene Expression Analysis
- **作者**: Haoyang Liu, Yijiang Li, Haohan Wang
- **年份**: 2025
- **来源**: arXiv:2507.21035
- **关键词**: gene-expression, multi-agent, code-driven-analysis, biomedical-discovery

## 核心思想
GenoMAS 用多智能体协作分析基因表达数据，目标是从复杂转录组数据中发现基因-表型关联。

## 方法细节
系统通过六个专门化 agents、typed message passing 和 shared analytic canvas 生成、执行、修正和验证代码。

## 关键结果
论文报告 GenoMAS 在 GenoTEX benchmark 上提高数据预处理和基因识别表现，并输出文献支持的生物学关联。

## 局限性
主要覆盖 gene expression analysis，不是通用 ASD 系统。

## 核心贡献
展示多智能体可以作为 code-driven biomedical discovery harness。

## 与综述的关联
适合放入 `X2-Y1-Z1/Z3/Z4/Z5/Z7,Z8`，支撑生物医学多智能体分析。

## 原文核对与分类复核
- **原文核对**：原文提出 six specialized LLM agents、typed message-passing protocols、shared analytic canvas，并允许 advance / revise / bypass / backtrack。
- **机制判断**：它是面向 gene expression analysis 的多智能体代码驱动发现框架，重点在结构化 workflow 和可回退规划。
- **分类复核**：保持 `ASD 相关系统`；`X2` 正确；`Y1` 正确，因为包含 revise/backtrack；`Z1,Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合说明多智能体交接、共享画布和 typed message passing。

## 深读补充（按 MARS 标准）

### 研究问题
GenoMAS 关注 gene expression analysis 中数据复杂、文件半结构化、领域知识要求高的问题。完全自由 agent 容易不够精确，固定流程又不够灵活。

### 系统架构 / 工作流
系统组织六个 specialized LLM agents，通过 typed message-passing protocols 和 shared analytic canvas 协作。编程 agents 将任务指南展开成 Action Units。

### 关键机制
核心是 guided planning、typed handoff 和 advance/revise/bypass/backtrack 控制。它在结构化流程和 agent 灵活性之间折中。

### 实验验证与证据
原文在 GenoTEX benchmark 上报告数据预处理和基因识别指标优于 prior art，并能提出文献支持的 gene-phenotype associations。

### 局限性补充
它主要是 gene expression analysis 系统，不覆盖真实实验干预或湿实验验证。

### XYZ 分类逐项解释
- `X2`：六个 specialized agents。
- `Y1`：revise/backtrack 支撑反馈修正。
- `Z1,Z3,Z4,Z5,Z7,Z8`：覆盖知识、代码/分析设计、执行、结果、验证和迭代。

### 综述写作用法
适合说明多智能体交接、typed protocols 和 shared canvas 在科学分析中的价值。
