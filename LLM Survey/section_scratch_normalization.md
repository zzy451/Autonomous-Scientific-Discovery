# Section 3: Normalization — Section Scratch

> 基于 35 篇笔记 (N01--N37) 生成 | 生成日期: 2026-04-06
> 对应论文清单: `paper_list_normalization.md`

---

## 0. Section 总论 (Opening Paragraph)

**中心论点**: 归一化 (normalization) 是 Transformer 架构中最"隐蔽的关键组件"——它既不像注意力机制那样定义架构身份，也不像位置编码那样引发直觉争论，但归一化的选择（类型、位置、是否保留）直接决定了训练稳定性上限、模型可缩放深度、硬件效率以及最终性能。从 2015 年 Batch Normalization 开创归一化范式，到 2026 年 GeoNorm / SiameseNorm 试图从流形几何和双流架构彻底解决位置之争，归一化的演化轨迹折射出深度学习对"训练稳定性本质"理解的持续深化。本节按九条技术分支系统梳理这一演化。

**演化总脉络**:
```
BN (2015) → LN (2016) → RMSNorm (2019) → 位置之争 (Pre/Post/Sub/Peri, 2018-2025)
                                          → 注意力内归一化 (QK-Norm, 2020-2026)
                                          → 条件化归一化 (adaLN, 2023)
                                          → 全面归一化 (nGPT, 2024)
                                          → 无归一化 (DyT/Derf, 2025)
                                          → 硬件协同 (FP8+Norm, 2025-2026)
```

---

## 3.1 基础归一化方法: BN → LN → IN → GN

### 分支定义与存在理由
这一分支建立了"归一化维度的选择"这一核心分类框架。四种基础方法沿 batch/feature/spatial 维度的不同切分定义了归一化的设计空间，最终 LayerNorm 因与 Transformer 的结构契合而成为标配。

### 技术介绍

**Batch Normalization (BN)** [N01, Ioffe & Szegedy 2015]:
- 公式: $\hat{x}_i = \frac{x_i - \mu_\mathcal{B}}{\sqrt{\sigma^2_\mathcal{B} + \epsilon}}$, $y_i = \gamma \hat{x}_i + \beta$
- 归一化维度: 跨 batch $(N, H, W)$
- 核心贡献: 允许更高学习率、降低初始化敏感性、隐式正则化
- 在 CNN (ResNet) 中极为成功，但在 Transformer/LLM 中**几乎不使用**

**LayerNorm (LN)** [N02, Ba et al. 2016]:
- 公式: 对单个样本的所有特征维度 $d$ 计算 $\mu, \sigma^2$，归一化后乘 $\gamma$ 加 $\beta$
- 归一化维度: 特征维度 $(D)$，与 batch 无关
- 可学习参数: $2d$ 个 ($\gamma, \beta$)
- 操作: 减均值 (zero-centering) + 除标准差 (variance normalization) + 仿射变换

**Instance Normalization (IN)** [N03, Ulyanov et al. 2016]:
- 归一化维度: 每样本每通道的空间维度 $(H, W)$
- 为风格迁移设计，NLP 中几乎不使用
- 定位: 归一化维度谱系的一环

**Group Normalization (GN)** [N04, Wu & He 2018]:
- 将 $C$ 个通道分为 $G$ 组，组内归一化
- $G = C$ 退化为 IN，$G = 1$ 退化为 LN → GN 是 IN 和 LN 的统一框架
- 重要近期应用: Differential Transformer 中用于注意力头输出归一化 [N24]

**为什么 LN 成为 Transformer 标配 (核心论证)**:
1. **与 batch 无关**: NLP 序列长度可变，BN 的 batch 维度统计不稳定
2. **训练-推理一致**: 不需要维护 running statistics
3. **分布式友好**: 不需跨设备同步 batch 统计量
4. **单样本推理**: 推理时每个样本独立计算，与训练完全一致
5. GPT-2/3 使用 LN (Pre-LN)，BERT 使用 LN (Post-LN)，奠定了 LN 的统治地位

### 理论支撑
- BN 的原始理论 ("Internal Covariate Shift") 后续被质疑 (Santurkar et al. 2018)，但其"可学习仿射变换"的设计范式被所有后续方法继承
- LN 的 re-centering 和 re-scaling 不变性为后续 RMSNorm 的简化提供了理论分析框架 [N09]
- GN 提供了 IN 和 LN 的统一视角，揭示了归一化维度选择是一个连续谱 [N04]

### 待解决问题
- LN 的均值中心化是否真正必要？→ 由 RMSNorm (3.2) 回答
- 归一化的最优维度粒度是什么？→ 由 GN in Diff-Transformer (3.4) 部分回答
- 为什么 BN 在 NLP 中失败的深层原因？→ 由 PowerNorm (3.2) 回答

### 对未来的影响
BN → LN 的迁移确立了"对特征维度归一化"作为序列模型的默认范式，为后续所有变体设定了基线。

### 潜在技术方向
- 动态粒度归一化 (根据输入自适应选择 LN/GN/IN 的粒度)
- 跨模态统一的归一化选择理论

---

## 3.2 高效变体: RMSNorm → ScaleNorm → PowerNorm

### 分支定义与存在理由
这一分支追问: LayerNorm 的哪些组件是真正必要的？通过系统性地去除组件 (减均值、逐元素仿射)，发现**重缩放不变性 (re-scaling invariance) 是归一化成功的关键，而重中心化 (re-centering) 可以安全去除**。这一发现使 RMSNorm 成为 2023+ 大语言模型的事实标准。

### 技术介绍

**RMSNorm** [N09, Zhang & Sennrich 2019]:
- 公式: $\text{RMS}(\mathbf{a}) = \sqrt{\frac{1}{n}\sum_{i=1}^{n} a_i^2}$, $\bar{a}_i = \frac{a_i}{\text{RMS}(\mathbf{a})}$, $y_i = \gamma_i \cdot \bar{a}_i$
- 核心假设: LayerNorm 的成功主要归因于 re-scaling invariance，re-centering 贡献可忽略
- 相比 LN: 仅一次归约操作 (vs 两次)，无偏移 $\beta$，可学习参数从 $2d$ 降至 $d$
- 实测加速 7%--64%
- **工业采用**: LLaMA 1/2/3, PaLM, Gemma 1/2, Qwen 1/2/3, Mistral, DeepSeek 等均采用

**ScaleNorm + FixNorm** [N22, Nguyen & Salazar 2019]:
- ScaleNorm: $\text{ScaleNorm}(x) = g \cdot \frac{x}{\|x\|_2}$ — 仅**1 个**可学习参数
- 将向量映射到半径为 $g$ 的超球面
- FixNorm: 对词嵌入强制固定 L2 范数 $c$，解决权重共享时嵌入范数漂移
- ScaleNorm 与 RMSNorm 的数学关系: 差别仅在 $\sqrt{d}$ 常数因子和参数化方式 (逐元素 $\gamma$ vs 全局 $g$)
- 在低资源翻译上 +1.1 BLEU，但在主流 LLM 中**未被广泛采用**
- 其超球面思想在 nGPT (3.6) 中得到全面发展

**PowerNorm** [N23, Shen et al. 2020]:
- 深入分析 BN 在 NLP 中失败的根因: NLP 数据的 batch 统计量波动远比视觉数据剧烈 (3--5 倍)
- 三项改进: (1) 去除均值中心化 (类似 RMSNorm)，(2) 用 running quadratic mean (EMA) 替代 per-batch 方差，(3) 近似反向传播保证梯度有界
- 公式: $\text{PN}(x) = \gamma \cdot \frac{x}{\psi_t} + \beta$，$\psi_t^2 = (1-\rho)\psi_{t-1}^2 + \rho \cdot \mathbb{E}_B[x^2]$
- 在 NLP 中超越 LN，但因仍依赖 batch 维度而未被主流 LLM 采用

### 理论支撑

**去均值中心化的理论依据 (核心论证)**:

1. **不变性分析** [N09]: RMSNorm 保持 re-scaling invariance ($\text{RMSNorm}(\alpha x) = \text{RMSNorm}(x)$)，这是归一化成功的关键不变性
2. **几何解释** [N27, Gupta et al. 2024]:
   - LN 的减均值本质是移除输入在均匀向量 $\mathbf{1} = [1,...,1]^T$ 方向上的投影
   - 此操作具有**不可逆性**——丢失的信息无法通过 $\gamma, \beta$ 恢复
   - 使用 RMSNorm 训练的 LLM (如 LLaMA) **自然学到**了与均匀向量正交的表示
   - 结论: LN 的均值减除是**冗余的显式约束**，模型会自发学到等效的几何结构
3. **统计量波动分析** [N23]: NLP 中 batch 统计量波动大，去除均值计算减少了不稳定源

### 待解决问题
- RMSNorm 在量化场景下的表现 (非零中心可能影响 INT8 对称量化)
- ScaleNorm 的极致简化 (仅 1 个参数) 在大规模 LLM 中是否可行？
- 逐元素 $\gamma$ vs 全局标量 $g$ 的表达力-效率权衡

### 对未来的影响
RMSNorm 取代 LN 成为 LLM 标准的过程是一个典范的"理论假设 → 实验验证 → 工业采纳 → 事后理论解释"循环。它确立了**最小化原则**: 归一化应只保留必要的不变性。

### 潜在技术方向
- 自适应精度的 RMSNorm (在低精度训练中动态调整 RMS 计算精度)
- 基于任务复杂度的归一化组件选择 (简单任务用 ScaleNorm，复杂任务用完整 LN)

---

## 3.3 归一化位置理论: Pre-Norm vs Post-Norm 及其超越

### 分支定义与存在理由
归一化放在子层的哪个位置，是 Transformer 架构设计中影响最深远的选择之一。这一分支从理论和实践两个层面系统分析了不同位置的梯度流、方差增长和最终性能，并推动了从单一位置向多位置、混合位置的演进。

### 技术介绍

**Pre-LN vs Post-LN 的奠基分析** [N05, Xiong et al. 2020]:
- Post-LN (原始 Transformer): $\text{Output} = \text{LN}(x + \text{SubLayer}(x))$ — 归一化在残差**之后**
- Pre-LN (现代标准): $\text{Output} = x + \text{SubLayer}(\text{LN}(x))$ — 归一化在子层**之前**
- Mean Field Theory 分析: Post-LN 在初始化阶段靠近输出层的参数梯度非常大 → 需要 warmup
- Pre-LN 提供"梯度高速公路" (gradient highway)，梯度可无衰减地流过任意深度
- **里程碑意义**: 直接影响了所有后续 LN 位置研究

**Sandwich LayerNorm** [N07, Ding et al. 2021 / CogView]:
- 结构: $\text{Output} = x + \text{LN}_2(\text{SubLayer}(\text{LN}_1(x)))$ — 子层前+后双 LN
- 动机: 解决 FP16 训练 4B 参数 Transformer 时的 NaN 问题
- 效果: 约束子层输出的数值范围，消除 FP16 训练中的 NaN 损失
- 2024 年被 Gemma 2 以 Pre+Post RMSNorm 形式重新采用

**DeepNorm** [N08, Wang et al. 2022]:
- 核心修改: $x_{l+1} = \text{LN}(\alpha \cdot x_l + f(x_l))$，$\alpha > 1$ 增大残差路径权重
- 配合理论推导的 Xavier 初始化缩放 ($\beta$ 因子)
- 成功训练 **1000 层** Transformer (2500 个子层)
- 200 层 3.2B DeepNet 超过 48 层 12B SOTA 5 BLEU → 深度是高效的缩放维度
- 结合了 Post-LN 的**性能优势**和 Pre-LN 的**训练稳定性**

**MAGNETO / Sub-LN** [N20, Wang et al. 2022]:
- 在子层**内部**投影之间插入额外 LN (细粒度控制)
- 注意力: $x \to \text{LN}_1 \to \text{QKV投影} \to \text{Attn} \to \text{LN}_2 \to \text{输出投影} \to +x$
- FFN: $x \to \text{LN}_1 \to W_1 + \text{Act} \to \text{LN}_2 \to W_2 \to +x$
- 配合 DeepNet 理论初始化，跨模态 (语言/视觉/语音/多模态) 统一超过 Pre-LN 和 Post-LN
- 代表了从子层级到**投影级**的归一化粒度细化

**Peri-LN** [N21, 2025]:
- 结构: $x_{l+1} = x_l + \text{LN}_2(f(\text{LN}_1(x_l)))$ — 子层两端归一化，残差连接后**无** LN
- 与 Sandwich-LN 的关键区别: LN_2 在残差加法**之前**，残差路径保持直连
- 同时获得: Pre-LN 的梯度流优势 + Post-LN 的方差控制优势
- 方差增长: $\text{Var}(x_{l+1}) \approx \text{Var}(x_l) + O(1)$ (线性受控增长)
- 在 3.2B 参数模型上验证

**SiameseNorm** [N37, 2026]:
- 根本性不同: **双流架构**，同时维护 Pre-Norm 流和 Post-Norm 流
- 两流**共享参数**，仅独立 Norm 层参数，最终融合输出
- Pre-Norm 流提供梯度高速公路 → 稳定性；Post-Norm 流提供表示质量 → 性能
- 1.3B 参数预训练验证，优化鲁棒性显著优于单流方案
- 代价: 推理时计算量接近翻倍 (双流前向)

**GeoNorm** [N30, 2026]:
- 用流形上的**测地线更新**替代传统归一化层: $h_{l+1} = \text{Exp}_{h_l}(\alpha_l \cdot v_l)$
- 从几何视角统一 Pre-Norm 和 Post-Norm (分别是切空间变换和流形投影的特例)
- 创新引入**归一化调度**: 训练初期强约束 (类 Post-Norm)，后期放松 (类 Pre-Norm)
- 类比学习率调度的思想

### 理论支撑 (梯度消失/爆炸分析)

**归一化动力学统一理论** [N28, Karagodin et al. 2025]:
- 将 token 表示建模为**超球面上的交互粒子**
- 自注意力 = 粒子间交互力，归一化 = **速度调节器**
- Post-LN: 速度随深度衰减，早期快速聚类
- Pre-LN: 速度基本恒定，聚类缓慢但稳定
- Peri-LN: 最优速度-稳定性权衡
- nGPT: 严格超球面约束，粒子轨迹最规则
- 核心发现: 归一化位置之争本质是**表示空间中的速度-稳定性权衡**

**位置演进谱系**:
```
Post-LN (2017) → Pre-LN (2018) → Sandwich-LN (2021) → Sub-LN (2022) → Peri-LN (2025)
                 → DeepNorm (2022, 缩放残差)
                 → GeoNorm (2026, 测地线)
                 → SiameseNorm (2026, 双流)
                 → HybridNorm (2025, 模块级混合, 见 3.9)
```

### 待解决问题
- 归一化位置的最优选择是否取决于模型规模？(小模型可能更适合 Post-LN，超大模型更适合 Pre-LN？)
- 归一化调度 (GeoNorm) 的最优策略——类 warmup 还是类 cosine？
- SiameseNorm 的推理效率能否通过蒸馏或剪枝解决？
- Sub-LN 的细粒度归一化在百亿级 LLM 中是否值得额外开销？

### 对未来的影响
位置之争推动了从"选择一个固定位置"到"设计位置策略"的范式转变。Peri-LN 和 HybridNorm 展示了不同子模块可以使用不同位置，GeoNorm 引入了训练过程中的动态调整，SiameseNorm 则彻底放弃了单一路径的假设。

### 潜在技术方向
- 可学习的归一化位置 (让模型自动选择每层的最优 LN 位置)
- 归一化位置的 NAS (神经架构搜索)
- 基于训练阶段的自适应位置切换 (GeoNorm 调度思想的进一步发展)

---

## 3.4 注意力内部归一化: QK-Norm, Logit Soft-Capping, GroupNorm in Diff-Transformer

### 分支定义与存在理由
传统归一化 (LN/RMSNorm) 作用于子层的输入或输出，但注意力机制**内部**同样存在数值不稳定源——特别是 $QK^T$ 点积的 logit 爆炸。这一分支将归一化从"子层级"深入到"注意力操作级"，在注意力的输入 (Q, K)、内部 (logits) 和输出 (head outputs) 三个层次施加约束。

### 技术介绍

**QK-Norm** [N10, Henry et al. 2020]:
- 公式: $\hat{Q} = Q / \|Q\|_2$, $\hat{K} = K / \|K\|_2$，$\text{Attn} = \text{softmax}(g \cdot \hat{Q}\hat{K}^T)V$
- 将注意力 logits 约束为余弦相似度 $\in [-1, 1]$，从根本上消除 logit 爆炸
- $g$: 每个 head 一个可学习标量 (初始化为 $\sqrt{d_k}$)，替代固定 $1/\sqrt{d_k}$
- 有效防止 softmax 饱和和注意力熵崩塌
- **主流 LLM 采用**: Gemma 2/3, Qwen 3, OLMo 2, Chameleon
- **与 MLA 不兼容**: DeepSeek-V3 的 Multi-Latent Attention 不具体化完整 Q/K → 不使用 QK-Norm

**Logit Soft-Capping** [N26, Gemma 2]:
- 公式: $\text{logits} = \text{cap} \cdot \tanh(\text{logits} / \text{cap})$
- 注意力 logits cap: 50.0; 最终 logits cap: 30.0
- 将 logits 约束在 $(-\text{cap}, +\text{cap})$ 范围内
- 与 QK-Norm 互补: QK-Norm 从输入侧约束，soft-capping 从输出侧约束

**GroupNorm in Differential Transformer** [N24, Ye et al. 2024]:
- 差分注意力: $\text{DiffAttn} = (\text{softmax}(Q_1K_1^T/\sqrt{d}) - \lambda \cdot \text{softmax}(Q_2K_2^T/\sqrt{d}))V$
- 差分输出的值域不再被 softmax 的 $[0,1]$ 约束 → 需要 GroupNorm 重新控制尺度
- GroupNorm 对每个注意力头独立归一化 (group 数 = head 数)
- $(1 - \lambda_\text{init})$ 缩放因子对齐梯度流
- 效果: 减少幻觉、增强上下文学习、降低激活异常值、改善量化

**Enhanced QKNorm (Lp 范数)** [N29, Lopez-Rubio et al. 2026]:
- 将 L2 归一化推广为 Lp 归一化: $\hat{Q} = Q / \|Q\|_p$
- 核心发现: L2 不是唯一有效选择，不同 p 值对应不同的注意力空间几何
- 局限: 仅在 nanoGPT/Tiny Shakespeare 小规模验证

### 理论支撑
- QK-Norm 的有界性保证: 归一化后 $\hat{Q}_i^T \hat{K}_j \in [-1, 1]$，logits 被约束在 $[-g, g]$
- Diff-Transformer 的差分消噪理论: 类似差分放大器消除共模噪声
- Lp 归一化定义了一族不同的注意力几何 [N29]，为架构设计提供了新的自由度

### 待解决问题
- QK-Norm 与 Multi-Latent Attention (MLA) 的兼容方案
- Lp-QKNorm 的最优 p 值是否取决于模型规模或任务？
- logit soft-capping 的最优 cap 值如何确定？

### 对未来的影响
注意力内部归一化已从"可选增强"变为"大规模训练的必要保护"。Gemma 2 的三层归一化保护体系 (Pre+Post RMSNorm + QK-Norm + soft-capping) 可能成为未来 LLM 的标准配置。

### 潜在技术方向
- 自适应 cap 值 (根据训练阶段或层深度动态调整 soft-capping 范围)
- 注意力内部归一化与线性注意力变体的交互
- V 向量的归一化 (目前主要关注 Q, K，HybridNorm [N31] 已开始探索 QKV-Norm)

---

## 3.5 条件化/自适应归一化: AdaNorm, adaLN-Zero/DiT, FiLM

### 分支定义与存在理由
标准归一化的仿射参数 ($\gamma, \beta$) 对所有输入共享。条件化归一化将这些参数变为**条件信号的函数**，使归一化层成为轻量级的条件信号注入载体。这一思想在扩散模型 (Diffusion Transformers) 中取得了决定性成功。

### 技术介绍

**AdaNorm** [N06, Xu et al. 2019]:
- 自适应版 LayerNorm: 根据输入动态调整归一化强度
- "容易"的输入减少归一化，"困难"的输入加强归一化
- 提出了均值偏移、方差缩放、可学习参数各自贡献的分析
- 在大规模 LLM 中未被广泛采用，但"自适应归一化"理念影响了后续工作

**adaLN / adaLN-Zero (DiT)** [N11, Peebles & Xie 2023]:
- **adaLN**: 条件信号通过 MLP 动态生成 $\gamma, \beta$ 替换 LayerNorm 的固定参数
  - $\gamma, \beta = \text{MLP}(\text{embed}(t) + \text{embed}(c))$
- **adaLN-Zero**: 额外生成 $\alpha$ (门控参数)，初始化 MLP 输出层为零
  - $\text{output} = x + \alpha \cdot \text{SubLayer}(\gamma \cdot \hat{x} + \beta)$
  - 初始状态: $\alpha = 0$ → 每个 block 等效于恒等函数
- 每个 block 需要 6 组参数: 注意力层和 FFN 层各需 $\gamma, \beta, \alpha$
- **显著优于** cross-attention 和 in-context conditioning
- ImageNet 256x256: DiT-XL/2 + adaLN-Zero 达到 FID=2.27 (当时 SOTA)
- **后续影响**: Stable Diffusion 3 (MMDiT), Flux, Sora 均采用 DiT + adaLN

**FiLM** (Feature-wise Linear Modulation, Perez et al. 2018):
- adaLN 的前身: $\text{FiLM}(x) = \gamma(c) \cdot x + \beta(c)$
- 最初用于视觉 QA，将问题特征注入视觉特征的归一化层
- adaLN 是 FiLM 在 Transformer 归一化层中的特化应用

### 理论支撑
- 条件化归一化的信息注入效率: 仿射参数空间是条件信号的**低维瓶颈**，迫使模型学习最紧凑的条件表示
- adaLN-Zero 的零初始化保证了训练初始的稳定性 (与 Fixup/T-Fixup 的"初始恒等函数"思想一致)

### 待解决问题
- adaLN 在自回归语言模型中的应用 (当前主要用于扩散模型)
- 条件化归一化与 Mixture of Experts (MoE) 的交互
- 多条件信号的融合策略 (不同条件如何组合生成 $\gamma, \beta$)

### 对未来的影响
adaLN 确立了"归一化层 = 条件注入点"的设计模式。在多模态生成 (文本→图像、文本→视频) 中，归一化层可能成为跨模态信号融合的标准接口。

### 潜在技术方向
- 条件化 RMSNorm (仅动态生成 $\gamma$，无 $\beta$，更轻量)
- 层级自适应: 不同层使用不同强度的条件化
- 条件化归一化在自回归 LLM 中的 prompting 机制

---

## 3.6 全面归一化架构: nGPT 超球面学习, Gemma 2 Pre+Post Norm

### 分支定义与存在理由
这一分支将归一化从"在特定位置的打补丁操作"推向"整个架构的设计原则"。nGPT 将所有向量约束在超球面上，Gemma 2 在多个层次构建归一化保护体系。两者代表了"归一化最大化"的方向——与 3.8 的"归一化最小化/去除"形成极性对比。

### 技术介绍

**nGPT — 超球面 Transformer** [N25, Loshchilov et al. 2024]:
- **全面归一化**: 所有嵌入、隐状态、QKV 投影权重、MLP 权重、输出权重均 L2 归一化到单位范数
- 层更新: $h_{l+1} = \text{Normalize}(h_l + \alpha_l \cdot (f_l(h_l) - h_l))$ — 超球面上的球面插值
- 注意力: Q, K 归一化 → 余弦相似度 $\in [-1, 1]$ (天然的 QK-Norm)
- **无传统 LN/RMSNorm 层**: 归一化是架构的固有属性而非附加组件
- 训练加速: 达到相同损失的步数减少 **4--20 倍**
- 范式转变: 从"在欧几里得空间中计算 + 在特定位置归一化"到"在超球面上全程计算"
- 局限: 基于 nanoGPT 的小规模实验，百亿级验证尚缺

**Gemma 2 — 多层次归一化保护** [N26, Google 2024]:
- **层级保护**: Pre+Post RMSNorm (子层输入+输出各一个 RMSNorm)
- **注意力保护**: QK-Norm (Q, K 的 L2 归一化)
- **logit 保护**: 注意力 logit soft-capping (cap=50) + 最终 logit soft-capping (cap=30)
- 本质是 Sandwich-LN (2021) 的 RMSNorm 版本 + QK-Norm + soft-capping
- 在工业规模 (2B/9B/27B) 上消除了 loss spikes
- 代表了"多层次防御"的工程哲学

**UnitNorm** [N32, 2024]:
- 时序 Transformer 专用: 仅 $\text{UnitNorm}(x) = x / \|x\|_2$，无 $\gamma, \beta$，零额外参数
- 解决时序数据中 LayerNorm 引发的 token shift、attention shift、sparse attention 问题
- 与 nGPT 的超球面思想一脉相承，但从时序数据实际问题独立得出
- 跨领域呼应: 不同领域独立发现超球面投影的有效性

### 理论支撑
- nGPT 的几何洞察: 在无约束空间中，优化器的很多更新方向是改变范数而非方向 → 浪费计算
- 超球面约束消除了范数这一冗余自由度 → 所有梯度更新都是"有效"的
- 粒子动力学分析 [N28] 证明 nGPT 的超球面约束使粒子轨迹最规则
- ScaleNorm (2019) → FixNorm (2019) → nGPT (2024) 形成了超球面归一化的完整发展线

### 待解决问题
- nGPT 在百亿级+模型上的验证
- 超球面约束是否限制了模型的表达力？(维度信息的范数分量被丢弃)
- Gemma 2 的多层次归一化是否过度 (over-normalized)？是否存在更精简的组合？

### 对未来的影响
nGPT 和 Gemma 2 代表了归一化设计的两个极端哲学: nGPT 追求几何的极致优雅 (一种约束统治所有)，Gemma 2 追求工程的极致稳健 (多重保护层层叠加)。未来可能需要在两者之间找到平衡。

### 潜在技术方向
- nGPT + RoPE 的兼容 (超球面约束与旋转位置编码的交互)
- 部分超球面约束 (只约束关键表示，如 Q, K，放松其他)
- Gemma 2 归一化体系的自动化搜索 (哪些保护层是必要的)

---

## 3.7 归一化-激活融合搜索: EvoNorm

### 分支定义与存在理由
归一化和激活函数在网络中通常紧邻使用，二者功能可能存在重叠和互补。EvoNorm 通过自动化搜索证明: 手工设计的 BN+ReLU 并非最优，融合归一化与激活的统一层可以超越分离式设计。

### 技术介绍

**EvoNorm** [N12, Liu et al. 2020]:
- 方法: 定义基本运算原语 (加、乘、除、sigmoid、方差、均值等)，构建计算图搜索空间，使用**进化搜索**发现最优归一化-激活层
- **EvoNorm-B0** (依赖 batch): $\text{EvoNorm-B0}(x) = x \cdot \text{sigmoid}(x / v(x))$
- **EvoNorm-S0** (不依赖 batch): $\text{EvoNorm-S0}(x) = x \cdot \text{sigmoid}(x / \text{GroupStd}(x))$
- 关键观察: sigmoid 项起"门控"作用，方差/标准差项起"归一化"作用 → 融合为一个操作
- EvoNorm-B0 超过 BN+ReLU，EvoNorm-S0 超过 GN+ReLU
- 搜索到的层在小代理任务上搜索，可直接迁移到大任务 (ImageNet、COCO)
- 在 LLM 中**尚未被广泛采用**

### 理论支撑
- 归一化和激活函数的功能重叠: 归一化约束值域，激活引入非线性 → 两者可统一
- 进化搜索空间覆盖了已知手工组合 (BN+ReLU, GN+Swish)，说明搜索是严格推广

### 待解决问题
- EvoNorm 在 Transformer/LLM 中的适用性 (原始工作仅在 CNN 上验证)
- 搜索空间能否扩展到包含 LN+GELU, RMSNorm+SwiGLU 等 Transformer 常用组合？
- 搜索的计算成本与手工设计的性价比

### 对未来的影响
EvoNorm 证明了归一化-激活的联合设计空间远未被充分探索。在 Transformer 的 FFN 中，RMSNorm + SwiGLU 的组合是否最优，值得用类似方法验证。

### 潜在技术方向
- Transformer 专用的归一化-激活融合搜索
- 将搜索空间扩展到包含注意力机制内部的归一化
- 与 NAS 结合的全架构搜索

---

## 3.8 无归一化方法: Fixup → T-Fixup → NFNet → DyT → Derf

### 分支定义与存在理由
如果归一化的核心功能可以通过其他手段 (初始化、激活函数、梯度裁剪) 实现，那么归一化层本身是否可以完全移除？这一分支从 CNN 中的初始化替代方案起步，发展到 Transformer 中的有界函数替代，最终在 DyT/Derf 上达到高潮——**归一化的本质可能不是统计归一化，而是非线性压缩**。

### 技术介绍

**Fixup** [N13, Zhang et al. 2019]:
- 核心洞察: BN 的核心功能是控制激活值尺度，可通过初始化替代
- 方法: 残差分支最后一层权重**零初始化**，其他层按 $L^{-1/(2m-2)}$ 缩放
- 效果: 初始化时每个 block = 恒等映射 → 方差不随深度增长
- CNN (ResNet) 中完全移除 BN，匹配有 BN 版本性能

**T-Fixup** [N14, Huang et al. 2020]:
- 将 Fixup 扩展到 Transformer: $W_V, W_O$ 按 $(9N)^{-1/4}$ 缩放，FFN $W_2$ 初始化为零/极小值，嵌入按 $d^{-1/2}$ 缩放
- 完全移除所有 LayerNorm 和 warmup
- 在机器翻译和 GLUE 上匹配标准 Transformer
- 核心启示: LN 在 Transformer 中的核心作用是**控制初始化阶段的激活尺度**

**NFNet** [N15, Brock et al. 2021]:
- 两项核心技术:
  1. **Scaled Weight Standardization**: 对卷积权重标准化 + 理论缩放因子
  2. **Adaptive Gradient Clipping (AGC)**: $G \leftarrow \lambda \frac{\|W\|_F}{\|G\|_F} G$ 当 $\|G\|_F / \|W\|_F > \lambda$
- AGC 的关键洞察: 梯度的"有效步长"是梯度相对于参数的**比值**，而非绝对大小
- ImageNet SOTA: 86.5% top-1，比 EfficientNet 快 8.7 倍
- BN 功能分解: (1) 控制前向信号方差 → WSS，(2) 隐式限制梯度更新 → AGC

**DyT (Dynamic Tanh)** [N16, Zhu et al. 2025]:
- 核心发现: LayerNorm 的输入-输出映射在统计上类似 tanh 的 S 形曲线
- 公式: $\text{DyT}(x) = \gamma \cdot \tanh(\alpha x) + \beta$
- $\alpha$: per-layer 可学习标量; $\gamma, \beta$: per-channel
- **纯逐元素操作，无归约** → 硬件友好性最好
- 在 ViT、LLaMA、DiT、MAE、DINO、wav2vec 2.0 等多领域**匹配**归一化
- 核心论点: **归一化的本质是非线性压缩，而非统计归一化**
- $\alpha$ 的层间变化: 浅层 $\alpha$ 小 (近似线性)，深层 $\alpha$ 大 (压缩更强)

**Derf (Dynamic Erf)** [N17, Chen et al. 2025]:
- 系统分析替代函数的关键属性: 有界性、单调性、光滑性、零中心性、**饱和速度**
- 公式: $\text{Derf}(x) = \text{erf}(\alpha x + s)$ — 比 DyT 更简洁 (无外部 $\gamma, \beta$)
- $\text{erf}$ vs $\tanh$ 的关键差异: erf 饱和速度更慢 (高斯衰减 $O(e^{-x^2})$ vs 指数衰减 $O(e^{-2|x|})$)
  - $|x|=2$ 处导数: erf ≈ 0.0183 vs tanh ≈ 0.0007 (26 倍差距)
- 更慢饱和 → 更好梯度流 → 更好优化 → **首次一致性超越**有归一化版本
- 在 ViT、LLaMA、DiT、MAE 所有任务上一致超过 LN/RMSNorm/DyT

**GeoNorm** [N30, 2026] 和 **SiameseNorm** [N37, 2026] 也可视为无传统归一化层的方法，但更多属于位置理论 (3.3)。

### 理论支撑
- **Fixup/T-Fixup**: 方差增长分析——残差连接使输出方差 $\text{Var}(x_L) \sim O(L)$，零初始化消除此增长
- **NFNet**: BN 功能的显式分解 (前向方差控制 + 反向梯度约束)
- **DyT/Derf**: 对"归一化本质"的重新理解——核心是有界非线性压缩而非统计量计算
- **异常值-归一化共生** [N33]: 归一化层与涌现异常值 (attention sink, massive activation) 形成不可分割的功能单元。DyT/Derf 用有界函数提供了替代的重缩放机制

### 待解决问题
- DyT/Derf 在百亿级 LLM 上的大规模验证
- Derf 超越归一化的优势是否随模型规模持续存在？
- 无归一化方法与低精度训练 (FP8) 的兼容性——无归一化是否消除异常值，使 FP8 更友好？
- 最优替代函数的理论界——是否存在证明某函数是最优的理论框架？

### 对未来的影响
DyT/Derf 的成功可能是过去十年归一化研究中最具颠覆性的发现。如果归一化的本质确实是非线性压缩，那么整个"归一化层"的概念可能需要重新定义。

### 潜在技术方向
- DyT/Derf + Muon 优化器的联合无归一化方案
- 层级自适应的替代函数 (每层自动选择 tanh/erf/其他)
- Derf 在扩散模型、多模态模型中的验证
- 理论上界: 有界函数能替代归一化的充分必要条件

---

## 3.9 前沿交叉: FP8 训练归一化, 优化器-归一化耦合, Outlier-Driven Rescaling, HybridNorm

### 分支定义与存在理由
归一化不再只是一个独立的架构组件，而是与硬件精度 (FP8)、优化器设计 (Muon)、异常值管理 (outlier rescaling)、模块级策略 (HybridNorm) 深度交织。这一分支汇集了 2025--2026 年归一化研究的最前沿交叉方向。

### 技术介绍

#### 9a. FP8 训练中的归一化

**FOG (Fast and Outlier-Guarded)** [N34, 2025]:
- FP8 训练的核心障碍: 激活异常值超出 FP8 动态范围 (±448)
- FOG 通过归一化重设计从架构层面抑制异常值:
  1. **QK-Norm (必选)**: 将注意力 logits 约束为余弦相似度 → FP8 安全范围内
  2. **RMSNorm 位置优化**: 在关键位置插入额外 RMSNorm → 控制 FFN 中间激活尺度
- 首次实现 Transformer block 内**所有 GEMM** (包括注意力) 均使用 FP8
- 吞吐量比 BF16 提升 **40%**
- 监控指标: **激活峰度 (kurtosis)** — 低峰度 = FP8 友好

**Why Low-Precision Training Fails** [N35, 2025]:
- 失败的两个交织机制:
  1. 注意力中涌现的**低秩相似表示** → 信息集中在少数维度 → 量化误差放大
  2. **有偏舍入误差**在归一化层中累积放大 (RMSNorm 除以被低估的 RMS → 全局过度放大)
- 正反馈循环: 低秩化 → 量化误差 → 通过 softmax/RMSNorm 放大 → 梯度异常 → 加剧低秩化 → loss 爆炸
- **归一化是双刃剑**: 全精度下提供稳定性，低精度下可能成为**误差放大器**
- 最小修复: QK-Norm + 关键累加步骤保持较高精度

#### 9b. 优化器-归一化耦合 (Muon)

**Muon 优化器与谱控制** [N36, 2025-2026]:
- Muon 的核心: 正交化动量更新 $\theta_t = \theta_{t-1} - \text{lr} \cdot UV^T$ (SVD 分解后取正交方向)
- 隐式功能: 维持权重矩阵的谱条件 → 间接控制激活范数 → 防止梯度爆炸/消失
- **谱控制替代归一化**: 仅在优化器层面维持谱条件就足以保持 $\mu P$ 兼容的缩放 → 可消除显式归一化层
- 与 DyT/Derf 的对偶关系:
  - DyT/Derf: 在**前向传播**中用有界函数替代归一化
  - Muon: 在**反向传播**中用谱控制替代归一化的隐式效果
- 规模化需要: 添加权重衰减 + 逐参数更新尺度调整 → 本质是补偿移除归一化后丢失的功能
- 开放问题: Muon + DyT/Derf 的联合方案能否**完全**消除归一化？

#### 9c. 异常值驱动的重缩放

**Outlier-Driven Rescaling** [N33, 2026]:
- 核心洞察: Transformer 训练中的异常值 (attention sink, massive activation) **不是 bug，而是 feature**
- 异常值-归一化共生:
  - 移除归一化 → 异常值消失，但训练退化
  - 保留归一化但裁剪异常值 → 同样退化
  - 结论: 异常值和归一化是不可分割的功能单元
- Massive Activation 的重缩放机制: 当 $x_k \gg x_i$ 时，$\text{RMS}(x) \approx |x_k|/\sqrt{d}$，非异常维度被缩放为 $\hat{x}_i \approx x_i \cdot \sqrt{d} / |x_k| \cdot \gamma_i$ → **异常值的幅值控制了所有其他维度的有效尺度**
- 对量化的启示: 量化方案需要**保留异常值的功能**而非简单消除
- 对 DyT/Derf 的新解释: 有界函数提供了替代的重缩放机制 (不依赖异常值)

#### 9d. HybridNorm — 模块级混合归一化

**HybridNorm** [N31, 2025]:
- 策略: 注意力用 QKV-Norm，FFN 用 Post-Norm
  - QKV-Norm: 控制 Q, K, V 的范数 → 防止 logit 爆炸 + 控制输出尺度
  - Post-Norm in FFN: 保留 Post-Norm 的梯度信号和表示质量优势
- 在 Dense Transformer 和 **Sparse MoE** 架构上均有效
- 对 MoE 的特殊价值: Post-Norm 帮助控制不同专家输出的尺度一致性
- 实用主义方案: 不追求理论统一，而是在不同子模块中使用最适合的归一化

### 理论支撑
- FP8 归一化: 归一化层中的归约操作 (RMS 计算) 在低精度下引入系统性偏差 [N35]
- 异常值共生: 归一化的"除法"操作本质上将异常值的幅值信息广播到所有维度 [N33]
- 优化器-归一化对偶: 归一化控制前向传播的激活尺度，Muon 控制反向传播的更新尺度 → 两者功能互补 [N36]

### 待解决问题
- Muon 的 SVD 计算开销是否值得用来换取移除归一化？
- FP8 + 无归一化 (DyT/Derf) 的组合是否消除了异常值问题？
- HybridNorm 的最优模块-归一化匹配是否可以自动搜索？
- 异常值-归一化共生关系在超大规模模型中是否更强？

### 对未来的影响
这些交叉方向暗示: **归一化的本质可能不在于特定的网络层，而在于维持训练过程中的某些不变量 (谱条件、范数约束、值域约束)**。这些不变量可以通过归一化层 (传统方式)、有界函数 (DyT/Derf)、优化器 (Muon)、架构约束 (nGPT) 或它们的组合来实现。

### 潜在技术方向
- **FP4/FP6 训练**: 更极端的低精度下，归一化需要怎样的重新设计？
- **Muon + Derf + nGPT**: 三管齐下的无传统归一化方案
- **自适应精度归一化**: 根据异常值分布动态选择 RMS 计算的精度
- **归一化的编译器优化**: 将归一化操作融合到矩阵乘法 kernel 中

---

## 综合图谱: 归一化方法的多维分类

### 按"归一化量"排序

```
最少归一化                                              最多归一化
  |                                                        |
  Derf  DyT  T-Fixup  Fixup  NFNet  RMSNorm  LN  Peri-LN  Gemma2  nGPT
  (无)  (无)  (无)    (无)   (无)   (极简)  (标准) (双重)  (三层)  (全面)
```

### 按"归一化层次"排序

| 层次 | 方法 | 目标 |
|------|------|------|
| 权重层 | nGPT 权重归一化, WSS (NFNet) | 控制权重尺度 |
| 嵌入层 | FixNorm, nGPT 嵌入归一化 | 控制嵌入范数 |
| 子层级 | Pre-LN, Post-LN, Peri-LN, Sub-LN | 控制激活尺度 |
| 注意力输入 | QK-Norm, QKV-Norm | 控制 logit 范围 |
| 注意力输出 | GroupNorm (Diff-Transformer), soft-capping | 控制注意力输出尺度 |
| 优化器级 | Muon 谱控制, AGC (NFNet) | 控制更新幅度 |
| 无归一化 | DyT, Derf | 有界非线性压缩 |

### 时间线总结

| 年份 | 关键里程碑 | 引用笔记 |
|------|-----------|---------|
| 2015 | Batch Normalization 开创归一化范式 | N01 |
| 2016 | LayerNorm 成为序列模型标准 | N02, N03 |
| 2018 | GroupNorm 统一 IN/LN 谱系 | N04 |
| 2019 | RMSNorm 去除均值中心化; Fixup 初始化替代 BN; ScaleNorm 极简化; AdaNorm 自适应 | N09, N13, N22, N06 |
| 2020 | Pre-LN vs Post-LN 理论分析; T-Fixup 无 LN Transformer; QK-Norm; PowerNorm; EvoNorm | N05, N14, N10, N23, N12 |
| 2021 | Sandwich-LN (CogView); NFNet 无 BN SOTA | N07, N15 |
| 2022 | DeepNorm 1000 层 Transformer; MAGNETO/Sub-LN 跨模态统一 | N08, N20 |
| 2023 | adaLN-Zero/DiT 条件化归一化 | N11 |
| 2024 | nGPT 超球面学习; Gemma 2 多层次保护; Diff-Transformer GroupNorm; Re-introducing LN 几何分析; UnitNorm | N25, N26, N24, N27, N32 |
| 2025 | DyT 无归一化匹配; Derf 无归一化超越; Peri-LN; HybridNorm; FOG FP8; 低精度失败分析; Muon 谱控制; 归一化动力学理论 | N16, N17, N21, N31, N34, N35, N36, N28 |
| 2026 | GeoNorm 流形统一; SiameseNorm 双流; Outlier-Driven Rescaling; Enhanced QKNorm | N30, N37, N33, N29 |

---

## Section 结尾: 开放问题与未来方向

1. **归一化的本质是什么？** DyT/Derf 说是非线性压缩，nGPT 说是几何约束，Muon 说是谱条件——这三种视角能否统一？
2. **归一化是否会消失？** 如果优化器 + 初始化 + 有界函数可以完全替代，归一化层是否会从架构中消失？
3. **归一化与硬件的协同进化**: FP4/FP6 时代的归一化设计
4. **归一化与稀疏架构**: MoE 中不同专家是否需要不同的归一化策略？
5. **归一化的自动化设计**: 能否像 NAS 一样自动搜索最优的归一化类型、位置和参数化？
6. **超大规模验证**: nGPT、Derf、GeoNorm 等新方法在万亿参数模型上的表现

---

> **引用笔记**: N01--N37 (共 35 篇)
> **核心参考文献**: 按出现频率排序 — RMSNorm (N09), Pre/Post-LN (N05), DyT (N16), Derf (N17), nGPT (N25), Gemma 2 (N26), QK-Norm (N10), DeepNorm (N08), Peri-LN (N21)
