# Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length
**作者**: Xuezhe Ma, Xiaomeng Yang, Wenhan Xiong, Beidi Chen, Lili Yu, Hao Zhang, Jonathan May, Luke Zettlemoyer, Omer Levy, Chunting Zhou | **年份**: 2024 | **arxiv**: 2404.08801

## 0. 摘要翻译
本文提出 Megalodon，一种面向无限上下文长度的高效序列建模架构。Megalodon 继承了 Mega（指数移动平均 + 门控注意力）的架构，并引入多项改进：复数指数移动平均（CEMA）、时间步归一化层、归一化注意力机制和预归一化残差连接。在 7B 参数、2T tokens 的受控对比中，Megalodon 的训练效率优于 Llama-2，训练损失 1.70（介于 Llama-2-7B 的 1.75 和 Llama-2-13B 的 1.67 之间）。

## 1. 方法动机
a) **为什么**: Mega 在中等规模上表现优异，但在 LLM 规模（7B+）上训练不稳定，且缺乏一些现代 LLM 的关键技术。
b) **痛点**: (1) Mega 的 EMA 使用实数衰减，无法建模振荡模式；(2) 大规模训练时注意力数值不稳定；(3) 块级注意力的块大小选择影响质量-效率权衡。
c) **假设**: 通过复数 EMA（建模振荡）、归一化注意力（稳定训练）和改进的残差连接，Mega 架构可以扩展到 LLM 规模并超越 Transformer。

## 2. 方法设计

### a) 架构概览（基于 Mega 改进）
```
Megalodon Block:
  Input → PreNorm
    ├─→ Complex EMA (CEMA) → 局部时序特征
    │     → 生成 Q, K, V (单头)
    └─→ 门控分支
         ↓
  Normalized Single-head Gated Attention
    → Chunk-wise attention (块大小 c)
         ↓
  Timestep Normalization → Residual → FFN → Output
```

### b) 核心改进

**1. 复数指数移动平均 (CEMA)**:
- Mega 的 EMA: `h_t = α · h_{t-1} + (1-αδ) · x_t` (实数，只能衰减)
- Megalodon 的 CEMA: `h_t = (α + βi) · h_{t-1} + (1-(α+βi)δ) · x_t` (复数)
- 复数衰减 = 衰减 + 旋转 → 可以建模振荡/周期模式
- 输出取实部

**2. 时间步归一化 (Timestep Normalization)**:
- 类似 GroupNorm，但沿时间维度归一化
- 稳定长序列训练中的数值范围
- `y_t = γ · (h_t - μ_t) / σ_t + β`

**3. 归一化注意力 (Normalized Attention)**:
- 标准: `Attn = softmax(QK^T/√d) V`
- Megalodon: `Attn = softmax(QK^T / (||Q|| · ||K||)) V` — L2 归一化
- 防止注意力 logit 爆炸，稳定大规模训练

**4. 预归一化残差 (Pre-Norm with Two-Hop Residual)**:
- 双跳残差连接: 同时连接前一层和前两层的输出
- 改善梯度流动，特别是在深层网络中

### c) 关键公式
- CEMA: `h_t = (α + βi) ⊙ h_{t-1} + (1 - (α+βi) ⊙ δ) ⊙ x_t`
- 归一化注意力: `A = softmax(q^T k / (||q|| · ||k|| · τ))` (τ 是温度)
- 块注意力: 序列分块，块内完整注意力，块间通过 EMA 状态传递
- 复杂度: O(n·c) 其中 c 是块大小

## 3. 对比
| 模型 | 基础 | EMA | 注意力 | 规模验证 |
|------|------|-----|--------|---------|
| Mega | EMA + 门控注意力 | 实数 | 单头+块 | 355M |
| Megalodon | CEMA + 归一化门控注意力 | 复数 | 单头+块+归一化 | 7B |
| Transformer | — | — | 多头 softmax | 70B+ |
| Mamba | 选择性 SSM | — | 无 | 3B |

## 4. 实验
- **语言建模**: Megalodon-7B 训练损失 1.70，优于 Llama-2-7B (1.75)
- **基准测试**: 在 HellaSwag, PIQA, ARC 等上与 Llama-2-7B 竞争力相当或更好
- **长上下文**: 在无限长度推理上保持稳定（EMA 状态固定大小）
- **训练效率**: 训练吞吐量与 Transformer 相当
- **推理效率**: 块注意力 + EMA 使推理内存恒定
- **Scaling**: 在 7B/2T 规模上首次证明 Mega 系列可以超越 Transformer

## 5. 总结
a) **一句话**: Megalodon 通过复数 EMA、归一化注意力和时间步归一化将 Mega 架构扩展到 7B LLM 规模，在受控对比中训练效率优于 Llama-2，是 EMA+门控注意力路线在 LLM 规模的首次成功验证。
b) **速记 pipeline**: `Input → CEMA(complex decay+oscillation) → (Q,K,V,Gate) → NormalizedAttn(chunk-wise) → TimestepNorm → 2-hop Residual → FFN → Output`
