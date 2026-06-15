# Self-Attention with Relative Position Representations
**论文**: Self-Attention with Relative Position Representations
**作者**: Peter Shaw, Jakob Uszkoreit, Ashish Vaswani
**年份**: 2018
**会议**: NAACL 2018
**arXiv**: 1803.02155

## 核心思想
扩展 self-attention 机制，显式引入 token 之间的相对距离信息，而非依赖绝对位置编码。这是最早的相对位置编码工作之一。

## 方法细节

### 核心修改
在 self-attention 中引入可学习的相对位置表示：
- 修改 attention score: 在 Q*K^T 中加入相对位置嵌入
- 修改 value 加权: 在加权求和中也加入相对位置嵌入
- 引入 clipping 机制: 设最大相对距离 k，超过 k 的距离统一处理

### Clipping 策略
$$a_{ij}^K = w_{clip(j-i, k)}^K$$
$$clip(x, k) = \max(-k, \min(k, x))$$

- 减少参数量（只需 2k+1 个位置嵌入）
- 假设超过一定距离后精确相对位置不重要
- 有助于长度泛化

### 与 Absolute PE 的关系
- 实验发现: 组合 relative PE 和 absolute PE 没有进一步提升
- 暗示 relative PE 已包含 absolute PE 的有效信息

## Position Encoding 维度分析

### 分类
- **类型**: Relative Position Encoding（首创性工作）
- **注入方式**: 修改 attention score 和 value 聚合
- **参数量**: 需学习 (2k+1) 个 d_model 维的嵌入向量
- **长度外推**: clipping 机制有助于泛化

### 关键贡献
1. 首次在 Transformer self-attention 中引入相对位置
2. clipping 策略影响了后续大量工作
3. 框架可泛化为 "relation-aware self-attention"

## 实验结果
- WMT 2014 EN-DE 翻译: 优于 absolute PE
- WMT 2014 EN-FR 翻译: 优于 absolute PE

## 影响
- 直接影响了 Transformer-XL 的相对位置编码设计
- 为 RoPE、ALiBi 等后续方法铺平道路
