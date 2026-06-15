# Section 1: Token Mixer — Section Scratch

> 基于 111 篇笔记生成，覆盖 12 个子分支
> 生成日期：2026-04-06

## 1.0 引言

Token Mixer 是 Transformer Block 中负责 token 间信息交换的核心组件，数学上定义为将输入序列 $X \in \mathbb{R}^{N \times d}$ 映射为混合后的表示 $Y = \text{TokenMix}(X)$，其中每个输出 token 的表示融合了其他 token 的信息。本节从注意力机制的数学本质出发，梳理从标准 Softmax Attention 到线性注意力、稀疏注意力、SSM、混合架构的完整演进脉络。Token Mixer 与其他 5 个维度的关系：Channel Mixer 负责 token 内部的特征变换（正交互补），Normalization 影响 Token Mixer 的训练稳定性（QK-Norm），Position Encoding 为 Token Mixer 注入顺序信息（RoPE 嵌入到 QK），Residual Connection 决定 Token Mixer 输出如何融入残差流，Module Sequence 决定 Token Mixer 在 Block 中的位置和排列。

---

## 1.1 Standard Dot-Product Attention (MHA)

### 分支定义与存在理由
标准多头注意力（Vaswani 2017）是所有 Token Mixer 的基准。它完全摒弃了 RNN 的顺序依赖和 CNN 的局部感受野限制，首次证明仅用注意力机制即可完成高质量的序列建模。QKV 三矩阵设计本质上是一个可微分的信息检索系统：Query="我在找什么"，Key="我包含什么"，Value="我提供什么"。O(N²) 复杂度是 softmax 全连接注意力的本质代价——每个 token 必须与所有其他 token 计算相关性，这既是其强大表达力的来源，也是可扩展性的根本限制。多头机制将注意力空间拆分为 h 个子空间并行计算，允许模型同时捕获不同类型的依赖关系。

### 技术介绍
核心公式：$\text{Attention}(Q,K,V) = \text{softmax}(QK^T / \sqrt{d_k}) V$，缩放因子 $\sqrt{d_k}$ 防止点积值过大导致 softmax 梯度饱和。多头：$\text{MultiHead} = \text{Concat}(\text{head}_1,...,\text{head}_h) W^O$。计算复杂度 O(N²d) FLOPs，内存 O(N²+Nd)。大厂采用：早期 GPT-2/3, BERT 直接使用 MHA；2023 后几乎所有模型转向 GQA/MLA，但 Llama 2 7B 和 Baichuan-M1 仍在较小模型上保留 MHA。Gated Self-Attention (Qiu 2025) 在输出上添加门控 $g = \sigma(W_g x)$，实现信息流精细控制。

### 理论支撑
Softmax 注意力等价于 Nadaraya-Watson 核回归（Tsai 2019）；注意力矩阵随深度趋向低秩（Dong 2021 rank collapse）；Transformer Universal Approximation（Yun 2020）证明足够宽度和深度的 Transformer 可逼近任意连续序列函数。

### 待解决问题
Attention Sink 现象（Xiao 2023）：LLM 将大量注意力分配给 BOS token 作为 softmax 的"垃圾桶"；Softmax 零和约束限制表达能力（所有权重和为1）；深层注意力退化（token uniformity）。

### 对未来的影响
仍是最强质量基线。FlashAttention 证明 IO-aware 优化可带来数倍加速。与 SSM/Linear Attention 的混合是趋势——未来架构可能不是"替代 MHA"而是"在关键层保留 MHA"。

### 潜在技术方向
量化注意力（SageAttention）、自适应精度注意力、可学习的注意力激活函数。

---

## 1.2 KV Cache 优化 (MQA → GQA → MLA → CLA → MFA)

### 分支定义与存在理由
自回归推理时 KV Cache 是显存瓶颈：每生成一个 token 须加载所有历史 KV，内存带宽而非计算量决定推理速度。以 Llama 2 70B 为例（80 层、64 KV 头），128K 上下文需约 160GB KV cache。五条技术路线从不同数学维度攻击同一物理瓶颈：MQA（头维度极端压缩）、GQA（头维度平衡压缩）、MLA（秩维度压缩）、CLA（层维度压缩）、MFA（矩阵分解压缩），形成丰富的正交组合空间。

### 技术介绍
**MQA (Shazeer 2019)**：所有 h 个 Query 头共享 1 组 KV，压缩比 h 倍（~32x），但质量显著下降。被 PaLM、StarCoder 采用后因质量问题被 GQA 取代。

**GQA (Ainslie 2023)**：H 个 Query 头分成 G 组共享 KV。G=1 退化为 MQA，G=H 退化为 MHA。关键创新是 Uptrain 方法——从 MHA checkpoint 出发，均值池化同组 KV 头初始化，仅用 ~5% 预训练计算完成转换。GQA-8 在 T5-XXL 上质量接近 MHA（<0.5 BLEU 差距）。**2024-2025 年绝对主流**：Llama 3、Mistral、Qwen2.5/3、Gemma 3、Llama 4、Phi-4、Hunyuan 均采用，8 个 KV 头是最常见配置。

**MLA (DeepSeek-V2 2024)**：将 KV 联合压缩到低维潜在向量 $c_{KV} = W_{DKV} h_t$（$d_c=512$），推理时只缓存 $c_{KV}$，通过上投影恢复 $K = W_{UK} c_{KV}$。KV cache 从 32768 压缩到 576（93.3%）。技术难点：RoPE 与低秩压缩不兼容，提出 Decoupled RoPE——额外生成小维度 RoPE Key 与压缩 K 拼接。DeepSeek-V2/V3/R1 全系列采用，性能反超 MHA。

**CLA (Brandon 2024)**：每 S 层共享一份 KV，与 GQA 在不同维度操作可叠加。CLA-2 困惑度仅升高 0.1-0.2。腾讯 Hunyuan-Large 和 Yi-Lightning 已在生产环境采用。

**MFA (Step-2)**：多矩阵分解注意力，第四条 KV cache 优化路线。

| 方法 | 压缩维度 | 压缩比(vs MHA) | 质量影响 | 工业采用 |
|------|---------|---------------|---------|---------|
| MQA | Head→1 | ~32x | 略降 | PaLM, StarCoder |
| GQA-8 | Head→G | 4x | 接近MHA | Llama 3, Mistral, Qwen, Gemma 3 |
| MLA | Head→低秩 | ~57x | 超过MHA | DeepSeek V2/V3/R1 |
| CLA-2 | Layer→共享 | 2x | 几乎无损 | Hunyuan-Large, Yi-Lightning |
| KIVI | Precision→2bit | 8x | 几乎无损 | 推理优化 |

### 理论支撑
KV 矩阵的低秩特性（Dong 2021）；注意力头冗余性分析；低秩矩阵近似理论（MLA 的数学基础）。

### 待解决问题
MLA 的 Decoupled RoPE 与 YaRN 等长上下文方法的兼容性；GQA 最优组数 G 的理论指导（从 GLM-4 的 2 到 Gemma 3 的 16）；各路线最优组合策略（MLA+CLA+量化叠加效果）。

### 对未来的影响
GQA 已是事实标准，但 MLA 93.3% 压缩率展示了秩维度的巨大潜力。未来可能是多维度联合优化——头、秩、层、精度四维度寻找最优配置。

### 潜在技术方向
动态 KV 压缩、GQA-to-MLA 自动转换、注意力头自动分组。

---

## 1.3 Sparse Attention

### 分支定义与存在理由
全注意力矩阵中绝大多数权重接近零，稀疏化可将复杂度从 O(N²) 降到 O(N√N)。从 2019 年 Sparse Transformer 的固定模式到 2025 年 NSA 的可学习动态稀疏，经历了"固定→手工混合→可学习"的演进。2024-2025 年异构层注意力已成为大厂主流。

### 技术介绍
**Sparse Transformer (Child 2019)**：strided/fixed 稀疏，每位置关注 O(√N) 个位置。

**滑动窗口**：Longformer (Beltagy 2020)→Mistral 7B SWA (W=4096)→Gemma 2 1:1 L/G→**Gemma 3 5:1 Local/Global**（Local base=10K, Global base=1M）。

**NSA (Yuan 2025, DeepSeek)**：三分支动态稀疏（压缩+选择+窗口），门控聚合 $o = g_1 o_{compress} + g_2 o_{select} + g_3 o_{window}$。硬件对齐，可原生训练。

**MoBA (Lu 2025, Kimi)**：MoE 风格块稀疏，路由选择 top-k KV 块。

### 理论支撑
注意力矩阵稀疏性统计分析；局部性先验。

### 待解决问题
稀疏模式依赖任务；硬件效率差距（不规则内存访问）；异构层最优配比缺乏理论指导。

### 对未来的影响
"可学习动态稀疏"将取代"手工固定模式"。未来每层可能有独立注意力配置。

### 潜在技术方向
Token 级自适应稀疏路由、自适应稀疏度、与 Speculative Decoding 结合。

---

## 1.4 Linear Attention

### 分支定义与存在理由
核心 insight：$\text{softmax}(QK^T)V$ 可核化为 $\phi(Q)(\phi(K)^T V)$，O(N²d)→O(Nd²)。Katharopoulos (2020) 揭示线性注意力 = RNN 对偶性。Dao & Gu (2024) SSD 框架统一 SSM-线性注意力-结构化矩阵。MiniMax-01 (456B) 验证工业可行性。

### 技术介绍
**原始线性注意力 (Katharopoulos 2020)**：$\phi(x)=\text{elu}(x)+1$，推理切换为 RNN $S_t = S_{t-1} + \phi(k_t)v_t^T$。

**GLA (Yang 2024)**：门控 $S_t = G_t \odot S_{t-1} + k_t v_t^T$，FLASHLINEARATTENTION 硬件高效训练。

**DeltaNet (Yang 2024)**：delta rule $S_t = (I - \beta_t k_t k_t^T) S_{t-1} + \beta_t v_t k_t^T$，"先擦后写"。Householder compact WY 表示实现并行。

**Based (Arora 2024)**：Taylor 展开核 + 滑动窗口混合。**Lightning Attention-2 (Qin 2024)**：块内因果+块间状态传递。**TransNormerLLM (Qin 2024)**：7B 超越 softmax LLM。

### 理论支撑
核方法理论（softmax = 无穷维 RBF 核）；线性注意力 = 线性 RNN；SSD 对偶性。

### 待解决问题
Recall 不如 softmax；ICL 受限；需配合少量 softmax 层。

### 对未来的影响
"简单核替代"→"门控增强"(GLA)→"记忆规则革新"(DeltaNet)→"混合架构"(Based)。Delta rule + 门控可能成为下一代标准。

### 潜在技术方向
更高质量核函数、线性/Softmax 最优混合自动搜索、SSD 指导的混合设计。

---

## 1.5 Attention with Negative Weights

### 分支定义与存在理由
Softmax 非负约束使注意力只能做"加权平均"，无法"主动抑制"。长上下文下不相关 token 的微小权重累积成显著噪声。负权重让模型获得"对比"能力。

### 技术介绍
**Differential Transformer (Ye 2024)**：两子头差分 $\text{DiffAttn} = (A_1 - \lambda A_2) V$，噪声模式被消除。长上下文检索和减少幻觉效果显著。

**CogAttention (Lv 2024)**：直接允许负权重，计算开销更低（~1x vs ~2x）。

### 理论支撑
差分估计器理论；从凸组合扩展为仿射组合，表达能力严格增大。

### 待解决问题
DiffTransformer 需两次 softmax，FA 兼容性待验证；负权重的可解释性影响。

### 对未来的影响
负权重可能成为下一代注意力标配，挑战"注意力=概率分布"范式。

### 潜在技术方向
差分+线性注意力、差分+稀疏、差分+MoE、推广到 cross-attention。

---

## 1.6 Different Activation (Softmax 替代)

### 分支定义与存在理由
Saratchandran (2024) 发现 softmax 真正价值在于 Frobenius 范数隐式正则化 $\|A\|_F \leq O(\sqrt{n})$，而非非负性或归一化。任何等效范数正则化的函数都可替代。

### 技术介绍
**Sigmoid Attention (Ramapuram 2024)**：$\sigma(QK^T/\sqrt{d}+b) \cdot V$，无需行级归一化，硬件更高效。**Polynomial Attention (Saratchandran 2024)**：$p(x)=x^2$，违反三约束但保留范数正则化。**Squared ReLU (So 2021)**：高稀疏性。

### 理论支撑
Frobenius 范数统一框架：softmax/sigmoid/多项式形成从"保守"到"激进"的替代连续谱。

### 待解决问题
缺乏 100B+ LLM 的充分验证；FA 已降低 softmax 实际开销。

### 潜在技术方向
可学习激活函数、混合激活策略、Frobenius 原则推广到注意力整体设计。

---

## 1.7 RNN-Like / SSM

### 分支定义与存在理由
打破 O(N²)，实现 O(N) 训练和 O(1) 状态推理。SSM 核心：连续时间系统 $dx/dt = Ax + Bu$ 的离散化，天然获得递归/卷积对偶性。Mamba 选择性机制让参数依赖输入。xLSTM 证明经典 RNN 经现代化改造仍有竞争力。

### 技术介绍
**S4 (Gu 2021)**：HiPPO 初始化 + DPLR 参数化，O(N log N)。**Mamba (Gu & Dao 2024)**：选择性 SSM + 硬件感知扫描。**Mamba-2 (Dao & Gu 2024)**：SSD 对偶性，2-8x 加速。**RWKV (v1-v7)**：channel-wise 线性循环，14B。**RetNet (Sun 2023)**：带衰减的注意力。**xLSTM (Beck 2024)**：sLSTM 指数门控 + mLSTM 矩阵记忆。**Hyena**：长卷积。**HGRN2**：层次门控。**Mega/Megalodon**：EMA+门控注意力。

### 理论支撑
HiPPO（最优多项式投影）；SSD 对偶性（SSM/线性注意力/结构化矩阵三向等价）。

### 待解决问题
ICL 弱于 Transformer；"遗忘"问题；精确检索不佳。

### 潜在技术方向
Mamba-3（复数 SSM + MIMO）、更好的选择性机制。

---

## 1.8 Hybrid Architectures

### 分支定义与存在理由
不同层/不同 token 对注意力需求不同。混合取两者之长，KV cache 仅在注意力层产生。2024-2025 年进入工业部署。

### 技术介绍
**Jamba (AI21 2024)**：7:1 Mamba/Attention + MoE，52B，256K 上下文。**Griffin/Hawk (De 2024)**：RG-LRU + Local Attention。**Zamba2**：共享注意力+LoRA。**MiniMax-01 (2025)**：Lightning+Softmax 7:1，456B，4M 上下文。**Nemotron-H**：Mamba-Transformer-MoE 三重混合。

### 理论支撑
7:1 比例的经验收敛（Jamba 和 MiniMax 不约而同）。

### 待解决问题
最优比例依赖任务？训练动态不一致？

### 潜在技术方向
自动搜索最优混合策略、任务自适应混合。

---

## 1.9 Hardware-Efficient Attention

### 分支定义与存在理由
不改变算法，IO-aware 重组获得数倍加速。与"替换注意力"思路互补。

### 技术介绍
**FlashAttention (Dao 2022)**：tiling + online softmax，内存 O(N)，IO 达理论下界。FA-2 利用率 50-73%，FA-3 针对 Hopper 达 75%+。**PagedAttention/vLLM (Kwon 2023)**：KV 分页，浪费从 60-80% 降至 <4%，吞吐 2-4x。**Ring Attention (Liu 2023)**：环形 KV 传递，线性扩展上下文。**SageAttention**：QK INT8 量化加速 2-3x。

### 理论支撑
IO 复杂度理论（FlashAttention 达最优下界）；GPU HBM vs SRAM 带宽差 10-100x。

### 待解决问题
新硬件适配；稀疏/线性注意力的硬件优化。

### 对未来的影响
已是所有大规模 LLM 系统的必备基础设施。

---

## 1.10 KV Cache 压缩

### 分支定义与存在理由
推理时 KV Cache 线性增长，与 1.2（架构层面减少生成量）正交——1.10 是推理时动态压缩已生成 KV，可叠加。

### 技术介绍
**H2O (Zhang 2023)**：保留 Heavy Hitters + 最近 token，5-10x 压缩。**StreamingLLM (Xiao 2023)**：[Sink tokens] + [Recent window]，固定大小。**SnapKV (Li 2024)**：一次性按注意力投票压缩，>10x，检索仍准确。**PyramidKV (Cai 2024)**：底层多/高层少金字塔分配，12x 压缩保持 >95%。**KIVI (Liu 2024)**：2bit 非对称量化（Key per-channel, Value per-token），2.6x。**MiniCache**：相邻层差值编码。

### 理论支撑
注意力分布长尾/幂律特性；PyramidKV 揭示集中度随层深递增。

### 待解决问题
压缩导致"遗忘"；与 RAG/ICL 交互；跨任务最优压缩率。

### 潜在技术方向
预测性驱逐、语义感知压缩、与结构化稀疏统一。

---

## 1.11 推理优化

### 分支定义与存在理由
打破自回归逐 token 串行瓶颈。

### 技术介绍
**Speculative Decoding**：小 draft model 猜测 + 大模型并行验证，1.5-2x 加速。**MTP (Gloeckle 2024)**：每位置预测未来 k token，训练质量提升（代码 +12-17%）+ 推理加速（额外头作 draft，2-3x）。DeepSeek-V3 和 Llama 4 均采用。

### 理论支撑
MTP 改变注意力训练信号——隐状态必须支持 k 步预测，迫使学习更长程依赖。

### 待解决问题
Draft model 质量-速度权衡；MTP 训练成本。

---

## 1.12 Test-Time Memory

### 分支定义与存在理由
传统 Transformer 权重固定，推理时仅靠 KV Cache 被动追加。TTM 提出推理时也学习。

### 技术介绍
**TTT (Sun 2024)**：隐状态 = 模型参数，更新 = 自监督梯度下降 $W_t = W_{t-1} - \eta \nabla_W L(W;x_t)$。TTT-Linear 等价于 DeltaNet。TTT-MLP 在 32K 上持续改善。

**Titans (Behrouz 2025)**：记忆 = 小型网络，惊喜遗忘 $\eta_t = \eta \cdot \sigma(\|M_\theta(k_t)-v_t\|^2)$。BABILong (>1M) 显著优于基线。

### 理论支撑
TTT-Linear = DeltaNet 的统一：线性注意力 delta rule = 线性模型一步 SGD。Titans 非线性网络突破 O(d²) 容量上限。

### 待解决问题
计算开销；稳定性；与标准注意力的集成。

### 对未来的影响
可能是 Transformer 之外的新范式。与 SSM 共享"有状态推理"思想，但状态通过学习更新。

---

## 跨分支汇总

### 子分支关系图

```
Standard MHA (1.1) ─┬──→ KV Cache 优化 (1.2) ────→ KV 压缩 (1.10)
                    │    [GQA/MQA/MLA/CLA]         [H2O/SnapKV/KIVI]
                    ├──→ Sparse Attention (1.3) [SWA/NSA/MoBA]
                    ├──→ Negative Weights (1.5) [DiffTransformer]
                    ├──→ Different Activation (1.6) [Sigmoid/Polynomial]
                    └──→ Hardware-Efficient (1.9) [FlashAttention/vLLM]

Linear Attention (1.4) ←── SSD 对偶性 ──→ SSM/RNN (1.7)
[GLA/DeltaNet/Lightning]                  [Mamba/RWKV/xLSTM]
      ↑ 特例                                    │
Test-Time Memory (1.12) ←── 新范式              └──→ Hybrid (1.8)
[TTT/Titans]                                    [Jamba/Griffin/MiniMax]

推理优化 (1.11) ←── 互相促进 ──→ KV 压缩 (1.10)
```

### 大厂 Token Mixer 选择矩阵

| 公司 | KV优化 | Sparse | Linear | SSM | Hybrid | Hardware |
|------|--------|--------|--------|-----|--------|----------|
| Meta | GQA | Llama4 iRoPE | - | - | Llama4交替 | FA |
| DeepSeek | **MLA** | - | - | - | - | FA |
| Google | GQA | Gemma 5:1 | - | Griffin | RecurrentGemma | FA |
| MiniMax | GQA | - | **Lightning** | - | **7:1混合** | - |
| Nvidia | GQA | - | - | Mamba | **Nemotron-H** | FA |
| Qwen | GQA(4KV) | - | - | - | - | FA |
| 阶跃 | **MFA** | - | - | - | - | FA |

### 核心 Trade-off 表

| 子分支 | 速度 | 质量 | 内存 | 实现难度 | 成熟度 |
|--------|------|------|------|---------|--------|
| MHA | ★★ | ★★★★★ | ★★ | ★ | ★★★★★ |
| GQA | ★★★ | ★★★★☆ | ★★★★ | ★★ | ★★★★★ |
| MLA | ★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★ |
| Sparse | ★★★ | ★★★★ | ★★★ | ★★★ | ★★★ |
| Linear | ★★★★★ | ★★★ | ★★★★★ | ★★★ | ★★ |
| SSM | ★★★★★ | ★★★☆ | ★★★★★ | ★★★★ | ★★★ |
| Hybrid | ★★★★ | ★★★★☆ | ★★★★ | ★★★★ | ★★★ |
| KV压缩 | ★★★★ | ★★★★ | ★★★★★ | ★★ | ★★★★ |
| TTT/Titans | ★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★ |

### 演化时间线 (2017-2026)

- **2017**: MHA (Vaswani) — Transformer 奠基
- **2019**: MQA (Shazeer), Sparse Transformer (Child)
- **2020**: Reformer/Longformer/Performer/Linear Attention — 效率探索爆发
- **2021**: S4 (Gu) — SSM 元年
- **2022**: FlashAttention (Dao) — IO-aware 革命
- **2023**: GQA/RetNet/RWKV/Hyena/StreamingLLM/H2O — 高效化大爆发
- **2024**: Mamba/MLA/GLA/DeltaNet/xLSTM/Jamba/Griffin/FA-3/SnapKV/KIVI/MTP/TTT — 巅峰年
- **2025**: NSA/MoBA/Mamba-2/Lightning/MiniMax-01/iRoPE/Titans/DeepSeek-V3/Nemotron-H — 混合走向生产
- **2026+**: Mamba-3/TTT-v2/统一稀疏-压缩框架/生产级 Titans — 新范式成形
