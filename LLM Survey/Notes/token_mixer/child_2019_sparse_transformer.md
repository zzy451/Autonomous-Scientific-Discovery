# Generating Long Sequences with Sparse Transformers
**作者**: Rewon Child, Scott Gray, Alec Radford, Ilya Sutskever | **年份**: 2019 | **arxiv**: 1904.10509

## 0. 摘要翻译
Transformer 是强大的序列模型，但其时间和内存复杂度随序列长度二次增长。本文引入注意力矩阵的稀疏分解（sparse factorizations），将复杂度从 O(n²) 降低到 O(n√n)，使得在数万个时间步的序列上训练成为可能。本文还引入了一系列工程优化（高效稀疏注意力核、梯度检查点、混合精度训练等），在文本、图像和音频生成任务上生成了具有全局一致性和多样性的无条件样本，并展示了原则上可以用自注意力建模长度达百万级的序列。

## 1. 方法动机
a) **为什么**: 标准 Transformer 的全注意力（dense attention）复杂度为 O(n²)，当序列长度 n 增大到数千甚至上万时，计算和内存成本变得不可接受，严重限制了长序列建模能力。
b) **痛点**: (1) 全注意力矩阵中大量权重接近零，存在冗余；(2) 图像、音频等数据天然具有局部结构，全局注意力并非每个位置都需要；(3) 需要一种既能捕获局部依赖又能保留长程依赖的注意力模式。
c) **假设**: 注意力矩阵可以被分解为若干稀疏模式的组合，每个头只关注序列的一个子集，通过多层堆叠仍可覆盖全部位置，从而在不显著损失表达能力的前提下大幅降低复杂度。

## 2. 方法设计

### a) Pipeline
`Input → Embedding → [Sparse Attention Block × N] → Output`
每个 Sparse Attention Block 内部用稀疏注意力模式替代全注意力。

### b) 稀疏注意力分解
将全注意力的连接集合 S（每个 query 关注的 key 集合）分解为 p 个不相交的子集：
```
Attend(X, S) = softmax( (QK^T) ⊙ Mask(S) / √d ) V
S_i = S_i^(1) ∪ S_i^(2) ∪ ... ∪ S_i^(p)
```
每个子集对应一个注意力头，只计算该子集内的注意力权重。

### c) 两种稀疏模式

**Strided Attention（步幅注意力）**:
- 适用于具有周期性结构的数据（如图像按行排列、音频按帧排列）
- 每个位置 i 关注：
  - 局部窗口: `S_i^(1) = {j : (i - l) ≤ j ≤ i}`，l 为局部窗口大小
  - 步幅位置: `S_i^(2) = {j : (j mod l) = (i mod l)}`，即同一列的位置
- 每个位置关注 O(√n) 个位置（取 l = √n）

**Fixed Attention（固定注意力）**:
- 适用于无明显周期结构的数据（如文本）
- 每个位置 i 关注：
  - 局部窗口: `S_i^(1) = {j : ⌊j/l⌋ = ⌊i/l⌋}`，即同一个块内的位置
  - 固定汇总位置: `S_i^(2) = {j : j mod l ∈ {l-c, ..., l-1}}`，即每个块的最后 c 个位置作为"汇总 token"
- 汇总 token 聚合块内信息，其他 token 通过关注汇总 token 获取跨块信息

### d) 复杂度
- 全注意力: O(n²)
- 稀疏注意力: O(n√n)（每个位置关注 ~√n 个位置）
- 内存: 通过梯度检查点（gradient checkpointing）从 O(n) 降低到 O(√n)

### e) 工程优化
- 高效 CUDA 稀疏注意力核（block-sparse）
- 混合精度训练（FP16 前向/反向 + FP32 梯度累积）
- 梯度检查点（recompute attention during backward）

## 3. 对比
| 方法 | 注意力复杂度 | 模式类型 | 长程依赖 | 适用场景 |
|------|------------|---------|---------|---------|
| Full Attention | O(n²) | 全连接 | 直接 | 短序列 |
| Sparse Transformer (Strided) | O(n√n) | 局部+步幅 | 2层可达 | 图像/音频 |
| Sparse Transformer (Fixed) | O(n√n) | 局部+汇总 | 2层可达 | 文本 |
| Local Attention | O(n·w) | 仅局部窗口 | 需多层 | 通用 |
| Longformer (后续) | O(n·w) | 局部+全局 | 全局token | 长文档 |

## 4. 实验
- **密度估计 (CIFAR-10)**: 在 CIFAR-10 图像生成上达到 2.80 bits/dim，优于当时的 Image Transformer
- **文本 (Enwik8)**: 在字符级语言建模上达到 0.99 bits/char（64层模型），与全注意力 Transformer 相当
- **音频 (音乐生成)**: 在原始音频波形上训练，生成具有全局一致性的音乐片段（序列长度 ~65k）
- **长序列扩展**: 展示了在序列长度 16,384 上的有效训练，理论上可扩展到百万级
- **速度**: 稀疏注意力核比全注意力快数倍（序列越长加速比越大）

## 5. 总结
a) **一句话**: Sparse Transformer 通过将全注意力分解为 strided 和 fixed 两种稀疏模式，将复杂度从 O(n²) 降至 O(n√n)，是稀疏注意力方向的奠基性工作，直接启发了 Longformer、BigBird 等后续方法。
b) **速记 pipeline**: `Input → Q,K,V → Sparse Mask (Strided: 局部+列 / Fixed: 块内+汇总token) → softmax(QK^T ⊙ Mask)V → Output`
