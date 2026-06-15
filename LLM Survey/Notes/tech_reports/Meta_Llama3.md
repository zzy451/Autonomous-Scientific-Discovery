# Meta - Llama 3 架构分析

## 基本信息
- 论文标题：The Llama 3 Herd of Models
- 参数量：8B / 70B / 405B（三个尺寸，均为 Dense 模型）
- 层数：32 (8B) / 80 (70B) / 126 (405B)
- 隐藏维度：4,096 (8B) / 8,192 (70B) / 16,384 (405B)
- 注意力头数：32 (8B) / 64 (70B) / 128 (405B)
- KV 头数：8（所有尺寸均为 8，GQA）
- FFN 维度：14,336 (8B) / 28,672 (70B) / 53,248 (405B)
- 上下文长度：128K tokens（Llama 3.1 版本）
- 词表大小：128,000（基于 tiktoken 的分词器）
- 训练数据量：约 15.6T tokens
- 发布时间：2024 年 7 月（论文）/ 2024 年 4 月（Llama 3 初版 8B/70B）
- 论文链接：arXiv:2407.21783

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped-Query Attention (GQA) | 所有尺寸使用 8 个 KV 头；8B: 32Q/8KV, 70B: 64Q/8KV, 405B: 128Q/8KV；标准 Softmax Attention | 统一使用 8 个 KV 头（而非按模型大小调整），简化工程实现；GQA 有效减少 KV cache 大小 |
| Channel Mixer | SwiGLU FFN | FFN 维度为隐藏维度的约 3.5 倍（8B: 14,336/4,096≈3.5x, 405B: 53,248/16,384≈3.25x）；SwiGLU 引入门控机制 | 沿用 Llama 2 的 SwiGLU 设计，但调大了 FFN 比例 |
| Normalization | RMSNorm (Pre-Norm) | 在 Attention 和 FFN 之前应用 RMSNorm | 标准做法，继承自 Llama 1/2 |
| Position Encoding | RoPE (theta=500,000) | 旋转位置编码，基频设为 500,000（远高于原始 RoPE 的 10,000）；支持 128K 长上下文 | 大幅提升 RoPE 基频（500K vs 10K）以支持长上下文，无需额外位置插值 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm -> Attn -> Add -> Norm -> FFN -> Add | 标准 Pre-Norm Transformer 序列 | 标准做法 |

## 关键架构创新

1. **大规模 Scaling 验证**：405B 是当时最大的开源 Dense Transformer 模型，在 126 层 / 128 注意力头的规模上验证了标准架构的可扩展性。Meta 选择不使用 MoE，证明 Dense 架构在足够 scale 下仍具竞争力。

2. **高基频 RoPE (theta=500K)**：通过将 RoPE 基频从传统的 10K 提升至 500K，直接支持 128K 上下文长度，避免了复杂的位置插值方案（如 NTK-aware、YaRN 等）。

3. **超大规模训练数据**：15.6T tokens 的训练数据规模远超同期模型（如 Llama 2 的 2T tokens），展示了数据规模对模型性能的关键作用。

4. **统一 KV 头设计**：所有模型尺寸统一使用 8 个 KV 头，简化了跨尺寸的工程实现和优化。

5. **扩大词表**：词表从 Llama 2 的 32K 扩展到 128K，提升多语言和代码的编码效率。

## 与前代/同期模型对比

- **vs Llama 2**：层数从 80 增至 126（405B vs 70B）；词表 32K -> 128K；训练数据 2T -> 15.6T tokens；增加 GQA（Llama 2 70B 已使用）；RoPE 基频从 10K 提升至 500K。
- **vs DeepSeek-V3**：Dense vs MoE 架构的根本对比——Llama 3 405B 全参数激活（405B），DeepSeek-V3 仅激活 37B/671B；Llama 3 推理计算量远大但架构更简单。
- **vs Mixtral 8x7B**：Dense vs MoE，Llama 3 证明在足够 scale 下 Dense 模型可媲美 MoE。
- **vs GPT-4**：首个在多项基准上接近 GPT-4 水平的开源模型。

## 对本综述的启示
- Llama 3 是"标准 Dense Transformer 架构 + 极致 Scaling"的代表，架构本身几乎没有新设计，但通过 scale（数据量、参数量）实现了 SOTA 性能
- 在六维度上几乎全部采用"标准"选择：GQA + SwiGLU FFN + RMSNorm + RoPE + Pre-Norm Residual + Pre-Norm Sequence
- 唯一值得注意的架构选择是 RoPE 基频提升和统一 KV 头数，属于超参数调优而非结构创新
- 可作为综述中"标准架构基线"的参照模型
- 在六维度框架中定位：GQA (Token Mixer) + SwiGLU FFN (Channel Mixer) + RMSNorm (Norm) + RoPE-500K (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
