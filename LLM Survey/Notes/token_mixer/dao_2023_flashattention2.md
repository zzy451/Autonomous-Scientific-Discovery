# Dao 2023 - FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

**论文信息**
- 标题: FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
- 作者: Tri Dao
- 年份: 2023
- arXiv: 2307.08691

## 0. 摘要翻译
FlashAttention虽然通过减少内存访问实现了加速，但仍远未达到GPU的理论最大FLOPS。我们提出FlashAttention-2，通过更好的工作分配和并行化策略，进一步提升速度。主要改进包括：减少非矩阵乘法运算量、在序列长度维度上并行化、以及在一个attention head内的warps之间更好地分配工作。

## 1. 方法动机
a) **为什么提出**: FlashAttention-1只达到GPU理论FLOPS的25-40%，有大量优化空间
b) **现有方法痛点**: 非matmul运算（如在线softmax的rescaling）占比过高；线程块间并行化不充分
c) **研究假设**: 通过减少非matmul FLOPS和改进并行策略，可以更接近理论最大吞吐

## 2. 方法设计
a) **方法流程**:
   - 外层循环遍历K/V的块（而非Q的块，与FA-1相反）
   - 内层循环遍历Q的块
   - 在序列长度维度上并行化不同线程块
   
b) **模块功能**:
   - **调换循环顺序**: 外层K/V、内层Q，减少rescaling写回次数
   - **序列并行**: 不同block处理不同序列位置的Q块
   - **Warp分配优化**: 在warps间分配Q和K/V的不同部分，减少通信
   
c) **关键改进**:
   - 非matmul FLOPS减少约2倍
   - 利用序列维度的并行性（当batch×head数不足以填满GPU时）
   - A100上达到理论最大FLOPS的50-73%

## 3. 与其他方法对比
| 特性 | FlashAttention | FlashAttention-2 |
|------|----------------|-------------------|
| GPU利用率 | 25-40% | 50-73% |
| 循环顺序 | 外层Q，内层KV | 外层KV，内层Q |
| 序列并行 | 无 | 有 |
| 速度(A100) | 基线 | 约2倍 |

## 4. 实验表现
a) **验证方式**: A100 GPU上的端到端速度测试
b) **关键数据**: 比FlashAttention快约2倍；比标准PyTorch attention快5-9倍
c) **优势场景**: 所有Transformer训练/推理
d) **局限性**: 仍是O(N²)复杂度

## 5. 学习与应用
a) **开源情况**: 完全开源，已成为PyTorch/HuggingFace标准
b) **实现细节**: 支持fp16/bf16，head_dim最大256
c) **迁移可能性**: 已经是LLM训练的事实标准

## 6. 总结
a) **一句话概括**: 通过优化循环顺序、序列并行和warp分配，将FlashAttention加速约2倍，达到GPU理论性能的50-73%
b) **速记版pipeline**: 与FA-1相同算法，但调换循环、增加并行、减少非matmul运算

**Token Mixer维度**: 注意力实现优化的进一步改进，工程层面最大化硬件利用率
