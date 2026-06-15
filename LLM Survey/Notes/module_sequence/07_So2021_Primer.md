# Primer: Searching for Efficient Transformers for Language Modeling

## 基本信息
- **作者**: David R. So, Wojciech Mańke, Hanxiao Liu, Zihang Dai, Noam Shazeer, Quoc V. Le
- **年份**: 2021 (NeurIPS 2021)
- **arXiv**: 2109.08668
- **关键词**: 架构搜索, 高效Transformer, Squared ReLU, 深度卷积

## 核心贡献（Module Sequence 维度）
使用神经架构搜索 (NAS) 在 Transformer 块设计空间中寻找更高效的变体。

### 1. 方法
- 在 Transformer 的模块设计空间中进行系统搜索
- 搜索空间包括子层类型、排列顺序、激活函数等
- 以语言建模效率为优化目标

### 2. Primer 的两个关键发现
1. **Squared ReLU**: 用 $\text{ReLU}^2$ 替代标准 ReLU
   - 产生更稀疏的激活
   - 提升语言建模性能
2. **Depthwise Convolution after QKV**: 在 Q, K, V 投影后各加一层深度卷积
   - 引入局部信息
   - 类似于对每个头的特征进行局部平滑

### 3. 效率收益
- 训练成本降低 3x-4x
- 效率增益随计算规模增大而增大
- 不改变基本的 Module Sequence 结构，而是优化子层内部

## 与综述的关联
- 展示了通过 NAS 自动发现 Module Sequence 变体的方法论
- 发现的改进（如 depthwise conv after projection）本质上是在现有子层内部插入新组件
- 与 Brainformers 形成对比：Primer 搜索简单修改，Brainformers 搜索复杂的异构块
- 说明 Module Sequence 的设计空间远大于人工探索的范围
