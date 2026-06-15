# On Layer Normalization in the Transformer Architecture
**作者**: Ruibin Xiong, Yunchang Yang, Ji He, Kai Zheng, Shuxin Zheng, Chen Xing, Huishuai Zhang, Yanyan Lan, Liwei Wang, Tie-Yan Liu | **年份**: 2020 | **arxiv**: 2002.04745 | **发表**: ICML 2020

## 0. 摘要翻译
本文研究了 Transformer 架构中层归一化（Layer Normalization）的放置位置问题。作者利用均场理论（mean field theory）分析了原始 Post-LN Transformer 在初始化阶段的梯度行为，发现靠近输出层的参数梯度过大，这是训练不稳定、需要学习率预热（warm-up）的根本原因。作者证明了 Pre-LN Transformer（将 LN 置于残差块内部、子层之前）在初始化时具有良好的梯度行为，因此可以省去学习率预热阶段，同时获得可比的性能。

## 1. 方法动机
- 原始 Transformer（Post-LN）在训练时必须使用学习率 warm-up，否则训练会发散
- 学习率 warm-up 引入了额外的超参数，增加了调参难度
- 需要从理论上解释 warm-up 的必要性，并寻找无需 warm-up 的替代方案

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### Post-LN（原始 Transformer）
- 结构：`x -> SubLayer -> Add -> LayerNorm`
- 即 LN 放在残差连接之后
- **问题**：通过均场理论证明，初始化时靠近输出层的参数梯度量级远大于内部层，导致大学习率下训练不稳定

### Pre-LN（本文重点推荐）
- 结构：`x -> LayerNorm -> SubLayer -> Add`
- 即 LN 放在残差块内部、子层（Attention/FFN）之前
- 最终输出前增加一个额外的 LN
- **理论保证**：初始化时梯度在各层间保持良好的量级，不会出现梯度爆炸
- **实际效果**：可以直接使用较大学习率训练，无需 warm-up

### 关键理论结果
- Post-LN 中，最后一层的梯度量级为 O(d * L)，其中 d 为模型维度，L 为层数
- Pre-LN 中，各层梯度量级保持 O(d) 的一致水平

## 3. 与其他方法对比
| 方法 | LN 位置 | 训练稳定性 | 需要 warm-up | 最终性能 |
|------|---------|-----------|-------------|---------|
| Post-LN | 残差后 | 低（梯度爆炸风险） | 是 | 较高（如果训练成功） |
| Pre-LN | 残差内（子层前） | 高 | 否 | 可比（略低于精调的 Post-LN） |

- Post-LN 在训练成功的情况下通常能达到更好的表示能力
- Pre-LN 牺牲了少量性能换取训练稳定性，成为后续大模型的默认选择（如 GPT 系列）

## 4. 实验表现
- **IWSLT14 De-En**：Pre-LN 无 warm-up 达到与 Post-LN + warm-up 可比的 BLEU
- **WMT14 En-De**：Pre-LN 在无 warm-up 情况下收敛更快
- **BERT 预训练**：Pre-LN 可以省去 warm-up 而不损失下游任务性能
- 训练速度方面，Pre-LN 收敛更快（减少了 warm-up 阶段的时间浪费）

## 5. 总结
a) **一句话概括**：通过均场理论证明 Post-LN 梯度爆炸是 warm-up 必要性的根因，Pre-LN 通过将 LN 移至子层前解决了这一问题。

b) **速记 pipeline**：`Input -> [LN -> Attn -> Add] -> [LN -> FFN -> Add] -> ... -> LN -> Output`（Pre-LN 结构）
