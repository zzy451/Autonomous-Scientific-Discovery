# FuseNorm: Achieving the Best of Both Worlds from PreNorm and PostNorm
**作者**: (OpenReview submission) | **年份**: 2025 | **发表**: ICLR 2025 submission | **链接**: https://openreview.net/forum?id=azXOzJFwuf

## 0. 摘要翻译
FuseNorm 旨在融合 PreNorm 和 PostNorm 的优势。它采用 PreNorm 的干净残差路径（clean residual path）来稳定信号传播，同时使用 PostNorm 风格的计算——对残差连接的输出进行归一化——从而增强表示能力。这种设计在保持训练稳定性的同时，恢复了 PostNorm 的性能优势。

## 1. 方法动机
- PreNorm 训练稳定但存在"表示塌缩"（representation collapse）问题：深层的残差流逐渐被未归一化的跳跃连接主导，导致各层贡献被稀释
- PostNorm 表示能力更强但训练不稳定，容易梯度爆炸
- 已有方法（如 DeepNorm、Admin）通过缩放因子缓解问题，但未从结构上统一两者
- 需要一种结构性方案，同时获得 PreNorm 的稳定性和 PostNorm 的表达力

## 2. 方法设计

### 核心思想：双重归一化路径
- **残差路径**：保持 PreNorm 的干净残差连接 `x + SubLayer(LN(x))`，确保梯度可以无阻碍地反向传播
- **输出归一化**：在残差相加之后，额外施加一次 PostNorm 风格的归一化，使每层输出的统计特性得到规范化

### 结构示意
```
x -> LN -> SubLayer -> + x -> LN_post -> output
     (PreNorm路径)    (残差)  (PostNorm风格)
```

### 关键设计点
- 干净残差路径保证了训练稳定性（梯度不会因归一化而被截断）
- PostNorm 风格的输出归一化防止了 PreNorm 的表示稀释问题
- 两次归一化的组合使得每层既能稳定训练，又能保持有效的表示更新

## 3. 与其他方法对比
| 方法 | 残差路径 | 输出归一化 | 训练稳定性 | 表示能力 |
|------|---------|-----------|-----------|---------|
| PreNorm | 干净 | 无 | 高 | 较弱（深层稀释） |
| PostNorm | 被LN截断 | 有 | 低 | 强 |
| DeepNorm | 缩放残差 | 有 | 中高 | 中高 |
| FuseNorm | 干净 | 有 | 高 | 强 |

## 4. 实验表现
- 在语言建模和机器翻译任务上，FuseNorm 同时优于 PreNorm 和 PostNorm
- 训练稳定性与 PreNorm 相当，无需 warm-up 或特殊初始化
- 最终性能接近或超过精调的 PostNorm

## 5. 总结
a) **一句话概括**：FuseNorm 通过保留 PreNorm 的干净残差路径并叠加 PostNorm 风格的输出归一化，结构性地统一了两种范式的优势。

b) **速记 pipeline**：`x -> [LN -> SubLayer -> +x -> LN] -> ... -> Output`（双重归一化：子层前 + 残差后）
