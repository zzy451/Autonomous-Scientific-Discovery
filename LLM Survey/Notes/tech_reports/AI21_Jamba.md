# AI21 Labs - Jamba 架构分析

## 基本信息
- 论文标题：Jamba: A Hybrid Transformer-Mamba Language Model
- 参数量：52B 总参数 / 12B 激活参数（MoE）
- 层数：混合层设计
- 上下文长度：256K tokens
- 发布时间：2024.03
- arxiv：2403.19887

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Mamba + Attention 交替（~7:1） | 每8层中1层GQA注意力+7层Mamba SSM | **首个大规模Transformer-SSM混合架构** |
| Channel Mixer | MoE（部分层） | 16专家选2，部分Mamba层叠加MoE | Mamba+MoE双重稀疏 |
| Normalization | RMSNorm | Pre-Norm | 标准配置 |
| Position Encoding | RoPE（仅注意力层） | Mamba层无需位置编码 | SSM天然具有位置感知 |
| Residual Connection | 标准残差 | 跨类型层（Mamba/Attention）统一残差流 | 异构层间的残差兼容 |
| Module Sequence | Pre-Norm + 异构层交替 | Mamba/Attention/MoE 三种模块灵活组合 | **非均匀层设计的先驱** |

## 关键架构创新
1. **Transformer-Mamba 混合比例**：7:1（SSM:Attention）已被后续工作（MiniMax-01 等）反复验证为鲁棒的默认比例
2. **三重混合**：首次将 Transformer + SSM + MoE 三种技术在同一模型中组合
3. **256K 上下文单 GPU 部署**：KV cache 仅在 1/8 的注意力层产生，相比纯 Transformer 节省约 87.5% 的 KV cache 内存
4. **推理效率**：Mamba 层推理时状态大小恒定，不随序列长度增长

## 对本综述的启示
- Jamba 证明了混合架构的可行性，是 Section 1.8 (Hybrid Architectures) 的核心案例
- 7:1 混合比例为后续 MiniMax-01、Nemotron-H 等提供了参考基线
- 架构设计从"选择最佳单一 Token Mixer"转向"组合多种 Token Mixer 的最优策略"
