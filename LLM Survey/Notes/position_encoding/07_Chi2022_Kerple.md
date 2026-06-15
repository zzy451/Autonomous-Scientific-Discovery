# Kerple: Kernelized Relative Positional Embedding
**论文**: KERPLE: Kernelized Relative Positional Embedding for Length Extrapolation
**作者**: Ta-Chung Chi, Ting-Han Fan, Peter J. Ramadge, Alexander I. Rudnicky
**年份**: 2022
**会议**: NeurIPS 2022
**arXiv**: 2205.09921

## 核心思想
将相对位置编码统一到 **条件正定核 (Conditionally Positive Definite, CPD) 核** 的框架下，提出了基于核函数的相对位置编码方法 Kerple，并发现对数变体具有优越的长度外推性能。

## 方法细节

### 核函数框架
- 将位置差异作为核函数的输入
- CPD 核可以通过加常数偏移转换为 PD 核
- 常数偏移被 softmax 归一化隐式吸收

### 统一视角
Kerple 证明了若干现有方法是其特例：
- **ALiBi**: 使用线性核 (|i-j|) 的特例
- **T5 RPE**: 也可纳入该框架

### 对数变体 (Logarithmic Variant)
$$b_{ij} = -r_1 \log(1 + r_2 |i-j|)$$

- r_1, r_2 是可学习参数（per head）
- 对数函数"压平"了远距离的衰减
- 使模型更好地利用远端信息
- 对比 ALiBi 的线性衰减，对数衰减更缓和

### 其他变体
- 幂律变体 (Power variant): $-r_1 |i-j|^{r_2}$
- 指数变体 (Exponential variant): $-r_1 (e^{r_2 |i-j|} - 1)$

## Position Encoding 维度分析

### 分类
- **类型**: Attention Matrix Bias（核函数框架）
- **注入方式**: 在 attention logits 上加偏置
- **参数量**: 每个 head 仅 2 个可学习参数 (r_1, r_2)
- **长度外推**: 对数变体表现优异

### 理论贡献
1. 统一框架：将多种 attention bias 方法纳入核函数视角
2. 证明 CPD 核在 softmax attention 中的合理性
3. 指出核函数形状对长度外推的关键影响

## 实验结果
- OpenWebText2, GitHub, ArXiv 数据集
- 对数变体在长度外推上优于 Sinusoidal, Rotary, T5, ALiBi
- 训练长度 512，测试 8192+ 时保持低困惑度

## 影响
- 提供了理解 attention bias 方法的统一数学框架
- 对数衰减 vs 线性衰减的比较具有重要实践指导意义
- 启发了 FIRE 等后续统一框架
