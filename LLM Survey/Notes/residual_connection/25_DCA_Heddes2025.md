# DeepCrossAttention: Supercharging Transformer Residual Connections

**论文信息**: Heddes, J., et al. (UC Irvine, USC, Google Research) (2025)
**arXiv**: 2502.06785 | **会议**: ICML 2025
**分类**: Depth (跨层注意力)

## 核心思想
DeepCrossAttention (DCA) 用可学习的、输入依赖的权重来替代标准残差连接中的固定加法。通过三个独立的 Generalized Residual Network (GRN) 模块在深度维度上进行交叉注意力，实现动态的跨层信息融合。

## 数学公式
标准残差: x_{l+1} = x_l + F(x_l)  （固定权重1的加法）
DCA: x_{l+1} = sum_{i=0}^{l} w_i(x) * h_i, 其中 w_i 是输入依赖的权重

三个 GRN 模块分别生成 Query, Key, Value:
- Q, K, V 作用于前序层输出的 stack
- 通过 depth-wise cross-attention 实现动态聚合

## 关键机制
- **输入依赖权重**: 不同于 DenseFormer 的固定标量权重，DCA 的聚合权重随输入变化
- **三路 GRN 模块**: 分别生成 Q/K/V，使得跨层注意力具有完整的注意力机制表达力
- **Depth-wise Cross-Attention**: 在"层"维度上做注意力，而非在"token"维度
- **极低参数开销**: 仅增加约 0.2% 参数

## 实验结果
- Perplexity 显著提升
- 训练收敛速度提升 3 倍（等效模型质量下）
- 增强训练稳定性，减少 loss spike
- 被 ICML 2025 接收

## 与其他方法对比
| 方法 | 聚合权重 | 注意力类型 | 额外参数 |
|------|----------|------------|----------|
| DenseFormer | 固定可学习标量 | 无 | O(L^2) 标量 |
| MUDDFormer | 输入依赖标量 | 无 | 0.23% |
| DCA | 输入依赖 + 注意力 | 深度交叉注意力 | 0.2% |
| AttnRes | softmax注意力 | 深度softmax注意力 | ~0% |

## 与综述的关联
属于 **Depth** 维度。是跨层信息融合方法中复杂度和表达力的"上限"之一，使用完整的 Q/K/V 注意力机制在层维度上实现动态聚合。与 MUDDFormer 的核心区别在于使用了注意力机制而非简单的标量权重。

## 核心贡献
在残差连接中引入深度维度的交叉注意力机制，实现输入自适应的跨层动态信息聚合。
