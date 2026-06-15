# 大厂技术报告清单

| 序号 | 公司 | 模型 | 论文标题 | arXiv ID | 年份 | 架构概要 | 笔记链接 | 状态 |
|------|------|------|----------|----------|------|----------|----------|------|
| 1 | DeepSeek | DeepSeek-V2 | DeepSeek-V2: A Strong, Economical, and Efficient MoE Language Model | 2405.04434 | 2024.05 | MLA + DeepSeekMoE, 236B/21B active | [笔记](Notes/tech_reports/DeepSeek_V2.md) | 已读 |
| 2 | DeepSeek | DeepSeek-V3 | DeepSeek-V3 Technical Report | 2412.19437 | 2024.12 | MLA + DeepSeekMoE, 671B/37B active, Aux-loss-free balancing, MTP | [笔记](Notes/tech_reports/DeepSeek_V3.md) | 已读 |
| 3 | DeepSeek | DeepSeek-R1 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | 2501.12948 | 2025.01 | 基于V3架构, GRPO强化学习训练范式 | [笔记](Notes/tech_reports/DeepSeek_R1.md) | 已读 |
| 4 | Meta | Llama 3 | The Llama 3 Herd of Models | 2407.21783 | 2024.07 | Dense Transformer, GQA, RoPE(base=500k), RMSNorm, SwiGLU | [笔记](Notes/tech_reports/Meta_Llama3.md) | 已读 |
| 5 | Meta | Llama 4 | The Llama 4 Herd (blog/community) | 2601.11659 | 2025.04 | MoE, iRoPE(RoPE+NoPE交替), Early Fusion多模态 | [笔记](Notes/tech_reports/Meta_Llama4.md) | 已读 |
| 6 | Alibaba | Qwen2.5 | Qwen2.5 Technical Report | 2412.15115 | 2024.12 | Dense + MoE variants, GQA, RoPE, SwiGLU, 18T tokens | [笔记](Notes/tech_reports/Alibaba_Qwen25.md) | 已读 |
| 7 | Alibaba | Qwen3 | Qwen3 Technical Report | 2505.09388 | 2025.05 | Dense+MoE(235B/22B), GQA, QK-Norm, 无shared expert, 128专家选8, 36T tokens | [笔记](Notes/tech_reports/Alibaba_Qwen3.md) | 已读 |
| 8 | Moonshot AI | Kimi k1.5 | Kimi k1.5: Scaling Reinforcement Learning with LLMs | 2501.12599 | 2025.01 | RL训练范式为主, Long-CoT, Long2Short, 128k上下文RL | [笔记](Notes/tech_reports/Moonshot_Kimi_k15.md) | 已读 |
| 9 | Google | Gemma 2 | Gemma 2: Improving Open Language Models at a Practical Size | 2408.00118 | 2024.06 | 交替local/global attention, GQA, Logit soft-capping, 额外RMSNorm, RoPE, GeGLU | [笔记](Notes/tech_reports/Google_Gemma2.md) | 已读 |
| 10 | Google | Gemma 3 | Gemma 3 Technical Report | 2503.19786 | 2025.03 | 5:1 local/global attention, sliding window 1024, RoPE(base rescaling), GQA | [笔记](Notes/tech_reports/Google_Gemma3.md) | 已读 |
| 11 | Mistral AI | Mixtral 8x7B | Mixtral of Experts | 2401.04088 | 2024.01 | SMoE 8专家选2, 47B/13B active, GQA, RoPE, SwiGLU, 32k context | [笔记](Notes/tech_reports/Mistral_Mixtral.md) | 已读 |
| 12 | Mistral AI | Mistral 7B | Mistral 7B | 2310.06825 | 2023.10 | Dense, Sliding Window Attention, GQA, RoPE, SwiGLU, RMSNorm | [笔记](Notes/tech_reports/Mistral_7B.md) | 已读 |
| 13 | Zhipu AI | GLM-4 | ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools | 2406.12793 | 2024.06 | Dense Transformer, GQA, RoPE, FlashAttention, 128k context | [笔记](Notes/tech_reports/Zhipu_GLM4.md) | 已读 |
| 14 | 01.AI | Yi-Lightning | Yi-Lightning Technical Report | 2412.01253 | 2024.12 | MoE, 细粒度expert分割, hybrid local+global attention, cross-layer KV sharing | [笔记](Notes/tech_reports/01AI_YiLightning.md) | 已读 |
| 15 | Tencent | Hunyuan-Large | Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters | 2411.02265 | 2024.11 | MoE 389B/52B active, shared expert + Top-K routing, GQA + CLA, expert-specific LR | [笔记](Notes/tech_reports/Tencent_Hunyuan.md) | 已读 |
| 16 | MiniMax | MiniMax-01 | MiniMax-01: Scaling Foundation Models with Lightning Attention | 2501.08313 | 2025.01 | Lightning Attention(线性) + Softmax混合(7:1), MoE 456B/45.9B active, 4M context | [笔记](Notes/tech_reports/MiniMax_01.md) | 已读 |
| 17 | Microsoft | Phi-4 | Phi-4 Technical Report | 2412.08905 | 2024.12 | 14B dense, 基于Phi-3架构微调, 合成数据为主 | [笔记](Notes/tech_reports/Microsoft_Phi4.md) | 已读 |
| 18 | AI2 | OLMo 2 | 2 OLMo 2 Furious | 2501.00656 | 2025.01 | Dense autoregressive, 7B/13B/32B, 训练稳定性改进 | [笔记](Notes/tech_reports/AI2_OLMo2.md) | 已读 |
| 19 | Baichuan | Baichuan-M1 | Baichuan-M1: Pushing the Medical Capability of LLMs | 2502.12671 | 2025.02 | Pre-norm RMSNorm, SwiGLU, RoPE, hybrid global+sliding window attention, temporal short conv on KV | [笔记](Notes/tech_reports/Baichuan_M1.md) | 已读 |
| 20 | Baidu | ERNIE 4.5 | ERNIE 4.5 Technical Report | 2506.xxxxx | 2025.06 | 异构MoE(模态隔离路由), 424B/47B active, 2D RoPE(视觉), FP8训练 | [笔记](Notes/tech_reports/Baidu_ERNIE45.md) | 已读 |
| 21 | Huawei | PanGu-Sigma | PanGu-Sigma: Towards Trillion Parameter Language Model with Sparse Heterogeneous Computing | 2303.10845 | 2023.03 | 1.085T稀疏模型, Random Routed Experts, MindSpore+Ascend | [笔记](Notes/tech_reports/Huawei_PanGu.md) | 已读 |

## 架构演进趋势总结

### 主要发现
1. **MoE成为主流**: DeepSeek-V3, Llama 4, Qwen3, Yi-Lightning, Hunyuan-Large, MiniMax-01, ERNIE 4.5 均采用MoE
2. **注意力机制多样化**: MLA(DeepSeek), GQA(几乎所有), Lightning Attention(MiniMax), iRoPE(Llama 4), Sliding Window混合(Gemma/Mistral)
3. **RMSNorm + Pre-Norm 成为标配**: 几乎所有2024-2025模型均采用
4. **RoPE主导位置编码**: 除Llama 4的iRoPE(RoPE+NoPE交替)外, 其余均用标准RoPE
5. **SwiGLU/GeGLU成为标准FFN激活**: 几乎完全取代了ReLU和GELU
6. **上下文长度急剧增长**: 从32k(Mixtral) -> 128k(Llama3/GLM4) -> 256k(Hunyuan) -> 1M(Qwen2.5-1M) -> 4M(MiniMax-01) -> 10M(Llama4 Scout)

### 各模型架构要素对比表

| 模型 | Token Mixer | Channel Mixer | Normalization | Position Encoding | Residual | Module Seq |
|------|-------------|---------------|---------------|-------------------|----------|------------|
| DeepSeek-V3 | MLA (latent KV压缩) | DeepSeekMoE (细粒度expert) | RMSNorm | RoPE | 标准残差 + mHC(V3改进) | Pre-Norm |
| Llama 3 | GQA | Dense SwiGLU FFN | RMSNorm | RoPE (base=500k) | 标准残差 | Pre-Norm |
| Llama 4 | GQA + MoE routing | MoE | RMSNorm | iRoPE (RoPE+NoPE 3:1交替) | 标准残差 | Pre-Norm |
| Qwen3 | GQA + QK-Norm | MoE (128专家选8, 无shared) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Gemma 2 | GQA + 交替local/global attn | Dense GeGLU FFN | RMSNorm (pre+post FFN额外层) | RoPE | 标准残差 | Pre-Norm |
| Gemma 3 | GQA + 5:1 local/global(SW=1024) | Dense GeGLU FFN | RMSNorm | RoPE (rescaled, global用1M base) | 标准残差 | Pre-Norm |
| Mixtral 8x7B | GQA | SMoE (8专家选2) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Mistral 7B | GQA + Sliding Window Attn | Dense SwiGLU FFN | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| GLM-4 | GQA + FlashAttention | Dense FFN | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Yi-Lightning | hybrid local+global attn | MoE (细粒度expert分割) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Hunyuan-Large | GQA + CLA (cross-layer attn) | MoE (shared + Top-K) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| MiniMax-01 | Lightning Attn + Softmax (7:1混合) | MoE (32专家) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Baichuan-M1 | hybrid global+sliding window, temporal conv on KV | Dense SwiGLU FFN | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| ERNIE 4.5 | Attention (模态隔离路由) | 异构MoE | RMSNorm | RoPE + 2D RoPE(视觉) | 标准残差 | Pre-Norm |
