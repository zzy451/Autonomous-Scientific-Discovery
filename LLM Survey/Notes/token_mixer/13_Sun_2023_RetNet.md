# Retentive Network: A Successor to Transformer for Large Language Models
**作者**: Sun et al. (Microsoft Research) | **年份**: 2023 | **arxiv**: 2307.08621

## 0. 摘要翻译
大语言模型面临 "不可能三角"：**训练并行性**、**推理效率**（O(1) 复杂度/步）和**性能质量**三者难以兼得。Transformer 有训练并行性和高质量但推理低效；RNN 有推理效率但训练不可并行。本文提出 **Retentive Network (RetNet)**，其核心是 **多尺度保留机制 (multi-scale retention)**。Retention 同时支持三种计算范式：(1) 并行表示（类似注意力，用于高效训练），(2) 递推表示（类似 RNN，用于高效推理），(3) 分块递推表示（两者的混合）。RetNet 在解决不可能三角的同时，实现了与 Transformer 相当的语言建模性能。

## 1. 方法动机
a) **为什么提出这个方法**：追求同时满足三个目标——像 Transformer 一样并行训练、像 RNN 一样 O(1) 推理、像 Transformer 一样高质量。

b) **现有方法的痛点**：
- Transformer：训练并行 + 高质量，但推理 O(n)/步（需要完整 KV cache）
- RNN/LSTM：推理 O(1)/步，但训练必须串行（BPTT）
- Linear Attention：可以同时并行训练和 O(1) 推理，但质量显著下降
- S4/Mamba（同期/后续）：也在尝试解决此三角，但 RetNet 的切入角度不同

c) **研究假设/直觉**：通过在注意力矩阵中引入 **指数衰减掩码 (exponential decay mask)**，可以使注意力公式同时具有并行形式（类似 Attention 的矩阵乘法）和递推形式（类似 RNN 的隐状态更新），从而统一两者的优势。

## 2. 方法设计
a) **方法流程 (pipeline)**：

**并行表示（训练时）**：
1. Q = x W_Q, K = x W_K, V = x W_V
2. 构造衰减矩阵 D：D_{nm} = γ^{n-m}（n>=m），γ 为衰减因子
3. Retention(Q,K,V) = (QK^T ⊙ D) V（注意没有 Softmax！）

**递推表示（推理时）**：
1. 维护隐状态 S_n = γ · S_{n-1} + K_n^T V_n
2. 输出 o_n = Q_n · S_n
3. 每步 O(d^2) 复杂度，固定大小隐状态

**分块递推（混合）**：
- 块内用并行表示，块间用递推传递隐状态

**多尺度**：不同 head 使用不同的衰减因子 γ_h，捕获不同时间尺度的依赖。

b) **核心模块功能**：
- **Retention 机制**：QK^T 乘以指数衰减矩阵 D，替代 Softmax 归一化
- **指数衰减 γ**：控制历史信息的遗忘速率，γ 越大记忆越长
- **多尺度 (Multi-Scale)**：不同 head 的 γ 值不同（如 1-2^{-1}, 1-2^{-2}, ..., 1-2^{-h}），使模型同时捕获短程和长程依赖
- **GroupNorm**：对 retention 输出做 GroupNorm（类似 DIFF Transformer），稳定训练
- **Swish Gate**：输出经过 swish 门控

c) **关键公式解释**：
- 并行：Retention(X) = (QK^T ⊙ D) V，D_{nm} = γ^{n-m} (n>=m), 0 (n<m)
- 递推：S_n = γ S_{n-1} + K_n^T V_n，o_n = Q_n S_n
- 隐状态大小：d_k × d_v（固定，不随序列增长）
- 多尺度：γ_h = 1 - 2^{-(5 + h/H · 7)}，h = 0, 1, ..., H-1

## 3. 与其他方法对比
- **与 Transformer 的本质区别**：用指数衰减替代 Softmax 归一化，使得递推表示成为可能
- **与 Linear Attention 的区别**：Linear Attention 可视为 γ=1（无衰减）的 Retention，RetNet 的衰减因子是关键改进
- **与 Mamba/S4 的比较**：RetNet 的衰减是标量的指数衰减，Mamba 的 A 矩阵更灵活；Mamba 有选择性机制而 RetNet 的 γ 是固定的
- **与 RWKV 的比较**：RWKV-4 也使用类似衰减机制，但 RetNet 的理论框架更清晰（基于对注意力矩阵的分解）
- **创新点**：三种等价表示统一了并行训练和递推推理
- **适用场景**：需要高效推理的 LLM 部署场景

## 4. 实验表现
- **关键结果**：
  - 语言建模质量与同规模 Transformer 接近（1.3B-6.7B 参数）
  - 推理速度：比 Transformer 快 8.4 倍（long-sequence），内存节省 70%
  - 训练速度：比 Transformer 快 25-50%（得益于无 Softmax 的简化计算）
  - 支持无损推理：并行和递推形式数学等价
- **优势场景**：流式推理、实时应用、资源受限的部署
- **局限性**：
  - 固定的 γ 不具备输入依赖的选择性（vs Mamba 的 input-dependent Δ）
  - 隐状态大小 d_k × d_v 固定，信息容量有限
  - 在需要精确长距离回忆的任务上可能不如全注意力
  - 在更大规模（>13B）上的验证相对有限

## 5. 总结
a) **一句话概括（≤20字）**：指数衰减注意力，统一并行训练与递推推理。

b) **速记 pipeline**：
`训练: (QK^T ⊙ γ^{n-m}) V → 并行矩阵乘`
`推理: S_n = γ·S_{n-1} + K_n^T V_n, o_n = Q_n·S_n → O(1)递推`
`多尺度: 不同head用不同γ捕获不同时间尺度`
