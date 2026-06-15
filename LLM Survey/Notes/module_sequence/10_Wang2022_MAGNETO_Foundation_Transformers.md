# Foundation Transformers (MAGNETO / Sub-LN)

## 基本信息
- **作者**: Hongyu Wang, Shuming Ma, Shaohan Huang, Li Dong, Wenhui Wang, Zhiliang Peng, Yu Wu, Payal Bajaj, Saksham Singhal, Alon Benhaim, Barun Patra, Zhun Liu, Vishrav Chaudhary, Xia Song, Furu Wei
- **年份**: 2022 (ICML 2023)
- **arXiv**: 2210.06423
- **关键词**: Sub-LN, MAGNETO, 通用基础架构, 训练稳定性

## 核心贡献（Module Sequence 维度）
提出 Sub-LN (Sub-Layer Normalization)，一种在子层**内部**添加额外 LayerNorm 的方案。

### 1. 动机
- Post-LN (BERT 风格) 训练不稳定
- Pre-LN (GPT 风格) 稳定但性能有限
- 目标：创建一个跨模态（语言、视觉、语音）通用的"基础 Transformer"

### 2. Sub-LN 结构
- 在子层（Multi-Head Attention / FFN）的**内部**添加 LayerNorm
- 具体位置：输入投影前 + 输出投影前
- 与 Pre-LN 和 Post-LN 都不同——归一化在子层计算的"中间"

### 3. 与 DeepNet 的关系
- 使用 DeepNet (Wang et al., 2022) 的初始化策略
- 提供训练稳定性的理论保证
- 可以扩展到大规模模型

### 4. 实验结果
- 实现仅需对标准 Transformer 做最小代码修改
- 在语言（BERT/GPT 风格）、视觉（ViT）、语音任务上均优于 Pre-LN 和 Post-LN
- 展示了跨模态的通用性

## 与综述的关联
- 提供了 Module Sequence 设计的"第三条路"：不只是 Pre/Post，还可以在子层内部放 Norm
- 与 NormFormer 思路类似但更系统化
- 是 DeepNet 系列工作的延续
- 代表了"归一化位置 + 初始化策略"的联合设计思路
