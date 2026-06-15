# Hyena Hierarchy: Towards Larger Convolutional Language Models
**作者**: Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, Christopher Ré | **年份**: 2023 | **arxiv**: 2302.10866

## 0. 摘要翻译
本文提出 Hyena，一种次二次复杂度的算子，作为注意力机制的直接替代。Hyena 基于隐式参数化的长卷积和数据控制的门控，实现了 O(n log n) 的计算复杂度。在序列长度 8K 时比高度优化的注意力快 2 倍，在 64K 时快 100 倍，同时在语言建模质量上匹配注意力。

## 1. 方法动机
a) **为什么**: 注意力的 O(n²) 复杂度是扩展到长序列的根本瓶颈。需要一种次二次算子，既能保持注意力的表达能力（数据依赖的交互），又能利用快速算法。
b) **痛点**: (1) 线性注意力等近似方法质量损失大；(2) SSM 缺乏显式的内容感知交互；(3) 需要一种统一框架来理解和超越注意力。
c) **假设**: 注意力可以被分解为两个原语——(1) 隐式长卷积（全局混合）和 (2) 逐元素门控（数据依赖性）。交替堆叠这两个原语可以匹配注意力质量。

## 2. 方法设计

### a) Pipeline
Hyena 算子是一个 N 阶递归结构（通常 N=2 即可匹配注意力）:
```
Input x
  → 线性投影得到 v, x₁, x₂, ..., xₙ (N+1 个投影)
  → 第1步: y₁ = LongConv_1(v) ⊙ x₁     (卷积 + 门控)
  → 第2步: y₂ = LongConv_2(y₁) ⊙ x₂    (卷积 + 门控)
  → ...
  → 第N步: yₙ = LongConv_N(y_{N-1}) ⊙ xₙ
  → Output = yₙ
```

### b) 核心模块

**隐式长卷积 (Implicitly Parametrized Long Convolution)**:
- 不直接存储长度为 n 的卷积核（太大）
- 用一个小型 FFN 参数化卷积核: `h(t) = FFN(t)` — 输入位置 t，输出卷积核值
- 通过 FFT 实现快速卷积: O(n log n)
- 卷积核带有指数衰减窗口以控制有效感受野

**数据控制门控 (Data-Controlled Gating)**:
- 每一阶的门控信号 xᵢ 由输入数据线性投影得到
- 提供数据依赖性（类似注意力中 Q·K 的作用）
- 门控是逐元素的，计算量 O(n)

**与注意力的关系**:
- 注意力 = 数据依赖的全局混合（QK^T 矩阵）作用于 V
- Hyena = 数据无关的全局混合（长卷积）+ 数据依赖的门控
- 通过多阶堆叠，Hyena 可以逼近注意力的表达能力

### c) 关键公式
- Hyena 算子（2阶）: `y = h₂ * (x₁ ⊙ (h₁ * (x₂ ⊙ v)))`
- 其中 * 表示卷积，⊙ 表示逐元素乘法
- 隐式卷积核: `h(t) = Window(t) · FFN_θ(t)`
- Window: 指数衰减 `w(t) = exp(-αt)`
- FFT 加速: `h * x = IFFT(FFT(h) ⊙ FFT(x))`

## 3. 对比
| 模型 | 复杂度 | 数据依赖 | 全局混合 | 参数化 |
|------|--------|----------|----------|--------|
| Attention | O(n²) | QK^T | 全局 | 显式 |
| S4/SSM | O(n log n) | 无 | 全局(卷积) | 隐式 |
| Hyena | O(n log n) | 门控 | 全局(卷积) | 隐式 |
| Linear Attn | O(n) | 核近似 | 全局 | 显式 |

## 4. 实验
- **语言建模**: WikiText-103 上 Hyena-355M 匹配同规模 Transformer 困惑度，训练计算减少 20%
- **The Pile**: 在大规模语料上 Hyena 与 Transformer 质量差距 <0.5 PPL
- **速度**: 序列长度 8K 时比 FlashAttention 快 2x，64K 时快 100x
- **Long Range Arena**: 在 LRA 基准上超越 S4
- **Recall**: 在合成 recall 任务上，Hyena 的多阶门控显著优于无门控的纯卷积模型
- **扩展性**: 在 125M-355M 参数范围验证了 scaling 行为

## 5. 总结
a) **一句话**: Hyena 通过交替堆叠隐式参数化长卷积（O(n log n) 全局混合）和数据控制门控（数据依赖性），构建了一种次二次复杂度的注意力替代算子。
b) **速记 pipeline**: `Input → N+1 Linear Projections → [LongConv(FFN+FFT) ⊙ Gate]×N → Output`
