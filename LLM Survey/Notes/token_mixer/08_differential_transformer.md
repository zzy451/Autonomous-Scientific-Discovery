# Differential Transformer
**作者**: Tianzhu Ye, Li Dong, Yuqing Xia, Yutao Sun, Yi Zhu, Gao Huang, Furu Wei (Microsoft Research) | **年份**: 2024 | **arxiv**: 2410.05258

## 0. 摘要翻译
Transformer倾向于将注意力分散到不相关的上下文上，即产生注意力噪声。本文提出Differential Transformer（DIFF Transformer），其关键创新是差分注意力机制——计算两组softmax注意力图之间的差值作为最终注意力分数。这类似于电子学中的差分放大器（抵消噪声、放大信号）。差分注意力消除了注意力噪声，促使模型关注关键信息。实验表明DIFF Transformer在语言建模、长上下文建模、关键信息检索、减轻幻觉、上下文学习和激活量化等方面优于标准Transformer。

## 1. 方法动机
a) **为什么提出**: 标准softmax注意力不可避免地将一部分注意力权重分配给不相关的上下文token（"注意力噪声"或"注意力汇"现象），浪费了模型容量。
b) **现有痛点**: (1) 注意力噪声导致模型关注无关信息；(2) 在信息检索任务中容易被干扰信息误导；(3) 在长上下文中注意力分散更严重，影响关键信息提取。
c) **研究假设**: 通过计算两组注意力的差值，可以抵消共模噪声（两组中共有的注意力噪声），保留差分信号（真正重要的注意力），类似差分信号处理。

## 2. 方法设计
a) **Pipeline**: 将每个注意力头拆分为两个子头，分别计算softmax注意力，然后相减得到差分注意力。

b) **模块功能**:
- **差分注意力**: 每个头包含两组Q,K投影：$(Q_1, K_1)$和$(Q_2, K_2)$，共享V投影。差分注意力：$\text{DiffAttn}(X) = (\text{softmax}(Q_1K_1^T/\sqrt{d}) - \lambda \cdot \text{softmax}(Q_2K_2^T/\sqrt{d}))V$
- **可学习的$\lambda$**: $\lambda = \exp(\lambda_{q1} \cdot \lambda_{k1}) - \exp(\lambda_{q2} \cdot \lambda_{k2}) + \lambda_{\text{init}}$，每个头有自己的$\lambda$参数，$\lambda_{\text{init}}$随层深度递减（浅层接近1，深层接近0）。
- **参数量保持**: 虽然Q,K拆分为两组，但$d_{head}$减半，总参数量与标准Multi-Head Attention相同。即每个"差分头"的维度是标准头的一半。
- **归一化**: 使用GroupNorm对差分注意力输出进行归一化：$\text{head}_i = \text{GroupNorm}(\text{DiffAttn}_i(X))$，稳定训练。

c) **公式解释**:
- 核心思想: $A_1 - \lambda A_2$，$A_1$和$A_2$共享相同的噪声模式，差值抵消噪声
- 每层6个投影矩阵: $W_{Q1}, W_{K1}, W_{Q2}, W_{K2}, W_V, W_O$
- 与标准MHA的FLOPs和参数量几乎相同

## 3. 与其他方法对比
| 方面 | DIFF Transformer | Transformer | Sigma (Sigmoid Attn) |
|------|-----------------|-------------|---------------------|
| 注意力计算 | softmax差分 | softmax | sigmoid |
| 注意力噪声 | 显式抵消 | 无处理 | 隐式减少 |
| 参数量 | 相同 | 基准 | 相同 |
| 幻觉问题 | 显著改善 | 基准 | - |
| 上下文学习 | 更稳健 | 基准 | - |

## 4. 实验表现
- **语言建模**: 在相同参数量下，DIFF Transformer的PPL显著低于标准Transformer（3B模型约提升0.5-1个PPL点）
- **长上下文**: 在Needle-in-a-Haystack测试中几乎完美（>99%准确率），标准Transformer约95%
- **幻觉缓解**: 在摘要任务（XSum、CNN/DM）上幻觉率显著降低
- **上下文学习 (ICL)**: 在many-shot ICL中优势明显，注意力更集中于相关示例
- **激活量化**: 由于注意力更稀疏、分布更集中，对量化更友好

## 5. 总结
a) **一句话概括**: Differential Transformer通过计算两组softmax注意力的差值来抵消注意力噪声，以几乎零额外成本显著提升模型在信息检索、长上下文和抗幻觉等方面的表现。
b) **速记pipeline**: X → (Q1K1ᵀ → softmax) - λ·(Q2K2ᵀ → softmax) → ·V → GroupNorm → Output
