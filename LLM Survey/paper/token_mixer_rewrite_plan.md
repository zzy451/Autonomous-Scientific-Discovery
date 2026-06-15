# Token Mixer Section 重写计划

## 核心论点 (Thesis)

Token Mixer 的演进不是简单的"方法替代"，而是围绕一个根本性张力展开的：
**训练时的表达力 vs 推理时的效率**。

所有方法都在这个张力的不同位置做出 trade-off：
- Softmax Attention: 训练表达力最强（精确recall），但推理 O(N) KV cache + O(N²) prefill
- Linear Attention/SSM: 推理 O(1) 状态，但训练时的固定状态容量限制了recall
- Hybrid: 用少量 Attention 层补回 recall，大量高效层处理长程

## 贯穿全文的三条主线

1. **Recall-Throughput Trade-off**: 从 MHA → GQA → MLA → Linear → SSM → Hybrid，每一步都在这个 trade-off 上移动
2. **训练/推理二象性**: 同一个数学对象（如线性注意力）在训练时是矩阵乘法，推理时是 RNN；FlashAttention 不改变数学但改变了 IO 模式
3. **收敛趋势**: 独立的研究路线（Linear Attn, SSM, Delta Rule, TTT）在数学上收敛到同一个框架（SSD/delta rule），暗示存在一个"最优线性复杂度 token mixer"

## 新的 Section 结构

### 引言段 (新增，~30行)
- Token Mixer 的角色：序列中 token 间信息交换的核心机制
- 核心张力：表达力 vs 效率
- 2017-2026 演进的鸟瞰图
- 本节组织逻辑

### 1. Softmax Attention: The Gold Standard (MHA + KV-Cache Opt)
- 保留现有内容，但加强"为什么它是 gold standard"的分析
- 训练时：universal approximator, 精确 recall
- 推理时：KV cache 瓶颈 → MQA/GQA/MLA/CLA 的演进
- **新增**: 训练/推理不对称性分析

### 2. Making Attention Affordable: Sparse and Hardware-Efficient Approaches
- 合并 Sparse Attention + Hardware-Efficient Attention
- 逻辑：都是在保持 softmax attention 数学的前提下降低实际成本
- Sparse: 减少计算量（哪些 token 对需要计算）
- FlashAttention: 减少 IO（怎么计算更快）
- **新增**: 两者的正交性和组合

### 3. Beyond Softmax: Linear Attention and the Recurrence Connection
- 保留现有 Linear Attention 内容
- **加强**: kernel trick → 结合律 → RNN 对偶性的推导
- **加强**: 为什么线性注意力的 recall 弱于 softmax（信息论分析）

### 4. State Space Models and Modern RNNs
- 保留现有 SSM 内容
- **加强**: S4 → Mamba → Mamba-2 → Mamba-3 的演进逻辑
- **新增**: RWKV-7, Gated Delta Networks 的收敛

### 5. The Great Convergence: Unifying Linear Attention, SSMs, and Delta Rule
- **全新**: SSD 框架如何统一这些方法
- Delta rule = TTT-Linear = DeltaNet = online gradient descent
- 这个收敛意味着什么

### 6. Hybrid Architectures: The Pragmatic Optimum
- 大幅扩展 Hybrid 部分
- Jamba, MiniMax-01, Zamba2, Griffin/RecurrentGemma
- 7:1 比例的普遍性
- **新增**: 为什么 hybrid 是当前最优解的理论分析

### 7. Extending Attention's Expressivity
- 合并 Negative Weights + Softmax Alternatives
- Diff Attention, Sigmoid Attention, Gated Attention
- 逻辑：都是在修改 attention 的数学性质

### 8. Inference-Time Optimization
- 合并 KV-Cache Compression + Inference Optimization
- 训练时 vs 推理时的不同优化目标
- H2O, SnapKV, PagedAttention, Speculative Decoding

### 9. Test-Time Adaptive Memory
- TTT, Titans
- 训练/推理边界的模糊化

### 10. Summary and Outlook
- 对比表格
- 未来方向
