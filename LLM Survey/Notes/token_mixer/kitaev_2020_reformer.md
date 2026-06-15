# Kitaev et al. 2020 - Reformer: The Efficient Transformer

**论文信息**
- 标题: Reformer: The Efficient Transformer
- 作者: Nikita Kitaev, Lukasz Kaiser, Anselm Levskaya
- 年份: 2020
- arXiv: 2001.04451
- 会议: ICLR 2020

## 0. 摘要翻译
大型Transformer模型在许多任务上取得了最先进的结果，但训练这些模型的成本极其高昂，尤其是在长序列上。我们引入了两种技术来提高Transformer的效率：(1) 用局部敏感哈希（LSH）替代点积注意力，将复杂度从O(L²)降低到O(L log L)；(2) 使用可逆残差代替标准残差，使得在反向传播时无需存储中间激活值。

## 1. 方法动机
a) **为什么提出**: 标准Transformer在长序列上内存和计算成本都是O(N²)，对于64K+序列不可行
b) **现有方法痛点**: 注意力矩阵占内存O(N²)；N层每层都需存储激活值用于反向传播
c) **研究假设**: 注意力分布通常是稀疏的（大部分注意力集中在少数token上），可以通过哈希近似找到高注意力的token对

## 2. 方法设计
a) **方法流程**:
   - 通过LSH将Q、K映射到哈希桶中
   - 只在同一桶内的token之间计算注意力
   - 使用可逆残差层减少内存占用
   
b) **模块功能**:
   - **LSH Attention**: 使用局部敏感哈希将相似的Q、K映射到同一桶，仅在桶内计算注意力
   - **可逆残差网络(RevNet)**: $y_1 = x_1 + F(x_2)$, $y_2 = x_2 + G(y_1)$，反向传播无需存储激活
   - **分块处理**: 将长序列分成块处理，进一步减少内存
   
c) **公式解释**:
   - LSH: $h(x) = \arg\max([xR; -xR])$，R为随机投影矩阵
   - 多轮哈希提高近似质量
   - 总复杂度: O(N log N)

## 3. 与其他方法对比
a) **本质不同**: 用数据依赖的哈希方法实现近似注意力，而非固定模式的稀疏
b) **创新点**: LSH用于注意力计算 + 可逆残差双重优化
c) **适用场景**: 超长序列建模（64K tokens+）
d) **对比表格**:

| 特性 | 标准Transformer | Reformer | Longformer |
|------|-----------------|----------|------------|
| 注意力复杂度 | O(N²) | O(N log N) | O(N·w) |
| 激活内存 | O(N·L) | O(N) | O(N·L) |
| 稀疏类型 | 无 | 数据依赖 | 固定模式 |

## 4. 实验表现
a) **验证方式**: enwiki8字符级建模、图像生成(imagenet64)
b) **关键数据**: 在64K长度序列上可训练，质量接近完整注意力
c) **优势场景**: 超长文本/序列建模
d) **局限性**: LSH引入近似误差；多轮哈希增加常数开销；实际wall-clock加速不如理论

## 5. 学习与应用
a) **开源情况**: Google开源（Trax框架）
b) **实现细节**: 推荐使用8轮LSH哈希，桶大小通常为序列长度的1/4-1/8
c) **迁移可能性**: 概念影响了后续稀疏注意力研究，但实际应用中被FlashAttention等方案取代

## 6. 总结
a) **一句话概括**: 通过LSH近似注意力和可逆残差网络，将Transformer的内存和计算效率提升到可处理超长序列
b) **速记版pipeline**: Input → LSH Hash → Bucket Sort → Intra-Bucket Attention → RevNet → Output

**Token Mixer维度**: Linear/Sub-quadratic Attention方案，使用LSH实现O(N log N)复杂度的数据依赖稀疏注意力
