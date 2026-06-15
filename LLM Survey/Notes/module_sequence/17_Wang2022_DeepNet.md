# DeepNet: Scaling Transformers to 1,000 Layers

## 基本信息
- **作者**: Hongyu Wang, Shuming Ma, Li Dong, Shaohan Huang, Dongdong Zhang, Furu Wei
- **年份**: 2022 (arXiv: 2203.00555)
- **关键词**: DeepNorm, 深层Transformer, Post-Norm改进, 1000层

## 核心贡献（Module Sequence 维度）
提出 DeepNorm 方法，使 Post-Norm Transformer 可以稳定扩展到 1000 层。

### 1. 核心思路
- 保持 Post-Norm 结构（因为其潜在性能优势）
- 通过修改残差连接的缩放和初始化来稳定训练
- 残差连接: $x_{l+1} = \text{LN}(\alpha \cdot x_l + G_l(x_l, \theta_l))$
- 其中 $\alpha > 1$ 是深度相关的缩放常数

### 2. 理论保证
- 证明了在特定的 $\alpha$ 和初始化条件下，模型更新是有界的
- 提供了与深度相关的 $\alpha$ 设定公式
- 使得训练1000层 Transformer 成为可能

### 3. 实验结果
- 成功训练 1000 层 Transformer
- 在机器翻译任务上显著优于浅层模型
- 验证了 Post-Norm + 正确缩放可以实现极端深度

## 与综述的关联
- Module Sequence 中 Post-Norm 路线的**极致扩展**
- 与 ADMIN 形成互补：ADMIN 通过初始化策略, DeepNorm 通过残差缩放
- 为 MAGNETO (Foundation Transformers) 提供了基础
- 此论文已在综述 tex 中引用

## 注意
此论文已在综述 tex 中引用，此处笔记仅作为 Module Sequence 维度的补充分析。
