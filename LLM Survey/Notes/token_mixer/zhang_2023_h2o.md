# H2O: Heavy-Hitter Oracle: Efficient Generative Inference of Large Language Models with Heavy-Hitter Oracle
**作者**: Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Ré, Clark Barrett, Zhangyang Wang, Beidi Chen | **年份**: 2023 | **arxiv**: 2306.14048

## 0. 摘要翻译
本文提出 H2O（Heavy-Hitter Oracle），一种动态 KV cache 淘汰策略。核心发现是：在注意力计算中，只有少量 token（"Heavy Hitters"）持续获得高注意力权重，而大部分 token 的注意力权重很低。H2O 在每步生成时动态淘汰低注意力的 KV，只保留 Heavy Hitters 和最近的 token，在大幅减少 KV cache 的同时保持生成质量。

## 1. 方法动机
a) **为什么**: KV cache 是 LLM 推理的主要内存瓶颈，尤其在长序列和大 batch 场景下。
b) **痛点**: (1) 静态压缩（如 SnapKV）只在 prefill 后做一次，无法适应生成过程中注意力模式的变化；(2) 均匀淘汰会丢失关键信息；(3) 需要一种动态的、基于重要性的淘汰策略。
c) **假设**: 注意力权重的分布高度不均匀（幂律分布），少量 Heavy Hitter token 贡献了大部分注意力质量，淘汰低权重 token 对输出影响极小。

## 2. 方法设计

### a) Pipeline
```
每步生成:
  1. 计算当前 token 与所有 cached KV 的注意力权重
  2. 累积每个位置的注意力分数（历史累积）
  3. 如果 cache 超过预算 B:
     - 保留: Heavy Hitters (累积注意力 top-k) + Recent tokens (最近 r 个)
     - 淘汰: 其余 token 的 KV
  4. 将新 token 的 KV 加入 cache
```

### b) 核心模块

**Heavy Hitter 识别**:
- 维护每个位置的累积注意力分数: `score[i] += Σ_h attn_h[current, i]`
- 累积分数高的位置 = Heavy Hitter
- 这些 token 在语义上通常是关键词、标点、特殊 token 等

**动态淘汰策略**:
- KV cache 预算: B = H (heavy hitters) + R (recent tokens)
- 每步检查: 如果 cache_size > B，淘汰累积分数最低的 token
- 保留策略: top-H heavy hitters + 最近 R 个 token
- Recent tokens 保证局部上下文完整

**与 Attention Sink 的关系**:
- H2O 自然会保留 attention sink token（因为它们累积注意力最高）
- 但 H2O 更灵活——可以动态发现新的 heavy hitter

### c) 关键公式
- 累积注意力: `s_i^{(t)} = s_i^{(t-1)} + Σ_h softmax(q_t^h · K^h)_i`
- 淘汰: 当 |cache| > B 时，移除 `argmin_i s_i` (排除 recent tokens)
- 保留集: `Keep = topk(s, H) ∪ {t-R+1, ..., t}`

## 3. 对比
| 方法 | 淘汰时机 | 策略 | 动态 | 每步开销 |
|------|----------|------|------|----------|
| StreamingLLM | 持续 | Sink + Window | 否(固定) | O(1) |
| SnapKV | Prefill 后一次 | Per-head top-k | 否 | O(1) |
| H2O | 每步 | Heavy Hitter + Recent | 是 | O(n) |
| PyramidKV | Prefill 后一次 | 层自适应 top-k | 否 | O(1) |

## 4. 实验
- **KV cache 压缩**: 在 5-10x 压缩下，H2O 质量损失 <1%
- **模型**: OPT-6.7B/13B/30B, Llama-7B/13B
- **长文本**: 在 LongBench 上优于均匀淘汰和随机淘汰
- **生成质量**: 在摘要、问答等任务上与全 KV cache 接近
- **速度**: 由于 cache 更小，注意力计算加速 2-3x
- **发现**: Heavy Hitter 通常是标点符号、连接词、BOS token 等"结构性" token

## 5. 总结
a) **一句话**: H2O 通过动态追踪累积注意力权重识别 Heavy Hitter token，在每步生成时淘汰低重要性 KV，实现了动态自适应的 KV cache 压缩。
b) **速记 pipeline**: `Generate → Accumulate attention scores → Evict lowest-score KV when over budget → Keep Heavy Hitters + Recent → Next step`
