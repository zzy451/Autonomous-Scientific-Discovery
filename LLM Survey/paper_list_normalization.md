# Normalization 论文清单

> 最后更新：2026-04-06
> 总计：35 篇笔记

## A. 基础规范化方法 (Foundation Normalization Methods)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 1 | N01_BatchNorm_Ioffe2015.md | Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift | [笔记](Notes/normalization/N01_BatchNorm_Ioffe2015.md) |
| 2 | N02_LayerNorm_Ba2016.md | Layer Normalization | [笔记](Notes/normalization/N02_LayerNorm_Ba2016.md) |
| 3 | N03_InstanceNorm_Ulyanov2016.md | Instance Normalization: The Missing Ingredient for Fast Stylization | [笔记](Notes/normalization/N03_InstanceNorm_Ulyanov2016.md) |
| 4 | N04_GroupNorm_Wu2018.md | Group Normalization | [笔记](Notes/normalization/N04_GroupNorm_Wu2018.md) |

## B. Transformer 中的规范化位置与理论分析 (Normalization Placement & Theory)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 5 | N05_PreLN_PostLN_Xiong2020.md | On Layer Normalization in the Transformer Architecture (Pre-LN vs Post-LN) | [笔记](Notes/normalization/N05_PreLN_PostLN_Xiong2020.md) |
| 6 | N06_AdaNorm_Xu2019.md | Understanding and Improving Layer Normalization (AdaNorm) | [笔记](Notes/normalization/N06_AdaNorm_Xu2019.md) |
| 7 | N07_SandwichLN_CogView_Ding2021.md | CogView: Mastering Text-to-Image Generation via Transformers (Sandwich LayerNorm) | [笔记](Notes/normalization/N07_SandwichLN_CogView_Ding2021.md) |
| 8 | N08_DeepNorm_Wang2022.md | DeepNet: Scaling Transformers to 1,000 Layers (DeepNorm) | [笔记](Notes/normalization/N08_DeepNorm_Wang2022.md) |
| 9 | N20_MAGNETO_SubLN_Wang2022.md | Foundation Transformers (MAGNETO / Sub-LayerNorm) | [笔记](Notes/normalization/N20_MAGNETO_SubLN_Wang2022.md) |
| 10 | N21_PeriLN_2025.md | Peri-LN: Revisiting Normalization Layer in the Transformer Architecture | [笔记](Notes/normalization/N21_PeriLN_2025.md) |
| 11 | N27_ReIntroducingLN_Gupta2024.md | Re-Introducing LayerNorm: Geometric Meaning, Irreversibility and a Comparative Study with RMSNorm | [笔记](Notes/normalization/N27_ReIntroducingLN_Gupta2024.md) |
| 12 | N28_NormAttentionDynamics_Karagodin2025.md | Normalization in Attention Dynamics | [笔记](Notes/normalization/N28_NormAttentionDynamics_Karagodin2025.md) |

## C. 高效变体 (Efficient Variants)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 13 | N09_RMSNorm_Zhang2019.md | Root Mean Square Layer Normalization (RMSNorm) | [笔记](Notes/normalization/N09_RMSNorm_Zhang2019.md) |
| 14 | N22_ScaleNorm_FixNorm_Nguyen2019.md | Transformers without Tears: Improving the Normalization of Self-Attention (ScaleNorm, FixNorm) | [笔记](Notes/normalization/N22_ScaleNorm_FixNorm_Nguyen2019.md) |
| 15 | N23_PowerNorm_Shen2020.md | PowerNorm: Rethinking Batch Normalization in Transformers | [笔记](Notes/normalization/N23_PowerNorm_Shen2020.md) |

## D. 注意力内部归一化 (Attention-Internal Normalization)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 16 | N10_QKNorm_Henry2020.md | Query-Key Normalization for Transformers (QK-Norm) | [笔记](Notes/normalization/N10_QKNorm_Henry2020.md) |
| 17 | N24_DiffTransformer_GroupNorm_Ye2024.md | Differential Transformer (GroupNorm in attention heads) | [笔记](Notes/normalization/N24_DiffTransformer_GroupNorm_Ye2024.md) |
| 18 | N29_EnhancedQKNorm_LopezRubio2026.md | Enhanced QKNorm normalization for neural transformers with the Lp norm | [笔记](Notes/normalization/N29_EnhancedQKNorm_LopezRubio2026.md) |

## E. 条件化归一化 (Conditional / Adaptive Normalization)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 19 | N11_AdaLN_DiT_Peebles2023.md | Scalable Diffusion Models with Transformers (DiT, adaLN-Zero) | [笔记](Notes/normalization/N11_AdaLN_DiT_Peebles2023.md) |

## F. 全面归一化架构 (Holistic Normalization Architectures)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 20 | N25_nGPT_Loshchilov2024.md | nGPT: Normalized Transformer with Representation Learning on the Hypersphere | [笔记](Notes/normalization/N25_nGPT_Loshchilov2024.md) |
| 21 | N26_Gemma2_PrePostNorm_2024.md | Gemma 2: Improving Open Language Models at a Practical Size (Pre+Post RMSNorm) | [笔记](Notes/normalization/N26_Gemma2_PrePostNorm_2024.md) |

## G. 自动化搜索归一化 (Automated / Evolved Normalization)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 22 | N12_EvoNorm_Liu2020.md | Evolving Normalization-Activation Layers (EvoNorm) | [笔记](Notes/normalization/N12_EvoNorm_Liu2020.md) |

## H. 无归一化方法 (Normalization-Free Methods)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 23 | N13_Fixup_Zhang2019.md | Fixup Initialization: Residual Learning Without Normalization | [笔记](Notes/normalization/N13_Fixup_Zhang2019.md) |
| 24 | N14_TFixup_Huang2020.md | Improving Transformer Optimization Through Better Initialization (T-Fixup) | [笔记](Notes/normalization/N14_TFixup_Huang2020.md) |
| 25 | N15_NFNet_Brock2021.md | High-Performance Large-Scale Image Recognition Without Normalization (NF-Net, AGC) | [笔记](Notes/normalization/N15_NFNet_Brock2021.md) |
| 26 | N16_DyT_Zhu2025.md | Transformers without Normalization (Dynamic Tanh / DyT) | [笔记](Notes/normalization/N16_DyT_Zhu2025.md) |
| 27 | N17_Derf_Chen2025.md | Stronger Normalization-Free Transformers (Dynamic Erf / Derf) | [笔记](Notes/normalization/N17_Derf_Chen2025.md) |

## I. 前沿与新方向 (Frontier, 2025-2026)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 28 | N30_GeoNorm_2026.md | GeoNorm — Unify Pre-Norm and Post-Norm with Geodesic Optimization | [笔记](Notes/normalization/N30_GeoNorm_2026.md) |
| 29 | N31_HybridNorm_2025.md | HybridNorm — Towards Stable and Efficient Transformer Training via Hybrid Normalization | [笔记](Notes/normalization/N31_HybridNorm_2025.md) |
| 30 | N32_UnitNorm_2024.md | UnitNorm — Rethinking Normalization for Transformers in Time Series | [笔记](Notes/normalization/N32_UnitNorm_2024.md) |
| 31 | N33_OutlierDrivenRescaling_2026.md | Outlier-Driven Rescaling is Essential for Transformer Training | [笔记](Notes/normalization/N33_OutlierDrivenRescaling_2026.md) |
| 32 | N34_FOG_FP8Norm_2025.md | FOG — Towards Fully FP8 GEMM LLM Training at Scale | [笔记](Notes/normalization/N34_FOG_FP8Norm_2025.md) |
| 33 | N35_WhyLowPrecisionFails_2025.md | Why Low-Precision Transformer Training Fails | [笔记](Notes/normalization/N35_WhyLowPrecisionFails_2025.md) |
| 34 | N36_MuonOptimizer_NormFree_2025.md | Muon 优化器与无归一化训练的交互 — 谱控制替代归一化 | [笔记](Notes/normalization/N36_MuonOptimizer_NormFree_2025.md) |
| 35 | N37_SiameseNorm_2026.md | SiameseNorm — Breaking the Barrier to Reconciling Pre/Post-Norm | [笔记](Notes/normalization/N37_SiameseNorm_2026.md) |
