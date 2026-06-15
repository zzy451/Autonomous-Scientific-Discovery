# Jamba: A Hybrid Transformer-Mamba Language Model
**作者**: Lieber et al. (AI21 Labs) | **年份**: 2024 | **arxiv**: 2403.19887

## 0. 摘要翻译
本文介绍 **Jamba**，一个新的大语言模型架构，将 **Transformer** 层和 **Mamba** (SSM) 层混合使用，同时在部分层中集成了 **Mixture-of-Experts (MoE)**。Jamba 52B（12B 激活参数）的上下文长度达到 256K token，能够在单张 80GB GPU 上运行。混合架构使得 Jamba 在质量、吞吐量和内存效率之间取得了优异的平衡：它在多项基准上匹配或超过同规模的 Transformer 和 Mamba 模型，同时提供更高的推理吞吐量和更小的内存占用。

## 1. 方法动机
a) **为什么提出这个方法**：纯 Transformer 推理慢（KV cache 大）但质量好（精确 recall）；纯 Mamba 推理快（固定隐状态）但在某些 recall-heavy 任务上弱。将两者混合可以取长补短。

b) **现有方法的痛点**：
- 纯 Transformer：KV cache 随序列长度线性增长，256K 上下文的 KV cache 极大
- 纯 Mamba：固定隐状态无法精确回忆所有历史细节，在某些 in-context learning 和 recall 任务上弱于 Transformer
- 需要在两者之间找到最优的层配比

c) **研究假设/直觉**：不同层可以承担不同的功能——Mamba 层高效处理大部分序列建模工作，少量 Attention 层提供精确的长距离 recall 能力。这种混合可以用少量 Attention 层就弥补 Mamba 的 recall 不足，同时大幅减少 KV cache。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 模型由若干个 block 组成，每个 block 包含多层
2. 每个 block 中，大部分层使用 **Mamba 层**，少数层使用 **Attention 层**
   - 例如：每 8 层中 6 层 Mamba + 2 层 Attention
3. 部分层（Mamba 或 Attention 层均可）的 FFN 替换为 **MoE** 层
4. Attention 层使用 GQA 以进一步减少 KV cache

**具体配比（Jamba 52B）**：
- 比例大约 7:1 (Mamba:Attention)
- MoE 用于部分层的 FFN，16 个专家选 2 个

b) **核心模块功能**：
- **Mamba 层**：提供高效的序列建模，固定大小隐状态，无 KV cache
- **Attention 层 (GQA)**：提供精确的长距离 recall，但产生 KV cache。使用 GQA 减少 cache
- **MoE 层**：增加模型容量而不增加激活参数（总参数 52B，激活 12B）
- **层配比**：关键超参数——Mamba 层占比越高推理越快，Attention 层越多 recall 越好

c) **关键公式解释**：
- KV cache 大小 = num_attention_layers × num_kv_heads × d × L × 2
- 由于 Mamba 层无 KV cache，总 KV cache 仅来自少量 Attention 层
- 对比纯 Transformer：KV cache 减少约 (total_layers / attn_layers) 倍
- 例：56 层中 8 层 Attention → KV cache 减少 ~7 倍

## 3. 与其他方法对比
- **与纯 Transformer 的区别**：大量层替换为 Mamba，KV cache 大幅减少，推理更快
- **与纯 Mamba 的区别**：保留少量 Attention 层确保 recall 能力，质量更好
- **与 Mamba-2 的区别**：Jamba 使用 Mamba-1，但混合了 Attention；Mamba-2 是纯 SSM 改进
- **与 MoE 模型（如 Mixtral）的区别**：Jamba 在 token mixer 层面也做了混合（Mamba + Attention），不仅在 FFN 层面用 MoE
- **创新点**：
  1. 首个大规模 Transformer-Mamba 混合架构
  2. 系统性探索了层配比的设计空间
  3. 三者混合：Attention + Mamba + MoE
- **适用场景**：长上下文推理（256K）、高吞吐部署、内存受限的单 GPU 部署

## 4. 实验表现
- **关键结果**：
  - Jamba 52B (12B active) 在多项基准上匹配 LLaMA-2 70B 和 Mixtral 8x7B
  - 256K 上下文长度：在单张 80GB GPU 上可运行（纯 Transformer 同参数量无法做到）
  - 推理吞吐量：比同规模纯 Transformer 高 3-5 倍
  - KV cache 大小：仅为纯 Transformer 的 1/8
  - 在 Needle-in-a-Haystack 测试中保持高精度
- **优势场景**：超长上下文推理、高吞吐在线服务、单 GPU 部署
- **局限性**：
  - 层配比（Mamba:Attention 比例）需要根据任务调节，缺乏理论指导
  - Mamba-1 层已有 Mamba-2 的后续改进，未采用
  - 三者混合增加了架构复杂度和工程实现难度
  - 在某些纯 recall 任务上仍略弱于纯 Transformer（但差距小）

## 5. 总结
a) **一句话概括（≤20字）**：Mamba + Attention + MoE 三合一混合架构。

b) **速记 pipeline**：
`输入 → [Mamba层 × 6 + Attention(GQA)层 × 2] × N_blocks → (部分FFN替换为MoE) → 输出`
`Mamba层: 无KV cache, 高效序列建模`
`Attention层: 有KV cache, 精确recall`
`MoE层: 增容量不增激活参数`
