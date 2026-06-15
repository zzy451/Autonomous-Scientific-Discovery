# TransNormerLLM: A Faster and Better Large Language Model with Improved TransNormer
**作者**: Zhen Qin, Dong Li, Weigao Sun, Weixuan Sun, Xuyang Shen, Xiaodong Han, Yunshen Wei, Baohong Lv, Xiao Luo, Yu Qiao, Yiran Zhong | **年份**: 2023 | **arxiv**: 2307.14995

## 0. 摘要翻译
本文提出 TransNormerLLM，第一个在准确性和效率上均超越传统 softmax 注意力模型的线性注意力大语言模型。该架构从 TransNormer 演化而来，引入了位置编码改进、线性注意力加速（Lightning Attention）、门控机制、张量归一化等关键改进，并在模型训练中采用了 LRPE（线性化相对位置编码）和新的 token 归一化方案。

## 1. 方法动机
a) **为什么**: 线性注意力理论上具有 O(n) 复杂度优势，但实际 LLM 中一直无法匹敌 softmax 注意力的质量。
b) **痛点**: (1) 线性注意力的因果版本无法利用矩阵乘法并行，导致实际速度慢；(2) 线性注意力缺乏有效的位置编码方案；(3) 训练不稳定。
c) **假设**: 通过系统性改进（位置编码、归一化、门控、IO 感知实现），线性注意力可以在 LLM 规模上超越 softmax 注意力。

## 2. 方法设计

### a) Pipeline
TransNormer → TransNormerLLM 的关键改进:
1. 位置编码: DiagAttention → LRPE (Linearized Relative Positional Encoding) → LRPE-d (带指数衰减)
2. 门控: 引入 GLA (Gated Linear Attention) 风格的门控
3. 归一化: SimpleRMSNorm 替代 LayerNorm，引入 SRMSNorm
4. 线性注意力加速: Lightning Attention

### b) 核心模块

**LRPE-d (Linearized Relative Positional Encoding with decay)**:
- 在线性注意力中引入相对位置信息
- 通过指数衰减因子控制远距离 token 的影响
- `A_{ij} = φ(q_i)^T φ(k_j) · λ^{i-j}` (λ < 1 为衰减因子)

**Lightning Attention**:
- 将因果线性注意力的计算分为 intra-block（块内，用常规注意力）和 inter-block（块间，用累积 KV 状态）
- IO-aware tiling 策略，最大化 GPU 利用率
- 实现恒定内存消耗，不随序列长度增长

**门控线性注意力**:
- `O = Gate ⊙ LinearAttn(Q, K, V)`
- Gate 由输入经线性变换 + Swish 激活得到

### c) 关键公式
- 线性注意力: `O_i = Σ_j φ(q_i)^T φ(k_j) · v_j / Σ_j φ(q_i)^T φ(k_j)`
- Lightning Attention 分块: 块内用 `Q_b K_b^T V_b`，块间用累积状态 `S_b = Σ_{b'<b} K_{b'}^T V_{b'}`
- 输出: `O_b = Q_b S_b + mask(Q_b K_b^T) V_b`

## 3. 对比
| 模型 | 注意力类型 | 复杂度 | 位置编码 | 门控 |
|------|-----------|--------|----------|------|
| Transformer | Softmax | O(n²) | RoPE | 无 |
| RWKV | Linear (WKV) | O(n) | 时间衰减 | Token shift |
| RetNet | Linear + 衰减 | O(n) | xPos | 无 |
| TransNormerLLM | Linear + LRPE-d | O(n) | LRPE-d | GLA 门控 |

## 4. 实验
- **规模**: 385M, 1B, 7B 参数
- **训练数据**: 自建中英文混合语料，6TB+
- **与 Transformer 对比**: TransNormerLLM-7B 在多个基准上超越同规模 Transformer LLM
- **速度**: 在长序列上训练速度显著快于 softmax attention（Lightning Attention 的贡献）
- **后续**: MiniMax-01 (456B MoE) 采用了 Lightning Attention + Softmax 7:1 混合方案，验证了该技术路线的工业可行性

## 5. 总结
a) **一句话**: TransNormerLLM 通过 LRPE-d 位置编码、Lightning Attention IO 感知加速和门控机制，首次证明线性注意力 LLM 可以在质量和效率上同时超越 softmax 注意力 LLM。
b) **速记 pipeline**: `Input → SRMSNorm → [LRPE-d + GatedLinearAttn + LightningAttn] → SRMSNorm → SwiGLU FFN → Output`
