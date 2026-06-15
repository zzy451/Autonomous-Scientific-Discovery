# High-Performance Large-Scale Image Recognition Without Normalization
**作者**: Andrew Brock, Soham De, Samuel L. Smith, Karen Simonyan | **年份**: 2021 | **arxiv**: 2102.06171

## 0. 摘要翻译

Batch Normalization 是大多数图像分类模型的关键组件，但它也带来了诸多实际弊端：计算开销、内存占用、训练与推理行为不一致、以及与分布式训练中 batch 统计量同步的复杂性。本文提出 **Normalizer-Free ResNets (NF-Nets)** 和 **Adaptive Gradient Clipping (AGC)**，在完全不使用 BatchNorm 的情况下，在 ImageNet 上达到 86.5% top-1 精度（当时 SOTA），且训练速度比 EfficientNet 快 8.7 倍。核心创新是 AGC：根据参数范数与梯度范数的比值自适应裁剪梯度，替代 BN 提供的隐式梯度约束。

## 1. 方法动机

### a) 为什么
尽管 BN 在图像分类中几乎无处不在，但它存在多个工程层面的弊端，特别是在大规模分布式训练中。已有工作（如 Fixup）证明可以训练无 BN 的网络，但性能仍有差距。NF-Net 的目标是在大规模任务上**完全匹配甚至超过**使用 BN 的模型。

### b) 痛点
- **BN 的计算/内存开销**: 需要存储和计算 running mean/var
- **训练-推理不一致**: 训练用 batch 统计量，推理用 running average
- **分布式训练复杂性**: 需要跨设备同步 batch 统计量
- **batch 大小敏感**: 小 batch 下 BN 不稳定
- **fine-tuning 中的问题**: BN 统计量在域迁移时可能不准确

### c) 假设
BN 的核心功能可以分解为两部分：(1) 控制前向传播中的信号方差，(2) 隐式地限制梯度的更新幅度。前者可通过 Scaled Weight Standardization 实现，后者可通过 Adaptive Gradient Clipping 实现。

## 2. 方法设计

### a) Pipeline
1. 使用 Signal Propagation Plots 分析无 BN 网络中的前向信号传播
2. 应用 Scaled Weight Standardization 控制每层输出方差
3. 设计带方差跟踪的缩放残差连接
4. 训练时使用 Adaptive Gradient Clipping (AGC) 替代 BN 的隐式梯度正则化

### b) 模块

**Normalizer-Free 设计**:
1. **Scaled Weight Standardization**: 对卷积权重 $W$ 进行标准化（减均值、除标准差），加上理论推导的缩放因子
   $$\hat{W}_{ij} = \frac{W_{ij} - \mu_W}{\sigma_W \sqrt{N}}$$
   其中 $N$ 是 fan-in

2. **缩放残差连接**:
   $$x_{l+1} = x_l + \alpha \cdot f_l(x_l / \beta_l)$$
   - $\alpha$: 残差分支权重
   - $\beta_l$: 基于方差跟踪的输入缩放因子
   - 维护每层的预期方差 $\text{Var}(x_l)$ 用于计算 $\beta_l$

**Adaptive Gradient Clipping (AGC)**:
$$G_i \leftarrow \begin{cases} \lambda \frac{\|W_i\|_F}{\|G_i\|_F} G_i & \text{if } \frac{\|G_i\|_F}{\|W_i\|_F} > \lambda \\ G_i & \text{otherwise} \end{cases}$$

### c) 公式
- AGC 的关键洞察: 梯度更新的"有效步长"不是梯度的绝对大小，而是梯度相对于参数的比值 $\|G\|_F / \|W\|_F$
- $\lambda$ 是裁剪阈值超参数（典型值 0.01--0.1）
- 逐层应用（每层参数矩阵独立判断）
- AGC 在大 batch 训练中尤其重要——大 batch 时梯度方差小但期望值大，容易导致过大更新

## 3. 对比

| 特性 | ResNet + BN | NF-Net (无 BN) |
|------|------------|----------------|
| 归一化层 | BatchNorm | 无 |
| 权重处理 | 标准 | Scaled Weight Standardization |
| 梯度控制 | BN 隐式控制 | AGC 显式控制 |
| batch 依赖 | 有 | 无 |
| ImageNet top-1 | ~80% (ResNet-50) | **86.5%** (NF-Net-F1) |
| 训练速度 | 基线 | 比 EfficientNet 快 8.7x |

**与其他无归一化方法对比**:
| 方法 | 年份 | 目标架构 | 核心技术 | ImageNet SOTA? |
|------|------|---------|---------|---------------|
| Fixup | 2019 | CNN | 初始化 | 否 |
| T-Fixup | 2020 | Transformer | 初始化 | N/A |
| **NF-Net** | 2021 | CNN | AGC + WSS | **是** |

## 4. 实验

- **ImageNet SOTA**: NF-Net-F1 达到 86.5% top-1（当时 SOTA）
- **训练效率**: 比 EfficientNet-B7 快 8.7 倍达到同等精度
- **大 batch 训练**: AGC 使得超大 batch (4096+) 下无 BN 训练稳定
- **消融**: AGC 是最关键的组件——移除 AGC 则训练发散
- **迁移学习**: 在下游任务上迁移效果与 BN 版本相当
- **AGC 超参数 $\lambda$**: 对 $\lambda$ 的选择有一定敏感性，但 0.01 是稳健的默认值

## 5. 总结

### a) 一句话
NF-Net 通过 Scaled Weight Standardization 和 Adaptive Gradient Clipping 两项技术，在完全不使用 BatchNorm 的情况下达到 ImageNet SOTA，证明了无归一化架构在大规模视觉任务上的可行性，为后续 DyT/Derf 提供了重要方法论启发。

### b) 速记 pipeline
```
权重标准化 (Scaled WSS) → 缩放残差连接 (方差跟踪) → AGC 梯度裁剪
核心: AGC → if ‖G‖/‖W‖ > λ, then clip G by λ·‖W‖/‖G‖
（不裁剪绝对值，裁剪 梯度/参数 的比值）
```

---
**阅读日期**: 2026-04-06
