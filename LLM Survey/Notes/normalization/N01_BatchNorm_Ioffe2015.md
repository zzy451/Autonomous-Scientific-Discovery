# N-01: Batch Normalization (Ioffe & Szegedy 2015)

> **论文**: Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift
> **作者**: Sergey Ioffe, Christian Szegedy (Google)
> **发表**: ICML 2015 | arXiv:1502.03167
> **关键词**: Batch Normalization, Internal Covariate Shift, 训练加速

---

## 核心思想

提出 **Batch Normalization (BN)**，通过对每个 mini-batch 内的激活值进行归一化（减均值、除标准差），减少所谓的"内部协变量偏移"(Internal Covariate Shift)，从而加速深度网络训练。

## 方法

对于一个 mini-batch $\mathcal{B} = \{x_1, ..., x_m\}$：

$$\hat{x}_i = \frac{x_i - \mu_\mathcal{B}}{\sqrt{\sigma^2_\mathcal{B} + \epsilon}}$$
$$y_i = \gamma \hat{x}_i + \beta$$

其中 $\mu_\mathcal{B}$ 和 $\sigma^2_\mathcal{B}$ 是 batch 内的均值和方差，$\gamma$ 和 $\beta$ 是可学习的缩放和偏移参数。

## 关键贡献

1. **训练加速**: 允许使用更高的学习率，显著加速收敛
2. **正则化效果**: BN 本身带有轻度正则化效果，有时可替代 Dropout
3. **降低初始化敏感性**: 减少对精心设计参数初始化的依赖

## 与 LLM/Transformer 的关系

BN 在 CNN (如 ResNet) 中极为成功，但在 Transformer 中**几乎不使用**，原因包括：

1. **Batch 依赖性**: BN 依赖 batch 统计量，使单个样本的表示依赖于同 batch 的其他样本
2. **序列长度可变**: NLP 中序列长度不一，跨 batch 计算统计量不稳定
3. **训练-推理不一致**: 训练时用 batch 统计量，推理时用 running average，存在偏差
4. **分布式训练**: 大规模分布式训练中需要跨设备同步 batch 统计量，通信开销大
5. **小 batch 问题**: LLM 训练的有效 batch 往往按 token 计，BN 的 batch 维度统计不稳定

因此 Transformer 转向了 LayerNorm (Ba et al. 2016)，后者对每个样本独立归一化，不依赖 batch。

## 在综述中的定位

作为归一化方法的**奠基性工作**，是理解后续 LayerNorm、RMSNorm 等方法的起点。虽然在 LLM 中不直接使用，但其"减少内部协变量偏移"的动机和"可学习仿射变换"的设计模式被后续所有方法继承。

---

**阅读日期**: 2026-04-05
