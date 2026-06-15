# KERPLE: Kernelized Relative Positional Embedding for Length Extrapolation
**作者**: Ta-Chung Chi, Ting-Han Fan, Peter J. Ramadge, Alexander Rudnicky | **年份**: 2022 | **来源**: NeurIPS 2022 | **arXiv**: 2205.09921

## 0. 摘要翻译
本文提出 KERPLE（Kernelized Relative Positional Embedding），一种基于核函数的相对位置编码框架。KERPLE 利用条件正定（CPD）核来泛化相对位置距离的度量方式，并证明 CPD 核可以通过加上常数偏移转化为正定核，而该偏移在 softmax 归一化中被隐式吸收。文章引入了多个变体，其中对数变体在长度外推基准上表现最优。

## 1. 方法动机
a) **为什么提出**: 现有相对位置编码方法（如 ALiBi 的线性偏置）是启发式设计的，缺乏统一的数学框架来理解和改进。
b) **现有痛点**: 
   - ALiBi 的线性偏置形式过于简单，可能不是最优的距离度量
   - 缺乏从核函数视角理解位置偏置的理论框架
   - 不知道什么样的偏置函数适合长度外推
c) **研究假设**: 通过核函数理论，可以系统地设计满足特定数学性质（条件正定性）的位置偏置函数，并从中找到比线性更优的形式。

## 2. 方法设计
a) **pipeline**: 
   1. 选择条件正定核 $K(r)$（$r$ 为相对距离）
   2. 将核值作为偏置加入注意力分数
   3. softmax 归一化自动处理 CPD 核到 PD 核的转换
   4. 各 head 使用不同的核参数

b) **模块功能**: 核函数将相对距离映射为注意力偏置值，提供了比线性更丰富的距离-偏置映射关系。

c) **公式解释**:
   - 注意力分数: $a_{ij} = q_i^T k_j + K(|i-j|)$
   - 对数核变体: $K(r) = -p_1 \log(1 + p_2 \cdot r)$，其中 $p_1, p_2 > 0$ 为可学习参数
   - 幂律变体: $K(r) = -p_1 r^{p_2}$，其中 $0 < p_2 \leq 2$
   - ALiBi 是 KERPLE 的特例：$K(r) = -m \cdot r$（线性核，$p_1=m, p_2=1$）
   - CPD 到 PD 的转换: $K_{PD}(r) = K_{CPD}(r) + c$，常数 $c$ 在 softmax 中消除

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 ALiBi：ALiBi 是 KERPLE 的线性特例；KERPLE 提供了更灵活的核函数族
   - 与 RoPE：RoPE 在 Q/K 空间旋转，KERPLE 在注意力分数上加核偏置
   - 与 T5 bias：T5 用分桶离散化，KERPLE 用连续核函数
b) **创新点**: 
   - 首次将核方法引入位置编码设计，提供理论框架
   - 证明 ALiBi 是更广泛框架的特例
   - 对数核在长度外推上显著优于线性核
c) **适用场景**: 需要强长度外推能力的语言建模任务；提供了设计新位置偏置函数的理论指导。

## 4. 实验表现
a) **验证方式**: 在 OpenWebText2、GitHub、ArXiv 数据集上训练语言模型，评估长度外推困惑度。
b) **关键数据**: 
   - 对数核在 8192 token 外推（训练 512 token）上困惑度最低
   - 对数核比 ALiBi（线性核）在外推上低约 0.5-1.0 困惑度
   - 幂律核表现介于线性和对数之间
c) **局限性**: 
   - 可学习核参数增加了训练复杂度
   - 核函数的选择仍有一定经验性
   - 在非常长的外推场景下，对数衰减是否最优仍需验证

## 5. 总结
a) **一句话概括**: KERPLE 通过核函数理论框架统一了位置偏置类方法，证明 ALiBi 是其线性特例，并提出的对数核变体在长度外推上显著优于线性偏置。
b) **速记 pipeline**: Relative Distance $r=|i-j|$ → CPD Kernel $K(r)$ (Log/Power/Linear) → Add to QK^T → Softmax (absorbs CPD→PD offset) → Attention
