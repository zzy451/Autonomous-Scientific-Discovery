# 阶跃星辰 - Step-2 / Step-2 mini 架构分析

## 基本信息
- 公司：阶跃星辰（StepFun）
- 模型：Step-2（万亿参数 MoE）/ Step-2 mini（推理优化版）
- 参数量：Step-2 约万亿参数（MoE 架构）；Step-2 mini 参数未公开
- 上下文长度：未明确公开
- 训练数据量：未明确公开
- 发布时间：Step-2 预览版 2024 年 3 月；正式版 2024 年 7 月（WAIC）
- 论文链接：无正式 arXiv 论文（通过官方博客和会议发布）
- MFA 论文：Multi-matrix Factorization Attention (Hu et al., 2025, ACL)

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | MFA (Multi-matrix Factorization Attention) [Step-2 mini] | 在 QK 交互阶段引入低秩矩阵分解；MFA-Key-Reuse 变体将 Key cache 复用为 Value cache；节省约 94% KV cache | MFA 是继 GQA/MLA 之后的第三条 KV cache 优化路线：通过矩阵分解而非头数缩减或低秩压缩 |
| Channel Mixer | MoE (SwiGLU) | Step-2 从头训练 MoE（非 Dense 转 MoE）；部分专家共享参数；异构化专家设计 | 共享参数 + 异构化专家的设计策略 |
| Normalization | 未明确公开（推测 RMSNorm） | — | — |
| Position Encoding | 未明确公开（推测 RoPE） | — | — |
| Residual Connection | 未明确公开（推测 Pre-Norm） | — | — |
| Module Sequence | 未明确公开（推测 Pre-Norm） | — | — |

## 关键架构创新

1. **Multi-matrix Factorization Attention (MFA)**：Step-2 mini 的核心创新。在注意力机制的 QK 交互阶段引入低秩矩阵分解，在严格的 KV cache 预算下保持高性能。与 GQA（减少 KV 头数）和 MLA（低秩压缩 KV 到潜在向量）不同，MFA 通过矩阵分解 QK 乘积来降低内存需求。

2. **MFA-Key-Reuse (MFA-KR)**：进一步创新，通过重参数化的 Value 投影将 Key cache 复用为 Value cache，消除单独存储 Value cache 的需要，实现约 94% 的 KV cache 节省。这一节省比例与 DeepSeek-V2 的 MLA（93.3%）相当。

3. **从头训练万亿 MoE**：Step-2 选择从头训练（train from scratch）而非从 Dense 模型 upcycle，虽然训练难度更高但性能上限更高。

4. **异构化专家设计**：MoE 中的专家并非同构，而是采用了参数共享和异构化设计，平衡计算效率与模型效果。

## 与前代/同期模型对比

- **vs DeepSeek-V2 (MLA)**：MFA 和 MLA 都实现约 93-94% 的 KV cache 节省，但技术路线不同——MFA 通过 QK 矩阵分解，MLA 通过 KV 低秩压缩到潜在向量。
- **vs GQA (Llama 3/Qwen)**：GQA 通过减少 KV 头数压缩 KV cache（典型节省 4-16 倍），MFA 通过矩阵分解实现更大的压缩比。
- **vs Hunyuan-Large (CLA)**：CLA 从层维度共享 KV cache，MFA 从矩阵分解维度优化，两者正交互补。

## 对本综述的启示
- MFA 是 Token Mixer 维度的重要创新，与 GQA、MLA、CLA 形成四条 KV cache 优化路线：头维度压缩（GQA）、秩维度压缩（MLA）、层维度共享（CLA）、矩阵分解（MFA）
- MFA-Key-Reuse 展示了 Key 和 Value 之间的冗余性可以被利用，为未来架构设计提供新思路
- 异构化专家设计与 ERNIE 4.5 的模态隔离路由共同体现了"非同构 MoE"的趋势
- 缺乏正式技术报告限制了详细的架构分析
- 在六维度框架中定位：MFA (Token Mixer) + MoE-SwiGLU (Channel Mixer) + RMSNorm (Norm, 推测) + RoPE (PE, 推测) + Pre-Norm Residual (Residual, 推测) + Standard Pre-Norm Sequence (Module Seq, 推测)
