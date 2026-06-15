# Sinusoidal Positional Encoding
**论文**: Attention Is All You Need
**作者**: Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin
**年份**: 2017
**会议**: NeurIPS 2017
**arXiv**: 1706.03762

## 核心思想
Transformer 架构因使用 self-attention 而非 RNN/CNN，不具备对序列顺序的归纳偏置。Sinusoidal PE 通过固定的正弦/余弦函数为每个位置生成唯一的编码向量，注入到输入 embedding 中。

## 方法细节

### 数学公式
$$PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$$
$$PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$

- pos: token 在序列中的位置 (0, 1, 2, ...)
- i: 维度索引 (0, 1, ..., d_model/2 - 1)
- d_model: embedding 维度

### 关键设计动机
1. **相对位置可学习性**: 对任意固定偏移 k，PE_{pos+k} 可以表示为 PE_{pos} 的线性函数，使模型可以学习相对位置的注意力
2. **外推能力**: sin/cos 函数对任意输入有定义，理论上可外推到训练未见长度
3. **无额外参数**: 完全确定性，不引入可训练参数

### 与 Learned PE 的对比
- 论文实验表明两者性能"几乎一致"
- 选择 sinusoidal 是因为其理论上的外推能力
- 后续工作（如 BERT）普遍采用 learned PE

## Position Encoding 维度分析

### 分类
- **类型**: Absolute Position Encoding
- **注入方式**: 加到输入 embedding 上（encoder 和 decoder 底层）
- **参数量**: 零（无可训练参数）
- **长度外推**: 理论上支持，但实践中效果有限

### 局限性
1. 不直接建模 token 之间的相对距离
2. 实际外推能力弱于理论预期
3. 位置信息在深层网络中会逐渐"稀释"

## 影响与后续
- 奠定了 Transformer 位置编码的基础范式
- 后续 RoPE 继承了旋转/频率的思想
- ALiBi、FIRE 等方法从不同角度改进
