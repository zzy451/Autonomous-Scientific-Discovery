# Ablate and Rescue: A Causal Analysis of Residual Stream Hyper-Connections

**论文信息**: Peng, W. G., et al. (2026)
**arXiv**: 2603.14833
**分类**: Interpretability / Width (残差流可解释性分析)

## 核心思想
多流（multi-stream）Transformer 架构（如 Hyper-Connections）通过允许多条并行残差流来缓解表征坍塌和梯度消失问题。本文提出系统性的"消融-拯救"（ablate-and-rescue）因果分析框架，直接在推理阶段对各残差流进行因果比较，揭示不同流的功能分工。

## 关键机制
- **Stream Ablation**: 在推理时选择性地消融（置零/冻结）特定残差流，观察模型输出变化
- **Rescue Framework**: 在消融某流后，用另一条流的信息"拯救"模型性能，从而建立流间的因果关系
- **直接因果比较**: 不依赖梯度或探针，而是通过干预实验直接测量各流的因果贡献

## 实验结果
- 揭示了 Hyper-Connections 中不同残差流承担不同功能角色
- 某些流主要负责低层特征传递，另一些负责高层语义整合
- 为多流架构的设计提供了可解释性指导

## 与综述的关联
属于 **Interpretability** 维度的重要工作。是对 Hyper-Connections (Note 19) 和 mHC (Note 20) 的可解释性补充。将机械可解释性方法应用于残差连接架构分析，连接了"残差流设计"与"残差流理解"两个方向。

## 核心贡献
首次对多流残差架构进行系统性因果分析，提出 ablate-and-rescue 框架，揭示不同残差流的功能分工。
