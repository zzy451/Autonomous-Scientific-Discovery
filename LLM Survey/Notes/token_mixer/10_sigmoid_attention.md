# Scaling Sigmoid Dot-Product Attention for Large Language Models
**作者**: Jason Ramapuram, Federico Danieli, Eeshan Dhekane, Floris Weers, Dan Busbridge, Russ Webb (Apple) | **年份**: 2024 | **arxiv**: 2409.04431

## 0. 摘要翻译
注意力机制是现代语言模型的核心，标准实现使用softmax函数进行归一化。本文研究了用sigmoid函数替代softmax的可行性，提出了一种简单有效的sigmoid注意力替代方案。通过引入适当的缩放因子和偏置项，sigmoid注意力可以匹配甚至超越softmax注意力在语言建模任务上的表现。该方法还具有一些理论和实践优势，包括更好的并行性和对FlashAttention的兼容性。

## 1. 方法动机
a) **为什么提出**: softmax注意力的归一化性质（所有权重之和为1）迫使模型将注意力视为"零和游戏"——关注一个token必然减少对其他token的关注。sigmoid没有这种约束。
b) **现有痛点**: (1) softmax的归一化约束限制了注意力的表达能力；(2) softmax需要全局归一化（需要所有score才能计算），不利于某些并行化场景；(3) 在长序列中softmax倾向于"稀释"注意力。
c) **研究假设**: 通过适当的缩放和偏置，sigmoid可以作为softmax的替代，获得更灵活的注意力分配——允许同时高注意力多个token或低注意力所有token。

## 2. 方法设计
a) **Pipeline**: 将标准Transformer中的$\text{softmax}(QK^T/\sqrt{d})$替换为$\sigma(QK^T/\sqrt{d} + b)$，其中$\sigma$是sigmoid函数。

b) **模块功能**:
- **Sigmoid注意力**: $\text{Attn}(Q,K,V) = \sigma(QK^T/\sqrt{d_k} + b) \cdot V$
- **缩放因子**: 由于sigmoid不像softmax那样自动归一化，需要额外的缩放。使用$1/n$（序列长度的倒数）作为缩放因子：$\text{Attn} = \frac{1}{n}\sigma(QK^T/\sqrt{d_k} + b) V$
- **偏置项$b$**: 一个可学习的标量偏置，初始化为负值（如$b = -\log(n)$），使sigmoid的默认输出接近0，模拟softmax的稀疏性。
- **与FlashAttention的兼容**: sigmoid注意力可以无需修改直接使用FlashAttention的tiling策略，因为sigmoid是逐元素操作，不需要全局归一化。

c) **公式解释**:
- softmax: $a_{ij} = \frac{\exp(q_i k_j^T / \sqrt{d})}{\sum_l \exp(q_i k_l^T / \sqrt{d})}$（归一化到和为1）
- sigmoid: $a_{ij} = \sigma(q_i k_j^T / \sqrt{d} + b)$（每个权重独立在[0,1]之间）
- 关键区别: sigmoid允许"全关注"或"全不关注"，softmax则强制分配总量为1的注意力

## 3. 与其他方法对比
| 方面 | Sigmoid Attention | Softmax Attention | DIFF Transformer |
|------|------------------|-------------------|-----------------|
| 归一化 | 逐元素sigmoid | 全局softmax | 差分softmax |
| 注意力约束 | 无总量约束 | 和为1 | 可正可负 |
| 并行友好度 | 更好（无全局依赖）| 需全局归一化 | 类似softmax |
| FlashAttn兼容 | 原生兼容 | 兼容 | 需适配 |
| 计算成本 | 略低 | 基准 | 约相同 |

## 4. 实验表现
- **语言建模**: 在多种模型规模（125M到1.3B参数）上，sigmoid注意力的PPL与softmax注意力相当或略优
- **下游任务**: 在GLUE等基准上性能一致
- **训练稳定性**: 使用适当的缩放和偏置初始化后，训练稳定性与softmax相当
- **FlashAttention加速**: 可直接利用现有的FlashAttention实现获得加速
- **长序列**: 在长序列上sigmoid注意力可能具有优势，因为不受softmax稀释效应影响

## 5. 总结
a) **一句话概括**: 通过引入适当的$1/n$缩放和负偏置初始化，sigmoid可以替代softmax作为注意力归一化函数，提供更灵活的注意力分配（无总量约束）且与FlashAttention原生兼容。
b) **速记pipeline**: Q,K,V → QKᵀ/√d + bias → sigmoid → ×(1/n) → ·V → Output
