# Improving Transformer Models by Reordering their Sublayers (Sandwich Transformer)

## 基本信息
- **作者**: Ofir Press, Noah A. Smith, Omer Levy
- **年份**: 2020 (ACL 2020)
- **arXiv**: 1911.03864
- **关键词**: Sandwich Transformer, 子层重排序, 语言建模

## 核心贡献（Module Sequence 维度）
本文是 Module Sequence 研究中的**标志性工作**，直接研究子层排列顺序对性能的影响。

### 1. 核心发现：子层顺序不是固定的
- 标准 Transformer: 交替排列 Self-Attention (s) 和 FFN (f): `s f s f s f ...`
- 作者探索了所有可能的子层排列方式
- 发现不同的排列方式会产生显著不同的性能

### 2. Sandwich 模式
- **底部**: n 层纯 Self-Attention
- **中间**: 标准交替排列 (s f s f ...)
- **顶部**: n 层纯 FFN
- 整体形状: `s s s [s f s f ...] f f f`

### 3. 直觉与动机
- 底部多放 Attention 层 → 更好地建立 token 间的关系
- 顶部多放 FFN 层 → 更好地进行特征变换
- 类似于"先理解上下文，再做预测"的信息处理流程

### 4. 实验结果
- 在 WikiText-103 和 enwik8 上超过标准交替排列的 baseline
- **无额外计算开销**：只是重排现有子层，不增加参数
- 在机器翻译任务上效果不显著，说明最优排列可能是任务相关的

## 与综述的关联
- **直接探讨 Module Sequence**：证明子层排列顺序是一个重要的设计自由度
- 突破了"必须交替排列"的固定思维
- 后续 CogView、Brainformers 等工作进一步扩展了这个方向
- 为"Attention 和 FFN 的功能分化"提供了实证支持
