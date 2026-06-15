# Evolving Normalization-Activation Layers
**作者**: Hanxiao Liu, Andrew Brock, Karen Simonyan, Quoc V. Le | **年份**: 2020 | **arxiv**: 2004.02967

## 0. 摘要翻译

归一化层和激活函数是现代深度网络的关键组件，但它们的设计长期依赖手工经验。本文提出使用**进化搜索** (evolutionary search) 联合搜索归一化和激活函数的最优组合，构建统一的搜索空间并发现了新的归一化-激活层 EvoNorm。EvoNorm 系列中的最佳层在图像分类、目标检测和实例分割等任务上超越了 BN+ReLU、GN+ReLU 等手工设计组合，特别是在 batch 统计量不可用的场景中表现突出。

## 1. 方法动机

### a) 为什么
归一化（如 BN、GN、LN）和激活函数（如 ReLU、Swish）在网络中通常是**紧邻**使用的——先归一化，再激活。二者的设计一直是独立进行的，但它们的功能可能存在重叠和互补。联合设计可能发现更优的组合。

### b) 痛点
- 手工设计的 BN+ReLU 组合虽然广泛使用，但并非经过系统优化
- BN 依赖 batch 统计量，在小 batch 或推理时不稳定
- GN 不依赖 batch，但性能通常低于 BN
- 归一化和激活函数的选择空间庞大，人工难以穷举

### c) 假设
归一化和激活函数可以被统一到一个由基本运算组成的计算图中，通过自动化搜索可以发现超越手工设计的归一化-激活层。

## 2. 方法设计

### a) Pipeline
1. 定义基本运算原语集合（加、乘、除、sigmoid、方差、均值等）
2. 将归一化-激活层表示为由原语构成的有向无环计算图 (DAG)
3. 使用进化算法在搜索空间中探索，以训练精度和速度为适应度
4. 筛选出性能最优的层，验证泛化能力

### b) 模块

**搜索空间**: 包含以下基本原语
- 一元运算: $x^2$, $\sqrt{x}$, $\text{sigmoid}(x)$, $-x$, $|x|$ 等
- 二元运算: $x+y$, $x \times y$, $x / y$, $\max(x,y)$ 等
- 统计运算: $\text{var}(x)$, $\text{mean}(x)$（跨 batch 或跨通道）
- 搜索空间覆盖 BN+ReLU、GN+Swish 等已知组合

**搜索发现的代表层**:

**EvoNorm-B0**（依赖 batch 统计）:
$$\text{EvoNorm-B0}(x) = x \cdot \text{sigmoid}\left(\frac{x}{v(x)}\right)$$
其中 $v(x)$ 是跨 batch 的方差统计

**EvoNorm-S0**（不依赖 batch 统计，sample-based）:
$$\text{EvoNorm-S0}(x) = x \cdot \text{sigmoid}\left(\frac{x}{\text{GroupStd}(x)}\right)$$
其中 GroupStd 是组内标准差（类似 GroupNorm）

### c) 公式
- EvoNorm-B0 和 EvoNorm-S0 均融合了归一化和激活功能
- 不再需要分别写 Norm + Activation，而是一个统一的操作
- 关键观察: sigmoid 项起到"门控"作用，方差/标准差项起到"归一化"作用

## 3. 对比

| 方法 | 归一化 | 激活 | batch 依赖 | ImageNet 精度 |
|------|--------|------|-----------|--------------|
| BN + ReLU | BN | ReLU | 是 | 基线 |
| GN + ReLU | GN | ReLU | 否 | 低于 BN |
| **EvoNorm-B0** | 融合 | 融合 | 是 | **超过 BN** |
| **EvoNorm-S0** | 融合 | 融合 | 否 | **超过 GN** |

## 4. 实验

- **ImageNet 分类**: EvoNorm-B0 在 ResNet-50 上超过 BN+ReLU
- **EvoNorm-S0**: 在不依赖 batch 统计的约束下，超过 GN+ReLU，缩小与 BN 的差距
- **COCO 目标检测与实例分割**: 迁移到下游任务后仍保持优势
- **MobileNet/EfficientNet**: 在轻量级架构上也有效
- **搜索到的层具有可迁移性**: 在小代理任务上搜索，可直接迁移到大任务

## 5. 总结

### a) 一句话
EvoNorm 通过进化搜索发现了融合归一化与激活功能的新层，证明手工设计的 BN+ReLU 等组合并非最优，为自动化归一化设计开辟了方向，但在 LLM 中尚未被广泛采用。

### b) 速记 pipeline
```
定义原语集合 → 构建计算图搜索空间 → 进化搜索 → EvoNorm-B0/S0
EvoNorm-S0: x * sigmoid(x / GroupStd(x))  ← 融合归一化 + 激活
```

---
**阅读日期**: 2026-04-06
