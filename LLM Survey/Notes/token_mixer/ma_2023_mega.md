# Mega: Moving Average Equipped Gated Attention
**作者**: Xuezhe Ma, Chunting Zhou, Xiang Kong, Junxian He, Liangke Gui, Graham Neubig, Hao Wang, Lei Li | **年份**: 2023 | **arxiv**: 2209.10655

## 0. 摘要翻译
本文提出 Mega，一种简单且理论上有根据的单头门控注意力机制，配备指数移动平均（EMA）来引入位置感知的局部依赖归纳偏置。此外，Mega 提出了一种将输入序列分成固定长度块的方法，使注意力复杂度降至线性。Mega 在多种序列建模基准上显著优于 Transformer 和 S4 等模型，包括 Long Range Arena、语言建模、机器翻译和图像分类。

## 1. 方法动机
a) **为什么**: 标准多头注意力有两个根本弱点——(1) 二次复杂度；(2) 对位置/局部结构缺乏归纳偏置，完全依赖位置编码。
b) **痛点**: SSM（如 S4）擅长捕捉局部和长程结构但缺乏内容感知的交互；注意力擅长内容感知但缺乏结构归纳偏置。两者各有短板。
c) **假设**: 将 EMA（捕捉局部时序结构）与单头门控注意力（捕捉全局内容交互）结合，可以同时获得两种优势。

## 2. 方法设计

### a) Pipeline
```
Input x
  ├─→ Multi-head EMA → 局部时序特征 → 生成 Q, K, V (单头)
  │     └─ 每个 head 有独立的 α, β, δ 参数
  └─→ 门控分支 → 生成 gate
       ↓
  Single-head Gated Attention(Q, K, V, gate)
       ↓
  Output (与 gate 逐元素相乘后投影)
```

### b) 核心模块

**Multi-dimensional Damped EMA**:
- 多头 EMA，每个维度有独立的衰减系数
- `h_t = α ⊙ h_{t-1} + (1 - α ⊙ δ) ⊙ x_t`
- α: 衰减因子（可学习），δ: 阻尼因子
- 可以用并行扫描高效计算
- 提供位置感知的局部归纳偏置

**Single-head Gated Attention**:
- 只用单个注意力头（而非多头），减少参数和计算
- 引入共享相对位置偏置
- 门控: `O = φ_h(gate) ⊙ Attn(Q, K, V)`
- φ_h 是 SiLU 激活函数

**Chunk-wise Attention (Mega-chunk)**:
- 将序列分成固定大小的块（chunk size = c）
- 块内: 完整注意力 O(c²)
- 块间: 每块压缩为单个表示后做块级注意力
- 总复杂度: O(n·c) ≈ O(n)（当 c 为常数时）

### c) 关键公式
- EMA: `h_t^{(j)} = α_j · h_{t-1}^{(j)} + (1 - α_j · δ_j) · x_t` (第 j 个 head)
- 注意力: `A = softmax(QK^T/√d + bias)`
- 门控输出: `O = SiLU(gate) ⊙ (A · V)`
- Chunk 注意力复杂度: O(n · c) 其中 c 是块大小

## 3. 对比
| 模型 | 局部建模 | 全局建模 | 注意力头数 | 复杂度 |
|------|----------|----------|-----------|--------|
| Transformer | 位置编码 | 多头注意力 | H 头 | O(n²) |
| S4 | SSM 卷积 | SSM 卷积 | — | O(n log n) |
| Mega | EMA | 单头门控注意力 | 1 头 | O(n·c) |
| Mega-chunk | EMA | 块级注意力 | 1 头 | O(n·c) |

## 4. 实验
- **Long Range Arena (LRA)**: Mega 平均准确率 90.19%，超越 S4 (86.09%) 和 Transformer (61.41%)
- **语言建模**: WikiText-103 上 Mega 困惑度优于 Transformer 基线
- **机器翻译**: WMT'16 En-De 上 Mega 匹配 Transformer 质量，参数更少
- **图像分类**: ImageNet 上 Mega 优于 DeiT
- **速度**: Mega-chunk 在长序列上比标准注意力快 2-5x
- **消融**: EMA 和门控各自贡献显著，移除任一都导致性能下降

## 5. 总结
a) **一句话**: Mega 通过将多维阻尼 EMA（局部时序归纳偏置）与单头门控注意力结合，并可选地使用块级注意力降低复杂度，在多种序列任务上超越 Transformer 和 S4。
b) **速记 pipeline**: `Input → Multi-head Damped EMA → (Q,K,V,Gate) → Single-head Gated Attn → SiLU(Gate) ⊙ AttnOut → Linear → Output`
