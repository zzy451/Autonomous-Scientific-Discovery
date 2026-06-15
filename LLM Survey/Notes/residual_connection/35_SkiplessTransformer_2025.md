# Cutting the Skip: Training Residual-Free Transformers

**论文信息**: Training Residual-Free Transformers (2025)
**arXiv**: 2510.00345
**会议**: ICLR 2026
**分类**: Depth (无残差训练 / Skipless Transformer)

## 核心思想
残差（skip）连接被广泛认为是训练深层 Transformer 的必要条件。本文挑战这一假设，提出首个能够稳定高效训练无残差连接 Transformer 的方法，且不改变标准架构。核心发现：skip connections 并非训练 ViT 的基本需求。

## 关键机制
- **专用初始化方案**: 通过精心设计的权重初始化策略，使无残差 Transformer 在训练初期保持信号传播稳定
- **不修改架构**: 与之前需要额外归一化或门控的方法不同，本方法仅通过初始化即可实现稳定训练
- **适用于 ViT**: 在监督学习和自监督学习两种设定下验证

## 实验结果
- Skipless ViT 在监督和自监督设定下均能成功训练
- 克服了无残差连接时的优化困难
- 为层次化表征学习（hierarchical representation learning）开辟新方向
- 表明残差连接的作用主要在于优化便利性，而非表达能力的必要条件

## 与综述的关联
属于 **Depth** 维度的极端探索。与 ReZero (Note 01)、SkipInit (Note 02)、Fixup (Note 03) 等初始化方法一脉相承，但走得更远——完全移除残差连接。为理解"残差连接为何有效"提供了反面证据：残差连接是优化的捷径，而非架构的必需品。

## 核心贡献
证明通过适当初始化可以完全移除 Transformer 中的残差连接，挑战了"残差连接是深层网络训练必要条件"的传统认知。
