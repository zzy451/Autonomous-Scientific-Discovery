# Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models

**论文**: Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models
**作者**: Tianwen Wei, Bo Zhu, Liang Zhao, et al. (Kunlun Inc.)
**年份**: 2024
**来源**: arXiv:2406.06563
**标签**: MoE, Upcycling, 门控归一化, 自适应辅助损失

---

## 0. 摘要
Skywork-MoE 是从 Skywork-13B dense 模型 upcycling 而来的 146B 参数 MoE 模型（22B 活跃参数，16专家）。提出了两项技术创新：门控逻辑归一化（Gating Logit Normalization）和自适应辅助损失系数（Adaptive Auxiliary Loss Coefficients）。

## 1. 方法动机
a) MoE 训练中门控分布容易偏斜，部分专家被过度使用。
b) 全局统一的辅助损失系数不适合所有层——不同层的负载均衡需求不同。
c) 假设：通过门控归一化和层级自适应损失可以改善训练质量。

## 2. 方法设计
a) 门控逻辑归一化（Gating Logit Normalization）：
   - 在 softmax 之前对门控 logits 进行归一化
   - 防止 logit 的尺度过大导致 softmax 输出过于极端
   - 促进专家多样化使用

b) 自适应辅助损失系数：
   - 不同层使用不同的辅助损失系数
   - 根据每层实际的负载均衡情况自适应调整
   - 比全局统一系数更精细

c) Upcycling：
   - 从预训练好的 Skywork-13B dense 模型初始化
   - 将每个 FFN 复制多份作为专家
   - 在 SkyPile 语料上继续训练

## 3. 与其他方法对比
| 方法 | 门控优化 | 辅助损失 | 初始化 |
|------|----------|----------|--------|
| Switch Transformer | 标准 softmax | 全局统一系数 | 从头训练 |
| Mixtral | 标准 softmax | 未详述 | 从头训练 |
| **Skywork-MoE** | **归一化+softmax** | **层级自适应** | **Dense upcycling** |

## 4. 实验表现
- 146B 参数（22B 活跃），性能优于同级别模型
- 门控归一化显著提升专家使用多样性
- 自适应辅助损失比固定系数带来更好的训练稳定性

## 5. 对 Channel Mixer 的意义
Skywork-MoE 在门控设计层面的两个细粒度优化（归一化和自适应损失）为 MoE 训练提供了实用改进。同时探索了 dense→MoE upcycling 的实践路径，为资源受限场景提供了参考。

## 6. 总结
a) 核心思想：门控归一化+自适应损失优化MoE训练（16字）
b) 速记 pipeline：
   1. 从 dense 模型 upcycling 初始化 MoE
   2. 门控 logit 归一化防止极端路由
   3. 每层自适应调整辅助损失系数
   4. 促进专家多样化和训练稳定性
