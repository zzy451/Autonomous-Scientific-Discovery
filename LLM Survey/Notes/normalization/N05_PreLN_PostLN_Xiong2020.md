# N-05: On Layer Normalization in the Transformer Architecture (Xiong et al. 2020)

> **论文**: On Layer Normalization in the Transformer Architecture
> **作者**: Ruibin Xiong, Yunchang Yang, Ji He, Kai Zheng, Shuxin Zheng, Chen Xing, Huishuai Zhang, Yanyan Lan, Liwei Wang, Tie-Yan Liu
> **发表**: ICML 2020 | arXiv:2002.04745
> **关键词**: Pre-LN, Post-LN, 训练稳定性, 梯度分析, warmup

---

## 核心思想

从理论上分析了 Transformer 中 LayerNorm 放置位置 (Pre-LN vs Post-LN) 对训练动态的影响，解释了为什么 Post-LN 需要 warmup 而 Pre-LN 不需要。

## Pre-LN vs Post-LN 定义

### Post-LN (原始 Transformer, Vaswani 2017)
$$\text{Output} = \text{LayerNorm}(x + \text{SubLayer}(x))$$
- 归一化在残差连接**之后**
- 原始 "Attention is All You Need" 的设计

### Pre-LN (现代标准)
$$\text{Output} = x + \text{SubLayer}(\text{LayerNorm}(x))$$
- 归一化在子层**之前**
- 残差路径保持"干净"的恒等映射

## 关键理论贡献

### 1. Mean Field Theory 分析
- **Post-LN 的问题**: 在初始化阶段，靠近输出层的参数梯度非常大，导致优化不稳定
- **Pre-LN 的优势**: 梯度在初始化时表现良好 (well-behaved)，无需 warmup

### 2. Warmup 的必要性
- Post-LN **需要** 精心调校的 learning rate warmup
- Pre-LN **不需要** warmup，可以直接使用较高学习率

### 3. 梯度高速公路
- Pre-LN 中残差连接提供了"梯度高速公路" (gradient highway)
- 梯度可以无衰减地流过任意深度的网络

## 对 LLM 架构的影响

| 模型 | LN 位置 | 备注 |
|------|---------|------|
| Original Transformer | Post-LN | 需要 warmup |
| BERT | Post-LN | 训练不稳定的来源之一 |
| GPT-2/3 | Pre-LN | 解决了深度缩放问题 |
| LLaMA 系列 | Pre-LN (RMSNorm) | 现代标准 |
| Gemma 2 | Pre+Post (RMSNorm) | 两者兼用 |

## 后续影响

此论文是 LN 位置研究的**里程碑**，直接影响了：
- DeepNorm (Wang 2022): 结合 Post-LN 的性能和 Pre-LN 的稳定性
- MAGNETO/Sub-LN (Wang 2022): 在子层内部放置 LN
- Peri-LN (2025): 在输入和输出都放置 LN
- Sandwich-LN/CogView (2021): 在子层前后都加 LN

## 在综述中的定位

这是 Normalization 章节中**最重要的理论分析论文之一**。它不仅解释了 Pre-LN 为何优于 Post-LN，还为后续所有 LN 位置变体的研究奠定了理论基础。综述中应重点讨论 Pre-LN 成为现代标准的原因。

---

**阅读日期**: 2026-04-05
