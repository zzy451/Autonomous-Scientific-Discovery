# Jamba: A Hybrid Transformer-Mamba Language Model
**作者**: Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonathan Osin, Itay Dalmedigos, Erez Safahi, Shaked Meirom, Yonatan Belinkov, Shai Shalev-Shwartz, Omri Abend, Raz Alon, Tomer Asida, Amir Bergman, Roman Glozman, Michael Gokhman, Avashalom Manevich, Nir Ratner, Noam Rozen, Erez Shwartz, Mor Zusman, Yoav Shoham (AI21 Labs) | **年份**: 2024 | **arxiv**: 2403.19887

## 0. 摘要翻译
本文提出Jamba，一种新的混合架构大语言模型，结合了Transformer层、Mamba层和混合专家（MoE）模块。Jamba是首个将这三种组件结合的生产级模型。该混合架构允许在吞吐量、内存使用和模型质量之间灵活权衡。Jamba的52B参数模型（12B活跃参数）在单张80GB GPU上即可运行，支持256K token的上下文长度，在多个基准上与Llama-2-70B和Mixtral-8x7B竞争。

## 1. 方法动机
a) **为什么提出**: 纯Transformer在长上下文上KV cache过大；纯Mamba在某些需要精确检索的任务上不如Transformer。混合架构可以取长补短。
b) **现有痛点**: (1) Transformer的KV cache在256K上下文时占用巨大内存；(2) Mamba在in-context learning和精确信息检索上有局限；(3) 需要在单GPU上运行大模型+长上下文。
c) **研究假设**: 通过交替使用Transformer层（精确注意力）和Mamba层（高效序列建模），可以在保持模型质量的同时大幅减少内存占用。

## 2. 方法设计
a) **Pipeline**: 将模型层分为多个block，每个block内混合Transformer层和Mamba层，部分层使用MoE替代密集FFN。

b) **模块功能**:
- **层混合比例**:
  - 每个block包含$l$层，其中$a$层是Attention层，$m$层是Mamba层
  - Jamba的配置: 每8层中1层Attention + 7层Mamba（1:7比例）
  - Attention层提供精确的全局信息检索能力
  - Mamba层提供高效的序列建模和低内存占用
- **MoE集成**:
  - 部分层的FFN替换为MoE（每2层中1层用MoE）
  - 16个专家，top-2路由
  - 总参数52B，每token活跃参数12B
  - MoE增加模型容量而不增加推理计算
- **KV cache优化**:
  - 只有Attention层需要KV cache
  - 1:7的比例意味着KV cache减少约8倍
  - 256K上下文在单80GB GPU上可行

c) **公式解释**:
- 内存分析: 假设$L$层全Attention的KV cache为$M$，Jamba只有$L/8$层Attention，KV cache约$M/8$
- 吞吐量: Mamba层的推理速度快于Attention层（无需KV cache读取），整体吞吐量提升
- 质量: 少量Attention层足以提供全局信息检索能力，Mamba层处理局部和序列建模

## 3. 与其他方法对比
| 方面 | Jamba | 纯Transformer | 纯Mamba | Mamba+MoE |
|------|-------|--------------|---------|-----------|
| 架构 | Attn+Mamba+MoE | Attn+FFN | Mamba+FFN | Mamba+MoE |
| KV cache | 极小（1/8 Attn层）| 大 | 无 | 无 |
| 精确检索 | 好（有Attn层）| 最好 | 有限 | 有限 |
| 长上下文 | 256K（单GPU）| 受限于内存 | 理论无限 | 理论无限 |
| 参数效率 | 高（MoE）| 低 | 低 | 高 |

## 4. 实验表现
- **通用基准**: 在MMLU、HellaSwag、ARC等上与Llama-2-70B和Mixtral-8x7B竞争
- **长上下文**: 在256K上下文的Needle-in-a-Haystack测试中表现良好
- **吞吐量**: 比同规模纯Transformer模型高约3倍
- **内存**: 256K上下文时KV cache仅约4GB（纯Transformer需约32GB+）
- **单GPU部署**: 52B参数模型可在单张80GB A100上运行
- **Ablation**: 1:7的Attn:Mamba比例是质量和效率的最佳平衡点；纯Mamba在某些检索任务上明显落后

## 5. 总结
a) **一句话概括**: Jamba通过1:7比例混合Transformer注意力层和Mamba层，配合MoE扩展容量，实现了在单GPU上支持256K上下文的高效大语言模型，证明了混合架构在质量-效率权衡上的优势。
b) **速记pipeline**: Input → [Mamba×7 → Attention×1 → (部分层MoE-FFN)] × N_blocks → Output
