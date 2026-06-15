# Root Mean Square Layer Normalization
**作者**: Biao Zhang, Rico Sennrich | **年份**: 2019 | **arxiv**: 1910.07467

## 0. 摘要翻译

Layer Normalization (LayerNorm) 已被成功应用于多种神经网络模型（如 Transformer），以稳定隐层状态的动态变化并加速训练收敛。然而，LayerNorm 的计算开销不可忽视，因为它需要计算隐层的均值和方差统计量。本文提出 Root Mean Square Layer Normalization (RMSNorm)，假设 LayerNorm 成功的关键在于其重缩放不变性 (re-scaling invariance) 而非重中心化 (re-centering)，因此去除了均值中心化操作，只保留基于均方根 (RMS) 的缩放归一化。大量实验表明 RMSNorm 在不同任务和模型上均能匹配 LayerNorm 的性能，同时减少了约 7%–64% 的计算时间。

## 1. 方法动机

### a) 为什么
LayerNorm 在 Transformer 等序列模型中是标准做法，但其计算包含**两次归约操作**——计算均值 $\mu$ 和计算方差 $\sigma^2$，以及后续的减均值和除标准差。在高速推理和大规模训练中，这些操作构成了不可忽视的开销。

### b) 痛点
- LayerNorm 的均值计算和减法操作是否真正必要？
- 在 GPU/TPU 上，两次归约操作（均值 + 方差）造成额外的内存访问和同步开销
- 大规模 LLM（数十亿参数）中，每层的归一化计算累积起来影响训练吞吐量

### c) 假设
LayerNorm 的成功主要归因于其**重缩放不变性** (re-scaling invariance)——即对输入进行缩放不改变输出。重中心化 (re-centering，即减均值) 对性能的贡献可以忽略。因此，可以安全地移除均值相关计算，仅保留 RMS 缩放。

## 2. 方法设计

### a) Pipeline
1. 计算输入向量的 Root Mean Square (RMS)
2. 将输入除以 RMS 进行归一化
3. 使用可学习缩放参数 $\gamma$ 进行仿射变换（无偏移 $\beta$）

### b) 模块

**LayerNorm（对照）**:
$$\text{LayerNorm}(x) = \gamma \cdot \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta$$

**RMSNorm（本文）**:
$$\text{RMS}(\mathbf{a}) = \sqrt{\frac{1}{n}\sum_{i=1}^{n} a_i^2}$$
$$\bar{a}_i = \frac{a_i}{\text{RMS}(\mathbf{a})}$$
$$y_i = \gamma_i \cdot \bar{a}_i$$

### c) 公式
- 输入: $\mathbf{a} \in \mathbb{R}^n$（隐层向量）
- RMS 统计量: $\text{RMS}(\mathbf{a}) = \sqrt{\frac{1}{n}\sum_{i=1}^{n} a_i^2}$
- 归一化: $\bar{a}_i = a_i / \text{RMS}(\mathbf{a})$
- 输出: $y_i = \gamma_i \cdot \bar{a}_i$
- 可学习参数: 仅 $\gamma \in \mathbb{R}^n$（$n$ 个参数），**无** $\beta$
- 相比 LayerNorm 减少了 $n+1$ 个参数（去掉 $\beta$ 和 $\mu$ 计算）

**不变性分析**:
- RMSNorm 保持 re-scaling invariance: 若 $\mathbf{a}' = \alpha \mathbf{a}$，则 $\text{RMSNorm}(\mathbf{a}') = \text{RMSNorm}(\mathbf{a})$
- 但不保持 re-centering invariance（因为不减均值）
- 作者在 partial RMSNorm (pRMSNorm) 变体中还探讨了仅对部分维度计算 RMS 的策略

## 3. 对比

| 特性 | LayerNorm | RMSNorm |
|------|-----------|---------|
| 统计量 | 均值 $\mu$ + 方差 $\sigma^2$ | 仅 RMS |
| 归约操作 | 2次（均值 + 方差） | 1次（RMS） |
| 可学习参数 | $2n$（$\gamma$ + $\beta$） | $n$（仅 $\gamma$） |
| 重缩放不变性 | 有 | 有 |
| 重中心化不变性 | 有 | 无 |
| 计算效率 | 基线 | 快 7%–64% |
| 性能 | 基线 | 匹配 |
| LLM 采用 | GPT-2/3 | LLaMA, PaLM, Qwen, Gemma, Mistral, DeepSeek |

## 4. 实验

- **机器翻译** (WMT14 En-De, WMT16 En-Ro): RMSNorm 匹配 LayerNorm 的 BLEU 分数
- **语言建模**: 在 Penn Treebank 上困惑度 (perplexity) 相当
- **图像分类**: 在 MNIST 上误差率相当
- **pRMSNorm 变体**: 仅使用部分维度计算 RMS 时也可保持性能，进一步降低开销
- **速度对比**: 在不同硬件和框架上实测加速 7%–64%
- **后续工业验证**: LLaMA 1/2/3, PaLM, Gemma 1/2, Qwen 1/2/3, Mistral, DeepSeek 等主流 LLM 均采用 RMSNorm 作为标准归一化方法

## 5. 总结

### a) 一句话
RMSNorm 通过去除 LayerNorm 中的均值中心化步骤，仅保留 RMS 缩放，在保持性能的同时降低计算成本，已成为 2023+ 大语言模型的事实标准归一化方法。

### b) 速记 pipeline
```
输入 x → 计算 RMS(x) → x / RMS(x) → 乘以 γ → 输出
（无减均值，无 β，仅一次归约操作）
```

---
**阅读日期**: 2026-04-06
