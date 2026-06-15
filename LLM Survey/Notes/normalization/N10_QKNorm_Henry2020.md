# Query-Key Normalization for Transformers
**作者**: Alex Henry, Prudhvi Raj Dachapally, Shubham Pawar, Yuxuan Chen | **年份**: 2020 | **arxiv**: 2010.04245

## 0. 摘要翻译

Transformer 中的缩放点积注意力在训练过程中可能出现 softmax 饱和 (saturation) 问题，即注意力 logits 的绝对值过大导致 softmax 输出近似 one-hot，梯度消失。本文提出 Query-Key Normalization (QK-Norm)，在计算注意力之前对 Query 和 Key 向量进行 L2 归一化，有效防止 logits 爆炸，并引入可学习的温度参数替代固定的 $1/\sqrt{d_k}$ 缩放。实验在多个低资源翻译任务上平均提升约 0.9 BLEU。

## 1. 方法动机

### a) 为什么
标准 Transformer 注意力机制使用 $1/\sqrt{d_k}$ 缩放来控制点积的量级，但这一固定缩放因子无法适应训练过程中 Q、K 向量范数的动态变化。当 Q、K 的元素值在训练中增长时，点积 $QK^T$ 的值会变得极大。

### b) 痛点
- **Softmax 饱和**: $QK^T$ 中出现极大值时，softmax 进入饱和区，梯度趋近于零
- **注意力坍缩**: 注意力分布退化为 "winner-take-all" 模式，丧失多样性
- **训练不稳定**: 特别是在大模型、长序列、FP16 训练中，logit 爆炸导致 NaN/Inf
- **熵崩塌**: 注意力熵在训练过程中持续下降，模型表达力受限

### c) 假设
如果将 Q 和 K 归一化到单位球面上，点积的值域将被约束在 $[-1, 1]$，从根本上消除 logit 爆炸风险。同时，固定的 $1/\sqrt{d_k}$ 缩放可以被可学习参数替代，让模型自行学习最优的注意力锐度。

## 2. 方法设计

### a) Pipeline
1. 计算 Q = XW_Q, K = XW_K, V = XW_V（标准投影）
2. 对 Q 和 K 在 head 维度上进行 L2 归一化
3. 使用可学习标量 $g$ 替代 $1/\sqrt{d_k}$ 作为缩放因子
4. 计算 softmax(g * Q_norm * K_norm^T) * V

### b) 模块

**标准注意力**:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

**QK-Norm 注意力**:
$$\hat{Q} = \frac{Q}{\|Q\|_2}, \quad \hat{K} = \frac{K}{\|K\|_2}$$
$$\text{Attention}(Q, K, V) = \text{softmax}\left(g \cdot \hat{Q}\hat{K}^T\right)V$$

### c) 公式
- L2 归一化在每个 head 的 $d_k$ 维度上独立进行
- 归一化后 $\hat{Q}_i^T \hat{K}_j \in [-1, 1]$（余弦相似度）
- $g$ 是每个 head 一个的可学习标量，初始化为 $\sqrt{d_k}$（与标准缩放等价）
- 梯度可以正常流过 L2 归一化操作

## 3. 对比

| 特性 | 标准缩放注意力 | QK-Norm |
|------|--------------|---------|
| 缩放方式 | 固定 $1/\sqrt{d_k}$ | 可学习 $g$ |
| logit 范围 | 无上界 | $[-g, g]$ |
| softmax 饱和风险 | 高（随训练增加） | 低（有界） |
| 注意力多样性 | 可能退化 | 保持 |
| 额外参数 | 无 | 每个 head 1 个标量 |
| 计算开销 | 基线 | 增加 L2 归一化 |

**与其他注意力归一化的对比**:
| 方法 | 归一化位置 | 目标 |
|------|-----------|------|
| QK-Norm | 注意力输入 (Q, K) | 防止 logit 爆炸 |
| GroupNorm (Diff-Attn) | 注意力输出 | 控制输出尺度 |
| Softmax 温度 | softmax 内部 | 调节锐度 |

## 4. 实验

- **低资源翻译** (5 个 IWSLT 语言对): 平均提升 **+0.928 BLEU**
- 注意力分布可视化: QK-Norm 产生更分散、更丰富的注意力模式
- 注意力熵分析: QK-Norm 有效防止了训练中的熵崩塌
- **现代 LLM 采用**: Gemma 2/3 (Google), Qwen 3 (Alibaba), OLMo 2 (AI2), Chameleon (Meta) 均使用 QK-Norm
- **与 MLA 不兼容**: DeepSeek-V3 的 Multi-Latent Attention 不具体化完整 Q/K 向量，因此不使用 QK-Norm

## 5. 总结

### a) 一句话
QK-Norm 通过对 Query 和 Key 进行 L2 归一化并引入可学习温度参数，将注意力 logits 约束在有界范围内，防止 softmax 饱和，已被 Gemma 2/3、Qwen 3 等主流模型采纳。

### b) 速记 pipeline
```
Q, K → L2 归一化(Q), L2 归一化(K) → 余弦相似度 ∈ [-1,1] → 乘可学习 g → softmax → 加权 V
```

---
**阅读日期**: 2026-04-06
