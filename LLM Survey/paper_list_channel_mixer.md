# Channel Mixer 论文清单

> 最后更新：2026-04-06
> 总计：42 篇笔记

## A. FFN 基础与激活函数

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 1 | Dauphin_2017_GLU.md | Language Modeling with Gated Convolutional Networks (GLU) | [笔记](Notes/channel_mixer/Dauphin_2017_GLU.md) |
| 2 | Ramachandran_2017_Swish.md | Searching for Activation Functions (Swish/SiLU) | [笔记](Notes/channel_mixer/Ramachandran_2017_Swish.md) |
| 3 | Zhang_2024_ReLU2Wins.md | ReLU^2 Wins: Discovering Efficient Activation Functions for Sparse LLMs | [笔记](Notes/channel_mixer/Zhang_2024_ReLU2Wins.md) |
| 4 | Liu_2024_KAN.md | KAN: Kolmogorov-Arnold Networks | [笔记](Notes/channel_mixer/Liu_2024_KAN.md) |
| 5 | PolyGLU_2026.md | PolyGLU: State-Conditional Activation Routing in Transformer Feed-Forward Networks | [笔记](Notes/channel_mixer/PolyGLU_2026.md) |

## B. Mixture of Experts (MoE) — 基础与路由策略

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 6 | Jacobs_1991_AdaptiveMoE.md | Adaptive Mixtures of Local Experts | [笔记](Notes/channel_mixer/Jacobs_1991_AdaptiveMoE.md) |
| 7 | Shazeer_2017_SparseMoE.md | Outrageously Large Neural Networks: The Sparsely-Gated MoE Layer | [笔记](Notes/channel_mixer/Shazeer_2017_SparseMoE.md) |
| 8 | Lepikhin_2021_GShard.md | GShard: Scaling Giant Models with Conditional Computation | [笔记](Notes/channel_mixer/Lepikhin_2021_GShard.md) |
| 9 | Fedus_2022_SwitchTransformer.md | Switch Transformers: Scaling to Trillion Parameter Models | [笔记](Notes/channel_mixer/Fedus_2022_SwitchTransformer.md) |
| 10 | Zoph_2022_STMoE.md | ST-MoE: Designing Stable and Transferable Sparse Expert Models | [笔记](Notes/channel_mixer/Zoph_2022_STMoE.md) |
| 11 | Zhou_2022_ExpertChoice.md | Mixture-of-Experts with Expert Choice Routing | [笔记](Notes/channel_mixer/Zhou_2022_ExpertChoice.md) |
| 12 | Wang_2024_AuxLossFree.md | Auxiliary-Loss-Free Load Balancing Strategy for MoE | [笔记](Notes/channel_mixer/Wang_2024_AuxLossFree.md) |
| 13 | Puigcerver_2024_SoftMoE.md | From Sparse to Soft Mixtures of Experts (Soft MoE) | [笔记](Notes/channel_mixer/Puigcerver_2024_SoftMoE.md) |
| 14 | Puigcerver_2023_SoftMoE.md | [重复] Soft MoE | [笔记](Notes/channel_mixer/Puigcerver_2023_SoftMoE.md) |
| 15 | Wang_2024_ReMoE.md | ReMoE: Fully Differentiable Mixture-of-Experts with ReLU Routing | [笔记](Notes/channel_mixer/Wang_2024_ReMoE.md) |
| 16 | DirMoE_2025.md | DirMoE: Dirichlet-Routed Mixture of Experts | [笔记](Notes/channel_mixer/DirMoE_2025.md) |
| 17 | He_2024_MillionExperts.md | Mixture of A Million Experts | [笔记](Notes/channel_mixer/He_2024_MillionExperts.md) |
| 18 | Zhong_2024_Lory.md | Lory: Fully Differentiable Mixture-of-Experts for Autoregressive Language Model Pre-training | [笔记](Notes/channel_mixer/Zhong_2024_Lory.md) |
| 19 | SharedExpert_vs_NoShared_2025.md | Shared Expert vs No Shared Expert: MoE 架构设计的核心分歧 | [笔记](Notes/channel_mixer/SharedExpert_vs_NoShared_2025.md) |
| 20 | DenseBP_2025_SparseMoE.md | Dense Backpropagation Improves Training for Sparse Mixture-of-Experts | [笔记](Notes/channel_mixer/DenseBP_2025_SparseMoE.md) |
| 21 | MoE_DoublePenalty_2026.md | MoE 推理的双重惩罚：训练效率 ≠ 推理效率 | [笔记](Notes/channel_mixer/MoE_DoublePenalty_2026.md) |

## C. MoE 应用模型

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 22 | Jiang_2024_Mixtral.md | Mixtral of Experts | [笔记](Notes/channel_mixer/Jiang_2024_Mixtral.md) |
| 23 | Dai_2024_DeepSeekMoE.md | DeepSeekMoE: Towards Ultimate Expert Specialization | [笔记](Notes/channel_mixer/Dai_2024_DeepSeekMoE.md) |
| 24 | DeepSeekAI_2024_DeepSeekV2.md | DeepSeek-V2: A Strong, Economical, and Efficient MoE LM | [笔记](Notes/channel_mixer/DeepSeekAI_2024_DeepSeekV2.md) |
| 25 | DeepSeekAI_2024_DeepSeekV3.md | DeepSeek-V3 Technical Report | [笔记](Notes/channel_mixer/DeepSeekAI_2024_DeepSeekV3.md) |
| 26 | Databricks_2024_DBRX.md | DBRX: An Open General-Purpose LLM | [笔记](Notes/channel_mixer/Databricks_2024_DBRX.md) |
| 27 | Muennighoff_2024_OLMoE.md | OLMoE: Open Mixture-of-Experts Language Models | [笔记](Notes/channel_mixer/Muennighoff_2024_OLMoE.md) |
| 28 | Wei_2024_SkyworkMoE.md | Skywork-MoE: Training Techniques for MoE LLMs | [笔记](Notes/channel_mixer/Wei_2024_SkyworkMoE.md) |
| 29 | xAI_2024_Grok1.md | Grok-1 (314B MoE) | [笔记](Notes/channel_mixer/xAI_2024_Grok1.md) |
| 30 | Lieber_2024_Jamba.md | Jamba: A Hybrid Transformer-Mamba Language Model | [笔记](Notes/channel_mixer/Lieber_2024_Jamba.md) |
| 31 | 01AI_2024_YiLightning.md | Yi-Lightning Technical Report | [笔记](Notes/channel_mixer/01AI_2024_YiLightning.md) |
| 32 | Tencent_2024_HunyuanLarge.md | Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters | [笔记](Notes/channel_mixer/Tencent_2024_HunyuanLarge.md) |
| 33 | MiniMax_2025_MiniMax01.md | MiniMax-01: Scaling Foundation Models with Lightning Attention | [笔记](Notes/channel_mixer/MiniMax_2025_MiniMax01.md) |
| 34 | Meta_2025_Llama4.md | Llama 4: The Llama 4 Herd of Models | [笔记](Notes/channel_mixer/Meta_2025_Llama4.md) |
| 35 | Qwen3_2025_MoE.md | Qwen3: 无 Shared Expert 的 MoE 与全局批次均衡 | [笔记](Notes/channel_mixer/Qwen3_2025_MoE.md) |
| 36 | Qwen_2025_Qwen3.md | Qwen3 Technical Report | [笔记](Notes/channel_mixer/Qwen_2025_Qwen3.md) |

## D. 条件计算与 FFN 变体

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 37 | Raposo_2024_MoD.md | Mixture-of-Depths: Dynamically Allocating Compute | [笔记](Notes/channel_mixer/Raposo_2024_MoD.md) |
| 38 | Liu_2023_DejaVu.md | Deja Vu: Contextual Sparsity for Efficient LLMs | [笔记](Notes/channel_mixer/Liu_2023_DejaVu.md) |
| 39 | Zhang_2022_MoEfication.md | MoEfication: Transformer FFN Layers are Mixtures of Experts | [笔记](Notes/channel_mixer/Zhang_2022_MoEfication.md) |
| 40 | DuoLLM_2024.md | Duo-LLM: A Framework for Studying Adaptive Computation in LLMs | [笔记](Notes/channel_mixer/DuoLLM_2024.md) |

## E. MoE 基础设施与综述

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 41 | DeepSeek_2025_DeepEP.md | DeepEP: Expert Parallelism 通信库与 MoE 分布式推理/训练 | [笔记](Notes/channel_mixer/DeepSeek_2025_DeepEP.md) |
| 42 | ExpertPruning_2024_Survey.md | MoE Expert Pruning: 专家级稀疏化与压缩 | [笔记](Notes/channel_mixer/ExpertPruning_2024_Survey.md) |
