# ReZero is All You Need: Fast Convergence at Large Depth

**论文信息**: Bachlechner, T., Majumder, B.P., Mao, H.H., Cottrell, G.W., McAuley, J. (2020/2021)
**arXiv**: 2003.04887 | **会议**: UAI 2021
**分类**: Control (残差缩放/初始化)

## 核心思想
ReZero（Residual with Zero initialization）是一种极简的残差连接改进方法。在每个残差分支上引入一个可学习标量参数 alpha，**初始化为零**。

## 数学公式
标准残差: x_{l+1} = x_l + F(x_l)
ReZero:   x_{l+1} = x_l + alpha_l * F(x_l), 其中 alpha_l 初始化为 0

## 关键机制
- **初始动态等距 (Initial Dynamical Isometry)**: alpha=0 时，网络退化为恒等映射，信号传播完全稳定
- 训练过程中 alpha 逐渐增大，网络逐步学习复杂变换
- 不需要 LayerNorm/BatchNorm 即可收敛（但 BN 仍可提供正则化）

## 实验结果
- 12层 Transformer 在 enwiki8 上收敛速度提升 **56%**
- 可训练超过 **100层** Transformer 和数千层全连接网络
- 消除了对复杂初始化方案和辅助损失的依赖

## 与综述的关联
属于 **Control** 维度 -- 通过零初始化标量控制残差分支的贡献。与 SkipInit 功能等价，但独立提出。是 DeepNorm 等深度缩放方法的先驱。

## 核心贡献
单行代码修改即可显著改善深度网络训练，体现了残差连接控制的"少即是多"思想。
