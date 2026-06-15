# Transformer Dynamics: A Neuroscientific Approach to Residual Stream Interpretability

**论文信息**: A neuroscientific approach to interpretability of large language models (2025)
**arXiv**: 2502.12131
**分类**: Interpretability (残差流可解释性 / 动力系统视角)

## 核心思想
将 Transformer 的残差流（residual stream）概念化为一个跨层演化的动力系统（dynamical system）。借鉴神经科学中分析神经活动轨迹的方法，研究残差流中激活值的连续性、密度和吸引子行为，建立"AI 神经科学"的理论基础。

## 关键发现
- **强连续性**: 残差流中单个单元的激活值在相邻层之间表现出强连续性，尽管残差流并非特权基（non-privileged basis）
- **密集轨迹**: 激活值在表征空间中形成密集的演化轨迹，类似于生物神经网络中的神经轨迹
- **吸引子行为（Attractor-like behavior）**: 残差流的演化呈现类吸引子动力学，深层的表征趋向于收敛到特定区域
- **层间动力学**: 不同层对残差流的扰动模式具有可预测的结构

## 方法论
- 将动力系统理论（dynamical systems theory）与机械可解释性（mechanistic interpretability）相结合
- 大规模数据分析验证理论预测
- 跨模型验证动力学特性的普遍性

## 与综述的关联
属于 **Interpretability** 维度的基础性工作。为理解"残差流为何有效"提供了动力系统视角的解释。与 Residual Stream Duality (Note 34) 互补：Duality 从算子等价性角度分析，本文从动力系统角度分析。为残差连接的设计选择（如 Pre-LN vs Post-LN、缩放系数等）提供了动力学层面的理论依据。

## 核心贡献
首次系统性地将神经科学的动力系统分析方法应用于 Transformer 残差流，发现激活值的连续性、密集轨迹和吸引子行为，为"AI 神经科学"奠基。
