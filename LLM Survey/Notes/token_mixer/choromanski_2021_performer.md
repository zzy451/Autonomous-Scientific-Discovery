# Choromanski et al. 2021 - Rethinking Attention with Performers

**论文信息**
- 标题: Rethinking Attention with Performers
- 作者: Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, David Belanger, Lucy Colwell, Adrian Weller
- 年份: 2021 (arXiv 2020)
- arXiv: 2009.14794
- 会议: ICLR 2021 (Oral)

## 0. 摘要翻译
我们提出Performers，一种能够通过FAVOR+（Fast Attention Via positive Orthogonal Random features）机制实现线性时间和空间复杂度的Transformer架构。FAVOR+利用正交随机特征来近似softmax注意力核，提供了对完整注意力的无偏估计，并且计算复杂度为O(N)。

## 1. 方法动机
a) **为什么提出**: 需要一种无需稀疏性或低秩假设的线性注意力方法
b) **现有方法痛点**: 
   - 标准softmax注意力O(N²)不可扩展
   - 现有近似方法（如Linformer）依赖低秩假设或固定模式
c) **研究假设**: softmax核可以通过随机特征映射来无偏近似，从而将注意力线性化

## 2. 方法设计
a) **方法流程**:
   - 定义特征映射函数 $\phi$，使得 $\text{softmax}(QK^T) \approx \phi(Q)\phi(K)^T$
   - 利用结合律改变矩阵乘法顺序：先算 $\phi(K)^TV$，再与 $\phi(Q)$ 相乘
   - 时间复杂度从 O(N²d) 降到 O(Nrd)，r为特征维度
   
b) **模块功能**:
   - **FAVOR+**: 使用正随机特征(Positive Random Features)近似softmax核
   - 特征映射: $\phi(x) = \frac{e^{-||x||^2/2}}{\sqrt{m}} [e^{w_1^Tx}, ..., e^{w_m^Tx}]$
   - 正交随机特征(ORF): 使用正交矩阵减少方差
   
c) **公式解释**:
   - 标准: $\text{Att}(Q,K,V) = D^{-1}(\phi(Q)(\phi(K)^TV))$，其中 $D = \text{diag}(\phi(Q)\phi(K)^T\mathbf{1})$
   - 利用结合律: $\phi(Q)·[\phi(K)^TV]$ 复杂度 O(Nrd)
   - r ≈ d log d 即可获得良好近似

## 3. 与其他方法对比
a) **本质不同**: 通过核方法理论来近似softmax，而非截断或低秩投影
b) **创新点**: 
   - 无偏估计（理论保证）
   - 正交随机特征降低方差
   - 同时适用于因果和非因果注意力
c) **适用场景**: 长序列建模（编码器和解码器均可）
d) **对比表格**:

| 特性 | Transformer | Performer | Linformer |
|------|-------------|-----------|-----------|
| 复杂度 | O(N²d) | O(Nrd) | O(Nkd) |
| 理论保证 | 精确 | 无偏近似 | 有偏近似 |
| 因果注意力 | 是 | 是 | 困难 |
| 近似方法 | - | 核随机特征 | 低秩投影 |

## 4. 实验表现
a) **验证方式**: ImageNet、蛋白质建模、LM1B语言建模
b) **关键数据**: 在大多数任务上接近完整注意力性能；长序列效率显著提升
c) **优势场景**: 蛋白质序列建模（序列极长）、通用长序列任务
d) **局限性**: 近似质量依赖于特征维度r；在短序列上可能慢于标准注意力；实际LLM中较少使用

## 5. 学习与应用
a) **开源情况**: Google开源（JAX实现）
b) **实现细节**: 推荐r = O(d log d)；正交随机特征矩阵需定期重新采样
c) **迁移可能性**: 理论优美但在实际LLM中被FlashAttention等硬件优化方案取代

## 6. 总结
a) **一句话概括**: 通过FAVOR+随机特征映射近似softmax核，实现O(N)线性注意力，理论上无偏但实际中被其他方案取代
b) **速记版pipeline**: Input → φ(Q), φ(K), V → φ(K)^T V（先算） → φ(Q)·[φ(K)^TV] → Output

**Token Mixer维度**: Linear Attention方案，核方法近似softmax，O(N)复杂度，适用于因果和非因果场景
