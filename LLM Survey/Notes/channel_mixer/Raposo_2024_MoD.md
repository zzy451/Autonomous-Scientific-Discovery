# Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models

**论文**: Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models
**作者**: David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter Conway Humphreys, Adam Santoro (Google DeepMind)
**年份**: 2024
**来源**: arXiv:2404.02258
**标签**: 条件计算, 动态计算分配, 路由

---

## 0. 摘要
Mixture-of-Depths（MoD）让 Transformer 动态地为序列中的不同 token 分配不同的计算量。在每层，top-k 路由机制决定哪些 token 经过完整的注意力+MLP 计算，哪些直接通过残差连接跳过。在相同 FLOPs 下超越 dense 模型 1.5%，推理速度提升 50%。

## 1. 方法动机
a) 标准 Transformer 对所有 token 施加相同的计算量，但不同 token 的处理难度不同。
b) MoE 解决了"用哪些专家"的问题，但每个 token 都会被某些专家处理——计算总量不变。
c) 假设：允许某些 token 在某些层"跳过"计算，可以将计算集中在"重要"token 上。

## 2. 方法设计
a) 路由机制：
   - 每层有一个路由器，为每个 token 计算一个标量得分
   - 选择 top-k 个 token 进行"完整计算"（注意力+MLP）
   - 其余 token 直接通过残差连接跳过该层
   - k 是预设的容量参数

b) 关键特性：
   - 静态计算预算：每层处理固定数量的 token → 计算图确定 → FLOPs 可预测
   - 与 MoE 类比：MoE 选择"用哪个专家"，MoD 选择"是否计算"
   - 可以与 MoE 组合使用

c) 训练：
   - 路由器通过标准反向传播训练
   - 模型学会识别哪些 token 在哪些层需要更多计算

## 3. 与其他方法对比
| 方法 | 计算分配 | 参数利用 | FLOPs 可控 |
|------|----------|----------|------------|
| Dense Transformer | 均匀 | 全部 | 固定 |
| MoE | 均匀（每token） | 部分（稀疏） | 固定 |
| Early Exit | 动态（按层） | 全部 | 不固定 |
| **MoD** | **动态（按token）** | **全部** | **固定** |

## 4. 实验表现
- isoFLOP 下超越 dense Transformer 1.5%（log-probability）
- 推理速度提升 50% 以上
- 学到了有意义的路由模式：功能词倾向被跳过，内容词获得更多计算

## 5. 对 Channel Mixer 的意义
MoD 提供了一个与 MoE 互补的条件计算视角。MoE 关注"token 特征如何被不同专家处理"，MoD 关注"token 是否需要被该层的 FFN 处理"。两者可以组合使用，形成更灵活的 Channel Mixer 设计空间。

## 6. 总结
a) 核心思想：按token动态跳过层计算节约资源（14字）
b) 速记 pipeline：
   1. 每层路由器为所有 token 评分
   2. 选择 top-k 个 token 进行完整计算
   3. 其余 token 通过残差连接跳过
   4. 计算预算可控，推理速度提升 50%
