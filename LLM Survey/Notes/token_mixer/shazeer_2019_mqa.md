# Shazeer 2019 - Fast Transformer Decoding: One Write-Head is All You Need (MQA)

**论文信息**
- 标题: Fast Transformer Decoding: One Write-Head is All You Need
- 作者: Noam Shazeer
- 年份: 2019
- arXiv: 1911.02150

## 0. 摘要翻译
多头注意力（Multi-Head Attention）在增量推理（逐token解码）时的主要瓶颈是内存带宽——需要反复从内存加载所有注意力头的Key和Value张量。我们提出Multi-Query Attention：所有注意力头共享一组Key和Value，仅Query保持多头。这大幅降低了KV缓存大小和内存带宽需求，显著加速了推理。

## 1. 方法动机
a) **为什么提出**: Transformer自回归推理时，每步都需加载完整的KV cache，内存带宽成为瓶颈
b) **现有方法痛点**: MHA中每个head有独立的K、V投影，KV cache大小 = 2 × n_heads × d_head × seq_len，随head数线性增长
c) **研究假设**: Key和Value可以跨所有头共享，而不会显著损害模型质量

## 2. 方法设计
a) **方法流程**: 
   - 保持多个Query头（h个）
   - 仅使用1组共享的Key和Value投影
   - 每个Query头与同一组K、V计算注意力
   
b) **模块功能**:
   - Query投影: $Q_i = XW_i^Q$（每个head独立）
   - Key/Value投影: $K = XW^K$, $V = XW^V$（所有head共享）
   - 注意力计算不变: $\text{Attention}(Q_i, K, V) = \text{softmax}(\frac{Q_i K^T}{\sqrt{d_k}})V$
   
c) **公式解释**:
   - KV cache从 $2 \times h \times d_k \times N$ 降低到 $2 \times d_k \times N$
   - 内存带宽减少约 h 倍（h通常为32-128）

## 3. 与其他方法对比
a) **本质不同**: 极端的KV参数共享——所有头共享一组K、V
b) **创新点**: 用极简方式解决推理内存带宽问题，无需修改注意力计算逻辑
c) **适用场景**: 推理密集型场景，尤其是大batch推理
d) **对比表格**:

| 特性 | MHA | MQA | GQA |
|------|-----|-----|-----|
| KV头数 | h | 1 | g (1<g<h) |
| KV cache大小 | 2hd | 2d | 2gd |
| 模型质量 | 最高 | 略降 | 接近MHA |
| 推理速度 | 慢 | 最快 | 快 |

## 4. 实验表现
a) **验证方式**: 翻译任务（WMT EN-DE）
b) **关键数据**: 推理加速显著，质量下降微小（~0.1-0.3 BLEU）
c) **优势场景**: 大batch自回归推理
d) **局限性**: 质量有轻微下降；训练不稳定性

## 5. 学习与应用
a) **开源情况**: 概念简单，各框架均有实现
b) **实现细节**: 仅修改KV投影维度，几乎无额外实现成本
c) **迁移可能性**: 已被PaLM、StarCoder等大模型采用

## 6. 总结
a) **一句话概括**: 通过让所有注意力头共享一组KV投影，将KV cache减少h倍，大幅加速推理
b) **速记版pipeline**: Input → Q_multi_head + K_shared + V_shared → Attention → Output

**Token Mixer维度**: KV Cache优化方案，通过极端参数共享减少推理内存带宽需求
