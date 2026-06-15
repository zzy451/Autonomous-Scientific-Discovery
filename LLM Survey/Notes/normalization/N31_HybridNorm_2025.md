# N-31: HybridNorm — Towards Stable and Efficient Transformer Training via Hybrid Normalization (2025)

> **论文**: Towards Stable and Efficient Transformer Training via Hybrid Normalization
> **arXiv**: 2503.04598
> **年份**: 2025
> **关键词**: HybridNorm, QKV-Norm, Post-Norm, Pre-Norm, 混合归一化, MoE

---

## 核心思想

Pre-Norm 稳定但性能次优，Post-Norm 性能好但难训练——这是长期存在的 trade-off。HybridNorm 提出一种简单而有效的混合策略：**在注意力机制中使用 QKV 归一化 (QKV-Norm)，在 FFN 中使用 Post-Norm**。这种组合同时获得了 Pre-Norm 的训练稳定性和 Post-Norm 的性能优势。

## 方法

### 混合归一化策略

```
Transformer Block:
  ┌─ Self-Attention ─────────────────────┐
  │  Q, K, V = Linear(x)                │
  │  Q = Norm(Q), K = Norm(K), V = Norm(V)  ← QKV-Norm
  │  attn_out = Attention(Q, K, V)       │
  │  x = x + attn_out                   │  (无 Post-Norm)
  └──────────────────────────────────────┘
  ┌─ FFN ────────────────────────────────┐
  │  ffn_out = FFN(x)                    │
  │  x = Norm(x + ffn_out)              │  ← Post-Norm
  └──────────────────────────────────────┘
```

### 设计动机

- **注意力中的 QKV-Norm**: 控制 Q, K 的范数防止 logit 爆炸（类似 QK-Norm），同时归一化 V 控制输出尺度。提供注意力层的训练稳定性
- **FFN 中的 Post-Norm**: FFN 是 Transformer 中主要的表示学习模块，Post-Norm 保留了更好的梯度信号和表示质量

### 理论分析

- 证明 QKV-Norm 约束了注意力 logits 的范围，防止 softmax 饱和
- 证明 FFN 的 Post-Norm 保持了更好的梯度范数比例，有利于深层网络训练
- 两者结合在理论上同时满足稳定性和表达力的需求

## 实验

| 设置 | Pre-Norm | Post-Norm | HybridNorm |
|------|----------|-----------|------------|
| Dense Transformer | 基线 | 不稳定/更好 | **最优** |
| Sparse MoE | 基线 | 不稳定 | **最优** |
| 收敛速度 | 慢 | 快(若稳定) | **快且稳定** |

关键结果：
1. **Dense 和 Sparse 架构均有效**: 在标准 Transformer 和 MoE 架构上都一致超过 Pre-Norm 和 Post-Norm
2. **收敛更快**: 比 Pre-Norm 收敛更快
3. **训练稳定**: 不需要 Post-Norm 所需的 warmup 调参
4. **SOTA**: 在多个 benchmark 上达到最优

## 与已有方法的对比

| 方法 | 注意力归一化 | FFN 归一化 | 稳定性 | 性能 |
|------|------------|-----------|--------|------|
| Pre-Norm | Pre-LN | Pre-LN | 高 | 次优 |
| Post-Norm | 无 | Post-LN | 低 | 好 |
| Sandwich-LN (N-07) | Pre+Post | Pre+Post | 高 | 好 |
| PeriLN (N-21) | Pre+Post | Pre+Post | 高 | 好 |
| DeepNorm (N-08) | 特殊缩放 | 特殊缩放 | 高 | 好 |
| **HybridNorm** | **QKV-Norm** | **Post-Norm** | **高** | **最优** |

## 对 MoE 的意义

HybridNorm 在 MoE 架构上的实验特别值得关注：
- MoE 中不同专家的激活尺度差异大，归一化策略更加关键
- Post-Norm 在 MoE 的 FFN（即专家层）中帮助控制不同专家输出的尺度一致性
- QKV-Norm 在共享的注意力层中提供稳定性

## 在综述中的定位

HybridNorm 是 Pre-Norm vs Post-Norm 之争的**实用主义解决方案**：不追求理论上的统一（如 GeoNorm N-30），而是通过经验驱动的组合策略，在不同子模块中使用最适合的归一化方式。其对 MoE 架构的验证也填补了归一化在稀疏架构中的研究空白。

---

**阅读日期**: 2026-04-06
