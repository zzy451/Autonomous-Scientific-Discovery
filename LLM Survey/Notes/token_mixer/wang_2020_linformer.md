# Wang et al. 2020 - Linformer: Self-Attention with Linear Complexity

**论文信息**
- 标题: Linformer: Self-Attention with Linear Complexity
- 作者: Sinong Wang, Belinda Z. Li, Madian Khabsa, Han Fang, Hao Ma
- 年份: 2020
- arXiv: 2006.04768

## 0. 摘要翻译
大型Transformer模型在NLP领域取得了巨大进展，但自注意力机制的O(N²)时间和空间复杂度限制了其在长序列上的应用。我们证明了自注意力机制是低秩的，并提出Linformer——通过将Key和Value矩阵投影到低维空间，将自注意力的时间和空间复杂度降低到O(N)。

## 1. 方法动机
a) **为什么提出**: 自注意力矩阵的O(N²)复杂度限制了处理长序列的能力
b) **现有方法痛点**: 即使注意力矩阵在实践中是低秩的，标准实现仍计算完整的N×N矩阵
c) **研究假设**: 注意力矩阵可以通过低秩近似来有效逼近，无需计算完整矩阵

## 2. 方法设计
a) **方法流程**:
   - 将Key和Value通过线性投影从N维降到k维（k << N）
   - 用降维后的K、V计算注意力
   - 原始N×N注意力矩阵被近似为N×k矩阵

b) **模块功能**:
   - 投影矩阵 $E, F \in \mathbb{R}^{k \times N}$
   - $\tilde{K} = EK$, $\tilde{V} = FV$ （将序列长度维度从N压缩到k）
   - $\text{Attention}(Q, \tilde{K}, \tilde{V}) = \text{softmax}(\frac{Q\tilde{K}^T}{\sqrt{d}})·\tilde{V}$
   
c) **公式解释**:
   - 复杂度从 O(N²·d) 降到 O(N·k·d)，当k为常数时为O(N)
   - 投影矩阵可以是学习的或固定的（随机/正交投影）
   - 可跨层/跨头共享投影矩阵进一步减少参数

## 3. 与其他方法对比
a) **本质不同**: 通过压缩KV序列长度维度实现线性化，而非修改注意力计算本身
b) **创新点**: 理论证明注意力矩阵低秩性 + 简单线性投影实现O(N)
c) **适用场景**: 固定长度编码器任务（BERT类），长文档理解
d) **对比表格**:

| 特性 | Transformer | Linformer | Performer |
|------|-------------|-----------|-----------|
| 复杂度 | O(N²d) | O(Nkd) | O(Nrd) |
| 近似方式 | 精确 | 低秩投影 | 核近似 |
| 是否数据依赖 | - | 否（固定投影） | 否（随机特征） |
| 解码器适用 | 是 | 困难 | 是 |

## 4. 实验表现
a) **验证方式**: GLUE/SQuAD等NLU基准
b) **关键数据**: k=128即可达到接近原始Transformer的性能；推理加速约2-3倍
c) **优势场景**: 长序列编码器模型
d) **局限性**: 不太适用于自回归解码器（投影矩阵依赖于固定的最大序列长度）；无法处理变长序列

## 5. 学习与应用
a) **开源情况**: Facebook开源
b) **实现细节**: k通常取128-256；投影矩阵可共享以节省参数
c) **迁移可能性**: 概念简单但在LLM解码场景受限，更适合编码器

## 6. 总结
a) **一句话概括**: 通过将KV矩阵投影到低维空间，将自注意力复杂度从O(N²)降到O(N)，但主要适用于编码器场景
b) **速记版pipeline**: Input → Q + Project(K)↓ + Project(V)↓ → Low-rank Attention → Output

**Token Mixer维度**: Linear Attention方案，通过低秩近似实现线性复杂度，适用于编码器但不适合自回归LLM
