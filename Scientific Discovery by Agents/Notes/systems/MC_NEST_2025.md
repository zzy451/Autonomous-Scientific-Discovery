# MC NEST 2025

## 基本信息
- **论文**: Iterative Hypothesis Generation for Scientific Discovery with Monte Carlo Nash Equilibrium Self-Refining Trees
- **作者**: Gollam Rabby, Diyana Muhammed, Prasenjit Mitra, Sören Auer
- **年份**: 2025
- **来源**: arXiv:2503.19309
- **关键词**: system, hypothesis-generation, search, scientific-discovery

## 核心思想
LLM 可以生成研究假设，但一次性生成往往质量不稳定，容易缺乏新颖性、清晰度、重要性或可检验性。科学假设生成更像搜索问题，需要在多个候选之间不断评估、修正和保留更优方向。

MC-NEST 要解决的问题是：如何把 scientific hypothesis generation 组织成可迭代搜索和自我精炼过程，而不是单次 prompt 输出。

## 方法细节
MC-NEST 将 Monte Carlo Tree Search 与 Nash equilibrium inspired refinement 结合。

核心流程是：

1. 从问题或研究背景出发生成多个候选假设；
2. 用树搜索扩展不同假设分支；
3. 对候选假设从 novelty、clarity、significance 和 verifiability 等维度进行评估；
4. 使用 self-refinement 机制改写或增强候选；
5. 在多轮搜索中保留更有价值的假设路径。

## 关键结果

论文在 social science、computer science 和 biomedicine 等领域评估 hypothesis generation。相较 prompt-based baseline，MC-NEST 的 average score 分别从 **2.36 / 2.51 / 2.52** 提升到 **2.65 / 2.74 / 2.80**。其核心结论是，搜索式迭代精炼相比一次性生成更能提升假设质量，尤其在新颖性和可验证性方面更适合科学发现任务。

## 与综述的关联

在 Scientific Workflow 中，MC-NEST 覆盖 Hypothesis Generation、Verification 和 Evolution。

在 Skill Lifecycle 中，它对应 Composition / search over candidate skills、Evolution / reflection 和 Verification / rubric evaluation。

Evidence Role 应标为 **Direct**。它为 hypothesis-generation skill 提供了明确机制：生成科学假设不是一次输出，而是搜索、评估、精炼和选择。

## 局限性

MC-NEST 仍依赖 LLM 评价和设定好的维度，真实科学可行性需要实验或专家验证。搜索计算成本也高于一次性 generation。

## 核心贡献

MC-NEST 的核心贡献是把科学假设生成建模为 tree search + self-refinement 的迭代优化过程，为 novelty/feasibility skill 提供可操作机制。
