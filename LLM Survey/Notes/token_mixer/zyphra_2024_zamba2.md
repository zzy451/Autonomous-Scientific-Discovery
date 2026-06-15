# Zamba2: A Suite of Hybrid Mamba2-Transformer Models
**作者**: Zyphra Team (Paolo Glorioso, Quentin Anthony, et al.) | **年份**: 2024 | **arxiv**: 2411.15242

## 0. 摘要翻译
Zamba2 是 Zyphra 发布的混合 Mamba2-Transformer 模型系列（1.2B、2.7B、7.4B 参数），在同规模开源模型中达到 SOTA。其核心设计是在 Mamba2 层序列中穿插少量共享参数的注意力层，并使用 LoRA 适配器为每个注意力实例提供差异化。这种设计在保持 SSM 推理效率的同时，以极小的参数开销获得了注意力的精确检索能力。

## 1. 方法动机
a) **为什么**: 纯 SSM 模型在 recall 任务上弱于 Transformer；纯 Transformer 推理效率低。混合架构是当前最优方案，但如何最优地混合仍是开放问题。
b) **痛点**: (1) Jamba 等混合模型的注意力层各自独立，参数量大；(2) 需要在参数效率和模型质量间找到更好的平衡；(3) 小模型（1-7B）对参数效率更敏感。
c) **假设**: 注意力层之间的参数高度相似，可以共享权重 + 用轻量 LoRA 适配器提供差异化，从而用更少参数获得更多注意力层的效果。

## 2. 方法设计

### a) 架构
```
Zamba2 架构 (以 7.4B 为例):
  Layer 1:  Mamba2
  Layer 2:  Mamba2
  Layer 3:  Mamba2
  Layer 4:  Mamba2
  Layer 5:  Mamba2
  Layer 6:  Shared Attention + LoRA_1  ← 共享注意力权重，独立 LoRA
  Layer 7:  Mamba2
  ...
  Layer 12: Shared Attention + LoRA_2  ← 同一份注意力权重，不同 LoRA
  ...
  (每 ~6 个 Mamba2 层插入 1 个共享注意力层)
```

### b) 核心模块

**Mamba2 层 (占大多数)**:
- 基于 SSD (State Space Duality) 的高效 SSM
- 线性复杂度训练和推理
- 固定大小状态，不需要 KV cache

**共享注意力层 + LoRA**:
- 所有注意力层共享同一份 Q, K, V, O 权重矩阵
- 每个注意力实例有独立的 LoRA 适配器: `W_i = W_shared + A_i B_i^T`
- LoRA rank 很小（如 64），参数开销极小
- 效果: 相当于有多个不同的注意力层，但参数量接近只有一个

**注意力层间的 KV 共享**:
- 连续的共享注意力层可以复用 KV cache
- 进一步减少推理时的内存开销

### c) 关键设计决策
- 注意力层比例: 约 1:6 (注意力:Mamba2)
- 共享权重 + LoRA 比独立注意力层节省 ~5x 参数
- Mamba2 层间穿插 MLP（与 Mamba2 交替）

## 3. 对比
| 模型 | 架构 | 注意力比例 | 参数共享 | 规模 |
|------|------|-----------|---------|------|
| Jamba | Mamba + Attention | ~1:3 | 无 | 52B MoE |
| Griffin | RG-LRU + Local Attn | ~1:2 | 无 | 14B |
| StripedHyena | Hyena + Attention | ~1:3 | 无 | 7B |
| Zamba2 | Mamba2 + Shared Attn + LoRA | ~1:6 | 注意力层共享 | 1.2-7.4B |

## 4. 实验
- **质量**: Zamba2-7.4B 在 MMLU, HellaSwag, ARC 等基准上超越 Llama-2-7B, Mistral-7B
- **参数效率**: 共享注意力 + LoRA 使得 Zamba2-2.7B 质量接近其他 3B+ 模型
- **推理效率**: 由于大部分层是 Mamba2，推理时内存和延迟显著优于同规模 Transformer
- **训练**: 在 3T tokens 上训练，使用 annealing 策略
- **小模型优势**: 在 1-3B 参数范围，Zamba2 的参数效率优势最为明显

## 5. 总结
a) **一句话**: Zamba2 通过在 Mamba2 层序列中穿插少量共享权重+LoRA 的注意力层，以极高的参数效率实现了混合架构，在小模型规模上达到 SOTA。
b) **速记 pipeline**: `Input → [Mamba2 × 6 → SharedAttn+LoRA_i × 1] × N_groups → Output | Attn weights shared, LoRA per instance`
