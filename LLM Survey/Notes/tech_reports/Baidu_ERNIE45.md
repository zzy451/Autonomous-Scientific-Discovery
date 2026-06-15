# Baidu - ERNIE 4.5 架构分析

## 基本信息
- 论文标题：ERNIE 4.5 Technical Report（Baidu 官方博客发布）
- 参数量：旗舰版 ERNIE-4.5-300B-A47B：300B 总参数/47B 激活；小版本 ERNIE-4.5-21B-A3B：21B 总参数/3B 激活
- 层数：ERNIE-4.5-300B-A47B：54 层
- 隐藏维度：未明确公开
- 注意力头数：未明确公开（使用 GQA）
- 上下文长度：未明确公开
- 训练数据量：未明确公开
- 发布时间：2025 年 6 月（开源）
- 论文链接：无正式 arXiv 论文（通过 Baidu 官方博客和 HuggingFace 发布）
- 模型家族：10 个变体，包含纯文本和多模态版本

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped Query Attention (GQA) | 使用 GQA 压缩 KV 头 | 标准做法 |
| Channel Mixer | 异构 MoE (Heterogeneous MoE) | 300B 版：64 个专家/层，Top-8 路由，47B 激活参数；21B 版：64 个专家/层，Top-6 路由，3B 激活参数；模态隔离路由：文本和视觉使用独立专家 + 共享专家 | 异构 MoE + 模态隔离路由是核心创新 |
| Normalization | 未明确公开（推测 RMSNorm） | — | — |
| Position Encoding | 未明确公开（推测 RoPE） | — | — |
| Residual Connection | 未明确公开（推测 Pre-Norm） | — | — |
| Module Sequence | 未明确公开（推测标准 Pre-Norm） | — | — |

## 关键架构创新

1. **异构 MoE（Heterogeneous MoE）**：核心创新。MoE 层中的专家不是同构的，而是针对不同模态（文本、视觉）设计了专用专家和共享专家。模态隔离路由将不同类型的数据导向专门的处理路径。

2. **模态隔离路由（Modality-Isolated Routing）**：文本 token 和视觉 token 被路由到不同的专家子集，避免模态间的干扰。同时保留共享专家处理跨模态通用模式。

3. **多模态异构预训练**：从预训练阶段就同时在文本和视觉数据上联合训练，而非先训练文本模型再适配视觉。

4. **大规模专家配置**：64 个专家/层是较大的专家数量（介于 Mixtral 的 8 个和 DeepSeek 的 256 个之间），Top-8 路由提供丰富的专家组合。

5. **全尺寸家族**：10 个变体覆盖从 3B 激活到 47B 激活的多个规模，包含纯文本和多模态版本。

## 与前代/同期模型对比

- **vs ERNIE 3.0/4.0**：从闭源转向开源；从 Dense 架构转向 MoE；引入异构 MoE 和模态隔离路由。
- **vs DeepSeek-V3**：ERNIE 4.5 的 64 专家 vs DeepSeek 的 256 专家；ERNIE 的异构 MoE（模态专用）vs DeepSeek 的同构 MoE。
- **vs Llama 4 Maverick**：两者都是大规模 MoE + 多模态。Llama 4 使用 128 专家 + iRoPE；ERNIE 4.5 使用 64 专家 + 模态隔离路由。
- **vs Mixtral 8x7B**：ERNIE 4.5 的专家数量（64）远多于 Mixtral（8），且引入异构设计。

## 对本综述的启示
- 异构 MoE 是 Channel Mixer 维度的重要创新方向，打破了"所有专家同构"的假设
- 模态隔离路由展示了 MoE 路由策略与多模态设计的交叉
- 无正式 arXiv 论文限制了架构细节的精确分析
- 在六维度框架中定位：GQA (Token Mixer) + Heterogeneous MoE (Channel Mixer) + RMSNorm (Norm, 推测) + RoPE (PE, 推测) + Pre-Norm Residual (Residual, 推测) + Standard Pre-Norm Sequence (Module Seq, 推测)
