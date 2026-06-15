# Titans: Learning to Memorize at Test Time
**作者**: Ali Behrouz, Peilin Zhong, Vahab Mirrokni (Google Research) | **年份**: 2025 | **arxiv**: 2501.00663

## 0. 摘要翻译
本文提出 Titans，一种新的序列模型家族，引入了神经长期记忆（Neural Long-term Memory）模块。该模块在测试时通过在线学习（类似梯度下降）来记忆历史上下文，并与短期注意力模块协同工作。Titans 将序列建模中的记忆问题重新定义为在线学习问题：记忆模块的参数在推理时持续更新以编码新信息，查询时通过前向传播检索。

## 1. 方法动机
a) **为什么**: 现有序列模型在长程记忆上面临根本性权衡——注意力精确但 O(n²)，RNN/SSM 高效但记忆有损。需要一种新的记忆机制，既能高效编码长历史又能精确检索。
b) **痛点**: (1) 线性注意力/SSM 的固定大小状态限制了记忆容量；(2) 注意力的 KV cache 随序列线性增长；(3) Infini-attention 等方法的压缩记忆检索精度有限。
c) **假设**: 将记忆视为在线学习问题——用一个小型神经网络作为记忆，通过梯度下降持续学习新信息，通过前向传播检索——可以获得比固定大小状态更好的记忆能力。

## 2. 方法设计

### a) 三种架构变体
```
1. MAC (Memory as Context):
   Memory output 作为额外 context 拼接到注意力的 KV 中
   [Attn(Q, [K_local; K_mem], [V_local; V_mem])]

2. MAG (Memory as Gate):
   Memory output 通过门控与注意力输出混合
   O = gate · Attn_output + (1-gate) · Memory_output

3. MAL (Memory as Layer):
   Memory 和 Attention 作为独立层交替堆叠
   [Memory Layer → Attention Layer → Memory Layer → ...]
```

### b) 核心模块：Neural Long-term Memory

**记忆模块 = 小型神经网络 M_θ**:
- 参数 θ 在推理时持续更新（test-time training）
- 写入（记忆）: 对新 token (k_t, v_t)，通过梯度下降更新 θ
  - `θ_t = θ_{t-1} - η · ∇_θ L(M_θ(k_t), v_t)`
  - 损失函数: `L = ||M_θ(k_t) - v_t||²`（让网络学会从 key 映射到 value）
- 读取（检索）: 对查询 q_t，直接前向传播
  - `mem_output = M_θ(q_t)`

**与线性注意力的联系**:
- 当 M_θ 是单层线性网络时: `θ = W`
- 写入: `W_t = W_{t-1} + η · (v_t - W_{t-1} k_t) k_t^T` — 这就是 delta rule！
- 读取: `output = W_t q_t` — 这就是线性注意力检索
- 因此线性注意力/DeltaNet 是 Titans 的特例（单层线性记忆）
- Titans 用多层非线性网络，记忆容量更大

**惊喜遗忘 (Surprise-based Forgetting)**:
- 不是所有 token 都值得记忆
- 用"惊喜度"（损失值大小）决定学习率: 惊喜大 → 学习率高 → 记忆更多
- `η_t = η · sigmoid(L(M_θ(k_t), v_t))` — 自适应学习率

### c) 关键公式
- 记忆写入: `θ_t = θ_{t-1} - η_t · ∇_θ ||M_θ(k_t) - v_t||²`
- 记忆读取: `o_t = M_{θ_t}(q_t)`
- 惊喜门控: `η_t = η · σ(||M_θ(k_t) - v_t||²)`
- 线性特例: 当 M 为线性层时退化为 DeltaNet

## 3. 对比
| 模型 | 记忆机制 | 记忆容量 | 写入方式 | 检索方式 |
|------|----------|----------|----------|----------|
| Transformer | KV cache | O(n·d) | 追加 | Softmax attn |
| Linear Attn | 矩阵状态 | O(d²) | 外积累加 | 线性投影 |
| DeltaNet | 矩阵状态 | O(d²) | Delta rule | 线性投影 |
| Infini-attn | 矩阵状态 | O(d²) | 外积累加 | 线性投影+门控 |
| Titans | 神经网络参数 | O(|θ|) 可扩展 | 梯度下降 | 前向传播 |

## 4. 实验
- **语言建模**: Titans-MAG 在 FineWeb 上训练，超越同规模 Transformer、Mamba、DeltaNet
- **长上下文**: 在 BABILong (>1M tokens) 上显著优于所有基线
- **Recall**: 在 MQAR (Multi-Query Associative Recall) 上，Titans 的非线性记忆优于线性记忆
- **Scaling**: 记忆网络越大（更多参数），记忆能力越强
- **效率**: 推理时记忆大小固定（网络参数量），不随序列增长
- **训练**: 需要二阶梯度（Hessian-vector product），训练开销比标准 Transformer 大

## 5. 总结
a) **一句话**: Titans 将序列记忆重新定义为在线学习问题，用一个在推理时通过梯度下降持续学习的小型神经网络作为长期记忆，统一了线性注意力（单层线性记忆的特例）并通过非线性扩展获得了更强的记忆能力。
b) **速记 pipeline**: `Input → [Short-term: Local Attention | Long-term: Neural Memory(write=SGD, read=forward)] → Gate/Concat/Alternate → Output`
