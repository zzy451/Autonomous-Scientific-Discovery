# Parallel Attention (GPT-J / GPT-NeoX Style)

**论文信息**: Wang, B., Komatsuzaki, A. (2021) - GPT-J; Black, S. et al. (2022) - GPT-NeoX
**分类**: Width (并行子层结构)

## 核心思想
将标准 Transformer 的串行结构（先 Attention 后 FFN）改为并行结构，Attention 和 FFN 同时计算，输出叠加到残差流。

## 数学公式
**串行 (标准)**:
  x' = x + Attention(LN(x))
  x'' = x' + MLP(LN(x'))

**并行 (GPT-J)**:
  x' = x + Attention(LN(x)) + MLP(LN(x))

## 关键优势
1. **通信效率**: 张量并行训练时，两个 all-reduce 合并为一个
2. **吞吐提升**: 约 **15%** 训练吞吐提升
3. **简化计算图**: 减少顺序依赖

## 与残差连接的关系
并行结构改变了残差连接的拓扑：
- 串行: 残差流经两次加法（先 Attn 再 MLP）
- 并行: 残差流只经一次加法（Attn+MLP 同时）
- 本质上是残差连接**宽度**的变化：同一层有更宽的残差分支

## 使用案例
- GPT-J-6B, GPT-NeoX-20B (EleutherAI)
- PaLM (Google)
- 被多个大规模 LLM 采用

## 与综述的关联
属于 **Width** 维度。并行结构可以理解为将两个窄残差分支合并为一个宽分支：
- 与 Hyper-Connection（多条残差通道）形成对比
- 并行是工程驱动的宽度扩展
- Hyper-Connection 是理论驱动的宽度扩展

## 核心贡献
通过改变残差连接拓扑实现训练效率优化，被工业界广泛采用。
