# SnapKV: LLM Knows What You Are Looking for Before Generation
**作者**: Yuhong Li, Yingbing Huang, Bowen Yang, Bharat Vasan, Jianhen Qin, Ethan Katz-Bassett, Junchen Jiang | **年份**: 2024 | **arxiv**: 2404.14469

## 0. 摘要翻译
本文提出 SnapKV，一种智能 KV cache 压缩方法。核心发现是：在 prompt 阶段，每个注意力头的注意力模式已经稳定地集中在特定的关键位置上。SnapKV 利用这一观察，在生成开始前对 KV cache 进行一次性压缩——只保留每个头中注意力权重最高的 token 对应的 KV，加上一个观察窗口。这使得 KV cache 大小大幅减少，同时几乎不影响生成质量。

## 1. 方法动机
a) **为什么**: 长上下文 LLM（如 128K context）的 KV cache 在推理时占用大量 GPU 内存，限制了 batch size 和部署效率。
b) **痛点**: (1) 均匀截断/滑动窗口会丢失关键信息；(2) 逐 token 动态淘汰（如 H2O）增加了每步的计算开销；(3) 需要一种一次性、低开销的压缩方法。
c) **假设**: 注意力模式在 prompt 处理阶段就已经确定了哪些 token 是重要的，可以在生成前一次性筛选，无需在生成过程中动态调整。

## 2. 方法设计

### a) Pipeline
```
1. Prefill 阶段: 正常处理整个 prompt，得到完整 KV cache
2. 观察: 取 prompt 末尾的一个窗口（observation window, 如最后 64 tokens）
3. 投票: 用观察窗口中的 Q 对所有 K 计算注意力权重，统计每个位置被关注的程度
4. 选择: 每个注意力头独立选择 top-k 个高注意力位置的 KV
5. 拼接: 保留的 KV + 观察窗口的 KV = 压缩后的 KV cache
6. 生成: 使用压缩后的 KV cache 进行自回归生成
```

### b) 核心模块

**观察窗口 (Observation Window)**:
- Prompt 末尾的固定长度窗口（如 64 或 128 tokens）
- 用于"投票"——这些 token 的注意力模式代表了模型对 prompt 的理解
- 观察窗口本身的 KV 也被完整保留

**注意力投票 (Attention Voting)**:
- 对每个注意力头 h:
  - 计算观察窗口 Q 与所有 K 的注意力权重: `A_h = softmax(Q_window · K_all^T / √d)`
  - 对观察窗口维度求和: `score_h[i] = Σ_j A_h[j, i]` — 位置 i 被关注的总次数
  - 选择 top-k 个位置: `selected_h = topk(score_h, k)`
- 每个头的选择可以不同（per-head selection）

**压缩后的 KV Cache**:
- `KV_compressed_h = concat(KV_selected_h, KV_window)`
- 大小: k + window_size（远小于原始 prompt 长度）

### c) 关键公式
- 投票分数: `s_h[i] = Σ_{j∈window} softmax(q_j · k_i / √d)` for each head h
- 选择: `I_h = argtopk(s_h, k)`
- 压缩: `K'_h = K_h[I_h ∪ window]`, `V'_h = V_h[I_h ∪ window]`
- 压缩比: 从 n 个 token 压缩到 k + w 个（如 128K → 1K+128）

## 3. 对比
| 方法 | 压缩时机 | 每步开销 | Per-head | 质量 |
|------|----------|----------|---------|------|
| 滑动窗口 | 持续 | O(1) | 否 | 丢失远距离 |
| H2O | 每步动态 | O(n) | 是 | 好 |
| StreamingLLM | 持续 | O(1) | 否 | 中 |
| SnapKV | 一次性(prefill后) | O(1) | 是 | 好 |

## 4. 实验
- **长上下文基准**: 在 LongBench 上，SnapKV 将 KV cache 压缩 3-10x 后质量几乎无损
- **Needle-in-a-Haystack**: 在 128K 上下文中，SnapKV (1024+128 KV) 仍能准确检索
- **模型兼容**: 在 Llama-2-7B-chat, Mistral-7B-Instruct, LWM-Text-Chat-1M 上均有效
- **速度**: 生成阶段加速 3.6x（因为注意力计算量减少）
- **内存**: KV cache 内存减少 >10x
- **与 GQA 正交**: SnapKV 可以与 GQA 等 head sharing 方法叠加使用

## 5. 总结
a) **一句话**: SnapKV 利用 prompt 阶段注意力模式的稳定性，在生成前一次性对每个注意力头独立选择高注意力位置的 KV 进行缓存压缩，实现了低开销、高质量的 KV cache 压缩。
b) **速记 pipeline**: `Prefill → Observation Window Voting(per-head top-k) → Compress KV cache → Generate with small KV`
