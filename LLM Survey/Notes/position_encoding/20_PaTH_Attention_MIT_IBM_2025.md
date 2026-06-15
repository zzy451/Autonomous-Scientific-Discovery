# PaTH Attention: Position Encoding via Accumulating Householder Transformations
**作者**: Yinzhu Quan, Kabir Ahuja, Yash Akhauri, David Cox, Florian Wenzel (MIT-IBM Watson AI Lab)
**年份**: 2025 | **arxiv**: 2505.16381

## 0. 摘要翻译
PaTH 是一种灵活的数据依赖位置编码方案，基于 Householder（类）变换的累积乘积。每个变换都是数据依赖的（即由当前 token 的内容决定），使得位置编码能够根据输入序列的语义内容自适应调整。PaTH 在合成任务和真实语言建模任务上均优于 RoPE。

## 1. 方法动机
- RoPE 的旋转矩阵是固定的、数据无关的：位置 $m$ 和 $n$ 之间的变换仅取决于 $m-n$，与 token 内容无关
- 这意味着 RoPE 无法根据语义上下文调整位置感知——所有 token 对之间的位置关系是刚性的
- 理想的位置编码应该是"内容感知"的：语义相关的 token 即使距离较远也应有较强的位置关联
- Householder 变换提供了一种参数高效的正交变换构造方式

## 2. 核心方法

### 2.1 Householder 变换基础
Householder 变换（反射）由一个向量 $v$ 定义：
$$H(v) = I - 2\frac{vv^T}{\|v\|^2}$$
- $H(v)$ 是正交矩阵（保范数）
- 任意正交矩阵都可以分解为 Householder 变换的乘积

### 2.2 数据依赖的位置编码
对于位置 $i$ 的 token $x_i$：
1. 通过可学习投影生成 Householder 向量：$v_i = W_v x_i$
2. 构造 Householder 矩阵：$H_i = H(v_i)$
3. 位置 $i$ 的累积变换：$P_i = H_1 H_2 \cdots H_i$
4. 对 query/key 施加变换：$q'_i = P_i q_i$, $k'_i = P_i k_i$

### 2.3 相对位置性质
位置 $i$ 和 $j$ 之间的相对变换：
$$P_i^T P_j = H_i^T \cdots H_{j+1}^T \quad (i < j)$$
- 相对变换仅依赖于中间 token 的内容
- 自然编码了"路径依赖"的相对位置信息
- 与 RoPE 的固定旋转形成对比

### 2.4 高效并行算法
- 直接计算累积乘积需要 $O(n)$ 的顺序操作
- 利用 Householder 矩阵的紧凑表示（仅需存储向量 $v$）
- 设计了 FlashAttention 风格的分块算法，实现高效 GPU 并行
- 训练速度与 RoPE 相当

## 3. 实验结果
- 在合成任务（排序、复制、关联记忆）上显著优于 RoPE
- 在语言建模（OpenWebText）上 perplexity 优于 RoPE
- 长度泛化能力优于 RoPE：训练 512 长度，可泛化到 2048+
- 消融实验证实数据依赖性是性能提升的关键

## 4. 关键优势与局限

### 优势
- 数据依赖：位置编码随内容自适应调整
- 理论优雅：基于正交群的严格数学框架
- 表达能力强：可表示任意正交变换（RoPE 仅是其子集）

### 局限
- 累积乘积引入了顺序依赖，可能影响极长序列的并行效率
- 尚未在大规模（>7B）模型上验证
- 数据依赖性可能增加训练不稳定性

## 5. 与本综述的关联
- 代表了"数据依赖位置编码"这一新兴方向的重要进展
- 从数学上证明 RoPE 是 PaTH 的特殊情况（固定 Householder 向量）
- 与 CoPE（Contextual PE）思路相似但实现路径不同
- 可能预示着下一代位置编码的发展方向：从固定到自适应

## 6. 标签
`#数据依赖PE` `#Householder变换` `#正交群` `#FlashAttention` `#MIT-IBM` `#超越RoPE`
