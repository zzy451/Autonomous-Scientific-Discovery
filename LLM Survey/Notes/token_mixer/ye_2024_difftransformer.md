# Ye et al. 2024 - Differential Transformer

**论文信息**
- 标题: Differential Transformer
- 作者: Tianzhu Ye, Li Dong, Yuqing Xia, Yutao Sun, Yi Zhu, Gao Huang, Furu Wei
- 年份: 2024
- arXiv: 2410.05258

## 0. 摘要翻译
Transformer倾向于过度关注无关上下文，我们称之为"注意力噪声"。本文提出Differential Transformer，其关键是差分注意力机制。差分注意力将注意力分数计算为两个独立softmax注意力映射的差，类似于电子工程中的差分放大器消除噪声的方式。该方法有效减少了注意力噪声，促进了稀疏且有意义的注意力模式。

## 1. 方法动机
a) **为什么提出**: 标准softmax注意力会将非零概率分配给所有token（包括无关token），产生"注意力噪声"
b) **现有方法痛点**: softmax输出始终非负且归一化为1，无法真正地"忽略"不相关token
c) **研究假设**: 类比差分放大器，用两个注意力分布的差来消除共模噪声，保留有意义的注意力信号

## 2. 方法设计
a) **方法流程**:
   - 每个头使用两组独立的Q、K计算两个注意力图
   - 两个注意力图取差得到差分注意力
   - 差分注意力可以产生负值，有效"取消"无关token
   
b) **模块功能**:
   - **双路注意力**: $A_1 = \text{softmax}(Q_1K_1^T/\sqrt{d})$, $A_2 = \text{softmax}(Q_2K_2^T/\sqrt{d})$
   - **差分**: $\text{DiffAttn} = (A_1 - A_2)V$
   - **可学习缩放**: $\lambda$ 参数控制差分强度
   - 实际公式: $\text{DiffAttn}(X) = (\text{softmax}(Q_1K_1^T/\sqrt{d}) - \lambda \cdot \text{softmax}(Q_2K_2^T/\sqrt{d})) V$
   
c) **公式解释**:
   - 差分机制消除两个注意力图的共模噪声
   - λ可学习，初始化接近1
   - 等效于每个head有2个sub-head（Q_1K_1和Q_2K_2），head数减半但每个head有两路

## 3. 与其他方法对比
a) **本质不同**: 引入负注意力权重的机制（通过差分实现）
b) **创新点**: 
   - 差分放大器类比用于注意力去噪
   - 注意力权重可以为负（有效抑制噪声）
   - 无需额外复杂性（仅参数翻倍但head数减半）
c) **适用场景**: 需要精确注意力的任务（长上下文、信息检索）
d) **对比表格**:

| 特性 | Standard Attention | Differential Attention |
|------|-------------------|----------------------|
| 注意力权重 | 非负 | 可正可负 |
| 噪声处理 | 无 | 差分消除共模噪声 |
| 参数量 | 基线 | 相当（head数减半，每头2路） |
| 信噪比 | 较低 | 较高 |

## 4. 实验表现
a) **验证方式**: 语言建模、长上下文任务、信息检索、幻觉评估
b) **关键数据**: 在几乎所有任务上超过标准Transformer；显著减少幻觉
c) **优势场景**: 长上下文信息检索、减少幻觉、提升注意力质量
d) **局限性**: 计算量略有增加（两次softmax）；需要从头训练

## 5. 学习与应用
a) **开源情况**: Microsoft Research开源
b) **实现细节**: 与FlashAttention兼容；可嵌入现有框架
c) **迁移可能性**: 可替换任何标准注意力层

## 6. 总结
a) **一句话概括**: 通过两个softmax注意力图的差分消除注意力噪声，实现更精准的token交互，有效减少幻觉
b) **速记版pipeline**: Input → [Q1K1→Softmax1, Q2K2→Softmax2] → Diff(A1-λA2) → ×V → Output

**Token Mixer维度**: Attention with Negative——通过差分机制引入负注意力权重，消除注意力噪声
