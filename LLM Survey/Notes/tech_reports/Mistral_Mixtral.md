# Mistral AI - Mixtral 8x7B 架构分析

## 基本信息
- 论文标题：Mixtral of Experts
- 参数量：46.7B 总参数 / 13B 激活参数
- 层数：32 层
- 隐藏维度：4096
- 注意力头数：32（KV 头数 8，GQA；每头维度 128）
- 上下文长度：32K tokens
- 词表大小：32,000
- 训练数据量：未公开（开放网络数据）
- 发布时间：2023 年 12 月 11 日
- 论文链接：arXiv:2401.04088

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped Query Attention (GQA) + Sliding Window | 32 个 Query 头，8 个 KV 头，每头维度 128；滑动窗口大小 4096 tokens | 结合 GQA 与滑动窗口注意力，降低 KV cache 同时支持长序列推理 |
| Channel Mixer | Sparse MoE (SwiGLU) | 每层 8 个专家，每 token 路由 Top-2 专家；每个专家为独立 SwiGLU FFN（中间维度 14336）；路由器为线性门控网络 | 首个开源高质量 MoE 大模型，证明 SMoE 在开源领域的可行性 |
| Normalization | RMSNorm (Pre-Norm) | 在注意力和 FFN 子层之前应用 RMSNorm | 标准做法 |
| Position Encoding | RoPE | 旋转位置编码，应用于 Q/K 向量 | 标准做法 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → MoE → Add | 每层先 RMSNorm 后注意力（GQA），残差连接；再 RMSNorm 后 MoE FFN，残差连接 | 标准 Pre-Norm 序列 |

## 关键架构创新

1. **Sliding Window Attention (SWA)**：每个 token 仅关注前 W=4096 个 token，通过多层堆叠实现信息传播（k 层后可覆盖 k×W 个 token）。配合 Rolling Buffer Cache，推理时 KV cache 固定为窗口大小，显著降低内存占用。

2. **开源 MoE 先驱**：Mixtral 是首个达到高质量水平的开源 MoE 模型，以 13B 激活参数匹配或超越 Llama 2 70B（Dense）的性能，证明了 MoE 架构在开源社区的实用价值。

3. **简洁的 MoE 设计**：8 个专家 + Top-2 路由的经典配置，没有共享专家，路由器为简单的线性层 + softmax，设计简洁高效。

## 与前代/同期模型对比

- **vs Mistral 7B**：共享相同基础架构（层数、隐藏维度、注意力配置），唯一区别是将 Dense FFN 替换为 8 专家 MoE 层，总参数从 7B 增至 46.7B，但激活参数仅 13B。
- **vs Llama 2 70B**：Mixtral 以 13B 激活参数在多数基准上匹配或超越 70B Dense 模型，推理速度快 6 倍。
- **vs DeepSeek-V3**：Mixtral 的 8 个大专家 vs DeepSeek-V3 的 256 个小专家（超细粒度），无共享专家 vs 1 个共享专家，Top-2 vs Top-8 路由。
- **vs GShard/Switch Transformer**：Mixtral 采用 Top-2 而非 Top-1 路由，每个 token 获得更丰富的专家组合。

## 对本综述的启示
- Mixtral 是 SMoE 架构在开源 LLM 中的里程碑，验证了"少量大专家 + Top-K 路由"的经典 MoE 范式
- SWA 是 Token Mixer 维度中注意力模式的重要变体，介于全局注意力和局部注意力之间
- 在六维度框架中定位：GQA+SWA (Token Mixer) + SMoE-SwiGLU (Channel Mixer) + RMSNorm (Norm) + RoPE (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
