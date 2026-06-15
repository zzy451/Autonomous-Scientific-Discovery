# Improving Transformer Optimization Through Better Initialization
**作者**: Xiao Shi Huang, Felipe Perez, Jimmy Ba, Maksims Volkovs | **年份**: 2020 | **arxiv**: 2004.08249

## 0. 摘要翻译

Transformer 的训练通常需要精心设计的学习率预热 (warmup) 策略和 LayerNorm 来保证稳定性。本文提出 **T-Fixup**，将 Fixup 初始化思想扩展到 Transformer 架构。通过分析 Transformer 中梯度的传播特性，我们设计了一种理论驱动的初始化方案，允许训练**完全不使用 LayerNorm**的 Transformer，同时消除对 warmup 的依赖。实验表明 T-Fixup 在机器翻译和语言理解任务上匹配甚至超过使用 LN 的标准 Transformer。

## 1. 方法动机

### a) 为什么
Transformer 中的 LayerNorm 和 warmup 被视为训练的必要条件，但它们增加了复杂性。Fixup 已经证明 CNN 中可以通过初始化替代 BN，那么 Transformer 中是否也可以？

### b) 痛点
- **LayerNorm 的计算开销**: 每层两次归约操作，影响训练吞吐量
- **warmup 的超参数敏感性**: warmup 步数需要精心调节，不同任务/模型需要不同设置
- **Transformer 的梯度问题**: 标准 Xavier 初始化在深层 Transformer 中不足以维持梯度稳定
- **注意力层的特殊性**: 注意力机制中的 softmax 使梯度传播分析比 CNN 更复杂

### c) 假设
LayerNorm 在 Transformer 中的核心作用是**控制初始化阶段的激活值和梯度尺度**。如果通过初始化直接控制好尺度，就可以移除 LN 且不需要 warmup。

## 2. 方法设计

### a) Pipeline
1. 分析 Transformer 中注意力层和 FFN 层对梯度增长的贡献
2. 推导每层参数的理论最优缩放因子
3. 移除所有 LayerNorm 层
4. 按推导出的缩放因子初始化所有参数
5. 直接使用目标学习率训练，无需 warmup

### b) 模块

**T-Fixup 初始化方案**:

对于编码器深度 $N$ 和解码器深度 $M$ 的 Transformer:

1. **注意力层**:
   - $W_V$（value 投影）和 $W_O$（输出投影）按 $(9N)^{-1/4}$ 或 $(9M)^{-1/4}$ 缩放
   - $W_Q, W_K$ 使用标准 Xavier 初始化

2. **FFN 层**:
   - 第二个线性层 $W_2$ 初始化为零或极小值
   - 第一个线性层 $W_1$ 按深度缩放

3. **嵌入层**:
   - 词嵌入和位置嵌入按 $d^{-1/2}$ 缩放

4. **移除**:
   - 所有 LayerNorm 层
   - 学习率 warmup

### c) 公式
- 关键缩放因子: 注意力输出投影 $W_O \leftarrow (9N)^{-1/4} W_O$
- FFN 第二层: $W_2 \leftarrow (12N)^{-1/4} W_2$ 或 $W_2 = \mathbf{0}$
- 词嵌入: $E \leftarrow d^{-1/2} E$
- 理论基础: 保证前向传播方差和反向传播梯度范数在每层保持 $O(1)$

## 3. 对比

| 特性 | 标准 Transformer | T-Fixup |
|------|-----------------|---------|
| 归一化层 | LayerNorm (Pre/Post) | 无 |
| warmup | 必需 | 不需要 |
| 初始化 | Xavier | T-Fixup (理论推导) |
| 训练稳定性 | 依赖 LN + warmup | 依赖初始化 |
| 最终性能 | 基线 | 匹配或超过 |
| 适用架构 | 通用 | Encoder-Decoder, Decoder-only |

**与相关工作对比**:
| 方法 | 目标架构 | 替代的归一化 | 核心技术 |
|------|---------|------------|---------|
| Fixup | ResNet (CNN) | BatchNorm | 零初始化 + 深度缩放 |
| **T-Fixup** | Transformer | LayerNorm | 理论缩放 + 无 warmup |
| ReZero | 通用残差网络 | 各种 | 可学习零初始化残差权重 |
| Admin | Transformer | 无 | 自适应初始化，保留 LN |

## 4. 实验

- **机器翻译** (IWSLT14 De-En): 无 LN 的 T-Fixup 匹配标准 Transformer
- **机器翻译** (WMT14 En-De): 匹配 BLEU 分数，且无需 warmup
- **文本分类** (GLUE 基准): 在 fine-tuning 场景下性能相当
- **深层 Transformer**: 在 12 层以上的深层模型中，T-Fixup 比无初始化修改的版本显著更稳定
- **消融**: 各缩放因子的贡献分析——注意力层的缩放最为关键

## 5. 总结

### a) 一句话
T-Fixup 将 Fixup 思想扩展到 Transformer，通过理论推导的参数缩放初始化实现了无 LayerNorm、无 warmup 的 Transformer 训练，证明 LN 的核心功能是控制初始化阶段的激活尺度。

### b) 速记 pipeline
```
注意力: W_V, W_O 按 (9N)^(-1/4) 缩放
FFN: W_2 初始化为零或极小值
嵌入: 按 d^(-1/2) 缩放
→ 移除所有 LayerNorm → 移除 warmup → 直接训练
```

---
**阅读日期**: 2026-04-06
