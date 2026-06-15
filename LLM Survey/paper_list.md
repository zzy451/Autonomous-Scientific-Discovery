# 总论文清单 — LLM Architecture in One Block: A Survey

> 最后更新：2026-04-06
> 总计：308 篇笔记

## 统计概览

| 类别 | 笔记数 |
|------|--------|
| Token Mixer | 92 |
| Channel Mixer | 41 |
| Normalization | 35 |
| Position Encoding | 40 |
| Residual Connection | 31 |
| Module Sequence | 47 |
| 大厂技术报告 | 22 |
| **总计** | **308** |

---

## 1. Token Mixer (92 篇)

### 1.1 Dot-Product Attention (标准注意力)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 1 | Attention Is All You Need | Vaswani et al. | 2017 | NeurIPS | Dot Self-Attention | 已读 |
| 2 | Gated Attention for Large Language Models | Qiu et al. | 2025 | arXiv:2505.06708 | Gated Self-Attention | 已读 |

### 1.2 KV Cache 优化 (Attention Head Sharing)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 3 | Fast Transformer Decoding: One Write-Head is All You Need | Shazeer | 2019 | arXiv:1911.02150 | Multi-Query Attention (MQA) | 已读 |
| 4 | GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | Ainslie et al. | 2023 | EMNLP (arXiv:2305.13245) | Grouped-Query Attention (GQA) | 已读 |
| 5 | DeepSeek-V2: A Strong, Economical, and Efficient MoE LM | DeepSeek-AI | 2024 | arXiv:2405.04434 | Multi-Head Latent Attention (MLA) | 已读 |

### 1.3 Sparse Attention (稀疏注意力)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 6 | Longformer: The Long-Document Transformer | Beltagy et al. | 2020 | arXiv:2004.05150 | Sliding Window + Global | 已读 |
| 7 | Mistral 7B | Jiang et al. | 2023 | arXiv:2310.06825 | Sliding Window Attention (SWA) | 已读 |
| 8 | Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention | Yuan et al. | 2025 | ACL (arXiv:2502.11089) | NSA | 已读 |
| 9 | MoBA: Mixture of Block Attention for Long-Context LLMs | Lu et al. | 2025 | arXiv:2502.13189 | Block Sparse | 已读 |

### 1.4 Linear Attention (线性注意力)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 10 | Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention | Katharopoulos et al. | 2020 | ICML (arXiv:2006.16236) | Kernel Linear Attention | 新增 |
| 11 | Reformer: The Efficient Transformer | Kitaev et al. | 2020 | ICLR (arXiv:2001.04451) | LSH Attention | 已读 |
| 12 | Linformer: Self-Attention with Linear Complexity | Wang et al. | 2020 | arXiv:2006.04768 | Low-rank Projection | 已读 |
| 13 | Rethinking Attention with Performers | Choromanski et al. | 2020 | ICLR 2021 (arXiv:2009.14794) | Random Feature Attention | 已读 |
| 14 | Based: Simple Linear Attention Language Models Balance the Recall-Throughput Tradeoff | Arora et al. | 2024 | arXiv:2402.18668 | Taylor Expansion Linear Attn | 已读 |
| 14b | Gated Linear Attention Transformers with Hardware-Efficient Training | Yang et al. | 2024 | ICML (arXiv:2312.06635) | Gated Linear Attention (GLA) | 已读 |
| 14c | Parallelizing Linear Transformers with the Delta Rule over Sequence Length | Yang et al. | 2024 | NeurIPS (arXiv:2406.06484) | DeltaNet | 已读 |
| 14d | HGRN2: Gated Linear RNNs with State Expansion | Qin et al. | 2024 | arXiv:2404.07904 | HGRN2 | 已读 |
| 14e | Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths | Qin et al. | 2024 | arXiv:2401.04658 | Lightning Attention-2 | 已读 |

### 1.5 Attention with Negative Weights (负权重注意力)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 15 | Differential Transformer | Ye et al. | 2024 | arXiv:2410.05258 | Differential Attention | 已读 |
| 16 | More Expressive Attention with Negative Weights (CogAttn) | Lv et al. | 2024 | arXiv:2411.07176 | Cog Attention | 已读 |

### 1.6 Different Activation (不同激活函数)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 17 | Theory, Analysis, and Best Practices for Sigmoid Self-Attention | Ramapuram et al. | 2024 | arXiv:2409.04431 | Sigmoid Attention | 已读 |

### 1.7 RNN-Like / SSM (循环式/状态空间模型)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 18 | Efficiently Modeling Long Sequences with Structured State Spaces (S4) | Gu et al. | 2021 | ICLR 2022 (arXiv:2111.00396) | SSM Foundation | 新增 |
| 19 | RWKV: Reinventing RNNs for the Transformer Era | Peng et al. | 2023 | arXiv:2305.13048 | Linear RNN | 已读 |
| 20 | Retentive Network: A Successor to Transformer for Large Language Models | Sun et al. | 2023 | arXiv:2307.08621 | Retention | 已读 |
| 21 | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | Gu, Dao | 2024 | COLM (arXiv:2312.00752) | Selective SSM | 已读 |
| 22 | Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality (Mamba-2) | Dao, Gu | 2024 | ICML (arXiv:2405.21060) | SSD / Mamba-2 | 已读 |
| 23 | Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence | Peng et al. | 2024 | arXiv:2404.05892 | RWKV-5/6 | 已读 |
| 24 | Gated Delta Networks: Improving Mamba2 with Delta Rule | Yang et al. | 2024 | arXiv:2412.06464 | Gated Delta Networks | 已读 |
| 24b | RWKV-7 "Goose" with Expressive Dynamic State Evolution | Peng et al. | 2025 | arXiv:2503.14456 | RWKV-7 / Delta Rule | 已读 |
### 1.8 Hybrid Architectures (混合架构)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 25 | Jamba: A Hybrid Transformer-Mamba Language Model | Lieber et al. | 2024 | arXiv:2403.19887 | Hybrid Transformer-SSM | 已读 |

### 1.9 Hardware-Efficient Attention (硬件高效注意力)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 26 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | Dao et al. | 2022 | NeurIPS (arXiv:2205.14135) | IO-Aware Attention | 已读 |
| 27 | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | Dao | 2023 | arXiv:2307.08691 | FlashAttention-2 | 已读 |
| 28 | FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision | Shah et al. | 2024 | arXiv:2407.08608 | FlashAttention-3 (Hopper) | 新增 |
| 28b | Efficient Memory Management for LLM Serving with PagedAttention | Kwon et al. | 2023 | SOSP (arXiv:2309.06180) | PagedAttention / vLLM | 已读 |

### 1.10 Lightning Attention / 大规模线性注意力工业应用

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子类别 | 状态 |
|------|----------|------|------|------|--------|------|
| 29 | MiniMax-01: Scaling Foundation Models with Lightning Attention | MiniMax Team | 2025 | arXiv:2501.08313 | Lightning Attn(线性)+Softmax 7:1混合, 456B MoE, 4M context | 新增 |

### 1.11 Surveys

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 状态 |
|------|----------|------|------|------|------|
| 30 | Efficient Transformers: A Survey | Tay et al. | 2020 | arXiv:2009.06732 | 已收录 |
| 31 | Efficient Attention Mechanisms for Large Language Models: A Survey | (Authors TBD) | 2025 | arXiv:2507.19595 | 新增 |

### 1.12 工业模型 Token Mixer 选型汇总

| 模型 | Token Mixer 方案 | arXiv ID | 年份 |
|------|------------------|----------|------|
| DeepSeek-V2/V3 | MLA (低秩联合KV压缩, KV cache减少93.3%) | 2405.04434 / 2412.19437 | 2024 |
| Llama 3 | GQA (8 KV heads) | 2407.21783 | 2024 |
| Llama 4 | GQA + iRoPE架构 (RoPE+NoPE 3:1交替) | 2601.11659 | 2025 |
| Qwen2.5 | GQA | 2412.15115 | 2024 |
| Qwen3 | GQA + QK-Norm (训练稳定性) | 2505.09388 | 2025 |
| Gemma 2 | GQA + 交替local/global attn + Logit soft-capping | 2408.00118 | 2024 |
| Gemma 3 | GQA + 5:1 local(SW=1024)/global交替 + RoPE base差异化 | 2503.19786 | 2025 |
| Mistral 7B | GQA + Sliding Window Attention | 2310.06825 | 2023 |
| Mixtral 8x7B | GQA + SMoE routing | 2401.04088 | 2024 |
| GLM-4 | GQA + FlashAttention | 2406.12793 | 2024 |
| Yi-Lightning | hybrid local+global attn + cross-layer KV cache sharing | 2412.01253 | 2024 |
| Hunyuan-Large | GQA + Cross-Layer Attention (CLA) | 2411.02265 | 2024 |
| MiniMax-01 | Lightning Attn(线性) + Softmax 7:1混合 | 2501.08313 | 2025 |
| Baichuan-M1 | hybrid global+sliding window + temporal short conv on KV | 2502.12671 | 2025 |
| OLMo 2 | GQA | 2501.00656 | 2025 |

---

## 2. Channel Mixer (41 篇)

### 2.A FFN 基础与激活函数

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 领域 | 状态 |
|------|----------|------|------|------|------|------|
| A1 | Language Modeling with Gated Convolutional Networks | Dauphin et al. | 2017 | ICML 2017 | [非LLM] GLU 原始论文 | 已完成 |
| A2 | Deep Learning Using Rectified Linear Units (ReLU) | Agarap | 2018 | arXiv:1803.08375 | 激活函数 | 已引用 |
| A3 | Gaussian Error Linear Units (GELUs) | Hendrycks & Gimpel | 2016 | arXiv:1606.08415 | 激活函数 | 已引用 |
| A4 | GLU Variants Improve Transformer | Shazeer | 2020 | arXiv:2002.05202 | SwiGLU/GLU变体 | 已引用 |
| A5 | ReLU^2 Wins: Discovering Efficient Activation Functions for Sparse LLMs | Zhang et al. | 2024 | arXiv:2402.03804 | 激活稀疏性 | 已完成 |
| A6 | Searching for Activation Functions (Swish) | Ramachandran et al. | 2017 | arXiv:1710.05941 | [非LLM] Swish/SiLU激活函数 | 已完成 |

### 2.B Mixture of Experts (MoE) — 基础与路由策略

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 领域 | 状态 |
|------|----------|------|------|------|------|------|
| B1 | Adaptive Mixtures of Local Experts | Jacobs, Jordan, Nowlan, Hinton | 1991 | Neural Computation | [非LLM] MoE 开山之作 | 已完成 |
| B2 | Outrageously Large Neural Networks: The Sparsely-Gated MoE Layer | Shazeer et al. | 2017 | ICLR 2017 | 稀疏门控 MoE | 已完成 |
| B3 | GShard: Scaling Giant Models with Conditional Computation | Lepikhin et al. | 2021 | ICLR 2021 | 大规模 MoE + Top-2 路由 | 已完成 |
| B4 | Switch Transformers: Scaling to Trillion Parameter Models | Fedus et al. | 2022 | JMLR 2022 | Top-1 路由 MoE | 已完成 |
| B5 | ST-MoE: Designing Stable and Transferable Sparse Expert Models | Zoph et al. | 2022 | arXiv:2202.08906 | MoE 训练稳定性 | 已完成 |
| B6 | Mixture-of-Experts with Expert Choice Routing | Zhou et al. | 2022 | NeurIPS 2022 | Expert Choice 路由 | 已完成 |
| B7 | Auxiliary-Loss-Free Load Balancing Strategy for MoE | Wang et al. | 2024 | arXiv:2408.15664 | 无辅助损失负载均衡 | 已完成 |

### 2.C MoE 应用模型（2024）

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 领域 | 状态 |
|------|----------|------|------|------|------|------|
| C1 | Mixtral of Experts | Jiang et al. (Mistral AI) | 2024 | arXiv:2401.04088 | 开源 MoE LLM | 已完成 |
| C2 | DeepSeekMoE: Towards Ultimate Expert Specialization | Dai et al. | 2024 | ACL 2024 | 细粒度+共享专家 MoE | 已完成 |
| C3 | DeepSeek-V2: A Strong, Economical, and Efficient MoE LM | DeepSeek-AI | 2024 | arXiv:2405.04434 | MoE+MLA | 已完成 |
| C4 | DeepSeek-V3 Technical Report | Liu et al. | 2024 | arXiv:2412.19437 | MoE 工业级实践 | 已引用 |
| C5 | DBRX: An Open General-Purpose LLM | Databricks | 2024 | arXiv:2404.14219 | 16选4 细粒度 MoE | 已完成 |
| C6 | OLMoE: Open Mixture-of-Experts Language Models | Muennighoff et al. (Ai2) | 2024 | arXiv:2409.02060 | 完全开源 MoE | 已完成 |
| C7 | Skywork-MoE: Training Techniques for MoE LLMs | Wei et al. (Kunlun) | 2024 | arXiv:2406.06563 | 门控归一化+自适应损失 | 已完成 |
| C8 | Grok-1 | xAI | 2024 | x.ai / GitHub | 314B MoE 开源 | 已完成 |
| C9 | Jamba: A Hybrid Transformer-Mamba Language Model | Lieber et al. (AI21) | 2024 | arXiv:2403.19887 | Transformer+Mamba+MoE | 已完成 |
### 2.D 条件计算与 FFN 变体

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 领域 | 状态 |
|------|----------|------|------|------|------|------|
| D1 | Mixture-of-Depths: Dynamically Allocating Compute | Raposo et al. (DeepMind) | 2024 | arXiv:2404.02258 | 动态计算分配 | 已完成 |
| D2 | Deja Vu: Contextual Sparsity for Efficient LLMs | Liu et al. | 2023 | ICML 2023 | FFN 上下文稀疏性 | 已完成 |
| D3 | MoEfication: Transformer FFN Layers are Mixtures of Experts | Zhang et al. | 2022 | ACL Findings 2022 | Dense→MoE 转换 | 已完成 |
| D4 | KAN: Kolmogorov-Arnold Networks | Liu et al. | 2024 | arXiv:2404.19756 | FFN 替代方案 | 已完成 |
| D5 | Duo-LLM: A Framework for Studying Adaptive Computation in LLMs | - | 2024 | arXiv:2410.10846 | 动态 FFN | 已完成 |

### 2.E MoE 应用模型（2025）

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 领域 | 状态 |
|------|----------|------|------|------|------|------|
| E1 | Qwen3 Technical Report | Qwen Team (Alibaba) | 2025 | arXiv:2505.09388 | MoE: 128专家选8, 无shared expert, global-batch均衡 | 新增 |
| E2 | Llama 4 (community notes) | Meta AI | 2025 | arXiv:2601.11659 | MoE + 原生多模态早融合 | 新增 |
| E3 | Hunyuan-Large: Open-Source MoE with 52B Active Params | Tencent | 2024 | arXiv:2411.02265 | MoE: shared expert + Top-K, 389B/52B, expert-specific LR | 新增 |
| E4 | MiniMax-01: Scaling Foundation Models with Lightning Attention | MiniMax | 2025 | arXiv:2501.08313 | MoE: 32专家, 456B/45.9B active, 4M context | 新增 |
| E5 | Yi-Lightning Technical Report | 01.AI | 2024 | arXiv:2412.01253 | MoE: 细粒度expert分割, 组路由均衡 | 新增 |
| E6 | ERNIE 4.5 Technical Report | Baidu | 2025 | arXiv (2025.06) | 异构MoE: 模态隔离路由, router正交损失 | 新增 |
| E7 | GLM-4.5 Series | Zhipu AI | 2025 | - | MoE: 355B/32B active (GLM-4.5), 106B/12B (Air) | 新增 |

### 2.F MoE 综述

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 领域 | 状态 |
|------|----------|------|------|------|------|------|
| F1 | A Survey on Mixture of Experts in Large Language Models | Cai et al. | 2024 | arXiv:2407.06204 | MoE 综述 | 已检索 |

---

## 3. Normalization (35 篇)

### 3.A 基础规范化方法

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-01 | Batch Normalization: Accelerating Deep Network Training | Ioffe, Szegedy | 2015 | ICML 2015 | arXiv:1502.03167 | 已读 |
| N-02 | Layer Normalization | Ba, Kiros, Hinton | 2016 | arXiv | arXiv:1607.06450 | 已读 |
| N-03 | Instance Normalization | Ulyanov, Vedaldi, Lempitsky | 2016 | arXiv | arXiv:1607.08022 | 已读 |
| N-04 | Group Normalization | Wu, He | 2018 | ECCV 2018 | arXiv:1803.08494 | 已读 |
### 3.B Transformer 中的规范化位置与理论分析

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-05 | On Layer Normalization in the Transformer Architecture (Pre-LN vs Post-LN) | Xiong et al. | 2020 | ICML 2020 | arXiv:2002.04745 | 已读 |
| N-06 | Understanding and Improving Layer Normalization (AdaNorm) | Xu et al. | 2019 | NeurIPS 2019 | arXiv:1911.07013 | 已读 |
| N-07 | CogView: Mastering Text-to-Image via Transformers (Sandwich LayerNorm) | Ding et al. | 2021 | NeurIPS 2021 | arXiv:2105.13290 | 已读 |
| N-08 | DeepNet: Scaling Transformers to 1,000 Layers (DeepNorm) | Wang et al. | 2022 | IEEE TPAMI 2024 | arXiv:2203.00555 | 已读 |
| N-20 | Foundation Transformers (MAGNETO / Sub-LayerNorm) | Wang et al. | 2022 | arXiv | arXiv:2210.06423 | 已读 |
| N-21 | Peri-LN: Revisiting Normalization Layer in the Transformer Architecture | (2025) | 2025 | arXiv | arXiv:2501.12948 | 已读 |
| N-27 | Re-Introducing LayerNorm: Geometric Meaning, Irreversibility and a Comparative Study with RMSNorm | Gupta, Ozdemir, Anumanchipalli | 2024 | arXiv | arXiv:2409.12951 | 已读 |
| N-28 | Normalization in Attention Dynamics | Karagodin et al. | 2025 | NeurIPS 2025 | arXiv:2510.22026 | 已读 |

### 3.C 高效变体

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-09 | Root Mean Square Layer Normalization (RMSNorm) | Zhang, Sennrich | 2019 | NeurIPS 2019 | arXiv:1910.07467 | 已读 |
| N-22 | Transformers without Tears (ScaleNorm, FixNorm) | Nguyen, Salazar | 2019 | IWSLT 2019 | arXiv:1910.05895 | 已读 |
| N-23 | PowerNorm: Rethinking Batch Normalization in Transformers | Shen et al. | 2020 | ICML 2020 | arXiv:2003.07845 | 已读 |

### 3.D 注意力内部归一化

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-10 | Query-Key Normalization for Transformers (QK-Norm) | Henry et al. | 2020 | Findings of EMNLP 2020 | arXiv:2010.04245 | 已读 |
| N-24 | Differential Transformer (GroupNorm in attention heads) | Ye et al. | 2024 | arXiv | arXiv:2410.05258 | 已读 |
| N-29 | Enhanced QKNorm with the Lp norm | Lopez-Rubio, Montes-Perez, Palomo | 2026 | arXiv | arXiv:2602.05006 | 已读 |

### 3.E 条件化归一化

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-11 | Scalable Diffusion Models with Transformers (DiT, adaLN-Zero) | Peebles, Xie | 2023 | ICCV 2023 | arXiv:2212.09748 | 已读 |

### 3.F 全面归一化架构

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-25 | nGPT: Normalized Transformer with Representation Learning on the Hypersphere | Loshchilov et al. | 2024 | ICLR 2025 | arXiv:2410.01131 | 已读 |
| N-26 | Gemma 2 (Pre+Post RMSNorm) | Gemma Team, Google | 2024 | arXiv | arXiv:2408.00118 | 已读 |
### 3.G 自动化搜索归一化

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-12 | Evolving Normalization-Activation Layers (EvoNorm) | Liu et al. | 2020 | NeurIPS 2020 | arXiv:2004.02967 | 已读 |

### 3.H 无归一化方法

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-13 | Fixup Initialization: Residual Learning Without Normalization | Zhang et al. | 2019 | ICLR 2019 | arXiv:1901.09321 | 已读 |
| N-14 | T-Fixup: Improving Transformer Optimization Through Better Initialization | Huang et al. | 2020 | ICML 2020 | arXiv:2004.08249 | 已读 |
| N-15 | High-Performance Large-Scale Image Recognition Without Normalization (NF-Net, AGC) | Brock et al. | 2021 | ICML 2021 | arXiv:2102.06171 | 已读 |
| N-16 | Transformers without Normalization (Dynamic Tanh / DyT) | Zhu, Chen, He, LeCun, Liu | 2025 | CVPR 2025 | arXiv:2503.10622 | 已读 |
| N-17 | Stronger Normalization-Free Transformers (Dynamic Erf / Derf) | Chen, Lu, Zhu, Sun, Liu | 2025 | CVPR 2026 | arXiv:2503.03817 | 已读 |

### 3.I 前沿 / 开放问题

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv / DOI | 状态 |
|------|----------|------|------|------|-------------|------|
| N-18 | Derf-Muon 交互研究 (normalization-free 与优化器的耦合效应) | (2026 研究) | 2026 | 多来源 | TBD | 待读 |
| N-19 | UnitNorm: Rethinking Normalization for Transformers in Time Series | Huang, Kummerle, Zhang | 2025 | ICLR 2026 (withdrawn) | TBD | 了解 |

---

## 4. Position Encoding (40 篇)

### 4.1 已完成笔记

| # | 论文标题 | 作者 | 年份 | arXiv ID | 状态 |
|---|---------|------|------|----------|------|
| 1 | Attention Is All You Need (Sinusoidal PE) | Vaswani et al. | 2017 | 1706.03762 | 已有 |
| 2 | RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE) | Su et al. | 2021 | 2104.09864 | 已有 |
| 3 | Train Short, Test Long: ALiBi | Press, Smith, Lewis | 2022 | 2108.12409 | 已有 |
| 4 | Contextual Position Encoding (CoPE) | Golovneva et al. | 2024 | 2405.18719 | 已有 |
| 5 | The Impact of Positional Encoding on Length Generalization (NoPE) | Kazemnejad et al. | 2023 | 2305.19466 | 已有 |
| 6 | Self-Attention with Relative Position Representations | Shaw et al. | 2018 | 1803.02155 | 已完成 |
| 7 | Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context | Dai et al. | 2019 | 1901.02860 | 已完成 |
| 8 | Exploring the Limits of Transfer Learning (T5 Relative Bias) | Raffel et al. | 2020 | 1910.10683 | 已完成 |
| 9 | DeBERTa: Decoding-enhanced BERT with Disentangled Attention | He et al. | 2021 | 2006.03654 | 已完成 |
| 10 | CAPE: Encoding Relative Positions with Continuous Augmented PE | Likhomanenko et al. | 2021 | 2106.03143 | 已完成 |
| 11 | KERPLE: Kernelized Relative Positional Embedding | Chi et al. | 2022 | 2205.09921 | 已完成 |
| 12 | A Length-Extrapolatable Transformer (xPos) | Sun et al. | 2023 | 2212.10554 | 已完成 |
| 13 | Extending Context Window via Position Interpolation (PI) | Chen et al. | 2023 | 2306.15595 | 已完成 |
| 14 | YaRN: Efficient Context Window Extension | Peng et al. | 2023 | 2309.00071 | 已完成 |
| 15 | FIRE: Functional Interpolation for Relative Positions | Li et al. | 2024 | 2310.04418 | 已完成 |
| 16 | LongRoPE: Extending LLM Context Beyond 2M Tokens | Ding et al. | 2024 | 2402.13753 | 已完成 |
| 17 | Randomized Positional Encodings Boost Length Generalization | Ruoss et al. | 2023 | 2305.16843 | 已完成 |
| 18 | NTK-aware Scaled RoPE / Dynamic NTK / ABF | bloc97, emozilla | 2023 | 社区(Reddit) | 已完成 |
| 19 | Forgetting Transformer (FoX) | Lin et al. | 2025 | 2503.02130 | 已完成 |
| 20 | Stick-Breaking Attention | Rule et al. | 2025 | 2410.17980 | 已完成 |
| 21 | PoPE: Polar Position Embeddings | Gopalakrishnan et al. | 2025 | 2509.10534 | 已完成 |
### 4.2 待完成论文

| # | 论文标题 | 作者 | 年份 | arXiv ID | 子分类 | 状态 |
|---|---------|------|------|----------|--------|------|
| 22 | Convolutional Sequence to Sequence Learning | Gehring et al. | 2017 | 1705.03122 | Learned APE (最早提出) | 待处理 |
| 23 | ReRoPE (Rectified RoPE) | Su (bojone) | 2023 | kexue.fm/archives/9708 | 免微调外推 | 参考 |
| 24 | CLEX: Continuous Length Extrapolation | Chen et al. | 2024 | 2310.16450 | ODE连续外推 | 待处理 |
| 25 | LongRoPE2: Near-Lossless LLM Context Window Scaling | Microsoft | 2025 | 2502.20082 | 进化搜索+混合训练 | 待处理 |
| 26 | DroPE: Extending Context by Dropping Positional Embeddings | Gelberg et al. (Sakana AI) | 2026 | 2512.12167 | 丢弃PE扩展 | 待处理 |
| 27 | PaTH Attention: Position via Accumulating Householder Transformations | MIT-IBM Watson AI Lab | 2025 | NeurIPS 2025 | 累积Householder变换 | 待处理 |
| 28 | iRoPE — Llama 4 Architecture | Meta AI | 2025 | Llama 4 Tech Report | RoPE+NoPE交替 | 待处理 |
| 29 | Qwen2-VL (M-RoPE) | Alibaba | 2024 | 2409.12191 | 多模态RoPE | 待处理 |

---

## 5. Residual Connection (31 篇)

### 5.A 基础/奠基性工作

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子维度 | arXiv ID | 状态 |
|------|----------|------|------|------|--------|----------|------|
| F1 | Deep Residual Learning for Image Recognition | He et al. | 2016 | CVPR 2016 | Foundation | 1512.03385 | 已完成 |
| F2 | Highway Networks / Training Very Deep Networks | Srivastava, Greff, Schmidhuber | 2015 | NeurIPS 2015 | Foundation (门控跳跃) | 1505.00387 | 待处理 |
| F3 | Densely Connected Convolutional Networks (DenseNet) | Gao Huang et al. | 2017 | CVPR 2017 | Foundation (密集连接) | 1608.06993 | 待处理 |
| F4 | Deep Networks with Stochastic Depth | Gao Huang et al. | 2016 | ECCV 2016 | Foundation (随机深度) | 1603.09382 | 待处理 |

### 5.B Width (残差流宽度扩展)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子维度 | arXiv ID | 状态 |
|------|----------|------|------|------|--------|----------|------|
| W1 | Hyper-Connections | Zhu et al. | 2024 | arXiv | Width | 2409.19606 | 已完成 |
| W2 | mHC: Manifold-Constrained Hyper-Connections | Xie et al. (DeepSeek-AI) | 2025 | arXiv | Width | 2512.24880 | 已完成 |
| W3 | go-mHC: Direct Parameterization via Generalized Orthostochastic Matrices | - | 2026 | arXiv | Width | 2604.02309 | 已完成 |
| W4 | GPT-J / Parallel Attention Architecture | Wang & Komatsuzaki; Black et al. | 2021-2022 | GPT-J/NeoX | Width (并行子层) | — | 新增 |
| W5 | Residual Matrix Transformers | Brian Mak, Jeffrey Flanigan | 2025 | arXiv | Width (外积记忆矩阵) | 2506.22696 | 待处理 |

### 5.C Depth (跨层密集连接 / 自适应深度)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子维度 | arXiv ID | 状态 |
|------|----------|------|------|------|--------|----------|------|
| D1 | Cross-Layer Retrospective Retrieving via Layer Attention (MRLA) | Fang et al. | 2023 | arXiv | Depth (跨层) | 2302.03985 | 已完成 |
| D2 | DenseFormer: Enhancing Information Flow via Depth Weighted Average | Pagliardini et al. | 2024 | NeurIPS 2024 | Depth (稠密) | 2402.02622 | 已完成 |
| D3 | MUDDFormer: Breaking Residual Bottlenecks | Xiao et al. | 2025 | ICML 2025 | Depth (动态稠密) | 2502.12170 | 已完成 |
| D4 | DeepCrossAttention: Supercharging Transformer Residual Connections | Heddes et al. | 2025 | ICML 2025 | Depth (跨层注意力) | 2502.06785 | 已完成 |
| D5 | Value Residual Learning (ResFormer/SVFormer) | Zhou et al. | 2024 | ACL 2025 | Depth (值残差) | 2410.17897 | 已完成 |
| D6 | RealFormer: Transformer Likes Residual Attention | He et al. | 2020 | ACL-IJCNLP 2021 | Depth (注意力残差) | 2012.11747 | 已完成 |
| D7 | Attention Residuals (AttnRes) | Kimi Team (Moonshot AI) | 2026 | arXiv | Depth (注意力残差) | 2603.15031 | 已完成 |
| D8 | Universal Transformers | Dehghani et al. | 2019 | ICLR 2019 | Depth (自适应) | 1807.03819 | 新增 |
| D9 | Reducing Transformer Depth on Demand (LayerDrop) | Fan et al. | 2020 | ICLR 2020 | Depth (弹性深度) | 1909.11556 | 新增 |
| D10 | Depth-Adaptive Transformer | Elbayad et al. | 2020 | ICLR 2020 | Depth (早退) | 1910.10073 | 新增 |
| D11 | Mixture-of-Depths: Dynamically Allocating Compute | Raposo et al. | 2024 | arXiv | Depth (条件计算) | 2404.02258 | 新增 |
| D12 | Cross-Layer Attention (KV cache sharing) | Brandon et al. | 2024 | NeurIPS 2024 | Depth (跨层共享) | 2405.12981 | 新增 |
| D13 | YOCO: Decoder-Decoder Architectures | Yutao Sun et al. | 2024 | arXiv | Depth (跨层KV缓存复用) | 2405.05254 | 待处理 |
### 5.D Control (残差流门控/缩放控制)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子维度 | arXiv ID | 状态 |
|------|----------|------|------|------|--------|----------|------|
| C1 | Highway Transformer: Self-Gating Enhanced Self-Attentive Networks | Chai et al. | 2020 | ACL 2020 | Control (门控) | 2004.08178 | 已完成 |
| C2 | LAuReL: Learned Augmented Residual Layer | Menghani et al. | 2024 | arXiv | Control (可学习缩放) | 2411.07501 | 已完成 |
| C3 | ResiDual: Transformer with Dual Residual Connections | Mak & Flanigan | 2023 | ICLR 2024 | Control (双残差) | 2304.14802 | 已引用 |
| C4 | DeepNet: Scaling Transformers to 1,000 Layers (DeepNorm) | Wang et al. | 2022 | arXiv (Microsoft) | Control (深度缩放) | 2203.00555 | 已完成 |
| C5 | ReZero is All You Need: Fast Convergence at Large Depth | Bachlechner et al. | 2020 | UAI 2021 | Control (零初始化) | 2003.04887 | 已完成 |
| C6 | T-Fixup: Improving Transformer Optimization Through Better Initialization | Huang et al. | 2020 | ICML 2020 | Control (初始化) | 1910.05449 | 已完成 |
| C7 | Admin: Understanding the Difficulty of Training Transformers | Liu et al. | 2020 | EMNLP 2020 | Control (自适应初始化) | 2004.08249 | 已完成 |
| C8 | Batch Normalization Biases Residual Blocks (SkipInit) | De & Smith | 2020 | NeurIPS 2020 | Control (初始化理论) | 2002.03432 | 新增 |
| C9 | Fixup Initialization: Residual Learning Without Normalization | Zhang et al. | 2019 | ICLR 2019 | Control (初始化) | 1901.09321 | 新增 |
| C10 | On Layer Normalization in the Transformer Architecture (Pre-LN) | Xiong et al. | 2020 | ICML 2020 | Control (归一化位置) | 2002.04745 | 新增 |
| C11 | The Curse of Depth in Large Language Models (LNS) | Sun et al. | 2025 | arXiv | Control (深度缩放) | 2502.05795 | 新增 |
| C12 | NormFormer: Improved Transformer Pretraining with Extra Normalization | Shleifer et al. | 2021 | arXiv (Meta) | Control (额外归一化) | 2110.09456 | 新增 |
| C13 | CogView (Sandwich LayerNorm) | Ding et al. | 2021 | NeurIPS 2021 | Control (值稳定化) | 2105.13290 | 新增 |
| C14 | Stabilizing Transformers for RL (GTrXL) | Parisotto et al. | 2020 | ICML 2020 | Control (门控残差) | 1910.06764 | 新增 |
| C15 | Foundation Transformers (MAGNETO) | Hongyu Wang, Shuming Ma et al. | 2022 | arXiv | Control (Sub-LN + 初始化) | 2210.06423 | 待处理 |

### 5.E 几何与理论分析

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子维度 | arXiv ID | 状态 |
|------|----------|------|------|------|--------|----------|------|
| T1 | Revisiting Residual Connections: Orthogonal Updates (ORU) | Giyeong Oh et al. | 2025 | arXiv | Theory (正交残差更新) | 2505.11881 | 待处理 |
| T2 | ShortGPT: Layers in LLMs are More Redundant Than You Expect | Xin Men et al. | 2024 | ACL 2025 Findings | Theory (层冗余) | 2403.03853 | 待处理 |

### 5.F 残差与归一化交互

| 序号 | 论文标题 | 作者 | 年份 | 来源 | 子维度 | arXiv ID | 状态 |
|------|----------|------|------|------|--------|----------|------|
| N1 | Mix-LN: Unleashing the Power of Deeper Layers | Pengxiang Li, Lu Yin, Shiwei Liu | 2024 | arXiv | Norm-Residual (Pre/Post混合) | 2412.13795 | 待处理 |
| N2 | FuseNorm: Achieving the Best of Both Worlds from PreNorm and PostNorm | Wang Chao, Bei Li et al. | 2026 | ICLR 2026 submission | Norm-Residual (融合) | — | 待处理 |

---

## 6. Module Sequence (47 篇)

### 6.A Post-Norm vs. Pre-Norm (基础理论)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-01 | Attention Is All You Need (Post-Norm 原始设计) | Vaswani et al. | 2017 | NeurIPS 2017 | 1706.03762 | 已收录 |
| M-02 | On Layer Normalization in the Transformer Architecture (Pre-LN 理论分析) | Xiong et al. | 2020 | ICML 2020 | 2002.04745 | 已完成 |
| M-03 | Understanding the Difficulty of Training Transformers (Admin) | Liu et al. | 2020 | EMNLP 2020 | 2004.08249 | 已完成 |
| M-04 | DeepNet: Scaling Transformers to 1,000 Layers (DeepNorm) | Wang et al. | 2022 | IEEE TPAMI 2024 | 2203.00555 | 已收录 |
| M-05 | Foundation Transformers (MAGNETO / Sub-LayerNorm) | Wang et al. | 2022 | ICML 2023 | 2210.06423 | 已完成 |
| M-05b | Very Deep Transformers for Neural Machine Translation (ADMIN) | Liu et al. | 2020 | arXiv | 2008.07772 | 新增 |
### 6.B Pre-Norm vs. Post-Norm 统一与混合

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-06 | ResiDual: Transformer with Dual Residual Connections | Xie et al. | 2023 | arXiv | 2304.14802 | 已完成 |
| M-07 | CogView: Mastering Text-to-Image via Transformers (Sandwich LayerNorm) | Ding et al. | 2021 | NeurIPS 2021 | 2105.13290 | 已完成 |
| M-08 | Gemma 2: Improving Open Language Models (Pre+Post RMSNorm) | Gemma Team, Google | 2024 | arXiv | 2408.00118 | 新增 |
| M-09 | Peri-LN: Revisiting Normalization Layer in the Transformer Architecture | (TBD) | 2025 | arXiv | 2501.12948 | 新增 |
| M-10 | Mix-LN: Mixing Pre-Norm and Post-Norm Across Layers | Li, Yin, Liu | 2024 | arXiv | 2412.13795 | 新增 |
| M-11 | FuseNorm: Unifying Pre-Norm and Post-Norm for Stable Training | (TBD) | 2025 | arXiv (late 2025) | TBD | 待调研 |

### 6.C Simplified Transformer (简化 Transformer Block)

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-12 | Batch Normalization Biases Residual Blocks Towards the Identity Function (SkipInit) | De & Smith | 2020 | NeurIPS 2020 | 2002.10444 | 已完成 |
| M-13 | The Shaped Transformer: Attention Models in the Infinite Depth-and-Width Limit | Noci et al. | 2023 | NeurIPS 2023 | 2306.17759 | 已收录 |
| M-14 | Simplifying Transformer Blocks | He & Hofmann | 2023 | ICLR 2024 | 2311.01906 | 已完成 |
| M-15 | Parallel Attention (GPT-J 并行子层设计) | Wang & Komatsuzaki | 2021 | GPT-J | -- | 新增 |

### 6.D 归一化替代与移除对模块顺序的影响

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-16 | Transformers without Normalization (DyT) | Zhu et al. | 2025 | CVPR 2025 | 2503.10622 | 新增 |
| M-17 | nGPT: Normalized Transformer on the Hypersphere | Loshchilov et al. | 2024 | ICLR 2025 | 2410.01131 | 新增 |

### 6.E 前沿 / 新范式

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-18 | GeoNorm: Geodesic Updates for Normalization-Free Transformers | (TBD) | 2026 | arXiv (Jan 2026) | TBD | 待调研 |

### 6.F 额外归一化 / 梯度平衡

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-19 | NormFormer: Improved Transformer Pretraining with Extra Normalization | Shleifer et al. | 2021 | arXiv | 2110.09456 | 已完成 |

### 6.G 模块排列与 ODE 理论

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-20 | Understanding and Improving Transformer From a Multi-Particle Dynamic System (Macaron Net) | Lu et al. | 2019 | ICLR 2020 | 1906.02762 | 已完成 |

### 6.H 并行子层

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-21 | PaLM: Scaling Language Modeling with Pathways (Parallel Attention+FFN) | Chowdhery et al. | 2022 | JMLR 2023 | 2204.02311 | 已完成 |
| M-22 | Scaling Vision Transformers to 22B Parameters (ViT-22B, Parallel+QK-Norm) | Dehghani et al. | 2023 | ICML 2023 | 2302.05442 | 已完成 |
| M-22b | Swin Transformer V2: Scaling Up Capacity and Resolution (Res-Post-Norm) | Liu et al. | 2022 | CVPR 2022 | 2111.09883 | 新增 |

### 6.I 残差初始化替代归一化

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-23 | ReZero is All You Need: Fast Convergence at Large Depth | Bachlechner et al. | 2020 | UAI 2021 | 2003.04887 | 已完成 |
| M-24 | Fixup Initialization: Residual Learning Without Normalization | Zhang et al. | 2019 | ICLR 2019 | 1901.09321 | 已完成 |

### 6.J 架构搜索与异构块

| 序号 | 论文标题 | 作者 | 年份 | 来源 | arXiv ID | 状态 |
|------|----------|------|------|------|----------|------|
| M-25 | Primer: Searching for Efficient Transformers for Language Modeling | So et al. | 2021 | NeurIPS 2021 | 2109.08668 | 已完成 |
| M-26 | Brainformers: Trading Simplicity for Efficiency (异构块搜索) | Zhou et al. | 2023 | ICML 2023 | 2306.00008 | 已完成 |
| M-27 | Improving Transformer Models by Reordering their Sublayers (Sandwich Transformer) | Press, Smith, Levy | 2020 | ACL 2020 | 1911.03864 | 新增 |

---

## 7. 大厂技术报告 (22 篇)

| 序号 | 公司 | 模型 | 论文标题 | arXiv ID | 年份 | 架构概要 | 状态 |
|------|------|------|----------|----------|------|----------|------|
| 1 | DeepSeek | DeepSeek-V2 | DeepSeek-V2: A Strong, Economical, and Efficient MoE Language Model | 2405.04434 | 2024.05 | MLA + DeepSeekMoE, 236B/21B active | 已读 |
| 2 | DeepSeek | DeepSeek-V3 | DeepSeek-V3 Technical Report | 2412.19437 | 2024.12 | MLA + DeepSeekMoE, 671B/37B active, Aux-loss-free, MTP | 已读 |
| 3 | DeepSeek | DeepSeek-R1 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | 2501.12948 | 2025.01 | 基于V3架构, GRPO强化学习训练范式 | 已读 |
| 4 | Meta | Llama 3 | The Llama 3 Herd of Models | 2407.21783 | 2024.07 | Dense Transformer, GQA, RoPE, RMSNorm, SwiGLU | 已读 |
| 5 | Meta | Llama 4 | The Llama 4 Herd | 2601.11659 | 2025.04 | MoE, iRoPE(RoPE+NoPE交替), Early Fusion多模态 | 已读 |
| 6 | Alibaba | Qwen2.5 | Qwen2.5 Technical Report | 2412.15115 | 2024.12 | Dense + MoE variants, GQA, RoPE, SwiGLU, 18T tokens | 已读 |
| 7 | Alibaba | Qwen3 | Qwen3 Technical Report | 2505.09388 | 2025.05 | Dense+MoE(235B/22B), GQA, QK-Norm, 128专家选8, 36T tokens | 已读 |
| 8 | Moonshot AI | Kimi k1.5 | Kimi k1.5: Scaling Reinforcement Learning with LLMs | 2501.12599 | 2025.01 | RL训练范式, Long-CoT, Long2Short, 128k上下文RL | 已读 |
| 9 | Google | Gemma 2 | Gemma 2: Improving Open Language Models at a Practical Size | 2408.00118 | 2024.06 | 交替local/global attention, GQA, Logit soft-capping, RoPE, GeGLU | 已读 |
| 10 | Google | Gemma 3 | Gemma 3 Technical Report | 2503.19786 | 2025.03 | 5:1 local/global attention, sliding window 1024, GQA | 已读 |
| 11 | Mistral AI | Mixtral 8x7B | Mixtral of Experts | 2401.04088 | 2024.01 | SMoE 8专家选2, 47B/13B active, GQA, RoPE, SwiGLU | 已读 |
| 12 | Mistral AI | Mistral 7B | Mistral 7B | 2310.06825 | 2023.10 | Dense, Sliding Window Attention, GQA, RoPE, SwiGLU, RMSNorm | 已读 |
| 13 | Zhipu AI | GLM-4 | ChatGLM: A Family of LLMs from GLM-130B to GLM-4 All Tools | 2406.12793 | 2024.06 | Dense Transformer, GQA, RoPE, FlashAttention, 128k context | 已读 |
| 14 | 01.AI | Yi-Lightning | Yi-Lightning Technical Report | 2412.01253 | 2024.12 | MoE, 细粒度expert分割, hybrid attention, cross-layer KV sharing | 已读 |
| 15 | Tencent | Hunyuan-Large | Hunyuan-Large: Open-Source MoE with 52B Active Params | 2411.02265 | 2024.11 | MoE 389B/52B active, shared expert + Top-K, GQA + CLA | 已读 |
| 16 | MiniMax | MiniMax-01 | MiniMax-01: Scaling Foundation Models with Lightning Attention | 2501.08313 | 2025.01 | Lightning Attention + Softmax混合(7:1), MoE 456B/45.9B, 4M context | 已读 |
| 17 | Microsoft | Phi-4 | Phi-4 Technical Report | 2412.08905 | 2024.12 | 14B dense, 基于Phi-3架构, 合成数据为主 | 已读 |
| 18 | AI2 | OLMo 2 | 2 OLMo 2 Furious | 2501.00656 | 2025.01 | Dense autoregressive, 7B/13B/32B, 训练稳定性改进 | 已读 |
| 19 | Baichuan | Baichuan-M1 | Baichuan-M1: Pushing the Medical Capability of LLMs | 2502.12671 | 2025.02 | Pre-norm RMSNorm, SwiGLU, RoPE, hybrid attention, temporal conv on KV | 已读 |
| 20 | Baidu | ERNIE 4.5 | ERNIE 4.5 Technical Report | 2506.xxxxx | 2025.06 | 异构MoE(模态隔离路由), 424B/47B active, 2D RoPE, FP8训练 | 已读 |
| 21 | Huawei | PanGu-Sigma | PanGu-Sigma: Towards Trillion Parameter LM | 2303.10845 | 2023.03 | 1.085T稀疏模型, Random Routed Experts, MindSpore+Ascend | 已读 |

### 各模型架构要素对比表

| 模型 | Token Mixer | Channel Mixer | Normalization | Position Encoding | Residual | Module Seq |
|------|-------------|---------------|---------------|-------------------|----------|------------|
| DeepSeek-V3 | MLA (latent KV压缩) | DeepSeekMoE (细粒度expert) | RMSNorm | RoPE | 标准残差 + mHC | Pre-Norm |
| Llama 3 | GQA | Dense SwiGLU FFN | RMSNorm | RoPE (base=500k) | 标准残差 | Pre-Norm |
| Llama 4 | GQA + MoE routing | MoE | RMSNorm | iRoPE (RoPE+NoPE 3:1交替) | 标准残差 | Pre-Norm |
| Qwen3 | GQA + QK-Norm | MoE (128专家选8, 无shared) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Gemma 2 | GQA + 交替local/global attn | Dense GeGLU FFN | RMSNorm (pre+post) | RoPE | 标准残差 | Pre-Norm |
| Gemma 3 | GQA + 5:1 local/global(SW=1024) | Dense GeGLU FFN | RMSNorm | RoPE (rescaled) | 标准残差 | Pre-Norm |
| Mixtral 8x7B | GQA | SMoE (8专家选2) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Mistral 7B | GQA + Sliding Window Attn | Dense SwiGLU FFN | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| GLM-4 | GQA + FlashAttention | Dense FFN | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Yi-Lightning | hybrid local+global attn | MoE (细粒度expert分割) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Hunyuan-Large | GQA + CLA | MoE (shared + Top-K) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| MiniMax-01 | Lightning Attn + Softmax (7:1) | MoE (32专家) | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| Baichuan-M1 | hybrid global+sliding window | Dense SwiGLU FFN | RMSNorm | RoPE | 标准残差 | Pre-Norm |
| ERNIE 4.5 | Attention (模态隔离路由) | 异构MoE | RMSNorm | RoPE + 2D RoPE(视觉) | 标准残差 | Pre-Norm |
