# Causal Hypothesis LLM 2025

## 基本信息
- **论文**: Large Language Models for Causal Hypothesis Generation in Science
- **作者**: Kai-Hendrik Cohrs et al.
- **年份**: 2025
- **来源**: Machine Learning: Science and Technology 6(1):013001, doi:10.1088/2632-2153/ada47f
- **关键词**: method, causal-hypothesis, scientific-discovery, llm

## 核心思想
复杂系统科学中，理解 causal structure 比单纯预测更重要，例如地球、气候和脑科学。LLM 拥有大量文本知识，但其因果推理能力有争议，不能直接当作可靠 causal discovery engine。

这篇论文要解决的问题是：如何把 LLM 作为不完美但有用的 probabilistic expert，嵌入由数据和专家知识共同约束的 causal hypothesis generation 框架。

## 方法细节
论文不是提出单一 agent 系统，而是提出方法论框架：

1. 将 LLM 视为 probabilistic imperfect expert；
2. 让 LLM 在 scientific framework 中与 expert knowledge 和 data-driven causal discovery 结合；
3. 发展 adaptive methods for causal hypothesis generation；
4. 用 hybrid LLM + data causal discovery algorithm 作为更深层集成示例；
5. 建议建立 model-agnostic universal benchmarks 来比较不同 causal hypothesis generation 方法。

## 关键结果

论文主要是概念和方法框架，不以单一 benchmark 数字为核心。其重点是把争论从“LLM 是否真的会因果推理”转向“如何在科学流程中安全地使用 LLM 的知识和假设生成能力”，并强调对 imperfect experts 的 reliability、consistency、uncertainty、content vs. reasoning 等维度进行表征。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Hypothesis Generation 和 Verification，尤其对应 causal reasoning。

在 Skill Lifecycle 中，它对应 Acquisition / literature-derived、Representation / causal hypothesis 和 Verification / data-expert validation。

Evidence Role 应标为 **Direct + Boundary**。它直接补足我们 taxonomy 中 Hypothesis Generation 的 causal reasoning 子能力，同时提醒 LLM 不应被当作因果真理来源，只能作为受数据和专家约束的候选假设生成器。

## 局限性

论文偏方法论和框架，缺少一个统一可复现系统来验证所有主张。实际部署时，如何校准 LLM 的概率性判断、如何与因果发现算法融合、如何构建通用 benchmark 仍是开放问题。

## 核心贡献

这篇论文的核心贡献是把 LLM 在科学因果发现中的角色定义为“imperfect probabilistic expert”，为 causal hypothesis generation 提供了比直接问答更稳的使用方式。
