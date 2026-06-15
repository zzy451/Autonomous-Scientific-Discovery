# Functional Interpolation for Relative Positions Improves Long Context Transformers (FIRE)
**作者**: Shanda Li, Chong You, Guru Guruganesh, Joshua Ainslie, Santiago Ontanon, Manzil Zaheer, Sumit Sanghai, Yiming Yang, Sanjiv Kumar, Srinadh Bhojanapalli | **年份**: 2023 (ICLR 2024) | **来源**: Google Research / arXiv | **arXiv**: 2310.04418

## 0. 摘要翻译
本文提出 FIRE（Functional Interpolation for Relative Positions），一种使用可学习连续函数（通常为 MLP）将相对位置映射为注意力偏置的方法。FIRE 通过渐进式插值，将任意序列长度映射到固定的 $[0,1]$ 区间，使得训练在短序列上的模型可以自然地处理更长序列。理论上，FIRE 可以表示 T5 RPE、ALiBi、KERPLE 等多种相对位置编码方法，是一种统一框架。

## 1. 方法动机
a) **为什么提出**: 现有相对位置编码方法各有局限，且手工设计的偏置函数（线性、对数等）可能不是最优的。需要一个能自动学习最优偏置函数的框架。
b) **现有痛点**: 
   - ALiBi 的线性偏置过于简单
   - KERPLE 的核函数选择仍有经验性
   - T5 bias 的分桶策略是离散且固定的
   - 这些方法都采用预定义的函数形式，无法自适应学习
c) **研究假设**: 使用可学习的连续函数（MLP）来参数化相对位置到偏置的映射，结合渐进式插值保证长度泛化，可以统一并超越现有方法。

## 2. 方法设计
a) **pipeline**: 
   1. 计算相对距离 $r = |i - j|$
   2. 通过渐进式插值将 $r$ 映射到 $[0, 1]$: $\hat{r} = r / L$（$L$ 为当前序列长度）
   3. 将 $\hat{r}$ 输入可学习 MLP $\phi$，输出偏置值 $b = \phi(\hat{r})$
   4. 将偏置加入注意力分数: $a_{ij} = q_i^T k_j + b$

b) **模块功能**: 
   - 渐进式插值：保证任何长度的相对位置都映射到 $[0,1]$ 范围
   - MLP：自动学习最优的距离-偏置函数，不受预定义函数形式限制

c) **公式解释**:
   - 标准化: $\hat{r} = r / L$，当 $L$ 增大时，形成 $[0,1]$ 上的更细网格
   - 学习函数: $b_{ij} = \phi(\hat{r}_{ij})$，其中 $\phi$ 是小型 MLP
   - 统一性证明: ALiBi $\equiv \phi(\hat{r}) = -m \cdot L \cdot \hat{r}$，T5 $\equiv$ 分段常数 $\phi$
   - 长度泛化: 由于 $\hat{r} \in [0,1]$ 不随 $L$ 变化，MLP 始终在训练过的输入范围内工作

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 ALiBi/KERPLE：固定函数形式 vs 可学习 MLP
   - 与 T5 bias：离散分桶 vs 连续函数
   - 与 RoPE：注意力偏置 vs Q/K 旋转
   - FIRE 是一个统一框架，能表示上述所有方法
b) **创新点**: 
   - 渐进式插值保证了长度泛化（输入始终在 $[0,1]$）
   - MLP 自动学习最优偏置函数，无需人工设计
   - 理论上统一了 T5、ALiBi、KERPLE 等方法
c) **适用场景**: 需要强长度泛化能力的模型；作为通用相对位置编码框架。

## 4. 实验表现
a) **验证方式**: 在 C4 数据集上预训练，评估零样本和微调后的长度泛化性能。
b) **关键数据**: 
   - 在 2048 token 上训练，零样本外推至 8192 时困惑度优于 ALiBi 和 KERPLE
   - 微调后可扩展至 16384+ 并保持良好性能
   - 在多个下游任务上与 RoPE 可比或略优
c) **局限性**: 
   - MLP 增加了一定的计算开销
   - 渐进式插值在极端扩展下仍可能出现分辨率问题
   - 在 RoPE 主导的 LLM 生态中尚未被广泛采用

## 5. 总结
a) **一句话概括**: FIRE 使用可学习 MLP 自动学习相对位置到注意力偏置的映射函数，通过渐进式插值保证长度泛化，统一了 ALiBi、T5 bias、KERPLE 等多种方法。
b) **速记 pipeline**: Relative Distance $r$ → Normalize to $[0,1]$ via $r/L$ → Learnable MLP $\phi$ → Attention Bias $b_{ij}$ → Add to $QK^T$ → Softmax
