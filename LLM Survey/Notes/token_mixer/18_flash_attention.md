# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
**作者**: Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré (Stanford, University at Buffalo) | **年份**: 2022 | **arxiv**: 2205.14135

## 0. 摘要翻译
Transformer在处理长序列时速度慢且内存消耗大，因为自注意力的时间和内存复杂度与序列长度成二次关系。近似注意力方法试图通过牺牲模型质量来降低计算复杂度，但往往无法实现实际的加速。本文提出FlashAttention，一种IO感知的精确注意力算法，通过分块（tiling）技术减少GPU高带宽内存（HBM）和片上SRAM之间的内存读写次数。FlashAttention在不使用任何近似的情况下，比标准注意力快2-4倍，内存使用从$O(N^2)$降至$O(N)$。

## 1. 方法动机
a) **为什么提出**: GPU的计算速度远快于内存带宽。标准注意力实现需要多次在HBM和SRAM之间搬运数据（写入$N \times N$的注意力矩阵），成为实际瓶颈。
b) **现有痛点**: (1) 标准注意力需要将$N \times N$的注意力矩阵写入HBM，内存$O(N^2)$；(2) 近似注意力方法（Linformer、Performer等）虽然降低了FLOP但实际wall-clock时间未必更快，因为它们没有优化IO；(3) 长序列训练受限于内存。
c) **研究假设**: 通过重新组织注意力计算的顺序（tiling + recomputation），可以避免将$N \times N$注意力矩阵写入HBM，从而在保持精确计算的同时大幅减少IO和内存。

## 2. 方法设计
a) **Pipeline**: 将Q、K、V分块加载到SRAM，在SRAM中完成注意力计算，只将最终结果写回HBM。

b) **模块功能**:
- **分块计算 (Tiling)**:
  - 将Q分为$T_r$个块，K/V分为$T_c$个块
  - 外层循环遍历K/V块，内层循环遍历Q块
  - 每次只将一个Q块和一个K/V块加载到SRAM中计算
- **在线Softmax (Online Softmax)**:
  - 挑战：softmax需要全局归一化（需要所有score的最大值和求和）
  - 解决：使用在线softmax算法，维护running max和running sum
  - 每处理一个K/V块，更新当前的max和sum，并修正之前的部分结果
  - $m_{\text{new}} = \max(m_{\text{old}}, m_{\text{block}})$
  - $l_{\text{new}} = e^{m_{\text{old}} - m_{\text{new}}} l_{\text{old}} + e^{m_{\text{block}} - m_{\text{new}}} l_{\text{block}}$
- **反向传播重计算 (Recomputation)**:
  - 前向传播不存储$N \times N$注意力矩阵，只存储softmax的统计量（$m$和$l$）
  - 反向传播时从Q、K、V重新计算注意力矩阵的每个块
  - 用额外的计算换取$O(N)$的内存

c) **公式解释**:
- HBM IO复杂度: 标准注意力$O(Nd + N^2)$，FlashAttention $O(N^2d^2/M)$，其中$M$是SRAM大小
- 当$M = \Theta(Nd)$时（典型情况），IO减少为$O(Nd)$，即线性
- 计算量不变（仍是$O(N^2d)$ FLOPs），但实际更快因为IO减少

## 3. 与其他方法对比
| 方面 | FlashAttention | 标准Attention | Linformer | Performer |
|------|---------------|--------------|-----------|-----------|
| 精确性 | 精确 | 精确 | 近似 | 近似 |
| 内存 | $O(N)$ | $O(N^2)$ | $O(N)$ | $O(N)$ |
| FLOPs | $O(N^2d)$ | $O(N^2d)$ | $O(Nkd)$ | $O(Nmd)$ |
| 实际速度 | 最快 | 慢 | 中等 | 中等 |
| IO复杂度 | $O(N^2d^2/M)$ | $O(Nd + N^2)$ | 未优化 | 未优化 |

## 4. 实验表现
- **速度**: 比PyTorch标准注意力快2-4倍，比Megatron-LM注意力快约2倍
- **内存**: 内存使用减少5-20倍（不存储$N \times N$矩阵）
- **GPT-2训练**: 在OpenWebText上训练速度提升约3倍
- **长序列**: 支持序列长度从1K扩展到4K-16K，无OOM
- **BERT**: 在GLUE基准上达到新的SOTA（MLM训练更快收敛）
- **长文档分类**: 在长文档任务上比之前的高效注意力方法更快且更准确

## 5. 总结
a) **一句话概括**: FlashAttention通过IO感知的分块计算和在线softmax，在不做任何近似的情况下将注意力的内存从$O(N^2)$降至$O(N)$，实际速度提升2-4倍，成为现代Transformer训练的标准基础设施。
b) **速记pipeline**: Q,K,V(HBM) → 分块加载到SRAM → 块内计算QK^T → Online-Softmax → ×V → 累积结果写回HBM
