# Nvidia - Nemotron 系列架构分析

## 基本信息

### Nemotron-4 340B (2024)
- 参数量：340B（Dense）
- 上下文长度：4,096 tokens
- 训练数据量：9T tokens
- 发布时间：2024 年 6 月
- 特点：标准 Decoder-only Transformer，GQA + RoPE + Squared ReLU

### Nemotron 3 Nano (2025)
- 论文标题：Nemotron 3 Nano Technical Report
- 参数量：31.6B 总参数 / 3.2B 激活参数（MoE）
- 上下文长度：1M tokens
- 训练数据量：25T tokens
- 发布时间：2025 年 12 月
- 特点：Hybrid Mamba-Transformer MoE

## 六维度架构选择（以 Nemotron 3 Nano 为主）

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | 混合 Mamba-2 + Self-Attention | 以 Mamba-2 层为主，穿插少量 Self-Attention 层；Mamba-2 仅需恒定状态，无需线性增长的 KV cache | 首个大规模验证 Mamba-Transformer 混合架构的 MoE 模型 |
| Channel Mixer | Granular MoE | 细粒度 MoE 设计，带可学习 MLP 路由器；MoE 层与 Mamba-2/Attention 层交替 | 将 MoE 与 SSM 混合架构结合 |
| Normalization | 未明确公开（推测 RMSNorm） | — | — |
| Position Encoding | RoPE（Attention 层）/ 无（Mamba-2 层） | Mamba-2 层通过循环状态隐式编码位置信息 | Mamba 层天然支持长序列，无需位置编码 |
| Residual Connection | Pre-Norm Residual（推测） | — | — |
| Module Sequence | 混合序列：Mamba-2 层 + Self-Attention 层 + MoE 层 | 非均匀的层间模式，Mamba-2 层占主导 | 三种层类型的异构混合 |

### Nemotron-4 340B 的六维度

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped Query Attention (GQA) | 标准 GQA | 标准做法 |
| Channel Mixer | Dense FFN (Squared ReLU) | 使用 Squared ReLU 激活函数（而非 SwiGLU） | Squared ReLU 是少数非 GLU 变体的选择 |
| Normalization | 未明确（推测 RMSNorm/LayerNorm） | — | — |
| Position Encoding | RoPE | 旋转位置编码 | 标准做法 |
| Residual Connection | Pre-Norm Residual | 无 bias，无 dropout | 标准做法 |
| Module Sequence | 标准 Pre-Norm | — | 标准做法 |

## 关键架构创新

1. **Mamba-Transformer 混合架构（Nemotron 3 Nano）**：核心创新。以 Mamba-2（SSM）层为主体，穿插少量 Self-Attention 层。Mamba-2 层仅需恒定大小的循环状态（constant state），无需线性增长的 KV cache，使得推理吞吐量大幅提升。这与 MiniMax-01 的 Lightning Attention + Softmax 混合方向不同——Nemotron 选择 SSM 而非线性注意力作为次二次复杂度组件。

2. **Multi-Token Prediction (MTP)**：借鉴 DeepSeek-V3 的思路，在训练时预测多个未来 token，提供更丰富的训练信号并鼓励模型进行规划。

3. **Squared ReLU（Nemotron-4 340B）**：在 MLP 层使用 Squared ReLU 而非主流的 SwiGLU，是 Channel Mixer 维度的少数派选择。

4. **SSM + MoE 结合**：首次在大规模模型中同时使用 Mamba（SSM）和 MoE，实现三重效率增益：SSM 减少 KV cache、MoE 减少激活参数、两者协同降低推理成本。

5. **百万级原生上下文**：Nemotron 3 Nano 支持 1M token 原生上下文，得益于 Mamba-2 层的线性复杂度。

## 与前代/同期模型对比

- **vs DeepSeek-V3**：Nemotron 3 Nano 使用 Mamba+Attention 混合 vs DeepSeek 的纯 MLA；两者都使用 MoE 和 MTP；Nemotron 上下文 1M vs DeepSeek 128K。
- **vs MiniMax-01**：两者都是"次二次 + Softmax"混合架构，但 Nemotron 用 Mamba-2（SSM）而 MiniMax 用 Lightning Attention（线性注意力），代表两条不同的次二次注意力路线。
- **vs Jamba (AI21)**：同属 Mamba-Transformer 混合架构方向，但 Nemotron 进一步引入 MoE。
- **vs Llama 3 405B / Nemotron-4 340B**：从纯 Transformer Dense 架构演进为 Mamba+Transformer+MoE 三重混合。

## 对本综述的启示
- Nemotron 系列展示了从标准 Transformer（340B）到 Mamba-Transformer 混合 MoE（3 Nano）的架构演进路径
- Mamba-Transformer 混合是 Token Mixer 维度的重要替代方案，与 Linear Attention 混合（MiniMax-01）形成两条次二次注意力的工业实践路线
- Squared ReLU 是 Channel Mixer 维度中非 GLU 激活函数的少数派代表
- 在六维度框架中定位（Nemotron 3 Nano）：Mamba-2+Attention (Token Mixer) + Granular MoE (Channel Mixer) + RMSNorm (Norm, 推测) + RoPE/SSM-implicit (PE) + Pre-Norm Residual (Residual, 推测) + 异构混合层序列 (Module Seq)
