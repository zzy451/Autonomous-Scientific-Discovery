# Residual Stream Duality in Modern Transformer Architectures

**论文信息**: Residual Stream Duality in Modern Transformer Architectures (2026)
**arXiv**: 2603.16039
**分类**: Theory / Interpretability (残差流对偶性理论)

## 核心思想
Transformer 解码器沿两个有序维度演化信息：序列位置（sequence position）和层深度（layer depth）。本文提出"残差流对偶性"：沿深度方向的因果残差注意力读取，在算子层面与沿序列方向的短滑动窗口注意力完全等价。这一对偶视角为统一理解各种残差连接变体提供了理论框架。

## 关键机制
- **双轴视角（Two-Axis View）**: 将 Transformer 视为在序列轴和深度轴上同时演化的系统
- **算子等价性**: 证明深度方向的因果残差读取 = 序列方向的局部滑动窗口注意力
- **统一设计空间**: 通过对偶性将 DenseFormer、Hyper-Connections、Cross-Layer Attention 等方法纳入统一框架

## 理论贡献
- 建立了深度维度和序列维度之间的形式化对偶关系
- 解释了为什么跨层注意力（Cross-Layer Attention）和密集连接（Dense Connections）有效
- 为设计新的残差连接变体提供了理论指导

## 与综述的关联
属于 **Theory** 维度的核心工作。提供了一个统一的理论框架来理解本综述中涉及的多种残差连接变体（DenseFormer Note 23、Cross-Layer Attention Note 15、Hyper-Connections Note 19 等）。对偶性视角是组织综述 taxonomy 的重要理论支撑。

## 核心贡献
提出残差流对偶性理论，证明深度方向残差读取与序列方向滑动窗口注意力的算子等价性，为统一理解残差连接设计空间提供理论基础。
