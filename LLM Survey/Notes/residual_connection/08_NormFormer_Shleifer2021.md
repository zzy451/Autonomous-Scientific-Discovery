# NormFormer: Improved Transformer Pretraining with Extra Normalization

**论文信息**: Shleifer, S., Weston, J., Ott, M. (2021)
**arXiv**: 2110.09456 | **机构**: Meta AI
**分类**: Control (额外归一化点)

## 核心思想
在 Pre-LN Transformer 中发现梯度量级不匹配问题（早期层梯度远大于后期层），通过在残差块内增加归一化点来解决。

## 三个微修改
1. **自注意力后额外 LayerNorm**: 归一化注意力输出
2. **FFN 第一全连接层后额外 LayerNorm**: 归一化 FFN 中间输出  
3. **头级别缩放**: 对每个注意力头的输出施加可学习缩放因子

## 关键结果
- 参数增加仅 **0.4%-0.5%**，计算开销可忽略
- 1.3B 参数模型达到目标困惑度速度提升 **24%**
- 达到 GPT-3 Large 零样本性能速度提升 **60%**
- 适用于 CLM 和 MLM

## 与综述的关联
属于 **Control** 维度。NormFormer 的核心洞察：残差连接中不同位置的信号量级差异很大，额外归一化点可以"平衡"梯度流。

与其他工作的关系:
- 与 Sandwich-LN (CogView) 类似的思路但更系统
- 比 DeepNorm 更轻量但适用范围更窄
- 补充了 Pre-LN vs Post-LN 的讨论

## 核心贡献
通过分析残差块内部的梯度分布，提出精准的额外归一化位置，以极小代价显著加速收敛。
