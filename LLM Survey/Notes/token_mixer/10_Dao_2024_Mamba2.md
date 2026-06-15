# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality (Mamba-2)
**作者**: Tri Dao, Albert Gu | **年份**: 2024 | **arxiv**: 2405.21060

## 0. 摘要翻译
本文建立了结构化状态空间模型 (SSM) 和注意力机制之间的理论联系，称为 **结构化状态空间对偶性 (Structured State Space Duality, SSD)**。具体而言，作者证明了某类 SSM 等价于一种特殊形式的半可分矩阵（semiseparable matrix），而 Softmax Attention 也可以视为一种特殊的此类矩阵。基于这一对偶性，提出了 **Mamba-2** 架构：使用更大的隐状态维度（如 N=64 vs Mamba-1 的 N=16）、多头结构，以及更高效的分块并行算法。Mamba-2 在语言建模上显著优于 Mamba-1，训练速度也更快。

## 1. 方法动机
a) **为什么提出这个方法**：Mamba-1 的选择性 SSM 虽然有效，但其理论基础不够清晰，且硬件利用效率仍有提升空间。需要建立 SSM 和 Attention 的统一理论框架，并据此设计更高效的算法。

b) **现有方法的痛点**：
- Mamba-1 的并行扫描算法虽然高效，但不能充分利用 GPU 的矩阵乘法单元（Tensor Core）
- Mamba-1 的隐状态维度 N=16 较小，限制了信息容量
- SSM 和 Attention 看似不同的机制，缺乏统一理解，阻碍了进一步优化

c) **研究假设/直觉**：如果能证明 SSM 和 Attention 在数学上是同一种运算的两种形式（对偶性），就能结合两者的优势——SSM 的线性递推效率 + Attention 的分块并行效率——设计出更优的算法。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 将序列分为多个 chunk（块）
2. **块内 (intra-chunk)**：使用类似注意力的二次方计算（矩阵乘法），充分利用 Tensor Core
3. **块间 (inter-chunk)**：使用 SSM 的线性递推传播隐状态
4. 两者结合形成 SSD (State Space Duality) 算法

**架构改进**：
- 引入多头结构：多个 SSM head 类似于 Attention 的多头
- 增大隐状态维度：N=64 或 N=256
- 保持与 Mamba-1 类似的选择性机制

b) **核心模块功能**：
- **SSD 层**：结合了 SSM 递推和注意力矩阵乘法的混合计算
  - 块内：M = L ⊙ (QK^T)，其中 L 是由 SSM 参数构造的掩码矩阵（半可分矩阵），Q = C, K = B
  - 块间：通过隐状态 h 传播跨块信息
- **多头 SSM**：P 个 head，每个 head 有独立的 (A, B, C) 参数，类似 MHA 的多头
- **简化的选择性**：A 标量化（每 head 只一个衰减标量），简化计算

c) **关键公式解释**：
- SSD 对偶性：SSM 递推 ↔ 半可分矩阵乘法
- 块内计算：Y_chunk = (L ⊙ QK^T) V（二次方，但块大小固定，可用 Tensor Core）
- 块间传递：h_{chunk+1} = A^{chunk_size} h_{chunk} + Σ 贡献
- 等效注意力矩阵：M_{ij} = C_i^T A^{i-j} B_j（半可分结构）
- 总复杂度：O(TN)，T 为序列长度，N 为隐状态维度

## 3. 与其他方法对比
- **与 Mamba-1 的区别**：
  1. 理论框架更清晰（SSD 对偶性）
  2. 隐状态更大（N=64 vs N=16）
  3. 引入多头结构
  4. 分块算法更好地利用 Tensor Core，训练速度快 2-8 倍
- **与 Transformer Attention 的理论联系**：Softmax Attention 对应 A=0（无衰减）的 SSD，即完全不压缩历史
- **与 Linear Attention 的联系**：Linear Attention 对应 A=I（无衰减 + 线性核）的 SSD
- **创新点**：
  1. 建立 SSM-Attention 的数学对偶性
  2. 分块混合计算算法（块内二次方 + 块间线性）
  3. 多头 SSM 架构
- **适用场景**：中大规模语言建模、需要高效训练和推理的场景

## 4. 实验表现
- **关键结果**：
  - Mamba-2 2.7B 显著优于 Mamba-1 同规模模型
  - 训练速度比 Mamba-1 快 2-8 倍（得益于 Tensor Core 利用）
  - 与 Transformer++ (with FlashAttention-2) 在质量上接近，在速度上更快
  - 支持更大的隐状态维度而不显著增加开销
- **优势场景**：大规模预训练、需要快速训练迭代的研究场景
- **局限性**：
  - 分块大小的选择影响性能（需要在块内二次方开销和块间信息传播之间平衡）
  - A 标量化简化了模型但可能损失表达能力
  - 精确的长距离 recall 能力仍不如全注意力

## 5. 总结
a) **一句话概括（≤20字）**：SSM 与 Attention 的对偶性，分块混合计算加速。

b) **速记 pipeline**：
`Input → 分块 → 块内: (L⊙QK^T)V (矩阵乘) + 块间: SSM隐状态递推 → 多头合并 → Output`
`理论: SSM递推 ≡ 半可分矩阵乘法 ≡ 特殊形式的Attention`
