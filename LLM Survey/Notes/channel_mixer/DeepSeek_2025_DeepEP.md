# DeepEP: Expert Parallelism 通信库与 MoE 分布式推理/训练

**项目**: DeepEP: An Efficient Expert-Parallel Communication Library
**作者**: DeepSeek-AI
**年份**: 2025
**来源**: https://github.com/deepseek-ai/DeepEP
**标签**: Expert Parallelism, All-to-All 通信, MoE 推理, NVSHMEM, 分布式系统

---

## 0. 摘要
DeepEP 是 DeepSeek 开源的高性能 MoE 专家并行通信库，专为 MoE 模型的 all-to-all dispatch/combine 操作优化。它绕过 NCCL，直接使用 NVSHMEM 实现单边 GPU 通信，在 NVLink 和 InfiniBand 上几乎打满硬件带宽。提供高吞吐训练内核和低延迟推理内核两套方案，并原生支持 FP8 dispatch，是 DeepSeek-V3 训练和推理的核心基础设施。

## 1. 背景：Expert Parallelism 的通信瓶颈
a) Expert Parallelism (EP) 将不同专家分布在不同 GPU 上，每个 token 需要被发送到持有目标专家的 GPU → 需要 all-to-all 通信。
b) 传统方案使用 NCCL 的 alltoall 原语，但 NCCL 为集合通信优化，在 MoE 的不规则、动态路由模式下效率低下。
c) MoE 的 all-to-all 有两个阶段：dispatch（将 token 发送到目标专家所在 GPU）和 combine（将专家输出收集回原 GPU）。
d) 随着专家数量增加（DeepSeek-V3 有 256 个），通信开销成为主要瓶颈。

## 2. DeepEP 的设计

### 2.1 高吞吐内核（训练场景）
- 使用 NVSHMEM 单边 put/get 操作替代 NCCL 集合通信
- 流水线化：将数据分块，计算与通信重叠
- NVLink 内节点通信：接近 900 GB/s 理论带宽
- InfiniBand 跨节点通信：接近 400 Gbps 线速
- 原生 FP8 支持：dispatch 时直接传输 FP8 数据，减少 50% 通信量

### 2.2 低延迟内核（推理场景）
- 推理时 batch size 小，吞吐不是瓶颈，延迟才是
- 使用 RDMA + GPUDirect 实现亚毫秒级 dispatch
- 针对小消息优化：减少协议开销和同步等待
- 支持 prefill 和 decode 两种推理模式的不同优化策略

### 2.3 与 Disaggregated Expert Parallelism 的关系
- 新兴趋势：将 attention 计算和 FFN/MoE 计算分离到不同硬件组
- Attention 节点处理注意力计算和 KV cache
- Expert 节点专门处理 MoE 层
- DeepEP 的低延迟内核为这种解耦架构提供通信支持

## 3. 与其他方案对比
| 方案 | 通信原语 | NVLink 利用率 | IB 利用率 | FP8 支持 |
|------|----------|---------------|-----------|----------|
| NCCL alltoall | 集合通信 | ~60-70% | ~50-60% | 无原生 |
| Tutel | 优化 alltoall | ~75% | ~65% | 无 |
| Perplexity MoE Comm | 自定义 | ~85% | ~80% | 有 |
| **DeepEP** | **NVSHMEM 单边** | **~95%** | **~90%** | **原生 FP8** |

## 4. Expert Parallelism 的最新进展（2025-2026）
- **Hybrid EP**: NVIDIA 提出混合专家并行，结合 EP + TP + DP，在不同并行维度间动态分配
- **Disaggregated EP**: 将 attention 和 expert 计算物理分离，独立扩展
- **Speculative Expert Pre-scheduling**: 预测下一层的路由决策，提前发起通信
- **Perplexity MoE Comm Library**: 可移植的高性能 MoE 通信库，比标准 alltoall 快 10x

## 5. 对 Channel Mixer 的意义
Expert Parallelism 是大规模 MoE 从理论走向实践的关键工程环节。DeepSeek-V3 的 256 专家能够高效训练和推理，DeepEP 功不可没。通信效率直接决定了 MoE 的实际加速比——如果 all-to-all 通信占比过高，MoE 的稀疏计算优势就会被通信开销抵消。DeepEP 的开源推动了整个 MoE 生态的工程水平。Disaggregated EP 是 2025-2026 年的重要趋势，可能根本性地改变 MoE 的部署架构。

## 6. 总结
a) 核心思想：NVSHMEM 单边通信替代 NCCL，打满带宽实现高效 EP（22字）
b) 速记 pipeline：
   1. Dispatch: 根据路由决策将 token 发送到目标专家 GPU
   2. Expert compute: 各 GPU 上的专家独立处理收到的 token
   3. Combine: 将专家输出收集回原 GPU
   4. DeepEP 在 1-3 步用 NVSHMEM 实现近线速通信
