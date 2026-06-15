# Peng et al. 2024 - Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence (RWKV v5/v6)

**论文信息**
- 标题: Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence
- 作者: Bo Peng et al.
- 年份: 2024
- arXiv: 2404.05892

## 0. 摘要翻译
我们提出RWKV-5 (Eagle) 和 RWKV-6 (Finch)，RWKV架构的新一代。Eagle引入多头矩阵值状态(matrix-valued states)来增加状态容量和表达能力。Finch在Eagle基础上增加了数据依赖的时间混合和衰减机制，使得模型能够根据输入内容动态调整信息传播。

## 1. 方法动机
a) **为什么提出**: RWKV-4的标量状态限制了信息容量；衰减参数w不依赖输入
b) **现有方法痛点**: 
   - v4的状态是向量值，容量有限
   - 时间衰减w是固定参数，无法根据内容自适应
   - 与Mamba等新方法相比缺乏选择性
c) **研究假设**: 矩阵值状态+输入依赖参数可以大幅提升表达能力

## 2. 方法设计
a) **RWKV-5 (Eagle)**:
   - 将隐状态从向量升级为矩阵：$S_t \in \mathbb{R}^{d_k \times d_v}$
   - 引入多头机制（类似Multi-Head Attention）
   - 状态更新: $S_t = \text{diag}(w) \cdot S_{t-1} + k_t v_t^T$（外积更新）
   - 输出: $o_t = r_t \cdot S_t$
   
b) **RWKV-6 (Finch)**:
   - 在Eagle基础上增加数据依赖:
   - Token shift变为数据依赖: $\mu_t = f(x_t)$
   - 时间衰减变为数据依赖: $w_t = g(x_t)$（类似Mamba的选择性Δ）
   - LoRA-style参数高效化

c) **公式解释**:
   - 矩阵状态: 容量从d增加到d_k × d_v
   - 外积更新: $k_t v_t^T$ 存储key-value关联
   - 数据依赖衰减: 可以根据内容决定何时遗忘

## 3. 与其他方法对比
a) **本质不同**: 矩阵值状态 + 数据依赖参数（与Mamba的选择性机制类似）
b) **创新点**: 
   - 从向量状态到矩阵状态的升级
   - 数据依赖的token shift和时间衰减
c) **适用场景**: 长序列语言建模、多语言任务
d) **对比表格**:

| 特性 | RWKV-4 | RWKV-5(Eagle) | RWKV-6(Finch) | Mamba |
|------|--------|--------------|--------------|-------|
| 状态形状 | 向量 | 矩阵 | 矩阵 | 向量 |
| 多头 | 否 | 是 | 是 | 否 |
| 数据依赖参数 | 否 | 否 | 是 | 是(Δ,B,C) |
| 训练并行 | 是 | 是 | 是 | 是 |

## 4. 实验表现
a) **验证方式**: 多语言语言建模、多种基准
b) **关键数据**: Eagle/Finch在多数任务上超过RWKV-4，竞争力与Mamba相当
c) **优势场景**: 多语言、长文本
d) **局限性**: 矩阵状态增加了状态大小

## 5. 学习与应用
a) **开源情况**: 完全开源，RWKV社区维护
b) **实现细节**: 支持多种规模
c) **迁移可能性**: 后续发展为RWKV-7 (Goose)

## 6. 总结
a) **一句话概括**: 通过矩阵值状态和数据依赖参数，显著提升RWKV的表达能力和选择性
b) **速记版pipeline**: Input → Data-dependent Token Shift → R,K,V → Matrix State Update(外积) → Output

**Token Mixer维度**: RNN-Like方案，矩阵值状态+外积更新，数据依赖衰减实现选择性
