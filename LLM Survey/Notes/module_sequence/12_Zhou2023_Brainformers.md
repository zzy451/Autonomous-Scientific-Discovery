# Brainformers: Trading Simplicity for Efficiency

## 基本信息
- **作者**: Yanqi Zhou, Nan Du, Yanping Huang, Daiyi Peng, Chang Lan, Da Huang, Siamak Shakeri, David So, Andrew Dai, Yifeng Lu, Zhifeng Chen, Quoc Le, Claire Cui, James Laudon, Jeff Dean
- **年份**: 2023 (arXiv: 2306.00802)
- **关键词**: 异构块设计, 架构搜索, MoE, 非均匀Transformer

## 核心贡献（Module Sequence 维度）
探索**非均匀**的 Transformer 块设计，用架构复杂度换取计算效率。

### 1. 核心理念
- 标准 Transformer 使用完全**均匀**的块结构：所有层都是相同的 Attention + FFN
- Brainformers 认为这种均匀性不是最优的
- 提出使用**异构块** (heterogeneous blocks)——不同层使用不同组件组合

### 2. 搜索空间
- 块内组件包括：
  - 稀疏 FFN (MoE 层) + 不同的门控机制
  - 稠密 FFN
  - Attention 层
  - 不同形式的 LayerNorm
  - 不同激活函数
- 使用 NAS 或手动探索在这个空间中搜索最优配置

### 3. 性能
- 8B 激活参数的 Brainformer 训练收敛速度是 GLaM 的 2x
- 推理速度提升 5x
- SuperGLUE 分数提升 3%
- 在 few-shot 任务上优于 Primer 等稠密模型

### 4. 关键发现
- 不同位置的层应该有不同的组件配置
- 最优配置不是均匀的 Attention + FFN 交替
- 某些位置适合用 MoE，某些位置用稠密 FFN

## 与综述的关联
- **Module Sequence 的极致探索**：完全打破均匀块的假设
- 从"选择一种排列方式"扩展到"每一层都可以不同"
- 与 Sandwich Transformer 的理念一脉相承但更激进
- 代表了"架构搜索驱动的 Module Sequence 设计"方向
- 成本很高，实际部署中较少使用
