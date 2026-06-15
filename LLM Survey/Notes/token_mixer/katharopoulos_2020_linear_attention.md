# Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention
**作者**: Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, François Fleuret | **年份**: 2020 | **arxiv**: 2006.16236

## 0. 摘要翻译
本文揭示了 Transformer 与 RNN 之间的深层联系：通过将 softmax 注意力中的指数核替换为一般的核函数 φ(·)，注意力可以被重写为线性形式，从而将自回归 Transformer 转化为 RNN。这种"线性注意力"在因果（自回归）设置下可以用循环形式计算，实现 O(n) 的训练复杂度和 O(1) 的推理步进复杂度。本文是线性注意力的奠基性工作。

## 1. 方法动机
a) **为什么**: Transformer 的 softmax 注意力在自回归推理时需要 O(n) 的 KV cache 和 O(n) 的每步计算。如果能将注意力转化为 RNN 形式，就能实现常数时间推理。
b) **痛点**: (1) softmax 注意力的非线性使得无法改变计算顺序；(2) 自回归推理时每步都要重新计算与所有历史 token 的注意力；(3) 需要找到一种既保持注意力表达能力又允许循环计算的方法。
c) **假设**: softmax(QK^T) 可以被分解为 φ(Q)φ(K)^T 的形式，利用矩阵乘法结合律改变计算顺序，从而实现线性复杂度。

## 2. 方法设计

### a) 核心推导

**标准注意力**:
```
O_i = Σ_j [exp(q_i · k_j) / Σ_j' exp(q_i · k_j')] · v_j
```

**核化注意力** (用核函数 κ(q,k) = φ(q)^T φ(k) 替代 exp(q·k)):
```
O_i = Σ_j [φ(q_i)^T φ(k_j) / Σ_j' φ(q_i)^T φ(k_j')] · v_j
    = φ(q_i)^T [Σ_j φ(k_j) v_j^T] / φ(q_i)^T [Σ_j' φ(k_j')]
    = φ(q_i)^T S_i / φ(q_i)^T z_i
```

**关键洞察**: 
- `S_i = Σ_{j≤i} φ(k_j) v_j^T` — 可以递推计算: `S_i = S_{i-1} + φ(k_i) v_i^T`
- `z_i = Σ_{j≤i} φ(k_j)` — 可以递推计算: `z_i = z_{i-1} + φ(k_i)`
- 因此因果线性注意力可以用 RNN 形式计算！

### b) 核函数选择
- 论文使用: `φ(x) = elu(x) + 1`（保证非负）
- 其他选择: ReLU, softmax 的 Taylor 展开, 随机特征等
- 核函数的选择直接影响近似质量

### c) 双重计算模式
**训练模式 (并行)**:
- 直接计算 `O = (φ(Q) φ(K)^T ⊙ mask) V` — O(n·d²) 或 O(n²·d)
- 当 d < n 时用左结合: `O = φ(Q) (φ(K)^T V)` — O(n·d²)

**推理模式 (循环)**:
- 维护状态: `S_t = S_{t-1} + φ(k_t) v_t^T` ∈ R^{d×d}
- 输出: `o_t = φ(q_t)^T S_t / φ(q_t)^T z_t`
- 每步: O(d²) 计算，O(d²) 内存 — 与序列长度无关

### d) 关键公式
- 线性注意力: `O_i = φ(q_i)^T S_i / φ(q_i)^T z_i`
- 状态更新: `S_i = S_{i-1} + φ(k_i) ⊗ v_i`
- 归一化: `z_i = z_{i-1} + φ(k_i)`
- 核函数: `φ(x) = elu(x) + 1`

## 3. 对比
| 方法 | 训练复杂度 | 推理/step | 精确注意力 | 循环形式 |
|------|-----------|----------|-----------|---------|
| Softmax Attention | O(n²d) | O(nd) | 是 | 否 |
| Linear Attention | O(nd²) | O(d²) | 否(近似) | 是 |
| Performer | O(nd²) | O(d²) | 否(随机特征) | 是 |
| Linformer | O(nkd) | O(kd) | 否(低秩) | 否 |

## 4. 实验
- **语言建模**: 在 WikiText-103 上，线性注意力质量略低于 softmax（PPL 差距 ~2-5）
- **速度**: 在长序列上训练速度提升 2-4x（n=4096 时）
- **推理**: 自回归推理速度提升 ~1000x（不需要 KV cache 线性增长）
- **图像生成**: 在自回归图像生成上效果良好
- **局限**: 核近似导致的质量损失在 LLM 规模上较为明显，后续工作（GLA、Based、Lightning Attention）致力于缩小这一差距

## 5. 总结
a) **一句话**: 本文揭示了通过核化替换 softmax，注意力可以转化为 RNN 的循环形式，实现 O(1) 推理步进复杂度，奠定了线性注意力的理论基础，催生了 GLA、DeltaNet、Lightning Attention 等后续工作。
b) **速记 pipeline**: `Input → φ(Q), φ(K), V → Train: O = φ(Q)(φ(K)^T V) | Infer: S_t += φ(k_t)v_t^T, o_t = φ(q_t)^T S_t → Output`
