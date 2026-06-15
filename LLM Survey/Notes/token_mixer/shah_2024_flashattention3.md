# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision
**作者**: Jay Shah, Ganesh Bikshandi, Ying Zhang, Vijay Thakkar, Pradeep Ramani, Tri Dao | **年份**: 2024 | **arxiv**: 2407.08608

## 0. 摘要翻译
本文提出 FlashAttention-3，针对 NVIDIA Hopper GPU (H100) 架构特性进行深度优化的注意力实现。通过三个关键技术——(1) warp 专业化实现异步计算与通信重叠，(2) 利用 Tensor Core 的 FP8 低精度计算，(3) 块量化和非相干处理保证低精度下的精度——FlashAttention-3 在 H100 上达到 740 TFLOPS（FP16），接近理论峰值的 75%，比 FlashAttention-2 快 1.5-2.0 倍。

## 1. 方法动机
a) **为什么**: FlashAttention-2 的设计针对 Ampere (A100) 架构，未能充分利用 Hopper 的新硬件特性（TMA、WGMMA、FP8 Tensor Core）。
b) **痛点**: (1) FA-2 在 H100 上仅达到约 35% 的理论 FLOPS 利用率；(2) GEMM 和 softmax 之间存在流水线气泡；(3) FP8 注意力的数值精度问题未解决。
c) **假设**: 通过 warp 级异步流水线和硬件感知的低精度策略，可以大幅提升 GPU 利用率。

## 2. 方法设计

### a) Pipeline

**三阶段异步流水线 (Warp Specialization)**:
```
Warp Group 0 (Producer): TMA 异步加载 K, V 块到共享内存
Warp Group 1 (Consumer): WGMMA 计算 S = Q·K^T
Warp Group 2 (Consumer): Softmax(S)，然后 WGMMA 计算 O = P·V
→ 三者通过 barrier 同步，形成流水线重叠
```

### b) 核心模块

**Warp Specialization (Warp 专业化)**:
- 将 warp group 分为 producer（数据加载）和 consumer（计算）
- Producer 使用 TMA (Tensor Memory Accelerator) 异步加载数据
- Consumer 使用 WGMMA (Warp Group Matrix Multiply-Accumulate) 计算
- 数据加载与计算完全重叠，消除流水线气泡

**FP8 注意力 with 块量化**:
- 将 Q, K 分块后各自量化到 FP8
- 每个块有独立的缩放因子（block quantization）
- `S_ij = scale_q_i · scale_k_j · (Q_i^{fp8} · K_j^{fp8T})`
- 精度损失可控（相比朴素 FP8 量化）

**非相干处理 (Incoherence Processing)**:
- 对 Q, K 应用随机正交变换使元素分布更均匀
- 减少量化误差的相干性（outlier 影响）
- `Q' = Q · R`, `K' = K · R` (R 是随机 Hadamard 矩阵)
- 注意力结果不变: `Q'K'^T = QRR^TK^T = QK^T`

### c) 关键公式
- 标准注意力不变: `O = softmax(QK^T/√d) V`
- FP8 块量化: `S = (s_q ⊗ s_k) ⊙ (Q_{fp8} K_{fp8}^T)`
- 在线 softmax: 与 FA-2 相同的数值稳定算法
- 吞吐量: 740 TFLOPS (FP16), 1.2 PFLOPS (FP8) on H100

## 3. 对比
| 实现 | GPU | FP16 TFLOPS | 峰值利用率 | FP8 支持 |
|------|-----|-------------|-----------|----------|
| FlashAttention | A100 | ~120 | ~40% | 否 |
| FlashAttention-2 | A100 | ~230 | ~73% | 否 |
| FlashAttention-2 | H100 | ~350 | ~35% | 否 |
| FlashAttention-3 | H100 | ~740 | ~75% | 是 |
| cuDNN Attention | H100 | ~600 | ~60% | 是 |

## 4. 实验
- **速度**: 在 H100 SXM5 上，FA-3 FP16 达到 740 TFLOPS，比 FA-2 快 1.5-2.0x
- **FP8**: FA-3 FP8 达到 1.2 PFLOPS，比 FP16 再快约 1.6x
- **精度**: FP8 + 块量化 + 非相干处理后，端到端训练质量与 FP16/BF16 基本无损
- **头维度**: 支持 d=64, 128, 256，在 d=128 时效率最高
- **因果掩码**: 因果注意力同样获得加速
- **实际影响**: 被集成到 PyTorch、Hugging Face 等主流框架

## 5. 总结
a) **一句话**: FlashAttention-3 通过 warp 专业化异步流水线、FP8 块量化和非相干处理，将 H100 上的注意力计算推至 75% 硬件利用率，比 FA-2 快 1.5-2x。
b) **速记 pipeline**: `Q,K,V → TMA Async Load → [Producer: Load KV | Consumer1: WGMMA(QK^T) | Consumer2: Softmax+WGMMA(PV)] pipelined → Online Softmax Merge → Output`
