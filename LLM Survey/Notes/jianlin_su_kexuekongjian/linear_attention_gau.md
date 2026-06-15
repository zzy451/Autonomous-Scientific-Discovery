# 苏剑林 线性 Attention 与 GAU 系列文章深度摘要

> 来源：科学空间 (kexue.fm / spaces.ac.cn) 苏剑林(Jianlin Su)系列博客文章
> 主要文章：
> - 从 Performer 到线性 Attention (kexue.fm/archives/8338)
> - 线性 Attention 的探索系列 (kexue.fm/archives/8765 等)
> - GAU 与 FLASH 相关分析 (kexue.fm/archives/9052 等)
> - 线性注意力简史：从模仿、创新到反哺 (kexue.fm, 2025-06-20)
> - 英文翻译参考：tylerromero.com/translations/scientific-spaces/a-brief-history-of-linear-attention/

---

## 1. 从 Performer 到线性 Attention

### 核心分析

苏剑林从标准 Softmax Attention 出发，系统分析了线性 Attention 的本质。

**标准 Softmax Attention 的形式：**

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d}}\right) V$$

对于第 $i$ 个 token，输出为：

$$o_i = \frac{\sum_{j=1}^{n} e^{q_i \cdot k_j} v_j}{\sum_{j=1}^{n} e^{q_i \cdot k_j}}$$

其中 $q_i, k_j \in \mathbb{R}^d$，$v_j \in \mathbb{R}^{d_v}$。

**核心观察：** Softmax Attention 本质上是一个以 $e^{q \cdot k}$ 为核函数的加权平均。苏剑林指出，如果我们将 $e^{q_i \cdot k_j}$ 视为某个核函数 $K(q_i, k_j)$，那么 Attention 就是一个核平滑(kernel smoothing)操作。

### Performer 的核方法逼近思路

Performer (Choromanski et al., 2020) 的核心思想是用随机特征(random features)来逼近 softmax 核：

$$e^{q \cdot k} \approx \phi(q)^\top \phi(k)$$

其中 $\phi: \mathbb{R}^d \to \mathbb{R}^D$ 是一个随机特征映射。Performer 使用 FAVOR+ (Fast Attention Via positive Orthogonal Random features) 方法：

$$\phi(x) = \frac{e^{-\|x\|^2/2}}{\sqrt{D}} \left[e^{w_1 \cdot x}, e^{w_2 \cdot x}, \ldots, e^{w_D \cdot x}\right]$$

其中 $w_1, \ldots, w_D$ 是从标准正态分布中采样的随机向量（正交化以降低方差）。

**苏剑林的关键分析：**

1. **结合律技巧**：一旦有了 $\phi(q)^\top \phi(k)$ 的分解，就可以利用矩阵乘法结合律：

$$o_i = \frac{\phi(q_i)^\top \sum_{j} \phi(k_j) v_j^\top}{\phi(q_i)^\top \sum_{j} \phi(k_j)}$$

先计算 $\sum_{j} \phi(k_j) v_j^\top$（$D \times d_v$ 矩阵），再与 $\phi(q_i)$ 相乘，复杂度从 $O(n^2 d)$ 降为 $O(n D d_v)$，即线性复杂度。

2. **逼近质量问题**：苏剑林指出 Performer 的随机特征逼近在实践中效果不佳，需要很大的 $D$ 才能获得合理的逼近精度，这削弱了效率优势。

### 线性 Attention 的一般形式与局限性分析

苏剑林将线性 Attention 的一般形式总结为：

$$o_i = \frac{\sum_{j=1}^{n} \phi(q_i)^\top \phi(k_j) \cdot v_j}{\sum_{j=1}^{n} \phi(q_i)^\top \phi(k_j)}$$

其中 $\phi$ 是某个非负的特征映射函数。常见选择包括：
- **Performer**: $\phi(x) = \text{elu}(x) + 1$ 或随机特征映射
- **Linear Transformer** (Katharopoulos et al., 2020): $\phi(x) = \text{elu}(x) + 1$
- **RFA** (Random Feature Attention): 类似 Performer 的随机特征

**苏剑林指出的核心局限性：**

1. **注意力矩阵的低秩退化**：线性 Attention 的注意力矩阵 $A_{ij} = \phi(q_i)^\top \phi(k_j)$ 的秩最多为 $D$（特征维度），而 Softmax Attention 的注意力矩阵理论上可以是满秩的。这意味着线性 Attention 的表达能力本质上受限。

2. **缺乏"锐利"的注意力分布**：Softmax 的指数函数天然产生"赢者通吃"的效果——少数相关 token 获得大部分注意力权重。线性 Attention 的注意力分布更加平坦，难以实现精确的信息检索。

3. **归一化的困难**：线性 Attention 中分母 $\sum_j \phi(q_i)^\top \phi(k_j)$ 可能非常小甚至接近零，导致数值不稳定。这是一个实践中的严重问题。

4. **因果(causal)场景下的退化**：在自回归生成中，线性 Attention 可以写成递推形式：
   $$S_i = S_{i-1} + \phi(k_i) v_i^\top, \quad z_i = z_{i-1} + \phi(k_i)$$
   $$o_i = \frac{\phi(q_i)^\top S_i}{\phi(q_i)^\top z_i}$$
   
   这个递推状态 $S_i \in \mathbb{R}^{D \times d_v}$ 是一个固定大小的"压缩记忆"，其容量有限，随着序列增长会出现信息遗忘和混淆。

### 独到见解

- **"模仿 Softmax 是一条死路"**：苏剑林在后续文章中明确指出，试图用线性方法去逼近 Softmax 的行为（如 Performer 的思路）本质上是在用低秩去逼近高秩，效果必然有限。正确的方向应该是重新思考线性 Attention 本身应该具备什么性质。

- **线性 Attention 的本质是"快速权重"(Fast Weight)**：线性 Attention 的递推形式 $S_i = S_{i-1} + \phi(k_i) v_i^\top$ 本质上是在维护一个外积累加的"快速权重矩阵"，这与 90 年代 Schmidhuber 提出的 Fast Weight Programmers 有深刻联系。

- **BERT 时代思考线性 Attention 并不明智**：苏剑林在"线性注意力简史"中回顾说，2020 年社区主要在 BERT 的语境下讨论 Softmax Attention，训练长度短且主要是 Encoder 模型，线性 Attention 几乎没有实际优势。

### 对综述 Section 1 (Token Mixer) 的补充价值

- 提供了从核方法视角理解 Attention 的统一框架
- 明确了线性 Attention 的表达能力上界（低秩约束）
- 指出了"模仿 softmax"路线的根本缺陷
- 建立了线性 Attention 与 Fast Weight Programmers 的理论联系
- 为理解后续 Mamba/SSM 等替代架构提供了铺垫

---

## 2. GAU (Gated Attention Unit)

### 来源论文
Hua et al., "Transformer Quality in Linear Time" (2022), arXiv:2202.10447

### 核心设计思想

GAU 的核心创新是将 Attention 和 FFN 融合为一个统一的层，同时用门控机制弥补单头注意力的表达能力不足。

**标准 Transformer 的一层包含两个子层：**
1. Multi-Head Attention (MHA)
2. Feed-Forward Network (FFN)

**GAU 将两者融合为一个操作：**

$$O = (U \odot \hat{V}) W_O$$

其中：
- $U = \phi_u(X W_u)$，$V = \phi_v(X W_v)$：两个独立的线性变换 + 激活
- $\hat{V} = A V$：$A$ 是注意力矩阵，$V$ 经过注意力加权
- $\odot$：逐元素乘法（门控机制）
- $W_O$：输出投影

**注意力矩阵的计算（简化版）：**

$$A = \frac{1}{n} \text{relu}^2\left(\frac{Q K^\top}{\sqrt{s}}\right)$$

或使用 softmax：

$$A = \text{softmax}\left(\frac{Q K^\top}{\sqrt{s}}\right)$$

其中 $Q = Z W_Q$, $K = Z W_K$, $Z = \phi_z(X W_z)$，且 $Q, K$ 的维度 $s$ 远小于 $d$（如 $s = 128$）。

### 苏剑林的关键分析

**1. GAU 本质上是"门控 + 弱注意力"的组合**

苏剑林指出 GAU 的设计哲学是：
- 用**门控机制**（$U \odot \hat{V}$）来提供类似 FFN 的非线性变换能力
- 用**单头弱注意力**来提供 token 间的信息交互
- 门控的存在使得即使注意力较弱（单头、低维），整体表达能力也足够

这与标准 Transformer 的"强注意力 + 简单 FFN"形成对比：GAU 选择了"弱注意力 + 强门控"的路线。

**2. 与 GLU (Gated Linear Unit) 的关系**

GAU 可以看作是 GLU 的注意力增强版本。标准 GLU：
$$\text{GLU}(X) = (X W_1) \odot \sigma(X W_2)$$

GAU 将其中一个分支替换为经过注意力加权的版本：
$$\text{GAU}(X) = U \odot (A \cdot V)$$

这样既保留了 GLU 的门控优势，又引入了序列内的信息交互。

**3. 单头注意力为何可行**

苏剑林分析了为什么 GAU 可以只用单头注意力而不显著损失质量：
- 门控机制本身提供了"多视角"的能力——$U$ 的不同维度可以选择性地保留或抑制 $\hat{V}$ 的不同维度
- 这在功能上类似于多头注意力中不同头关注不同方面的效果
- 但计算成本远低于多头注意力

### 关键公式

**GAU 完整前向传播：**
```
Z = φ(X W_z)           # 共享的中间表示
Q = Z W_Q, K = Z W_K   # 低维 query/key (dim = s << d)
U = SiLU(X W_u)         # 门控分支
V = SiLU(X W_v)         # 值分支
A = softmax(QK^T / √s)  # 单头注意力 (或 relu^2 归一化)
O = (U ⊙ AV) W_O        # 门控输出
```

### FLASH: GAU 的线性化

FLASH (Fast Linear Attention with a Single Head) 是 GAU 的线性复杂度版本：

1. 将序列分成长度为 $c$ 的 chunk
2. chunk 内使用完整的 quadratic attention
3. chunk 间使用线性 attention 近似

$$O_{\text{chunk}} = \text{GAU}_{\text{local}}(X_{\text{chunk}}) + \text{LinearAttn}_{\text{global}}(X)$$

这种混合策略在保持质量的同时实现了近似线性的复杂度。

### 独到见解

- **Attention 和 FFN 的边界是人为的**：GAU 表明这两个组件可以自然融合，暗示标准 Transformer 的双子层设计可能不是最优的。
- **门控是比多头更高效的"多样性"来源**：多头注意力通过多个独立的注意力头来捕获不同模式，而门控通过逐元素的乘法实现类似效果，参数效率更高。
- **弱注意力 + 强门控 ≈ 强注意力 + 弱 FFN**：这个等价关系暗示了 Transformer 设计空间中的一个重要对称性。

### 对综述 Section 1 (Token Mixer) 的补充价值

- GAU 展示了 Token Mixer 和 Channel Mixer 融合的可能性
- 提供了一种减少 Attention 头数而不损失质量的方法论
- FLASH 的 chunk-wise 策略是局部-全局混合注意力的早期实践
- 为后续 GLA (Gated Linear Attention) 等工作奠定了基础

---

## 3. 线性 Attention 在实际模型中的表现

### 苏剑林的实验探索

苏剑林在多篇博客中记录了他在 BERT 级别模型上测试线性 Attention 的实验。

**实验设置：**
- 基础模型：BERT-base 规模 (12层, 768维, 12头)
- 任务：MLM 预训练 + 下游 NLU 任务微调
- 对比方案：标准 Softmax Attention vs 各种线性 Attention 变体

**测试的线性 Attention 变体：**

1. **ELU+1 映射**：$\phi(x) = \text{elu}(x) + 1$
   - 来自 Linear Transformer (Katharopoulos et al., 2020)
   - 效果：明显低于 Softmax，尤其在需要精确匹配的任务上

2. **ReLU 映射**：$\phi(x) = \text{relu}(x)$
   - 简单但有效的非负映射
   - 效果：略好于 ELU+1，但仍有差距

3. **1+cos 映射**：$\phi(x) = 1 + \cos(x)$（或类似的非负周期函数）
   - 效果：与 ReLU 类似

4. **Performer 的随机特征**
   - 效果：理论上最接近 Softmax，但实际效果不稳定

### 关键发现

1. **线性 Attention 在短序列上几乎没有优势**：BERT 的典型序列长度为 512，此时 Softmax Attention 的 $O(n^2)$ 复杂度并不是瓶颈，而线性 Attention 的质量损失却很明显。

2. **归一化至关重要**：不同的归一化策略对线性 Attention 的效果影响巨大。苏剑林发现简单的除以序列长度 $n$ 的归一化有时比精确的核归一化效果更好，因为后者容易出现数值问题。

3. **位置编码的交互**：线性 Attention 与位置编码的交互方式与 Softmax Attention 不同。RoPE (Rotary Position Embedding，苏剑林自己提出的) 在线性 Attention 中的效果不如在 Softmax Attention 中好，因为 RoPE 依赖于内积空间的性质。

4. **Encoder vs Decoder 的差异**：线性 Attention 在 Encoder（双向）中的质量损失比在 Decoder（因果/自回归）中更大，这与直觉相反——因为 Encoder 可以看到全部 token，信息压缩的压力更大。

### 独到见解

- **"在 BERT 时代思考线性 Attention 并不明智"**：苏剑林在回顾中坦承，当时的实验条件（短序列、Encoder 为主）不利于展示线性 Attention 的优势。线性 Attention 的真正价值在长序列自回归生成中才能体现。

- **线性 Attention 需要配套的架构设计**：不能简单地将 Softmax 替换为线性 Attention，需要同时调整归一化、位置编码、层数等超参数。

### 对综述的补充价值

- 提供了线性 Attention 在 NLU 任务上的第一手实验数据
- 揭示了线性 Attention 与位置编码（特别是 RoPE）的兼容性问题
- 指出了序列长度对线性 Attention 优势的决定性影响

---

## 4. Softmax 的本质分析

### 苏剑林对 Softmax 在 Attention 中作用的深度分析

**Softmax 的三个关键性质：**

1. **非负性**：$\text{softmax}(x)_i \geq 0$，确保注意力权重为非负
2. **归一化**：$\sum_i \text{softmax}(x)_i = 1$，确保注意力权重和为 1
3. **锐化/稀疏化**：指数函数放大差异，使大值更大、小值更小

苏剑林认为第 3 点是 Softmax 最关键的性质，也是线性 Attention 最难复制的。

### 关键公式与分析

**Softmax 的温度参数视角：**

$$\text{softmax}(x/\tau)_i = \frac{e^{x_i/\tau}}{\sum_j e^{x_j/\tau}}$$

- $\tau \to 0$：趋向 one-hot（硬注意力）
- $\tau \to \infty$：趋向均匀分布
- $\tau = 1/\sqrt{d}$：标准 scaled dot-product attention

苏剑林指出，$1/\sqrt{d}$ 的缩放因子本质上是在控制注意力分布的"温度"，使其既不太尖锐也不太平坦。

**Softmax 与核函数的联系：**

$$e^{q \cdot k} = e^{\|q\|^2/2} \cdot e^{\|k\|^2/2} \cdot e^{-\|q-k\|^2/2}$$

这表明 Softmax Attention 本质上是一个高斯核（RBF 核），其中：
- $e^{-\|q-k\|^2/2}$ 是标准高斯核，衡量 $q$ 和 $k$ 的相似度
- $e^{\|q\|^2/2}$ 和 $e^{\|k\|^2/2}$ 是与各自范数相关的缩放因子

**苏剑林的洞察：** 高斯核是一个无限维的核函数（其对应的特征空间是无限维的），这解释了为什么有限维的线性 Attention 难以完美逼近 Softmax——本质上是在用有限维去逼近无限维。

### Softmax 的替代方案分析

苏剑林讨论了多种 Softmax 替代方案：

1. **$\text{relu}^2$ 归一化**（用于 GAU）：
   $$A_{ij} = \frac{\text{relu}(q_i \cdot k_j)^2}{\sum_l \text{relu}(q_i \cdot k_l)^2}$$
   优点：计算简单，可线性化；缺点：稀疏性不如 Softmax

2. **Sigmoid Attention**：
   $$A_{ij} = \sigma(q_i \cdot k_j)$$
   不归一化，依赖门控或 LayerNorm 来稳定。后来在 FlashSigmoid 等工作中被重新发现。

3. **Squared Attention**：
   $$A_{ij} = (q_i \cdot k_j)^2$$
   可以分解为 $\phi(q)^\top \phi(k)$ 的形式（其中 $\phi$ 是二次特征映射），天然支持线性化。

### 独到见解

- **Softmax 的成功不仅仅是归一化**：很多线性 Attention 工作只关注保持归一化性质，但忽略了 Softmax 的锐化效果。苏剑林认为锐化（即注意力的稀疏性）才是 Softmax 成功的关键。

- **"注意力不需要是概率分布"**：苏剑林在后续工作中逐渐认识到，注意力权重不一定需要满足概率分布的性质（非负+归一化）。Sigmoid Attention 和无归一化的线性 Attention 在配合适当的架构设计后也能工作良好。

- **缩放因子 $1/\sqrt{d}$ 的深层含义**：不仅是为了控制梯度，更是为了让注意力分布处于"有意义"的温度区间——既能区分相关和不相关的 token，又不会过度集中在单个 token 上。

### 对综述的补充价值

- 从核函数视角统一理解 Softmax 和线性 Attention
- 明确了 Softmax 三个性质的相对重要性（锐化 > 归一化 > 非负性）
- 为评估各种 Attention 变体提供了理论框架

---

## 5. 线性注意力简史：从模仿、创新到反哺

### 三个阶段的演进

苏剑林在 2025 年的综述性文章中将线性 Attention 的发展分为三个阶段：

**阶段一：模仿 (Imitation, 2020-2021)**

目标是用线性方法逼近 Softmax Attention 的行为。

代表工作：
- **Performer** (Choromanski et al., 2020): FAVOR+ 随机特征
- **Linear Transformer** (Katharopoulos et al., 2020): ELU+1 特征映射
- **RFA** (Peng et al., 2021): Random Feature Attention
- **cosFormer** (Qin et al., 2022): 余弦重加权

苏剑林的评价：这个阶段的工作普遍效果不佳，因为"用低秩去逼近高秩"本身就是一个注定失败的策略。

**阶段二：创新 (Innovation, 2022-2024)**

放弃模仿 Softmax，转而探索线性 Attention 自身的设计空间。

代表工作：
- **GAU/FLASH** (Hua et al., 2022): 门控 + 单头注意力
- **RetNet** (Sun et al., 2023): 将线性 Attention 与递推/并行双模式结合
- **Mamba/S4** (Gu et al., 2023): 状态空间模型，线性 Attention 的连续化
- **GLA** (Yang et al., 2024): Gated Linear Attention，GAU 思想的延续
- **HGRN** (Qin et al., 2024): 层次化门控递推网络
- **Mamba-2** (Dao & Gu, 2024): 揭示 SSM 与线性 Attention 的等价性

苏剑林的评价：这个阶段的关键突破是认识到线性 Attention 不应该模仿 Softmax，而应该发展自己的优势——高效的递推推理和与门控机制的自然结合。

**阶段三：反哺 (Feeding Back, 2024-2025)**

线性 Attention 的设计思想反过来影响了 Softmax Attention 的改进。

代表现象：
- **混合架构 (Hybrid)**：Jamba, Zamba 等模型混合使用 Softmax Attention 层和线性 Attention/SSM 层
- **门控思想的回流**：GQA (Grouped Query Attention) 等可以看作是 GAU 门控思想在多头注意力中的体现
- **递推视角的启发**：线性 Attention 的递推形式启发了对 Softmax Attention 的 KV Cache 压缩研究
- **Attention Residuals** (Kimi/Moonshot, 2026): 苏剑林参与的工作，用注意力机制替代标准残差连接

苏剑林的评价：线性 Attention 最大的贡献可能不是替代 Softmax Attention，而是为整个 Attention 设计空间提供了新的视角和工具。

### 核心论点总结

1. **线性 Attention 的价值不在于"线性"本身**：真正的价值在于它迫使研究者重新思考 Attention 的本质——什么是必要的，什么是可以简化的。

2. **门控是关键的补偿机制**：从 GAU 到 GLA 到 Mamba，成功的线性 Attention 变体几乎都引入了某种形式的门控。门控提供了 Softmax 所提供的"选择性"，但以一种更灵活的方式。

3. **混合架构可能是最终答案**：纯线性 Attention 模型在质量上仍然难以匹敌纯 Softmax Attention 模型，但混合架构可以兼得两者的优势。

4. **训练长度是决定性因素**：线性 Attention 的优势只在长序列（数千到数万 token）时才显现。随着 LLM 训练长度从 512 增长到 128K+，线性 Attention 的实际价值才真正体现。

### 对综述的整体补充价值

- 提供了线性 Attention 发展的完整历史脉络
- 从实践者视角评估了各种方法的优劣
- 揭示了线性 Attention 与 SSM 的深层联系
- 指出了混合架构作为实用方案的趋势
- 强调了门控机制在现代高效 Attention 设计中的核心地位

---

## 6. 补充：苏剑林的其他相关贡献

### RoPE (Rotary Position Embedding)

苏剑林是 RoPE 的提出者，这与线性 Attention 有重要交叉：
- RoPE 通过旋转矩阵编码相对位置：$f(q, m) = R_m q$, $f(k, n) = R_n k$
- 使得 $\langle f(q,m), f(k,n) \rangle = \langle R_{m-n} q, k \rangle$，只依赖相对位置 $m-n$
- RoPE 在 Softmax Attention 中效果极好（被 LLaMA, GPT-NeoX 等广泛采用）
- 但在线性 Attention 中效果受限，因为线性 Attention 的特征映射 $\phi$ 与旋转操作不兼容

### 对 Attention 机制的哲学思考

苏剑林在多篇文章中表达了对 Attention 机制的深层思考：
- Attention 本质上是一种"软检索"机制
- Softmax 的成功在于它实现了一种"竞争性"的信息选择
- 线性 Attention 的递推形式揭示了 Attention 与记忆系统的联系
- 未来的方向可能是"可学习的信息压缩"，而非固定的注意力模式

---

## 附：关键术语对照

| 中文 | 英文 | 说明 |
|------|------|------|
| 线性注意力 | Linear Attention | 复杂度为 O(n) 的注意力机制 |
| 核方法 | Kernel Method | 通过核函数隐式映射到高维空间 |
| 随机特征 | Random Features | 用随机映射近似核函数 |
| 门控注意力单元 | Gated Attention Unit (GAU) | 融合 Attention 和 FFN 的层 |
| 快速权重 | Fast Weights | 通过外积累加维护的动态权重矩阵 |
| 状态空间模型 | State Space Model (SSM) | 线性 Attention 的连续化形式 |
| 旋转位置编码 | Rotary Position Embedding (RoPE) | 苏剑林提出的位置编码方法 |
| 注意力残差 | Attention Residuals | 用注意力替代标准残差连接 |
