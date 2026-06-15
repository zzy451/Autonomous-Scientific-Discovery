# N-04: Group Normalization (Wu & He 2018)

> **论文**: Group Normalization
> **作者**: Yuxin Wu, Kaiming He
> **发表**: ECCV 2018 | arXiv:1803.08494
> **关键词**: Group Normalization, 小 batch 归一化, 通道分组

---

## 核心思想

提出 **Group Normalization (GN)**，将通道分为若干组，在每组内计算归一化统计量。GN 独立于 batch size，解决了 BN 在小 batch 下性能退化的问题。

## 方法

将 $C$ 个通道分为 $G$ 组，每组 $C/G$ 个通道，在每组的 $(C/G, H, W)$ 维度上计算均值和方差：

$$\mu_g = \frac{1}{|S_g|} \sum_{(c,h,w) \in S_g} x_{c,h,w}$$

其中 $S_g$ 是第 $g$ 组的索引集合。

## 特殊情况

- $G = C$: 退化为 Instance Normalization
- $G = 1$: 退化为 Layer Normalization
- GN 是 IN 和 LN 的统一框架

## 与 LLM 的关系

GN 最初为视觉任务设计，在标准 Transformer LLM 中**极少作为主要归一化层使用**。但有一个重要的近期应用：

### Differential Transformer 中的 GroupNorm (Ye et al. 2024)

在 **Differential Transformer** (arXiv:2410.05258) 中，GroupNorm 被应用于**注意力头的输出**：
- 对每个注意力头独立进行 GroupNorm
- 用于差分注意力 (differential attention) 的输出归一化
- 配合 $(1 - \lambda_\text{init})$ 的固定乘子，对齐梯度流
- 这是 GN 在 LLM attention 机制中的重要应用案例

## 在综述中的定位

作为归一化维度谱系的重要一环，提供了 IN 和 LN 的统一视角。重点关注其在 Differential Transformer 中的注意力头归一化应用。

---

**阅读日期**: 2026-04-05
