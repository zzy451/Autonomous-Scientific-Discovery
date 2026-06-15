# Google - Gemma 3 架构分析

## 基本信息
- 论文标题：Gemma 3 Technical Report
- 参数量：1B / 4B / 12B / 27B（Dense 模型系列）
- 旗舰模型 Gemma 3 27B 配置：
  - 层数：62 层
  - 隐藏维度：5,376
  - FFN 中间维度：21,504（约 4x 隐藏维度）
  - 注意力头数：32（Query）/ 16（KV），GQA 比例 2:1
- 上下文长度：128K tokens（4B/12B/27B）；32K tokens（1B）
- 词表大小：262,144（SentencePiece 分词器，与 Gemini 共享）
- 训练数据量：14T tokens（27B 模型）
- 发布时间：2025 年 3 月 10 日
- 论文链接：arXiv:2503.19786

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA + 交替 Local/Global 注意力 + QK-Norm | 5 层 Local (Sliding Window) + 1 层 Global 的交替模式（5:1）；Local 窗口大小 1024 tokens；Global 层存储完整 128K KV cache；GQA: 32Q/16KV (2:1)；QK-Norm 替代 Gemma 2 的 soft-capping | 交替 Local/Global 模式大幅降低 KV cache 内存（仅 1/6 层存储全局 KV）；QK-Norm 比 soft-capping 更高效 |
| Channel Mixer | SwiGLU FFN (Dense) | FFN 中间维度 21,504，约为隐藏维度的 4 倍；SwiGLU 激活函数 | 标准 Dense FFN，无 MoE |
| Normalization | RMSNorm (Pre-Norm) + QK-Norm | 层级 RMSNorm 用于 Pre-Norm；额外的 QK-Norm 应用于注意力的 Q 和 K 矩阵 | QK-Norm 是 Normalization 的新趋势，替代 Gemma 2 的 logit soft-capping |
| Position Encoding | RoPE (双基频设计) | Global 注意力层：RoPE 基频 1,000,000 (1M)；Local 注意力层：RoPE 基频 10,000 (10K)；针对不同注意力类型使用不同基频 | 首创双基频 RoPE：Global 层高基频支持长距离依赖，Local 层低基频保持局部精度 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm + 5:1 Local/Global 交替 | 重复模式：5 层 (Norm -> SlidingWindowAttn -> Add -> Norm -> FFN -> Add) + 1 层 (Norm -> GlobalAttn -> Add -> Norm -> FFN -> Add) | 非均匀层间模式，与 MiniMax 的 7:1 类似但方向不同（Local/Global vs Linear/Softmax） |

## 关键架构创新

1. **交替 Local/Global 注意力（5:1 模式）**：核心架构创新。5 层 Sliding Window Attention（窗口 1024 tokens）后接 1 层 Global Attention。只有 Global 层（占 1/6）需要存储完整 128K 上下文的 KV cache，其余 5/6 的层仅存储 1024 tokens 的 KV cache。这使得 128K 上下文在消费级硬件上成为可能。

2. **双基频 RoPE**：不同注意力类型使用不同 RoPE 基频——Global 层 1M（支持长距离），Local 层 10K（保持局部精度）。这是对 RoPE 使用方式的精细化设计。

3. **QK-Norm 替代 Soft-capping**：Gemma 2 使用 logit soft-capping 来稳定注意力，Gemma 3 改用 QK-Norm（直接对 Q 和 K 矩阵归一化），更简洁高效，且与 FlashAttention 等加速框架兼容性更好。

4. **多模态集成**：
   - 冻结的 SigLIP 视觉编码器
   - 图像压缩为固定 256 个 soft tokens
   - Pan & Scan (P&S) 方法：将不同宽高比图像拆分为多个裁剪区域，保留细节信息

5. **超大词表**：262K 词表（是 Llama 3 的 2 倍、DeepSeek-V3 的 2 倍），继承自 Gemini 分词器，对多语言支持更优。

## 与前代/同期模型对比

- **vs Gemma 2**：保持 Dense 架构不变；soft-capping -> QK-Norm；新增 Local/Global 交替注意力支持 128K 上下文（Gemma 2 为 8K）；新增多模态支持。
- **vs Llama 3**：均为 Dense 架构，但 Gemma 3 引入 Local/Global 交替注意力降低 KV cache 开销；Gemma 3 27B 在参数量远小于 Llama 3 405B 的情况下支持相同的 128K 上下文。
- **vs MiniMax-01**：均采用非均匀层间模式，但策略不同——Gemma 3 交替 Local/Global (5:1)，MiniMax 交替 Linear/Softmax (7:1)；Gemma 3 保持 Dense，MiniMax 使用 MoE。
- **vs Qwen3**：均采用 QK-Norm；Gemma 3 保持 Dense 而 Qwen3 旗舰走 MoE；Gemma 3 通过 Local/Global 交替解决长上下文问题。

## 对本综述的启示
- Gemma 3 是 Token Mixer 维度"异构层设计"的另一种实践：通过交替 Local/Global 注意力而非混合不同注意力机制
- 双基频 RoPE 展示了 Position Encoding 可以按层进行差异化配置
- QK-Norm 的采用（与 Qwen3 一致）标志着 Normalization 维度的新趋势
- Module Sequence 维度的非均匀模式（5:1）是对传统"每层相同"设计的重要突破
- 作为 Dense 模型，展示了不依赖 MoE 也能通过注意力模式创新实现 128K 长上下文
- 在六维度框架中定位：GQA+Local/Global+QK-Norm (Token Mixer) + Dense SwiGLU FFN (Channel Mixer) + RMSNorm+QK-Norm (Norm) + Dual-freq RoPE (PE) + Pre-Norm Residual (Residual) + 5:1 非均匀层模式 (Module Seq)
