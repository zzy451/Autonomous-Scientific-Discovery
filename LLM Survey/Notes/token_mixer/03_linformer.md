# Linformer: Self-Attention with Linear Complexity
**作者**: Zhanpeng Wang, Matei Zaharia, Haonan Wang | **年份**: 2020 | **arxiv**: 2006.04768

## 0. 摘要翻译
大型预训练Transformer模型在各种NLP任务上取得了巨大成功。然而，这些模型中self-attention机制的时间和空间复杂度为$O(n^2)$。本文证明了self-attention机制可以用低秩矩阵近似，并提出Linformer模型，将self-attention的时间和空间复杂度从$O(n^2)$降低至$O(n)$（线性复杂度）。实验表明Linformer在效率和有效性之间取得了良好平衡。

## 1. 方法动机
a) **为什么提出**: Transformer的self-attention的$O(n^2)$复杂度是长序列处理的主要瓶颈，限制了输入长度和模型规模。
b) **现有痛点**: (1) 内存消耗随序列长度二次增长；(2) 计算成本限制了实际可用的上下文窗口长度；(3) 之前的高效注意力方法（如Sparse Transformer）仍需要$O(n\sqrt{n})$复杂度。
c) **研究假设**: 注意力矩阵$P = \text{softmax}(QK^T/\sqrt{d_k})$是低秩的。通过实验验证，大部分信息集中在少数几个最大的奇异值上，因此可以用低秩投影近似。

## 2. 方法设计
a) **Pipeline**: 在标准Transformer架构中，将self-attention中的Key和Value矩阵通过线性投影降维。

b) **模块功能**:
- **低秩投影**: 将$n \times d$的Key和Value矩阵通过$k \times n$的投影矩阵$E_i$和$F_i$映射到$k \times d$维度（$k \ll n$）。
- **线性注意力计算**: $\text{head}_i = \text{Attention}(Q W_i^Q, E_i K W_i^K, F_i V W_i^V)$
- **投影维度$k$**: 与序列长度$n$无关，是固定的超参数（实验中$k=128$或$k=256$足够）。

c) **公式解释**:
- 原始注意力: $\text{Attn}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$，其中$QK^T$是$n \times n$矩阵
- Linformer: $\tilde{K} = E \cdot K$（$k \times d$），$\tilde{V} = F \cdot V$（$k \times d$），$\text{Attn} = \text{softmax}(\frac{Q\tilde{K}^T}{\sqrt{d_k}})\tilde{V}$
- 注意力矩阵从$n \times n$变为$n \times k$，实现线性复杂度

**参数共享策略**: (1) Headwise sharing: 所有头共享投影矩阵; (2) Key-Value sharing: K和V共享投影矩阵; (3) Layerwise sharing: 所有层共享投影矩阵。

## 3. 与其他方法对比
| 方面 | Linformer | Transformer | Reformer | Performer |
|------|-----------|-------------|----------|-----------|
| 复杂度 | $O(nk)$ ≈ $O(n)$ | $O(n^2)$ | $O(n\log n)$ | $O(n)$ |
| 近似方式 | 低秩投影 | 精确 | LSH | 随机特征 |
| 适用场景 | 编码器 | 通用 | 通用 | 通用 |
| 因果掩码支持 | 困难 | 原生 | 原生 | 需修改 |

**局限性**: Linformer的投影矩阵维度固定，不能直接支持因果注意力（decoder），主要适用于编码器场景。

## 4. 实验表现
- **预训练任务（RoBERTa）**: 在GLUE基准的8个任务中，Linformer-k=128与标准Transformer性能相当（差距<1%），同时速度提升约2-4倍
- **推理速度**: 当序列长度为512时，Linformer约快1.5倍；序列长度为1024时约快2.5倍；更长序列优势更大
- **内存消耗**: 线性增长而非二次增长
- **低秩验证**: 对已训练好的BERT模型分析，前128个奇异值解释了90%以上的注意力矩阵信息

## 5. 总结
a) **一句话概括**: Linformer通过证明注意力矩阵的低秩性质，用固定维度$k$的线性投影将K/V压缩，实现$O(n)$复杂度的self-attention，但主要适用于编码器场景。
b) **速记pipeline**: Input → Q + Project(K,V)→k维 → softmax(Q·K̃ᵀ/√d)·Ṽ → Output
