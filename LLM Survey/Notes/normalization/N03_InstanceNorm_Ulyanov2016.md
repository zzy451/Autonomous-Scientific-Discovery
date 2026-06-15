# N-03: Instance Normalization (Ulyanov et al. 2016)

> **论文**: Instance Normalization: The Missing Ingredient for Fast Stylization
> **作者**: Dmitry Ulyanov, Andrea Vedaldi, Victor Lempitsky
> **发表**: arXiv:1607.08022 (2016)
> **关键词**: Instance Normalization, 风格迁移, 逐实例归一化

---

## 核心思想

提出 **Instance Normalization (IN)**，对每个样本的每个通道独立计算均值和方差进行归一化。最初为快速风格迁移设计。

## 方法

对于特征图 $x \in \mathbb{R}^{C \times H \times W}$ 的第 $c$ 个通道：

$$\mu_c = \frac{1}{HW} \sum_{h,w} x_{c,h,w}, \quad \sigma^2_c = \frac{1}{HW} \sum_{h,w} (x_{c,h,w} - \mu_c)^2$$

归一化在 $(H, W)$ 空间维度上进行，每个样本、每个通道独立。

## 与其他归一化的关系

| 方法 | 归一化维度 | 适用场景 |
|------|-----------|---------|
| BatchNorm | $(N, H, W)$ | CNN 分类 |
| LayerNorm | $(C, H, W)$ 或 $(D)$ | Transformer / RNN |
| InstanceNorm | $(H, W)$ | 风格迁移 |
| GroupNorm | $(C/G, H, W)$ | 小 batch 视觉 |

## 与 LLM 的关系

IN 在 LLM/NLP 中**几乎不使用**。NLP 中的 token embedding 没有空间维度 $(H, W)$，IN 的设计假设不适用。但它的提出丰富了归一化方法的谱系，帮助理解"归一化维度的选择"这一核心设计决策。

## 在综述中的定位

作为归一化方法谱系的一环，帮助建立"不同归一化方法对应不同统计量计算维度"的分类框架。在综述中可简要提及，重点是与 LayerNorm、GroupNorm 的维度选择对比。

---

**阅读日期**: 2026-04-05
