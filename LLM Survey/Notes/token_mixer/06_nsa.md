# NSA: Native Sparse Attention
**作者**: Jingyang Yuan, Huazuo Gao, Damai Dai, Junxiong Wang, Dongqi Sun, Liang Zhao, Zhengyan Zhang, Maosong Sun, Jie Tang (DeepSeek-AI) | **年份**: 2025 | **arxiv**: 2502.11089

## 0. 摘要翻译
长上下文建模对大语言模型至关重要，但标准全注意力的二次复杂度带来了显著的计算挑战。本文提出NSA（Native Sparse Attention），一种硬件对齐且可原生训练的稀疏注意力机制。NSA通过动态层次化稀疏策略整合三种注意力路径：(1) 粗粒度token压缩用于全局上下文感知；(2) 选择性保留的细粒度token用于捕获关键细节；(3) 滑动窗口用于局部上下文建模。通过算术强度平衡的算法设计和专门的内核实现，NSA在预训练阶段就可端到端训练，使模型能够学习最优的稀疏模式。

## 1. 方法动机
a) **为什么提出**: 大多数稀疏注意力方法是在推理阶段事后应用的（post-hoc），即模型仍以全注意力训练，推理时才用稀疏近似。这导致训练与推理不一致，性能下降。
b) **现有痛点**: (1) 全注意力在长序列上（如64K+）计算成本极高；(2) 事后稀疏方法的训练-推理不匹配问题；(3) 现有稀疏注意力方法在硬件利用率上不理想（如内存访问模式不规则）。
c) **研究假设**: 如果稀疏注意力从预训练阶段就参与，模型可以学习更好的稀疏模式，同时通过硬件友好的设计实现实际加速。

## 2. 方法设计
a) **Pipeline**: 每个注意力头并行执行三条路径，然后通过门控机制融合。

b) **模块功能**:
- **压缩注意力 (Compressed Attention)**: 将KV按时间块（block）压缩为粗粒度表示。对每个block用可学习的线性变换将多个token压缩为一个，然后在压缩后的token上做全局注意力。提供全局上下文概览。
- **选择注意力 (Selected Attention)**: 基于压缩注意力的得分，选择注意力权重最高的top-k个block，然后在这些block内的原始细粒度token上计算精确注意力。保留关键细节。
- **滑动窗口注意力 (Sliding Window)**: 保留最近$w$个token的局部注意力，捕获短程依赖。
- **门控融合 (Gating)**: 三条路径的输出通过可学习的标量门控加权融合：$o = g_1 \cdot o_{\text{compress}} + g_2 \cdot o_{\text{select}} + g_3 \cdot o_{\text{window}}$

c) **公式解释**:
- 压缩: $\tilde{K}_j = \text{Linear}([K_{(j-1)B+1}, ..., K_{jB}])$, 将B个token压缩为1个
- 选择: $\mathcal{S} = \text{top-k}(\text{score}(Q, \tilde{K}))$, 选出重要的block
- 总复杂度: $O(n \cdot (n/B + k \cdot B + w))$，远小于$O(n^2)$

## 3. 与其他方法对比
| 方面 | NSA | Full Attention | Longformer | FlashAttention |
|------|-----|---------------|------------|----------------|
| 复杂度 | 亚二次 | $O(n^2)$ | $O(n \cdot w)$ | $O(n^2)$（速度优化）|
| 训练方式 | 端到端原生 | 标准 | 标准 | 标准 |
| 动态稀疏 | 是（数据依赖） | 否 | 否（固定模式）| 否 |
| 硬件优化 | Triton内核 | cuBLAS | TVM | CUDA内核 |

## 4. 实验表现
- **预训练**: 在通用基准上保持或超越全注意力模型的性能
- **长上下文任务**: 在RULER、Needle-in-a-Haystack等长文本评测上表现优异
- **推理加速**: 解码阶段在64K上下文上约6-9倍加速
- **训练加速**: 前向和反向传播均有显著加速
- **推理能力**: 在数学推理和编程任务上不输全注意力baseline

## 5. 总结
a) **一句话概括**: NSA通过压缩+选择+滑动窗口三路径动态稀疏注意力，实现硬件对齐且可端到端预训练的高效注意力，在保持质量的同时大幅降低长序列计算成本。
b) **速记pipeline**: Q,K,V → [Compress-Attn(全局) ‖ Select-Attn(top-k blocks) ‖ Window-Attn(局部)] → Gate融合 → Output
