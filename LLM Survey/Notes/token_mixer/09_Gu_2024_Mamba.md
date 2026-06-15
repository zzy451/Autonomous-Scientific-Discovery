# Mamba: Linear-Time Sequence Modeling with Selective State Spaces
**作者**: Albert Gu, Tri Dao | **年份**: 2024 (arXiv: 2312) | **arxiv**: 2312.00752

## 0. 摘要翻译
基础模型（如大语言模型）的核心是序列变换骨架。尽管 Transformer 及其核心注意力机制主导了这一领域，但其二次方复杂度限制了长序列建模。本文提出 **Mamba**，一种基于选择性状态空间模型 (Selective State Space Model, Selective SSM) 的新架构。Mamba 的核心创新是 **选择性机制 (selection mechanism)**：让 SSM 的参数（B, C, Δ）成为输入依赖的（input-dependent），使模型能够根据内容选择性地传播或遗忘信息。结合硬件感知的并行扫描算法，Mamba 实现了线性时间复杂度的序列建模，在语言、音频、基因组学等多领域达到或超过了同等规模 Transformer 的性能。

## 1. 方法动机
a) **为什么提出这个方法**：SSM（如 S4）拥有线性复杂度和长距离建模的优势，但因为参数与输入无关（time-invariant），在离散信息密集的语言建模中表现不如 Transformer。需要让 SSM 具备内容感知的选择能力。

b) **现有方法的痛点**：
- Transformer：O(n^2) 注意力复杂度，KV cache 随序列长度线性增长
- 传统 SSM (S4)：线性复杂度但参数固定不变（time-invariant），无法根据内容选择性记忆，在语言建模上落后于 Transformer
- Linear Attention：理论线性复杂度但质量显著下降

c) **研究假设/直觉**：序列建模的核心挑战是如何在固定大小的隐状态中有选择地压缩上下文。Attention 通过存储完整 KV 来避免压缩（牺牲效率），RNN/SSM 通过固定规则压缩（牺牲质量）。让 SSM 的压缩规则依赖于输入内容，就能在保持线性复杂度的同时实现选择性记忆。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 输入 x 经过线性投影扩展维度
2. 一路经过因果卷积（short convolution）
3. SSM 参数 (B, C, Δ) 由输入动态生成（选择性机制）：
   - B = Linear(x)，C = Linear(x)，Δ = softplus(Linear(x))
4. 执行离散化的 SSM 递推：h_t = Ā h_{t-1} + B̄_t x_t，y_t = C_t h_t
5. 另一路经过 SiLU 激活作为门控
6. 两路相乘后经过输出投影

b) **核心模块功能**：
- **选择性机制 (Selection)**：B, C, Δ 随输入变化，使得模型能根据内容调节信息传播
  - Δ 控制"遗忘速度"：大 Δ → 更多遗忘旧信息，关注当前输入
  - B 控制"输入选择"：决定当前输入如何写入隐状态
  - C 控制"输出选择"：决定从隐状态中读取什么
- **硬件感知算法**：由于选择性使 SSM 变为 time-variant，无法用 FFT 卷积，改用并行扫描 (parallel scan) 算法在 GPU SRAM 中高效计算
- **简化架构**：去掉标准 Transformer 的 MLP 层，将 SSM 与门控融合为单一模块（类似 H3/Gated MLP 的合并）

c) **关键公式解释**：
- 连续 SSM：h'(t) = A h(t) + B(t) x(t)，y(t) = C(t) h(t)
- 离散化：Ā = exp(Δ A)，B̄ = (Δ A)^{-1} (Ā - I) · Δ B
- 选择性参数：B_t = s_B(x_t), C_t = s_C(x_t), Δ_t = softplus(s_Δ(x_t))
- 隐状态维度 N（通常 16），模型维度 D，扩展比 E=2

## 3. 与其他方法对比
- **与 Transformer 的本质区别**：Mamba 用固定大小隐状态递推替代 KV cache，推理复杂度 O(1)/step vs Attention 的 O(L)/step
- **与 S4 的区别**：S4 的 SSM 参数固定不变（LTI），Mamba 的参数依赖输入（time-varying + selective）
- **与 RWKV/RetNet 的比较**：都是线性递推模型，但 Mamba 的选择性机制让参数随输入动态变化，表达能力更强
- **与 Linear Attention 的比较**：Linear Attention 可视为无选择性的退化 SSM，Mamba 的选择性是关键优势
- **创新点**：
  1. 选择性 SSM（参数输入依赖）
  2. 硬件感知并行扫描算法
  3. 简化的无 MLP 架构
- **适用场景**：长序列建模、语言建模、音频、DNA 序列等

## 4. 实验表现
- **关键结果**：
  - Mamba-3B 性能匹配或超过同规模 Transformer (如 2x Mamba-1.4B ≈ Transformer-3B)
  - 在长序列基准上显著优于 Transformer（如合成的 selective copy、induction head 任务）
  - 推理吞吐量：在长序列上比 Transformer 快 5 倍
  - 推理内存：隐状态大小固定，不随序列长度增长
- **优势场景**：长序列建模、流式推理（O(1) 内存/步）、音频和基因组学
- **局限性**：
  - 在需要精确长距离点查（recall）的任务上可能不如全注意力
  - 隐状态维度 N 有限，信息压缩可能丢失细节
  - 不支持并行的 prefix 查询（需要顺序递推来访问中间隐状态）
  - 预训练规模（3B）相对较小，更大规模的验证后续在 Mamba-2 中进行

## 5. 总结
a) **一句话概括（≤20字）**：输入依赖的选择性 SSM，线性复杂度序列建模。

b) **速记 pipeline**：
`Input → LinearProj → ┌ Conv1d → SSM(B(x),C(x),Δ(x)) ┐ ⊙ Gate(SiLU) → OutputProj`
`SSM递推: h_t = Ā·h_{t-1} + B̄(x_t)·x_t, y_t = C(x_t)·h_t`
