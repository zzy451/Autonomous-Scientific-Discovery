# PolyGLU: State-Conditional Activation Routing in Transformer Feed-Forward Networks

**论文**: State-Conditional Activation Routing in Transformer Feed-Forward Networks
**作者**: (2026)
**来源**: arXiv:2603.13347
**标签**: FFN 激活函数, 动态路由, SwiGLU 替代, Channel Mixer

---

## 0. 摘要
PolyGLU（Polychromatic Gated Linear Unit）是 SwiGLU 的直接替代方案（drop-in replacement），其核心创新在于让 FFN 中的每个神经元能够根据输入状态动态选择 K=4 种激活函数之一。通过可微分的路由机制，PolyGLU 在不显著增加参数量的前提下提升了 FFN 的表达能力。

## 1. 方法动机
a) SwiGLU 虽然是当前主流 LLM 的标准 FFN 激活函数，但所有神经元使用同一个固定激活函数，限制了表达多样性。
b) 不同类型的输入（如事实回忆 vs 推理 vs 语法处理）可能需要不同的非线性变换特征。
c) 假设：如果每个神经元能根据当前隐状态动态选择最合适的激活函数，FFN 的表达能力可以进一步提升。

## 2. 方法设计
a) 核心机制 — 状态条件激活路由：
   - 维护 K=4 种候选激活函数（如 SiLU, ReLU², GELU, Identity 等）
   - 对每个 FFN 神经元，根据输入隐状态计算一个路由分布
   - 通过可微分机制（如 Gumbel-Softmax 或软加权）选择/混合激活函数
   - 输出 = Σ_k w_k · σ_k(x)，其中 w_k 是路由权重，σ_k 是第 k 种激活函数

b) 与标准 GLU 的关系：
   - SwiGLU: FFN(x) = (Swish(xW₁) ⊙ xV) W₂
   - PolyGLU: FFN(x) = (PolyAct(xW₁, x) ⊙ xV) W₂
   - PolyAct 替换了固定的 Swish，变为状态条件的多激活函数混合

c) 设计优势：
   - Drop-in replacement：不改变 FFN 的整体结构，仅替换激活函数部分
   - 路由开销小：路由网络是轻量级的（低秩投影 + softmax）
   - 可微分训练：无需离散路由，端到端可训练

## 3. 与其他方法对比
| 方法 | 激活函数 | 动态性 | 额外参数 | 稀疏性 |
|------|----------|--------|----------|--------|
| ReLU FFN | ReLU | 固定 | 无 | 天然稀疏 |
| SwiGLU | Swish | 固定 | 门控投影 | 无严格稀疏 |
| ReLU² | ReLU² | 固定 | 无 | 高稀疏 |
| KAN | B-spline | 可学习（边上） | 大量 | 无 |
| **PolyGLU** | **K=4 混合** | **输入条件动态** | **少量路由** | **取决于候选** |

## 4. 实验表现
- 作为 SwiGLU 的 drop-in 替代，在语言建模任务上取得一致的 perplexity 改善
- 额外参数开销约 1-3%（仅路由网络）
- 不同层/不同位置的神经元学到了不同的激活函数偏好分布，验证了"不同计算需要不同非线性"的假设

## 5. 对 Channel Mixer 的意义
PolyGLU 代表了 FFN 设计的一个新方向：不是替换整个 FFN 结构（如 MoE），而是在激活函数层面引入条件计算。这与 MoE 在专家层面的路由形成了有趣的互补——MoE 路由选择"哪组参数"，PolyGLU 路由选择"哪种非线性"。两者可以正交组合。

## 6. 总结
a) 核心思想：每个 FFN 神经元动态选择激活函数，提升表达多样性（20字）
b) 速记 pipeline：
   1. 维护 K=4 种候选激活函数
   2. 根据输入隐状态计算路由权重
   3. 软加权混合多种激活函数输出
   4. Drop-in 替换 SwiGLU，端到端可微训练
