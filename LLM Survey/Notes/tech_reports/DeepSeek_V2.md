# DeepSeek - DeepSeek-V2 架构分析

## 基本信息
- 论文标题：DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model
- 参数量：236B 总参数 / 21B 激活参数
- 层数：60 层
- 隐藏维度：5120
- 注意力头数：128（每头维度 128）
- KV 压缩维度：512，Query 压缩维度：1536
- 上下文长度：128K tokens（通过 YaRN 扩展）
- 训练数据量：8.1T tokens
- 发布时间：2024 年 5 月
- 论文链接：arXiv:2405.04434

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Multi-head Latent Attention (MLA) | 128 个注意力头，每头维度 128；KV 压缩维度 512，Query 压缩维度 1536；解耦 RoPE 维度 64/头；低秩联合压缩 KV 到潜在向量 | MLA 首次提出：通过 KV cache 低秩压缩替代 GQA/MQA，KV cache 减少 93.3%，同时保持 MHA 级别性能 |
| Channel Mixer | DeepSeekMoE (SwiGLU) | 160 个路由专家 + 2 个共享专家；每 token 激活 Top-6 路由专家；专家中间维度 1536；SwiGLU 激活函数；第 1 层为 Dense FFN | 超细粒度专家分割（160 个小专家），2 个共享专家捕获通用知识 |
| Normalization | RMSNorm (Pre-Norm) | 在注意力和 FFN 子层之前应用 RMSNorm | 标准做法 |
| Position Encoding | Decoupled RoPE | RoPE 与 KV 压缩解耦；Q/K 各有专用 RoPE 维度（每头 64 维）；支持 YaRN 扩展至 128K | 解耦设计避免 RoPE 与低秩压缩的冲突，是 MLA 的关键组成部分 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → FFN/MoE → Add | 每层先 RMSNorm 后 MLA，残差连接；再 RMSNorm 后 MoE FFN，残差连接 | 标准 Pre-Norm 序列 |

## 关键架构创新

1. **Multi-head Latent Attention (MLA)**：核心创新。将 KV 联合压缩到低维潜在向量（512 维），推理时仅需缓存该向量而非完整 KV，KV cache 减少 93.3%。通过解耦 RoPE 策略解决位置编码与压缩的兼容性问题。

2. **DeepSeekMoE 超细粒度设计**：160 个路由专家（远多于 Mixtral 的 8 个），每个专家更小更专精。2 个共享专家始终激活，处理跨领域通用模式。

3. **Device-Limited 路由**：限制每个 token 最多被发送到 M 个设备上的专家，减少通信开销，提升训练效率。

## 与前代/同期模型对比

- **vs DeepSeek 67B (V1)**：从 Dense 架构演进为 MoE，参数从 67B 增至 236B 但激活参数仅 21B；引入全新的 MLA 和 DeepSeekMoE 架构。
- **vs Mixtral 8x7B**：专家数量从 8 增至 160（超细粒度），引入 2 个共享专家；注意力从 GQA 演进为 MLA；路由从 Top-2 变为 Top-6。
- **vs DeepSeek-V3**：V3 继承 MLA+MoE 框架，专家数增至 256+1 共享，路由改为 Top-8，新增 Auxiliary-Loss-Free 负载均衡和 MTP。
- **vs Llama 3 70B**：DeepSeek-V2 以 21B 激活参数达到接近 70B Dense 模型的性能，推理成本大幅降低。

## 对本综述的启示
- MLA 是 Token Mixer 维度的重大创新，开辟了"KV cache 压缩"这一新方向，与 GQA/MQA 形成互补路线
- DeepSeekMoE 的超细粒度设计展示了 Channel Mixer 中专家粒度的重要性
- 解耦 RoPE 说明 Position Encoding 与 Token Mixer 设计之间存在深层耦合关系
- 在六维度框架中定位：MLA (Token Mixer) + DeepSeekMoE-SwiGLU (Channel Mixer) + RMSNorm (Norm) + Decoupled RoPE (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
