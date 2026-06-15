# Yang et al. 2024 - Parallelizing Linear Transformers with the Delta Rule over Sequence Length (DeltaNet)

**论文信息**
- 标题: Parallelizing Linear Transformers with the Delta Rule over Sequence Length
- 作者: Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, Yoon Kim
- 年份: 2024
- arXiv: 2406.06484
- 会议: NeurIPS 2024

## 0. 摘要翻译
线性Transformer通过将softmax注意力替换为线性核来实现线性复杂度。DeltaNet使用delta规则替代标准的外积加法来更新隐状态，已被证明在联想记忆任务上更有效。然而，delta规则的标准算法是顺序的，无法在序列长度维度上并行化。我们提出了一种硬件高效的并行训练算法。

## 1. 方法动机
a) **为什么提出**: Delta规则优于外积加法，但之前无法并行训练
b) **现有方法痛点**: 
   - 外积加法: $S_t = S_{t-1} + k_t v_t^T$，信息叠加导致干扰
   - Delta规则虽好但顺序计算太慢
   - 需要高效的并行化方案
c) **研究假设**: 通过将Delta规则重写为Householder变换矩阵乘积，可以实现高效并行

## 2. 方法设计
a) **方法流程**:
   - Delta规则: $S_t = (I - \beta_t k_t k_t^T) S_{t-1} + \beta_t v_t k_t^T$
   - 重写为: $S_t = H_t S_{t-1} + \beta_t v_t k_t^T$，其中 $H_t = I - \beta_t k_t k_t^T$（Householder矩阵）
   - 使用compact WY表示法将连续Householder矩阵乘积高效计算
   - 结合chunk-wise分块实现并行训练
   
b) **模块功能**:
   - **Delta Rule**: 先用当前key查询旧状态，再做误差更新
   - **Householder变换**: 将状态转移表示为反射变换
   - **WY表示**: 将T个Householder矩阵乘积紧凑表示为 $I - WY^T$
   - **Chunk-wise并行**: 块内WY并行，块间递归
   
c) **公式解释**:
   - $H_t = I - \beta_t k_t k_t^T$: 广义Householder反射矩阵
   - $\prod_{t=1}^{T} H_t = I - W_T Y_T^T$: compact WY分解
   - W, Y可以增量计算，避免显式矩阵乘法

## 3. 与其他方法对比
a) **本质不同**: Delta规则的状态更新 + Householder并行化（vs GLA的简单门控）
b) **创新点**: 
   - 首个可并行训练的Delta规则线性Transformer
   - Householder变换的巧妙应用
   - 在检索任务上显著优于外积加法模型
c) **适用场景**: 需要精确联想记忆的任务
d) **对比表格**:

| 特性 | Linear Attn | GLA | DeltaNet |
|------|------------|-----|----------|
| 更新规则 | 外积加法 | 门控外积加法 | Delta规则 |
| 记忆冲突 | 严重 | 门控缓解 | 先擦后写 |
| 并行化 | 简单 | chunk-wise | WY + chunk-wise |
| 检索能力 | 弱 | 中 | 强 |

## 4. 实验表现
a) **验证方式**: 语言建模、MQAR检索任务
b) **关键数据**: 
   - DeltaNet-1.3B超过Mamba-1.3B和GLA-1.3B
   - 在MQAR上大幅领先外积加法模型
   - 训练速度acceptable（WY有额外开销但可接受）
c) **优势场景**: 联想记忆、精确检索
d) **局限性**: WY分解的额外计算和内存开销

## 5. 学习与应用
a) **开源情况**: 开源（flash-linear-attention库）
b) **实现细节**: 基于Triton实现；chunk_size=64
c) **迁移可能性**: 为Gated Delta Networks和RWKV-7提供了基础

## 6. 总结
a) **一句话概括**: 通过Householder变换和compact WY表示法，首次实现了Delta规则在线性Transformer中的高效并行训练
b) **速记版pipeline**: Input → K,V,β → Householder矩阵(I-βkkT) → WY并行分解 → 状态更新 → Output

**Token Mixer维度**: RNN-Like/Linear Attention方案，Delta规则替代外积加法实现精确联想记忆
