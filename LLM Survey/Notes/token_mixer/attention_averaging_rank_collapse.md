# Attention 均匀化与 Rank Collapse 综述

## 1. 现象定义与数学描述

### 1.1 核心现象概览

在深层 Transformer 中存在一系列相互关联的注意力退化现象，统称为 **Attention Degeneration**。这些现象从不同角度描述了同一类问题：随着网络深度或序列长度增加，模型内部表示和注意力模式逐渐丧失区分能力。

| 现象 | 核心描述 | 首次/关键论文 |
|------|----------|--------------|
| **Rank Collapse (in Depth)** | 注意力矩阵收敛到 rank-1，所有 token 获得相同表示 | Dong et al. (2021) |
| **Rank Collapse (in Width)** | 随 context length 增加，softmax 注意力矩阵出现谱间隙导致崩塌 | Naderi et al. (2025) |
| **Token Uniformity** | 不同 token 的隐状态表示趋向一致 | Dong et al. (2021) |
| **Attention Entropy Collapse** | 注意力分布变得极度尖锐（集中在极少数 token），熵趋近 0 | 多项研究 |
| **Representation Degeneration** | 嵌入空间中表示坍缩到低维锥形子空间（各向异性） | Gao et al. (2019), Ethayarajh (2019) |
| **Over-smoothing** | 类比 GNN，token 表示经多层后变得不可区分 | 多项研究 |
| **Curse of Depth** | Pre-LN 导致深层 block 退化为恒等映射，不贡献有效计算 | Sun et al. (2025) |

### 1.2 Rank Collapse 的数学描述

**纯注意力网络的双指数收敛** (Dong et al., 2021)：

对于不含 skip connection 和 MLP 的纯自注意力网络，设第 $l$ 层的输出为 $X^{(l)} \in \mathbb{R}^{n \times d}$，自注意力操作为：

$$X^{(l+1)} = \text{softmax}(X^{(l)} W_Q W_K^T (X^{(l)})^T) \cdot X^{(l)} W_V$$

Dong et al. 通过 **路径分解 (path decomposition)** 证明：
- 纯自注意力网络可分解为指数多条路径之和
- 每条路径以**双指数速率**退化为 rank-1 矩阵
- 因此整体输出 $X^{(L)}$ 以双指数速率收敛到 rank-1 矩阵（即所有行相同）

$$\text{rank}(X^{(L)}) \to 1 \quad \text{doubly exponentially with } L$$

**谱间隙导致的宽度维度 Rank Collapse** (Naderi et al., 2025)：

对于单层 softmax attention 矩阵 $A = \text{softmax}(QK^T / \sqrt{d})$，利用随机矩阵理论分析：
- $A$ 的谱中存在一个**离群特征值 (outlier eigenvalue)**，与其余特征值之间存在显著的**谱间隙 (spectral gap)**
- 随着 context length $n$ 增大，这个谱间隙导致注意力矩阵丧失区分不同 token 的能力
- 这种"宽度维度的 rank collapse"在单层内就会发生，并会加速深度维度的 rank collapse
- 同时加剧梯度消失/爆炸问题

**Token Uniformity 的奇异值刻画**：

设第 $l$ 层的隐状态矩阵为 $H^{(l)} \in \mathbb{R}^{n \times d}$，对其做 SVD：$H^{(l)} = U \Sigma V^T$。Token uniformity 表现为：
- 奇异值分布极度偏斜：$\sigma_1 \gg \sigma_2 \gg \cdots$（少数维度主导）
- token 间的余弦相似度趋近 1
- 表示的有效秩 (effective rank) 远小于 $\min(n, d)$

### 1.3 Attention Entropy Collapse

与 rank collapse / token uniformity 对偶的现象：

- Rank collapse：注意力趋向**均匀分布**（每个 token 获得相等权重），熵最大
- Entropy collapse：注意力趋向**尖锐分布**（集中在少数 token），熵趋近 0

两者都导致信息传递退化，但机制不同：
- 均匀化：softmax 的输入（logits）趋近相同 → 权重趋近 $1/n$
- 尖锐化：logits 的谱范数过大 → 指数放大后主导一个 token

---

## 2. 根本原因分析

### 2.1 Softmax 的固有性质

Softmax 函数将注意力分数映射为概率分布（权重和为 1），这意味着注意力本质上是一种**加权平均**操作。重复应用加权平均天然具有平滑效应：
- 从动力系统角度，softmax attention 等价于**完全图上的退化扩散过程**
- 收敛速率为 $O(1/L)$（$L$ 为层数），最终收敛到 token 特征超球面上的 Dirac 测度
- softmax 的归一化约束（权重和为 1）使其无法实现"不混合"（即恒等映射）

### 2.2 Pre-Layer Normalization (Pre-LN) 的作用

**Curse of Depth (Sun et al., 2025)** 揭示了 Pre-LN 是深层退化的关键诱因：

- Pre-LN 的公式：$x_{l+1} = x_l + \text{Block}(\text{LN}(x_l))$
- 随着层数增加，残差流 $x_l$ 的方差**指数增长**
- LN 的归一化操作将日益增大的 $x_l$ 压缩回固定范围
- 这导致 $\text{Block}(\text{LN}(x_l))$ 的贡献相对于 $x_l$ 越来越小
- 最终，每层的 Jacobian 趋近**恒等矩阵**：$\frac{\partial x_{l+1}}{\partial x_l} \approx I$

实验验证：Llama, Mistral, DeepSeek, Qwen 等主流 LLM 的深层可以被大量剪枝而几乎不影响性能。

### 2.3 残差流的累积效应

Transformer 的残差流结构 $x_{l+1} = x_l + f_l(x_l)$ 意味着：
- 每层的贡献 $f_l(x_l)$ 被累加到残差流中
- 如果 $f_l$ 的幅度相对于 $x_l$ 很小（如 Pre-LN 下的深层），该层几乎不改变表示
- 不同 token 的差异主要来自浅层，深层的区分贡献递减

### 2.4 训练目标的影响

- 最大似然估计 (MLE) 配合 weight tying（输入嵌入与输出 softmax 层共享权重）时，优化过程会将大部分低频 token 的嵌入推向共同方向
- 这导致嵌入空间的各向异性 (anisotropy)，表现为表示在高维空间中占据一个狭窄的锥形区域

### 2.5 初始化阶段的退化

Noci et al. (2022) 发现 rank collapse 并非仅在训练后出现，**在初始化时就已存在**：
- 堆叠多层注意力层在初始化时就会导致 token 表示趋向相关
- 这导致 query 和 key 的梯度在初始化时就已消失
- 暗示问题具有**架构层面的结构性根源**，而非仅仅是训练动态的结果

---

## 3. 与 Attention Sink 的关系

### 3.1 Attention Sink 现象

Attention Sink 指在自回归 LLM 中，序列的第一个 token（通常是 `<BOS>` 或 `<s>`）在许多层和 head 中吸收了不成比例的大量注意力权重，即使该 token 在语义上并不重要。

### 3.2 Attention Sink 是 Rank Collapse 的对抗机制

两者之间存在深层联系：**Attention Sink 是模型学习到的一种防御 rank collapse 的机制**。

1. **问题**：softmax 强制注意力权重和为 1，如果模型没有"丢弃"注意力的方式，所有注意力都会被迫分配给语义 token，导致过度混合 (over-mixing)，加剧 rank collapse
2. **解决**：模型学会将"多余"的注意力权重倾倒到 sink token 上，本质上执行一种 **no-op（空操作）**或**近似恒等映射**
3. **效果**：通过将大量权重分配给 sink token，剩余 token 之间的有效混合被减弱，从而**保护了 token 表示的多样性**

### 3.3 实验证据

- 如果在 sliding window 推理中移除 sink token，softmax 被迫将权重重新分配给其他 token → 模型立即崩溃（流畅度急剧下降）
- 这表明 sink token 是模型维持内部表示多样性的**关键锚点**

### 3.4 同一枚硬币的两面？

| 视角 | Rank Collapse | Attention Sink |
|------|--------------|----------------|
| 性质 | 病理现象（退化） | 适应性机制（补偿） |
| 方向 | 注意力过度分散/均匀 → 信息混合 | 注意力过度集中在无意义 token → 减少混合 |
| 关系 | 根本问题 | 模型自发学到的局部解决方案 |
| 局限 | --- | 浪费了注意力容量；依赖特定 token 的存在 |

可以说，Attention Sink 是模型在 softmax 约束下对 rank collapse 的一种**自发的次优应对**。更好的架构设计（如 Differential Attention）可以从根本上解决这个问题，而不需要依赖 sink token。

---

## 4. 理论分析（按时间线）

### 4.1 早期发现：Over-smoothing in GNNs（~2018-2020）

**背景**：Transformer 的 self-attention 可以视为**完全图上的消息传递**，与 GNN 共享关键数学结构。

- GNN 中的 over-smoothing：重复的邻域聚合使节点表示收敛到公共向量
- 将 Transformer 视为完全图上的 GNN，token 为节点，attention 权重为边权
- 两者共有的问题：迭代聚合导致指数级表达能力损失

**启示**：GNN 领域的去平滑技术（edge dropping、正则化、架构修改）为 Transformer 设计提供了思路。

### 4.2 Gao et al. (2019): Representation Degeneration Problem

- 发现语言模型的词嵌入空间呈各向异性 (anisotropic)
- token 嵌入集中在高维空间的一个狭窄锥形区域
- MLE + weight tying 是关键诱因
- 提出了 cosine regularization 等缓解方法

### 4.3 Dong, Cordonnier & Loukas (2021): 纯注意力的双指数 Rank Collapse

**论文**: "Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth" (ICML 2021)

**核心贡献**：
- **定理**：纯自注意力网络（无 skip connection、无 MLP）的输出以双指数速率收敛到 rank-1 矩阵
- **路径分解方法**：将深层注意力网络分解为指数多条路径之和，每条路径独立退化
- **关键结论**：Skip connection 和 MLP 不是"锦上添花"，而是**防止 rank collapse 的必要组件**

**数学要点**：
- 路径数随深度指数增长：$\sim 2^L$
- 每条路径以双指数速率退化为 rank-1
- 整体仍以双指数速率收敛（因为退化速率远快于路径数增长速率）

### 4.4 Wang et al. (2022): DeepNet / DeepNorm

**论文**: "DeepNet: Scaling Transformers to 1,000 Layers" (2022)

**核心贡献**：
- 分析了深层 Transformer 的训练不稳定性：LN 与大模型更新的交互导致浅层接收递减的更新
- 提出 **DeepNorm**：$\text{Output} = \text{LayerNorm}(\alpha \cdot x + \text{Sublayer}(x))$
  - $\alpha$ 用于缩放残差连接
  - 配合残差分支权重的 $\beta$ 缩放初始化
- 成功将 Transformer 扩展到 **1000 层**
- 理论保证：模型更新在深度上有界

### 4.5 Noci et al. (2022): 信号传播与 Rank Collapse

**论文**: "Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse" (NeurIPS 2022)

**核心贡献**：
- 发现 rank collapse **在初始化时就已存在**，不是训练的结果
- 分析了初始化时 token 表示的相关性如何随深度增长
- 揭示了 query/key 梯度在初始化时消失的原因
- 提出**深度相关的残差分支缩放**策略

### 4.6 Noci et al. (2023): Shaped Transformer

**论文**: "The Shaped Transformer: Attention Models in the Infinite Depth-and-Width Limit" (NeurIPS 2023)

**核心贡献**：
- 在 depth 和 width 同时趋向无穷的**比例极限 (proportional limit)** 下分析 Transformer
- 提出 **Shaped Attention** 修改，包含三个关键变化：
  1. **中心化 (Centering)**：使 softmax 注意力成为恒等矩阵的扰动
  2. **缩放 (Scaling)**：用宽度相关的温度参数 $\tau$ 缩放 softmax logits
  3. **恒等加法 (Identity Addition)**：显式地向注意力矩阵加恒等矩阵
- 推导了**神经协方差随机微分方程 (Neural Covariance SDE)**，刻画 Shaped Transformer 在大深度-宽度极限下的分布
- 为超参数选择提供了理论指导

### 4.7 Sun et al. (2025): Curse of Depth

**论文**: "The Curse of Depth in Large Language Models" (2025)

**核心贡献**：
- **实验观察**：Llama, Mistral, DeepSeek, Qwen 等主流 LLM 的大量顶层可以被剪枝而几乎不影响性能
- **根因分析**：Pre-LN 导致 Transformer block 的输出方差随深度指数增长
  - $\text{Var}(x_l) \propto \exp(\alpha \cdot l)$
  - 导致 layer-wise Jacobian 趋近恒等矩阵
  - 深层 block 退化为恒等函数
- **解决方案：LayerNorm Scaling (LNS)**
  - 将 LN 的输出按 $1/\sqrt{l}$ 缩放（$l$ 为层深度）
  - 控制方差的指数增长
  - 稳定梯度流
  - 在 130M 到 7B 参数规模下均有效

### 4.8 Naderi, Nait Saada & Tanner (2025): 谱分析

**论文**: "Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers" (ICLR 2025 / ICML 2025)

**核心贡献**：
- 首次发现**宽度维度的 rank collapse**：在单层 attention 中随 context length 增加而发生
- 用随机矩阵理论分析 softmax attention 矩阵的谱：发现离群特征值与谱间隙
- 提出通过**移除谱中的离群特征值**来缓解
- 为 Differential Transformer 提供了**理论解释**：两个 softmax 相减本质上是在消除谱中的离群值

### 4.9 Chen et al. (2025): Critical Attention Scaling

**核心贡献**：
- 为长 context 下的注意力缩放提供严格理论基础
- 发现 attention scaling 存在**相变 (phase transition)**：
  - 缩放因子 $\beta_n$ 太小 → 收缩坍缩（token 过度聚集）
  - $\beta_n$ 太大 → attention 退化为恒等算子
- **临界缩放阈值**：$\beta_n \asymp \log n$
- 为 YaRN、Qwen 等模型中使用的对数缩放提供了数学解释

---

## 5. 解决/缓解方法

### 5.1 架构级解决方案

#### 5.1.1 Differential Attention (Ye et al., 2024)

**论文**: "Differential Transformer" (Microsoft Research & Tsinghua, 2024.10)

**机制**：
- 将 Q, K 向量分为两组
- 计算两个独立的 softmax attention map
- 最终注意力 = 两者之差：$A_{\text{diff}} = \text{softmax}(Q_1 K_1^T) - \text{softmax}(Q_2 K_2^T)$

**与 rank collapse 的关系**：
- 两个 softmax 相减的效果等同于**消除注意力矩阵谱中的离群特征值**（Naderi et al. 2025 的理论解释）
- 产生更稀疏、更聚焦的注意力模式
- 减少 attention noise，缓解对 attention sink 的依赖

**效果**：提升长上下文建模、减少幻觉、增强量化友好性

#### 5.1.2 nGPT: 超球面约束 (Loshchilov et al., 2024)

**论文**: "nGPT: Normalized Transformer with Representation Learning on the Hypersphere" (NVIDIA, 2024.10)

**机制**：
- 将所有内部表示（嵌入、MLP、attention、隐状态）约束到**单位超球面**上
- 前向传播变为超球面上的一系列位移
- 消除传统的归一化层

**与 rank collapse 的关系**：
- 超球面约束创建了更各向同性 (isotropic) 的嵌入空间
- 从根本上避免了表示坍缩到锥形子空间
- 保证了表示多样性

**效果**：4-20x 更快的训练收敛

#### 5.1.3 Mix-LN (2025)

**机制**：
- 在同一模型中动态组合 Post-LN 和 Pre-LN
- 浅层用 Post-LN（维持深层梯度范数），深层用 Pre-LN（保持稳定性）
- 目标：在所有层上实现更均匀的梯度范数分布

**与 rank collapse 的关系**：
- 直接解决 Pre-LN 导致的深层退化（Curse of Depth）
- 允许深层也能有效贡献学习

#### 5.1.4 Peri-LN (2025)

**机制**：
- 在每个子层的前后**都**放置 LayerNorm：$\text{LN} \to \text{Sublayer} \to \text{LN} \to \text{Residual}$
- 已被 Gemma 2/3、OLMo 2 等模型采用

**效果**：
- 更平衡的方差增长
- 更稳定的梯度流
- 在 ICML 2025 展示了相比 Pre-LN 和 Post-LN 的优势

#### 5.1.5 Shaped Attention (Noci et al., 2023)

**机制**（见 4.6 节）：
- 中心化 + 缩放 + 恒等加法
- 使注意力矩阵成为恒等矩阵的小扰动，而非可能退化的 doubly-stochastic 矩阵

#### 5.1.6 DeepNorm (Wang et al., 2022)

**机制**（见 4.4 节）：
- 缩放残差连接：$\text{LN}(\alpha x + f(x))$
- 缩放初始化：残差分支权重乘以 $\beta$
- 支持 1000 层 Transformer

### 5.2 训练技术

#### 5.2.1 LayerNorm Scaling (LNS) (Sun et al., 2025)

- 将 LN 输出按 $1/\sqrt{l}$ 缩放
- 简单、无需额外参数
- 在多种模型规模下有效

#### 5.2.2 注意力温度调整

- **熵引导温度**：根据 attention entropy 动态调整 softmax 温度，防止过度尖锐或过度均匀
- **对数缩放**：$\beta_n \asymp \log n$，用于长 context 下维持注意力质量
- **sigmaReparam**：用谱归一化和可学习标量约束线性层的谱范数，防止 entropy collapse

#### 5.2.3 正则化方法

- **余弦正则化 (CosReg)**：惩罚 token 嵌入之间的高余弦相似度
- **NeuTRENO (NeurIPS 2023)**：惩罚注意力平滑输出与原始输入之间的差异，保持 token 的局部信息
- **对比损失**：添加对比学习目标，显式维护表示的多样性

### 5.3 模型压缩与剪枝

#### 5.3.1 ShortGPT (2024)

**论文**: "ShortGPT: Layers in Large Language Models are More Redundant Than You Expect"

**核心方法**：
- 定义 **Block Influence (BI)** 指标：量化每层对隐状态的改变程度
- 直接移除 BI 最低的层（无需重训练）
- 移除 ~25% 的层后仍保持 ~90% 的原始性能
- 可与量化等其他压缩方法正交组合

**意义**：
- 实证验证了深层冗余的普遍性（不仅限于 Transformer，在 Mamba 中也存在）
- 冗余主要集中在中间和深层

#### 5.3.2 Attention Head 剪枝

- 研究表明 40%-75% 的 attention head 可被剪除而无显著性能损失
- 早期和中间层包含更多冗余 head
- 最后几层的 head 最为关键
- 方法：梯度归因、Shapley 值、KL 散度度量、动态 gating

### 5.4 ViT 领域的特定方法

#### 5.4.1 Registers (Darcet et al., 2024)

- 在 ViT 中添加可学习的 **register token**（不对应图像 patch）
- 吸收全局语义信息，防止信息在标准 token 中扩散
- 消除高范数 token 的 artifact

#### 5.4.2 Token Merging (ToMe, ICLR 2023)

- 有意合并相似 token 以提升效率
- 与无意的 over-smoothing 不同，这是有控制的冗余消除
- 可视为利用 token uniformity 现象的实用手段

---

## 6. 对架构设计的启示

### 6.1 LayerNorm 的位置至关重要

| 方案 | 优势 | 劣势 | 与 rank collapse 的关系 |
|------|------|------|------------------------|
| **Pre-LN** | 训练稳定 | 深层退化 (Curse of Depth) | 直接导致深层贡献递减 |
| **Post-LN** | 深层梯度更强 | 浅层梯度消失 | 更好地保持深层有效性 |
| **Mix-LN** | 两者兼顾 | 实现复杂 | 缓解 Curse of Depth |
| **Peri-LN** | 平衡方差与梯度 | 计算量略增 | 最佳平衡方案之一 |

### 6.2 Skip Connection 和 MLP 是必需的

Dong et al. (2021) 的理论明确表明：
- 没有 skip connection → 双指数 rank collapse
- 没有 MLP → 仅有线性混合，无法恢复表示多样性
- 两者共同作用才能维持网络的表达能力

### 6.3 Attention 机制需要谱控制

- 标准 softmax attention 的谱间隙是结构性问题
- Differential Attention 通过消除离群特征值解决此问题
- 对数缩放 $\beta_n \asymp \log n$ 在长 context 下是必要的

### 6.4 表示空间的几何约束

- nGPT 的超球面约束展示了几何约束的力量
- 约束表示到良定义的流形上可以从根本上避免各向异性退化
- 但可能带来量化敏感性等新问题

### 6.5 深度 vs. 宽度的权衡

- rank collapse 同时存在于深度维度和宽度维度
- 盲目增加深度可能带来递减回报（Curse of Depth）
- 长 context 应用需要特别注意宽度维度的 rank collapse
- 适当的缩放策略可以同时缓解两个维度的问题

---

## 7. 开放问题

### 7.1 理论层面

1. **完整架构的 rank collapse 理论**：Dong et al. (2021) 分析的是纯注意力网络。对于包含 skip connection、MLP、LayerNorm 的完整 Transformer，rank collapse 的精确速率和条件是什么？虽然 Noci et al. 的工作有所推进，但完整的理论仍未建立。

2. **训练动态与 rank collapse 的交互**：rank collapse 在初始化时就存在，但训练过程如何影响其演化？模型是学会了对抗还是加剧了 collapse？

3. **与涌现能力的关系**：模型规模增大时 rank collapse 的行为如何变化？是否存在规模阈值使得 collapse 自然被缓解？

4. **因果注意力的特殊性**：大多数理论分析针对双向注意力。因果掩码 (causal mask) 如何影响 rank collapse 的动态？

### 7.2 方法层面

5. **统一的解决框架**：目前的解决方案（Diff Attention、nGPT、Mix-LN 等）各有侧重，是否存在一个统一的原则来指导架构设计以同时解决所有退化问题？

6. **Attention Sink 的可消除性**：如果 attention sink 是对 rank collapse 的补偿机制，那么完全消除 rank collapse 后，sink 现象是否会消失？Differential Attention 在这方面的实验结果如何？

7. **量化与 rank collapse**：nGPT 的超球面约束可能对量化更敏感。如何在缓解 rank collapse 和保持量化友好性之间取得平衡？

### 7.3 实践层面

8. **最优深度确定**：给定模型参数预算，如何确定最优的深度-宽度分配以最小化 rank collapse 的影响？

9. **动态深度**：是否可以根据输入的复杂度动态决定使用多少层（如早期退出），以避免不必要的深层退化？

10. **跨架构的泛化**：rank collapse 是否也影响非 attention 架构（如 SSM/Mamba）？ShortGPT 在 Mamba 上的初步结果表明冗余层是普遍现象，但理论理解仍然缺乏。

### 7.4 2024-2026 年研究前沿

11. **MoE 与 rank collapse**：Mixture-of-Experts 架构中，不同专家是否有助于维护表示多样性？还是每个专家内部仍然存在 collapse？

12. **超长 context 的新挑战**：随着 context window 扩展到百万级 token，宽度维度的 rank collapse 变得更加严峻。$\log n$ 缩放是否足够，还是需要更激进的架构改变？

13. **Layer-Integrated Memory (LIMe)**：允许 attention 访问所有前序层的表示（而非仅前一层），是否能根本性地缓解深度方向的退化？

---

## 参考文献

### 核心理论论文

- Dong, Y., Cordonnier, J.-B., & Loukas, A. (2021). "Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth." ICML 2021.
- Noci, L., et al. (2022). "Signal Propagation in Transformers: Theoretical Perspectives and the Role of Rank Collapse." NeurIPS 2022.
- Noci, L., et al. (2023). "The Shaped Transformer: Attention Models in the Infinite Depth-and-Width Limit." NeurIPS 2023.
- Naderi, A., Nait Saada, T., & Tanner, J. (2025). "Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers." ICLR 2025 / ICML 2025.
- Sun, Y., et al. (2025). "The Curse of Depth in Large Language Models." 2025.
- Chen, Y., et al. (2025). "Critical Attention Scaling." 2025.

### 解决方案论文

- Ye, L., et al. (2024). "Differential Transformer." Microsoft Research & Tsinghua University, 2024.
- Loshchilov, I., et al. (2024). "nGPT: Normalized Transformer with Representation Learning on the Hypersphere." NVIDIA, 2024.
- Wang, H., et al. (2022). "DeepNet: Scaling Transformers to 1,000 Layers." Microsoft Research, 2022.
- Men, X., et al. (2024). "ShortGPT: Layers in Large Language Models are More Redundant Than You Expect." 2024.

### 相关现象论文

- Gao, J., et al. (2019). "Representation Degeneration Problem in Training Natural Language Generation Models." ICLR 2019.
- Xiao, G., et al. (2023). "Efficient Streaming Language Models with Attention Sinks." 2023.
- Darcet, T., et al. (2024). "Vision Transformers Need Registers." ICLR 2024.
