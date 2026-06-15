# N-07: CogView / Sandwich LayerNorm (Ding et al. 2021)

> **论文**: CogView: Mastering Text-to-Image Generation via Transformers
> **作者**: Ming Ding, Zhuoyi Yang, Wenyi Hong, Wendi Zheng, Chang Zhou, Da Yin, Junyang Lin, Xu Zou, Zhou Shao, Hongxia Yang, Jie Tang
> **发表**: NeurIPS 2021 | arXiv:2105.13290
> **关键词**: Sandwich LayerNorm, 训练稳定性, FP16, 文生图

---

## 核心思想

为训练大规模文生图 Transformer (40亿参数)，提出 **Sandwich LayerNorm (Sandwich-LN)** 和 **PB-Relaxation** 来解决 FP16 训练中的数值不稳定问题。

## Sandwich LayerNorm

### 动机
在标准 Pre-LN 或 Post-LN 架构中，使用 FP16 训练深层 Transformer 时频繁出现 NaN (数值溢出)。原因是：
- 多头注意力和 FFN 的输出可能超出 FP16 的表示范围
- 标准 LN 位置不足以约束这些输出的数值范围

### 方法
在每个子层（Attention / FFN）的**输入和输出**都添加 LayerNorm：

$$\text{Output} = x + \text{LayerNorm}_2(\text{SubLayer}(\text{LayerNorm}_1(x)))$$

这相当于在 Pre-LN 的基础上，在子层**输出**处再加一层 LN，形成"三明治"结构。

### 效果
- 有效消除了 FP16 训练中的 NaN 损失
- 约束了子层输出的数值范围
- 允许使用纯 FP16 训练 4B 参数的 Transformer

## PB-Relaxation (Precision Bottleneck Relaxation)

与 Sandwich-LN 配合使用的辅助技术，放宽注意力机制中的精度瓶颈。

## 与后续工作的关系

| 方法 | 归一化位置 | 特点 |
|------|-----------|------|
| Post-LN | 残差后 | 原始设计 |
| Pre-LN | 子层前 | 现代标准 |
| Sandwich-LN | 子层前+后 | CogView 提出 |
| Sub-LN/MAGNETO | 子层内部 | 更精细的控制 |
| Peri-LN | 外围 | 最新研究 |
| Gemma 2 | Pre+Post RMSNorm | 工业实践 |

Sandwich-LN 的思想在 2024 年被 Gemma 2 以 "Pre+Post RMSNorm" 的形式重新采用，验证了在子层输入输出都归一化的有效性。

## 在综述中的定位

Sandwich-LN 是 LN 位置研究的重要节点，展示了"更多归一化 = 更好的数值稳定性"的思路。它连接了 Pre-LN 和后续的 Sub-LN、Peri-LN 等更复杂的位置策略。

---

**阅读日期**: 2026-04-05
