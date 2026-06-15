# StripedHyena: Moving Beyond Transformers with Hybrid Signal Processing Models
**作者**: Michael Poli, Jue Wang, Stefano Massaroli, Jeffrey Quesnelle, Ryan Beal, Tri Dao, Karan Goel, Albert Gu, Christopher Ré (Together AI) | **年份**: 2023 | **arxiv**: 2312.00752 (blog/tech report)

## 0. 摘要翻译
StripedHyena 是第一个基于 Hyena 算子的可替代 Transformer 的语言模型，由 Together AI 发布。它采用 Hyena（长卷积）层与注意力层交替混合的架构，在保持与同规模 Transformer 相当质量的同时，实现了更快的长序列处理。发布了 StripedHyena-Nous-7B（聊天模型）和 StripedHyena-Hessian-7B（基座模型）。

## 1. 方法动机
a) **为什么**: Hyena 论文证明了长卷积可以替代注意力，但纯 Hyena 模型在某些 recall 任务上仍有差距。需要找到最优的混合比例。
b) **痛点**: (1) 纯卷积模型在精确检索任务上弱于注意力；(2) 纯注意力模型在长序列上效率低；(3) 工业部署需要在质量和效率间找到最佳平衡。
c) **假设**: 少量注意力层（提供精确检索能力）+ 大量 Hyena 层（提供高效长程建模）的混合架构可以兼得两者优势。

## 2. 方法设计

### a) Pipeline
```
StripedHyena 架构:
  Layer 1: Hyena (长卷积 + 门控)
  Layer 2: Hyena
  Layer 3: Attention (标准多头注意力)
  Layer 4: Hyena
  Layer 5: Hyena
  Layer 6: Attention
  ... (交替，注意力层占比约 1/3 或更少)
```

### b) 核心模块

**Hyena 层** (占大多数):
- 隐式参数化长卷积 + 数据控制门控
- O(n log n) 复杂度
- 负责大部分序列混合工作

**注意力层** (少量穿插):
- 标准多头注意力 + RoPE
- 提供精确的内容感知检索能力
- 弥补纯卷积在 recall 任务上的不足

**混合策略**:
- 注意力层与 Hyena 层按固定模式交替（如每 3-4 个 Hyena 层插入 1 个注意力层）
- 这种 "striped"（条纹状）交替是模型名称的由来
- 混合比例是关键超参数

### c) 工程优化
- 自定义 CUDA kernel 实现高效长卷积
- 支持 FlashAttention 用于注意力层
- 针对推理优化: Hyena 层可以用循环模式（O(1) 步进），注意力层用 KV cache

## 3. 对比
| 模型 | 架构 | 长序列效率 | Recall 能力 | 参数量 |
|------|------|-----------|-------------|--------|
| Llama-2-7B | 纯 Transformer | 低 | 强 | 7B |
| Hyena (纯) | 纯长卷积 | 高 | 中 | — |
| StripedHyena-7B | Hyena + Attn 混合 | 高 | 强 | 7B |
| Mamba-3B | 纯 SSM | 高 | 中 | 3B |

## 4. 实验
- **语言建模**: StripedHyena-7B 在标准基准上匹配 Llama-2-7B 和 Mistral-7B
- **长序列**: 在长文本任务上优于同规模纯 Transformer
- **推理速度**: 在长序列生成时比 Transformer 快 1.5-2x
- **聊天**: StripedHyena-Nous-7B 经过指令微调后聊天质量良好
- **意义**: 首次证明 Hyena 混合架构可以在 7B 规模上实际部署

## 5. 总结
a) **一句话**: StripedHyena 通过将 Hyena 长卷积层与少量注意力层条纹状交替混合，首次在 7B 规模上实现了可替代 Transformer 的高效语言模型。
b) **速记 pipeline**: `Input → [Hyena(LongConv+Gate) × 3 → MHA × 1] × N_groups → Output`
