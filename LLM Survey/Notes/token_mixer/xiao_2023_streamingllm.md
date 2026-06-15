# Efficient Streaming Language Models with Attention Sinks (StreamingLLM)
**作者**: Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis | **年份**: 2023 | **arxiv**: 2309.17453

## 0. 摘要翻译
本文发现了"注意力汇聚"（Attention Sink）现象：LLM 在自回归生成时，无论输入内容如何，都会将大量注意力分配给最初几个 token。基于此发现，提出 StreamingLLM 框架——只保留最初几个 token（attention sink）和最近的滑动窗口 token 的 KV cache，即可让有限窗口训练的 LLM 稳定地处理无限长度的流式输入，无需微调。

## 1. 方法动机
a) **为什么**: LLM 部署中经常需要处理流式输入（如长对话、实时翻译），但标准 Transformer 的 KV cache 会无限增长。
b) **痛点**: (1) 简单的滑动窗口会在窗口滑过初始 token 时导致困惑度爆炸；(2) 重新计算（re-computation）代价太高；(3) 需要理解为什么丢弃初始 token 会导致崩溃。
c) **假设**: 初始 token 充当了 softmax 注意力的"汇聚点"（sink），即使它们的语义不重要，它们的 KV 对注意力分布的稳定性至关重要。保留它们即可解决问题。

## 2. 方法设计

### a) Attention Sink 现象
- 观察: 在所有层中，第 1 个 token（通常是 BOS/`<s>`）获得了异常高的注意力权重
- 原因: softmax 需要一个"垃圾桶"来分配不需要的注意力概率质量
- 第 1 个 token 因为总是可见（因果掩码下），自然成为了这个汇聚点
- 移除它会导致注意力分布崩溃 → 困惑度爆炸

### b) StreamingLLM 框架
```
KV Cache 组成:
  [Sink tokens (前 1-4 个)] + [Recent window (最近 w 个)]
  
例如: sink=4, window=2044 → 总 KV cache = 2048 (固定)

生成过程:
  Step t: KV = [k₁,k₂,k₃,k₄, k_{t-w+1},...,k_{t-1},k_t]
  Step t+1: 丢弃 k_{t-w+1}, 加入 k_{t+1}
  Sink tokens 永远保留
```

### c) 关键设计
- **Sink token 数量**: 通常 1-4 个即可（实验表明 4 个最稳定）
- **位置编码处理**: 使用相对位置编码（如 RoPE）时，需要重新分配位置 ID
  - Sink tokens: 位置 0,1,2,3
  - Window tokens: 位置 4,5,...,w+3（连续编号，不留间隔）
- **无需微调**: 直接应用于已训练的 LLM

### d) 关键公式
- KV cache 大小: 固定为 s + w（s=sink 数, w=窗口大小）
- 内存: O(s + w) — 与序列长度无关
- 质量: 在窗口内的信息完整保留，窗口外的信息丢失

## 3. 对比
| 方法 | KV Cache | 远距离信息 | 稳定性 | 需要微调 |
|------|----------|-----------|--------|---------|
| 全 KV cache | O(n) 增长 | 完整 | 稳定 | 否 |
| 滑动窗口 | O(w) 固定 | 丢失 | 不稳定(崩溃) | 否 |
| StreamingLLM | O(s+w) 固定 | 丢失 | 稳定 | 否 |
| Infini-attention | O(d²) 固定 | 压缩保留 | 稳定 | 是 |

## 4. 实验
- **流式生成**: 在 4M+ token 的流式输入上，StreamingLLM 困惑度稳定（滑动窗口在 ~4K 后崩溃）
- **模型兼容**: 在 Llama-2, MPT, Falcon, Pythia 等模型上均有效
- **Sink 数量**: 1 个 sink 即可防止崩溃，4 个最优
- **速度**: 与滑动窗口相同（固定大小 KV cache）
- **局限**: 无法利用窗口外的信息（只是稳定，不是真正的长上下文）
- **后续**: 启发了 Sink Token 训练策略（在训练时显式添加 sink token）

## 5. 总结
a) **一句话**: StreamingLLM 发现了 Attention Sink 现象（初始 token 充当注意力汇聚点），通过保留少量 sink token + 滑动窗口实现了固定内存的无限长度流式推理。
b) **速记 pipeline**: `Input stream → KV Cache = [Sink(1-4 tokens) + SlidingWindow(w tokens)] → Generate with fixed O(s+w) memory`
