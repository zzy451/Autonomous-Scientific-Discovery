# 覆盖完整性检查报告

生成日期：2026-04-06

## 1. bib 引用 vs 笔记对照

### Survey 类
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| vaswani2017attention | Attention is all you need | 是 | Notes/token_mixer/vaswani_2017_attention.md |
| tay2020efficient | Efficient Transformers: A Survey | 否 | — (综述类无需笔记) |
| shao2024survey | Survey of different LLM architectures | 否 | — (综述类无需笔记) |
| sajun2024historical | A historical survey of advances in transformer architectures | 否 | — (综述类无需笔记) |
| raiaan2024review | A review on large language models | 否 | — (综述类无需笔记) |
| kim2025survey | Survey and Evaluation of Converging Architecture in LLMs | 否 | — (综述类无需笔记) |

### Token Mixer
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| kitaev2020reformer | Reformer: The efficient transformer | 是 | Notes/token_mixer/kitaev_2020_reformer.md |
| wang2020linformer | Linformer: Self-attention with linear complexity | 是 | Notes/token_mixer/wang_2020_linformer.md |
| choromanski2021rethinking | Rethinking attention with performers | 是 | Notes/token_mixer/choromanski_2021_performer.md |
| beltagy2020longformer | Longformer: The long-document transformer | 是 | Notes/token_mixer/beltagy_2020_longformer.md |
| tay2020sparse | Sparse sinkhorn attention | 否 | — |
| yang2024gated | Gated delta networks | 是 | Notes/token_mixer/yang_2024_gatedDelta.md |
| yuan2025native | Native sparse attention (NSA) | 是 | Notes/token_mixer/yuan_2025_nsa.md |
| lu2025moba | MoBA: Mixture of block attention | 是 | Notes/token_mixer/lu_2025_moba.md |
| lv2024more | More Expressive Attention with Negative Weights (CogAttn) | 是 | Notes/token_mixer/lv_2024_cogattention.md |
| qiu2025gated | Gated Attention for LLMs | 是 | Notes/token_mixer/qiu_2025_gatedSelfAttn.md |
| gu2024mamba | Mamba: Linear-time sequence modeling | 是 | Notes/token_mixer/gu_2024_mamba.md |
| peng2023rwkv | RWKV: Reinventing RNNs for the transformer era | 是 | Notes/token_mixer/peng_2023_rwkv.md |
| ramapuram2024theory | Sigmoid self-attention | 是 | Notes/token_mixer/ramapuram_2024_sigmoid.md |
| shazeer2019fast | Fast transformer decoding (MQA) | 是 | Notes/token_mixer/shazeer_2019_mqa.md |
| ainslie2023gqa | GQA | 是 | Notes/token_mixer/ainslie_2023_gqa.md |
| deepseekv2_2024_mla | DeepSeek-V2 (MLA) | 是 | Notes/token_mixer/deepseek_2024_mla.md |
| katharopoulos2020transformers | Transformers are RNNs (linear attention) | 否 | — |
| eyuboglu2024based | Based: Simple linear attention | 是 | Notes/token_mixer/arora_2024_based.md |
| gu2022efficiently | S4: Structured state spaces | 是 | Notes/token_mixer/gu_2021_s4.md |
| sun2023retentive | RetNet | 是 | Notes/token_mixer/sun_2023_retnet.md |
| dao2024transformers | Mamba-2 (SSD) | 是 | Notes/token_mixer/dao_2024_mamba2.md |
| peng2024eagle | RWKV-5/6 (Eagle and Finch) | 是 | Notes/token_mixer/peng_2024_rwkv56.md |
| jiang2023mistral | Mistral 7B (sliding window) | 是 | Notes/token_mixer/jiang_2023_mistral.md |
| dao2022flashattention | FlashAttention | 是 | Notes/token_mixer/dao_2022_flashattention.md |
| dao2023flashattention2 | FlashAttention-2 | 是 | Notes/token_mixer/dao_2023_flashattention2.md |
| shah2024flashattention3 | FlashAttention-3 | 是 | Notes/token_mixer/shah_2024_flashattention3.md |
| dehghani2023scaling | ViT-22B (QK-Norm) | 否 | — (归一化方向有覆盖) |

### Channel Mixer
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| agarap2018deep | Deep learning using ReLU | 否 | — |
| hendrycks2016gaussian | Gaussian Error Linear Units (GELU) | 否 | — |
| shazeer2020glu | GLU variants improve transformer (SwiGLU) | 否 | — (Dauphin GLU笔记部分覆盖) |
| liu2024deepseek | DeepSeek-V3 technical report | 是 | Notes/channel_mixer/DeepSeekAI_2024_DeepSeekV3.md |
| dauphin2017language | Language modeling with gated convolutional networks (GLU) | 是 | Notes/channel_mixer/Dauphin_2017_GLU.md |
| ramachandran2017searching | Searching for activation functions (Swish) | 是 | Notes/channel_mixer/Ramachandran_2017_Swish.md |
| zhang2024relu2 | ReLU^2 Wins | 是 | Notes/channel_mixer/Zhang_2024_ReLU2Wins.md |
| jacobs1991adaptive | Adaptive mixtures of local experts | 是 | Notes/channel_mixer/Jacobs_1991_AdaptiveMoE.md |
| shazeer2017outrageously | Sparsely-gated MoE layer | 是 | Notes/channel_mixer/Shazeer_2017_SparseMoE.md |
| lepikhin2020gshard | GShard | 是 | Notes/channel_mixer/Lepikhin_2021_GShard.md |
| fedus2022switch | Switch Transformers | 是 | Notes/channel_mixer/Fedus_2022_SwitchTransformer.md |
| zoph2022stmoe | ST-MoE | 是 | Notes/channel_mixer/Zoph_2022_STMoE.md |
| zhou2022mixture | Expert Choice Routing | 是 | Notes/channel_mixer/Zhou_2022_ExpertChoice.md |
| wang2024auxiliary | Aux-Loss-Free Load Balancing | 是 | Notes/channel_mixer/Wang_2024_AuxLossFree.md |
| jiang2024mixtral | Mixtral of experts | 是 | Notes/channel_mixer/Jiang_2024_Mixtral.md |
| dai2024deepseekmoe | DeepSeekMoE | 是 | Notes/channel_mixer/Dai_2024_DeepSeekMoE.md |
| deepseekv2_2024 | DeepSeek-V2 | 是 | Notes/channel_mixer/DeepSeekAI_2024_DeepSeekV2.md |
| databricks2024dbrx | DBRX | 是 | Notes/channel_mixer/Databricks_2024_DBRX.md |
| muennighoff2024olmoe | OLMoE | 是 | Notes/channel_mixer/Muennighoff_2024_OLMoE.md |
| wei2024skyworkmoe | Skywork-MoE | 是 | Notes/channel_mixer/Wei_2024_SkyworkMoE.md |
| lieber2024jamba | Jamba | 是 | Notes/channel_mixer/Lieber_2024_Jamba.md |
| raposo2024mixture | Mixture-of-Depths | 是 | Notes/channel_mixer/Raposo_2024_MoD.md |
| liu2023deja | Deja Vu: Contextual sparsity | 是 | Notes/channel_mixer/Liu_2023_DejaVu.md |
| zhang2022moefication | MoEfication | 是 | Notes/channel_mixer/Zhang_2022_MoEfication.md |
| liu2024kan | KAN: Kolmogorov-Arnold Networks | 是 | Notes/channel_mixer/Liu_2024_KAN.md |
| duollm2024 | Duo-LLM | 是 | Notes/channel_mixer/DuoLLM_2024.md |
| cai2024survey | A survey on MoE in LLMs | 否 | — (综述类) |

### Normalization
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| ioffe2015batch | Batch Normalization | 是 | Notes/normalization/N01_BatchNorm_Ioffe2015.md |
| ba2016layer | Layer Normalization | 是 | Notes/normalization/N02_LayerNorm_Ba2016.md |
| ulyanov2016instance | Instance Normalization | 是 | Notes/normalization/N03_InstanceNorm_Ulyanov2016.md |
| wu2018group | Group Normalization | 是 | Notes/normalization/N04_GroupNorm_Wu2018.md |
| xiong2020layer | On Layer Normalization in the Transformer Architecture | 是 | Notes/normalization/N05_PreLN_PostLN_Xiong2020.md |
| xu2019understanding | Understanding and Improving Layer Normalization (AdaNorm) | 是 | Notes/normalization/N06_AdaNorm_Xu2019.md |
| ding2021cogview | CogView: Sandwich LN | 是 | Notes/normalization/N07_SandwichLN_CogView_Ding2021.md |
| wang2022magneto | Foundation Transformers (MAGNETO/SubLN) | 是 | Notes/normalization/N20_MAGNETO_SubLN_Wang2022.md |
| kim2025periln | Peri-LN | 是 | Notes/normalization/N21_PeriLN_2025.md |
| zhang2019root | RMSNorm | 是 | Notes/normalization/N09_RMSNorm_Zhang2019.md |
| nguyen2019transformers | ScaleNorm/FixNorm | 是 | Notes/normalization/N22_ScaleNorm_FixNorm_Nguyen2019.md |
| shen2020powernorm | PowerNorm | 是 | Notes/normalization/N23_PowerNorm_Shen2020.md |
| henry2020query | QK-Norm | 是 | Notes/normalization/N10_QKNorm_Henry2020.md |
| peebles2023scalable | AdaLN (DiT) | 是 | Notes/normalization/N11_AdaLN_DiT_Peebles2023.md |
| loshchilov2024ngpt | nGPT | 是 | Notes/normalization/N25_nGPT_Loshchilov2024.md |
| gemma2024improving | Gemma 2 (Pre+Post Norm) | 是 | Notes/normalization/N26_Gemma2_PrePostNorm_2024.md |
| liu2020evolving | EvoNorm | 是 | Notes/normalization/N12_EvoNorm_Liu2020.md |
| zhang2019fixup | Fixup Initialization | 是 | Notes/normalization/N13_Fixup_Zhang2019.md |
| brock2021high | NFNet | 是 | Notes/normalization/N15_NFNet_Brock2021.md |
| zhu2025transformers | DyT: Transformers without normalization | 是 | Notes/normalization/N16_DyT_Zhu2025.md |
| chen2025stronger | Derf: Stronger Normalization-Free Transformers | 是 | Notes/normalization/N17_Derf_Chen2025.md |
| ye2024differential | Differential Transformer | 是 | Notes/normalization/N24_DiffTransformer_GroupNorm_Ye2024.md |
### Position Encoding
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| gehring2017convolutional | Convolutional sequence to sequence learning | 否 | — |
| kazemnejad2023impact | The impact of positional encoding on length generalization (NoPE) | 是 | Notes/position_encoding/Kazemnejad_2023_NoPE.md |
| su2024roformer | RoFormer: RoPE | 是 | Notes/position_encoding/Su_2021_RoPE.md |
| golovneva2024contextual | CoPE: Contextual Position Encoding | 是 | Notes/position_encoding/Golovneva_2024_CoPE.md |
| gopalakrishnan2025decoupling | PoPE: Polar Coordinate Positional Embeddings | 是 | Notes/position_encoding/Gopalakrishnan_2025_PoPE.md |
| press2021train | ALiBi | 是 | Notes/position_encoding/Press_2022_ALiBi.md |
| lin2025forgetting | Forgetting Transformer | 是 | Notes/position_encoding/Lin_2025_Forgetting_Transformer.md |
| tan2024stick | Stick-breaking attention | 是 | Notes/position_encoding/Rule_2025_Stick_Breaking.md |
| chen2023extending | Position Interpolation (PI) | 是 | Notes/position_encoding/Chen_2023_Position_Interpolation.md |
| peng2023yarn | YaRN | 是 | Notes/position_encoding/Peng_2023_YaRN.md |
| shaw2018self | Relative position representations (Shaw) | 是 | Notes/position_encoding/02_Shaw2018_RelativePE.md |
| dai2019transformerxl | Transformer-XL | 是 | Notes/position_encoding/03_Dai2019_TransformerXL.md |
| likhomanenko2021cape | CAPE | 是 | Notes/position_encoding/Likhomanenko_2021_CAPE.md |
| sun2023length | xPos | 是 | Notes/position_encoding/Sun_2022_XPOS.md |
| raffel2020exploring | T5 Relative Bias | 是 | Notes/position_encoding/Raffel_2020_T5_Relative_Bias.md |
| he2021deberta | DeBERTa | 是 | Notes/position_encoding/05_He2021_DeBERTa.md |
| chi2022kerple | KERPLE | 是 | Notes/position_encoding/Chi_2022_KERPLE.md |
| li2024fire | FIRE | 是 | Notes/position_encoding/Li_2024_FIRE.md |
| ruoss2023randomized | Randomized Positional Encodings | 是 | Notes/position_encoding/13_Ruoss2023_RandomizedPE.md |
| chen2024clex | CLEX | 是 | Notes/position_encoding/17_CLEX_Chen2024.md |
| ding2024longrope | LongRoPE | 是 | Notes/position_encoding/Ding_2024_LongRoPE.md |
| longrope2_2025 | LongRoPE2 | 是 | Notes/position_encoding/16_LongRoPE2_Microsoft_2025.md |
| gelberg2026drope | DroPE | 是 | Notes/position_encoding/17_DroPE_SakanaAI_2025.md |
| path2025 | PaTH Attention | 是 | Notes/position_encoding/20_PaTH_Attention_MIT_IBM_2025.md |
| qwen2vl2024 | Qwen2-VL (M-RoPE) | 是 | Notes/position_encoding/16_MRoPE_Qwen2VL_2024.md |

### Residual Connection
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| he2016deep | ResNet | 是 | Notes/residual_connection/17_ResNet_He2016.md |
| zhu2024hyper | Hyper-Connections | 是 | Notes/residual_connection/19_HyperConnections_Zhu2024.md |
| xie2025mhc | mHC: Manifold-constrained Hyper-Connections | 是 | Notes/residual_connection/20_mHC_Xie2025.md |
| xiao2025muddformer | MUDDFormer | 是 | Notes/residual_connection/24_MUDDFormer_Xiao2025.md |
| pagliardini2024denseformer | DenseFormer | 是 | Notes/residual_connection/23_DenseFormer_Pagliardini2024.md |
| menghani2024laurel | LAuReL | 是 | Notes/residual_connection/30_LAuReL_Menghani2024.md |
| mak2025residual | Residual Matrix Transformers | 否 | — |
| heddes2025deepcrossattention | DeepCrossAttention (DCA) | 是 | Notes/residual_connection/25_DCA_Heddes2025.md |
| fang2023cross | MRLA: Cross-layer retrospective retrieving | 是 | Notes/residual_connection/22_MRLA_Fang2023.md |
| chai2020highway | Highway Transformer | 是 | Notes/residual_connection/29_HighwayTransformer_Chai2020.md |
| srivastava2015highway | Highway Networks | 否 | — (基础参考) |
| srivastava2015training | Training very deep networks | 否 | — (基础参考) |
| huang2017densely | DenseNet | 否 | — (基础参考) |
| huang2016deep | Stochastic Depth | 否 | — (基础参考) |
| bachlechner2021rezero | ReZero | 是 | Notes/residual_connection/01_ReZero_Bachlechner2020.md |
| huang2020tfixup | T-Fixup | 是 | Notes/residual_connection/31_TFixup_Huang2020.md |
| parisotto2020stabilizing | GTrXL | 是 | Notes/residual_connection/10_GTrXL_Parisotto2020.md |
| kimi2026attnres | Attention Residuals (AttnRes) | 是 | Notes/residual_connection/28_AttnRes_Kimi2026.md |
| sun2024yoco | YOCO | 否 | — (token_mixer有覆盖) |
| brandon2024reducing | CLA: Cross-Layer Attention | 是 | Notes/residual_connection/15_CrossLayerAttention_Brandon2024.md |
| he2020realformer | RealFormer | 是 | Notes/residual_connection/27_RealFormer_He2020.md |
| zhou2024value | Value Residual Learning (ResFormer) | 是 | Notes/residual_connection/26_ResFormer_Zhou2024.md |
| oh2025revisiting | ORU: Orthogonal Residual Update | 否 | — |
| men2024shortgpt | ShortGPT | 否 | — |
| sun2025curse | The Curse of Depth | 是 | Notes/residual_connection/07_CurseOfDepth_Sun2025.md |
| gomhc2026 | go-mHC | 是 | Notes/residual_connection/21_goMHC_2026.md |
| wang2026fusenorm | FuseNorm | 否 | — (module_sequence有覆盖) |
| dehghani2019universal | Universal Transformers | 是 | Notes/residual_connection/12_UniversalTransformer_Dehghani2019.md |
| fan2020reducing | LayerDrop | 是 | Notes/residual_connection/11_LayerDrop_Fan2020.md |
| elbayad2020depth | Depth-Adaptive Transformer | 是 | Notes/residual_connection/14_DepthAdaptive_Elbayad2020.md |
### Module Sequence
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| liu2020understanding | Understanding the Difficulty of Training Transformers | 是 | Notes/module_sequence/02_Liu2020_Understanding_Difficulty_Training.md |
| wang2024deepnet | DeepNet: Scaling transformers to 1000 layers | 是 | Notes/module_sequence/17_Wang2022_DeepNet.md |
| he2023simplifying | Simplifying Transformer Blocks | 是 | Notes/module_sequence/16_He2023_Simplifying_Transformer_Blocks.md |
| de2020batch | Batch normalization biases residual blocks | 否 | — |
| noci2023shaped | The Shaped Transformer | 否 | — |
| press2020sandwich | Sandwich Transformer | 是 | Notes/module_sequence/04_Press2020_Sandwich_Transformer.md |
| shleifer2022normformer | NormFormer | 是 | Notes/module_sequence/06_Shleifer2021_NormFormer.md |
| xie2023residual | ResiDual | 否 | — (residual_connection有覆盖) |
| chen2024mixln | Mix-LN | 是 | Notes/module_sequence/14_Chen2024_MixLN.md |
| chowdhery2022palm | PaLM (Parallel Attention+FFN) | 是 | Notes/module_sequence/08_Chowdhery2022_PaLM.md |
| so2021primer | Primer: Searching for Efficient Transformers | 是 | Notes/module_sequence/07_So2021_Primer.md |
| zhou2023brainformers | Brainformers | 是 | Notes/module_sequence/12_Zhou2023_Brainformers.md |
| he2023deep | Deep Transformers without Shortcuts | 否 | — |
| liu2022swinv2 | Swin Transformer V2 | 是 | Notes/module_sequence/11_Liu2022_SwinV2.md |
| wang2024whatmatters | What Matters in Transformers? Not All Attention is Needed | 否 | — |

### Tech Reports
| bib key | 论文标题 | 有笔记? | 笔记路径 |
|---------|---------|---------|---------|
| grattafiori2024llama3 | Llama 3 | 是 | Notes/tech_reports/Meta_Llama3.md |
| openai2023gpt4 | GPT-4 technical report | 否 | — |
| yang2024qwen25 | Qwen2.5 technical report | 是 | Notes/tech_reports/Alibaba_Qwen25.md |
| yang2025qwen3 | Qwen3 technical report | 是 | Notes/tech_reports/Alibaba_Qwen3.md |
| gemma2025gemma3 | Gemma 3 technical report | 是 | Notes/tech_reports/Google_Gemma3.md |
| efficientattn2025survey | Efficient attention mechanisms survey | 否 | — (综述类) |
| moesurveyfull2025 | Comprehensive survey of MoE | 否 | — (综述类) |
| minimax2025 | MiniMax-01 | 是 | Notes/tech_reports/MiniMax_01.md |

### 笔记中有但 bib 中缺失的条目

以下笔记文件在 Notes/ 中存在，但在 reference.bib 中没有对应的 bib 条目：

| 笔记文件 | 可能需要补充 bib? |
|---------|---------|
| Notes/channel_mixer/01AI_2024_YiLightning.md | 是 (Yi-Lightning) |
| Notes/channel_mixer/DeepSeek_2025_DeepEP.md | 是 (DeepEP) |
| Notes/channel_mixer/DirMoE_2025.md | 是 (DirMoE) |
| Notes/channel_mixer/ExpertPruning_2024_Survey.md | 视情况 |
| Notes/channel_mixer/He_2024_MillionExperts.md | 是 |
| Notes/channel_mixer/Meta_2025_Llama4.md | 是 (Llama 4) |
| Notes/channel_mixer/MiniMax_2025_MiniMax01.md | 已有 minimax2025 |
| Notes/channel_mixer/MoE_DoublePenalty_2026.md | 是 |
| Notes/channel_mixer/PolyGLU_2026.md | 是 |
| Notes/channel_mixer/Puigcerver_2023_SoftMoE.md | 是 (Soft MoE) |
| Notes/channel_mixer/Puigcerver_2024_SoftMoE.md | 是 (Soft MoE v2) |
| Notes/channel_mixer/Qwen3_2025_MoE.md | 已有 yang2025qwen3 |
| Notes/channel_mixer/SharedExpert_vs_NoShared_2025.md | 视情况 |
| Notes/channel_mixer/Wang_2024_ReMoE.md | 是 (ReMoE) |
| Notes/channel_mixer/Tencent_2024_HunyuanLarge.md | 是 |
| Notes/channel_mixer/Zhong_2024_Lory.md | 是 (Lory) |
| Notes/token_mixer/beck_2024_xlstm.md | 是 (xLSTM) |
| Notes/token_mixer/de_2024_griffin_hawk.md | 是 (Griffin/Hawk) |
| Notes/token_mixer/poli_2023_hyena.md | 是 (Hyena) |
| Notes/token_mixer/poli_2023_stripedhyena.md | 是 (StripedHyena) |
| Notes/token_mixer/qin_2024_hgrn2.md | 是 (HGRN2) |
| Notes/token_mixer/qin_2024_lightning2.md | 是 (Lightning Attention 2) |
| Notes/token_mixer/qin_2024_transnormerllm.md | 是 (TransNormerLLM) |
| Notes/token_mixer/yang_2024_gla.md | 是 (GLA) |
| Notes/token_mixer/yang_2024_deltanet.md | 是 (DeltaNet) |
| Notes/token_mixer/sun_2024_yoco.md | 已有 sun2024yoco |
| Notes/token_mixer/ma_2023_mega.md | 是 (MEGA) |
| Notes/token_mixer/munkhdalai_2024_infini_attention.md | 是 (Infini-Attention) |
| Notes/token_mixer/liu_2023_ring_attention.md | 是 (Ring Attention) |
| Notes/token_mixer/cai_2024_pyramidkv.md | 是 (PyramidKV) |
| Notes/token_mixer/li_2024_snapkv.md | 是 (SnapKV) |
| Notes/token_mixer/liu_2024_minicache.md | 是 (MiniCache) |
| Notes/token_mixer/peng_2025_rwkv7.md | 是 (RWKV-7) |
| Notes/token_mixer/baichuan_2025_temporal_conv_kv.md | 是 |
| Notes/token_mixer/brandon_2024_cla.md | 已有 brandon2024reducing |
| Notes/normalization/N28_NormAttentionDynamics_Karagodin2025.md | 是 |
| Notes/normalization/N29_EnhancedQKNorm_LopezRubio2026.md | 是 |
| Notes/normalization/N30_GeoNorm_2026.md | 是 |
| Notes/normalization/N31_HybridNorm_2025.md | 是 |
| Notes/normalization/N32_UnitNorm_2024.md | 是 |
| Notes/normalization/N33_OutlierDrivenRescaling_2026.md | 是 |
| Notes/normalization/N34_FOG_FP8Norm_2025.md | 是 |
| Notes/normalization/N35_WhyLowPrecisionFails_2025.md | 是 |
| Notes/normalization/N36_MuonOptimizer_NormFree_2025.md | 是 |
| Notes/normalization/N37_SiameseNorm_2026.md | 是 |
| Notes/position_encoding/15_iRoPE_Llama4_2025.md | 是 (iRoPE) |
| Notes/position_encoding/21_3D_RPE_Yang_2024.md | 是 |
| Notes/position_encoding/22_Wavelet_PE_Oka_2025.md | 是 |

---
## 2. 各方向遗漏检查

### Token Mixer

**注意力变体覆盖情况：**
- 标准 Multi-Head Attention (Vaswani 2017): 已覆盖
- GQA (Ainslie 2023): 已覆盖
- MQA (Shazeer 2019): 已覆盖
- MLA (DeepSeek-V2 2024): 已覆盖
- 线性注意力 (Katharopoulos 2020, Based): 已覆盖
- 稀疏注意力 (Reformer, Longformer, NSA, MoBA): 已覆盖
- SSM (S4, Mamba, Mamba-2): 已覆盖
- 混合架构 (Jamba): 已覆盖
- Sigmoid Attention: 已覆盖
- Differential Transformer: 已覆盖
- Gated Attention / CogAttention: 已覆盖
- RWKV 系列 (v1-v7): 已覆盖 (笔记中有 v7，但 bib 缺 RWKV-7 条目)
- RetNet: 已覆盖
- Gated Delta Networks: 已覆盖

**FlashAttention 系列：**
- FlashAttention-1: 已覆盖
- FlashAttention-2: 已覆盖
- FlashAttention-3: 已覆盖
- PagedAttention (vLLM): 笔记有 (kwon_2023_pagedattention.md)，bib 缺失
- Ring Attention: 笔记有，bib 缺失
- Lightning Attention: 笔记有，bib 缺失

**KV Cache 压缩方法：**
- MQA/GQA/MLA (结构级压缩): 已覆盖
- CLA (Cross-Layer Attention): 已覆盖
- SnapKV: 笔记有，bib 缺失
- PyramidKV: 笔记有，bib 缺失
- MiniCache: 笔记有，bib 缺失
- 可能遗漏: H2O (Heavy-Hitter Oracle, Zhang et al. 2023)、StreamingLLM (Xiao et al. 2023)、KIVI (量化KV Cache)、GQA-to-MLA 转换方法

**可能遗漏的重要论文：**
1. xLSTM (Beck et al. 2024) — 笔记有，bib 缺失
2. Griffin/Hawk (De et al. 2024) — 笔记有，bib 缺失
3. Hyena / StripedHyena (Poli et al. 2023) — 笔记有，bib 缺失
4. HGRN2 (Qin et al. 2024) — 笔记有，bib 缺失
5. GLA (Gated Linear Attention, Yang et al. 2024) — 笔记有，bib 缺失
6. DeltaNet (Yang et al. 2024) — 笔记有，bib 缺失
7. MEGA (Ma et al. 2023) — 笔记有，bib 缺失
8. Infini-Attention (Munkhdalai et al. 2024) — 笔记有，bib 缺失
9. TransNormerLLM (Qin et al. 2024) — 笔记有，bib 缺失
10. RWKV-7 (Peng et al. 2025) — 笔记有，bib 缺失
11. H2O: Heavy-Hitter Oracle (Zhang et al. 2023) — 笔记和 bib 均缺失
12. StreamingLLM (Xiao et al. 2023) — 笔记和 bib 均缺失
13. Sparse Transformer (Child et al. 2019) — 笔记和 bib 均缺失 (经典稀疏注意力)

### Channel Mixer

**激活函数覆盖情况：**
- ReLU (Agarap 2018): 已覆盖 (bib有，无独立笔记但属基础知识)
- GELU (Hendrycks 2016): 已覆盖 (bib有)
- SwiGLU (Shazeer 2020): 已覆盖 (bib有)
- GeGLU: 包含在 Shazeer 2020 GLU variants 中，已覆盖
- GLU (Dauphin 2017): 已覆盖
- Swish/SiLU (Ramachandran 2017): 已覆盖
- ReLU^2 (Zhang 2024): 已覆盖
- PolyGLU: 笔记有，bib 缺失

**MoE 路由策略覆盖情况：**
- Top-k routing (Shazeer 2017): 已覆盖
- Expert Choice (Zhou 2022): 已覆盖
- Aux-Loss-Free (Wang 2024): 已覆盖
- GShard top-2 (Lepikhin 2020): 已覆盖
- Switch Transformer top-1 (Fedus 2022): 已覆盖
- ST-MoE (Zoph 2022): 已覆盖
- DeepSeekMoE shared expert (Dai 2024): 已覆盖

**Soft MoE / 新方法：**
- Soft MoE (Puigcerver 2023/2024): 笔记有，bib 缺失
- ReMoE (Wang 2024): 笔记有，bib 缺失
- DirMoE (2025): 笔记有，bib 缺失
- Lory (Zhong 2024): 笔记有，bib 缺失

**可能遗漏的重要论文：**
1. Soft MoE (Puigcerver et al. 2023) — 笔记有，bib 缺失，这是重要方法
2. ReMoE — 笔记有，bib 缺失
3. Sigma-MoE (Csordas et al. 2024) — 笔记和 bib 均缺失
4. MoE-Mamba (Pioro et al. 2024) — 笔记和 bib 均缺失 (MoE+SSM 混合)
5. PolyGLU (2026) — 笔记有，bib 缺失

### Normalization

**基础方法覆盖情况：**
- LayerNorm (Ba 2016): 已覆盖
- RMSNorm (Zhang 2019): 已覆盖
- DyT (Zhu 2025): 已覆盖
- Derf (Chen 2025): 已覆盖
- nGPT (Loshchilov 2024): 已覆盖
- BatchNorm / InstanceNorm / GroupNorm: 已覆盖

**QK-Norm 覆盖情况：**
- QK-Norm (Henry 2020): 已覆盖
- ViT-22B QK-Norm (Dehghani 2023): 已覆盖
- Enhanced QK-Norm (Lopez-Rubio 2026): 笔记有，bib 缺失
- Norm Attention Dynamics (Karagodin 2025): 笔记有，bib 缺失

**其他已覆盖：**
- AdaNorm, AdaLN, Sandwich LN, DeepNorm, MAGNETO/SubLN, Peri-LN
- ScaleNorm/FixNorm, PowerNorm, EvoNorm
- Fixup, NFNet, Gemma2 Pre+Post Norm

**可能遗漏的重要论文：**
1. GeoNorm (2026) — 笔记有，bib 缺失
2. HybridNorm (2025) — 笔记有，bib 缺失
3. SiameseNorm (2026) — 笔记有，bib 缺失
4. UnitNorm (2024) — 笔记有，bib 缺失
5. FOG/FP8Norm (2025) — 笔记有，bib 缺失 (低精度训练相关)
6. Outlier-Driven Rescaling (2026) — 笔记有，bib 缺失
7. Muon Optimizer Norm-Free (2025) — 笔记有，bib 缺失

### Position Encoding

**RoPE 及其扩展覆盖情况：**
- RoPE (Su 2021): 已覆盖
- YaRN (Peng 2023): 已覆盖
- PI / Position Interpolation (Chen 2023): 已覆盖
- NTK / Dynamic NTK / ABF: 笔记有 (14_NTK_DynamicNTK_ABF.md)，bib 缺失 (社区方法，无正式论文)
- LongRoPE (Ding 2024): 已覆盖
- LongRoPE2 (2025): 已覆盖
- CLEX (Chen 2024): 已覆盖
- xPos (Sun 2023): 已覆盖
- DroPE (Gelberg 2026): 已覆盖
- iRoPE (Llama 4, 2025): 笔记有，bib 缺失
- M-RoPE (Qwen2-VL): 已覆盖

**ALiBi / CoPE / NoPE 覆盖情况：**
- ALiBi (Press 2021): 已覆盖
- CoPE (Golovneva 2024): 已覆盖
- NoPE (Kazemnejad 2023): 已覆盖

**其他已覆盖：**
- Sinusoidal PE, Shaw Relative PE, Transformer-XL, T5 Relative Bias, DeBERTa
- CAPE, KERPLE, FIRE, Randomized PE
- Forgetting Transformer, Stick-breaking Attention, PaTH Attention, PoPE

**可能遗漏的重要论文：**
1. iRoPE (Llama 4) — 笔记有，bib 缺失
2. 3D RPE (Yang 2024) — 笔记有，bib 缺失
3. Wavelet PE (Oka 2025) — 笔记有，bib 缺失
4. Sandwich frequency encoding — 笔记和 bib 均缺失 (较新方法)

### Residual Connection

**Width / Depth / Control 三个子维度覆盖情况：**

**Width (残差流宽度)：**
- Hyper-Connections (Zhu 2024): 已覆盖
- mHC (Xie 2025): 已覆盖
- go-mHC (2026): 已覆盖
- DenseFormer (Pagliardini 2024): 已覆盖
- MUDDFormer (Xiao 2025): 已覆盖
- DCA / DeepCrossAttention (Heddes 2025): 已覆盖
- MRLA (Fang 2023): 已覆盖
- ResFormer / Value Residual (Zhou 2024): 已覆盖
- RealFormer (He 2020): 已覆盖
- LAuReL (Menghani 2024): 已覆盖
- Residual Matrix Transformers (Mak 2025): bib 有，笔记缺失
- AttnRes (Kimi 2026): 已覆盖

**Depth (深度自适应)：**
- Universal Transformer (Dehghani 2019): 已覆盖
- LayerDrop (Fan 2020): 已覆盖
- Mixture-of-Depths (Raposo 2024): 已覆盖
- Depth-Adaptive Transformer (Elbayad 2020): 已覆盖
- CLA / Cross-Layer Attention (Brandon 2024): 已覆盖
- Stochastic Depth (Huang 2016): 已覆盖 (bib有)
- ShortGPT (Men 2024): bib 有，笔记缺失
- Curse of Depth (Sun 2025): 已覆盖

**Control (残差缩放/门控)：**
- ReZero (Bachlechner 2021): 已覆盖
- T-Fixup (Huang 2020): 已覆盖
- GTrXL (Parisotto 2020): 已覆盖
- Fixup (Zhang 2019): 已覆盖
- SkipInit (De & Smith 2020): 已覆盖
- Highway Transformer (Chai 2020): 已覆盖
- ORU (Oh 2025): bib 有，笔记缺失

**可能遗漏的重要论文：**
1. 无明显重大遗漏，覆盖较为全面

### Module Sequence

**Pre-Norm vs Post-Norm 覆盖情况：**
- Pre-Norm 理论分析 (Xiong 2020): 已覆盖
- Post-Norm 训练困难 (Liu 2020): 已覆盖
- DeepNet (Wang 2022): 已覆盖
- Mix-LN (Chen 2024): 已覆盖
- ResiDual (Xie 2023): 已覆盖
- FuseNorm (Wang 2026): bib 有，module_sequence 笔记有 (17_FuseNorm_2025.md)

**Simplified Transformer 覆盖情况：**
- Simplifying Transformer Blocks (He & Hofmann 2023): 已覆盖
- Deep Transformers without Shortcuts (He et al. 2023): bib 有，笔记缺失

**Parallel Attention+FFN 覆盖情况：**
- PaLM parallel (Chowdhery 2022): 已覆盖
- GPT-J parallel: 笔记有 (09_Wang2021_GPT_J.md)
- Primer (So 2021): 已覆盖
- Brainformers (Zhou 2023): 已覆盖

**其他已覆盖：**
- Sandwich Transformer, NormFormer, MAGNETO, Swin V2
- Gemma 2 interleaved local/global attention
- Jamba hybrid interleaved
- MiniMax-01 non-uniform sequence
- Attention-only Transformers

**可能遗漏的重要论文：**
1. Macaron Net (Lu et al. 2019) — 笔记有 (02_lu2019_macaron.md)，bib 缺失
2. 无其他明显重大遗漏

---

## 3. 建议补充的论文

### 高优先级 (笔记已有，仅需补充 bib 条目)

1. **Soft MoE** — Puigcerver et al. 2023/2024, 重要的 MoE 新范式
2. **xLSTM** — Beck et al. 2024, 重要的 RNN 复兴工作
3. **Griffin/Hawk** — De et al. 2024, Google 的 RNN-Transformer 混合
4. **Hyena** — Poli et al. 2023, 重要的长卷积替代方案
5. **GLA** — Yang et al. 2024, Gated Linear Attention
6. **RWKV-7** — Peng et al. 2025, RWKV 最新版本
7. **iRoPE** — Llama 4 (2025), Meta 的无显式位置编码方案
8. **PagedAttention** — Kwon et al. 2023 (vLLM), KV Cache 管理的重要工作
9. **SnapKV** — Li et al. 2024, KV Cache 压缩
10. **Ring Attention** — Liu et al. 2023, 分布式长序列训练
11. **Lightning Attention 2** — Qin et al. 2024, 线性注意力加速
12. **Infini-Attention** — Munkhdalai et al. 2024, Google 的无限上下文方案
13. **GeoNorm** — 2026, 新归一化方法
14. **SiameseNorm** — 2026, 新归一化方法
15. **HybridNorm** — 2025, 新归一化方法
16. **Macaron Net** — Lu et al. 2019, FFN-Attn-FFN 结构的先驱

### 中优先级 (笔记已有，可选补充)

17. **DeltaNet** — Yang et al. 2024
18. **HGRN2** — Qin et al. 2024
19. **TransNormerLLM** — Qin et al. 2024
20. **MEGA** — Ma et al. 2023
21. **StripedHyena** — Poli et al. 2023
22. **ReMoE** — Wang et al. 2024
23. **DirMoE** — 2025
24. **PolyGLU** — 2026
25. **PyramidKV** — Cai et al. 2024
26. **MiniCache** — Liu et al. 2024
27. **Enhanced QK-Norm** — Lopez-Rubio 2026
28. **FOG/FP8Norm** — 2025
29. **3D RPE** — Yang 2024
30. **Wavelet PE** — Oka 2025

### 低优先级 (笔记和 bib 均缺失，但领域内有一定影响力)

31. **H2O: Heavy-Hitter Oracle** — Zhang et al. 2023, KV Cache 驱逐策略
32. **StreamingLLM** — Xiao et al. 2023, 流式推理中的 attention sink
33. **Sparse Transformer** — Child et al. 2019, 经典稀疏注意力
34. **Sigma-MoE** — Csordas et al. 2024, sigmoid 门控 MoE
35. **MoE-Mamba** — Pioro et al. 2024, MoE + SSM 混合
36. **KIVI** — Liu et al. 2024, KV Cache 量化压缩

---

## 4. 统计摘要

| 类别 | bib 条目数 | 有笔记数 | 缺笔记数 | 笔记有但 bib 缺失 |
|------|-----------|---------|---------|-----------------|
| Survey | 6 | 1 | 5 (综述类正常) | 0 |
| Token Mixer | 27 | 25 | 2 | ~18 |
| Channel Mixer | 27 | 22 | 5 | ~12 |
| Normalization | 22 | 22 | 0 | ~10 |
| Position Encoding | 25 | 24 | 1 | ~3 |
| Residual Connection | 30 | 24 | 6 | 0 |
| Module Sequence | 15 | 11 | 4 | ~1 |
| Tech Reports | 8 | 6 | 2 | 0 |
| **合计** | **160** | **135** | **25** | **~44** |

**总体评估：** 综述在六大方向上的核心论文覆盖较为扎实，主要问题是 Token Mixer 和 Channel Mixer 方向有大量笔记已完成但尚未添加到 reference.bib 中。建议优先补充高优先级列表中的 16 篇 bib 条目，尤其是 Soft MoE、xLSTM、Griffin/Hawk、GLA、RWKV-7、iRoPE 和 PagedAttention 等在领域内影响力较大的工作。
