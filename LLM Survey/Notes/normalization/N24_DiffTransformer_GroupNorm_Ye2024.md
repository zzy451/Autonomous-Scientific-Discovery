# Differential Transformer
**作者**: Tianzhu Ye, Li Dong, Yuqing Xia, Yutao Sun, Yi Zhu, Gao Huang, Furu Wei | **年份**: 2024 | **arxiv**: 2410.05258

## 0. 摘要翻译

Transformer 倾向于为不相关的上下文分配不必要的注意力。本文提出 **Differential Transformer (Diff Transformer)**，通过将注意力分数计算为两个独立 softmax 注意力映射的**差值**来消除注意力噪声。对差分注意力头的输出应用 **GroupNorm** 以控制尺度和稳定训练。实验表明 Diff Transformer 在语言建模中减少了幻觉 (hallucination)、增强了上下文学习能力、改善了长上下文建模，并降低了激活值异常值 (outlier)，有利于模型量化。

## 1. 方法动机

### a) 为什么
标准 Transformer 的注意力机制存在噪声问题：softmax 注意力总是为所有 token 分配非零权重（即使是完全不相关的 token），这些噪声注意力可能导致幻觉和上下文理解错误。

### b) 痛点
- **注意力噪声**: softmax 的非负性和归一化约束导致不相关 token 也获得非零权重
- **幻觉 (Hallucination)**: 噪声注意力可能导致模型关注无关上下文并生成错误内容
- **激活异常值**: 注意力噪声的累积导致隐状态中出现极端异常值，影响量化
- **差分输出尺度不确定**: 两个 softmax 相减后，输出的值域和尺度不再被 softmax 的 $[0,1]$ 自然约束

### c) 假设
通过两组独立的注意力权重的差值，可以消除公共的噪声成分（类似于差分放大器消除共模噪声）。差分后的输出需要 GroupNorm 来重新控制尺度。

## 2. 方法设计

### a) Pipeline
1. 将 Q, K 各分为两组 $(Q_1, Q_2)$, $(K_1, K_2)$
2. 分别计算两组的 softmax 注意力
3. 用差值（相减）作为最终注意力权重
4. 对每个差分注意力头的输出应用 GroupNorm
5. 使用可学习 $\lambda$ 和初始化因子 $(1-\lambda_\text{init})$ 对齐梯度流

### b) 模块

**差分注意力**:
$$\text{DiffAttn}(X) = \left(\text{softmax}\left(\frac{Q_1 K_1^T}{\sqrt{d}}\right) - \lambda \cdot \text{softmax}\left(\frac{Q_2 K_2^T}{\sqrt{d}}\right)\right) V$$

- $(Q_1, Q_2) = \text{split}(XW_Q)$, $(K_1, K_2) = \text{split}(XW_K)$
- $\lambda$: 可学习标量，通过 $\lambda = \exp(\lambda_{q1} \cdot \lambda_{k1}) - \exp(\lambda_{q2} \cdot \lambda_{k2}) + \lambda_\text{init}$ 参数化
- $\lambda_\text{init}$: 初始化超参数（典型值 0.8）

**GroupNorm 的应用**:
$$\text{head}_i = (1 - \lambda_\text{init}) \cdot \text{GroupNorm}(\text{DiffAttn}_i(X))$$

- GroupNorm 对每个注意力头的输出独立归一化
- $(1 - \lambda_\text{init})$ 因子对齐梯度流与标准 Transformer

### c) 公式
- 每个头: 将标准 $d_k$ 维的 Q, K 各分为 $d_k/2$ 维的两组
- GroupNorm 的 group 数 = head 数（每个 head 是一个 group）
- 差分输出值域: 理论上 $\in [-1-\lambda, 1+\lambda]$，但实际集中在 $[-\epsilon, 1]$ 附近
- GroupNorm 归一化后: 输出尺度稳定为 $O(1)$

## 3. 对比

| 特性 | 标准 Attention | Diff Attention + GroupNorm |
|------|--------------|--------------------------|
| 注意力权重 | $\geq 0$（softmax 保证） | 可为负（差分允许"抑制"） |
| 噪声 token 权重 | 非零 | 接近零（被差分消除） |
| 输出尺度控制 | softmax 自然约束 | GroupNorm 显式约束 |
| 幻觉倾向 | 较高 | **较低** |
| 激活异常值 | 常见 | **减少** |
| 量化友好性 | 一般 | **更好** |

**与其他注意力归一化的对比**:
| 方法 | 归一化对象 | 位置 |
|------|-----------|------|
| QK-Norm | Q, K 向量 | 注意力**输入** |
| **GroupNorm (Diff-Attn)** | 注意力头输出 | 注意力**输出** |

## 4. 实验

- **语言建模** (1B-7B 参数): Diff Transformer 在困惑度上匹配或超过标准 Transformer
- **幻觉减少**: 在 TruthfulQA、HaluEval 等基准上显著降低幻觉率
- **上下文学习**: 在 few-shot 任务上性能提升
- **长上下文**: 在 128K token 长度的任务上表现更好
- **激活异常值**: 隐状态中的 outlier 数量和幅度显著减少
- **量化**: 由于 outlier 减少，INT8/INT4 量化精度损失更小
- **关键信息检索**: 在 "needle-in-a-haystack" 测试中更准确

## 5. 总结

### a) 一句话
Differential Transformer 通过两组注意力权重的差值消除注意力噪声，使用 GroupNorm 控制差分输出尺度，是 GroupNorm 在 LLM 中最重要的应用案例，展示了归一化在注意力输出层的新角色。

### b) 速记 pipeline
```
Q → split → Q₁, Q₂;  K → split → K₁, K₂
Attn = softmax(Q₁K₁ᵀ/√d) - λ·softmax(Q₂K₂ᵀ/√d)  ← 差分消除噪声
Attn * V → GroupNorm → × (1-λ_init) → 输出
（GroupNorm 按 head 分组，控制差分输出的尺度）
```

---
**阅读日期**: 2026-04-06
