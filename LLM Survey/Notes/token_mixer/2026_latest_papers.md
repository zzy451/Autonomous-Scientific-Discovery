# Token Mixer / Attention 最新论文汇总 (2025-2026)

> 搜索日期: 2026-04-10
> 覆盖范围: 2024Q4 — 2026Q2

---

## 一、State Space Models (SSM) 新进展

### 1. Mamba-3: Improved Sequence Modeling using State Space Principles
- **作者**: Gu, Dao et al.
- **年份**: 2026
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **核心贡献**: Mamba系列第三代，引入架构改进，在1.5B规模上平均下游准确率比Gated DeltaNet高0.6个百分点；MIMO变体进一步提升检索、状态追踪和语言建模性能。
- **子分支**: SSM / 纯RNN架构

### 2. RWKV-7 "Goose" with Expressive Dynamic State Evolution
- **作者**: Bo Peng & RWKV Community
- **年份**: 2025
- **arXiv**: [2503.14456](https://arxiv.org/abs/2503.14456)
- **核心贡献**: 引入动态状态演化(Dynamic State Evolution)机制，突破attention/linear attention的TC0表达力限制。2.9B参数模型在多语言任务上达到3B SoTA，英语性能匹配当前3B最佳。常数内存、常数推理时间、无KV缓存的纯RNN架构。本质上是一个meta-in-context learner，通过上下文梯度下降在每个token上进行test-time training。
- **子分支**: 纯RNN / 线性时间架构

### 3. Falcon Mamba 7B
- **作者**: TII (Technology Innovation Institute)
- **年份**: 2024
- **arXiv**: [2410.05355](https://arxiv.org/abs/2410.05355)
- **核心贡献**: 首个具有竞争力的纯Mamba架构7B语言模型，在5.8T tokens上训练。超越Mistral 7B、Llama3.1 8B等Transformer模型，证明纯SSM设计可达到SOTA性能。
- **子分支**: SSM / 纯Mamba架构

---

## 二、线性注意力 / Delta Rule

### 4. Gated Delta Networks: Improving Mamba2 with Delta Rule
- **作者**: Yang, Schlag, et al.
- **年份**: 2024
- **arXiv**: [2412.06464](https://arxiv.org/abs/2412.06464)
- **核心贡献**: 引入门控delta规则(gated delta rule)，开发了针对现代硬件优化的并行训练算法。Gated DeltaNet在语言建模、常识推理、上下文检索等多个基准上持续超越Mamba2和DeltaNet。已成为2025-2026年混合架构的核心组件。
- **子分支**: 线性注意力 / Delta Rule

### 5. Log-Linear Attention
- **作者**: Gu et al.
- **年份**: 2025
- **arXiv**: [2506.04761](https://arxiv.org/abs/2506.04761)
- **核心贡献**: 提出log-linear attention通用框架，在现有线性注意力变体之上实现对数-线性复杂度。以Mamba-2和Gated DeltaNet为案例研究，其log-linear变体性能与线性时间变体相当，同时保留了matmul-rich的并行训练能力。
- **子分支**: 线性注意力 / 理论框架

---

## 三、混合架构 (Hybrid Architectures)

### 6. Nemotron-H: Hybrid Mamba-Transformer Models
- **作者**: NVIDIA ADLR
- **年份**: 2025
- **arXiv**: [2504.03624](https://arxiv.org/abs/2504.03624)
- **核心贡献**: 8B和56B/47B混合Mamba-Transformer模型家族，将大部分self-attention层替换为Mamba层。在同等或更优精度下实现最高3x推理加速（对比Qwen-2.5-7B/72B和Llama-3.1-8B/70B）。
- **子分支**: 混合架构 / Mamba-Transformer

### 7. NVIDIA Nemotron Nano 2 (9B)
- **作者**: NVIDIA
- **年份**: 2025
- **arXiv**: [2508.14444](https://arxiv.org/abs/2508.14444)
- **核心贡献**: 基于Nemotron-H架构的9B混合Mamba-Transformer推理模型，主要由Mamba-2和MLP层组成，仅保留4个Attention层。在同等规模模型中达到SOTA精度，同时大幅提升推理吞吐量。
- **子分支**: 混合架构 / Mamba-Transformer

### 8. Nemotron 3 Family (Nano/Super/Ultra)
- **作者**: NVIDIA
- **年份**: 2025
- **arXiv**: [2512.20856](https://arxiv.org/abs/2512.20856) (Nano: [2512.20848](https://arxiv.org/abs/2512.20848))
- **核心贡献**: MoE + 混合Mamba-Transformer架构家族，支持最高1M tokens上下文。引入LatentMoE（新型MoE路由）和NVFP4量化。Nano 30B-A3B在25T tokens上预训练，attention层极少且使用GQA（仅2个KV头）。
- **子分支**: 混合架构 / MoE + Mamba-Transformer

### 9. OLMo Hybrid: From Theory to Practice and Back
- **作者**: AI2 (Allen Institute for AI)
- **年份**: 2026
- **arXiv**: [2604.03444](https://arxiv.org/abs/2604.03444)
- **核心贡献**: 7B参数混合模型，将OLMo 3的滑动窗口注意力层替换为Gated DeltaNet层。提供了混合LLM架构的系统理论和实证研究，证明Gated DeltaNet比滑动窗口注意力和Mamba2具有更强的上下文学习能力。在标准预训练和中期训练评估中超越纯Transformer的OLMo 3。
- **子分支**: 混合架构 / Attention + Gated DeltaNet

### 10. InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model
- **作者**: (多机构)
- **年份**: 2026
- **arXiv**: [2603.18031](https://arxiv.org/abs/2603.18031)
- **核心贡献**: 无注意力的混合Mamba-Transformer模型，在计算约束下平衡细粒度局部建模与长程依赖捕获。Mamba风格SSM线性扩展但难以捕获高秩全局交互，InfoMamba从信息论角度解决这一问题。
- **子分支**: 混合架构 / 无注意力混合

### 11. Qwen3.5 (397B-A17B) — 混合注意力 + MoE
- **作者**: Alibaba Qwen Team
- **年份**: 2026
- **发布**: [GitHub](https://github.com/QwenLM/Qwen3.5), [Blog](https://qwen.ai/blog)
- **核心贡献**: 首个大规模采用Gated DeltaNet + Full Attention混合架构的前沿模型。397B总参数/17B激活参数的MoE模型，75%层使用Gated DeltaNet线性注意力，25%保留标准注意力（3:1比例）。支持262K tokens上下文窗口，推理效率远超纯Transformer。
- **子分支**: 混合架构 / Gated DeltaNet + MoE (产业落地)

### 12. Qwen3-Next-80B-A3B — 超稀疏MoE + 混合注意力
- **作者**: Alibaba Qwen Team
- **年份**: 2025
- **发布**: [HuggingFace](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking)
- **核心贡献**: Qwen3-Next系列首款模型，采用Gated DeltaNet + Gated Attention的混合注意力机制，支持超长上下文。超稀疏MoE（80B总参/3B激活），面向极致效率。
- **子分支**: 混合架构 / 超稀疏MoE + 混合注意力

---

## 四、稀疏注意力 (Sparse Attention)

### 13. NSA: Native Sparse Attention
- **作者**: DeepSeek
- **年份**: 2025
- **arXiv**: [2502.11089](https://arxiv.org/abs/2502.11089)
- **会议**: ACL 2025
- **核心贡献**: 硬件对齐的原生可训练稀疏注意力机制，集成压缩、选择和滑动窗口三分支动态门控。从预训练阶段即原生支持稀疏注意力，而非后训练近似。
- **子分支**: 稀疏注意力 / 硬件对齐

### 14. DeepSeek Sparse Attention (DSA) — DeepSeek-V3.2
- **作者**: DeepSeek-AI
- **年份**: 2025
- **arXiv**: [2512.02556](https://arxiv.org/abs/2512.02556)
- **核心贡献**: DeepSeek-V3.2的核心技术突破之一。DSA是基于MLA的细粒度稀疏注意力机制，配合lightning indexer，在长上下文场景中大幅降低计算复杂度同时保持模型性能。从DeepSeek-V3.1-Terminus继续训练而来。
- **子分支**: 稀疏注意力 / MLA + 动态稀疏

### 15. VideoNSA: Native Sparse Attention Scales Video Understanding
- **作者**: Song, Chai et al.
- **年份**: 2025 (ICLR 2026)
- **arXiv**: [2510.02295](https://arxiv.org/abs/2510.02295)
- **核心贡献**: 将NSA引入视频语言模型，仅使用3.6%注意力预算实现128K token视频理解。对文本保留密集注意力，对视频使用NSA的硬件感知混合方法。在长视频理解、时序推理和空间理解任务上全面超越token压缩和无训练稀疏基线。
- **子分支**: 稀疏注意力 / 多模态应用

### 16. MSA: Memory Sparse Attention (100M Tokens)
- **作者**: Yu Chen et al. (EverMind-AI)
- **年份**: 2026
- **arXiv**: [2603.23516](https://arxiv.org/abs/2603.23516)
- **核心贡献**: 可扩展稀疏注意力框架，配合document-wise RoPE和KV缓存压缩，将端到端建模扩展到生命周期级上下文（100M tokens）。O(L)复杂度，从16K到100M tokens仅有<9%性能下降。引入Memory Parallel（快速100M token处理）和Memory Interleave（跨分布式内存段的多跳推理）。
- **子分支**: 稀疏注意力 / 超长上下文

### 17. Flux Attention: Context-Aware Hybrid Attention
- **作者**: (多机构)
- **年份**: 2026
- **arXiv**: [2604.07394](https://arxiv.org/abs/2604.07394)
- **核心贡献**: 动态上下文感知的层级混合注意力机制，在Full Attention和Sparse Attention之间动态切换。解决现有混合注意力方法依赖静态分配比例、无法适应不同任务检索需求的问题。
- **子分支**: 稀疏注意力 / 动态混合

---

## 五、KV Cache 压缩

### 18. TurboQuant / PolarQuant (Google)
- **作者**: Google Research
- **年份**: 2025 (ICLR 2026)
- **arXiv**: [2504.19874](https://arxiv.org/abs/2504.19874) (TurboQuant), [2502.02617](https://arxiv.org/abs/2502.02617) (PolarQuant)
- **核心贡献**: 通过随机旋转(random rotation) + QJL实现KV缓存6x内存压缩和8x注意力计算加速（H100上4-bit），零精度损失。PolarQuant使用极坐标变换将KV缓存量化到3-bit。已在llama.cpp等开源框架中讨论集成。
- **子分支**: KV缓存压缩 / 量化

### 19. KVSculpt: KV Cache Compression as Distillation
- **作者**: (多机构)
- **年份**: 2026
- **arXiv**: [2603.27819](https://arxiv.org/abs/2603.27819)
- **核心贡献**: 将KV缓存压缩重新定义为蒸馏问题。统一了序列长度维度上的eviction（选择保留哪些KV对）和merging（合并相似KV对）方法，与量化/低秩分解等per-pair方法正交。
- **子分支**: KV缓存压缩 / 蒸馏框架

### 20. TriAttention: Trigonometric KV Compression for Long Reasoning
- **作者**: Weian Mao et al.
- **年份**: 2026
- **arXiv**: [2604.04921](https://arxiv.org/abs/2604.04921)
- **代码**: [GitHub](https://github.com/WeianMao/triattention)
- **核心贡献**: 针对长推理场景的KV缓存压缩。发现pre-RoPE Q/K向量集中在固定中心附近，通过三角级数确定距离偏好。TriAttention使用这些中心和范数对key评分，无需选择代表性query，避免了RoPE旋转导致的top-key选择不稳定问题。
- **子分支**: KV缓存压缩 / 长推理优化

---

## 六、注意力机制改进

### 21. MoH: Multi-Head Attention as Mixture-of-Head Attention
- **作者**: Jin et al.
- **年份**: 2024 (ICLR 2025)
- **arXiv**: [2410.11842](https://arxiv.org/abs/2410.11842)
- **核心贡献**: 将多头注意力重新表述为求和形式，提出Mixture-of-Head attention (MoH)。用加权求和替代标准求和，仅使用50%-90%的注意力头即可超越标准多头注意力。在ViT、DiT和LLM上均有效。
- **子分支**: 注意力机制改进 / 头部稀疏化

### 22. TransMLA: Multi-Head Latent Attention Is All You Need
- **作者**: Fanxu Meng et al. (PKU)
- **年份**: 2025 (NeurIPS 2025 Spotlight)
- **arXiv**: [2502.07864](https://arxiv.org/abs/2502.07864)
- **核心贡献**: 将任意GQA模型无缝转换为MLA模型的框架，证明MLA在相同KV缓存开销下比GQA具有更强表达力。在LLaMA-2-7B上压缩93% KV缓存，实现10.6x推理加速。兼容DeepSeek代码库（vLLM、SGLang）。
- **子分支**: 注意力机制改进 / MLA推广

### 23. Bayesian Attention Mechanism (BAM)
- **作者**: Bianchessi, Barros, Kupssinskü
- **年份**: 2025 (ICLR 2026)
- **arXiv**: [2505.22842](https://arxiv.org/abs/2505.22842)
- **核心贡献**: 将位置编码形式化为注意力中的先验(prior)的概率框架。引入广义高斯先验变体，改善长上下文外推能力。为位置编码提供了理论清晰度，超越了现有PE方法有限的评估指标。
- **子分支**: 注意力机制改进 / 位置编码理论

---

## 七、Test-Time Training (TTT)

### 24. In-Place Test-Time Training (In-Place TTT)
- **作者**: Tianle Cai et al.
- **年份**: 2026 (ICLR 2026 Oral)
- **arXiv**: [2604.06169](https://arxiv.org/abs/2604.06169)
- **核心贡献**: 将LLM的MLP块最终投影矩阵作为快速权重(fast weights)，在推理时通过NTP对齐的目标函数更新，实现"即插即用"的TTT能力。无需新模块、无需从头重训。解决了TTT在当前LLM生态中的架构不兼容、计算低效和快速权重目标不对齐三大障碍。
- **子分支**: Test-Time Training / 快速权重

---

## 八、前沿模型架构总览 (产业级)

### 25. DeepSeek-V3 / V3.2
- **arXiv**: V3 [2412.19437](https://arxiv.org/abs/2412.19437), V3.2 [2512.02556](https://arxiv.org/abs/2512.02556)
- **架构**: MoE (671B/37B active) + MLA + DeepSeekMoE + DSA (V3.2)
- **关键创新**: Multi-head Latent Attention压缩KV缓存; V3.2引入DeepSeek Sparse Attention (DSA)

### 26. Llama 4 Scout / Maverick (Meta, 2025)
- **发布**: [Meta AI Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- **架构**: MoE + 原生多模态 + interleaved position embeddings
- **关键创新**: Meta首个MoE架构; Scout支持10M上下文窗口; 原生多模态（非后接adapter）
- **备注**: 独立评测显示vanilla Maverick性能低于GPT-4o/Claude 3.5 Sonnet/Gemini 1.5 Pro

### 27. Qwen3.5 (Alibaba, 2026)
- **发布**: [GitHub](https://github.com/QwenLM/Qwen3.5)
- **架构**: MoE (397B/17B active) + Gated DeltaNet + Full Attention (3:1) + 262K context
- **关键创新**: 首个前沿级混合线性注意力模型，验证了Gated DeltaNet在产业规模的可行性

---

## 九、分析性文章 / 博客

### 28. Sebastian Raschka: New LLM Architecture Gallery (2026)
- **链接**: [sebastianraschka.com](https://sebastianraschka.com/blog/2026/llm-architecture-gallery.html)
- **内容**: 汇集了"The Big LLM Architecture Comparison"和"A Dream of Spring for Open-Weight LLMs"中的架构图、fact sheets和链接。覆盖GQA、MLA、MoE等关键架构组件。

### 29. "2026 Frontier LLM Architectures Compared" (largo.dev)
- **链接**: [largo.dev](https://largo.dev/articles/frontier-llm-architectures-2026/)
- **核心观点**: 所有前沿LLM都已收敛到MoE架构，但效率路径分化明显——DeepSeek压缩注意力到潜空间、Meta交错位置编码、Google押注原生多模态、Alibaba支持可调推理深度。"架构战争正在成熟为工程战争"。

### 30. Sebastian Raschka: LLM Research Papers — The 2025 List
- **链接**: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one)
- **内容**: 手工策划的200+篇2025年LLM研究论文，按主题组织。

---

## 十、趋势总结

### 2025-2026 Token Mixer 关键趋势

1. **混合架构成为主流**: Gated DeltaNet已从学术论文走向产业落地（Qwen3.5、OLMo Hybrid），与标准注意力的3:1混合比例成为新范式。NVIDIA的Nemotron系列则验证了Mamba-2 + Transformer混合的可行性。

2. **MoE + 高效注意力的双重稀疏**: 前沿模型同时在FFN层（MoE）和注意力层（稀疏/线性注意力）实现稀疏化，如Qwen3.5 (MoE + Gated DeltaNet)、Nemotron 3 (MoE + Mamba-2)。

3. **SSM持续进化**: Mamba-3在检索和状态追踪上超越Gated DeltaNet; RWKV-7通过动态状态演化突破TC0限制; 纯SSM模型（Falcon Mamba）证明了无注意力架构的竞争力。

4. **KV缓存压缩进入3-bit时代**: TurboQuant/PolarQuant实现6x压缩零精度损失; TriAttention针对长推理场景优化; KVSculpt统一了eviction和merging。

5. **稀疏注意力从后训练走向原生训练**: NSA和DSA证明从预训练阶段即支持稀疏注意力的可行性; MSA将端到端建模扩展到100M tokens。

6. **架构收敛与分化并存**: 所有前沿模型收敛到MoE，但注意力机制路径分化——MLA (DeepSeek)、Gated DeltaNet混合 (Qwen/OLMo)、Mamba-2混合 (NVIDIA)、标准GQA+稀疏 (Meta)。

7. **TTT复兴**: In-Place TTT (ICLR 2026 Oral) 证明可以将LLM权重作为持续吸收新知识的长期记忆，无需新模块。RWKV-7本质上也是meta-in-context learner。
