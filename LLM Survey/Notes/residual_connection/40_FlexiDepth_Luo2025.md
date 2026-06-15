# FlexiDepth: Adaptive Layer-Skipping in Pre-trained LLMs

**论文信息**: Luo, X., et al. (2025). Adaptive Layer-skipping in Pre-trained LLMs
**arXiv**: 2503.23798
**分类**: Dynamic Depth (动态深度 / 自适应层跳过)

## 核心思想
文本生成中不同 token 需要的计算深度不同。FlexiDepth 动态调整每个 token 使用的 Transformer 层数，通过插件式路由器和适配器实现自适应层跳过，无需修改预训练模型的原始参数。

## 关键机制
- **Plug-in Router**: 每层附加轻量路由器，基于当前 hidden state 决定是否跳过该层
- **Plug-in Adapter**: 当层被跳过时，用轻量适配器补偿跳过层的信息损失
- **参数冻结**: 原始 LLM 参数完全冻结，仅训练路由器和适配器参数
- **Per-Token 动态深度**: 同一序列中不同 token 可使用不同数量的层

## 实验结果
- 应用于 Llama-3-8B，在 32 层中跳过 8 层（25% 层跳过率）
- 性能保持与全层推理相当
- 简单 token（标点、常见功能词）倾向于使用更少层，复杂 token 使用更多层
- 实现了实际的推理加速

## 与综述的关联
属于 **Dynamic Depth** 维度的实用工作。与 LayerDrop (Note 11) 的训练时随机丢层不同，FlexiDepth 是推理时的自适应跳层。与 TIDE (Note 38) 类似都是后训练方法，但 FlexiDepth 额外引入 adapter 来补偿跳层损失。与 Mixture of Depths (Note 13) 的 token 级路由思想一致，但 FlexiDepth 面向已有预训练模型的后训练部署。

## 核心贡献
提出插件式路由器+适配器的后训练层跳过方案，在不修改原始模型参数的前提下实现 per-token 自适应深度，兼顾效率和性能。
