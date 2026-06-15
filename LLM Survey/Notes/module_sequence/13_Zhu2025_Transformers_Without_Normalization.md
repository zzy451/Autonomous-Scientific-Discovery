# Transformers without Normalization (Dynamic Tanh / DyT)

## 基本信息
- **作者**: Jiachen Zhu, Xinlei Chen, Kaiming He, Yann LeCun, Zhuang Liu
- **年份**: 2025 (CVPR 2025)
- **arXiv**: 2503.10622
- **关键词**: Dynamic Tanh, 移除归一化, 简化Transformer

## 核心贡献（Module Sequence 维度）
证明 Transformer 中的 LayerNorm 可以被一个简单的逐元素函数完全替代。

### 1. 关键观察
- LayerNorm 在深层网络中通常产生 S 形的 tanh-like 输入输出映射
- LN 的主要功能是**抑制异常激活值** (outlier suppression)
- 这个功能不需要复杂的统计计算（均值、方差）

### 2. Dynamic Tanh (DyT)
$$\text{DyT}(\mathbf{x}) = \tanh(\alpha \mathbf{x})$$
- $\alpha$ 是可学习的标量参数
- 逐元素操作，计算极其简单
- 不需要计算批次/层的统计量

### 3. 实验结果
- 在视觉、语言、监督学习、自监督学习等任务上均匹配或超越标准 LN
- 不需要显著的超参数调整
- 证明 LN 的核心贡献是激活值裁剪，而非统计归一化

### 4. 后续影响
- 使得移除归一化后的 Transformer 更容易分析和优化
- 某些权重矩阵（如 $W_Q$）在无归一化的情况下可以被证明是冗余的
- 为 Transformer 架构的进一步简化开辟了道路

## 与综述的关联
- Module Sequence 中"组件移除"的代表性工作
- 与 He & Hofmann 2023 (Simplifying Transformer Blocks) 互补：前者移除归一化，后者移除其他冗余组件
- 挑战了"归一化是必需的"这一长期假设
- 属于 Simplified Transformer 研究线的最新进展
