# Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation
**作者**: Ofir Press, Noah A. Smith, Mike Lewis | **年份**: 2022 | **来源**: ICLR 2022 | **arXiv**: 2108.12409

## 0. 摘要翻译
本文提出 ALiBi（Attention with Linear Biases），一种简洁的位置编码替代方案。ALiBi 不向 word embedding 添加位置编码，而是在注意力分数中添加与 query-key 距离成线性比例的惩罚偏置。该方法使模型能在训练时使用较短序列，但在推理时有效处理更长序列（"Train Short, Test Long"），同时训练速度提升 11%、内存开销更低。

## 1. 方法动机
a) **为什么提出**: 训练长上下文模型的计算成本极高。如果能用短序列训练但在推理时处理长序列，将大幅降低训练成本。
b) **现有痛点**: 
   - Sinusoidal PE 和 learned PE 在外推至训练长度以外时性能急剧下降
   - Rotary PE 的外推能力也有限
   - 需要一种天然支持长度外推的位置编码机制
c) **研究假设**: 通过在注意力分数中直接施加与距离成正比的固定偏置，模型可以学习到一种对长度变化更鲁棒的位置感知方式。

## 2. 方法设计
a) **pipeline**: 
   1. 正常计算 Q·K 注意力分数
   2. 加上距离偏置矩阵 $M$
   3. 经过 softmax 得到注意力权重
   4. 无需在 embedding 层添加任何位置信息

b) **模块功能**: 偏置矩阵对远距离 token 施加负向惩罚（penalty），使注意力自然偏向近距离 token。

c) **公式解释**:
   - $\text{Attention}(Q, K, V) = \text{softmax}(QK^T + m \cdot [-(i-1), ..., -1, 0])V$
   - 其中 $m$ 是每个 head 特有的斜率（slope）
   - 斜率按几何级数分配: $m_h = 2^{-8/H \cdot h}$，$H$ 为 head 总数
   - 不同斜率使不同 head 关注不同范围：陡斜率聚焦局部，平斜率关注全局

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 sinusoidal/learned PE：ALiBi 不修改输入 embedding，直接在注意力分数上操作
   - 与 RoPE：RoPE 通过旋转编码位置到 Q/K 中，ALiBi 通过加性偏置编码
   - 与 T5 relative bias：T5 使用可学习的分桶偏置，ALiBi 使用固定的线性偏置
b) **创新点**: 
   - 极简设计：无需学习参数，完全由距离和预设斜率决定
   - 计算效率高：偏置矩阵可预计算并缓存
   - 长度外推能力强：在 1024 token 上训练可外推至 2048+
c) **适用场景**: 适用于需要长度外推的场景；被 BLOOM、MPT 等模型采用；在固定上下文窗口任务中表现稳定。

## 4. 实验表现
a) **验证方式**: 在 WikiText-103 上训练语言模型，评估不同长度上的困惑度（perplexity）。
b) **关键数据**: 
   - 在 1024 token 上训练、2048 token 上推理时，ALiBi 的困惑度仅比在 2048 上训练的模型高 0.07
   - Sinusoidal PE 在同条件下困惑度恶化超过 10 倍
   - 训练速度比 sinusoidal PE 快 11%
c) **局限性**: 
   - 外推倍数有上限（通常 2-4 倍），超出后仍会退化
   - 固定的线性衰减假设可能不适合所有任务（有些任务需要关注远距离信息）
   - 在一些下游任务（如 coding）中不如 RoPE
   - 无法编码绝对位置信息

## 5. 总结
a) **一句话概括**: ALiBi 通过在注意力分数上添加与距离成正比的固定线性偏置，以极简方式实现位置编码，天然支持长度外推，但固定的衰减模式限制了其灵活性。
b) **速记 pipeline**: Q·K^T + Linear Distance Bias (head-specific slope) → softmax → Attention Output
