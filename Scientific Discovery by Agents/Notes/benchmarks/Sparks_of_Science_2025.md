# Sparks of Science 2025

## 基本信息
- **论文**: Sparks of Science: Hypothesis Generation Using Structured Paper Data
- **作者**: Charles O'Neill, Tirthankar Ghosal, Roberta Răileanu, Mike Walmsley, Thang Bui, Kevin Schawinski, Ioana Ciucă
- **年份**: 2025
- **来源**: arXiv:2504.12976
- **关键词**: benchmark, hypothesis-generation, dataset, scientific-ideation

## 核心思想
Sparks of Science 关注如何从已有论文结构中生成科学假设。其目标是把 hypothesis generation 从开放式写作转化为有数据结构、有输入输出、有评价维度的任务。

## 评测目标
Sparks of Science 关注如何从已有论文结构中生成科学假设。其目标是把 hypothesis generation 从开放式写作转化为有数据结构、有输入输出、有评价维度的任务。

## 基准设计
论文构建 HypoGen 数据集，并用结构化 paper data 支撑假设生成。

其公开描述包括：

- 从论文摘要中抽取 Bit、Flip、Spark，并从正文中抽取 Chain-of-Reasoning；
- 使用 Bit-Flip-Spark schema 表示科学创新元素，其中 Bit 是 conventional assumption，Spark 是 4-6 词的 key insight，Flip 是 resulting counterproposal；
- 生成 chain-of-reasoning；
- 用自动指标、LLM judge 和小规模 human evaluation 评估生成假设的新颖性、可行性和整体质量。

## 关键数字

| 指标 | 数值 |
|---|---:|
| HypoGen 数据规模 | 5,478 个 structured problem-hypothesis pairs |
| 数据来源 | NeurIPS 2023（3,218 篇）和 ICLR 2024（2,260 篇） |
| 评测集 | 50 个主要来自 2024-2025 文献的 hypotheses |
| 表示 schema | Bit-Flip-Spark + Chain-of-Reasoning |

论文将 scientific hypothesis generation 形式化为 conditional language modelling：训练时使用 Bit-Flip-Spark 和 Chain-of-Reasoning，推理时只提供 Bit。原文报告 fine-tuning 相比同架构 one-shot 版本提升 overall quality（LLM judge 中 fine-tuned 版本偏好率 86-92%）和 feasibility（74-86% win rate），但同时出现 novelty-feasibility trade-off：非微调版本在 novelty 上更强，human hypotheses 在整体质量上仍以 82-90% win rate 胜过 LLM 生成假设。

## 设计哲学

Sparks of Science 的设计哲学是：科学想法不是从空白处生成，而是围绕已有论文中的 conventional assumption 形成 counterproposal，并用显式 reasoning chain 记录从 Bit 到 Flip 的过渡。结构化 paper data 可以让 hypothesis generation 更可解释、更可复现，但这种结构化也会把复杂科学创意压缩进特定 schema。

## 局限性

假设质量评价主要依赖 LLM-as-a-judge，论文自己指出这可能受 judge 模型偏差影响；human evaluation 规模仍小，不能替代后续实验验证。数据和评测集中在计算机科学，跨 astrophysics、biology、materials science 等领域的泛化仍是开放问题。结构化 schema 可能简化真实科学创意过程。

## 核心贡献
Sparks of Science 2025 的核心贡献是把 scientific hypothesis generation 组织为 Bit-Flip-Spark + Chain-of-Reasoning 的条件生成任务，并发布 HypoGen 数据集，为“文献结构如何转化为假设生成 skill”提供可训练、可评测的表示基础。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Knowledge Grounding 和 Hypothesis Generation。

在 Skill Lifecycle 中，它对应 Acquisition / literature-derived 和 Representation / hypothesis schema。

Evidence Role 应标为 **Infrastructure**。它为 hypothesis-generation skill 提供数据和表示基础，适合支撑“从文献中抽取可组合 research skill / idea unit”的观点。
