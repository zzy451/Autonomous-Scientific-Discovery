# Scideator 2024

## 基本信息
- **论文**: Human-LLM Compound System for Scientific Ideation through Facet Recombination and Novelty Evaluation
- **作者**: Marissa Radensky, Simra Shahid, Raymond Fok, Pao Siangliulue, Tom Hope, Daniel S. Weld
- **年份**: 2024
- **来源**: arXiv:2409.14634
- **关键词**: scientific-ideation, human-LLM, facet-recombination, novelty-checking

## 核心思想
Scideator 用论文 facets 的重组支持人类和 LLM 共同生成科学想法。

## 方法细节
系统包含 facet finder、faceted idea generator、novelty checker 和 novelty iterator。

## 关键结果
用户研究显示研究者使用 Scideator 能识别更多有趣想法。

## 局限性
人类主导较强，不是 autonomous discovery。

## 核心贡献
把 scientific ideation 表示为可组合、可检查的 facet recombination。

## 与综述的关联
适合放入 `X0-Y2-Z1/Z2,Z7`，支撑 artifact handoff 和 novelty checking。

## 原文核对与分类复核
- **原文核对**：arXiv 标题为 Human-LLM Compound System for Scientific Ideation through Facet Recombination and Novelty Evaluation；Scideator 是系统名称。
- **机制判断**：核心是 human-in-the-loop facet recombination、analogous paper retrieval 和 novelty checking。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确，因为它是人机复合系统而非多 agent；`Y2` 正确；`Z1,Z2,Z7` 正确。
- **写作用途**：适合作为 scientific ideation / novelty evaluation 的人机系统案例。


## 深读补充（按 MARS 标准）

### 研究问题
Scideator 关注科学创意往往来自不同论文 facet 的重组，但普通 LLM 生成难以支持可控、可追踪的人机创意过程。

### 系统架构 / 工作流
系统包含 facet extraction、analogous paper facet finding、faceted idea generator 和 idea novelty checker。用户选择 facets，系统辅助重组生成想法。

### 关键机制
核心是 human-in-the-loop facet recombination 与 novelty checking。

### 实验验证与证据
原文通过用户研究和消融实验显示 Scideator 比普通 LLM baseline 提供更强创意支持。

### 局限性补充
它是人机协同 ideation 工具，不是自主发现系统；输出仍需专家判断和实验验证。

### XYZ 分类逐项解释
- `X0`：不是多智能体，而是人机复合系统。
- `Y2`：facet recombination 和 novelty checking 支撑候选生成与筛选。
- `Z1,Z2,Z7`：覆盖文献、想法和新颖性评价。

### 综述写作用法
适合说明 scientific ideation 可以围绕可追踪 facets 和 novelty verification 组织。
