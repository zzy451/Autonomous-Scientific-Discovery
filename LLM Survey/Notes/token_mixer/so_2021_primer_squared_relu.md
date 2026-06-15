# Primer: Searching for Efficient Transformers for Language Modeling
**作者**: David R. So, Wojciech Mańke, Hanxiao Liu, Zihang Dai, Noam Shazeer, Quoc V. Le | **年份**: 2021 | **arxiv**: 2109.08668

## 0. 摘要翻译

通过自动化架构搜索（进化算法），Primer 发现了两个简单但高效的 Transformer 改进：(1) 用 **Squared ReLU** ($\text{ReLU}(x)^2$) 替代标准 ReLU 激活，(2) 在 Q/K/V 投影后添加 **Depthwise Convolution**。这两个修改在语言建模任务上可将达到同等质量所需的计算量减少最多 4.2 倍。

## 1. 方法动机

- **Transformer 效率瓶颈**: 标准 Transformer 虽然效果好，但计算效率有优化空间
- **架构搜索的潜力**: Evolved Transformer (So et al., 2019) 表明 NAS 可以发现更好的 Transformer 变体，但搜索空间和目标函数的选择至关重要
- **简单性优先**: 与 Evolved Transformer 发现的复杂架构不同，Primer 的搜索目标是**训练效率**（而非固定步数的最优质量），结果发现最有效的改进反而极为简单
- **核心发现**: 复杂的架构修改不如几个简单的"即插即用"改动

## 2. 方法设计

### 2.1 Squared ReLU 激活

标准 ReLU:
$$f(x) = \max(0, x)$$

Squared ReLU:
$$f(x) = (\max(0, x))^2 = \text{ReLU}(x)^2$$

**设计效果**:
- 产生**更稀疏**的激活模式：平方操作放大大值、压缩小值
- 激活值的分布更加集中，有利于特征选择
- 梯度 $f'(x) = 2 \cdot \text{ReLU}(x)$，在正值区域梯度与激活值成正比

### 2.2 Depthwise Convolution（注意力中的空间混合）

在 Multi-Head Attention 的 Q、K、V 投影之后各添加一个 kernel size=3 的 depthwise convolution：
```
Input → Linear(Q) → DepthwiseConv1D(k=3) → Q'
Input → Linear(K) → DepthwiseConv1D(k=3) → K'  
Input → Linear(V) → DepthwiseConv1D(k=3) → V'
```

这为注意力引入了局部上下文信息，弥补了纯注意力缺乏局部归纳偏置的不足。

### 2.3 完整 Primer 架构
除上述两个主要改进外，其余结构与标准 Transformer 相同。Primer 的核心贡献在于证明了这两个微小改动的显著效果。

## 3. 对比

### 3.1 Squared ReLU vs. 其他激活函数

| 激活函数 | 公式 | 稀疏性 | 梯度特性 | 训练效率 |
|---------|------|:------:|---------|:-------:|
| ReLU | $\max(0,x)$ | 中 | 常数 (x>0) | 基线 |
| GELU | $x \cdot \Phi(x)$ | 低 | 平滑非单调 | 好 |
| SwiGLU | $\text{Swish}(xW) \odot xV$ | 中 | 门控 | 很好 |
| **Squared ReLU** | $\text{ReLU}(x)^2$ | **高** | 与激活值成正比 | **最好** |

### 3.2 Squared ReLU 在注意力中的应用（Different Activation 视角）

虽然 Primer 原文将 Squared ReLU 用于 **FFN**（Channel Mixer），但后续研究也将其探索为**注意力激活函数**（Token Mixer）：

$$\text{Attn}(Q,K,V) = \text{ReLU}(QK^T / \sqrt{d})^2 \cdot V$$

与 softmax 注意力的对比：
| 特性 | Softmax Attention | Squared ReLU Attention |
|------|:-----------------:|:---------------------:|
| 非负性 | 是 | 是 |
| 行归一化 | 是 | **否** |
| 稀疏性 | 依赖温度 | **天然高稀疏** |
| 全局归一化 | 需要行级 reduce | **逐元素** |
| 线性化潜力 | 难 | **可以用于线性注意力** |

### 3.3 与 Sigmoid Attention 的互补
- Sigmoid Attention: 每个注意力权重独立在 $[0,1]$ 内 → 逐元素，**上界固定**
- Squared ReLU Attention: 每个权重独立在 $[0, +\infty)$ → 逐元素，**无上界但更稀疏**

## 4. 实验

- **语言建模 (LM1B, C4)**: Primer 达到 T5 基线同等质量所需的训练 FLOPS 减少 **4.2 倍**
- **训练效率**: 在 auto-regressive 和 masked LM 设定下均一致有效
- **消融**: Squared ReLU 单独贡献约 **2 倍**效率提升，Depthwise Conv 贡献约 **1.5 倍**
- **迁移性**: 改进在不同模型规模（从小到大）和不同任务上均一致有效
- **简单性**: 实现仅需修改一行激活函数代码

## 5. 总结

### a) 一句话
Primer 通过自动架构搜索发现了 Squared ReLU 激活和 Depthwise Convolution 两个极简改进，在语言建模中实现最高 4.2 倍训练效率提升，其中 Squared ReLU 的高稀疏性使其成为 softmax 注意力的潜在替代激活函数。

### b) 速记 pipeline
```
Primer FFN:  x → Linear → Squared ReLU [ReLU(x)²] → Linear → Output
                                ↑ 比 ReLU/GELU 更稀疏，训练更快

Primer Attention:  Q,K,V → DepthwiseConv1D(k=3) → Standard Attention
                              ↑ 注入局部归纳偏置
```

## 6. 与本综述的关联
- 作为 **Different Activation** 子类别的重要方法，与 Sigmoid Attention 形成互补
- Squared ReLU 的高稀疏性与 MoE 的稀疏激活哲学一脉相承
- Depthwise Conv 的加入预示了后来 Hyena / Mamba 等 CNN-Attention 混合架构的趋势
- 架构搜索发现的简单改进常常被忽视，但实践价值很高

---
**阅读日期**: 2026-04-06
