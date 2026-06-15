# Fast Transformer Decoding: One Write-Head is All You Need
**作者**: Noam Shazeer | **年份**: 2019 | **arxiv**: 1911.02150

## 0. 摘要翻译
增量式 Transformer 解码（自回归生成）的速度瓶颈之一在于每一步都需要加载整个 Key-Value 缓存。Multi-Head Attention (MHA) 中，每个注意力头都有独立的 Key 和 Value 投影，导致 KV 缓存的内存占用和带宽需求随 head 数线性增长。本文提出 **Multi-Query Attention (MQA)**：所有注意力头共享同一组 Key 和 Value 投影，仅 Query 保留多头结构。这一简单修改大幅减少了 KV 缓存大小和内存带宽需求，从而显著加速了增量解码，且模型质量仅有微小下降。

## 1. 方法动机
a) **为什么提出这个方法**：自回归解码的每一步都需要重新加载完整的 KV cache，这在标准 MHA 中 KV cache 大小 = num_heads * d_head * seq_len * 2（K+V），对 GPU 内存带宽造成巨大压力，成为推理速度的主要瓶颈。

b) **现有方法的痛点**：
- MHA 中每个 head 的 K, V 投影独立，KV cache 总量 = h * d_k * L（h 为 head 数）
- 在推理时，计算是 memory-bound 而非 compute-bound：大部分时间花在从 HBM 读取 KV cache
- 增大模型或增长序列时，KV cache 占用快速膨胀

c) **研究假设/直觉**：Key 和 Value 在不同 head 之间的差异远小于 Query 的差异。不同 head 可以"共享"一组 KV 而不显著损失质量，但能将 KV cache 缩小 h 倍。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 输入 token 投影为多个 Query head：Q_1, Q_2, ..., Q_h
2. 输入 token 仅投影为 **一组** Key 和 Value：K, V（共享给所有 head）
3. 每个 head 用自己的 Q_i 与共享的 K 计算注意力分数
4. 用共享的 V 加权求和
5. 各 head 输出拼接后经过输出投影

b) **核心模块功能**：
- **多头 Query**：保留标准 MHA 的 h 个独立 Query 投影，保证模型表达能力
- **单头 KV**：所有 head 共享一组 K, V 投影，KV cache 缩减为原来的 1/h
- **内存带宽节省**：推理时加载 KV cache 的数据量减少 h 倍，显著加速

c) **关键公式解释**：
- MHA：Q_i = x W_Q^i, K_i = x W_K^i, V_i = x W_V^i（每 head 独立 KV）
- MQA：Q_i = x W_Q^i, K = x W_K, V = x W_V（所有 head 共享一组 KV）
- KV cache 大小：MHA = h * d_k * L * 2 → MQA = d_k * L * 2（减少 h 倍）

## 3. 与其他方法对比
- **与标准 MHA 的本质区别**：MHA 每个 head 有独立 KV，MQA 所有 head 共享一组 KV
- **与后续 GQA 的关系**：GQA 是 MQA 和 MHA 的推广——将 head 分组，每组共享一组 KV。MQA 是 GQA 的极端情况（所有 head 一组）
- **与 MLA 的区别**：MLA 通过低秩压缩 KV 来减少缓存，方法论不同
- **创新点**：极简的改动（去掉 KV 的多头），获得巨大的推理加速
- **适用场景**：推理效率优先的生产部署场景，如在线服务、边缘设备

## 4. 实验表现
- **关键结果**：
  - 推理速度提升：encoder-decoder 模型中解码速度提升约 2-5 倍
  - 模型质量：在翻译任务上 BLEU 分数仅下降 0.1-0.3
  - KV cache 内存减少 h 倍（h 通常为 8-128）
- **优势场景**：大 batch 推理、长序列生成、内存受限的部署环境
- **局限性**：
  - 质量确实有微小下降，尤其在需要细粒度多角度关注的任务上
  - 训练时没有加速（训练通常是 compute-bound 而非 memory-bound）
  - 论文较早（2019），当时的实验规模相比现代标准较小

## 5. 总结
a) **一句话概括（≤20字）**：所有 head 共享一组 KV，KV 缓存缩减 h 倍。

b) **速记 pipeline**：
`Input → 多头Q + 单头K,V → 各head用自己Q与共享KV计算Attn → Concat → OutputProj`
