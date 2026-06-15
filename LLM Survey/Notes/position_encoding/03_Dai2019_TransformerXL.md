# Transformer-XL: Relative Positional Encoding
**论文**: Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context
**作者**: Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, Ruslan Salakhutdinov
**年份**: 2019
**会议**: ACL 2019
**arXiv**: 1901.02860

## 核心思想
Transformer-XL 引入 segment-level recurrence 来建模超长上下文。为解决跨 segment 复用 hidden states 时的"时间混淆"问题，设计了新的相对位置编码方案。

## 方法细节

### 问题: 时间混淆 (Temporal Confusion)
- 使用 segment-level recurrence 时，不同 segment 的 token 如果使用绝对位置编码，会得到相同的位置表示
- 模型无法区分 "当前 segment 的位置 0" 和 "前一个 segment 的位置 0"

### 解决方案: 相对位置编码
将位置信息从输入 embedding 移到 attention score 计算中：

$$A_{i,j} = \underbrace{E_{x_i}^T W_q^T W_{k,E} E_{x_j}}_{(a)} + \underbrace{E_{x_i}^T W_q^T W_{k,R} R_{i-j}}_{(b)} + \underbrace{u^T W_{k,E} E_{x_j}}_{(c)} + \underbrace{v^T W_{k,R} R_{i-j}}_{(d)}$$

四个分项：
- (a) content-based addressing: 纯内容交互
- (b) content-dependent positional bias: 内容依赖的位置偏置
- (c) global content bias: 全局内容偏置（用可学习向量 u 替代绝对位置查询）
- (d) global positional bias: 全局位置偏置（用可学习向量 v）

### 关键设计
- 使用固定 sinusoidal encoding 作为 R_{i-j}（但通过可学习投影矩阵 W_{k,R}）
- u, v 是全局可学习向量，跨所有位置共享
- 不再在输入层添加位置编码

## Position Encoding 维度分析

### 分类
- **类型**: Relative Position Encoding（attention score 分解）
- **注入方式**: 直接修改 attention logits
- **参数量**: W_{k,R}, u, v 可训练; R_{i-j} 使用固定 sinusoidal
- **长度外推**: 因为只依赖相对距离，理论上可泛化到任意长度

### 与 Shaw et al. 2018 的区别
1. 更系统的 attention score 分解（4 项 vs 2 项修改）
2. 引入全局偏置 u, v
3. 与 segment-level recurrence 配合

## 影响
- 相对位置编码范式的重要确立
- 影响了后续 XLNet、DeBERTa 等模型
- "在 attention 中注入位置"的思路被 RoPE、ALiBi 继承
