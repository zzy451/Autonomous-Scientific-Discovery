# DeBERTa: Disentangled Attention
**论文**: DeBERTa: Decoding-enhanced BERT with Disentangled Attention
**作者**: Pengcheng He, Xiaodong Liu, Jianfeng Gao, Weizhu Chen
**年份**: 2021
**会议**: ICLR 2021
**arXiv**: 2006.03654

## 核心思想
DeBERTa 将每个 token 用两个独立向量表示——内容向量和相对位置向量——并在 attention 计算中将内容-内容、内容-位置、位置-内容的交互解耦（disentangle）。

## 方法细节

### 解耦表示 (Disentangled Representation)
每个 token i 有两个向量：
- **内容向量** H_i: 编码语义信息
- **位置向量** P_{i|j}: 编码与 token j 的相对位置

### 解耦注意力 (Disentangled Attention)
Attention score 分解为三个分项（省略了 position-to-position 项）：

$$A_{ij} = \underbrace{H_i W_q^c \cdot (H_j W_k^c)^T}_{content-to-content} + \underbrace{H_i W_q^c \cdot (P_{j|i} W_k^p)^T}_{content-to-position} + \underbrace{P_{i|j} W_q^p \cdot (H_j W_k^c)^T}_{position-to-content}$$

- 三组交互使用独立的投影矩阵
- position-to-position 项被省略（实验证明贡献小）
- 每种交互可以独立学习其最优模式

### Enhanced Mask Decoder
- 核心 attention 使用相对位置
- 在 MLM 预训练的最后一层解码时引入绝对位置
- 因为某些 MLM 任务（如预测 masked token）确实需要绝对位置信息

## Position Encoding 维度分析

### 分类
- **类型**: Relative Position Encoding（解耦式）
- **注入方式**: 在 attention score 中通过独立投影矩阵引入
- **参数量**: 需要额外的 W_q^p, W_k^p 投影矩阵
- **长度外推**: 相对位置本身有助于泛化，但 clipping 范围限制了外推

### 创新点
1. 内容与位置的解耦：更灵活的表示
2. 三分项 attention：独立建模不同类型的交互
3. 混合策略：主体使用相对位置 + 解码层使用绝对位置

## 实验结果
- 超越 RoBERTa（在 SuperGLUE 上超过人类基线）
- 证明了相对位置的解耦表示的有效性

## 影响
- 表明位置信息的精细化建模（解耦）比简单叠加更有效
- 混合绝对/相对位置的思路对后续工作有启发
