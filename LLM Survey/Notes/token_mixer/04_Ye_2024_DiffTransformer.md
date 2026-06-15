# Differential Transformer
**作者**: Ye et al. (Microsoft Research) | **年份**: 2024 | **arxiv**: 2410.05258

## 0. 摘要翻译
Transformer 在大语言模型中是基础架构，但标准的 Softmax 注意力倾向于将注意力分配到不相关的上下文中（注意力噪声）。本文提出 **Differential Transformer (DIFF Transformer)**，其核心是 **差分注意力 (Differential Attention)** 机制：将注意力分数计算为两组独立 Softmax 注意力图的差值。类似于电气工程中的差分放大器消除共模噪声的原理，差分注意力能够消除注意力中的噪声，使模型更关注关键信息。实验表明，DIFF Transformer 在语言建模、长上下文建模、关键信息检索、幻觉抑制、上下文学习等方面均优于标准 Transformer。

## 1. 方法动机
a) **为什么提出这个方法**：标准 Softmax Attention 的一个根本问题是注意力权重必须为正且归一化，这导致即使不相关的 token 也会获得非零的注意力（注意力噪声）。这种噪声会干扰模型对关键信息的聚焦。

b) **现有方法的痛点**：
- Softmax 注意力不可避免地将部分概率质量分配给不相关 token（因为概率必须和为 1）
- 这种注意力噪声导致模型在检索关键信息时不够精确，容易产生幻觉
- 现有注意力机制缺乏内建的噪声抑制机制

c) **研究假设/直觉**：借鉴差分放大器的原理——用两路信号的差值来消除共模噪声。如果两组注意力都对噪声 token 给出相似的注意力分数，那么两者的差值就能有效消除这些噪声，只保留真正有区分度的信号。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 输入 token 分别投影为两组 Q/K 对：(Q1, K1) 和 (Q2, K2)，共享同一组 V
2. 分别计算两组 Softmax 注意力图：A1 = softmax(Q1 K1^T / √d), A2 = softmax(Q2 K2^T / √d)
3. 计算差分注意力：A_diff = A1 - A2
4. 输出 = A_diff · V（差分注意力加权的 value 求和）
5. 引入可学习标量 λ 对差分进行缩放调节

b) **核心模块功能**：
- **双路注意力**：两组独立的 Q/K 投影，生成两张注意力图。两组参数独立学习，但共享 V
- **差分操作**：A1 - A2 的差值运算消除了两组注意力中共同的噪声部分
- **可学习缩放因子 λ**：λ 初始化为接近 1 的值，控制差分的幅度。公式为 λ_init - λ · (1 - λ_init)，其中 λ_init 是超参数
- **GroupNorm**：在差分输出上应用 GroupNorm（而非 LayerNorm），稳定训练

c) **关键公式解释**：
- DiffAttn(X) = (softmax(Q1 K1^T / √d) - λ · softmax(Q2 K2^T / √d)) V
- 其中 Q1, Q2, K1, K2 分别由不同的投影矩阵生成
- λ 为可学习参数，控制噪声消除的强度
- 每个 head 分裂为两个 "半 head"，参数量与标准 MHA 基本相同

## 3. 与其他方法对比
- **与标准 Softmax Attention 的本质区别**：注意力权重可以为负值（通过差分），打破了 Softmax 的非负约束
- **与 Cog Attention 的比较**：两者都允许负权重注意力，但 CogAttn 通过减去一个基准向量实现，DIFF Transformer 通过两路 Softmax 差值实现，原理不同
- **与 Sigmoid Attention 的比较**：Sigmoid 注意力也不需要归一化，但 DIFF 仍然使用 Softmax，通过差分来去噪
- **创新点**：差分信号处理思想首次引入注意力机制；同参数量下显著提升模型质量
- **适用场景**：需要精确信息检索的任务、长上下文建模、需要减少幻觉的应用场景

## 4. 实验表现
- **关键结果**：
  - 语言建模：3B DIFF Transformer 性能匹配 6.8B 标准 Transformer
  - 长上下文检索：在 "Needle-in-a-Haystack" 多针检索场景中大幅优于标准 Transformer
  - 幻觉减少：在摘要和问答任务中幻觉率显著降低
  - 上下文学习：在 many-shot ICL 中表现更好，对无关示例更鲁棒
- **优势场景**：信息检索、长文档理解、抑制幻觉、上下文学习
- **局限性**：
  - 每个 head 需要两组 Q/K 投影，虽然总参数量接近但计算量略增
  - GroupNorm 的引入增加了实现复杂度
  - 需要调节 λ_init 超参数

## 5. 总结
a) **一句话概括（≤20字）**：双路 Softmax 做差分，消除注意力噪声。

b) **速记 pipeline**：
`Input → [Q1,K1] & [Q2,K2] → Softmax1 - λ·Softmax2 → DiffAttn·V → GroupNorm → Output`
