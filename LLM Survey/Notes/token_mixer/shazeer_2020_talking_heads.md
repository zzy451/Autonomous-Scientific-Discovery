# Talking-Heads Attention
**作者**: Noam Shazeer, Zhenzhong Lan, Youlong Cheng, Nan Ding, Le Hou | **年份**: 2020 | **arxiv**: 2003.02436

## 0. 摘要翻译
本文提出 Talking-Heads Attention，在标准多头注意力的基础上引入两个跨头的可学习线性投影：一个在 softmax 之前作用于注意力 logits（logit 空间），一个在 softmax 之后作用于注意力权重（权重空间）。这使得各注意力头之间可以"交流"信息，而非完全独立运算。

## 1. 方法动机
a) **为什么提出**：标准 MHA 中各头完全独立计算，头与头之间没有信息交换。这限制了注意力的表达能力——每个头只能在自己的子空间中工作。
b) **现有痛点**：MHA 的头数通常受限于 d_model/d_head，增加头数需要减小 head dimension，导致每个头的表达能力下降。
c) **研究假设**：如果允许头之间在注意力计算过程中交换信息（而非仅在最终拼接时合并），可以用更少的头达到更好的效果。

## 2. 方法设计
a) **Pipeline**：
标准 MHA: Q,K → logits → softmax → weights → ×V → concat → output
Talking-Heads: Q,K → logits → **W_l (跨头线性)** → softmax → **W_w (跨头线性)** → ×V → concat → output

两个关键投影：
- $P_l \in \mathbb{R}^{h_k \times h}$：将 logit 空间从 $h_k$ 个头映射到 $h$ 个头（softmax 前）
- $P_w \in \mathbb{R}^{h \times h_v}$：将 weight 空间从 $h$ 个头映射到 $h_v$ 个头（softmax 后）

b) **关键创新**：头数可以在 Q/K 投影（$h_k$）、softmax（$h$）、V 投影（$h_v$）三个阶段不同，实现更灵活的容量分配。
c) **计算开销**：额外参数量仅为 $h_k \times h + h \times h_v$（通常 <0.1% 模型参数），几乎可忽略。

## 3. 与其他方法对比
| 方法 | 头间交互 | 额外参数 | 适用场景 |
|------|---------|---------|---------|
| MHA | 无（完全独立） | 0 | 通用基线 |
| Talking-Heads | 有（线性投影） | 极少 | 需要更丰富注意力模式 |
| MQA/GQA | 共享 KV（减少头） | 减少参数 | 推理效率优化 |
| MoH | MoE 路由选择头 | 路由器参数 | 动态头选择 |

## 4. 实验
在翻译和语言建模任务上验证，Talking-Heads 在多数配置下优于标准 MHA，特别是在头数较多时改进更明显。改进幅度约 0.2-0.5 BLEU。

## 5. 总结
a) **一句话**：通过在 softmax 前后添加跨头线性投影，让注意力头之间可以交流信息。
b) **速记 pipeline**：QK logits → 跨头投影1 → softmax → 跨头投影2 → 乘V → 输出
