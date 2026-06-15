# Simplifying Transformer Blocks

## 基本信息
- **作者**: Bobby He, Thomas Hofmann
- **年份**: 2023 (ICLR 2024 submission)
- **arXiv**: (已在综述 tex 中引用)
- **关键词**: 简化Transformer, 移除组件, 信号传播理论

## 核心贡献（Module Sequence 维度）
系统性地研究 Transformer 块中哪些组件可以安全移除。

### 1. 可移除的组件
- **跳跃连接 (Skip Connections)**：在某些条件下可以移除
- **Value 和 Projection 参数**：可以简化
- **归一化层**：在特定初始化下可以省略
- 多个子层可以合并

### 2. 信号传播分析
- 使用信号传播理论分析每个组件对梯度流的贡献
- 发现标准 Transformer 中存在冗余组件
- 简化后的模型在保持性能的同时减少参数量

### 3. 简化后的 Transformer
- 训练速度更快
- 参数效率更高
- 证明标准块结构并非不可简化

## 与综述的关联
- Module Sequence 中"减法"方向的代表作
- 与 Zhu et al. 2025 (移除归一化) 互补
- 核心问题：Transformer 块的标准构成中，哪些是真正必要的？

## 注意
此论文已在综述 tex 中引用，此处笔记仅作为 Module Sequence 维度的补充分析。
