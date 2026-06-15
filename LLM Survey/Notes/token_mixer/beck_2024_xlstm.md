# xLSTM: Extended Long Short-Term Memory
**作者**: Maximilian Beck, Korbinian Pöppel, Markus Spanring, Andreas Auer, Oleksandra Prudnikova, Michael Kopp, Günter Klambauer, Johannes Brandstetter, Sepp Hochreiter | **年份**: 2024 | **arxiv**: 2405.04517

## 0. 摘要翻译
LSTM 的核心思想——常数误差传送带和门控——自 1990 年代提出以来经受住了时间考验。本文提出 xLSTM，通过两个关键改进扩展 LSTM：(1) 指数门控（exponential gating）和 (2) 新的记忆结构。由此产生两个变体：sLSTM（标量记忆+指数门控）和 mLSTM（矩阵记忆+协方差更新规则）。将 xLSTM 块组合成残差网络架构后，在语言建模上与 Transformer 和 SSM 竞争力相当。

## 1. 方法动机
a) **为什么**: LSTM 曾是序列建模的主力，但被 Transformer 取代。然而 Transformer 的二次复杂度和 SSM 的有限记忆容量都有局限。能否通过现代化改造让 LSTM 重新具有竞争力？
b) **痛点**: 传统 LSTM 的三个限制——(1) 无法修改已存储的信息（sigmoid 门控范围 [0,1]）；(2) 标量记忆容量有限；(3) 缺乏并行训练能力。
c) **假设**: 通过指数门控（允许更精确的存储控制）和矩阵记忆（扩大容量），LSTM 可以在大规模语言建模上匹配 Transformer。

## 2. 方法设计

### a) 两个变体

**sLSTM (Scalar LSTM)**:
- 保持标量记忆单元（与经典 LSTM 相同）
- 引入指数门控: 遗忘门和输入门使用 exp() 而非 sigmoid
- 新增多个记忆单元和头结构
- 支持记忆混合（不同单元间交互）
- 不可并行化，但适合需要精确状态跟踪的任务

**mLSTM (Matrix LSTM)**:
- 将标量记忆扩展为矩阵记忆 `C_t ∈ R^{d×d}`
- 协方差更新规则: `C_t = f_t · C_t-1 + i_t · v_t k_t^T`
- 类似线性注意力的外积更新，但带有指数门控
- 完全可并行化（类似线性 Transformer）
- 查询: `h_t = C_t q_t / max(|n_t^T q_t|, 1)` — 归一化检索

### b) 核心模块

**指数门控 (Exponential Gating)**:
- 输入门: `i_t = exp(w_i^T x_t + b_i)`
- 遗忘门: `f_t = exp(w_f^T x_t + b_f)` 或 `sigmoid(w_f^T x_t + b_f)`
- 归一化器: `n_t = f_t · n_{t-1} + i_t` — 防止数值溢出
- 使用 log-space 稳定化技巧避免指数爆炸

**mLSTM 的矩阵记忆**:
- 记忆更新: `C_t = f_t · C_{t-1} + i_t · v_t k_t^T`
- 这本质上是带门控的线性注意力
- k, v, q 分别由输入线性投影得到
- 记忆容量从 O(d) 提升到 O(d²)

### c) 关键公式
- mLSTM 更新: `C_t = f_t C_{t-1} + i_t v_t k_t^T`
- mLSTM 输出: `h_t = C_t q_t / max(|n_t^T q_t|, 1)`
- 归一化器: `n_t = f_t n_{t-1} + i_t k_t`
- 指数门控: `i_t = exp(ĩ_t)`, `f_t = exp(f̃_t)` 或 `σ(f̃_t)`

## 3. 对比
| 模型 | 记忆类型 | 门控 | 并行训练 | 记忆容量 |
|------|----------|------|----------|----------|
| LSTM | 标量 | sigmoid | 否 | O(d) |
| sLSTM | 标量+多头 | 指数 | 否 | O(d·H) |
| mLSTM | 矩阵 | 指数 | 是 | O(d²) |
| Linear Attn | 矩阵(KV状态) | 无 | 是 | O(d²) |
| Mamba | 对角矩阵 | 选择性 | 是(扫描) | O(d·N) |
| GLA | 矩阵 | 数据依赖 | 是(chunk) | O(d²) |

- mLSTM 与 GLA/DeltaNet 的关系: mLSTM 的更新规则类似线性注意力 + 指数门控
- sLSTM 的独特价值: 精确状态跟踪能力（如括号匹配、计数）

## 4. 实验
- **语言建模**: SlimPajama 上训练，xLSTM (7:1 mLSTM:sLSTM 比例) 在 125M-1.3B 参数范围匹配或超越 Transformer、Mamba、RWKV-4
- **Scaling**: xLSTM 的 scaling law 斜率与 Transformer 相当
- **长序列**: 在合成任务（Multi-Query Associative Recall）上，mLSTM 显著优于 Mamba
- **消融**: 指数门控和矩阵记忆各自贡献显著；sLSTM 在状态跟踪任务上不可替代
- **架构比例**: 最优配比约 7:1 (mLSTM:sLSTM)，纯 mLSTM 也很强

## 5. 总结
a) **一句话**: xLSTM 通过指数门控和矩阵记忆两个关键改进，将经典 LSTM 升级为可与 Transformer 和 SSM 竞争的现代序列模型，其中 mLSTM 本质上是带指数门控的线性注意力。
b) **速记 pipeline**: `Input → [sLSTM(ExpGate+ScalarMem) | mLSTM(ExpGate+MatrixMem: C+=iv·k^T)] × L layers → Output`
