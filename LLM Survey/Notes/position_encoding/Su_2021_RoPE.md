# RoFormer: Enhanced Transformer with Rotary Position Embedding
**作者**: Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu | **年份**: 2021 | **来源**: arXiv (后收录于 Neurocomputing 2024) | **arXiv**: 2104.09864

## 0. 摘要翻译
本文提出了旋转位置编码（Rotary Position Embedding, RoPE），一种利用旋转矩阵编码绝对位置同时在自注意力内积中自然引入相对位置依赖的方法。RoPE 具有灵活的序列长度扩展性、随相对距离增大的 token 间依赖衰减特性，并可与线性自注意力结合使用。作者将 RoPE 集成到 Transformer（称为 RoFormer），在中文和英文长文本分类基准上均取得了优异表现。

## 1. 方法动机
a) **为什么提出**: 现有位置编码方法要么只编码绝对位置（sinusoidal PE、learned PE），要么需要额外修改注意力计算（relative PE）。需要一种统一框架，既编码绝对位置又自然产生相对位置依赖。
b) **现有痛点**: 
   - Sinusoidal PE 通过加法融合，理论上可编码相对位置但实际效果有限
   - 相对位置编码（如 Shaw et al. 2018）需要修改注意力机制，增加复杂度
   - 现有方法难以在绝对位置信息和相对位置信息间取得平衡
c) **研究假设**: 通过对 query 和 key 向量施加与位置相关的旋转变换，可以使其内积仅依赖于相对位置差，从而同时编码绝对和相对位置信息。

## 2. 方法设计
a) **pipeline**: 
   1. 计算 query $q$ 和 key $k$（通过线性投影）
   2. 对 $q_m$ 和 $k_n$ 分别施加旋转矩阵 $R_{\Theta,m}$ 和 $R_{\Theta,n}$
   3. 计算注意力分数 $q_m^T k_n = (R_{\Theta,m} W_q x_m)^T (R_{\Theta,n} W_k x_n)$
   4. 内积结果仅依赖于 $m-n$（相对位置）

b) **模块功能**: 旋转矩阵将 $d$ 维向量的每对相邻维度视为二维子空间，在该子空间上按位置索引执行旋转。

c) **公式解释**:
   - 旋转角度: $\theta_i = 10000^{-2i/d}$，与 sinusoidal PE 使用相同的频率基底
   - 旋转操作: $f(x_m, m) = R_{\Theta,m} x_m$，其中旋转矩阵为分块对角矩阵
   - 内积: $\langle f(q, m), f(k, n) \rangle = q^T R_{\Theta,n-m} k$，仅依赖相对位置 $n-m$
   - 实际实现中可用元素级乘法+重排代替矩阵乘法，计算高效

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 sinusoidal PE 的加法融合不同，RoPE 采用乘法融合（旋转变换）
   - 与 relative PE 不同，RoPE 在 query/key 上操作而非修改注意力分数
   - 与 ALiBi 不同，RoPE 编码在 Q/K 向量中而非注意力偏置
b) **创新点**: 
   - 统一了绝对位置编码（每个位置有唯一旋转角度）和相对位置编码（内积只取决于位置差）
   - 无额外参数，计算开销极小
   - 自然具有远程衰减特性
c) **适用场景**: 已成为 LLM 事实标准（LLaMA, Mistral, Gemma, Qwen 等均采用）。适用于各种序列长度，配合 PI/NTK/YaRN 等扩展方法可支持超长上下文。

## 4. 实验表现
a) **验证方式**: 在中文（CLUE/CAIL）和英文（IMDB/Amazon Reviews）长文本分类任务上评估。
b) **关键数据**: RoFormer 在所有评估任务上表现优于使用其他位置编码的 BERT 变体；在英文任务上比 BERT 高约 0.5-1% 准确率。
c) **局限性**: 
   - 原始 RoPE 的外推能力有限，超出训练长度后性能下降（需配合 PI/YaRN 等扩展）
   - 高维旋转可能在极长序列中出现数值精度问题
   - 对短距离位置区分度不如某些方法

## 5. 总结
a) **一句话概括**: RoPE 通过对 Q/K 向量施加位置相关的旋转变换，在不增加参数的情况下同时编码绝对和相对位置，已成为当代 LLM 的标准位置编码方案。
b) **速记 pipeline**: Q/K Linear Projection → Apply Rotation $R_\Theta$ per position → Rotated Q·K inner product (relative-position-dependent) → Attention
