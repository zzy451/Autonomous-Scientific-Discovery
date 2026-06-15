# Attention Is All You Need
**作者**: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin | **年份**: 2017 | **arxiv**: 1706.03762

## 0. 摘要翻译
当时主流的序列转换模型基于复杂的循环或卷积神经网络，包含编码器和解码器。性能最佳的模型还通过注意力机制连接编码器和解码器。本文提出了一种新的简单网络架构——Transformer，完全基于注意力机制，摒弃了循环和卷积。在两个机器翻译任务上的实验表明，该模型在质量上更优，同时更具可并行性，训练时间显著减少。模型在WMT 2014英德翻译任务上达到28.4 BLEU，超越现有最佳结果（包括集成模型）超过2个BLEU分。在WMT 2014英法翻译任务上，模型在8个GPU上训练3.5天后建立了新的单模型最佳BLEU分数41.8。

## 1. 方法动机
a) **为什么提出**: 循环神经网络（RNN/LSTM/GRU）的顺序计算特性限制了并行化能力，在长序列上训练效率低下。即使存在各种优化（如分解技巧、条件计算），顺序计算的根本约束依然存在。
b) **现有痛点**: (1) RNN的顺序依赖使得无法在序列维度上并行化；(2) 长距离依赖建模困难，信号需要经过多个时间步传播；(3) 注意力机制虽已被使用但仍与RNN结合。
c) **研究假设**: 纯注意力机制可以替代循环结构完成序列建模任务，同时获得更好的并行性和性能。

## 2. 方法设计
a) **Pipeline**: Encoder-Decoder架构。Encoder由N=6个相同层堆叠，每层包含Multi-Head Self-Attention + Feed-Forward Network（FFN），均带残差连接和LayerNorm。Decoder类似但增加了Masked Self-Attention和Cross-Attention。

b) **模块功能**:
- **Scaled Dot-Product Attention**: $\text{Attention}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$。缩放因子$\sqrt{d_k}$防止点积过大导致softmax梯度消失。
- **Multi-Head Attention**: 将Q、K、V分别通过h个不同的线性投影，并行计算h个注意力，然后拼接并再次投影。$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,...,\text{head}_h)W^O$，其中$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$。使用h=8个头，$d_k = d_v = d_{model}/h = 64$。
- **Position-wise FFN**: $\text{FFN}(x) = \max(0, xW_1+b_1)W_2+b_2$，两层线性变换中间用ReLU激活，内部维度$d_{ff}=2048$。
- **Positional Encoding**: 使用正弦/余弦函数编码位置信息，$PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}})$。

c) **公式解释**: 注意力本质是查询（Query）与键（Key）的兼容性函数加权值（Value）的过程。Multi-Head允许模型同时关注不同位置的不同表示子空间。

## 3. 与其他方法对比
| 方面 | Transformer | RNN (LSTM/GRU) | CNN |
|------|-------------|----------------|-----|
| 序列操作复杂度 | $O(1)$ | $O(n)$ | $O(1)$或$O(\log n)$ |
| 每层计算复杂度 | $O(n^2 \cdot d)$ | $O(n \cdot d^2)$ | $O(k \cdot n \cdot d^2)$ |
| 最大路径长度 | $O(1)$ | $O(n)$ | $O(\log_k(n))$ |
| 并行化 | 完全并行 | 无法并行 | 完全并行 |

当$n < d$时（通常情况），Self-Attention比循环层更快。

## 4. 实验表现
- **WMT 2014 EN-DE**: 28.4 BLEU（big model），超越所有之前发布的模型和集成模型
- **WMT 2014 EN-FR**: 41.0 BLEU（单模型），训练成本仅为之前最佳模型的1/4
- **训练效率**: base model在8块P100 GPU上训练12小时；big model训练3.5天
- **English Constituency Parsing**: 在半监督设置下达到与最佳模型相当的结果，验证了泛化能力

## 5. 总结
a) **一句话概括**: Transformer提出了完全基于Multi-Head Self-Attention的encoder-decoder架构，以$O(1)$的最大路径长度和完全并行化能力替代了RNN，成为现代深度学习的基础架构。
b) **速记pipeline**: Input → Embedding + PosEnc → [Multi-Head Self-Attn → Add&Norm → FFN → Add&Norm] × N → Output
