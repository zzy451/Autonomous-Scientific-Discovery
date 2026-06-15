# NormFormer: Improved Transformer Pretraining with Extra Normalization
**作者**: Sam Shleifer, Jason Weston, Myle Ott | **年份**: 2021 | **arxiv**: 2110.09456

## 0. 摘要翻译
本文发现 Pre-LN Transformer 中存在梯度幅度不匹配问题：早期层的梯度远大于后期层。NormFormer 通过在每个 Transformer 层中引入三个针对性的归一化/缩放操作来平衡网络深度方向上的梯度流，以极小的计算开销（约 +0.4% 参数）获得显著的预训练效率提升。

## 1. 方法动机
- Pre-LN Transformer 虽然训练稳定，但存在**梯度幅度不匹配**问题
- 早期层接收到的梯度远大于后期层，导致早期层被"过度训练"
- 这种不均衡影响了模型的训练效率和最终性能
- 需要一种轻量级的修改来平衡各层的梯度流

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### 三项关键修改

#### 1) Head-wise Scaling（注意力头缩放）
- 在多头注意力的输出端，对每个注意力头应用可学习的缩放参数
- 控制不同注意力头贡献的信息量级
- 位置：Attention 输出、输出投影之前

#### 2) Post-Attention LayerNorm（注意力后 LN）
- 在自注意力输出之后（残差连接合并之前）增加一个额外的 LayerNorm
- 对注意力机制的输出进行归一化
- 位置：Attention -> **LN** -> Add

#### 3) Mid-FFN LayerNorm（FFN 中间 LN）
- 在 FFN 的第一个全连接层之后增加一个额外的 LayerNorm
- 位置：FFN_fc1 -> **LN** -> FFN_fc2

### 完整的 NormFormer 块结构
```
标准 Pre-LN:  LN -> Attn -> Add -> LN -> FFN -> Add
NormFormer:   LN -> Attn -> HeadScale -> LN_extra -> Add -> LN -> FC1 -> LN_extra -> FC2 -> Add
```

### 理论分析
- 三个修改点共同作用，使得梯度范数在网络深度方向上的分布变得更"平坦"
- 早期层不再接收过大的梯度，避免过度更新
- 总参数增加仅约 0.4%，计算开销可忽略

## 3. 与其他方法对比
| 方法 | 额外 Norm 位置 | 参数开销 | 梯度平衡 |
|------|---------------|---------|---------|
| Pre-LN | 无额外 | 0% | 差（早期层梯度大） |
| Post-LN | 无额外 | 0% | 差（梯度消失） |
| Sandwich-LN | 残差分支末端 | 极小 | 中等 |
| NormFormer | Attn 后 + FFN 中间 + Head Scale | ~0.4% | 好 |

## 4. 实验表现
- **125M - 2.7B 参数**：在不同规模上均有改进
- **预训练效率**：1.3B 模型达到基线 perplexity 速度快 24%
- **Perplexity**：固定计算预算下，perplexity 降低约 0.27
- **下游任务**：
  - Zero-shot：HellaSwag、PIQA 等任务上性能更强
  - Fine-tuning：GLUE 基准平均提升约 1.9%
- **对 CLM 和 MLM 均有效**：因果语言模型和掩码语言模型都受益
- 代码集成在 fairseq 库中

## 5. 总结
a) **一句话概括**：NormFormer 通过在 Attention 输出后、FFN 中间添加 LayerNorm 并引入 Head-wise Scaling，以极小代价平衡了 Pre-LN Transformer 的梯度分布。

b) **速记 pipeline**：`LN -> Attn -> HeadScale -> LN -> Add -> LN -> FC1 -> LN -> FC2 -> Add`
