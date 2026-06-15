# Ring Attention with Blockwise Transformers for Near-Infinite Context
**作者**: Hao Liu, Matei Zaharia, Pieter Abbeel | **年份**: 2023 | **arxiv**: 2310.01889

## 0. 摘要翻译
本文提出 Ring Attention，一种利用 blockwise Transformer 在多设备间分布式处理超长序列的方法。通过将输入序列分块分配到不同设备上，并以环形通信模式传递 KV 块，Ring Attention 可以在不丢失信息的情况下将上下文长度扩展到与设备数量成正比，同时完全隐藏通信开销。

## 1. 方法动机
a) **为什么**: 单设备内存限制了 Transformer 可处理的最大序列长度。即使有 FlashAttention，单 GPU 仍无法处理百万级 token。
b) **痛点**: (1) 序列并行方法（如 Megatron-SP）需要额外的 all-gather 通信；(2) 简单的序列分片会破坏注意力的全局性；(3) 需要一种既能保持精确注意力又能跨设备扩展的方案。
c) **假设**: 通过环形通信拓扑，每个设备可以在计算当前块注意力的同时异步接收下一个 KV 块，从而完全重叠计算和通信。

## 2. 方法设计

### a) Pipeline
```
设备 0: [Q_0, K_0, V_0]  →  计算 Attn(Q_0, K_0) → 接收 K_1,V_1 → 计算 Attn(Q_0, K_1) → ...
设备 1: [Q_1, K_1, V_1]  →  计算 Attn(Q_1, K_1) → 接收 K_2,V_2 → 计算 Attn(Q_1, K_2) → ...
设备 2: [Q_2, K_2, V_2]  →  计算 Attn(Q_2, K_2) → 接收 K_0,V_0 → 计算 Attn(Q_2, K_0) → ...
... (环形传递，每个设备最终看到所有 KV 块)
```

### b) 核心模块

**Blockwise Parallel Transformer**:
- 将 FlashAttention 的分块计算推广到跨设备场景
- 每个设备持有序列的一个连续块
- Q 块固定在本地，KV 块在设备间环形传递

**环形通信 (Ring Communication)**:
- N 个设备排成逻辑环
- 每一步: 设备 i 将自己的 KV 块发送给设备 (i+1) % N
- 同时接收来自设备 (i-1) % N 的 KV 块
- 经过 N-1 步后，每个设备已经看到所有 KV 块

**计算-通信重叠**:
- 关键洞察: 每个 KV 块的注意力计算时间 ≥ KV 块的传输时间
- 因此可以完全重叠: 在计算当前 KV 块注意力的同时，异步传输下一个 KV 块
- 通信开销接近零

**在线 Softmax 聚合**:
- 使用 FlashAttention 的在线 softmax 技巧
- 每处理一个 KV 块后更新: `O_new = (e^{m_old - m_new} · O_old · l_old + e^{m_cur - m_new} · O_cur · l_cur) / l_new`
- 数值稳定且精确等价于全序列注意力

### c) 关键公式
- 每设备内存: O(S/N) — S 是总序列长度，N 是设备数
- 最大上下文长度: S_max = N × S_per_device
- 通信量: 每步传输 O(S/N × d) 的 KV 块
- 总计算量: 与标准注意力相同，只是分布在 N 个设备上

## 3. 对比
| 方法 | 最大序列长度 | 通信开销 | 精确注意力 | 内存效率 |
|------|-------------|----------|-----------|----------|
| 标准注意力 | 受单 GPU 限制 | — | 是 | O(n²) |
| FlashAttention | 受单 GPU 限制 | — | 是 | O(n) |
| Megatron-SP | 多 GPU | all-gather | 是 | 中 |
| Ring Attention | N × 单 GPU | 可完全隐藏 | 是 | O(n/N) |

## 4. 实验
- **扩展性**: 在 TPU 上验证，上下文长度随设备数线性扩展
- **百万级上下文**: 使用 32 个 TPU，实现 >1M token 的训练和推理
- **通信隐藏**: 实测通信开销 <5%（几乎完全被计算重叠）
- **质量**: 与标准注意力数学等价，无质量损失
- **训练**: 在长文档语料上训练，困惑度随上下文长度增加持续下降
- **后续影响**: Ring Attention 的思想被广泛采用于长上下文 LLM 训练（如 Llama 3 的 128K 上下文训练）

## 5. 总结
a) **一句话**: Ring Attention 通过在多设备间环形传递 KV 块并与注意力计算完全重叠通信，实现了上下文长度随设备数线性扩展的精确注意力，是长上下文 LLM 训练的基础设施级创新。
b) **速记 pipeline**: `Sequence → Split to N devices → [Compute Attn(Q_local, KV_current) ‖ Send/Recv KV_next] × (N-1) rounds → Online Softmax Merge → Output`
