# Batch Normalization Biases Residual Blocks Towards the Identity Function in Deep Networks

**论文信息**: De, S., Smith, S.L. (2020)
**arXiv**: 2002.03432 | **会议**: NeurIPS 2020
**分类**: Control (残差缩放/初始化)

## 核心思想
揭示了 Batch Normalization 在残差网络中的真正作用：BN 在初始化时将残差分支的激活值缩小约 1/sqrt(L) 倍，使残差块偏向恒等映射。基于此提出 **SkipInit** 作为 BN 的替代。

## 数学公式
SkipInit: y = x + alpha * f(x), alpha 初始化为 0（或小常数）

## 关键发现
1. **BN 的隐藏作用**: BN 不仅归一化统计量，更重要的是在初始化时抑制残差分支
2. **恒等偏置**: 这种抑制使深层残差网络的初始行为接近恒等映射
3. **SkipInit 替代**: 仅用一个零初始化标量即可替代 BN 的训练稳定性功能

## 与 ReZero 的关系
SkipInit 与 ReZero 在功能上**完全等价**，两者独立提出。区别在于理论视角：
- ReZero 从动态等距角度出发
- SkipInit 从解释 BN 作用的角度出发

## 与综述的关联
属于 **Control** 维度。提供了理论解释：为什么零初始化残差缩放有效。证明了残差连接的控制可以替代归一化层的核心功能。
