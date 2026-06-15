# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
**作者**: Tri Dao et al. (Stanford) | **年份**: 2022 | **arxiv**: 2205.14135

## 0. 摘要翻译
Transformer 的速度和内存瓶颈在于注意力机制。现有的近似注意力方法虽然减少了计算量，但往往无法实现真正的加速（因为忽略了内存访问开销）。本文提出 **FlashAttention**，一种 **IO-aware**（IO 感知）的精确注意力算法。核心思想是利用 **分块计算 (tiling)** 和 **重计算 (recomputation)**，避免将完整的 N×N 注意力矩阵写入 GPU 高带宽内存 (HBM)，而是在快速的 SRAM 中完成所有中间计算。FlashAttention 计算精确注意力（非近似），同时速度更快、内存更省。

## 1. 方法动机
a) **为什么提出这个方法**：GPU 的计算能力远超内存带宽（compute-bound vs memory-bound）。标准注意力实现产生大量的 HBM 读写（N×N 注意力矩阵），成为实际速度的瓶颈。需要从 IO 角度而非 FLOPs 角度优化注意力。

b) **现有方法的痛点**：
- 标准注意力实现：将 S = QK^T (N×N), P = softmax(S), O = PV 三步都实例化（materialize）在 HBM 中，产生 O(N^2) 的 HBM 读写
- 近似注意力（Linformer, Performer 等）：减少了 FLOPs 但在实际短/中等序列上反而不快
- GPU SRAM 容量小（如 A100 只有 20MB）但速度极快，未被充分利用

c) **研究假设/直觉**：如果能在 SRAM 中分块完成 Softmax 注意力的所有计算，只在最后将结果写回 HBM，就能将 HBM 访问量从 O(N^2) 降低到 O(N^2 d / M)（M 为 SRAM 大小），实现显著加速。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 将 Q, K, V 矩阵沿序列维度分成小块（每块大小适配 SRAM 容量）
2. 外层循环遍历 KV 块，内层循环遍历 Q 块
3. 在 SRAM 中计算当前 Q 块与 KV 块的注意力分数
4. 使用 **在线 Softmax** 技术：无需完整的注意力矩阵即可增量计算 softmax
5. 增量更新输出 O 和 softmax 统计量（max, sum）
6. 反向传播时不存储注意力矩阵，而是从 Q, K, V 和输出 O 重新计算

b) **核心模块功能**：
- **Tiling（分块）**：将 N×N 注意力计算分解为多个 B_r × B_c 的小块，每块适配 SRAM
- **在线 Softmax (Online Softmax)**：分块增量计算 softmax，维护 running max 和 running sum
  - 核心递推：m_new = max(m_old, m_block)，l_new = e^{m_old - m_new} · l_old + e^{m_block - m_new} · l_block
- **Recomputation（重计算）**：反向传播时不存储 O(N^2) 的注意力矩阵 P，而是从 Q, K, V 重新计算，用额外计算换取内存节省

c) **关键公式解释**：
- HBM 访问量：标准 = O(Nd + N^2)，FlashAttention = O(N^2 d^2 / M)
- 当 M > d^2 时（通常满足），FlashAttention 的 IO 复杂度远小于标准实现
- 在线 softmax 更新：O_new = diag(l_new)^{-1} [diag(l_old) · e^{m_old - m_new} · O_old + e^{m_block - m_new} · P_block V_block]

## 3. 与其他方法对比
- **与标准 Attention 实现的本质区别**：计算结果完全相同（精确注意力），但 IO 模式完全不同——避免实例化 N×N 矩阵
- **与近似注意力（Linformer, Performer）的比较**：FlashAttention 是精确的，不损失质量；且在实际序列长度上通常更快
- **与 xFormers/Cutlass 的比较**：FlashAttention 是首个将 IO-aware 优化系统化应用于注意力的工作
- **创新点**：
  1. IO-aware 的优化视角（关注 HBM 访问而非 FLOPs）
  2. 在线 Softmax 的分块增量计算
  3. 重计算策略节省 O(N^2) 内存
- **适用场景**：所有使用标准注意力的 Transformer，作为底层 kernel 替换

## 4. 实验表现
- **关键结果**：
  - 速度：比 PyTorch 标准实现快 2-4 倍，比 Megatron-LM 快 2.4 倍
  - 内存：从 O(N^2) 降低到 O(N)（不存储注意力矩阵）
  - 支持更长序列：GPT-2 从 1K → 4K 序列长度，BERT 从 512 → 2K
  - 长文档建模质量提升 0.7 perplexity（得益于更长上下文）
- **优势场景**：中长序列训练（1K-16K）、大 batch 训练、内存受限场景
- **局限性**：
  - 需要自定义 CUDA kernel，实现和维护成本高
  - 在极短序列上开销可能超过收益
  - 最初只支持特定的 head 维度（如 64, 128）
  - 对不同 GPU 架构需要调参（block size 等）

## 5. 总结
a) **一句话概括（≤20字）**：分块在 SRAM 算精确注意力，省 IO 即加速。

b) **速记 pipeline**：
`Q,K,V分块 → SRAM中: 块内QK^T → 在线Softmax → 增量更新O → 写回HBM`
`反向传播: 不存注意力矩阵，从Q,K,V重计算`
