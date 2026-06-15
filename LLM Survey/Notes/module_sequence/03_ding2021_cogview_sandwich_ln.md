# CogView: Mastering Text-to-Image Generation via Transformers (Sandwich-LN)
**作者**: Ming Ding, Zhuoyi Yang, Wenyi Hong, Wendi Zheng, Chang Zhou, Da Yin, Junyang Lin, Xu Zou, Zhou Shao, Hongxia Yang, Jie Tang | **年份**: 2021 | **arxiv**: 2105.13290 | **发表**: NeurIPS 2021

## 0. 摘要翻译
CogView 是首个基于 Transformer 的大规模文本到图像生成模型（40 亿参数）。在训练如此大规模的模型时，作者遇到了严重的训练不稳定性（NaN loss），并提出了两项关键技术来解决：Sandwich LayerNorm (Sandwich-LN) 和 Precision Bottleneck Relaxation (PB-relax)。这些技术使得模型能够在几乎完全使用 FP16 精度的条件下稳定训练。

## 1. 方法动机
- 训练 4B 参数的 Pre-LN Transformer 使用 FP16 混合精度时，通常在 1000 步内就会出现 NaN loss
- 深层 Transformer 中隐藏状态值会逐层膨胀，达到 10^4 ~ 10^5 的量级
- 溢出频繁发生在两个位置：块末尾的 LayerNorm 和注意力机制的 softmax
- 需要不改变模型表达能力的前提下解决数值稳定性问题

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### Sandwich LayerNorm
- **标准 Pre-LN**：`LN -> SubLayer -> Add`（残差块内仅在子层前有一个 LN）
- **Sandwich-LN**：`LN -> SubLayer -> LN -> Add`（在残差分支的输出端额外增加一个 LN）
- **原理**：标准 Pre-LN 允许值逐层增长（通过残差累加），额外的 LN 确保每层输入值保持在合理范围内
- **效果**：限制了"逐层值膨胀"问题

### Precision Bottleneck Relaxation (PB-relax)
- 对 LayerNorm 的输入进行预缩放：`LayerNorm(x)` 等价于 `LayerNorm(x / max(|x|))`
- 对注意力分数进行分解缩放：将 `softmax(QK^T/sqrt(d))` 改为分别缩放 Q 和 K
- 引入较大常数 alpha（如 32）进一步降低中间值量级

### 模块排列结构
```
Pre-LN（标准）: x + SubLayer(LN(x))
Sandwich-LN:    x + LN(SubLayer(LN(x)))
```

## 3. 与其他方法对比
| 方法 | 结构 | 训练稳定性 | 应用场景 |
|------|------|-----------|---------|
| Post-LN | SubLayer -> LN | 差（深层） | 原始 Transformer |
| Pre-LN | LN -> SubLayer | 中等（值仍可膨胀） | GPT 系列 |
| Sandwich-LN | LN -> SubLayer -> LN | 好（值受控） | 超大模型 FP16 训练 |

- Sandwich-LN 可视为 Pre-LN 的加强版，在残差分支的两端都加 LN
- 与 NormFormer 的思路类似但更简单直接

## 4. 实验表现
- **4B 参数 CogView**：使用 Sandwich-LN + PB-relax 成功消除了 NaN loss
- **8.3B CogView-large**：同样稳定训练
- **10B GLM**：验证了技术的通用性
- 在几乎完全 FP16 精度下完成训练，大幅降低显存和计算开销
- 生成质量在当时的文本到图像任务中达到最优

## 5. 总结
a) **一句话概括**：Sandwich-LN 在 Pre-LN 的残差分支输出端额外增加 LayerNorm，配合 PB-relax 缩放技术，解决了超大 Transformer FP16 训练中的数值溢出问题。

b) **速记 pipeline**：`x + LN(Attn(LN(x))) -> x + LN(FFN(LN(x)))` (Sandwich-LN 结构)
