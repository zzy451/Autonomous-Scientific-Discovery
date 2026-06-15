# Brainformers: Trading Simplicity for Efficiency

## 基本信息
- **作者**: Yanqi Zhou, Nan Du, Yanping Huang, Daiyi Peng, Chang Lan, Da Huang, Siamak Shakeri, David So, Andrew Dai, Yifeng Lu, Zhifeng Chen, Quoc Le, Claire Cui, Jason Wei, Evgeny Brevdo
- **年份**: 2023 (ICML 2023)
- **arXiv**: 2306.00008
- **机构**: Google
- **关键词**: 异构块, 非均匀架构, 稀疏门控, 架构搜索, MoE

## 核心贡献（Module Sequence 维度）
本文打破了 Transformer "每层结构相同" 的传统设计，提出**异构块** (heterogeneous blocks)，用不同类型的子层组合来构建更高效的模型。这是 Module Sequence 维度上最激进的探索之一。

### 1. 核心动机
- 标准 Transformer 使用**均匀骨架** (uniform backbone)：每个块都是相同的 [Attn → FFN] 结构
- 但没有先验理由认为每层都应该相同
- 类似于人脑不同区域有不同的结构和功能
- 假设：异构设计可能比均匀设计更高效

### 2. Brainformer 块的设计
Brainformer 块由多种子层的**非标准排列组合**构成：
- **稀疏门控 FFN** (Sparsely-gated Feed-Forward): MoE 风格的条件计算
- **密集 FFN** (Dense Feed-Forward): 标准全连接层
- **注意力层** (Attention): 标准多头自注意力
- **多种归一化层**: 在不同位置使用不同的归一化
- **不同激活函数**: 在不同子层使用不同的激活

### 3. 搜索方法
- 使用**架构搜索**来确定最优的子层排列
- 搜索空间包括子层类型、顺序、数量
- 在代理任务上搜索，然后迁移到大规模模型

### 4. 实验结果
- **训练收敛速度提升 2x**: 相比 GLaM 架构
- **每步训练时间缩短 5x**: 对于 8B 激活参数模型
- **SuperGLUE 分数提升 3%**: 在 fine-tuning 评估中
- 在 few-shot 评估中超过 Primer dense 模型

### 5. 关键洞察
- 最优块结构中，Attention 和 FFN 的比例不一定是 1:1
- 某些位置放置稀疏门控层比密集层更高效
- 归一化层的位置和类型也是重要的搜索维度
- 异构设计的收益随模型规模增大而增大

## 与综述的关联
- **Module Sequence 设计空间最大化探索**：
  - Sandwich Transformer 只调整 Attn/FFN 的顺序
  - Primer 只在标准块内部做小修改
  - Brainformers 彻底重新定义了块的组成
- 与 Primer 的对比：Primer 搜索简单修改，Brainformers 搜索完整的异构块
- 挑战了 "简洁就是好" 的设计哲学（与 Simplifying Transformer 形成对比）
- 说明了在足够大的计算预算下，复杂的 Module Sequence 可以显著提升效率
- MoE 组件的引入模糊了 Module Sequence 和条件计算的边界

## 关键对比
| 模型 | 块结构 | 设计理念 |
|------|--------|----------|
| 标准 Transformer | [Attn, FFN] 重复 | 均匀、简洁 |
| Sandwich | [Attn...Attn, Attn-FFN..., FFN...FFN] | 重排现有子层 |
| Primer | [修改的Attn, 修改的FFN] 重复 | 微调子层内部 |
| Brainformers | [各种子层的异构组合] | 完全异构 |

## 局限性
- 搜索代价高昂，需要大量计算资源
- 搜索到的最优架构可能不具备良好的可迁移性（跨任务/跨规模）
- 异构架构增加了工程实现的复杂度
- 难以获得理论解释（为什么某种排列更好？）
- 复现困难：搜索空间巨大，结果可能对搜索细节敏感
