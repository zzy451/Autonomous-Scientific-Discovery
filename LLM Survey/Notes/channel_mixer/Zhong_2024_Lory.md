# Lory: Fully Differentiable Mixture-of-Experts for Autoregressive Language Model Pre-training

**论文**: Lory: Fully Differentiable Mixture-of-Experts for Autoregressive Language Model Pre-training
**作者**: Ziyun Zhong, Zihan Wang, Yikang Shen, et al.
**年份**: 2024
**来源**: arXiv:2405.03133
**标签**: MoE, 全可微, 参数空间合并, 因果段路由

---

## 0. 摘要
Lory 是一种全可微的 MoE 架构，通过在参数空间中软合并专家（而非在 token 空间中路由）来实现条件计算。核心创新包括：(1) 因果段路由策略（causal segment routing），在段级别进行专家合并以保持自回归性质并提高效率；(2) 基于相似度的数据批处理（similarity-based data batching），提升专家专业化程度。在 150B token 上预训练，最大 30B 参数（1.5B 活跃），显著优于参数匹配的 dense 和 sparse MoE 基线。

## 1. 方法动机
a) 传统 Sparse MoE 使用离散 Top-K 路由，导致不可微、需要辅助损失、存在 token dropping 等问题。
b) SMEAR（Muqeeth et al., 2023）提出在参数空间中软合并专家，但仅在小规模 encoder 模型上验证，未扩展到自回归 LLM。
c) 参数空间合并在自回归模型中面临因果性挑战：合并权重不能依赖未来 token。
d) 假设：通过段级别的因果路由 + 数据批处理优化，参数空间合并可以扩展到大规模自回归 LLM。

## 2. 方法设计
a) 参数空间专家合并（核心思想）：
   - 不是将 token 路由到不同专家，而是将多个专家的参数加权合并为一个"虚拟专家"
   - 合并后的参数: W_merged = Σ_i w_i · W_i，其中 w_i 是路由权重
   - 所有 token 通过同一个合并后的 FFN 处理
   - 全可微：路由权重的梯度可以直接反传到路由网络

b) 因果段路由（Causal Segment Routing）：
   - 将输入序列分割为固定长度的段（segment）
   - 每个段的路由权重仅基于该段之前的 token 计算（保持因果性）
   - 同一段内所有 token 共享相同的合并专家参数
   - 效率优势：每段只需做一次参数合并，而非每个 token 一次

c) 基于相似度的数据批处理：
   - 训练时，将语义相似的文档聚合到同一个 batch
   - 使相同段内的 token 更可能需要相似的专家组合
   - 促进专家专业化：不同专家学习处理不同领域/主题的数据

## 3. 与其他方法对比
| 方法 | 路由空间 | 可微性 | 粒度 | 自回归兼容 |
|------|----------|--------|------|------------|
| Switch/Mixtral | Token 空间 | 不可微 | Token 级 | 是 |
| Soft MoE | Token 空间（软） | 全可微 | Token 级 | 困难 |
| SMEAR | 参数空间 | 全可微 | Token 级 | 未验证 |
| **Lory** | **参数空间** | **全可微** | **段级** | **是** |

## 4. 实验表现
- 在 150B token 上预训练，模型规模从 1B 到 30B（1.5B 活跃参数）
- 32 专家的 Lory 显著优于参数匹配的 dense 模型和传统 Top-K MoE
- 因果段路由的效率接近 dense 模型（参数合并的开销被段级摊销）
- 相似度数据批处理带来额外 0.5-1.0 perplexity 改善
- 专家利用率分析显示不同专家确实学到了不同领域的专业化

## 5. 对 Channel Mixer 的意义
Lory 开辟了 MoE 的另一条路径：不在 token 空间做路由，而在参数空间做合并。这从根本上消除了 token dropping 和负载不均问题，因为所有 token 都通过同一个（动态合并的）FFN。段级路由是对 Soft MoE 因果性问题的优雅解决方案。但参数空间合并的计算开销（需要实际合并权重矩阵）限制了专家数量的扩展性，目前仅验证到 32 专家。

## 6. 总结
a) 核心思想：在参数空间软合并专家，段级因果路由实现全可微 MoE（23字）
b) 速记 pipeline：
   1. 将序列分割为固定长度的段
   2. 每段基于前文计算路由权重（因果性）
   3. 加权合并多个专家的参数为一个虚拟 FFN
   4. 段内所有 token 通过合并后的 FFN 处理
