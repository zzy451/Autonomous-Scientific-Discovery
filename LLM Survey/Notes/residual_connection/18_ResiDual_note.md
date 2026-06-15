# ResiDual: Transformer with Dual Residual Connections (Pre-Post-LN)

**论文信息**: (见原文已引用 Mak & Flanigan 2025)
**arXiv**: 2304.14802 | **会议**: ICLR 2024
**分类**: Control (双残差路径)

## 说明
此论文已在综述 tex 中引用。补充笔记要点：

## 核心思想
同时维护两条残差路径：
- 一条类似 Pre-LN: 保证梯度流
- 一条类似 Post-LN: 保持表示多样性

## 与其他 Control 方法的关系
- DeepNorm: 修改 Post-LN 的缩放
- ResiDual: 同时使用两种残差路径
- Admin: 自适应调节残差权重

ResiDual 的创新在于：不是选择 Pre-LN 或 Post-LN，而是两者并行。

## 与综述的关联
已列入 Control 子维度。是 Pre-LN vs Post-LN 争论的最新解答之一。
