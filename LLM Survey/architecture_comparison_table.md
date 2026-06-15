# 大厂 LLM 架构六维度对比总表

> 基于 22 份技术报告整理，覆盖 18 家公司

| 模型 | 年份 | 参数量 | Token Mixer | Channel Mixer | Normalization | Position Encoding | Residual Connection | Module Sequence |
|------|------|--------|-------------|---------------|---------------|-------------------|---------------------|-----------------|
| Llama 2 | 2023 | 7B/13B/70B | MHA (7B); GQA (70B, 8 KV头) | SwiGLU FFN (Dense) | RMSNorm | RoPE | Pre-Norm Residual | Pre-Norm |
| Mistral 7B | 2023 | 7.3B | GQA (8 KV头) + Sliding Window (W=4096) | SwiGLU FFN (Dense) | RMSNorm | RoPE | Pre-Norm Residual | Pre-Norm |
| Mixtral 8x7B | 2023 | 46.7B/13B激活 | GQA (8 KV头) + Sliding Window | SMoE-SwiGLU (8专家, Top-2) | RMSNorm | RoPE | Pre-Norm Residual | Pre-Norm |
| PanGu-Sigma | 2023 | 1.085T | 标准自注意力 | RRE-MoE (随机路由, 领域分组) | LayerNorm (推测) | 学习式 PE (推测) | 标准残差 | Dense下层 + Sparse上层 异构序列 |
| DeepSeek-V2 | 2024 | 236B/21B激活 | MLA (KV压缩维度512, 128头) | DeepSeekMoE-SwiGLU (160专家+2共享, Top-6) | RMSNorm | Decoupled RoPE | Pre-Norm Residual | Pre-Norm |
| Llama 3 | 2024 | 8B/70B/405B | GQA (8 KV头) | SwiGLU FFN (Dense) | RMSNorm | RoPE (theta=500K) | Pre-Norm Residual | Pre-Norm |
| Gemma 2 | 2024 | 2B/9B/27B | GQA + 交替局部/全局注意力 (SWA 4096 + Global 8192) | GeGLU FFN (Dense) | RMSNorm (Pre+Post双重) | RoPE | Pre-Norm Residual | Pre+Post-Norm 交替序列 |
| Qwen2.5 | 2024 | 0.5B~72B | GQA (8 KV头, 72B) | SwiGLU FFN (Dense) / MoE (闭源) | RMSNorm | RoPE (ABF扩展, base=1M) | Pre-Norm Residual | Pre-Norm |
| GLM-4 | 2024 | 9B (开源版) | GQA (2 KV头, 16:1极端比例) | SwiGLU FFN (Dense) | RMSNorm | RoPE | Pre-Norm Residual | Pre-Norm |
| Yi-Lightning | 2024 | 未公开 (MoE) | 混合注意力 (Full+SWA) + 跨层KV共享 | 细粒度 MoE | RMSNorm (推测) | RoPE (推测) | Pre-Norm Residual (推测) | Pre-Norm (推测) |
| Phi-4 | 2024 | 14B | GQA (10 KV头, 4:1) | SwiGLU FFN (Dense) | RMSNorm | RoPE | Pre-Norm Residual | Pre-Norm |
| Hunyuan-Large | 2024 | 389B/52B激活 | GQA (8 KV头) + Cross-Layer Attention (CLA, 每2层共享KV) | MoE-SwiGLU (16专家+1共享, Top-1) | RMSNorm | RoPE | Pre-Norm Residual | Pre-Norm |
| DeepSeek-V3 | 2024 | 671B/37B激活 | MLA (KV压缩维度512, 128头) | DeepSeekMoE-SwiGLU (256专家+1共享, Top-8) | RMSNorm | Decoupled RoPE | Pre-Norm Residual | Pre-Norm |
| DeepSeek-R1 | 2025 | 671B/37B激活 | MLA (继承V3) | DeepSeekMoE-SwiGLU (256专家+1共享, Top-8) | RMSNorm | Decoupled RoPE | Pre-Norm Residual | Pre-Norm |
| MiniMax-01 | 2025 | 456B/45.9B激活 | Lightning Attention + Softmax Attention (7:1混合) | MoE (32专家, Top-2) | RMSNorm (推测) | RoPE (base=10M, 半维度应用) | Pre-Norm Residual | 7:1 非均匀层模式 |
| OLMo 2 | 2025 | 7B/13B/32B | 标准注意力 + QKV Clipping | SwiGLU FFN (Dense) | RMSNorm (Reordered/Post-Norm) | RoPE | Post-Norm Residual | Reordered-Norm: Attn→Norm→Add→FFN→Norm→Add |
| Kimi k1.5 | 2025 | 未公开 | 未公开 (推测标准注意力) | 未公开 (推测标准FFN) | 未公开 | 未公开 (推测RoPE) | 未公开 | 未公开 |
| Baichuan-M1 | 2025 | 14B | MHA + Short Convolution on K/V + 部分层SWA | SwiGLU FFN (Dense) | RMSNorm | RoPE (base=1M) | Pre-Norm Residual | Pre-Norm |
| Gemma 3 | 2025 | 1B/4B/12B/27B | GQA (2:1) + 交替Local/Global (5:1) + QK-Norm | SwiGLU FFN (Dense) | RMSNorm + QK-Norm | RoPE (双基频: Global 1M / Local 10K) | Pre-Norm Residual | 5:1 非均匀层模式 |
| Qwen3 | 2025 | 235B-A22B (旗舰MoE); 0.6B~32B (Dense) | GQA (4 KV头, 16:1) + QK-Norm | MoE-SwiGLU (128专家, Top-8, 无共享专家) / Dense-SwiGLU | RMSNorm | RoPE + YaRN | Pre-Norm Residual | Pre-Norm |
| Llama 4 | 2025 | Scout 109B/17B激活; Maverick 400B/17B激活 | GQA (8 KV头) + iRoPE (交替RoPE/NoPE层) | MoE-SwiGLU (Scout 16专家; Maverick 128专家; +1共享; 交替Dense/MoE层) | RMSNorm + Q/K额外归一化 | iRoPE (交替RoPE层+NoPE层, 每4层交替) | Pre-Norm Residual | 交替Dense/MoE层 Pre-Norm |
| ERNIE 4.5 | 2025 | 300B/47B激活 | GQA | 异构MoE (64专家, Top-8, 模态隔离路由) | RMSNorm (推测) | RoPE (推测) | Pre-Norm Residual (推测) | Pre-Norm (推测) |

---

## 六维度架构趋势总结

### 1. Token Mixer 趋势

- **GQA 成为绝对主流**：22 个模型中 18 个采用 GQA 或其变体，完全取代了早期的 MHA（仅 Llama 2 7B、Baichuan-M1 保留 MHA）。KV 头数从 2（GLM-4）到 16（Gemma 3）不等，8 个 KV 头是最常见配置。
- **MLA 开辟新路线**：DeepSeek 系列（V2/V3/R1）独创 MLA，通过低秩压缩 KV cache 替代 GQA 的头数缩减策略，KV cache 减少 93.3%，是 Token Mixer 最具原创性的创新。
- **异构层注意力成为趋势**：从 Mistral 7B 的全层 SWA，演进到 Gemma 2/3 的交替 Local/Global、MiniMax-01 的 Lightning+Softmax 7:1 混合、Llama 4 的 iRoPE 交替 RoPE/NoPE。"不同层使用不同注意力"已成为 2024-2025 年的主流设计模式。
- **跨层 KV 共享**：Hunyuan-Large 的 CLA 和 Yi-Lightning 的跨层 KV 共享从层维度压缩 KV cache，与 GQA（头维度）和 MLA（秩维度）形成三条正交的 KV cache 优化路线。
- **线性注意力进入实用阶段**：MiniMax-01 首次在 456B 参数模型上验证 Lightning Attention（线性注意力）的可行性，配合少量 Softmax 层实现百万级上下文。

### 2. Channel Mixer 趋势

- **SwiGLU 统一 GLU 变体**：除 Gemma 2 使用 GeGLU 外，其余所有模型均采用 SwiGLU 作为 FFN 激活函数，SwiGLU 已成为事实标准。
- **MoE 从少数派变为主流**：2023 年仅 Mixtral 和 PanGu-Sigma 使用 MoE；到 2024-2025 年，DeepSeek V2/V3、Hunyuan、MiniMax、Yi-Lightning、Qwen3、Llama 4、ERNIE 4.5 均采用 MoE，MoE 已成为大模型的主流选择。
- **专家粒度分化**：形成两大路线——DeepSeek 系列的超细粒度（160-256 个小专家）vs Mixtral/Hunyuan 的粗粒度（8-16 个大专家），Qwen3（128 专家）和 ERNIE 4.5（64 专家）居中。
- **共享专家的分歧**：DeepSeek V2/V3（1-2 个共享专家）、Hunyuan（1 个共享专家）、Llama 4（1 个共享专家）采用共享专家；而 Qwen3 和 Mixtral 不使用共享专家，两种路线均有成功案例。
- **异构 MoE 出现**：ERNIE 4.5 的模态隔离路由和 PanGu-Sigma 的随机路由打破了"所有专家同构"的假设。

### 3. Normalization 趋势

- **RMSNorm 完全统一**：22 个模型中 21 个使用 RMSNorm（PanGu-Sigma 推测为 LayerNorm），RMSNorm 已完全取代 LayerNorm 成为 LLM 的标准归一化方法。
- **QK-Norm 成为新标准**：Gemma 3 和 Qwen3 引入 QK-Norm（对 Q/K 矩阵归一化），Llama 4 对 Q/K 施加额外 RMSNorm，表明注意力内部归一化正成为新趋势，替代 Gemma 2 的 logit soft-capping。
- **双重归一化实验**：Gemma 2 的 Pre+Post 双重 RMSNorm 和 OLMo 2 的 Reordered-Norm 展示了归一化位置仍有探索空间。

### 4. Position Encoding 趋势

- **RoPE 一统天下**：除 PanGu-Sigma（推测学习式 PE）外，所有模型均采用 RoPE 或其变体，RoPE 已成为 LLM 位置编码的唯一主流选择。
- **基频调整成为长上下文关键**：从原始 10K 到 Llama 3 的 500K、Qwen2.5/Baichuan-M1/Gemma 3 Global 层的 1M、MiniMax-01 的 10M，RoPE 基频持续提升以支持更长上下文。
- **解耦 RoPE**：DeepSeek 系列的 Decoupled RoPE 将位置编码与 KV 压缩分离，是 MLA 架构的关键配套设计。
- **差异化位置编码**：Llama 4 的 iRoPE（交替 RoPE/NoPE 层）和 Gemma 3 的双基频 RoPE（Global 1M / Local 10K）打破了"所有层使用相同位置编码"的惯例，按层差异化配置位置编码。

### 5. Residual Connection 趋势

- **Pre-Norm Residual 高度统一**：21/22 个模型采用标准 Pre-Norm 残差连接，这是最稳定、最无争议的维度。
- **OLMo 2 的 Reordered-Norm 是唯一例外**：将归一化从子层输入移至子层输出（Post-Norm 变体），被证明能提升训练稳定性，但尚未被其他模型采纳。
- **该维度创新空间有限**：残差连接的设计已高度收敛，未来创新更可能出现在与 Normalization 和 Module Sequence 的组合方式上。

### 6. Module Sequence 趋势

- **标准 Pre-Norm 序列仍是主流**：约 14/22 个模型采用标准 Pre-Norm 序列（Norm→Attn→Add→Norm→FFN→Add）。
- **非均匀层模式兴起**：Gemma 2/3 的交替 Local/Global（1:1 和 5:1）、MiniMax-01 的 Lightning/Softmax 7:1、Llama 4 的交替 Dense/MoE 层和 RoPE/NoPE 层、PanGu-Sigma 的 Dense 下层+Sparse 上层，展示了"不同层使用不同配置"的设计趋势。
- **归一化位置多样化**：Gemma 2 的 Pre+Post 双重归一化和 OLMo 2 的 Reordered-Norm 在模块序列层面引入了新变体。
- **整体趋势**：Module Sequence 从"每层完全相同"向"异构层组合"演进，层间差异化设计成为 2024-2025 年的重要方向。
