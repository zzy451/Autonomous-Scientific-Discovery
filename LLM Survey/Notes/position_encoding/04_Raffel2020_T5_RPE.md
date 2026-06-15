# T5 Relative Position Bias
**论文**: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
**作者**: Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu
**年份**: 2020
**会议**: JMLR 2020
**arXiv**: 1910.10683

## 核心思想
T5 采用简化的相对位置偏置方案：在 attention logits 上加一个标量偏置，使用对数分桶（log-binning）将相对距离映射到固定数量的 bucket 中。

## 方法细节

### 标量偏置 vs 嵌入向量
- 与 Shaw et al. (2018) 使用可学习嵌入向量不同，T5 仅使用一个标量偏置
- 直接加到 attention logit（softmax 之前的分数）上
- 显著减少参数量

### 对数分桶 (Log-Binning)
- 相对距离被分到固定数量的 bucket 中（默认 32 个）
- 小距离使用线性间距（精确区分近邻 token）
- 大距离使用对数间距（粗粒度区分远端 token）
- 优势：
  - 参数高效（只需 32 个可学习标量/head）
  - 可泛化到训练时未见的序列长度
  - 体现了"近处精确、远处粗略"的归纳偏置

### 参数共享
- 偏置参数在所有层之间共享
- 但每个 attention head 有独立的偏置参数集

## Position Encoding 维度分析

### 分类
- **类型**: Relative Position Encoding / Attention Matrix Bias
- **注入方式**: 在 attention logits 上加标量偏置
- **参数量**: 极少（num_buckets × num_heads 个标量）
- **长度外推**: 分桶策略有助于长度泛化

### 设计亮点
1. 极简设计，参数量极小
2. 对数分桶：近距离精细、远距离粗略
3. 跨层共享，进一步减少参数

## 与其他方法的关系
- 可视为 attention matrix bias 家族的一员（与 ALiBi 同族）
- FIRE 证明了 T5 RPE 是其特例
- Kerple 也将其纳入统一框架

## 影响
- T5 的成功使该方案被广泛采用
- 对数分桶的思想影响后续工作
- 表明简单的位置偏置方案即可有效
