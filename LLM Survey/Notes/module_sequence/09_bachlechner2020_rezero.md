# ReZero is All You Need: Fast Convergence at Large Depth
**作者**: Thomas Bachlechner, Bodhisattwa Prasad Majumder, Huanru Henry Mao, Garrison W. Cottrell, Julian McAuley | **年份**: 2020 | **arxiv**: 2003.04887 | **发表**: UAI 2021

## 0. 摘要翻译
ReZero 提出了一种极简的架构修改：在残差连接中引入可学习的标量参数 alpha，初始化为 0。这使得网络在训练开始时表现为恒等映射，满足"动态等距"（dynamical isometry）条件，从而实现深层网络的快速收敛。作者成功训练了 120 层 Transformer，12 层时收敛速度比标准 Transformer 快 56%，且无需 LayerNorm 或学习率 warm-up。

## 1. 方法动机
- 深层 Transformer（超过 12 层）训练困难，需要 LayerNorm、warm-up 等辅助手段
- 这些辅助手段增加了模型复杂性和超参数
- 寻找一种最简单的方法来实现深层网络的稳定训练
- 从信号传播理论（动态等距）出发设计方案

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### ReZero 残差连接
```
标准残差: x_{l+1} = x_l + F(x_l)
ReZero:   x_{l+1} = x_l + alpha_l * F(x_l)    其中 alpha_l 初始化为 0
```

### 理论分析：动态等距
- **初始化时（alpha=0）**：每一层都是恒等映射 x_{l+1} = x_l
- 输入-输出 Jacobian 矩阵为单位矩阵
- 所有奇异值均为 1 -> 完美的动态等距
- **信号传播**：梯度既不消失也不爆炸

### 训练过程
- alpha 从 0 开始，逐步被学习
- 网络缓慢地"开启"残差分支
- 整个过程保持接近动态等距
- 作者展示了 64 层 Transformer 的 Jacobian 奇异值分布始终集中在 1 附近

### 与 LayerNorm 的关系
- ReZero 可以**完全替代** LayerNorm
- 无需 LayerNorm、无需 warm-up、无需辅助损失
- 大幅简化了 Transformer 架构

### 模块结构
```
标准 Pre-LN:  x + F(LN(x))
ReZero:       x + alpha * F(x)      (alpha 初始为 0, 可学习)
```

## 3. 与其他方法对比
| 方法 | 核心思想 | 初始行为 | 需要 LN | 需要 warm-up |
|------|---------|---------|--------|-------------|
| 标准 Transformer | 固定残差 | F(x) 随机 | 是 | 是 |
| Pre-LN | LN 在前 | 梯度稳定 | 是 | 否 |
| Fixup | 深度依赖的缩放 | 缩放的 F | 否 | 否 |
| SkipInit | alpha 初始为 0 | 恒等映射 | 否 | 否 |
| ReZero | alpha 初始为 0 | 恒等映射 | 否 | 否 |

- ReZero 和 SkipInit 的核心思想非常相似（均为 alpha=0 初始化）
- ReZero 侧重 Transformer，SkipInit 侧重 ResNet

## 4. 实验表现
- **12 层 Transformer (enwiki8)**：收敛速度比 vanilla Transformer 快 **56%**
- **120 层 Transformer**：成功稳定训练，标准 Transformer 在此深度无法训练
- **64 层 Transformer**：Jacobian 奇异值分布验证了动态等距的保持
- 无需 LayerNorm、warm-up 或辅助损失
- 在 ResNet 上同样有效，成功训练 10,000 层网络

## 5. 总结
a) **一句话概括**：ReZero 通过将残差分支乘以初始为零的可学习标量，在初始化时实现完美的动态等距，从而使 120 层 Transformer 也能快速稳定收敛。

b) **速记 pipeline**：`x_{l+1} = x_l + alpha_l * F(x_l), alpha_l init=0`
