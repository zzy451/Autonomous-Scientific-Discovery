# Primer: Searching for Efficient Transformers for Language Modeling
**作者**: David R. So, Wojciech Manke, Hanxiao Liu, Zihang Dai, Noam Shazeer, Quoc V. Le | **年份**: 2021 | **arxiv**: 2109.08668 | **发表**: NeurIPS 2021

## 0. 摘要翻译
本文使用进化搜索（evolutionary search）在 TensorFlow 程序的原语级别搜索空间中，寻找比标准 Transformer 更高效的自回归语言建模架构。搜索发现的 "Primer" 架构的改进主要归结于两个简单修改：Squared ReLU 激活函数和在注意力 QKV 投影后添加深度可分离卷积（Depthwise Convolution）。在 500M 参数规模上，Primer 相比 T5 基线实现了 4 倍训练成本降低。

## 1. 方法动机
- 大规模 Transformer 的训练和推理成本极高
- 手工设计的架构可能不是最优的
- 通过自动化架构搜索，在原语级别（而非高级模块级别）发现更高效的设计
- 目标是找到可以直接"嵌入"现有代码库的简单改进

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### 搜索方法
- 在 TensorFlow 程序的原语级别进行进化搜索
- 搜索空间包括各种基本操作（矩阵乘、非线性、卷积等）
- 不限于传统的 Attn-FFN 结构

### 两个关键发现

#### 1) Squared ReLU（平方 ReLU）
- 将标准 `ReLU(x)` 替换为 `ReLU(x)^2`
- 提供更强的稀疏性和更平滑的梯度
- 后续被 PaLM 等模型中的 SwiGLU/GeGLU 等门控激活函数延续

#### 2) Multi-DConv-Head Attention (MDHA)
- 在注意力的 Q、K、V 投影之后各添加一个 3x1 深度可分离卷积
- 卷积在序列维度上操作，捕获局部位置模式
- 增强了模型对局部特征的归纳偏置

### Primer-EZ
- 仅使用上述两个修改的简化版本
- 可以轻松集成到任何现有 Transformer 代码库中

### 模块结构
```
标准 Transformer:  Q,K,V = Linear(x)
Primer MDHA:       Q,K,V = DConv_3x1(Linear(x))

标准 FFN:          FFN(x) = Linear(ReLU(Linear(x)))
Primer FFN:        FFN(x) = Linear(ReLU(Linear(x))^2)
```

## 3. 与其他方法对比
| 方法 | 修改类型 | 发现方式 | 训练效率提升 |
|------|---------|---------|------------|
| 标准 Transformer | 基线 | 手工设计 | - |
| Evolved Transformer | 整体架构 | NAS | ~1.5x |
| Primer | 原语级别修改 | 进化搜索 | ~4x (500M) |
| Primer-EZ | 两个简单修改 | 提炼 | ~3x (1.9B) |

## 4. 实验表现
- **500M 参数 (C4)**：相比 T5 基线，训练成本降低约 4 倍
- **1.9B 参数**：使用 1/3 训练计算量达到标准 Transformer 同等的 one-shot 性能
- **效率增益随规模增长**：计算规模越大，相对优势越明显（服从幂律关系）
- **跨代码库泛化**：在 T5、GPT 等不同代码库中均有效
- **即插即用**：无需额外超参数调整

## 5. 总结
a) **一句话概括**：通过原语级别进化搜索发现 Squared ReLU 和 Depthwise Convolution 两个简单修改，在不改变整体 Transformer 结构的情况下实现了显著的训练效率提升。

b) **速记 pipeline**：`Input -> [LN -> DConv(QKV) -> Attn -> Add -> LN -> SquaredReLU-FFN -> Add] x L -> Output`
