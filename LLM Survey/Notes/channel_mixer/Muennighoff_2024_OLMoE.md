# OLMoE: Open Mixture-of-Experts Language Models

**论文**: OLMoE: Open Mixture-of-Experts Language Models
**作者**: Niklas Muennighoff, Luca Soldaini, et al. (Allen Institute for AI, Contextual AI)
**年份**: 2024
**来源**: arXiv:2409.02060
**标签**: MoE, 开源, 全透明

---

## 0. 摘要
OLMoE 是完全开源的 MoE 语言模型，总参数 7B，活跃参数 1B。使用 64 个专家、每个 token 激活 8 个专家的设计。在 5 万亿 token 上预训练。开源了模型权重、训练代码、训练数据、训练日志和中间检查点。

## 1. 方法动机
a) 之前的高性能 MoE 模型（Mixtral, DeepSeek 等）虽然开放了权重，但训练细节不完全公开。
b) MoE 研究社区缺乏一个真正完全透明的基准模型来进行深入分析。
c) 假设：完全开放的 MoE 模型可以加速社区对 MoE 架构的理解和改进。

## 2. 方法设计
a) 架构配置：
   - Decoder-only Transformer
   - 总参数 7B，每 token 活跃参数 1B
   - 64 个专家，每个 token 激活 8 个
   - FFN 被 MoE 层替换

b) 训练：
   - 5 万亿 token 预训练
   - 标准 Top-K 路由
   - 辅助损失负载均衡

c) 开源内容：
   - 模型权重
   - 训练代码
   - 训练数据集
   - 训练日志
   - 中间检查点

## 3. 与其他方法对比
| 方法 | 总参数 | 活跃参数 | 专家数 | 开放程度 |
|------|--------|----------|--------|----------|
| Mixtral 8x7B | 47B | 13B | 8 | 权重+推理 |
| DBRX | 132B | 36B | 16 | 权重 |
| **OLMoE** | **7B** | **1B** | **64** | **完全开源** |

## 4. 实验表现
- 在 MMLU、GSM8k、HumanEval 等基准上超越同级别活跃参数的模型
- OLMoE-Instruct 在某些任务上与 LLaMA 2 13B Chat 相当
- 小规模但高效，适合边缘部署

## 5. 对 Channel Mixer 的意义
OLMoE 的价值主要在于为 MoE 研究提供了一个完全透明的实验平台。64 专家+8 激活的高稀疏度配置也展示了 MoE 在小型模型上的可行性，证明了细粒度专家设计的普适价值。

## 6. 总结
a) 核心思想：完全开源的64专家MoE为社区提供透明基准（19字）
b) 速记 pipeline：
   1. 64 个细粒度专家，每 token 激活 8 个
   2. 5 万亿 token 预训练
   3. 7B 总参数仅 1B 活跃
   4. 完全开源（代码+数据+日志+检查点）
