# CogView: Mastering Text-to-Image Generation via Transformers (Sandwich LayerNorm)

**论文信息**: Ding, M., Yang, Z., Hong, W., et al. (2021)
**arXiv**: 2105.13290 | **会议**: NeurIPS 2021
**分类**: Control (残差分支值爆炸抑制)

## 核心思想
在训练大规模 Transformer 时发现深层的"值爆炸"问题。提出 **Sandwich LayerNorm** 来限制残差分支输出的量级。

## 问题分析
- LayerNorm 输出量级正比于 sqrt(d_model)
- 残差连接将大量级值累加回主分支
- 逐层累积导致数值不稳定（FP16 下 NaN）

## Sandwich LayerNorm 方案
在标准 Pre-LN 或 Post-LN 基础上，**在每个残差分支末端（加回主路径之前）再加一个 LayerNorm**:

Output = x + LayerNorm_extra(SubLayer(LayerNorm(x)))

## 效果
- 有效防止值爆炸的逐层累积
- 配合 PB-relaxation 实现 FP16 稳定训练
- 4B 参数 CogView 模型成功训练

## 与综述的关联
属于 **Control** 维度。Sandwich-LN 是一种实用的残差连接稳定化技巧：
- 与 NormFormer 思路一致（额外归一化点）
- 但动机不同：NormFormer 关注梯度平衡，Sandwich-LN 关注值爆炸
- 为大模型工程实践提供了重要参考

## 核心贡献
针对超大规模 Transformer 残差连接的值爆炸问题，提供了简单有效的"夹心"归一化方案。
