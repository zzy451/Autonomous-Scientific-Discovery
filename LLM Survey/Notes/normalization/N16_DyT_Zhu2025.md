# Transformers without Normalization
**作者**: Jiachen Zhu, Xinlei Chen, Kaiming He, Yann LeCun, Zhuang Liu | **年份**: 2025 | **arxiv**: 2503.10622

## 0. 摘要翻译

归一化层（如 LayerNorm、RMSNorm）是现代 Transformer 架构中几乎不可或缺的组件。本文提出一个出人意料的发现：归一化层可以被一个简单的逐元素函数 **Dynamic Tanh (DyT)** 直接替代，且不损失性能。DyT 的定义为 $\text{DyT}(x) = \gamma \cdot \tanh(\alpha x) + \beta$，其中 $\alpha$ 是可学习标量。我们的关键观察是：LayerNorm 对激活值的映射效果在统计上类似于 tanh 的 S 形曲线——将极端值压缩到有限范围。DyT 在视觉（ViT）、语言（LLaMA）、扩散模型（DiT）、自监督学习（MAE、DINO）等多个领域的 Transformer 中均能匹配归一化版本的性能。

## 1. 方法动机

### a) 为什么
归一化层在 Transformer 中被视为不可替代的组件，但它们涉及统计量计算（均值、方差/RMS），这些操作在计算和通信上有固有开销。更重要的是，一个基础性的问题被忽视了：**归一化到底在做什么？**

### b) 痛点
- **计算开销**: 归一化需要跨特征维度的归约操作（计算均值/方差/RMS），在每一层的每个 token 上都要执行
- **硬件不友好**: 归约操作需要同步，不利于并行加速
- **概念复杂性**: 为什么一个统计归一化操作是训练深层网络所必需的？
- **量化/低精度困难**: 归一化的精确统计量计算在低精度下可能不准确

### c) 假设
归一化层的核心效果不是"统计归一化"本身，而是一种**非线性压缩**——将极端值压缩到有限范围。如果用一个简单的有界非线性函数模拟这种压缩，就可以完全替代归一化层。

## 2. 方法设计

### a) Pipeline
1. 观察 LayerNorm 的输入-输出映射（散点图）
2. 发现其形状类似 tanh 的 S 形曲线
3. 设计 DyT 作为 drop-in replacement
4. 在所有归一化层位置替换为 DyT
5. 使用标准训练配方训练

### b) 模块

**DyT 定义**:
$$\text{DyT}(x) = \gamma \cdot \tanh(\alpha x) + \beta$$

- $\alpha \in \mathbb{R}$: 可学习标量 (per-layer)，控制 tanh 的"陡度"
- $\gamma \in \mathbb{R}^d$: 可学习逐通道缩放参数
- $\beta \in \mathbb{R}^d$: 可学习逐通道偏移参数

**关键设计选择**:
- $\alpha$ 是 per-layer 的（不是 per-channel），减少参数
- $\gamma, \beta$ 是 per-channel 的（与 LayerNorm 一致）
- $\alpha$ 的初始化: 通常设为 0.5--1.0（任务相关）

### c) 公式

**与 LayerNorm 的对比**:
- LayerNorm: $y = \gamma \cdot \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta$（需要归约操作计算 $\mu, \sigma$）
- DyT: $y = \gamma \cdot \tanh(\alpha x) + \beta$（纯逐元素操作，无归约）

**为什么 tanh？**
- 有界性: $\tanh(x) \in (-1, 1)$，自然约束输出范围
- 近似线性区: 当 $|\alpha x|$ 较小时，$\tanh(\alpha x) \approx \alpha x$
- 压缩区: 当 $|\alpha x|$ 较大时，输出被压缩到 $\pm 1$
- 奇函数: 零中心，保持信号对称性

## 3. 对比

| 特性 | LayerNorm | RMSNorm | DyT |
|------|-----------|---------|-----|
| 操作类型 | 归约 + 逐元素 | 归约 + 逐元素 | 纯逐元素 |
| 需要统计量 | $\mu, \sigma^2$ | RMS | 无 |
| 有界输出 | 是（间接） | 是（间接） | 是（$\tanh$ 显式有界） |
| 可学习参数 | $\gamma, \beta$ ($2d$) | $\gamma$ ($d$) | $\alpha, \gamma, \beta$ ($1+2d$) |
| 计算复杂度 | $O(d)$ 归约 | $O(d)$ 归约 | $O(1)$ 逐元素 |
| token 间依赖 | 无 | 无 | 无 |
| 硬件友好性 | 一般 | 较好 | **最好** |

## 4. 实验

- **视觉分类** (ViT on ImageNet): DyT 匹配 LayerNorm
- **语言建模** (LLaMA 架构): DyT 匹配 RMSNorm
- **扩散模型** (DiT on ImageNet): DyT 匹配 adaLN
- **自监督学习** (MAE, DINO v2): DyT 匹配 LayerNorm
- **语音** (wav2vec 2.0): DyT 匹配 LayerNorm
- **关键可视化**: LayerNorm 的输入-输出散点图呈现清晰的 S 形曲线，与 tanh 高度吻合
- **$\alpha$ 分析**: 不同层学到不同的 $\alpha$ 值——浅层 $\alpha$ 较小（近似线性），深层 $\alpha$ 较大（压缩更强）

## 5. 总结

### a) 一句话
DyT 通过一个简单的 $\gamma \cdot \tanh(\alpha x) + \beta$ 操作替代 LayerNorm/RMSNorm，证明归一化层的核心功能是非线性压缩而非统计归一化，在多个领域的 Transformer 中匹配归一化版本的性能，开启了"无归一化 Transformer"的新范式。

### b) 速记 pipeline
```
输入 x → tanh(α·x) → 乘 γ → 加 β → 输出
（无均值/方差/RMS 计算，纯逐元素操作）
α: per-layer 可学习标量，控制压缩强度
```

---
**阅读日期**: 2026-04-06
