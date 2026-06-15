# MosaicML (Databricks) - MPT 架构分析

## 基本信息
- 论文标题：MPT-7B / MPT-30B（MosaicML 官方博客和 LLM Foundry 文档）
- 参数量：MPT-7B (6.7B) / MPT-30B
- 层数：MPT-7B：32 层
- 隐藏维度：MPT-7B：4096
- 注意力头数：MPT-7B：32
- 上下文长度：MPT-7B：2048 tokens（基础）/ 65K+ tokens（StoryWriter 变体）
- 词表大小：50,432
- 训练数据量：MPT-7B：1T tokens
- 发布时间：2023 年 5 月
- 代码：LLM Foundry (开源)

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Multi-Head Attention + FlashAttention | 标准 Multi-Head Attention；使用 FlashAttention 加速；可选 QK LayerNorm 增强稳定性 | QK LayerNorm 是早期的注意力稳定性技巧 |
| Channel Mixer | 标准 FFN (Dense) | 标准 FFN 层 | 标准做法 |
| Normalization | LayerNorm (Low Precision) | 低精度 LayerNorm；可选 QK LayerNorm | QK LayerNorm 是 QK-Norm 的早期实践 |
| Position Encoding | ALiBi (Attention with Linear Biases) | 不使用传统位置嵌入（无 RoPE/学习式 PE）；在注意力分数中直接添加线性偏置，距离越远偏置越大（负值）；天然支持序列长度外推 | ALiBi 是 RoPE 的主要竞争者：无需位置嵌入参数，天然支持超出训练长度的序列 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接；无 bias | 标准做法 |
| Module Sequence | Pre-Norm: Norm -> Attn -> Add -> Norm -> FFN -> Add | 标准 Pre-Norm 序列 | 标准做法 |

## 关键架构创新

1. **ALiBi (Attention with Linear Biases)**：核心架构选择。不同于 RoPE 或学习式位置编码，ALiBi 完全不使用位置嵌入参数，而是在注意力分数矩阵中直接添加与 token 距离成比例的线性偏置（负值）。这使得模型天然支持序列长度外推——MPT-7B-StoryWriter 在仅 2K 上下文训练后可外推至 65K+ tokens。

2. **QK LayerNorm**：可选的 Query-Key LayerNorm 增强训练稳定性，是后来 Gemma 3/Qwen3 采用的 QK-Norm 的早期实践。

3. **训练效率与可复现性**：使用 LION 优化器（内存效率高于 AdamW）、FSDP 并行、自动容错恢复，展示了高效且可复现的 LLM 训练方法论。

4. **无 Bias 设计**：所有层均不使用 bias 参数，简化架构并提升训练效率。

## 与前代/同期模型对比

- **vs Llama 1/2**：MPT 使用 ALiBi vs Llama 使用 RoPE，是位置编码方案的直接对比。ALiBi 天然支持长度外推，但 RoPE 在精度上更优且被更广泛采用。
- **vs Falcon 1**：两者都是早期开源 LLM 的竞争者，Falcon 同样采用 ALiBi + MHA 设计。
- **vs Mistral 7B**：Mistral 使用 RoPE + SWA，MPT 使用 ALiBi + 全局注意力，两种不同的长序列处理策略。
- **vs GPT-NeoX / Pythia**：同属早期开源 LLM 生态，MPT 强调训练效率和可部署性。

## 对本综述的启示
- ALiBi 是 Position Encoding 维度中 RoPE 的唯一实质性竞争者，代表了"无参数位置编码"的设计理念
- 尽管 RoPE 已成为绝对主流，ALiBi 的长度外推特性仍有理论价值，且其失败案例（为何未被广泛采用）值得在综述中讨论
- QK LayerNorm 是 QK-Norm 的历史先驱，展示了注意力内部归一化的早期探索
- MPT 虽非最新模型，但其 ALiBi 选择提供了位置编码设计空间的重要对照组
- 在六维度框架中定位：MHA+FlashAttn (Token Mixer) + Dense FFN (Channel Mixer) + LayerNorm+QK-LayerNorm (Norm) + ALiBi (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
