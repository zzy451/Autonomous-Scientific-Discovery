# Token Mixer 论文清单

> 最后更新：2026-04-06
> 总计：103 篇笔记

## 1. Dot-Product Attention (标准注意力)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 1 | 01_transformer_attention.md | Attention Is All You Need | [笔记](Notes/token_mixer/01_transformer_attention.md) |
| 2 | vaswani_2017_attention.md | Attention Is All You Need | [笔记](Notes/token_mixer/vaswani_2017_attention.md) |
| 3 | 01_Qiu_2025_GatedAttn.md | Gated Attention for Large Language Models | [笔记](Notes/token_mixer/01_Qiu_2025_GatedAttn.md) |
| 4 | qiu_2025_gatedSelfAttn.md | Gated Self-Attention | [笔记](Notes/token_mixer/qiu_2025_gatedSelfAttn.md) |
| 5 | 14_gated_slot_attention.md | Gated Slot Attention for Efficient Linear-Time Sequence Modeling | [笔记](Notes/token_mixer/14_gated_slot_attention.md) |

## 2. KV Cache 优化 (Attention Head Sharing)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 6 | 06_Shazeer_2019_MQA.md | Fast Transformer Decoding: One Write-Head is All You Need | [笔记](Notes/token_mixer/06_Shazeer_2019_MQA.md) |
| 7 | 16_mqa.md | Fast Transformer Decoding: One Write-Head is All You Need (MQA) | [笔记](Notes/token_mixer/16_mqa.md) |
| 8 | shazeer_2019_mqa.md | Fast Transformer Decoding: One Write-Head is All You Need (MQA) | [笔记](Notes/token_mixer/shazeer_2019_mqa.md) |
| 9 | 07_Ainslie_2023_GQA.md | GQA: Training Generalized Multi-Query Transformer Models | [笔记](Notes/token_mixer/07_Ainslie_2023_GQA.md) |
| 10 | 15_gqa.md | GQA: Training Generalized Multi-Query Transformer Models | [笔记](Notes/token_mixer/15_gqa.md) |
| 11 | ainslie_2023_gqa.md | GQA: Training Generalized Multi-Query Transformer Models | [笔记](Notes/token_mixer/ainslie_2023_gqa.md) |
| 12 | 08_DeepSeek_2024_MLA.md | DeepSeek-V2: Multi-Head Latent Attention (MLA) | [笔记](Notes/token_mixer/08_DeepSeek_2024_MLA.md) |
| 13 | 17_mla.md | DeepSeek-V2: Multi-Head Latent Attention (MLA) | [笔记](Notes/token_mixer/17_mla.md) |
| 14 | deepseek_2024_mla.md | DeepSeek-V2: A Strong, Economical, and Efficient MoE Language Model (MLA) | [笔记](Notes/token_mixer/deepseek_2024_mla.md) |
| 15 | brandon_2024_cla.md | Reducing Transformer Key-Value Cache Size with Cross-Layer Attention (CLA) | [笔记](Notes/token_mixer/brandon_2024_cla.md) |

## 3. Sparse Attention (稀疏注意力)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 16 | 05_longformer.md | Longformer: The Long-Document Transformer | [笔记](Notes/token_mixer/05_longformer.md) |
| 17 | beltagy_2020_longformer.md | Longformer: The Long-Document Transformer | [笔记](Notes/token_mixer/beltagy_2020_longformer.md) |
| 18 | jiang_2023_mistral.md | Mistral 7B (Sliding Window Attention) | [笔记](Notes/token_mixer/jiang_2023_mistral.md) |
| 19 | 02_Yuan_2025_NSA.md | Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention | [笔记](Notes/token_mixer/02_Yuan_2025_NSA.md) |
| 20 | 06_nsa.md | NSA: Native Sparse Attention | [笔记](Notes/token_mixer/06_nsa.md) |
| 21 | yuan_2025_nsa.md | Native Sparse Attention (NSA) | [笔记](Notes/token_mixer/yuan_2025_nsa.md) |
| 22 | 03_Lu_2025_MoBA.md | MoBA: Mixture of Block Attention for Long-Context LLMs | [笔记](Notes/token_mixer/03_Lu_2025_MoBA.md) |
| 23 | 07_moba.md | MOBA: Mixture of Block Attention | [笔记](Notes/token_mixer/07_moba.md) |
| 24 | lu_2025_moba.md | MOBA: Mixture of Block Attention | [笔记](Notes/token_mixer/lu_2025_moba.md) |
| 25 | fu_2024_moa.md | Mixture of Sparse Attention for Automatic Large Language Model Compression (MoA) | [笔记](Notes/token_mixer/fu_2024_moa.md) |
| 26 | baichuan_2025_temporal_conv_kv.md | Baichuan-M1: Pushing the Medical Capability of Large Language Models | [笔记](Notes/token_mixer/baichuan_2025_temporal_conv_kv.md) |

## 4. Linear Attention (线性注意力)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 27 | 02_reformer.md | Reformer: The Efficient Transformer | [笔记](Notes/token_mixer/02_reformer.md) |
| 28 | kitaev_2020_reformer.md | Reformer: The Efficient Transformer | [笔记](Notes/token_mixer/kitaev_2020_reformer.md) |
| 29 | 03_linformer.md | Linformer: Self-Attention with Linear Complexity | [笔记](Notes/token_mixer/03_linformer.md) |
| 30 | wang_2020_linformer.md | Linformer: Self-Attention with Linear Complexity | [笔记](Notes/token_mixer/wang_2020_linformer.md) |
| 31 | 04_performer.md | Rethinking Attention with Performers | [笔记](Notes/token_mixer/04_performer.md) |
| 32 | choromanski_2021_performer.md | Rethinking Attention with Performers | [笔记](Notes/token_mixer/choromanski_2021_performer.md) |
| 33 | arora_2024_based.md | Simple Linear Attention Language Models Balance the Recall-Throughput Tradeoff (Based) | [笔记](Notes/token_mixer/arora_2024_based.md) |
| 34 | 25_based.md | Based: Simple Linear Attention Language Models Balance the Recall-Throughput Tradeoff | [笔记](Notes/token_mixer/25_based.md) |
| 35 | yang_2024_gla.md | Gated Linear Attention Transformers with Hardware-Efficient Training (GLA) | [笔记](Notes/token_mixer/yang_2024_gla.md) |
| 36 | yang_2024_deltanet.md | Parallelizing Linear Transformers with the Delta Rule over Sequence Length (DeltaNet) | [笔记](Notes/token_mixer/yang_2024_deltanet.md) |
| 37 | qin_2024_hgrn2.md | HGRN2: Gated Linear RNNs with State Expansion | [笔记](Notes/token_mixer/qin_2024_hgrn2.md) |
| 37b | qin_2023_hgrn.md | HGRN: Hierarchically Gated Recurrent Neural Network for Sequence Modeling | [笔记](Notes/token_mixer/qin_2023_hgrn.md) |
| 37c | katharopoulos_2020_linear_attention.md | Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention | [笔记](Notes/token_mixer/katharopoulos_2020_linear_attention.md) |
| 38 | qin_2024_lightning2.md | Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths | [笔记](Notes/token_mixer/qin_2024_lightning2.md) |
| 39 | 26_lightning_attention.md | Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths | [笔记](Notes/token_mixer/26_lightning_attention.md) |

## 5. Attention with Negative Weights (负权重注意力)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 40 | 04_Ye_2024_DiffTransformer.md | Differential Transformer | [笔记](Notes/token_mixer/04_Ye_2024_DiffTransformer.md) |
| 41 | 08_differential_transformer.md | Differential Transformer | [笔记](Notes/token_mixer/08_differential_transformer.md) |
| 42 | ye_2024_difftransformer.md | Differential Transformer | [笔记](Notes/token_mixer/ye_2024_difftransformer.md) |
| 43 | 05_Lv_2024_CogAttn.md | More Expressive Attention with Negative Weights (Cog Attention) | [笔记](Notes/token_mixer/05_Lv_2024_CogAttn.md) |
| 44 | 09_cog_attention.md | CogAttn: Cognitive Attention for Large Language Models | [笔记](Notes/token_mixer/09_cog_attention.md) |
| 45 | lv_2024_cogattention.md | CogAttention: More Expressive Attention with Negative Weights | [笔记](Notes/token_mixer/lv_2024_cogattention.md) |

## 6. Different Activation (不同激活函数)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 46 | 10_sigmoid_attention.md | Scaling Sigmoid Dot-Product Attention for Large Language Models | [笔记](Notes/token_mixer/10_sigmoid_attention.md) |
| 47 | ramapuram_2024_sigmoid.md | Theory, Analysis, and Best Practices for Sigmoid Self-Attention | [笔记](Notes/token_mixer/ramapuram_2024_sigmoid.md) |

## 7. RNN-Like / SSM (循环式/状态空间模型)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 48 | gu_2021_s4.md | Efficiently Modeling Long Sequences with Structured State Spaces (S4) | [笔记](Notes/token_mixer/gu_2021_s4.md) |
| 49 | ma_2023_mega.md | Mega: Moving Average Equipped Gated Attention | [笔记](Notes/token_mixer/ma_2023_mega.md) |
| 50 | poli_2023_hyena.md | Hyena Hierarchy: Towards Larger Convolutional Language Models | [笔记](Notes/token_mixer/poli_2023_hyena.md) |
| 51 | poli_2023_stripedhyena.md | StripedHyena: Moving Beyond Transformers with Hybrid Signal Processing Models | [笔记](Notes/token_mixer/poli_2023_stripedhyena.md) |
| 52 | beck_2024_xlstm.md | xLSTM: Extended Long Short-Term Memory | [笔记](Notes/token_mixer/beck_2024_xlstm.md) |
| 52b | ma_2024_megalodon.md | Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length | [笔记](Notes/token_mixer/ma_2024_megalodon.md) |
| 53 | 12_rwkv.md | RWKV: Reinventing RNNs for the Transformer Era | [笔记](Notes/token_mixer/12_rwkv.md) |
| 54 | peng_2023_rwkv.md | RWKV: Reinventing RNNs for the Transformer Era | [笔记](Notes/token_mixer/peng_2023_rwkv.md) |
| 55 | 13_Sun_2023_RetNet.md | Retentive Network: A Successor to Transformer for Large Language Models | [笔记](Notes/token_mixer/13_Sun_2023_RetNet.md) |
| 56 | 21_retnet.md | Retentive Network: A Successor to Transformer for Large Language Models (RetNet) | [笔记](Notes/token_mixer/21_retnet.md) |
| 57 | sun_2023_retnet.md | Retentive Network: A Successor to Transformer for Large Language Models (RetNet) | [笔记](Notes/token_mixer/sun_2023_retnet.md) |
| 58 | 09_Gu_2024_Mamba.md | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | [笔记](Notes/token_mixer/09_Gu_2024_Mamba.md) |
| 59 | 11_mamba.md | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | [笔记](Notes/token_mixer/11_mamba.md) |
| 60 | gu_2024_mamba.md | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | [笔记](Notes/token_mixer/gu_2024_mamba.md) |
| 61 | 10_Dao_2024_Mamba2.md | Transformers are SSMs: Generalized Models and Efficient Algorithms (Mamba-2) | [笔记](Notes/token_mixer/10_Dao_2024_Mamba2.md) |
| 62 | 20_mamba2.md | Transformers are SSMs: Generalized Models and Efficient Algorithms (Mamba-2) | [笔记](Notes/token_mixer/20_mamba2.md) |
| 63 | dao_2024_mamba2.md | Transformers are SSMs: Generalized Models and Efficient Algorithms (Mamba-2) | [笔记](Notes/token_mixer/dao_2024_mamba2.md) |
| 64 | 14_Peng_2024_RWKV56.md | Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence | [笔记](Notes/token_mixer/14_Peng_2024_RWKV56.md) |
| 65 | 22_rwkv_v5v6.md | Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence (RWKV v5/v6) | [笔记](Notes/token_mixer/22_rwkv_v5v6.md) |
| 66 | peng_2024_rwkv56.md | Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence (RWKV v5/v6) | [笔记](Notes/token_mixer/peng_2024_rwkv56.md) |
| 67 | 13_gated_delta_networks.md | Gated Delta Networks: Improving Mamba2 with Delta Rule | [笔记](Notes/token_mixer/13_gated_delta_networks.md) |
| 68 | yang_2024_gatedDelta.md | Gated Delta Networks: Improving Mamba2 with Delta Rule | [笔记](Notes/token_mixer/yang_2024_gatedDelta.md) |
| 69 | 23_rwkv_v7.md | RWKV-7 Goose with Expressive Dynamic State Evolution | [笔记](Notes/token_mixer/23_rwkv_v7.md) |
| 70 | peng_2025_rwkv7.md | RWKV-7 "Goose" with Expressive Dynamic State Evolution | [笔记](Notes/token_mixer/peng_2025_rwkv7.md) |
| 70b | sun_2024_ttt.md | Learning to (Learn at Test Time): RNNs with Expressive Hidden States (TTT) | [笔记](Notes/token_mixer/sun_2024_ttt.md) |
| 70c | behrouz_2025_titans.md | Titans: Learning to Memorize at Test Time | [笔记](Notes/token_mixer/behrouz_2025_titans.md) |
| 70d | qin_2023_hgrn.md | HGRN: Hierarchically Gated Recurrent Neural Network for Sequence Modeling | [笔记](Notes/token_mixer/qin_2023_hgrn.md) |
| 70e | gu_2025_mamba3.md | Mamba-3: Improved Sequence Modeling using State Space Principles | [笔记](Notes/token_mixer/gu_2025_mamba3.md) |

## 8. Hybrid Architectures (混合架构)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 71 | 15_Lieber_2024_Jamba.md | Jamba: A Hybrid Transformer-Mamba Language Model | [笔记](Notes/token_mixer/15_Lieber_2024_Jamba.md) |
| 72 | 24_jamba.md | Jamba: A Hybrid Transformer-Mamba Language Model | [笔记](Notes/token_mixer/24_jamba.md) |
| 73 | lieber_2024_jamba.md | Jamba: A Hybrid Transformer-Mamba Language Model | [笔记](Notes/token_mixer/lieber_2024_jamba.md) |
| 74 | griffin_2024_hybrid.md | Griffin: Mixing Gated Linear Recurrences with Local Attention | [笔记](Notes/token_mixer/griffin_2024_hybrid.md) |
| 75 | de_2024_griffin_hawk.md | Griffin & Hawk: Mixing Gated Linear Recurrences with Local Attention | [笔记](Notes/token_mixer/de_2024_griffin_hawk.md) |
| 76 | botev_2024_recurrentgemma.md | RecurrentGemma: Moving Past Transformers for Efficient Open Language Models | [笔记](Notes/token_mixer/botev_2024_recurrentgemma.md) |
| 76b | zyphra_2024_zamba2.md | Zamba2: A Suite of Hybrid Mamba2-Transformer Models | [笔记](Notes/token_mixer/zyphra_2024_zamba2.md) |

## 9. Hardware-Efficient Attention (硬件高效注意力)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 77 | 11_Dao_2022_FlashAttn.md | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | [笔记](Notes/token_mixer/11_Dao_2022_FlashAttn.md) |
| 78 | 18_flash_attention.md | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | [笔记](Notes/token_mixer/18_flash_attention.md) |
| 79 | dao_2022_flashattention.md | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | [笔记](Notes/token_mixer/dao_2022_flashattention.md) |
| 80 | 12_Dao_2023_FlashAttn2.md | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | [笔记](Notes/token_mixer/12_Dao_2023_FlashAttn2.md) |
| 81 | 19_flash_attention_2.md | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | [笔记](Notes/token_mixer/19_flash_attention_2.md) |
| 82 | dao_2023_flashattention2.md | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | [笔记](Notes/token_mixer/dao_2023_flashattention2.md) |
| 83 | shah_2024_flashattention3.md | FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision | [笔记](Notes/token_mixer/shah_2024_flashattention3.md) |
| 84 | liu_2023_ring_attention.md | Ring Attention with Blockwise Transformers for Near-Infinite Context | [笔记](Notes/token_mixer/liu_2023_ring_attention.md) |
| 85 | kwon_2023_pagedattention.md | Efficient Memory Management for LLM Serving with PagedAttention | [笔记](Notes/token_mixer/kwon_2023_pagedattention.md) |
| 85b | zhang_2024_sageattention.md | SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration | [笔记](Notes/token_mixer/zhang_2024_sageattention.md) |

## 10. KV Cache 压缩 (KV Cache Compression)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 86 | cai_2024_pyramidkv.md | PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | [笔记](Notes/token_mixer/cai_2024_pyramidkv.md) |
| 87 | li_2024_snapkv.md | SnapKV: LLM Knows What You Are Looking for Before Generation | [笔记](Notes/token_mixer/li_2024_snapkv.md) |
| 88 | liu_2024_minicache.md | MiniCache: KV Cache Compression in Depth Dimension for Large Language Models | [笔记](Notes/token_mixer/liu_2024_minicache.md) |
| 89 | munkhdalai_2024_infini_attention.md | Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention | [笔记](Notes/token_mixer/munkhdalai_2024_infini_attention.md) |
| 90 | sun_2024_yoco.md | You Only Cache Once: Decoder-Decoder Architectures for Language Models (YOCO) | [笔记](Notes/token_mixer/sun_2024_yoco.md) |
| 90b | zhang_2023_h2o.md | H2O: Heavy-Hitter Oracle: Efficient Generative Inference with Heavy-Hitter Oracle | [笔记](Notes/token_mixer/zhang_2023_h2o.md) |
| 90c | xiao_2023_streamingllm.md | Efficient Streaming Language Models with Attention Sinks (StreamingLLM) | [笔记](Notes/token_mixer/xiao_2023_streamingllm.md) |

## 11. Lightning Attention / 大规模线性注意力工业应用

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 91 | minimax_2025_minimax01.md | MiniMax-01: Scaling Foundation Models with Lightning Attention | [笔记](Notes/token_mixer/minimax_2025_minimax01.md) |
| 92 | qin_2024_transnormerllm.md | TransNormerLLM: A Faster and Better Large Language Model with Improved TransNormer | [笔记](Notes/token_mixer/qin_2024_transnormerllm.md) |

## 12. 其他 (Surveys / Misc)

| 序号 | 文件名 | 论文标题 | 笔记链接 |
|------|--------|----------|----------|
| 93 | gloeckle_2024_multi_token_prediction.md | Better & Faster Large Language Models via Multi-token Prediction | [笔记](Notes/token_mixer/gloeckle_2024_multi_token_prediction.md) |
| 94 | speculative_decoding_attention_survey.md | Speculative Decoding 与 Attention 的关系综述笔记 | [笔记](Notes/token_mixer/speculative_decoding_attention_survey.md) |
| 95 | katharopoulos_2020_linear_attention.md | Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention | [笔记](Notes/token_mixer/katharopoulos_2020_linear_attention.md) |
| 96 | wen_2025_irope.md | RoPE to NoPE and Back Again: A New Hybrid Attention Strategy (iRoPE) | [笔记](Notes/token_mixer/wen_2025_irope.md) |
