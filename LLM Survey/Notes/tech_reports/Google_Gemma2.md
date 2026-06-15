# Google - Gemma 2 架构分析

## 基本信息
- 论文标题：Gemma 2: Improving Open Language Models at a Practical Size
- 参数量：2B / 9B / 27B（三个尺寸）
- 层数：2B：26 层；9B：42 层；27B：46 层
- 隐藏维度：2B：2304；9B：3584；27B：4608
- 注意力头数：2B：8 Q/4 KV；9B：16 Q/8 KV；27B：32 Q/16 KV（均为 GQA）
- 每头维度：2B/9B：256；27B：128
- FFN 维度：2B：18432；9B：28672；27B：73728
- 上下文长度：8192 tokens
- 词表大小：256,128
- 训练数据量：2T tokens（2B）；8T tokens（9B）；13T tokens（27B）
- 发布时间：2024 年 8 月
- 论文链接：arXiv:2408.00118

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA + 交替局部/全局注意力 | 每隔一层交替使用局部滑动窗口注意力（窗口 4096）和全局注意力（8192）；GQA 压缩 KV 头 | 交替局部/全局注意力模式，平衡计算效率与全局建模能力 |
| Channel Mixer | GeGLU FFN (Dense) | 使用近似 GeGLU（Gated GELU）非线性激活；FFN 维度较大（27B 模型为 73728） | GeGLU 替代 SwiGLU，是 GLU 变体的另一选择 |
| Normalization | RMSNorm (Pre-Norm + Post-Norm) | 在注意力和 FFN 子层前后均应用 RMSNorm（即 Pre-Norm 和 Post-Norm 同时使用） | 双重 RMSNorm（前后均归一化）增强训练稳定性 |
| Position Encoding | RoPE | 旋转位置编码 | 标准做法 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre+Post-Norm: Norm → Attn → Norm → Add → Norm → FFN → Norm → Add | 每个子层前后都有 RMSNorm，交替使用局部和全局注意力 | 双重归一化的模块序列 |

## 关键架构创新

1. **交替局部/全局注意力**：奇数层使用局部滑动窗口注意力（窗口 4096），偶数层使用全局注意力（8192）。这种设计减少了约一半注意力层的计算量，同时保持全局信息流动。

2. **Logit Soft-Capping**：在自注意力层（cap=50.0）和最终输出层（cap=30.0）使用 soft-capping 函数 `logits ← cap * tanh(logits / cap)` 来防止 logit 值过大，稳定训练过程。

3. **知识蒸馏训练**：27B 模型从更大的教师模型蒸馏而来，而非纯粹从头训练。这使得较小模型能获得超越其规模的性能。

4. **双重 RMSNorm**：在每个子层的输入和输出都应用 RMSNorm，比标准 Pre-Norm 多一次归一化，进一步稳定训练。

5. **大头维度**：2B 和 9B 模型使用 256 维的注意力头（而非常见的 128），增强每个头的表达能力。

## 与前代/同期模型对比

- **vs Gemma 1**：引入交替局部/全局注意力（Gemma 1 为全局注意力）；引入 GQA（Gemma 1 为 MHA/MQA）；增加 logit soft-capping；引入知识蒸馏。
- **vs Mistral 7B**：两者都使用滑动窗口注意力，但 Gemma 2 是交替使用（每隔一层），Mistral 7B 是全部层使用。
- **vs Llama 3 8B**：Gemma 2 9B 使用交替注意力 + GeGLU + 双重 RMSNorm vs Llama 3 的全局 GQA + SwiGLU + 标准 Pre-Norm。
- **vs Llama 4**：两者都使用交替注意力模式，但 Llama 4 的 iRoPE 更激进（NoPE 层无位置编码），Gemma 2 的局部层仍使用 RoPE。

## 对本综述的启示
- 交替局部/全局注意力是 Token Mixer 维度的重要设计模式，在 Gemma 2、Llama 4、Yi-Lightning 中均有体现
- 双重 RMSNorm（Pre+Post）是 Normalization 维度的新变体，影响 Module Sequence 的定义
- Logit soft-capping 是训练稳定性技巧，可作为 Normalization 维度的补充讨论
- GeGLU vs SwiGLU 的选择展示了 Channel Mixer 中 GLU 变体的多样性
- 在六维度框架中定位：GQA+Alternating Local/Global Attn (Token Mixer) + GeGLU-Dense (Channel Mixer) + RMSNorm Pre+Post (Norm) + RoPE (PE) + Pre-Norm Residual (Residual) + Pre+Post-Norm Alternating Sequence (Module Seq)
