# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
**作者**: Tri Dao (Princeton University) | **年份**: 2023 | **arxiv**: 2307.08691

## 0. 摘要翻译
FlashAttention通过减少内存读写实现了显著加速，但其GPU占用率仍未达到理论最优。本文提出FlashAttention-2，通过改进工作分配和并行策略进一步提升性能：(1) 调整算法以减少非矩阵乘法FLOPs的比例；(2) 在序列长度维度上并行化，特别是在前向传播中跨不同query块并行；(3) 在一个注意力头内更好地分配warps之间的工作以减少通信。FlashAttention-2达到了理论最大FLOPs的约70%，比FlashAttention快约2倍。

## 1. 方法动机
a) **为什么提出**: FlashAttention虽然减少了IO，但GPU计算利用率仅约25-35%（理论峰值的），存在大量优化空间。
b) **现有痛点**: (1) FlashAttention-1的循环顺序（外层K/V，内层Q）导致需要频繁的rescaling操作；(2) 前向传播中没有在序列长度维度并行化，batch size小或head数少时GPU利用率低；(3) warp间的工作分配不均衡，存在不必要的shared memory读写。
c) **研究假设**: 通过优化循环顺序、增加并行维度、改进warp级工作分配，可以将GPU利用率从~30%提升到~70%。

## 2. 方法设计
a) **Pipeline**: 与FlashAttention-1相同的分块策略，但优化了三个关键方面。

b) **模块功能**:
- **调整循环顺序**:
  - FlashAttention-1: 外层遍历K/V块，内层遍历Q块（每个Q块需要rescale）
  - FlashAttention-2: 外层遍历Q块，内层遍历K/V块
  - 好处: 每个Q块只需在最后做一次rescale，减少非matmul FLOPs
- **序列长度维度并行化**:
  - FlashAttention-1: 在batch和head维度并行（$B \times H$个thread blocks）
  - FlashAttention-2: 额外在Q的序列长度维度并行（$B \times H \times T_r$个thread blocks）
  - 当$B \times H$较小时（如长序列、少head），显著提升GPU占用率
- **Warp级工作分配优化**:
  - FlashAttention-1: 4个warps都计算QK^T，然后通过shared memory通信计算PV
  - FlashAttention-2: 将Q分给不同warps，每个warp独立计算自己的QK^T和PV，最后合并
  - 减少了warp间的shared memory读写（shared memory带宽远低于寄存器）
- **因果掩码优化**: 对于因果注意力，跳过完全被mask的块，减少约50%的计算

c) **公式解释**:
- 理论峰值: A100 GPU的FP16/BF16 matmul峰值为312 TFLOPS
- FlashAttention-1: ~85 TFLOPS（~27%利用率）
- FlashAttention-2: ~220 TFLOPS（~70%利用率）
- 非matmul FLOPs占比: FA-1约50%，FA-2降至约25%

## 3. 与其他方法对比
| 方面 | FlashAttention-2 | FlashAttention-1 | Triton FA | cuDNN FA |
|------|-----------------|-----------------|-----------|----------|
| GPU利用率 | ~70% | ~25-35% | ~50% | ~65% |
| 速度(A100) | ~220 TFLOPS | ~85 TFLOPS | ~150 TFLOPS | ~200 TFLOPS |
| 循环顺序 | 外Q内KV | 外KV内Q | 外Q内KV | - |
| 序列并行 | 是 | 否 | 否 | 是 |
| 因果优化 | 跳过masked块 | 无 | 无 | 有 |

## 4. 实验表现
- **前向传播**: 比FlashAttention-1快约2倍
- **反向传播**: 比FlashAttention-1快约1.5-2倍
- **端到端训练**: GPT-style模型训练速度提升约1.5-2倍
- **A100基准**: 序列长度2K时达到约230 TFLOPS（FP16）
- **长序列**: 序列长度16K时仍保持高效
- **与cuDNN对比**: 在大多数配置下与cuDNN的fused attention持平或更快
- **实际影响**: 成为PyTorch 2.0+的默认注意力实现

## 5. 总结
a) **一句话概括**: FlashAttention-2通过优化循环顺序（外Q内KV）、增加序列维度并行、改进warp工作分配，将GPU利用率从~30%提升到~70%，比FlashAttention-1快约2倍，成为现代LLM训练的标准注意力内核。
b) **速记pipeline**: Q块(并行) → 遍历KV块 → Warp独立计算QK^T和PV → 最终rescale → 写回HBM
