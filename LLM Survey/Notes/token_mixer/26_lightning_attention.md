# Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths in Large Language Models
**作者**: Zhen Qin, Weigao Sun, Dong Li, Xuyang Shen, Weixuan Sun, Yiran Zhong (MiniMax, ANU) | **年份**: 2024 | **arxiv**: 2401.04658

## 0. 摘要翻译
线性注意力在理论上具有线性复杂度，但在因果（causal）设置下，由于累积求和（cumsum）操作的开销，实际速度并未达到理论预期。本文提出Lightning Attention-2，采用分治策略将注意力计算分为块内（intra-block）和块间（inter-block）两部分：块内使用传统注意力计算，块间使用线性注意力的核技巧。该算法在Triton中实现，IO感知且硬件友好，使线性注意力在训练和推理中均能实现恒定速度，不受序列长度影响。

## 1. 方法动机
a) **为什么提出**: 线性注意力的因果版本需要cumsum操作，这在GPU上是顺序的，导致实际速度远低于理论预期。
b) **现有痛点**: (1) 因果线性注意力的cumsum无法高效并行化；(2) 现有实现（如Lightning Attention-1）仍有IO瓶颈；(3) 线性注意力在实际wall-clock时间上并不比FlashAttention快多少。
c) **研究假设**: 通过将计算分为块内（可用标准注意力的tiling技巧）和块间（可用线性注意力的累积状态），可以同时利用两种范式的优势。

## 2. 方法设计
a) **Pipeline**: 将序列分块，块内用常规注意力计算（精确），块间用线性注意力的状态传递（高效）。

b) **模块功能**:
- **块内计算 (Intra-block)**:
  - 对于块内的token对$(i,j)$（$i,j$在同一块内），使用标准的注意力计算
  - $O_{\text{intra}} = \text{causal\_mask}(\phi(Q_b)\phi(K_b)^T) V_b$
  - 可以用FlashAttention式的tiling在SRAM中高效计算
  
- **块间计算 (Inter-block)**:
  - 维护累积状态$S_b = \sum_{b'<b} \phi(K_{b'})^T V_{b'}$
  - 块间输出: $O_{\text{inter}} = \phi(Q_b) S_b$
  - 状态更新: $S_{b+1} = S_b + \phi(K_b)^T V_b$
  - 这是线性注意力的标准形式，无需cumsum

- **合并**: $O_b = O_{\text{intra}} + O_{\text{inter}}$

- **Triton实现**:
  - 前向和反向传播均在Triton中实现
  - IO感知: 最小化HBM和SRAM之间的数据搬运
  - 支持任意线性注意力核$\phi$

c) **公式解释**:
- 分治的关键: 因果掩码只在块内需要处理（块间天然满足因果性）
- 块内: $O(C^2)$计算，$C$是块大小
- 块间: $O(C \cdot d_\phi)$计算，$d_\phi$是特征维度
- 总复杂度: $O(L \cdot (C + d_\phi))$，当$C$和$d_\phi$为常数时为$O(L)$

## 3. 与其他方法对比
| 方面 | Lightning Attn-2 | FlashAttention-2 | 朴素线性注意力 | Lightning Attn-1 |
|------|-----------------|-----------------|--------------|-----------------|
| 理论复杂度 | $O(L)$ | $O(L^2)$ | $O(L)$ | $O(L)$ |
| 实际速度 | 恒定（不随L变化）| 随L二次增长 | 随L线性但慢 | 随L线性 |
| 因果支持 | 高效 | 高效 | cumsum瓶颈 | 中等 |
| 实现 | Triton (IO-aware) | CUDA | PyTorch | CUDA |
| 精确性 | 取决于核$\phi$ | 精确softmax | 取决于核$\phi$ | 取决于核$\phi$ |

## 4. 实验表现
- **训练速度**: 在长序列上（8K-32K+）比FlashAttention-2快2-4倍
- **恒定速度**: 序列长度从1K增加到32K，训练速度几乎不变
- **内存**: 恒定内存消耗，不随序列长度增加
- **反向传播**: 反向传播同样高效，支持端到端训练
- **MiniMax部署**: 作为MiniMax-01模型的核心注意力实现，支持1M token训练和4M token推理
- **与FlashAttention对比**: 短序列上速度相当，长序列上显著更快

## 5. 总结
a) **一句话概括**: Lightning Attention-2通过分治策略将线性注意力分为块内（标准注意力tiling）和块间（线性状态传递），配合IO感知的Triton实现，首次让线性注意力在实际中达到恒定训练/推理速度，已在MiniMax-01中大规模部署。
b) **速记pipeline**: 序列分块 → [块内: causal φ(Q)φ(K)ᵀV | 块间: φ(Q)·S_cumulative] → 合并 → 状态传递到下一块
