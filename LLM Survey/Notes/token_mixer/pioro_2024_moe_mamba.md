# MoE-Mamba: Efficient Selective State Space Models with Mixture of Experts
**作者**: Maciej Pioro, Kamil Ciebiera, Krystian Krol, Jan Ludziejewski, Sebastian Jaszczur | **年份**: 2024 | **arxiv**: 2401.04081

## 0. 摘要翻译
状态空间模型（SSM）已成为序列建模领域的有力竞争者，挑战了 Transformer 的主导地位。与此同时，混合专家（MoE）显著提升了基于 Transformer 的 LLM 的效率。本文将 SSM 与 MoE 结合，提出 MoE-Mamba。该模型在 Mamba 层之间交替插入 MoE 前馈层，使模型在保持 Mamba 推理效率的同时获得条件计算带来的容量提升。MoE-Mamba 在相同性能下比 Mamba 少用 2.2 倍训练步数，同时优于 Transformer-MoE 基线。

## 1. 方法动机
a) **为什么**: Mamba 作为 SSM 的代表在序列建模上展现了与 Transformer 相当的性能，但其每层参数全部激活（dense），缺乏条件计算能力。MoE 已被证明能有效扩展 Transformer 的参数量而不成比例增加计算量，自然的问题是：MoE 能否同样提升 SSM？
b) **痛点**: (1) 纯 Mamba 模型的参数效率受限于 dense 计算；(2) 简单地将 Mamba 内部的线性层替换为 MoE 并不直观，因为 SSM 的循环结构与 MoE 的 token-wise 路由存在设计张力；(3) 需要找到 SSM 与 MoE 的最佳组合方式。
c) **假设**: Mamba 层负责序列级的"无条件"信息聚合（类似全局记忆），MoE 层负责 token 级的"条件"处理（根据每个 token 的内容路由到不同专家），两者交替可以互补。

## 2. 方法设计

### a) 整体架构
MoE-Mamba 采用交替（interleaved）架构：
```
[Mamba Block] → [MoE FFN Block] → [Mamba Block] → [MoE FFN Block] → ...
```
即每隔一个 Mamba 层插入一个 MoE 前馈层，替代原始 Mamba 中的普通 FFN。

### b) Mamba Block（不变）
标准 Mamba 块，包含：
- 输入投影（扩展 E 倍）
- 1D 因果卷积（Conv1d）
- 选择性 SSM（S6 机制）
- 输出投影（压缩回原维度）
- 残差连接 + LayerNorm

```
x → Linear(expand) → Conv1d → SSM(S6) → Linear(compress) → + residual
```

### c) MoE FFN Block
替代普通 FFN 的 MoE 层：
- 使用 Top-k 路由（通常 k=2），每个 token 选择 k 个专家
- 每个专家是一个标准 FFN（两层线性 + 激活函数）
- 路由器（Router）: `g(x) = TopK(softmax(W_r · x))`
- 输出: `y = Σ_{i∈TopK} g_i(x) · Expert_i(x)`
- 辅助负载均衡损失防止路由坍塌

### d) 设计变体（消融）
论文探索了多种组合方式：
1. **Vanilla Mamba**: 纯 Mamba 层堆叠（baseline）
2. **Mamba-MoE (every layer)**: 每个 Mamba 层后都接 MoE
3. **Mamba-MoE (alternating)**: 交替放置（最终采用方案）
4. **MoE inside Mamba**: 将 Mamba 内部的线性投影替换为 MoE（效果不如交替方案）

### e) 关键设计选择
- 交替放置优于每层都加 MoE（计算效率更高，性能相当）
- Mamba 层提供序列混合（token mixing），MoE 层提供通道混合（channel mixing）
- 保持 Mamba 的线性推理复杂度不变（MoE 只在 FFN 层，不影响循环状态）

## 3. 对比
| 方法 | Token Mixer | Channel Mixer | 条件计算 | 推理复杂度 |
|------|------------|--------------|---------|-----------|
| Transformer | Self-Attention | FFN | 否 | O(n²) |
| Transformer-MoE | Self-Attention | MoE FFN | 是(FFN) | O(n²) |
| Mamba | SSM (S6) | Linear Proj | 否 | O(n) |
| MoE-Mamba | SSM (S6) | MoE FFN | 是(FFN) | O(n) |
| Jamba (后续) | Attention+Mamba | MoE FFN | 是(FFN) | 混合 |

## 4. 实验
- **训练设置**: 在 C4 数据集上训练，模型规模约 ~350M-800M 参数（活跃参数更少）
- **核心结果**:
  - MoE-Mamba 达到与 Mamba 相同的 perplexity 仅需 2.2x 更少的训练步数
  - 在相同训练步数下，MoE-Mamba 的 perplexity 显著低于 Mamba 和 Transformer-MoE
  - 推理吞吐量与 Mamba 相当（MoE 的稀疏激活不显著增加推理延迟）
- **消融实验**:
  - 交替放置 vs 每层放置: 交替方案在相同 FLOPs 下更优
  - 专家数量: 8 个专家 Top-2 路由效果良好
  - MoE 放置位置: FFN 层比 Mamba 内部投影层效果更好
- **Scaling**: 随模型规模增大，MoE-Mamba 相对 Mamba 的优势保持

## 5. 总结
a) **一句话**: MoE-Mamba 将 MoE 条件计算引入 Mamba 架构，通过交替堆叠 Mamba 层（序列混合）和 MoE FFN 层（条件通道混合），在保持线性推理复杂度的同时以 2.2 倍更少的训练步数达到 Mamba 同等性能，为 SSM+MoE 的结合开辟了方向。
b) **速记 pipeline**: `Input → [Mamba(Conv1d→S6 SSM) → MoE-FFN(TopK Router→Experts)] × N layers → Output`
