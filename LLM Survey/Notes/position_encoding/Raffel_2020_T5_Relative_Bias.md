# Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5)
**作者**: Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu | **年份**: 2020 | **来源**: JMLR 2020 | **arXiv**: 1910.10683

## 0. 摘要翻译
本文提出 T5（Text-to-Text Transfer Transformer），通过将所有 NLP 任务统一为文本到文本的格式来系统性地探索迁移学习。在位置编码方面，T5 采用了一种简化的相对位置偏置（Relative Position Bias），将标量偏置直接加入注意力 logits。偏置值按距离分桶（bucketing）共享，使模型能高效处理不同长度序列。

## 1. 方法动机
a) **为什么提出**: 需要一种高效的相对位置编码方法，既能编码相对距离又不增加太多计算开销。
b) **现有痛点**: 
   - Shaw et al. (2018) 的相对 PE 在 key 和 value 上都添加向量，计算较重
   - 绝对 PE 无法有效编码相对距离
   - 需要一种参数高效且可跨长度泛化的方案
c) **研究假设**: 使用简单的标量偏置（而非向量）即可有效编码相对位置，通过对数分桶可以处理不同距离尺度。

## 2. 方法设计
a) **pipeline**: 
   1. 计算 query 和 key 的相对距离 $r = i - j$
   2. 将距离 $r$ 映射到桶索引 $b(r)$（对数分桶）
   3. 查找桶对应的可学习标量偏置 $B_{b(r)}$
   4. 将偏置加入注意力分数: $a_{ij} = q_i^T k_j / \sqrt{d} + B_{b(r)}$

b) **模块功能**: 
   - 分桶函数：小距离（$|r| \leq 8$）每个距离一个桶，大距离使用对数分桶
   - 标量偏置：每个桶对应一个可学习参数
   - 参数共享：所有层共享同一组偏置参数，每个 head 有独立偏置

c) **公式解释**:
   - 分桶策略: 
     - 精确桶：$|r| \leq 8$ 时，$b(r) = r$
     - 对数桶：$|r| > 8$ 时，$b(r) = 8 + \lfloor \log_{\beta}(|r|/8) \rfloor$
   - 总桶数通常为 32（可配置）
   - 偏置矩阵: $B \in \mathbb{R}^{H \times n_{buckets}}$（$H$ 为 head 数）
   - 跨层共享：所有 Transformer 层共享同一个 $B$ 矩阵

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 Shaw et al. (2018)：Shaw 使用向量偏置加到 K 和 V，T5 只用标量偏置加到 logits
   - 与 ALiBi：ALiBi 使用固定线性偏置，T5 使用可学习分桶偏置
   - 与 RoPE：RoPE 通过旋转在 Q/K 中编码位置，T5 在注意力分数上加偏置
   - 与 KERPLE/FIRE：KERPLE 用连续核函数，T5 用离散分桶
b) **创新点**: 
   - 将相对 PE 简化为标量偏置（大幅降低计算量）
   - 对数分桶策略平衡了近距离精度和远距离覆盖
   - 跨层参数共享进一步减少参数量
c) **适用场景**: T5、mT5、FLAN-T5 等 encoder-decoder 模型；适合需要参数高效的相对位置编码场景。

## 4. 实验表现
a) **验证方式**: 在大规模 NLP 基准上评估 T5 系列模型。
b) **关键数据**: 
   - T5-11B 在 GLUE、SuperGLUE、SQuAD、WMT 等多个基准上达到 SOTA
   - 相对位置偏置相比绝对 PE 在多数任务上更稳定
   - 跨层共享偏置几乎不影响性能
c) **局限性**: 
   - 分桶策略是离散的，丧失了精确距离信息
   - 桶数和分桶边界需要手工设定
   - 在 decoder-only LLM 中不如 RoPE 主流
   - 对数分桶假设远距离精度不重要，可能不适合所有任务

## 5. 总结
a) **一句话概括**: T5 的相对位置偏置通过对数分桶将相对距离映射为可学习的标量偏置加入注意力分数，以极少参数实现了高效的相对位置编码。
b) **速记 pipeline**: Relative Distance $r=i-j$ → Log Bucketing $b(r)$ → Learnable Scalar Bias $B_{b(r)}$ → Add to $QK^T/\sqrt{d}$ → Softmax → Attention
