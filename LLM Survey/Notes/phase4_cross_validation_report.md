# Phase 4: 交叉验证报告

> 生成日期: 2026-04-05
> 检查范围: main.tex, reference.bib, 6 份 paper_list_*.md, 1 份 paper_list_tech_reports.md

---

## 一、引用完整性检查 (main.tex \cite{} vs reference.bib)

### 结论: 全部通过

逐一比对 main.tex 中约 130 个 `\cite{}` key 与 reference.bib 中的条目，**未发现缺失的 bib 条目**。所有引用均有对应的 bib entry。

### 注意事项
- `deepseekv2_2024_mla` 和 `deepseekv2_2024` 是同一篇论文的两个 bib key（均指向 arXiv:2405.04434），建议统一。
- `huang2020improving`（Normalization 章节 T-Fixup）和 `huang2020tfixup`（Residual 章节 T-Fixup）指向同一工作但使用不同 key，建议统一为一个。
- `dai2019transformerxl` 和 `dai2019transformer` 是同一篇论文的两个 key，目前 main.tex 只用了 `dai2019transformer`，`dai2019transformerxl` 冗余但无害。

---

## 二、大厂架构 vs 六大类别覆盖缺口

基于 paper_list_tech_reports.md 中 21 份技术报告的架构对比表，逐项检查六大类别论文清单的覆盖情况。

### 2.1 已覆盖的架构创新 (无缺口)

| 架构创新 | 使用模型 | 对应论文清单位置 |
|----------|----------|-----------------|
| MLA | DeepSeek-V2/V3 | token_mixer #5 |
| GQA | 几乎所有 | token_mixer #4 |
| SWA (Sliding Window) | Mistral, Gemma, Baichuan-M1 | token_mixer #7 |
| Lightning Attention | MiniMax-01 | token_mixer #14e, #29 |
| MQA | (历史参考) | token_mixer #3 |
| QK-Norm | Qwen3, Gemma 2/3, OLMo 2 | normalization N-10 |
| RMSNorm + Pre-Norm | 几乎所有 | normalization N-09, N-05 |
| Pre+Post RMSNorm | Gemma 2 | normalization N-26 |
| RoPE | 几乎所有 | position_encoding #2 |
| SwiGLU / GeGLU | 几乎所有 | channel_mixer A4 |
| DeepSeekMoE | DeepSeek-V2/V3 | channel_mixer C2 |
| Aux-loss-free balancing | DeepSeek-V3 | channel_mixer B7 |
| mHC | DeepSeek-V3 | residual_connection W2 |
| CLA (Cross-Layer Attention) | Hunyuan-Large, Yi-Lightning | residual_connection D12 |
| Logit soft-capping | Gemma 2 | 通过 Gemma 2 论文覆盖 |

### 2.2 覆盖缺口 (需补充)

| # | 架构创新 | 使用模型 | 所属类别 | 缺口描述 | 严重程度 |
|---|----------|----------|----------|----------|----------|
| 1 | iRoPE (RoPE+NoPE 3:1交替) | Llama 4 | Position Encoding | paper_list_PE #28 标记"待处理"，无独立论文（仅 Llama 4 tech report 描述），建议基于 Llama 4 报告补充笔记 | **高** |
| 2 | Temporal short conv on KV | Baichuan-M1 | Token Mixer | 六大类别中完全未覆盖。Baichuan-M1 在 KV 上施加时序短卷积是独特创新，无对应论文笔记 | **高** |
| 3 | 异构 MoE / 模态隔离路由 | ERNIE 4.5 | Channel Mixer | paper_list_CM E6 标记"新增"但无笔记，且无独立方法论文（仅 tech report）。模态隔离路由是新范式 | **中** |
| 4 | 2D RoPE (视觉) | ERNIE 4.5 | Position Encoding | 与 M-RoPE (Qwen2-VL) 不同的 2D 位置编码方案，未覆盖 | **中** |
| 5 | Differential RoPE frequencies per layer type | Gemma 3 | Position Encoding | Gemma 3 对 global 层用 base=1M、local 层用 base=10K，这种分层差异化 RoPE 频率策略无独立论文覆盖 | **中** |
| 6 | Expert-specific learning rate | Hunyuan-Large | Channel Mixer | 为不同专家设置不同学习率的训练策略，无对应论文 | **低** |
| 7 | Global-batch load balancing (无 shared expert) | Qwen3 | Channel Mixer | paper_list_CM E1 标记"新增"但无笔记。Qwen3 移除 shared expert + 全局批次均衡是重要设计选择 | **中** |
| 8 | M-RoPE (3D 多模态位置编码) | Qwen2-VL | Position Encoding | paper_list_PE #29 标记"待处理"，已在 main.tex 中引用但无笔记 | **低** |

---

## 三、各子类别覆盖均衡性分析

### 3.1 Token Mixer (31 篇)

| 子类别 | 论文数 | 评估 |
|--------|--------|------|
| Standard Dot-Product Attention | 2 | 适当 |
| KV Cache Optimization (MQA/GQA/MLA) | 3 | 适当 |
| Sparse Attention (SWA/NSA/MoBA) | 4 | 适当 |
| Linear Attention (Kernel/GLA/DeltaNet/HGRN2/Lightning) | 8 | 充足 |
| Negative Weights (Diff Transformer/CogAttn) | 2 | 适当 |
| Different Activation (Sigmoid Attention) | 1 | **薄弱** — 仅 1 篇 |
| RNN-Like / SSM (S4/Mamba/RWKV/RetNet/GDN) | 7 | 充足 |
| Hybrid Architectures | 1 | **薄弱** — 仅 Jamba，缺 Zamba、Griffin、RecurrentGemma 等 |
| Hardware-Efficient (FlashAttention 1/2/3 + PagedAttn) | 4 | 适当 |
| Industrial Lightning Attention | 1 | 适当 (与 Linear Attention 合并看) |

### 3.2 Channel Mixer (33 篇)

| 子类别 | 论文数 | 评估 |
|--------|--------|------|
| FFN & Activation Functions | 6 | 充足 |
| MoE Foundations & Routing | 7 | 充足 |
| MoE Application Models 2024 | 9 | 充足 |
| MoE Application Models 2025 | 7 | 适当 (多为新增待完善) |
| Conditional Computation & FFN Alternatives | 5 | 适当 |
| MoE Survey | 1 | 适当 |
| **缺失: Soft MoE / Token Merging** | 0 | **薄弱** — Soft MoE (Puigcerver 2024) 未收录 |

### 3.3 Normalization (29 篇)

| 子类别 | 论文数 | 评估 |
|--------|--------|------|
| Foundation (BN/LN/IN/GN) | 4 | 充足 |
| Placement & Theory | 8 | 充足 |
| Efficient Variants (RMSNorm/ScaleNorm/PowerNorm) | 3 | 适当 |
| Attention-Internal (QK-Norm/DiffTransformer/Lp-Norm) | 3 | 适当 |
| Conditional/Adaptive (adaLN) | 1 | **薄弱** — 仅 DiT 的 adaLN |
| Holistic (nGPT/Gemma2) | 2 | 适当 |
| Automated Search (EvoNorm) | 1 | 适当 (领域较窄) |
| Normalization-Free (Fixup/T-Fixup/NF-Net/DyT/Derf) | 5 | 充足 |

### 3.4 Position Encoding (约 29 篇，去重后)

| 子类别 | 论文数 | 评估 |
|--------|--------|------|
| NoPE | 1 | 适当 (领域较窄) |
| Absolute PE (Sinusoidal/Learned/CAPE) | 3 | 适当 |
| Rotation-based Relative PE (RoPE/xPos/PoPE/CoPE) | 4 | 充足 |
| Attention Matrix Bias (Shaw/T-XL/T5/DeBERTa/ALiBi/KERPLE/FIRE/Rand) | 8 | 充足 |
| RoPE Context Extension (PI/NTK/YaRN/CLEX/LongRoPE/LongRoPE2/DroPE) | 7-8 | 充足 |
| Self-Modulator / Implicit PE (FoX/Stick-breaking) | 2 | 适当 |
| Content-Aware PE (PaTH) | 1 | **薄弱** — 仅 1 篇且待处理 |
| Multimodal PE (M-RoPE) | 1 | **薄弱** — 待处理 |
| iRoPE / Hybrid | 1 | **薄弱** — 待处理 |

### 3.5 Residual Connection (42 篇) — Focus Area

| 子类别 | 论文数 | 评估 |
|--------|--------|------|
| Foundation (ResNet/Highway/DenseNet/StochasticDepth) | 4 | 充足 |
| Width (HC/mHC/go-mHC/GPT-J/ResidualMatrix) | 5 | 充足 |
| Depth — Cross-Layer (MRLA/DenseFormer/MuddFormer/DCA/etc.) | 13 | 充足 |
| Control (ReZero/Fixup/DeepNorm/GTrXL/Highway/etc.) | 15 | 充足 |
| Theory (ORU/ShortGPT) | 2 | 适当 |
| Norm-Residual Interaction (Mix-LN/FuseNorm) | 2 | 适当 |

### 3.6 Module Sequence (26+ 篇)

| 子类别 | 论文数 | 评估 |
|--------|--------|------|
| Post-Norm vs Pre-Norm 基础 | 6 | 充足 |
| Unification & Hybrid (ResiDual/Sandwich/Peri-LN/Mix-LN) | 6 | 充足 |
| Simplified Transformer | 4 | 适当 |
| Parallel Sub-layers (GPT-J/PaLM/ViT-22B) | 3 | 适当 |
| Architecture Search (Primer/Brainformers) | 2 | 适当 |
| Residual Initialization (ReZero/Fixup) | 2 | 适当 |
| ODE Theory (Macaron) | 1 | **薄弱** — 仅 1 篇 |
| Norm Removal Impact (DyT/nGPT) | 2 | 适当 |

---

## 四、建议补充的论文列表

### 优先级 Tier 1 (高优先 — 填补大厂架构覆盖缺口)

| # | 论文/来源 | 所属类别 | 理由 |
|---|-----------|----------|------|
| 1 | **Llama 4 Tech Report** (arXiv:2601.11659) — iRoPE 笔记 | Position Encoding | iRoPE 是 2025 年最重要的 PE 创新之一，实现 10M context，当前仅标记"待处理" |
| 2 | **Baichuan-M1** (arXiv:2502.12671) — temporal conv on KV 分析 | Token Mixer | 六大类别完全未覆盖的独特创新 |
| 3 | **ERNIE 4.5 Tech Report** — 异构 MoE + 模态隔离路由 | Channel Mixer | 新型 MoE 路由范式，当前仅标记"新增" |
| 4 | **Qwen3 Tech Report** (arXiv:2505.09388) — 无 shared expert + global-batch 均衡 | Channel Mixer | 与 DeepSeek-V3 的 shared expert 设计形成重要对比 |

### 优先级 Tier 2 (中优先 — 填补子类别薄弱环节)

| # | 论文 | 所属类别 | 理由 |
|---|------|----------|------|
| 5 | **Griffin** (De Mesmay et al., 2024) 或 **RecurrentGemma** | Token Mixer / Hybrid | Hybrid 子类别仅 Jamba 1 篇，缺少 Google 的混合架构代表 |
| 6 | **Zamba** (Zyphra, 2024) | Token Mixer / Hybrid | 另一种 Mamba-Attention 混合方案 |
| 7 | **Soft MoE** (Puigcerver et al., 2024) | Channel Mixer | 完全可微的 MoE 路由，当前清单未收录 |
| 8 | **M-RoPE / Qwen2-VL** (arXiv:2409.12191) 笔记 | Position Encoding | 多模态 PE 子类别仅 1 篇且待处理 |
| 9 | **PaTH Attention** (MIT-IBM, NeurIPS 2025) 笔记 | Position Encoding | Content-Aware PE 子类别仅 1 篇且待处理 |
| 10 | **CLEX** (arXiv:2310.16450) 笔记 | Position Encoding | RoPE 扩展中 ODE 方法的代表，当前待处理 |

### 优先级 Tier 3 (低优先 — 完善性补充)

| # | 论文 | 所属类别 | 理由 |
|---|------|----------|------|
| 11 | **Gemma 3** (arXiv:2503.19786) — 分层差异化 RoPE 频率分析 | Position Encoding | global/local 层不同 RoPE base 的工程实践 |
| 12 | **Conditional Computation Survey** (如 Bengio 2013 或最新综述) | Channel Mixer | 条件计算理论基础 |
| 13 | **ODE/SDE 理论** 补充 (如 Neural ODE, Chen 2018) | Module Sequence | ODE Theory 子类别仅 Macaron 1 篇 |
| 14 | **DroPE** (arXiv:2512.12167) 笔记 | Position Encoding | 最新 PE 扩展方法，当前待处理 |
| 15 | **LongRoPE2** (arXiv:2502.20082) 笔记 | Position Encoding | 进化搜索方法，当前待处理 |

---

## 五、总结

### 整体评估
- **引用完整性**: 通过。约 130 个 cite key 全部有对应 bib 条目，存在 3 处冗余/重复 key 建议清理。
- **大厂架构覆盖**: 发现 **8 处覆盖缺口**，其中 2 处为高严重程度（iRoPE、temporal conv on KV）。
- **子类别均衡性**: 6 大类别共识别出 **7 个薄弱子类别**（论文数 <= 1），主要集中在:
  - Token Mixer: Hybrid Architectures (仅 1 篇)、Different Activation (仅 1 篇)
  - Position Encoding: Content-Aware PE (1 篇待处理)、Multimodal PE (1 篇待处理)、iRoPE (1 篇待处理)
  - Normalization: Conditional/Adaptive (仅 1 篇)
  - Module Sequence: ODE Theory (仅 1 篇)
- **Residual Connection (Focus Area)**: 覆盖最为全面（42 篇），各子维度均衡，无明显缺口。

### 建议优先行动
1. 完成 iRoPE (Llama 4) 笔记 — 填补最重要的 PE 覆盖缺口
2. 补充 Hybrid Architecture 论文 (Griffin/Zamba) — 填补 Token Mixer 最薄弱环节
3. 完成 Qwen3 和 ERNIE 4.5 的 Channel Mixer 笔记 — 填补 MoE 新范式缺口
4. 清理 reference.bib 中的重复 key (deepseekv2_2024 vs deepseekv2_2024_mla, huang2020improving vs huang2020tfixup)
