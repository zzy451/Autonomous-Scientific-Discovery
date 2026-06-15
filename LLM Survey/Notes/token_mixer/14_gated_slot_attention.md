# Gated Slot Attention for Efficient Linear-Time Sequence Modeling
**作者**: Yu Zhang, Songlin Yang, Ruijie Zhu, Yue Zhang, Leyang Cui, Yiqiao Wang, Bolun Wang, Freda Shi, Bo Zheng, Wei Bi (Alibaba, UCSB) | **年份**: 2025 | **arxiv**: 2505.06708

## 0. 摘要翻译
本文提出Gated Slot Attention (GSA)，一种基于slot attention思想的线性时间序列建模方法。GSA将隐藏状态组织为多个"slot"（槽位），每个slot维护一个独立的记忆向量。通过门控机制控制信息的写入和读取，GSA在保持线性复杂度的同时实现了更强的记忆管理能力。该方法在语言建模和多种下游任务上取得了与Mamba2和GLA等方法相当或更优的性能。

## 1. 方法动机
a) **为什么提出**: 线性注意力模型的矩阵值状态（$d_k \times d_v$）虽然提供了大容量记忆，但缺乏结构化的记忆管理——所有信息混合在一个大矩阵中。
b) **现有痛点**: (1) 线性注意力的状态更新缺乏结构化组织；(2) 不同类型的信息在状态矩阵中相互干扰；(3) 需要更好的记忆分配和管理机制。
c) **研究假设**: 借鉴slot attention的思想，将状态分为多个独立的slot，每个slot专注于存储特定类型的信息，可以减少干扰并提升记忆效率。

## 2. 方法设计
a) **Pipeline**: 将线性注意力的状态矩阵分解为多个slot，每个slot通过门控机制独立更新。

b) **模块功能**:
- **Slot结构**: 将$d_k \times d_v$的状态矩阵分为$M$个slot，每个slot维度为$d_k/M \times d_v$。每个slot可以看作一个独立的"记忆单元"。
- **门控写入 (Gated Write)**:
  - 写入门$g_t^w$控制新信息写入哪些slot
  - 遗忘门$g_t^f$控制每个slot保留多少旧信息
  - $S_t^{(m)} = g_t^f \cdot S_{t-1}^{(m)} + g_t^w \cdot k_t^{(m)} v_t^T$
- **门控读取 (Gated Read)**:
  - 读取门$g_t^r$控制从哪些slot读取信息
  - $o_t = \sum_m g_t^{r,(m)} \cdot q_t^{(m)T} S_t^{(m)}$
- **Softmax归一化**: 对slot的选择使用softmax归一化，使得模型在每个时间步集中关注少数slot。

c) **公式解释**:
- Slot attention的核心: 不同的slot竞争性地存储不同的信息模式
- 门控机制: 输入依赖的门控让模型动态决定"写入哪个slot"和"从哪个slot读取"
- 与GLA的关系: GSA可以看作GLA（Gated Linear Attention）的结构化扩展，增加了slot维度的组织

## 3. 与其他方法对比
| 方面 | GSA | GLA | Mamba2 | Delta Net | Transformer |
|------|-----|-----|--------|-----------|-------------|
| 状态结构 | 多slot | 单矩阵 | 多头矩阵 | 单矩阵+delta | KV cache |
| 记忆管理 | slot竞争 | 门控衰减 | 选择性 | 先删后写 | 精确存储 |
| 复杂度 | $O(Ld)$ | $O(Ld)$ | $O(LdN)$ | $O(LdN)$ | $O(L^2d)$ |
| 记忆组织 | 结构化 | 非结构化 | 多头 | 非结构化 | 无 |

## 4. 实验表现
- **语言建模**: PPL与Mamba2和GLA相当，在部分设置下略优
- **关联记忆**: 在MQAR等记忆密集型任务上表现良好
- **下游任务**: 在多个NLU基准上与同规模线性模型竞争
- **效率**: 保持线性时间和常数内存的推理效率
- **可解释性**: slot结构提供了一定的可解释性——可以分析不同slot存储了什么信息

## 5. 总结
a) **一句话概括**: GSA通过将线性注意力的状态矩阵组织为多个竞争性slot，配合门控读写机制，实现了更结构化的记忆管理，在保持线性复杂度的同时提升了记忆效率和模型性能。
b) **速记pipeline**: x → Q,K,V,Gates → 分配到M个Slot → 门控写入各Slot → 门控读取各Slot → 聚合 → Output
