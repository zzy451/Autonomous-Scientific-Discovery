# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
**作者**: Tri Dao | **年份**: 2023 | **arxiv**: 2307.08691

## 0. 摘要翻译
FlashAttention 通过减少 HBM 访问实现了注意力的加速，但其计算效率仍远未达到 GPU 的理论峰值（仅约 25-40% 的理论 FLOPs 利用率）。本文提出 **FlashAttention-2**，通过三项关键优化显著提升计算效率：(1) 减少非矩阵乘法运算的比例，(2) 改进并行化策略——在序列长度维度上并行，(3) 优化线程块间的工作分配——使用更好的 warp 分区减少同步和共享内存访问。FlashAttention-2 在 A100 GPU 上达到约 70% 的理论 FLOPs 利用率（比 FlashAttention 提升约 2 倍）。

## 1. 方法动机
a) **为什么提出这个方法**：FlashAttention-1 虽然减少了 HBM 访问，但 GPU 利用率仍然很低（~25-40%）。大量时间花在非矩阵乘法运算（如 softmax 的 exp, max, sum）和线程同步上。

b) **现有方法的痛点**：
- FlashAttention-1 的外层循环遍历 KV 块，内层循环遍历 Q 块——这使得每轮 KV 块更新时需要对所有 Q 块的 softmax 统计量做修正，产生额外的非矩阵乘法运算
- FlashAttention-1 在 batch 和 head 维度上并行，当 batch*head 较小时无法填满 GPU
- warp 间的工作分配效率低

c) **研究假设/直觉**：通过调换内外循环顺序（外层 Q，内层 KV）并优化 warp 级别的工作分配，可以大幅减少非矩阵乘法运算和同步开销，从而提升 GPU 利用率。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. **调换循环顺序**：外层遍历 Q 块，内层遍历 KV 块（FlashAttention-1 相反）
   - 好处：对每个 Q 块，遍历所有 KV 块后直接得到最终输出，无需额外的 rescaling 步骤
2. **序列并行**：除了 batch 和 head 维度，在序列长度维度上也做并行（不同 Q 块分配给不同 thread block）
3. **优化 warp 分区**：
   - 对于前向传播：每个 warp 负责 Q 的不同部分，共享 KV（避免 warp 间通信）
   - 对于反向传播：每个 warp 负责 KV 的不同部分

b) **核心模块功能**：
- **外Q内KV循环**：减少了在线 softmax 的 rescaling 运算——每个 Q 块只需要在最后做一次最终的 rescaling
- **序列维度并行**：thread block 数 = ceil(N / B_r) * batch * head，当序列长时并行度更高
- **Warp 级优化**：4 个 warp 分割 Q（而非分割 KV），避免 warp 间对 softmax 统计量的同步

c) **关键公式解释**：
- GPU 利用率 = 实际 FLOPs / 理论峰值 FLOPs
- FlashAttention-1: ~25-40% → FlashAttention-2: ~70%
- 矩阵乘法占比提升：通过减少 softmax rescaling 操作的次数
- 前向 FLOPs = 4 * N^2 * d（QK^T 和 PV 各 2N^2d）

## 3. 与其他方法对比
- **与 FlashAttention-1 的区别**：
  1. 循环顺序调换（外Q内KV vs 外KV内Q）
  2. 新增序列维度并行
  3. 优化 warp 级工作分配
  4. GPU 利用率从 ~35% → ~70%，速度提升 ~2x
- **与 Triton-based FlashAttention 的比较**：FlashAttention-2 使用手写 CUDA，比 Triton 实现更快
- **与 cuDNN/CUTLASS 的比较**：FlashAttention-2 是专为注意力优化的 kernel，通常比通用库更快
- **创新点**：纯工程优化层面的重大贡献——不改变算法，只优化 GPU 执行效率
- **适用场景**：所有 NVIDIA GPU 上的 Transformer 训练和推理（A100, H100 等）

## 4. 实验表现
- **关键结果**：
  - A100 上端到端训练速度：比 FlashAttention-1 快约 2 倍
  - GPU FLOPs 利用率：达到 ~72%（A100 上），接近矩阵乘法的理论利用率
  - GPT-style 模型训练：比标准 Attention 快 3-5 倍，比 FA1 快 2 倍
  - 支持因果注意力的优化（跳过不需要计算的三角区域）
- **优势场景**：大规模预训练、长序列训练
- **局限性**：
  - 仍然是 NVIDIA GPU 专用（CUDA kernel）
  - head 维度有限制（最优为 64, 128）
  - 实现复杂度高，维护成本大

## 5. 总结
a) **一句话概括（≤20字）**：调换循环顺序 + warp 优化，GPU 利用率翻倍。

b) **速记 pipeline**：
`外层循环Q块 → 内层遍历所有KV块 → SRAM中计算 → 序列维度并行 → Warp级优化 → ~70% GPU利用率`
