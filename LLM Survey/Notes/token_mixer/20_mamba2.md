# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality (Mamba-2)
**作者**: Tri Dao, Albert Gu (Princeton, CMU) | **年份**: 2024 | **arxiv**: 2405.21060

## 0. 摘要翻译
本文建立了结构化状态空间模型（SSM）与注意力变体之间的理论联系，称为结构化状态空间对偶性（SSD）。具体地，某一类SSM等价于半可分矩阵（semiseparable matrix）上的线性注意力。基于这一联系，提出了Mamba-2架构，其核心层是SSD层——比Mamba的选择性SSM快2-8倍，同时在语言建模上保持竞争力。SSD框架还揭示了SSM和注意力之间丰富的算法和系统优化的联系。

## 1. 方法动机
a) **为什么提出**: Mamba的选择性SSM虽然有效，但其硬件实现（基于scan的算法）无法充分利用GPU的矩阵乘法单元（Tensor Cores），限制了训练吞吐量。
b) **现有痛点**: (1) Mamba的scan算法是顺序的，虽然可以并行但效率不如矩阵乘法；(2) SSM和注意力之间的理论联系不清晰，阻碍了统一优化；(3) 需要一种既保持SSM的线性复杂度又能利用Tensor Cores的算法。
c) **研究假设**: 通过限制SSM的结构（对角+标量结构），可以将SSM计算转化为矩阵乘法形式，从而利用Tensor Cores加速。

## 2. 方法设计
a) **Pipeline**: SSD层 = 输入投影 → 分块矩阵乘法（chunk-wise matmul）→ 块间状态传递 → 输出投影。

b) **模块功能**:
- **结构化状态空间对偶性 (SSD)**:
  - SSM视角: $h_t = A_t h_{t-1} + B_t x_t$, $y_t = C_t h_t$（循环形式）
  - 注意力视角: $Y = M \odot (QK^T) V$，其中$M$是由$A_t$决定的掩码矩阵（半可分矩阵）
  - 关键约束: $A_t = aI$（标量乘以单位矩阵），使得状态转移矩阵可交换
- **分块算法 (Chunk-wise Algorithm)**:
  - 将序列分为大小为$C$的块
  - 块内: 使用矩阵乘法形式计算（注意力视角），$O(C^2)$
  - 块间: 使用循环形式传递状态（SSM视角），$O(C \cdot N)$
  - 总复杂度: $O(L \cdot C \cdot \max(C, N))$，可以充分利用Tensor Cores
- **多头结构**:
  - 类似MHA/GQA，支持多头SSM
  - 每个头有独立的$A$、$B$、$C$参数
  - 头维度$P$（类似$d_k$），状态维度$N$

c) **公式解释**:
- 对偶性: 循环$h_t = a_t h_{t-1} + b_t x_t$ ↔ 矩阵$Y = (L \odot QK^T)V$
- 其中$L_{ij} = \prod_{k=j+1}^{i} a_k$（累积衰减矩阵）
- 块内用matmul（利用Tensor Cores），块间用scan（状态传递）
- 比Mamba-1快的原因: matmul的硬件利用率远高于element-wise scan

## 3. 与其他方法对比
| 方面 | Mamba-2 (SSD) | Mamba-1 | Linear Attention | Transformer |
|------|--------------|---------|-----------------|-------------|
| 核心算法 | 分块matmul+scan | 全scan | matmul | matmul |
| 硬件利用率 | 高（Tensor Cores）| 中 | 高 | 高 |
| 状态转移 | 标量$A_t$ | 对角$A_t$ | 无衰减 | N/A |
| 训练速度 | 比Mamba快2-8x | 基准 | 快 | 快但$O(N^2)$ |
| 表达能力 | 略低于Mamba | 基准 | 低 | 最高 |

## 4. 实验表现
- **训练速度**: 比Mamba-1快2-8倍（取决于序列长度和状态维度）
- **语言建模**: 在Pile上的PPL与Mamba-1相当（略优或持平）
- **下游任务**: 在zero-shot评估上与Mamba-1竞争
- **Scaling**: 在不同模型规模（370M-2.7B）上一致有效
- **与Transformer对比**: 在相同训练FLOPs下，Mamba-2接近Transformer++（带GQA和SwiGLU的优化Transformer）
- **混合架构**: Mamba-2层可以与注意力层混合使用，获得更好的性能

## 5. 总结
a) **一句话概括**: Mamba-2通过建立SSM与半可分矩阵注意力的对偶性（SSD），将SSM计算转化为分块矩阵乘法形式以利用Tensor Cores，实现比Mamba-1快2-8倍的训练速度，同时保持相当的模型质量。
b) **速记pipeline**: x → 分块(chunk C) → [块内: matmul形式QK^TV | 块间: scan传递状态] → 合并 → Output
