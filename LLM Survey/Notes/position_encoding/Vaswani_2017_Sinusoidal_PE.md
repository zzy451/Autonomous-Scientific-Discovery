# Attention Is All You Need (Sinusoidal Positional Encoding)
**作者**: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin | **年份**: 2017 | **来源**: NeurIPS 2017 | **arXiv**: 1706.03762

## 0. 摘要翻译
本文提出了 Transformer 架构，一种完全基于注意力机制的序列转导模型，摒弃了循环和卷积结构。模型在机器翻译任务上取得了当时最优结果（WMT 2014 英德翻译 BLEU 28.4，英法翻译 BLEU 41.8），同时训练效率大幅提升。其中，正弦位置编码（Sinusoidal PE）作为 Transformer 的核心组件之一，为模型注入了序列位置信息。

## 1. 方法动机
a) **为什么提出**: Transformer 的自注意力机制天然是置换不变的（permutation-invariant），无法区分不同位置的 token，因此需要显式注入位置信息。
b) **现有痛点**: RNN/LSTM 通过递归结构隐式编码位置信息，但训练速度慢、难以并行化。需要一种既能编码位置又不依赖递归的方法。
c) **研究假设**: 使用不同频率的正弦/余弦函数可以编码绝对位置，同时由于三角函数的线性变换性质，模型也能学习到相对位置关系。

## 2. 方法设计
a) **pipeline**: 位置编码向量与输入 embedding 逐元素相加，注入到 encoder 和 decoder 的底层输入中。
b) **模块功能**: 为每个位置 pos 和维度 i 生成唯一的编码值，使模型能区分不同位置的 token。
c) **公式解释**:
   - $PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$
   - $PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$
   - 每个维度对应不同频率的正弦波（从 $2\pi$ 到 $10000 \cdot 2\pi$）
   - 对于固定偏移 $k$，$PE_{pos+k}$ 可以表示为 $PE_{pos}$ 的线性变换，理论上便于学习相对位置

## 3. 与其他方法对比
a) **本质不同**: 与 learned PE 相比，sinusoidal PE 无需训练参数，且理论上可外推至更长序列（虽然实践中效果有限）。
b) **创新点**: 首次在纯注意力架构中引入位置编码的概念；利用三角函数的数学性质（线性可表示性）来编码相对位置。
c) **适用场景**: 适用于固定长度或短上下文序列任务；作为后续所有位置编码研究的基准对照。

## 4. 实验表现
a) **验证方式**: 在 WMT 2014 英德/英法翻译任务上进行评估。
b) **关键数据**: Sinusoidal PE 与 learned PE 实验结果几乎相同（Table 3），作者选择 sinusoidal 是因为其可能的外推优势。
c) **局限性**: 
   - 实际外推能力有限，超出训练长度后性能显著下降
   - 绝对位置编码在长序列建模中效果不佳
   - 逐元素加法融合方式可能丢失位置与语义的交互信息

## 5. 总结
a) **一句话概括**: Sinusoidal PE 是 Transformer 中最早引入的位置编码方案，用固定的多频正弦/余弦函数为每个位置生成独特编码，开创了位置编码研究方向。
b) **速记 pipeline**: Input Embedding + Sinusoidal PE (element-wise add) → Self-Attention → FFN → Output
