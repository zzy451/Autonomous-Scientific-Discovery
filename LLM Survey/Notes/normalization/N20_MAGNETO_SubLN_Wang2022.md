# Foundation Transformers (MAGNETO)
**作者**: Hongyu Wang, Shuming Ma, Shaohan Huang, Li Dong, Wenhui Wang, Zhiliang Peng, Yu Wu, Payal Bajaj, Saksham Singhal, Alon Benhaim, Barun Patra, Zhun Liu, Vishrav Chaudhary, Xia Song, Furu Wei | **年份**: 2022 | **arxiv**: 2210.06423

## 0. 摘要翻译

我们提出 **MAGNETO** 架构，引入 **Sub-LayerNorm (Sub-LN)** 策略——在 Transformer 子层的**内部**放置额外的 LayerNorm，而非仅在子层的输入或输出。结合从 DeepNet 理论推导的初始化方案，MAGNETO 旨在作为跨模态（语言、视觉、语音、多模态）的统一 Transformer 基础架构 ("Foundation Transformer")。实验表明 MAGNETO 在所有模态上均超过标准 Pre-LN 和 Post-LN Transformer。

## 1. 方法动机

### a) 为什么
Pre-LN 和 Post-LN 各有优劣，且不同模态（语言、视觉、语音）可能需要不同的归一化策略。是否可以设计一种**统一的**归一化位置，同时获得 Pre-LN 的稳定性和 Post-LN 的表达力？

### b) 痛点
- **Pre-LN**: 训练稳定但表达力受限——残差路径上缺少归一化约束，深层后激活值可能"漂移"
- **Post-LN**: 表达力强但训练不稳定——梯度流受阻，需要精心的 warmup
- **模态分裂**: 不同模态的最佳实践不同，缺乏统一架构
- **粗粒度归一化**: Pre/Post-LN 在子层级别操作，对子层内部的中间表示缺乏控制

### c) 假设
将 LayerNorm 放置在子层**内部**（即各投影操作之间），可以在更细粒度上控制激活尺度，同时保持残差连接的梯度高速公路畅通。结合理论初始化，可以实现跨模态的统一训练稳定性。

## 2. 方法设计

### a) Pipeline
1. 在每个子层（注意力/FFN）的内部投影之间插入额外的 LayerNorm
2. 保留子层输入的 Pre-LN
3. 使用 DeepNet 论文的理论初始化方案
4. 在所有模态（语言、视觉、语音、多模态）上统一应用

### b) 模块

**归一化位置对比**:
```
Post-LN:   x → [SubLayer] → [+x] → [LN] → output
Pre-LN:    x → [LN] → [SubLayer] → [+x] → output
Sub-LN:    x → [LN₁] → [Proj₁] → [LN₂] → [Proj₂] → [+x] → output
```

**多头自注意力中的 Sub-LN**:
1. LN₁ 应用于 QKV 投影之前（与 Pre-LN 相同）
2. LN₂ 应用于注意力输出投影之前（新增）

**FFN 中的 Sub-LN**:
1. LN₁ 应用于第一个线性层之前
2. LN₂ 应用于第二个线性层之前

### c) 公式
**Self-Attention with Sub-LN**:
$$Q, K, V = \text{LN}_1(x) W_Q, \text{LN}_1(x) W_K, \text{LN}_1(x) W_V$$
$$\text{Attn} = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
$$\text{output} = x + \text{LN}_2(\text{Attn}) W_O$$

**FFN with Sub-LN**:
$$h = \text{Activation}(\text{LN}_1(x) W_1)$$
$$\text{output} = x + \text{LN}_2(h) W_2$$

**初始化**: 使用 DeepNet 理论的 $\alpha, \beta$ 缩放（按深度推导）

## 3. 对比

| 特性 | Post-LN | Pre-LN | Sandwich-LN | Sub-LN (MAGNETO) |
|------|---------|--------|-------------|-------------------|
| LN 位置 | 残差后 | 子层前 | 子层前+后 | 子层**内部** |
| 粒度 | 粗（子层级） | 粗（子层级） | 粗（子层级） | **细（投影级）** |
| 训练稳定性 | 差 | 好 | 好 | **最好** |
| 表达力 | 强 | 受限 | 中 | **强** |
| 理论支持 | 无 | 有（部分） | 经验 | **理论推导的初始化** |
| 跨模态通用 | 部分 | 广泛 | 未测 | **全部** |

## 4. 实验

- **语言建模** (GPT-style): 超过 Pre-LN 基线
- **机器翻译** (Encoder-Decoder): 超过 Pre-LN 和 Post-LN
- **视觉预训练** (BEiT): 超过 Pre-LN ViT
- **语音识别** (wav2vec 2.0): 超过 Pre-LN
- **多模态** (BEiT-3): 超过 Pre-LN 多模态模型
- **稳定性**: 在所有模态上，MAGNETO 均无需额外的 warmup 调节
- **缩放**: 测试了从 small 到 large 的多种模型规模

## 5. 总结

### a) 一句话
MAGNETO 通过在子层内部投影之间插入 LayerNorm（Sub-LN），结合理论推导的初始化，实现了在语言/视觉/语音/多模态上统一超过 Pre-LN 和 Post-LN 的 Foundation Transformer 架构。

### b) 速记 pipeline
```
注意力: x → LN₁ → QKV投影 → Attention → LN₂ → 输出投影 → +x
FFN:    x → LN₁ → W₁ + Act → LN₂ → W₂ → +x
（Sub-LN = 子层内部的细粒度归一化，配合 DeepNet 初始化）
```

---
**阅读日期**: 2026-04-06
