# ShortGPT: Layers in Large Language Models are More Redundant Than You Expect
**作者**: Xin Men, Mingyu Xu, Qingyu Zhang, Bingning Wang, Hongyu Lin, Yaojie Lu, Xianpei Han, Weipeng Chen | **年份**: 2024 | **arxiv**: 2403.03853

## 0. 摘要翻译
在扩展基于 Transformer 的大语言模型 (LLM) 的过程中，模型架构中引入了大量冗余结构，给实际部署带来效率挑战。本文研究 LLM 中各层的冗余性，发现层间存在惊人的高度相似性。基于此观察，定义了 Block Influence (BI) 指标来衡量每层的重要性，并提出简单直接的层剪枝方法——直接删除 BI 分数最低的冗余层。该方法称为 ShortGPT，在多个基准上优于先前的剪枝方法，且与量化方法正交，可进一步组合使用。

## 1. 方法动机
- 大规模 LLM 的层数不断增加（如 LLaMA-2-70B 有 80 层），但并非所有层都同等重要
- 观察到许多层的输入和输出之间具有极高的余弦相似度，说明这些层几乎是恒等映射
- 这种冗余性暗示可以直接删除部分层而不显著影响性能
- 需要一个量化指标来识别哪些层是冗余的

## 2. 方法设计
- **Block Influence (BI) 指标**: 衡量每个 Transformer 层对隐藏状态的实际影响程度
  - 计算第 $l$ 层输入 $\mathbf{h}_l$ 与输出 $\mathbf{h}_{l+1}$ 之间的余弦相似度
  - $\text{BI}(l) = 1 - \cos(\mathbf{h}_l, \mathbf{h}_{l+1})$
  - BI 越低 → 该层越接近恒等映射 → 越冗余
- **层删除策略**: 按 BI 分数从低到高排序，直接删除分数最低的层
- **无需微调**: 删除后直接评估，无需重新训练
- **与量化正交**: 可以先删层再量化，进一步压缩

## 3. 对比
| 方法 | 粒度 | 是否需要微调 | 压缩方式 |
|------|------|------------|---------|
| 权重剪枝 (SparseGPT等) | 权重级别 | 通常需要 | 稀疏化 |
| 量化 (GPTQ等) | 权重级别 | 通常需要 | 低比特 |
| ShortGPT | 层级别 | 不需要 | 直接删层 |
| 知识蒸馏 | 模型级别 | 需要 | 小模型 |

## 4. 实验
- **模型**: LLaMA-2-7B/13B/70B, Mistral-7B, Qwen-7B 等
- **关键发现**:
  - LLaMA-2-70B 删除 50% 注意力层后仅损失 2.4% 性能，获得 48.4% 加速
  - 中间层的冗余度最高，首尾层最重要
  - BI 分数在训练早期就已稳定，冗余模式在预训练初期即形成
- **基准**: MMLU, CMMLU, HellaSwag, PIQA, ARC 等
- **优于**: 权重级别剪枝方法 (Wanda, SparseGPT 等)

## 5. 总结
a) 一句话: ShortGPT 通过 Block Influence 指标发现 LLM 中间层高度冗余，直接删除低 BI 层即可在几乎不损失性能的情况下大幅加速推理。
b) 速记 pipeline: `计算每层 BI = 1-cos(输入,输出) → 按 BI 排序 → 删除最冗余层 → 无需微调直接部署`; 核心发现: 中间层≈恒等映射。
