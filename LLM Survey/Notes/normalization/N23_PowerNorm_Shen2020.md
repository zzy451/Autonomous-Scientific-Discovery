# PowerNorm: Rethinking Batch Normalization in Transformers
**作者**: Sheng Shen, Zhewei Yao, Amir Gholami, Michael W. Mahoney, Kurt Keutzer | **年份**: 2020 | **arxiv**: 2003.07845

## 0. 摘要翻译

Batch Normalization (BN) 在 Transformer/NLP 任务中表现不如 Layer Normalization (LN)，这一经验事实被广泛接受但缺少系统性解释。本文深入分析了 BN 在 NLP 中失败的根本原因：NLP 数据的 batch 统计量（均值、方差）波动远比视觉数据剧烈，导致 running average 不可靠。基于此分析，我们提出 **Power Normalization (PN)**，通过三项改进——去除均值中心化、使用运行二次均值 (running quadratic mean)、近似反向传播——成功在 NLP Transformer 中超越 LayerNorm 和 BatchNorm。

## 1. 方法动机

### a) 为什么
BN 在 CNN (ResNet, EfficientNet) 中极为成功，但在 Transformer 中几乎完全被 LN 取代。这种差异背后的原因是什么？理解这一点不仅有理论价值，还可能催生更好的归一化方法。

### b) 痛点
- **BN 在 NLP 中失败**: 直接将 BN 应用于 Transformer 会导致性能下降甚至训练不稳定
- **流行解释不充分**: "BN 依赖 batch，不适合变长序列"的解释过于简单，未触及核心
- **Running average 不可靠**: NLP 中 batch 间的统计量波动是 CV 的数倍，running average 无法准确跟踪
- **训练-推理鸿沟加剧**: 波动的 running statistics 使得推理时使用的统计量与训练时差距更大

### c) 假设
BN 在 NLP 中失败的根源是**统计量的高方差波动**，而非 batch 依赖性本身。如果用更稳定的统计量估计（running quadratic mean）替代 per-batch 统计量，BN 风格的归一化可以在 NLP 中成功。

## 2. 方法设计

### a) Pipeline
1. 分析 NLP 和 CV 数据中 batch 统计量的波动特性
2. 去除均值中心化（类似 RMSNorm 的动机）
3. 用 running quadratic mean 替代 per-batch 方差
4. 设计近似反向传播方案保证梯度有界

### b) 模块

**三项核心改进**:

**改进 1: 放松零均值约束**
- BN: $\hat{x} = (x - \mu_B) / \sigma_B$
- PN: $\hat{x} = x / \psi$（无减均值，类似 RMSNorm）

**改进 2: 运行二次均值 (Running Quadratic Mean)**
$$\psi_t^2 = (1 - \rho) \cdot \psi_{t-1}^2 + \rho \cdot \frac{1}{|B|}\sum_{i \in B} x_i^2$$
- 使用**指数移动平均** (EMA) 而非 per-batch 统计量
- 减少了统计量在 batch 间的波动
- 训练和推理使用**同一个**统计量（消除 train-test 不一致）

**改进 3: 近似反向传播**
- 前向传播: 使用 running statistics $\psi_t$
- 反向传播: 近似 $\frac{\partial \psi_t}{\partial x}$（不完全展开 EMA 的梯度链）
- 理论保证梯度有界

### c) 公式
$$\text{PN}(x) = \gamma \cdot \frac{x}{\psi_t} + \beta$$

$\psi_t$ 通过 EMA 更新:
$$\psi_t^2 = (1-\rho) \psi_{t-1}^2 + \rho \cdot \mathbb{E}_{B}[x^2]$$

关键: $\psi_t$ 是**跨 batch 共享的 running statistic**，但不使用均值

## 3. 对比

| 特性 | BatchNorm | LayerNorm | RMSNorm | PowerNorm |
|------|-----------|-----------|---------|-----------|
| 归一化维度 | batch | feature | feature | **batch (running)** |
| 均值中心化 | 有 | 有 | 无 | **无** |
| 统计量来源 | per-batch | per-sample | per-sample | **running (EMA)** |
| 训练-推理一致 | 否 | 是 | 是 | **是** |
| NLP 性能 | 差 | 基线 | 匹配 LN | **超过 LN** |
| Lipschitz 常数 | 较大 | 中 | 中 | **较小** |

## 4. 实验

- **机器翻译** (IWSLT14 De-En): PN 超过 LN 约 0.5 BLEU
- **机器翻译** (WMT14 En-De): PN 超过 LN
- **语言建模** (Penn Treebank): PN 的困惑度低于 LN
- **语言建模** (WikiText-103): PN 超过 LN
- **统计量波动分析**: 可视化显示 NLP 中 batch 统计量的波动是 CV 的 3-5 倍
- **Running average 分析**: running quadratic mean 比 per-batch 方差稳定得多
- **BatchNorm 在所有 NLP 任务上均不如 LN**: 验证了问题的普遍性

## 5. 总结

### a) 一句话
PowerNorm 通过分析 BN 在 NLP 中失败的根本原因（统计量高方差波动），提出用 running quadratic mean 替代 per-batch 统计量并去除均值中心化，成功在 NLP Transformer 中超越 LayerNorm，但因仍依赖 batch 维度而未被主流 LLM 采用。

### b) 速记 pipeline
```
1. 去除减均值（类似 RMSNorm）
2. 用 running quadratic mean ψ 替代 per-batch 方差
   ψ² ← (1-ρ)·ψ² + ρ·E[x²]  (EMA 更新)
3. 近似反向传播保证梯度有界
输出: γ · (x / ψ) + β
```

---
**阅读日期**: 2026-04-06
