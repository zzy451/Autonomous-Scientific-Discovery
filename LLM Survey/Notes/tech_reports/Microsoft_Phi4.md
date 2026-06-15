# Microsoft - Phi-4 架构分析

## 基本信息
- 论文标题：Phi-4 Technical Report
- 参数量：14B（Dense）
- 层数：40 层
- 隐藏维度：5120
- 注意力头数：40 个 Query 头，10 个 KV 头（GQA，4:1 比例）
- 上下文长度：4096 tokens（预训练）→ 16K tokens（中期训练扩展）
- 词表大小：100,352（tiktoken tokenizer）
- 训练数据量：9.8T tokens
- 发布时间：2024 年 12 月
- 论文链接：arXiv:2412.08905

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped Query Attention (GQA) | 40 Q 头，10 KV 头（4:1 比例）；全注意力（无滑动窗口）；上下文 4K→16K | 从 Phi-3-medium 的滑动窗口回归全注意力 |
| Channel Mixer | SwiGLU FFN (Dense) | 标准 SwiGLU 激活函数 | 标准做法 |
| Normalization | RMSNorm (Pre-Norm) | 在注意力和 FFN 子层之前应用 RMSNorm | 标准做法 |
| Position Encoding | RoPE | 旋转位置编码；支持从 4K 扩展至 16K | 标准做法 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → FFN → Add | 标准 Pre-Norm 序列 | 标准做法 |

## 关键架构创新

注：Phi-4 的核心创新不在模型架构，而在数据策略。

1. **合成数据驱动训练**：Phi-4 的核心创新是数据质量策略。9.8T tokens 中大量使用合成数据，合成数据在训练全程发挥战略性作用，而非仅用于补充。

2. **数据质量优先于规模**：延续 Phi 系列"小模型 + 高质量数据"的理念，14B 参数模型通过精心策划的数据配方达到远超其规模的性能。

3. **从滑动窗口回归全注意力**：Phi-3-medium 使用 2K 滑动窗口，Phi-4 改为 4K 全注意力，说明全注意力在中等上下文长度下仍有优势。

4. **中期训练上下文扩展**：预训练使用 4K 上下文，中期训练阶段扩展至 16K，是渐进式上下文扩展的实践。

## 与前代/同期模型对比

- **vs Phi-3-medium**：架构高度相似，主要变化是从滑动窗口回归全注意力；训练数据策略升级；tokenizer 从 SentencePiece 改为 tiktoken。
- **vs Llama 3 8B**：Phi-4 参数更多（14B vs 8B），但训练数据策略不同（合成数据驱动 vs 大规模网络数据）。
- **vs Qwen2.5-14B**：相同参数规模，架构选择相似（GQA+SwiGLU+RMSNorm+RoPE），Phi-4 更强调合成数据。
- **vs Gemma 2 9B**：Phi-4 使用全注意力 vs Gemma 2 的交替局部/全局注意力；Phi-4 无 logit soft-capping。

## 对本综述的启示
- Phi-4 证明了"标准架构 + 极致数据质量"路线的有效性，架构本身无显著创新
- 从滑动窗口回归全注意力的决策值得在 Token Mixer 维度讨论
- 合成数据策略虽非架构创新，但对模型性能影响巨大，可作为综述的补充讨论
- 在六维度框架中定位：GQA (Token Mixer) + SwiGLU-Dense (Channel Mixer) + RMSNorm (Norm) + RoPE (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
