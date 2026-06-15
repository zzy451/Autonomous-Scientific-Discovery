# GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints
**作者**: Ainslie et al. (Google Research) | **年份**: 2023 | **arxiv**: 2305.13245

## 0. 摘要翻译
Multi-Query Attention (MQA) 通过共享 KV 头显著加速推理，但可能导致质量下降和训练不稳定。本文提出 **Grouped-Query Attention (GQA)**，一种介于 Multi-Head Attention (MHA) 和 Multi-Query Attention (MQA) 之间的注意力机制。GQA 将 Query 头分为若干组，每组共享一组 KV 头。同时提出一种 **uptrain** 方法：从已训练好的 MHA 模型出发，通过对 KV 头做均值池化初始化，以少量额外训练即可转换为 GQA 模型。实验表明 GQA 在接近 MQA 推理速度的同时，质量接近 MHA。

## 1. 方法动机
a) **为什么提出这个方法**：MQA 只有 1 组 KV head，虽推理快但质量损失明显。MHA 有 h 组 KV head，质量好但推理慢。需要一个可调节的中间方案。

b) **现有方法的痛点**：
- MQA (1 个 KV head) 质量下降明显，训练不稳定
- MHA (h 个 KV head) KV cache 过大，推理慢
- 想从 MHA 转 MQA 需要完全重新训练

c) **研究假设/直觉**：KV head 数量不必是 1 (MQA) 或 h (MHA) 的极端值，可以取一个中间值 g（如 8），在速度和质量之间取得最优平衡。同时，可以从已有 MHA 模型出发，通过均值池化 KV head 来快速适配。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 将 h 个 Query head 均匀分成 g 组（每组 h/g 个 Q head）
2. 为每组分配一个独立的 KV head
3. 组内的 Q head 共享同一组 KV
4. 其余计算与标准 MHA 相同

**Uptrain 方法**：
1. 从预训练好的 MHA checkpoint 出发
2. 将每组内的 KV head 权重取均值，作为该组共享 KV head 的初始化
3. 继续训练少量步数（原训练量的 5-10%）即可恢复质量

b) **核心模块功能**：
- **分组机制**：g 个 KV group，每个 group 对应 h/g 个 Q head。g=1 退化为 MQA，g=h 退化为 MHA
- **KV cache 大小**：g * d_k * L * 2（比 MHA 减少 h/g 倍，比 MQA 增加 g 倍）
- **Uptrain 初始化**：GroupAvg(KV heads) 初始化，加速收敛

c) **关键公式解释**：
- GQA 的 KV cache 大小 = g * d_k * L * 2
- MHA: g = h → cache = h * d_k * L * 2
- MQA: g = 1 → cache = 1 * d_k * L * 2
- GQA: 1 < g < h，如 g = 8 → 相比 32-head MHA 减少 4 倍

## 3. 与其他方法对比
- **与 MHA 的关系**：GQA 是 MHA 的特例推广（g=h 时退化为 MHA）
- **与 MQA 的关系**：GQA 是 MQA 的特例推广（g=1 时退化为 MQA）
- **与 MLA 的区别**：GQA 通过分组共享减少 KV head 数，MLA 通过低秩投影压缩 KV 维度，方法论不同
- **创新点**：
  1. 统一了 MHA 和 MQA 的框架
  2. 提出 uptrain 方法实现低成本模型转换
- **适用场景**：大规模 LLM 的推理优化。被 LLaMA-2、Mistral 等主流模型广泛采用

## 4. 实验表现
- **关键结果**：
  - GQA-8（8 个 KV group）的质量接近 MHA，仅有微小下降
  - 推理速度接近 MQA（相比 MHA 快 3-5 倍）
  - Uptrain 只需原训练量的 5% 即可从 MHA 转换为 GQA
  - 在 T5 XXL 模型上验证有效
- **优势场景**：高吞吐推理、大 batch 服务、长上下文推理
- **局限性**：
  - 分组数 g 需要根据模型规模和硬件特性调节
  - Uptrain 仍需额外训练成本（虽然只有 5-10%）
  - 本质上仍然是一种质量-速度的 trade-off

## 5. 总结
a) **一句话概括（≤20字）**：Q 头分组共享 KV，统一了 MHA 和 MQA。

b) **速记 pipeline**：
`h个Q头 → 分为g组 → 每组共享1个KV头 → 组内各Q与共享KV算Attn → Concat → Output`
