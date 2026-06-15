# You Only Cache Once: Decoder-Decoder Architectures for Language Models (YOCO)
**作者**: Yutao Sun, Li Dong, Yi Zhu, Shaohan Huang, Wenhui Wang, Shuming Ma, Quanlu Zhang, Jianyong Wang, Furu Wei | **年份**: 2024 | **arxiv**: 2405.05254

## 0. 摘要翻译
本文提出 YOCO (You Only Cache Once)，一种 decoder-decoder 架构，将模型分为两部分：前半部分（self-decoder）使用高效注意力（如滑动窗口或线性注意力）处理输入，后半部分（cross-decoder）通过交叉注意力复用前半部分生成的全局 KV cache。这样整个模型只需缓存一次 KV，大幅减少推理时的内存占用。

## 1. 方法动机
a) **为什么**: LLM 推理时 KV cache 是主要内存瓶颈。标准 Transformer 每层都需要独立的 KV cache，L 层模型需要 L 份 KV cache。
b) **痛点**: (1) KV cache 内存随层数线性增长；(2) GQA/MQA 虽然减少了 head 数但仍需每层缓存；(3) 长上下文场景下 KV cache 可达数十 GB。
c) **假设**: 如果前半部分用高效注意力（不需要 KV cache 或只需局部 cache），后半部分通过交叉注意力共享同一份全局 KV cache，就可以将 KV cache 从 L 份减少到约 L/2 份甚至更少。

## 2. 方法设计

### a) Pipeline
```
YOCO 架构 (L 层总共):
  
  Self-Decoder (前 L/2 层):
    - 使用高效自注意力（滑动窗口 / 线性注意力）
    - 不需要全局 KV cache（或只需局部窗口 cache）
    - 输出: 全局 KV 表示 (K_global, V_global)
  
  Cross-Decoder (后 L/2 层):
    - Q 来自当前层输入
    - K, V 来自 Self-Decoder 的输出（共享同一份）
    - 标准交叉注意力: Attn(Q_l, K_global, V_global)
    - 所有 cross-decoder 层共享同一份 KV cache
```

### b) 核心模块

**Self-Decoder**:
- 可选多种高效注意力:
  - 滑动窗口注意力 (SWA): 只关注局部窗口，cache 大小固定
  - 门控线性注意力 (GLA): O(1) 状态，无需 KV cache
- 目的: 生成包含全局信息的中间表示

**Cross-Decoder**:
- 每层执行交叉注意力: `O_l = softmax(Q_l K_global^T / √d) V_global`
- K_global, V_global 由 self-decoder 最后一层的输出投影得到
- 所有 cross-decoder 层共享同一份 K_global, V_global
- 推理时只需缓存这一份 KV → "You Only Cache Once"

**KV Cache 节省**:
- 标准 Transformer: L 层 × 2(K+V) × n × d = O(Lnd)
- YOCO: 1 份全局 KV + L/2 层局部/无 cache = O(nd + L/2 · w · d)
- 当 L 大时，节省接近 L/2 倍

### c) 关键公式
- Self-decoder 层: `h_l = EfficientAttn(h_{l-1})` for l = 1..L/2
- 全局 KV: `K_g = W_K · h_{L/2}`, `V_g = W_V · h_{L/2}`
- Cross-decoder 层: `h_l = CrossAttn(Q_l, K_g, V_g)` for l = L/2+1..L
- 其中 `Q_l = W_Q^l · h_{l-1}`

## 3. 对比
| 方法 | KV Cache 大小 | 全局信息 | 推理速度 |
|------|-------------|----------|----------|
| 标准 Transformer | O(L·n·d) | 每层完整 | 基线 |
| GQA | O(L·n·d/G) | 每层完整 | 快 |
| MLA | O(L·n·d') | 每层压缩 | 快 |
| YOCO | O(n·d) + 局部 | 共享全局 | 很快 |

## 4. 实验
- **语言建模**: YOCO-3B 在标准基准上匹配同规模 Transformer
- **KV Cache**: 推理时 KV cache 减少约 L/2 倍（如 32 层模型减少 ~16x）
- **长上下文**: 在 1M token 上下文长度下，YOCO 的内存优势更加显著
- **预填充速度**: 由于 self-decoder 使用高效注意力，prefill 阶段也更快
- **吞吐量**: 在相同内存预算下，YOCO 可以服务更大的 batch size
- **后续**: Hunyuan-Large (腾讯) 采用了类似的 Cross-Layer Attention 思想

## 5. 总结
a) **一句话**: YOCO 通过 decoder-decoder 架构（前半高效自注意力 + 后半共享 KV 的交叉注意力），将 KV cache 从每层独立缓存压缩为全模型共享一份，实现了接近 L/2 倍的推理内存节省。
b) **速记 pipeline**: `Input → Self-Decoder[SWA/GLA × L/2] → (K_g, V_g) → Cross-Decoder[CrossAttn(Q_l, K_g, V_g) × L/2] → Output`
