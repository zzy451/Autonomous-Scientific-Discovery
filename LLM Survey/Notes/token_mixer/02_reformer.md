# Reformer: The Efficient Transformer
**作者**: Nikita Kitaev, Lukasz Kaiser, Anselm Levskaya | **年份**: 2020 | **arxiv**: 2001.04451

## 0. 摘要翻译
大型Transformer模型在许多任务上取得了最先进的成果，但训练这些模型成本高昂，特别是在长序列上。本文引入两种技术来提高Transformer的效率：(1) 用局部敏感哈希（LSH）注意力替代点积注意力，将复杂度从$O(L^2)$降至$O(L\log L)$；(2) 使用可逆残差层替代标准残差层，使得激活值只需存储一次而非N次。由此产生的Reformer模型与标准Transformer性能相当，同时在长序列上具有更高的内存效率和更快的速度。

## 1. 方法动机
a) **为什么提出**: Transformer的内存和计算瓶颈限制了其处理长序列的能力。一个64K token序列、$d_{model}=1024$、$N=12$层的模型仅存储激活值就需要约16GB内存。
b) **现有痛点**: (1) 注意力的$O(L^2)$内存和计算复杂度；(2) 每层的激活值需要被存储用于反向传播，N层模型需要N倍内存；(3) FFN层的中间维度$d_{ff}$通常很大（4倍$d_{model}$），占用大量内存。
c) **研究假设**: 注意力矩阵是稀疏的——对于每个query，只有少数key的注意力权重是显著的；因此可以用近似最近邻搜索高效找到这些key。

## 2. 方法设计
a) **Pipeline**: 与标准Transformer结构一致，但替换了注意力机制和残差连接方式。

b) **模块功能**:
- **LSH Attention**: 使用局部敏感哈希将query和key映射到哈希桶中，只在同一桶内计算注意力。具体步骤：(1) 对query和key共享同一组随机投影进行哈希，$h(x) = \arg\max([xR; -xR])$；(2) 按哈希桶排序token；(3) 在每个桶内以及相邻桶之间计算注意力。使用多轮哈希提高召回率。
- **可逆残差网络 (Reversible Residual)**: 将输入分为$(x_1, x_2)$两部分，$y_1 = x_1 + \text{Attention}(x_2)$，$y_2 = x_2 + \text{FFN}(y_1)$。反向传播时可以从输出重建输入，无需存储中间激活值。
- **分块FFN**: 将FFN层的计算沿序列长度维度分块执行，减少峰值内存占用。

c) **公式解释**: LSH的核心思想是相似的向量有更高概率被映射到同一桶。通过选择$Q=K$（共享QK），保证query与自身总在同一桶中，简化了哈希匹配。

## 3. 与其他方法对比
| 方面 | Reformer | Transformer | Sparse Transformer |
|------|----------|-------------|-------------------|
| 注意力复杂度 | $O(L\log L)$ | $O(L^2)$ | $O(L\sqrt{L})$ |
| 内存(激活值) | $O(L)$ | $O(N \cdot L)$ | $O(N \cdot L)$ |
| 注意力类型 | LSH近似 | 精确 | 固定稀疏模式 |
| 长序列支持 | 优秀 | 受限 | 中等 |

## 4. 实验表现
- **enwiki8字符级语言建模**: 与全注意力Transformer性能持平（1.05 bpc），同时极大减少内存占用
- **WMT 2014 EN-DE**: 翻译质量接近全注意力baseline
- **长序列实验（64K tokens）**: Reformer可以在单设备上处理，而标准Transformer会OOM
- 可逆层对模型质量几乎无影响，但将内存减少至约1/N

## 5. 总结
a) **一句话概括**: Reformer通过LSH注意力（$O(L\log L)$）和可逆残差层将Transformer的内存和计算效率提升至可处理极长序列的水平，同时保持与标准Transformer相当的性能。
b) **速记pipeline**: Input → [LSH-Attention + RevResidual → FFN(chunked) + RevResidual] × N → Output
