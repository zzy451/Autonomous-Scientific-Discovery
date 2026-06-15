# Dao & Gu 2024 - Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality (Mamba-2)

**论文信息**
- 标题: Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality
- 作者: Tri Dao, Albert Gu
- 年份: 2024
- arXiv: 2405.21060
- 会议: ICML 2024

## 0. 摘要翻译
虽然Transformer一直是深度学习架构的主力，但状态空间模型(SSM)如Mamba最近展示了可比或更优的性能。我们证明了这些模型族之间的深层联系——当SSM的状态转移矩阵具有特定结构（标量乘以单位矩阵）时，SSM递归等价于半可分矩阵乘法，后者推广了因果线性注意力。我们利用这一对偶性设计Mamba-2，比Mamba快2-8倍。

## 1. 方法动机
a) **为什么提出**: Mamba-1的选择性扫描无法充分利用GPU的矩阵乘法硬件（Tensor Cores）
b) **现有方法痛点**: 
   - Mamba的扫描操作是IO密集的，在Tensor Cores上利用率低
   - Transformer和SSM之间的理论关系不清晰
   - 需要统一理解框架
c) **研究假设**: SSM和注意力是同一数学结构的不同计算方式

## 2. 方法设计
a) **方法流程**:
   - 证明结构化SSM ↔ 半可分矩阵 ↔ 线性注意力 的对偶关系
   - 利用对偶性设计SSD (Structured State Space Duality)层
   - SSD可以用矩阵乘法高效计算
   
b) **模块功能**:
   - **SSD Layer**: 约束A = aI（标量×单位矩阵），使SSM等价于线性注意力
   - **Chunk-wise计算**: 将序列分块，块内用矩阵乘法，块间用递归
   - **Multi-head设计**: 类似注意力的多头机制
   
c) **公式解释**:
   - 当 $A_t = a_t I$ 时：
     - SSM视角: $h_t = a_t h_{t-1} + B_t x_t$, $y_t = C_t h_t$
     - 注意力视角: $y_i = \sum_{j \leq i} (\prod_{k=j+1}^{i} a_k) (C_i B_j^T) x_j$
     - 矩阵视角: $Y = M \cdot X$，M是半可分矩阵
   - 块内: 用因果注意力矩阵计算（利用matmul）
   - 块间: 用递归传递状态

## 3. 与其他方法对比
a) **本质不同**: 理论统一了SSM和注意力，在此基础上设计更高效算法
b) **创新点**: 
   - State Space Duality理论框架
   - 将SSM计算转化为matmul，充分利用Tensor Cores
   - 2-8x加速 vs Mamba-1
c) **适用场景**: 同Mamba-1（长序列建模），但更快
d) **对比表格**:

| 特性 | Mamba-1 | Mamba-2 | Transformer |
|------|---------|---------|-------------|
| 核心操作 | 选择性扫描 | SSD(块matmul+递归) | 注意力matmul |
| 硬件利用 | IO密集 | 计算密集(Tensor Cores) | 计算密集 |
| 速度(vs Mamba-1) | 1x | 2-8x | - |
| 状态维度N | 16 | 64-256 | - |

## 4. 实验表现
a) **验证方式**: 语言建模（Pile）、合成任务
b) **关键数据**: Mamba-2 2.7B达到Mamba-1 相当的性能，速度提升2-8倍；可使用更大状态维度
c) **优势场景**: 需要高吞吐的长序列任务
d) **局限性**: A约束为标量×I可能限制表达能力

## 5. 学习与应用
a) **开源情况**: 完全开源
b) **实现细节**: chunk_size通常256；支持更大状态维度(64-256)
c) **迁移可能性**: 可替换Mamba-1；为后续混合架构提供基础

## 6. 总结
a) **一句话概括**: 通过证明SSM和注意力的数学对偶性，设计出基于矩阵乘法的SSD算法，将Mamba加速2-8倍
b) **速记版pipeline**: Input → 分块 → 块内: 半可分矩阵乘法(matmul) + 块间: 递归 → Output

**Token Mixer维度**: RNN-Like/SSM方案（Mamba进化版），通过SSM-Attention对偶性实现硬件高效计算
