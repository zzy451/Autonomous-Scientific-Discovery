# PaLM: Scaling Language Modeling with Pathways

## 基本信息
- **作者**: Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, et al.
- **年份**: 2022
- **arXiv**: 2204.02311
- **关键词**: Parallel Attention+FFN, 大规模语言模型, TPU效率

## 核心贡献（Module Sequence 维度）
PaLM 在 540B 参数规模上采用了 **Parallel Attention + FFN** 的块结构。

### 1. 标准串行结构 vs 并行结构
- **串行 (Standard)**:
  $y = x + \text{MLP}(\text{LN}(x + \text{Attn}(\text{LN}(x))))$
- **并行 (PaLM)**:
  $y = x + \text{Attn}(\text{LN}(x)) + \text{MLP}(\text{LN}(x))$

### 2. 并行结构的优势
- Attention 和 MLP 可以**同时计算**
- 减少分布式训练中的通信开销（只需一次 all-reduce 而非两次）
- 配合编译器优化（XLA on TPU）可进一步融合计算
- 训练吞吐量提升约 15%

### 3. 来源与前驱
- GPT-J (Wang & Komatsuzaki, 2021) 首先采用此设计
- PaLM 在更大规模上验证了其有效性
- 对于大模型（>8B），并行结构对质量的影响可忽略
- 对于小模型，可能会有轻微质量损失

### 4. PaLM 的其他架构选择
- SwiGLU 激活函数
- RoPE 位置编码
- Multi-Query Attention
- 无 bias

## 与综述的关联
- **Parallel Attention + FFN 的代表性工作**
- 在 Module Sequence 维度上，将串行变为并行是一个根本性的结构变化
- 权衡：计算效率 vs 表示能力（小模型可能损失质量）
- 后续被 Cerebras-GPT 等模型跟进
