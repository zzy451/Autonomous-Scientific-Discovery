# N-06: Understanding and Improving Layer Normalization / AdaNorm (Xu et al. 2019)

> **论文**: Understanding and Improving Layer Normalization
> **作者**: Jingjing Xu, Xu Sun, Zhiyuan Zhang, Guangxiang Zhao, Junyang Lin
> **发表**: NeurIPS 2019 | arXiv:1911.07013
> **关键词**: AdaNorm, 自适应归一化, LayerNorm 分析

---

## 核心思想

深入分析 LayerNorm 在 Transformer 中的作用机制，提出 **AdaNorm** -- 一种自适应版本的 LayerNorm，根据输入动态调整归一化的强度。

## 关键分析

1. **均值偏移的作用**: 分析了 LayerNorm 中减均值操作的具体贡献
2. **方差缩放的作用**: 分析了除标准差操作如何帮助训练
3. **可学习参数的必要性**: 讨论了 $\gamma$ 和 $\beta$ 的角色

## AdaNorm 方法

与标准 LayerNorm 使用固定的归一化强度不同，AdaNorm 使输入的归一化程度成为**输入自身的函数**：
- 对于"容易"的输入，减少归一化的强度
- 对于"困难"的输入，加强归一化

这种自适应性让模型能够更灵活地处理不同复杂度的输入。

## 与 LLM 的关系

AdaNorm 本身在大规模 LLM 中未被广泛采用（主流仍使用固定的 LN 或 RMSNorm），但它提出的"自适应归一化"理念影响了后续工作：
- **adaLN (DiT)**: 根据条件信号动态生成 $\gamma$ 和 $\beta$
- **nGPT**: 通过归一化到超球面实现隐式的自适应

## 在综述中的定位

作为 LayerNorm 的理论分析工作，帮助理解归一化的各个组件（减均值、除方差、仿射变换）各自的贡献。可以在综述中简要提及其分析视角。

---

**阅读日期**: 2026-04-05
