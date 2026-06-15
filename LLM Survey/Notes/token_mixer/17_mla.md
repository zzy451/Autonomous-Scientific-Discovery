# DeepSeek-V2: Multi-Head Latent Attention (MLA)
**作者**: DeepSeek-AI (Aixin Liu, Bei Feng, Bin Wang, Bingxuan Wang, Bo Liu, Chenggang Zhao, et al.) | **年份**: 2024 | **arxiv**: 2405.04434

## 0. 摘要翻译
DeepSeek-V2是一个强大、经济且高效的混合专家（MoE）语言模型。在注意力机制方面，提出了多头潜注意力（Multi-Head Latent Attention, MLA），通过低秩联合压缩键值对来显著减少推理时的KV cache，同时保持与标准MHA相当甚至更优的性能。MLA将KV cache压缩到一个低维潜向量中，推理时从潜向量恢复KV，实现了比GQA和MQA更好的质量-效率权衡。

## 1. 方法动机
a) **为什么提出**: GQA/MQA通过减少KV头数来压缩KV cache，但这种方式直接丢弃了信息（多个头共享同一KV）。需要一种更优雅的压缩方式。
b) **现有痛点**: (1) MQA/GQA的KV共享是一种"有损压缩"，质量损失不可忽略；(2) 随着模型规模增大，KV cache仍然是推理的主要内存瓶颈；(3) 需要在极低KV cache开销下保持MHA级别的表达能力。
c) **研究假设**: 通过将KV联合压缩到低维潜空间（而非简单共享），可以用更少的cache存储更多信息，实现更好的质量-效率权衡。

## 2. 方法设计
a) **Pipeline**: 将KV的生成过程分为"压缩"和"恢复"两步：训练时先压缩到潜向量再恢复；推理时只缓存潜向量。

b) **模块功能**:
- **KV联合压缩**:
  - 压缩: $c_t^{KV} = W^{DKV} h_t$，将$d_{model}$维的隐状态压缩到$d_c$维潜向量（$d_c \ll d_{model}$）
  - 恢复K: $k_t^{(i)} = W_i^{UK} c_t^{KV}$（每个头从潜向量恢复自己的key）
  - 恢复V: $v_t^{(i)} = W_i^{UV} c_t^{KV}$（每个头从潜向量恢复自己的value）
  - KV cache只需存储$c_t^{KV}$（$d_c$维），而非所有头的KV
- **Query压缩（可选）**:
  - $c_t^Q = W^{DQ} h_t$，将query也压缩到低维再恢复
  - $q_t^{(i)} = W_i^{UQ} c_t^Q$
- **解耦的RoPE**: 
  - 由于KV被压缩，无法直接对$c_t^{KV}$应用RoPE（位置编码会与压缩矩阵耦合）
  - 解决方案：为RoPE单独分配额外的key维度$d_R$，不经过压缩
  - $k_t = [k_t^{content}; k_t^{rope}]$，$k_t^{rope} = \text{RoPE}(W^{KR} h_t)$
  - KV cache = $c_t^{KV}$（$d_c$维）+ $k_t^{rope}$（$d_R$维）

c) **公式解释**:
- 核心思想: $[K; V] = W^{up} \cdot c^{KV}$，$c^{KV} = W^{down} \cdot h$
- KV cache大小: $d_c + d_R$ per token（如$d_c=512, d_R=64$），远小于MHA的$2 \times h \times d_k$（如$2 \times 128 \times 128 = 32768$）
- 吸收技巧: 推理时可以将$W^{UQ}$和$W^{UK}$合并为$W^{UQ \cdot UK}$，避免显式恢复K，直接用$q$和$c^{KV}$计算注意力

## 3. 与其他方法对比
| 方面 | MLA | MHA | GQA-8 | MQA |
|------|-----|-----|-------|-----|
| KV cache/token | $d_c + d_R$ ≈ 576 | $2hd_k$ ≈ 32768 | $2 \times 8 \times d_k$ ≈ 2048 | $2d_k$ ≈ 256 |
| 质量 | ≈ MHA | 基准 | 略低于MHA | 低于GQA |
| 信息保留 | 低秩压缩（保留主成分）| 完整 | 共享（丢弃）| 共享（丢弃）|
| 每头独立性 | 从潜向量恢复独立KV | 完全独立 | 组内共享 | 全部共享 |

## 4. 实验表现
- **DeepSeek-V2 (236B MoE, 21B active)**: 在多个基准上匹配或超越Llama-3-70B
- **KV cache**: 比MHA减少约93.3%，比GQA-8仍减少约70%
- **推理吞吐量**: 比DeepSeek-67B（MHA）提升5.76倍
- **训练效率**: 训练成本仅为DeepSeek-67B的42.5%
- **质量**: 在MMLU、HumanEval、GSM8K等基准上全面超越前代模型
- **后续采用**: DeepSeek-V3、DeepSeek-R1均沿用MLA架构

## 5. 总结
a) **一句话概括**: MLA通过将KV联合压缩到低维潜向量并在计算时恢复，以极小的KV cache（$d_c + d_R$维/token）实现了MHA级别的注意力表达能力，是目前KV cache压缩的最优方案。
b) **速记pipeline**: h → W_down → c_KV(低维潜向量, 缓存) → W_up恢复K,V → Q·K^T/√d → softmax → ·V → Output
