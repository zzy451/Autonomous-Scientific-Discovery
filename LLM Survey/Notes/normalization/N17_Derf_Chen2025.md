# Stronger Normalization-Free Transformers
**作者**: Jiachen Chen, Jiaqi Lu, Jiachen Zhu, Yutao Sun, Zhuang Liu | **年份**: 2025 | **arxiv**: 2503.03817

## 0. 摘要翻译

DyT (Dynamic Tanh) 近期证明了归一化层可以被简单的逐元素函数替代，但只能**匹配**归一化版本的性能。本文进一步探索：能否找到一个替代函数**超越**归一化？通过对替代函数关键属性的系统性分析，我们提出 **Dynamic Erf (Derf)**，使用高斯误差函数 $\text{erf}$ 替代 $\tanh$。Derf 不仅匹配，更在视觉、语言、生成模型等多个任务上**一致性地超过** LayerNorm 和 RMSNorm，建立了无归一化 Transformer 的新 SOTA。

## 1. 方法动机

### a) 为什么
DyT 打开了"无归一化 Transformer"的大门，但它仅做到匹配。一个自然的后续问题：替代函数的选择空间很大，$\tanh$ 是否最优？如果不是，什么特性决定了替代函数的好坏？

### b) 痛点
- **DyT 的匹配瓶颈**: DyT 在所有任务上只能匹配但不能超过归一化，暗示 $\tanh$ 可能不是最优选择
- **缺乏系统分析**: DyT 的 $\tanh$ 选择主要基于经验观察（输入-输出散点图像 S 形），缺少对替代函数属性的理论分析
- **tanh 的饱和过快**: $\tanh$ 的尾部以指数速度衰减，在较大输入时梯度几乎为零

### c) 假设
替代函数的关键属性包括：有界性、单调性、平滑性、零中心性、以及**饱和速度**。具有更慢饱和速度（更好的梯度流）的函数可能带来更好的优化性能。$\text{erf}$ 函数满足所有这些属性，且饱和速度比 $\tanh$ 慢（高斯衰减 vs 指数衰减）。

## 2. 方法设计

### a) Pipeline
1. 系统列举替代函数需满足的关键属性
2. 对比 $\tanh$、$\text{erf}$、sigmoid、arctan 等候选函数
3. 选出 $\text{erf}$ 作为最优候选
4. 设计 Derf，在 DyT 的所有位置替换 $\tanh \to \text{erf}$
5. 微调偏移参数的设计

### b) 模块

**Derf 定义**:
$$\text{Derf}(x) = \text{erf}(\alpha x + s)$$

- $\text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} dt$: 高斯误差函数
- $\alpha \in \mathbb{R}$: 可学习缩放参数
- $s \in \mathbb{R}$: 可学习偏移参数

**注意**: Derf 的形式比 DyT 更简洁——没有外部的 $\gamma, \beta$，偏移通过 $s$ 在 $\text{erf}$ 内部实现。

### c) 公式

**属性对比**:

| 属性 | $\tanh$ (DyT) | $\text{erf}$ (Derf) |
|------|:---:|:---:|
| 有界 $\in (-1, 1)$ | 有 | 有 |
| 单调递增 | 有 | 有 |
| 光滑 ($C^\infty$) | 有 | 有 |
| 零中心 $f(0) = 0$ | 有 | 有 |
| 尾部衰减速度 | 指数 $O(e^{-2|x|})$ | 高斯 $O(e^{-x^2})$ |
| $|x| = 2$ 处导数 | $\approx 0.0007$ | $\approx 0.0183$ |

**梯度对比**:
- $\frac{d}{dx}\tanh(x) = 1 - \tanh^2(x)$
- $\frac{d}{dx}\text{erf}(x) = \frac{2}{\sqrt{\pi}} e^{-x^2}$
- 关键差异: 在 $|x| > 1$ 区域，$\text{erf}$ 的梯度显著大于 $\tanh$

## 3. 对比

| 方法 | 基础函数 | 参数 | 性能 vs 归一化 | 理论框架 |
|------|---------|------|--------------|---------|
| LayerNorm | 统计归一化 | $\gamma, \beta$ | 基线 | N/A |
| RMSNorm | RMS 归一化 | $\gamma$ | 匹配 LN | re-scaling |
| DyT | $\tanh$ | $\alpha, \gamma, \beta$ | 匹配 | 经验观察 |
| **Derf** | $\text{erf}$ | $\alpha, s$ | **超过** | 属性分析 |

## 4. 实验

- **ViT ImageNet 分类**: Derf 超过 LN 和 DyT
- **LLaMA 语言建模**: Derf 超过 RMSNorm 和 DyT（更低困惑度）
- **DiT 图像生成**: Derf 超过 adaLN 和 DyT（更低 FID）
- **MAE 自监督**: Derf 超过 LN
- **一致性超越**: 在所有测试的任务/模型/设置上，Derf 均一致地超过归一化和 DyT
- **候选函数消融**: 对比 $\tanh, \text{erf}, \text{sigmoid}, \text{arctan}$ 等，$\text{erf}$ 在所有任务上最优
- **饱和速度分析**: 更慢的饱和 → 更好的梯度流 → 更好的优化 → 更高性能

## 5. 总结

### a) 一句话
Derf 通过系统分析替代函数的关键属性，选择具有更慢饱和速度的 $\text{erf}$ 替代 DyT 中的 $\tanh$，首次实现了无归一化 Transformer **一致性超越**有归一化版本的性能，暗示传统归一化层可能并非最优设计。

### b) 速记 pipeline
```
输入 x → erf(α·x + s) → 输出
（比 DyT 更简洁：无外部 γ, β；偏移在 erf 内部通过 s 实现）
关键: erf 比 tanh 饱和更慢 → 梯度流更好 → 性能超过归一化
```

---
**阅读日期**: 2026-04-06
