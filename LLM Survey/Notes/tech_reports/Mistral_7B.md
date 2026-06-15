# Mistral AI - Mistral 7B 架构分析

## 基本信息
- 论文标题：Mistral 7B
- 参数量：7.3B
- 层数：32 层
- 隐藏维度：4096
- FFN 中间维度：14336
- 注意力头数：32 个 Query 头，8 个 KV 头（GQA）；每头维度 128
- 上下文长度：8192 tokens（滑动窗口 4096）
- 词表大小：32,000
- 训练数据量：未公开
- 发布时间：2023 年 10 月
- 论文链接：arXiv:2310.06825

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA + Sliding Window Attention (SWA) | 32 Q 头，8 KV 头（GQA，4:1 比例）；滑动窗口大小 W=4096；通过 k 层堆叠可覆盖 k×W tokens 的理论感受野；Rolling Buffer Cache 固定 KV cache 大小 | 首次在开源 LLM 中系统性地结合 GQA 与 SWA，开创了高效注意力的实践范式 |
| Channel Mixer | SwiGLU FFN (Dense) | 中间维度 14336；SwiGLU 激活函数 | 标准做法 |
| Normalization | RMSNorm (Pre-Norm) | 在注意力和 FFN 子层之前应用 RMSNorm | 标准做法 |
| Position Encoding | RoPE | 旋转位置编码 | 标准做法 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → FFN → Add | 标准 Pre-Norm 序列 | 标准做法 |

## 关键架构创新

1. **Sliding Window Attention (SWA)**：核心创新。每个 token 仅关注前 W=4096 个 token（而非全部历史 token），将注意力计算从 O(n²) 降低为 O(n×W)。通过多层堆叠，信息可在 k 层后传播 k×W 个位置，32 层模型理论感受野为 131,072 tokens。

2. **Rolling Buffer Cache**：KV cache 大小固定为窗口大小 W，使用循环缓冲区（position i 存储在 cache[i mod W]），推理时内存占用恒定，不随序列长度增长。

3. **Pre-fill 与 Chunking**：推理时将 prompt 分块处理，每块大小为窗口大小，利用已知 prompt 的特性预计算注意力，提升推理效率。

4. **高效 7B 基准**：Mistral 7B 以 7B 参数在多项基准上超越 Llama 2 13B，成为高效小模型的标杆。

## 与前代/同期模型对比

- **vs Llama 2 7B/13B**：Mistral 7B 引入 SWA 和 GQA（Llama 2 7B 使用 MHA），以 7B 参数超越 Llama 2 13B。
- **vs Mixtral 8x7B**：Mixtral 直接继承 Mistral 7B 的全部架构，仅将 Dense FFN 替换为 8 专家 MoE。
- **vs Llama 3 8B**：Llama 3 放弃了 SWA 回归全局注意力，但保留了 GQA；Mistral 7B 的 SWA 在推理效率上更优。
- **vs Gemma 2**：Gemma 2 采用交替局部/全局注意力（部分层 SWA），而 Mistral 7B 全部层使用 SWA。

## 对本综述的启示
- Mistral 7B 是 SWA 在 LLM 中的开创性应用，直接影响了后续 Mixtral、Gemma 2、Yi-Lightning 等模型的注意力设计
- GQA + SWA 的组合成为高效 Token Mixer 的经典范式
- Rolling Buffer Cache 展示了架构设计与推理系统优化的紧密关联
- 在六维度框架中定位：GQA+SWA (Token Mixer) + SwiGLU-Dense (Channel Mixer) + RMSNorm (Norm) + RoPE (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
