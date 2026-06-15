# NormFormer: Improved Transformer Pretraining with Extra Normalization

## 基本信息
- **作者**: Sam Shleifer, Jason Weston, Myle Ott
- **年份**: 2022 (arXiv: 2110.09456)
- **关键词**: NormFormer, 额外归一化, 梯度幅度不匹配

## 核心贡献（Module Sequence 维度）
在标准 Pre-LN Transformer 中插入额外的归一化层，解决梯度幅度不匹配问题。

### 1. 问题诊断：梯度幅度不匹配
- Pre-LN Transformer 在大规模预训练时，早期层梯度显著大于后期层
- 导致早期层"过度训练"，后期层"训练不足"
- 标准 Pre-LN 的归一化不足以均衡各层的梯度分布

### 2. 三个针对性修改
1. **Attention 后加 LayerNorm**: 在 self-attention 子层输出后加额外 LN
2. **FFN 第一层后加 LayerNorm**: 在 FFN 的第一个线性层后加额外 LN
3. **Head-wise Scaling**: 每个注意力头的输出乘以可学习的标量参数

### 3. 效果
- 额外参数极少（+0.4%~0.5%）
- 计算速度几乎无影响
- 模型收敛速度最多提升 40%
- 在 GLUE 等下游任务上提升 fine-tuned 性能
- 三个操作缺一不可——去掉任何一个都退回 baseline

## 与综述的关联
- 展示了在 Transformer 块内部"哪里放归一化"是一个重要的设计选择
- 与 CogView Sandwich-LN 形成互补：Sandwich-LN 关注数值稳定性，NormFormer 关注梯度均衡
- 说明 Module Sequence 不仅仅是"Pre vs Post"的二元选择，还包括更细粒度的归一化位置选择
