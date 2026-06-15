# Mix-LN: Unleashing the Power of Deeper Layers by Combining Pre-LN and Post-LN

## 基本信息
- **作者**: Pengxiang Li, Lu Yin, Shiwei Liu
- **年份**: 2024 (arXiv: 2412.13795)
- **arXiv**: 2412.13795
- **关键词**: Mix-LN, Pre-LN, Post-LN, 混合归一化, 深层激活, 梯度均衡

## 核心贡献（Module Sequence 维度）
本文提出 Mix-LN，一种在同一模型中**混合使用 Pre-LN 和 Post-LN** 的归一化策略，解决了 Pre-LN 深层网络中"深层退化"问题。是 Module Sequence 中归一化位置选择的最新进展。

### 1. 问题诊断：深层退化
- 现代 LLM (GPT, LLaMA 等) 普遍使用 **Pre-LN**
- Pre-LN 训练稳定，但存在**深层梯度范数衰减**问题
- 深层对最终性能贡献极小——甚至可以被剪枝而不显著损失性能
- 这意味着大量参数（深层的）被"浪费"了

### 2. Pre-LN vs Post-LN 的互补性
| 属性 | Pre-LN | Post-LN |
|------|--------|---------|
| 训练稳定性 | 高 | 低 |
| 浅层梯度 | 正常 | 可能消失 |
| 深层梯度 | 衰减 | 保持较大 |
| 深层贡献 | 弱 | 强 |

- **核心洞察**: Pre-LN 和 Post-LN 的梯度分布问题恰好互补
- Pre-LN 的深层梯度小 → Post-LN 的深层梯度大
- Post-LN 的浅层梯度不稳定 → Pre-LN 的浅层梯度稳定

### 3. Mix-LN 方案
- **浅层使用 Post-LN**：保持深层梯度的流动
- **深层使用 Pre-LN**：确保训练稳定性
- 转换点通过超参数控制（例如：前 25% 用 Post-LN，后 75% 用 Pre-LN）
- 实现为简单的"即插即用"替换，无需其他架构修改

### 4. 实验效果
- **预训练 perplexity 显著降低**
- **SFT (Supervised Fine-Tuning) 性能提升**
- **RLHF 阶段也有改善**
- **无额外参数成本**：只是改变了 LN 的位置
- 所有层的梯度范数分布更加均匀

## 与综述的关联
- **Pre-LN vs Post-LN 争论的"第三条路"**：不是二选一，而是混合使用
- 与 Xiong et al. 2020 的理论分析直接相关：基于 Pre/Post-LN 各自的梯度特性
- 与 DeepNet 的理念不同：DeepNet 修改 Post-LN 的缩放，Mix-LN 在层间切换 LN 类型
- 说明了 Module Sequence 中归一化位置不必全局统一——可以**逐层定制**
- 实用性强：可以直接应用于现有 LLM 架构，改动极小

## 关键公式
- Pre-LN 层: $y = x + F(\text{LN}(x))$
- Post-LN 层: $y = \text{LN}(x + F(x))$
- Mix-LN: 层 $l < l^*$ 使用 Post-LN，层 $l \geq l^*$ 使用 Pre-LN
  - $l^*$ 为转换点，通常设为总层数的 25%

## 局限性
- 转换点 $l^*$ 是一个需要调节的超参数，最优值可能因模型/任务而异
- 转换点处的梯度不连续性是否会造成问题尚需更多研究
- 主要在中等规模模型上验证（~7B），超大规模的效果不确定
- Post-LN 部分仍可能需要 learning rate warmup 等稳定性技巧
