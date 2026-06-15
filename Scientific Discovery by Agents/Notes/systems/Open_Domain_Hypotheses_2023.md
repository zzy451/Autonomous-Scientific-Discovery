# Open-Domain Hypotheses 2023

## 基本信息
- **论文**: Large Language Models for Automated Open-domain Scientific Hypotheses Discovery
- **作者**: Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, Erik Cambria
- **年份**: 2023
- **来源**: arXiv:2309.02726
- **关键词**: open-domain, hypothesis-generation, social-science, feedback

## 核心思想
该工作研究 LLM 是否能从开放语料中生成新颖且有效的科学假设。

## 方法细节
系统包含多模块 pipeline 和反馈机制，用于从 raw web corpus 中提出社会科学假设。

## 关键结果
论文通过 GPT-4 和专家评估展示了 LLM 生成开放域科学假设的可行性。

## 局限性
不是多智能体系统，且缺少实验执行闭环。

## 核心贡献
较早把 open-domain scientific hypothesis discovery 作为可评估任务提出。

## 与综述的关联
适合放入 `X0-Y1-Z1/Z2/Z7`，作为早期 hypothesis generation 系统。

## 原文核对与分类复核
- **原文核对**：原文提出开放域社会科学假设发现数据集和 multi-module framework，并使用 feedback mechanisms 提升假设质量。
- **机制判断**：它是较早的开放域 hypothesis discovery 工作，覆盖 observation -> hypothesis，但不构成完整 ASD 闭环。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y1` 正确，因为核心有反馈机制；`Z1,Z2,Z7` 正确。
- **写作用途**：可作为早期 open-domain hypothesis generation 背景案例。

## 深读补充（按 MARS 标准）

### 研究问题
该工作关注开放域科学假设发现：给定原始 web corpus，系统是否能生成 valid、novel、helpful 的科学假设，而不是只在封闭数据集上做 commonsense induction。

### 系统架构 / 工作流
系统构建社会科学开放域假设发现数据集，并设计 multi-module framework，通过不同 feedback mechanisms 提升假设质量。

### 关键机制
核心是 open-domain observation -> hypothesis generation，以及基于反馈的修正。

### 实验验证与证据
原文使用 GPT-4 评估和专家评估，声称系统能生成文献中不存在但反映现实的科学假设。

### 局限性补充
领域集中在社会科学；假设有效性主要来自专家/模型评估，缺少后续实验闭环。

### XYZ 分类逐项解释
- `X0`：multi-module 但非显式多智能体。
- `Y1`：feedback mechanisms 支撑修正。
- `Z1,Z2,Z7`：覆盖开放域证据、假设生成和评价。

### 综述写作用法
适合作为早期 open-domain hypothesis discovery 背景案例。
