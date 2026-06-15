# Batch Normalization Biases Residual Blocks Towards the Identity Function in Deep Networks (SkipInit)
**作者**: Soham De, Samuel L. Smith | **年份**: 2020 | **arxiv**: 2002.10444 | **发表**: NeurIPS 2020

## 0. 摘要翻译
本文揭示了 Batch Normalization (BN) 在深层残差网络中的真正作用：BN 将残差块偏置向恒等函数方向，即在初始化时以约 sqrt(depth) 的比例缩小残差分支相对于跳跃连接的贡献。基于这一洞察，作者提出 SkipInit——一种仅需一行代码修改的替代方案：在残差分支末端添加初始化为零的可学习标量乘法器。SkipInit 可以在不使用 BN 的情况下成功训练 1000 层残差网络。

## 1. 方法动机
- Batch Normalization 被广泛使用，但其成功的真正原因仍有争议
- 流行的解释（如"平滑损失面"、"控制内部协变量偏移"）可能不是核心原因
- 需要找到 BN 在残差网络中最关键的贡献
- 如果找到了，能否用更简单的方法替代？

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### 核心发现
- BN 在初始化时自然地将残差分支的输出**缩小**了约 `1/sqrt(L)` 倍（L 为网络深度）
- 这种缩放使得深层残差网络在训练初期表现得像浅层网络
- 随着训练进行，残差分支逐渐"开启"
- 这种"偏置向恒等函数"的效应是 BN 使能深层训练的**主要原因**

### SkipInit
```
标准残差:  x_{l+1} = x_l + F(x_l)
SkipInit:  x_{l+1} = x_l + alpha * F(x_l)    其中 alpha 初始化为 0
```

- 一行代码修改：在残差分支末端乘以可学习的 alpha
- alpha 初始化为 0（或小常数）
- 网络初始时为恒等映射，训练过程中学习适当的残差贡献
- 无需任何归一化层

### 与 BN 的关系
```
BN 的隐式行为:   x + (1/sqrt(L)) * F(x)    在初始化时
SkipInit 的显式行为: x + 0 * F(x) -> x + alpha * F(x)  (alpha 从 0 学习)
```

## 3. 与其他方法对比
| 方法 | 核心机制 | 复杂度 | 来源 |
|------|---------|-------|------|
| Batch Norm | 隐式缩放残差分支 | 高 | Ioffe & Szegedy 2015 |
| Layer Norm | 逐样本归一化 | 中 | Ba et al. 2016 |
| Fixup | 显式深度缩放 + 零初始化 | 低 | Zhang et al. 2019 |
| ReZero | alpha=0 + 可学习 | 极低 | Bachlechner et al. 2020 |
| SkipInit | alpha=0 + 可学习 | 极低 | De & Smith 2020 |

- SkipInit 和 ReZero 本质上是同一方法，独立提出
- SkipInit 侧重于理论分析（为什么 BN 有效），ReZero 侧重于实际应用（快速收敛）
- Fixup 更复杂（需要深度相关的缩放因子），SkipInit 更简洁

## 4. 实验表现
- **1000 层 ResNet**：SkipInit 成功训练，无需 BN
- **图像分类**：在 CIFAR-10/ImageNet 上达到与 BN 版本可比的性能
- 但作者也指出 BN 在某些场景下仍有额外优势（泛化、大 batch 训练）
- 主要贡献在于**理论洞察**：解释了 BN 为什么能使深层训练成功

## 5. 总结
a) **一句话概括**：揭示了 BN 的核心作用是在初始化时将残差分支偏置向恒等函数，并用 SkipInit（alpha=0 的可学习标量）以一行代码复现这一效应。

b) **速记 pipeline**：`x_{l+1} = x_l + alpha_l * F(x_l), alpha_l init=0`（与 ReZero 相同的形式化）
