# Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention
**作者**: Tsendsuren Munkhdalai, Manaal Faruqui, Siddharth Gopal | **年份**: 2024 | **arxiv**: 2404.07143

## 0. 摘要翻译
本文提出 Infini-attention，一种高效的注意力机制，将压缩记忆（compressive memory）融入标准注意力中，使 Transformer 能在有限内存和计算资源下处理无限长的输入序列。Infini-attention 在单个注意力层中同时集成了掩码局部注意力和长期线性注意力机制。

## 1. 方法动机
a) **为什么**: LLM 需要处理越来越长的上下文（书籍、代码库、长对话），但标准注意力的内存和计算随序列长度二次增长。
b) **痛点**: (1) 现有长上下文方法（如滑动窗口）会丢弃旧信息；(2) 简单增大上下文窗口成本过高；(3) 需要一种既能保留全局信息又不增加内存的方案。
c) **假设**: 通过在注意力层中维护一个压缩记忆（类似线性注意力的 KV 状态），可以在有限内存中编码无限长的历史信息。

## 2. 方法设计

### a) Pipeline
对每个注意力层，处理流程为:
1. 将输入序列分成固定大小的段（segments）
2. 对每段执行标准因果注意力（局部）
3. 同时从压缩记忆中检索信息（全局）
4. 将局部注意力输出和记忆检索输出通过学习的门控混合
5. 用当前段的 KV 更新压缩记忆

### b) 核心模块

**压缩记忆 (Compressive Memory)**:
- 维护一个固定大小的关联记忆矩阵 `M ∈ R^{d_key × d_value}`
- 记忆检索: `A_mem = σ(Q M) / σ(Q z)` — 其中 z 是归一化项
- 记忆更新: `M ← M + K^T V`（线性注意力风格的外积累积）
- 可选 delta 更新规则: `M ← M + K^T (V - σ(K)M)` — 减少冗余写入

**门控混合 (Gated Aggregation)**:
- `O = sigmoid(β) ⊙ A_mem + (1 - sigmoid(β)) ⊙ A_dot`
- β 是可学习的标量门控参数
- A_dot 是标准 dot-product 注意力输出
- A_mem 是从压缩记忆检索的输出

### c) 关键公式
- 局部注意力: `A_dot = softmax(QK^T/√d) V` （标准段内注意力）
- 记忆检索: `A_mem = σ(Q) M_s-1 / (σ(Q) z_s-1)` （线性注意力检索）
- 记忆更新: `M_s = M_{s-1} + σ(K)^T V`
- 归一化更新: `z_s = z_{s-1} + Σ_i σ(k_i)`
- 最终输出: `O = sigmoid(β) ⊙ A_mem + (1 - sigmoid(β)) ⊙ A_dot`

## 3. 对比
| 方法 | 上下文长度 | 额外内存 | 信息保留 |
|------|-----------|----------|----------|
| 标准注意力 | 固定窗口 | O(n²) | 窗口内完整 |
| 滑动窗口 | 局部 | O(w²) | 丢弃远距离 |
| Ring Attention | 分布式长 | 多设备 | 完整 |
| Infini-attention | 无限 | O(d²) 固定 | 压缩保留 |

- 与 Memorizing Transformers 对比: Infini-attention 不需要存储原始 KV，内存恒定
- 与纯线性注意力对比: 保留了局部精确注意力的能力

## 4. 实验
- **长文本语言建模**: 在 PG19 和 Arxiv-Math 上，1M token 输入下困惑度持续下降
- **书籍摘要**: 在 BookSum 上，使用 Infini-attention 的 8B 模型处理 500K token 输入，超越之前的 SOTA
- **Passkey Retrieval**: 在 1M token 长度的大海捞针任务中达到完美准确率
- **内存效率**: 相比全注意力，内存使用减少 114x（处理 1M tokens 时）
- **即插即用**: 可以对已有 Transformer 模型进行 continual pre-training 来添加 Infini-attention

## 5. 总结
a) **一句话**: Infini-attention 通过在每个注意力层中维护固定大小的压缩记忆（线性注意力状态），并与局部注意力门控混合，实现了有限内存下的无限上下文处理。
b) **速记 pipeline**: `Input segments → [Local Causal Attn ‖ Memory Retrieval(σ(Q)·M)] → Gated Mix(β) → Update Memory(M += σ(K)^T V) → Output`
