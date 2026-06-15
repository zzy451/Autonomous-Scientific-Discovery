# MiniMax-01: Scaling Foundation Models with Lightning Attention
**作者**: MiniMax Team | **年份**: 2025 | **arxiv**: 2501.08313

## 0. 摘要翻译
MiniMax-01 是 MiniMax 发布的大规模基础模型，包含 456B 总参数（45.9B 激活）的 MoE 架构，支持 4M token 上下文长度。其核心创新在于 token mixer 设计：采用 Lightning Attention（线性注意力）与 Softmax Attention 7:1 混合的方案，即每 8 层中 7 层使用线性注意力、1 层使用标准 softmax 注意力。这是线性注意力在超大规模工业模型中的首次成功应用。

## 1. 方法动机
a) **为什么**: 4M token 上下文长度下，标准 softmax 注意力的 O(n²) 复杂度完全不可行。需要一种线性复杂度的注意力替代方案。
b) **痛点**: (1) 纯线性注意力在 recall 任务上弱于 softmax；(2) 纯 softmax 无法扩展到百万级上下文；(3) 需要找到最优的混合比例。
c) **假设**: 少量 softmax 注意力层（提供精确检索）+ 大量线性注意力层（提供高效长程建模）的混合可以在超长上下文下兼得质量和效率。

## 2. 方法设计

### a) 架构概览
- **总参数**: 456B (MoE), 激活参数 45.9B
- **层数**: 80 层
- **Token Mixer 混合**: 每 8 层中 7 层 Lightning Attention + 1 层 Softmax Attention
- **FFN**: MoE (每层 32 experts, top-2 routing)
- **上下文**: 训练 4M tokens, 支持更长推理

### b) Lightning Attention 层 (7/8 层)
- 基于 TransNormerLLM 的 Lightning Attention-2
- 线性注意力 + LRPE-d 位置编码
- IO-aware tiling: 块内用标准注意力，块间用累积 KV 状态
- 复杂度: O(n) 训练和推理
- 推理时: 维护固定大小的 KV 状态（不随序列长度增长）

### c) Softmax Attention 层 (1/8 层)
- 标准 dot-product attention + RoPE
- 提供精确的内容感知检索能力
- 这些层使用 KV cache（但只有 1/8 的层需要）
- 弥补线性注意力在 needle-in-a-haystack 等任务上的不足

### d) 关键设计决策
- **7:1 比例**: 经过大量实验确定的最优比例
  - 纯线性: recall 不足
  - 1:1 混合: 效率优势不够
  - 7:1: 质量接近纯 softmax，效率接近纯线性
- **KV cache 节省**: 只有 1/8 的层需要 KV cache → 在 4M 上下文下可行
- **训练效率**: Lightning Attention 保持恒定速度，不随序列长度增加

## 3. 对比
| 模型 | Token Mixer | 上下文 | 参数量 |
|------|------------|--------|--------|
| GPT-4 | Softmax (推测 MoE) | 128K | ~1.8T(推测) |
| Llama 3 405B | GQA Softmax | 128K | 405B |
| Jamba | Mamba + Attention | 256K | 52B(激活) |
| MiniMax-01 | Lightning(7) + Softmax(1) | 4M | 45.9B(激活) |

## 4. 实验
- **标准基准**: 在 MMLU, GSM8K, HumanEval 等上与 GPT-4o, Llama-3.1-405B 竞争力相当
- **长上下文**: 在 4M token 的 needle-in-a-haystack 中表现良好（得益于 softmax 层）
- **效率**: 4M 上下文下推理可行（纯 softmax 模型在此长度下不可行）
- **训练**: 在 12T tokens 上训练，Lightning Attention 使长序列训练高效
- **意义**: 首次证明线性注意力混合方案可以在 >400B 参数的工业模型中成功应用

## 5. 总结
a) **一句话**: MiniMax-01 通过 Lightning Attention 与 Softmax Attention 7:1 混合，在 456B MoE 模型上实现了 4M token 上下文，首次在工业规模验证了线性注意力的可行性。
b) **速记 pipeline**: `Input → [Lightning Attn(Linear, O(n)) × 7 → Softmax Attn(O(n²)) × 1] × 10 groups → MoE FFN → Output`
