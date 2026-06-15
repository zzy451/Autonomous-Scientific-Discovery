# XPOS: Extrapolatable Position Embedding
**论文**: A Length-Extrapolatable Transformer
**作者**: Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, Furu Wei
**年份**: 2023
**会议**: ACL 2023
**arXiv**: 2212.10554

## 核心思想
XPOS 在 RoPE 的基础上引入 **指数衰减因子**，使旋转位置编码具备更好的长度外推能力。同时提出 blockwise causal attention 辅助提升"注意力分辨率"。

## 方法细节

### RoPE 的问题
- RoPE 在训练长度内表现优异
- 但超出训练长度时，attention score 不稳定
- 高频旋转维度在长距离时振荡过大

### XPOS 的解决方案
在 RoPE 的旋转矩阵中加入指数衰减：

对于 query 位置 m 和 key 位置 n：
$$q_m = x_m \cdot \gamma^m \cdot e^{im\theta}$$
$$k_n = x_n \cdot \gamma^{-n} \cdot e^{in\theta}$$

attention score 中出现：
$$\gamma^{m-n} \cdot e^{i(m-n)\theta}$$

- gamma 是 per-dimension 的衰减率
- 高频维度衰减更快，低频维度衰减更慢
- 效果：稳定化长距离 attention score

### Attention Resolution
- 定义为模型区分不同相对位置的能力
- XPOS 通过指数衰减提高 attention resolution
- Blockwise causal attention 进一步提升

### Blockwise Causal Attention
- 将长序列分为固定大小的 block
- 在 block 内使用全 attention，block 间使用聚合表示
- 相当于一种分层 attention 机制

## Position Encoding 维度分析

### 分类
- **类型**: Relative Position Encoding（RoPE 扩展）
- **注入方式**: 在 Q, K 上施加旋转 + 指数衰减
- **参数量**: 衰减率可固定或可学习
- **长度外推**: 显著优于原始 RoPE

### 与 RoPE 的关系
- XPOS 是 RoPE 的严格泛化
- 当 gamma = 1 时退化为 RoPE
- 指数衰减类似于为 attention 添加了"遗忘"机制

### 与其他方法的关系
- 类似 ALiBi 的距离衰减思想，但融入了 RoPE 的旋转框架
- Forgetting Transformer 也使用了类似的"遗忘"概念
- RetNet 后来也采用了类似的指数衰减 + 旋转编码

## 实验结果
- 训练长度 1024/2048，可外推到 8x-16x
- 在语言建模任务上优于 RoPE、ALiBi

## 影响
- 启发了 RetNet、GLA 等后续工作中的衰减机制
- 表明 RoPE + 衰减是一个有效的组合方向
