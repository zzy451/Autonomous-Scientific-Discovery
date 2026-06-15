# Meta - Llama 2 架构分析

## 基本信息
- 论文：Llama 2: Open Foundation and Fine-Tuned Chat Models
- arXiv: 2307.09288
- 参数量：7B / 13B / 70B
- 层数：32 (7B) / 40 (13B) / 80 (70B)
- 隐藏维度：4096 (7B) / 5120 (13B) / 8192 (70B)
- 注意力头数：32 (7B) / 40 (13B) / 64 (70B)
- 发布时间：2023年7月

## 六维度架构选择
| 维度 | 具体选择 | 创新点/说明 |
|------|----------|-------------|
| Token Mixer | Multi-Head Attention (7B); Grouped-Query Attention/GQA (13B, 70B) | 70B使用GQA (8个KV头)，提升推理效率 |
| Channel Mixer | SwiGLU FFN | 中间维度约为 hidden_dim * 8/3，如7B为11008 |
| Normalization | RMSNorm (Pre-Norm) | 每个子层前应用RMSNorm |
| Position Encoding | RoPE (Rotary Position Embedding) | 旋转位置编码，支持相对位置建模 |
| Residual Connection | Pre-Norm Residual | 标准残差连接 + Pre-Norm |
| Module Sequence | Pre-Norm: x + Attn(Norm(x)), x + FFN(Norm(x)) | 标准串行 Attention → FFN |

## 特殊创新
- 相比Llama 1，训练数据增加40%（2万亿token）
- 上下文长度从2048扩展到4096
- 大模型(34B/70B)引入GQA以优化推理
