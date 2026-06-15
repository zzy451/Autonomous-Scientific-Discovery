# Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models

**论文信息**: Raposo, D., et al. (2024)
**arXiv**: 2404.02258 | **机构**: Google DeepMind
**分类**: Depth (动态深度/条件计算)

## 核心思想
并非所有 token 在每一层都需要完整计算。通过路由机制让部分 token 跳过某些层（仅走残差连接），实现 FLOP 的动态分配。

## 关键机制
1. **路由器**: 每层一个路由器，为每个 token 计算重要性分数
2. **Top-k 选择**: 选择 k 个最重要的 token 通过完整的 Attention+FFN
3. **旁路**: 未选中的 token 通过**恒等残差连接**直接传递
4. **静态计算图**: k 固定，张量大小确定，兼容标准硬件

## 与残差连接的关系
MoD 直接利用残差连接作为"跳过"路径：
- 被选中的 token: x_{l+1} = x_l + F_l(x_l)  (完整计算)
- 被跳过的 token: x_{l+1} = x_l            (纯残差)

残差连接不仅是训练工具，更是**推理效率的基础设施**。

## 实验结果
- 与基线 Transformer 性能相当，FLOP 更少
- 推理速度最高提升 **50%**
- 可与 MoE 结合为 MoDE (Mixture-of-Depths-and-Experts)

## 与综述的关联
属于 **Depth** 维度的代表性工作。将残差连接从被动的训练稳定工具转变为主动的计算分配机制：
- 层不再是必须执行的，而是可选的
- 残差连接成为"快速通道"
- 深度变成了"按需分配"的资源

## 核心贡献
将残差连接重新定义为动态计算图的核心组件，开创了深度维度的条件计算范式。
