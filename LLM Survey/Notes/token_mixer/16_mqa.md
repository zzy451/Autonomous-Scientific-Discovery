# Fast Transformer Decoding: One Write-Head is All You Need
**作者**: Noam Shazeer (Google) | **年份**: 2019 | **arxiv**: 1911.02150

## 0. 摘要翻译
多头注意力中的增量解码很慢，因为每一步的解码都需要从内存中加载整个键值缓存（KV cache），而KV cache的大小与头数、序列长度和维度成正比。批量大小受限于内存容量。本文提出多查询注意力（Multi-Query Attention, MQA），其中键和值在所有查询头之间共享（只有一个KV头），大幅减少了KV cache的大小和内存带宽需求，显著加速推理，同时模型质量仅有微小下降。

## 1. 方法动机
a) **为什么提出**: Transformer推理（自回归解码）的主要瓶颈不是计算而是内存带宽——每个解码步骤需要从GPU HBM加载全部KV cache到计算单元。
b) **现有痛点**: (1) MHA的KV cache随头数线性增长，占用大量内存；(2) 内存带宽限制了批量大小和推理吞吐量；(3) 解码是内存带宽受限（memory-bandwidth-bound）而非计算受限（compute-bound）的操作。
c) **研究假设**: 由于解码的瓶颈在于KV cache的内存读取而非计算，减少KV cache的数据量（共享KV头）可以直接提升解码速度，而质量损失可接受。

## 2. 方法设计
a) **Pipeline**: 标准MHA中，$h$个query头各有独立的$K_i$和$V_i$投影。MQA中，所有$h$个query头共享同一个$K$和$V$投影。

b) **模块功能**:
- **Multi-Query Attention**:
  - Query: $Q_i = XW_i^Q$（每个头独立，与MHA相同）
  - Key: $K = XW^K$（所有头共享同一个K）
  - Value: $V = XW^V$（所有头共享同一个V）
  - $\text{head}_i = \text{Attention}(Q_i, K, V)$
  - $\text{Output} = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$
- **KV cache减少**: 从$2 \times h \times d_k \times L$减少到$2 \times d_k \times L$，减少$h$倍
- **参数量变化**: 减少了$(h-1) \times 2 \times d_k \times d_{model}$个参数（KV投影矩阵），通常约减少总参数的几个百分点

c) **公式解释**:
- 核心变化仅在于KV投影的共享，计算流程不变
- 内存带宽需求: MHA需要加载$2hd_kL$个元素，MQA只需$2d_kL + hd_kL$（Q仍是多头）
- 当$h=32$、$d_k=128$时，KV cache减少32倍

## 3. 与其他方法对比
| 方面 | MQA | MHA | GQA |
|------|-----|-----|-----|
| KV头数 | 1 | $h$ | $g$ |
| KV cache | $2d_kL$ | $2hd_kL$ | $2gd_kL$ |
| 解码速度 | 最快 | 最慢 | 中间 |
| 质量 | 略低 | 最好 | 接近MHA |
| 参数效率 | 最高 | 基准 | 中间 |

## 4. 实验表现
- **WMT 2014 EN-DE翻译**: MQA质量损失<0.5 BLEU，推理速度提升显著
- **推理加速**: 在自回归解码上，MQA比MHA快数倍（具体取决于头数和批量大小）
- **训练速度**: 训练时由于MQA参数更少，每步略快
- **模型质量**: 在大模型上质量损失更小（大模型对共享KV更鲁棒）
- **后续影响**: PaLM、Falcon等模型采用MQA; Llama 2+、Mistral等采用GQA作为改进

## 5. 总结
a) **一句话概括**: MQA通过让所有query头共享单一KV头，将KV cache减少$h$倍，以极小的质量代价实现了自回归解码的大幅加速，开创了高效KV cache管理的研究方向。
b) **速记pipeline**: X → Q(h heads, 独立) + K(1头, 共享) + V(1头, 共享) → h个Attention并行 → Concat → Output
