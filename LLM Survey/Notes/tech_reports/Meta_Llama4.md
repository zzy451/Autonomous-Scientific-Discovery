# Meta - Llama 4 架构分析

## 基本信息
- 论文标题：The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes
- 参数量：Scout 109B 总参数/17B 激活；Maverick 400B 总参数/17B 激活；Behemoth（教师模型）~2T 总参数/288B 激活
- 层数：48 层（Scout 和 Maverick 共享）
- 隐藏维度：5120
- 注意力头数：40 个 Query 头，8 个 KV 头（GQA）
- 注意力分块大小：8192
- 上下文长度：Scout 10M tokens；Maverick 1M tokens
- 训练数据量：约 40T tokens（200 种语言）
- 发布时间：2025 年 4 月
- 论文链接：arXiv:2601.11659（注：该论文因署名问题被 arXiv 管理员移除）

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA + iRoPE（交替 RoPE/NoPE 层） | 40 个 Q 头，8 个 KV 头（GQA）；RoPE 层使用分块注意力（chunk=8192）处理局部信息；NoPE 层无位置编码，访问全局上下文；每 4 层交替一次；推理时温度缩放增强长度泛化 | iRoPE 是全新的位置编码策略，通过交替 RoPE/NoPE 实现超长上下文（10M），RoPE 层处理局部、NoPE 层处理全局 |
| Channel Mixer | MoE (SwiGLU) | Scout：16 个专家；Maverick：128 个专家；交替 Dense 层和 MoE 层；每层含 1 个共享专家 + 路由专家；gate/up/down 投影结构 | 交替 Dense/MoE 层设计；共享专家处理通用模式 |
| Normalization | RMSNorm | 标准 RMSNorm；RoPE 层中对 Q/K 施加额外无参数 RMSNorm（在 RoPE 之后） | Q/K 额外归一化增强训练稳定性 |
| Position Encoding | iRoPE（Interleaved RoPE） | RoPE 层：标准旋转位置编码 + 分块注意力；NoPE 层：无位置编码 + 全局注意力；每 4 层交替 | 突破性设计，实现 10M 级别上下文长度 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → FFN/MoE → Add | Dense 层和 MoE 层交替出现 | 交替 Dense/MoE 的混合序列 |

## 关键架构创新

1. **iRoPE（Interleaved RoPE）**：核心创新。交替使用 RoPE 层（局部分块注意力，chunk=8192）和 NoPE 层（全局注意力，无位置编码）。RoPE 层捕获局部位置关系，NoPE 层关注全局语义关联。这种混合策略使 Scout 支持 10M token 上下文。

2. **推理时温度缩放**：动态调整注意力分布的温度参数，增强长度泛化能力，使模型在超出训练长度时仍能保持性能。

3. **Codistillation 训练**：使用 Behemoth（~2T 参数）作为教师模型，通过硬目标和软目标的组合蒸馏训练 Scout 和 Maverick，显著提升小模型性能。

4. **早期融合多模态**：从预训练阶段就同时处理文本、图像和视频数据，将视觉 token 与文本 token 拼接后统一处理。

5. **交替 Dense/MoE 层**：不是所有层都使用 MoE，而是 Dense 层和 MoE 层交替出现，平衡计算效率和模型容量。

## 与前代/同期模型对比

- **vs Llama 3 405B**：从 Dense 架构转向 MoE；从标准 RoPE 演进为 iRoPE；上下文从 128K 扩展至 1M-10M；引入原生多模态。
- **vs Mixtral 8x7B**：Maverick 的 128 专家远多于 Mixtral 的 8 专家；引入共享专家和交替 Dense/MoE 层；iRoPE vs 标准 RoPE。
- **vs DeepSeek-V3**：两者都是大规模 MoE，但 Llama 4 使用 GQA+iRoPE vs DeepSeek 的 MLA+Decoupled RoPE；Llama 4 的交替 Dense/MoE vs DeepSeek 的全 MoE（除第 1 层）。
- **vs Gemma 2**：两者都使用交替注意力模式（局部/全局），但 Llama 4 的 iRoPE 更激进（NoPE 层完全无位置编码）。

## 对本综述的启示
- iRoPE 是 Position Encoding 维度的重大创新，打破了"所有层使用相同位置编码"的惯例
- 交替 Dense/MoE 层是 Module Sequence 维度的新变体
- 10M 级别上下文长度展示了架构设计对长度泛化的关键作用
- 在六维度框架中定位：GQA+iRoPE (Token Mixer) + MoE-SwiGLU (Channel Mixer) + RMSNorm (Norm) + iRoPE (PE) + Pre-Norm Residual (Residual) + Alternating Dense/MoE Pre-Norm Sequence (Module Seq)
