# Reducing Transformer Key-Value Cache Size with Cross-Layer Attention (CLA)
**作者**: William Brandon, Mayank Mishra, Aniruddha Nrusimha, Rameswar Panda, Jonathan Ragan Kelly | **年份**: 2024 | **arxiv**: 2405.12981

## 0. 摘要翻译
本文提出 Cross-Layer Attention (CLA)，一种简单而有效的 KV cache 压缩方法：让相邻层共享同一份 KV 投影。与 MQA/GQA 在 head 维度共享不同，CLA 在层维度共享。CLA 可以与 MQA/GQA 正交组合，进一步减少 KV cache。在 1B 和 3B 模型上，CLA 将 KV cache 减少 2x 而质量损失极小。

## 1. 方法动机
a) **为什么**: MQA/GQA 通过减少 KV head 数来压缩 KV cache，但这只是一个维度的压缩。层维度的冗余尚未被利用。
b) **痛点**: (1) 即使用了 GQA，L 层模型仍需 L 份 KV cache；(2) 相邻层的 KV 表示可能高度相似（冗余）；(3) 需要一种与 head sharing 正交的压缩方法。
c) **假设**: 相邻层的 KV 投影足够相似，可以直接共享而不显著影响模型质量。

## 2. 方法设计

### a) Pipeline
```
标准 Transformer (每层独立 KV):
  Layer 1: Q1, K1, V1 → Attn(Q1, K1, V1)
  Layer 2: Q2, K2, V2 → Attn(Q2, K2, V2)
  Layer 3: Q3, K3, V3 → Attn(Q3, K3, V3)
  Layer 4: Q4, K4, V4 → Attn(Q4, K4, V4)

CLA (每2层共享 KV):
  Layer 1: Q1, K1, V1 → Attn(Q1, K1, V1)  ← 计算 KV
  Layer 2: Q2       → Attn(Q2, K1, V1)  ← 复用 Layer 1 的 KV
  Layer 3: Q3, K3, V3 → Attn(Q3, K3, V3)  ← 计算 KV
  Layer 4: Q4       → Attn(Q4, K3, V3)  ← 复用 Layer 3 的 KV
```

### b) 核心模块

**跨层 KV 共享**:
- 将层分组（如每 2 层一组）
- 每组中只有第一层计算 K, V 投影
- 组内其他层直接复用第一层的 K, V
- Q 投影每层仍然独立（保持每层的查询多样性）

**共享粒度**:
- CLA-2: 每 2 层共享 → KV cache 减半
- CLA-3: 每 3 层共享 → KV cache 减少到 1/3
- CLA-2 是最佳平衡点（质量损失最小）

**与 MQA/GQA 组合**:
- CLA 在层维度压缩，MQA/GQA 在 head 维度压缩
- 两者正交，可以叠加: CLA-2 + GQA-8 → 总压缩比 = 2 × (H/8)
- 例如: 32 head 模型用 CLA-2 + MQA → KV cache 减少 64x

### c) 关键公式
- 标准: 每层 KV cache = 2 × n × d_head × n_kv_heads
- CLA-S (S 层共享): 总 KV cache = L/S × 2 × n × d_head × n_kv_heads
- 压缩比: S 倍（层维度）× H/n_kv_heads 倍（head 维度）

## 3. 对比
| 方法 | 压缩维度 | 压缩比 | 需要重训 | 与 GQA 兼容 |
|------|----------|--------|---------|-------------|
| MQA | Head → 1 | H× | 是 | — |
| GQA | Head → G | H/G× | 是 | — |
| MLA | Head → 低秩 | ~10x | 是 | 否 |
| CLA-2 | Layer → 共享 | 2× | 是 | 是 |
| YOCO | Layer → 全局共享 | ~L/2× | 是 | 是 |

## 4. 实验
- **模型规模**: 1B 和 3B 参数，从头训练
- **CLA-2 质量**: 在 1B 模型上，CLA-2 的困惑度仅比基线高 0.1-0.2（几乎无损）
- **CLA-3 质量**: 损失稍大但仍可接受
- **组合效果**: CLA-2 + MQA 在 3B 模型上，KV cache 减少 >50x，质量损失 <1% PPL
- **下游任务**: 在 HellaSwag, PIQA, ARC 等任务上，CLA-2 与基线差距在噪声范围内
- **工业采用**: 腾讯 Hunyuan-Large 采用了 CLA 技术

## 5. 总结
a) **一句话**: CLA 通过让相邻层共享 KV 投影（层维度压缩），与 MQA/GQA（head 维度压缩）正交组合，以极小的质量代价实现了 KV cache 的进一步大幅压缩。
b) **速记 pipeline**: `Input → [Layer 2i: Compute Q,K,V → Attn | Layer 2i+1: Compute Q only → Attn(Q, K_{2i}, V_{2i})] × L/2 → Output`
