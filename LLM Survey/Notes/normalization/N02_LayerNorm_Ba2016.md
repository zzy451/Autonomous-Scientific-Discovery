# N-02: Layer Normalization (Ba, Kiros & Hinton 2016)

> **论文**: Layer Normalization
> **作者**: Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton
> **发表**: arXiv:1607.06450 (2016)
> **关键词**: Layer Normalization, Transformer 核心组件, 序列模型归一化

---

## 核心思想

提出 **Layer Normalization (LN)**，对单个样本的**所有特征维度**计算均值和方差进行归一化，而非像 BN 那样跨 batch 维度。这使得归一化完全独立于 batch 中的其他样本。

## 方法

对于隐层向量 $\mathbf{h} \in \mathbb{R}^d$：

$$\mu = \frac{1}{d} \sum_{i=1}^{d} h_i, \quad \sigma^2 = \frac{1}{d} \sum_{i=1}^{d} (h_i - \mu)^2$$
$$\hat{h}_i = \frac{h_i - \mu}{\sqrt{\sigma^2 + \epsilon}}$$
$$y_i = \gamma_i \hat{h}_i + \beta_i$$

其中 $\gamma$ 和 $\beta$ 是逐元素 (per-element) 的可学习参数。

## 关键贡献

1. **与 batch 无关**: 归一化只依赖当前样本的特征，适合小 batch、可变长序列
2. **训练/推理一致**: 不需要维护 running statistics，训练和推理行为完全一致
3. **RNN 友好**: 原始动机之一是解决 BN 在 RNN 中的应用困难
4. **Transformer 标配**: 成为原始 Transformer (Vaswani 2017) 及后续几乎所有 Transformer 的标准归一化方式

## 计算特性

- 两个统计量 (均值 + 方差) 需要两遍扫描或在线计算
- 包含减均值 (zero-centering) 和除标准差 (variance normalization)
- 可学习参数: $2d$ 个 ($\gamma$ 和 $\beta$，各 $d$ 维)

## 与 RMSNorm 的比较

| 特性 | LayerNorm | RMSNorm |
|------|-----------|---------|
| 减均值 | 有 | 无 |
| 可学习偏移 $\beta$ | 有 | 无 |
| 统计量 | 均值 + 方差 | 仅 RMS |
| 计算成本 | 较高 | 较低 |
| 量化友好性 | 更好 (零中心) | 稍差 (非零中心) |

## 在 LLM 中的使用

- **GPT-2/3**: 使用 LayerNorm (Pre-LN 位置)
- **BERT**: 使用 LayerNorm (Post-LN 位置)
- **LLaMA 系列**: 转向 RMSNorm，去除均值中心化
- **现代趋势**: 多数 2024+ 的 LLM 已切换至 RMSNorm

## 在综述中的定位

LayerNorm 是 Transformer 架构中**最核心的归一化方法**，理解它是理解所有后续变体的基础。它定义了"对特征维度归一化 + 可学习仿射变换"的范式，后续 RMSNorm、ScaleNorm 等都是对其的简化或改进。

---

**阅读日期**: 2026-04-05
