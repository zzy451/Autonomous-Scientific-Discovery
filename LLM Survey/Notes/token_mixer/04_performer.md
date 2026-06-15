# Rethinking Attention with Performers
**作者**: Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, David Belanger, Lucy Colwell, Adrian Weller | **年份**: 2020 | **arxiv**: 2009.14794

## 0. 摘要翻译
本文提出FAVOR+（Fast Attention Via positive Orthogonal Random features），一种通过随机特征分解实现注意力机制线性化的方法。Performer使用FAVOR+机制，能够提供注意力矩阵的可证明近似——包括softmax核以及更广义的核——同时保持线性时间和空间复杂度。此外，该方法是第一个能够有效近似softmax注意力的线性化方法，保证了无偏估计和低方差。Performer可以直接替代标准Transformer中的注意力模块。

## 1. 方法动机
a) **为什么提出**: 之前的线性注意力方法（如使用$\text{elu}(x)+1$作为特征映射）无法准确近似softmax注意力，导致质量下降。
b) **现有痛点**: (1) 标准softmax注意力的$O(L^2)$复杂度；(2) 已有的核方法近似不够准确，特别是对softmax核的近似；(3) 随机特征方法可能产生负值，导致注意力权重为负（物理上无意义）。
c) **研究假设**: 通过精心设计的正交随机特征映射（positive random features），可以高效、无偏地近似softmax核，实现线性复杂度的注意力。

## 2. 方法设计
a) **Pipeline**: 将softmax注意力中的核$K(x,y) = \exp(x^Ty)$用随机特征映射分解，将矩阵乘法顺序从$(QK^T)V$改为$Q(K^TV)$。

b) **模块功能**:
- **随机特征映射$\phi$**: $\phi(x) = \frac{\exp(-\|x\|^2/2)}{\sqrt{m}}[\exp(w_1^Tx), ..., \exp(w_m^Tx)]$，其中$w_i$是从正交随机矩阵中采样的向量。使用正随机特征（Positive Random Features, PRF）保证特征值为正。
- **FAVOR+**: 使用正交随机特征（Orthogonal Random Features）降低方差。具体地，随机向量$w_1, ..., w_m$通过正交化处理。
- **线性注意力计算**: $\text{Attn}(Q,K,V) \approx \hat{D}^{-1}(\phi(Q)(\phi(K)^TV))$，其中$\hat{D} = \text{diag}(\phi(Q)\phi(K)^T\mathbf{1}_L)$用于归一化。

c) **公式解释**:
- 关键变换: $\text{softmax}(QK^T) \approx \hat{D}^{-1}\phi(Q)\phi(K)^T$
- 计算顺序改变: 先计算$\phi(K)^TV$得到$m \times d$矩阵（$m$是随机特征数），再乘以$\phi(Q)$。总复杂度$O(Lmd)$，线性于$L$。
- 因果注意力: 通过前缀和（prefix sum）维护累积$\phi(K)^TV$，支持自回归。

## 3. 与其他方法对比
| 方面 | Performer | Linear Attention (Katharopoulos) | Linformer | Transformer |
|------|-----------|--------------------------------|-----------|-------------|
| 复杂度 | $O(Lmd)$ | $O(Ld^2)$ | $O(Lkd)$ | $O(L^2d)$ |
| 核近似 | softmax核 (无偏) | elu+1核 | N/A (低秩投影) | 精确softmax |
| 因果支持 | 是 | 是 | 困难 | 是 |
| 理论保证 | 无偏+低方差 | 无理论保证 | 低秩近似 | 精确 |

## 4. 实验表现
- **蛋白质序列建模**: 在较长序列上显著优于标准Transformer（内存/速度）
- **ImageNet**: 与标准注意力相当
- **语言建模**: 在使用足够多随机特征（$m \geq 256$）时接近标准Transformer
- **速度提升**: 序列长度$L=2048$时约4倍加速；$L=4096$时约8倍
- **内存**: 线性增长 vs. 二次增长

## 5. 总结
a) **一句话概括**: Performer通过FAVOR+（正交正随机特征映射）将softmax注意力核分解为线性可计算的形式，实现$O(L)$复杂度并保持无偏近似的理论保证。
b) **速记pipeline**: Q,K,V → φ(Q), φ(K) → φ(K)ᵀV → φ(Q)·[φ(K)ᵀV] → Normalize → Output
