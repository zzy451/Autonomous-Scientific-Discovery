# MiniMax - MiniMax-01 架构分析

## 基本信息
- 论文标题：MiniMax-01: Scaling Foundation Models with Lightning Attention
- 参数量：456B 总参数 / 45.9B 激活参数
- 层数：80 层
- 隐藏维度：6,144
- 注意力头数：64（每头维度 128）
- 上下文长度：1M tokens（训练）/ 4M tokens（推理外推）
- 词表大小：200,064
- 训练数据量：约 12T tokens（文本）+ 512B tokens（视觉-语言，VL-01）
- 发布时间：2025 年 1 月 15 日
- 论文链接：arXiv:2501.08313

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | 混合注意力：Lightning Attention + Softmax Attention | 每 7 层 Lightning Attention 后接 1 层 Softmax Attention（7:1 模式）；64 头，每头维度 128；Lightning Attention 是线性注意力的高效实现 | 首个在超大规模模型上验证线性注意力与 Softmax 注意力混合的架构；7:1 的稀疏全局注意力实现百万级上下文 |
| Channel Mixer | MoE (Top-2 路由) | 32 个专家，Top-2 路由；专家隐藏维度 9,216 | 相比 DeepSeek-V3 的 256 个超细粒度专家，MiniMax 选择 32 个中等粒度专家 |
| Normalization | 未明确公开（推测 RMSNorm） | 现代 Transformer 标准做法 | — |
| Position Encoding | RoPE (基频 10,000,000) | RoPE 应用于注意力头维度的一半（64/128 维）；基频极高（10M），是 Llama 3 的 20 倍 | 超高基频 RoPE（10M）+ 半维度应用，为百万级上下文提供位置编码支持 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm + 7:1 交替模式 | 7 层 (Norm -> Lightning Attn -> Add -> Norm -> MoE -> Add) 后接 1 层 (Norm -> Softmax Attn -> Add -> Norm -> MoE -> Add) | 非均匀的层间模式设计，每 8 层形成一个注意力"超级块" |

## 关键架构创新

1. **Lightning Attention 混合架构**：核心创新在于将线性注意力（Lightning Attention）与标准 Softmax Attention 按 7:1 比例混合。Lightning Attention 的计算复杂度为 O(n) 而非 O(n^2)，使得百万级上下文成为可能。每隔 7 层插入一层全局 Softmax Attention 保证信息整合质量。

2. **百万级上下文窗口**：训练时支持 1M tokens 上下文，推理时可外推至 4M tokens。这是目前公开报告中最长的上下文窗口之一。

3. **超高基频 RoPE (10M)**：RoPE 基频设为 10,000,000（比 Llama 3 的 500K 高 20 倍），且仅应用于注意力头维度的一半，为超长上下文提供位置编码支持。

4. **高效分布式训练框架**：
   - LASP+（Linear Attention Sequence Parallelism Plus）：针对线性注意力的序列并行优化
   - Varlen Ring Attention：处理变长超长序列的环形注意力
   - ETP（Expert Tensor Parallelism）：MoE 专家的张量并行
   - 大量计算-通信重叠优化

5. **多模态扩展**：MiniMax-VL-01 通过冻结的 303M ViT + 2 层 MLP 投影器接入视觉输入，使用动态分辨率机制处理不同宽高比图像。

## 与前代/同期模型对比

- **vs DeepSeek-V3**：Token Mixer 是最大差异——MiniMax 的 Lightning+Softmax 混合 vs DeepSeek 的 MLA；MoE 粒度不同（32 专家 Top-2 vs 256+1 专家 Top-8）；MiniMax 支持 4M 上下文 vs DeepSeek-V3 的 128K。
- **vs Llama 3 405B**：MiniMax 总参数更多（456B vs 405B）但激活更少（45.9B vs 405B）；MiniMax 上下文长 30 倍以上（4M vs 128K）。
- **vs Jamba (AI21)**：同属线性/Softmax 混合架构方向，Jamba 混合 Mamba（SSM）+ Attention，MiniMax 混合 Lightning Attention + Softmax Attention；不同的次二次注意力选择。
- **vs 标准线性注意力**：Lightning Attention 是线性注意力的工程优化版本，解决了纯线性注意力在实践中的性能问题。

## 对本综述的启示
- MiniMax-01 是 Token Mixer 维度最具创新性的模型之一：验证了线性注意力在超大规模模型中的可行性
- 7:1 混合模式展示了 Token Mixer 的"异构层"设计趋势——不同层可以使用不同的注意力机制
- 超高基频 RoPE + 半维度应用是 Position Encoding 的有趣变体
- 在综述中可将其与 Mamba/SSM 混合架构（如 Jamba）对比讨论，代表"次二次注意力"在 LLM 中的实践
- 在六维度框架中定位：Lightning+Softmax 混合 (Token Mixer) + MoE-Top2 (Channel Mixer) + RMSNorm (Norm, 推测) + RoPE-10M-半维 (PE) + Pre-Norm Residual (Residual) + 7:1 非均匀层模式 (Module Seq)
