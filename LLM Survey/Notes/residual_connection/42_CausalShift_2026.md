# Residual Connections and the Causal Shift

**论文信息**: Residual Connections and the Causal Shift (2026)
**arXiv**: 2602.14760
**分类**: Theory (残差连接理论分析 / 因果偏移)

## 核心思想
揭示残差连接与自回归训练目标之间存在微妙的不对齐（misalignment）。残差连接将激活值绑定到当前 token，而监督信号指向下一个 token。这种"因果偏移"（causal shift）可能在当前 token 与下一个 token 信息不匹配时传播错误信息。

## 关键机制
- **因果偏移问题**: 残差连接的恒等映射保留了当前 token 的表征，但 next-token prediction 目标要求模型输出下一个 token 的信息，两者之间存在结构性张力
- **信息传播分析**: 当当前 token 与下一个 token 语义差异大时，残差路径传递的"当前 token 信息"可能干扰预测
- **理论框架**: 形式化分析这种偏移对训练动态和模型性能的影响

## 理论贡献
- 首次明确指出残差连接的恒等映射与自回归目标之间的结构性矛盾
- 解释了为什么某些 token 位置的预测比其他位置更困难
- 为设计更好的残差连接变体提供了新的理论视角

## 与综述的关联
属于 **Theory** 维度的深刻洞察。与 Residual Stream Duality (Note 34) 一起构成残差连接理论分析的最新进展。为理解"为什么需要修改标准残差连接"提供了新的理论动机：不仅是梯度传播和表征坍塌的问题，还有与训练目标的结构性不对齐。

## 核心贡献
发现并形式化分析了残差连接恒等映射与 next-token prediction 目标之间的因果偏移问题，为残差连接设计提供新的理论视角。
