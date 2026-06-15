# AI Idea Bench 2025

## 基本信息
- **论文**: AI Idea Bench 2025: AI Research Idea Generation Benchmark
- **作者**: Yansheng Qiu, Haoquan Zhang, Zhaopan Xu, Ming Li, Diping Song, Zheng Wang, Kaipeng Zhang
- **年份**: 2025
- **来源**: arXiv:2504.14191
- **关键词**: benchmark, idea-generation, ai-research, leakage

## 核心思想
AI Idea Bench 2025 评测模型生成 AI research ideas 的能力，特别关注开放式 idea generation 中的 benchmark leakage、ground-truth comparison、novelty 和 feasibility。它把 2023 年 10 月 10 日之后发表的高质量 AI 会议论文作为 ground truth，并用 arXiv API 排除 2023 年 10 月 3 日前已经公开的预印本，再把这些论文的 inspiring papers 作为输入，从而测试模型能否从已有文献出发生成与后续真实研究发展相吻合的 idea。

## 评测目标
AI Idea Bench 2025 评测模型生成 AI research ideas 的能力，特别关注开放式 idea generation 中的 benchmark leakage 和 ground-truth comparison。评测不只问"idea 看起来好不好"，还问生成 idea 是否能在动机、实验方案、主题匹配、创新性和可行性上接近真实后续论文。

## 基准设计
该 benchmark 试图构建 leakage-aware evaluation，使模型不能简单复述训练或近期文献中的已知 idea。

核心设计包括：

- 数据集由 CVPR 2024、ECCV 2024、ICML 2024、NeurIPS 2024、NAACL 2024、EMNLP 2024、ACL 2024、ICLR 2025 等顶会论文构成；论文描述数据集论文发表于 2023 年 10 月 10 日之后，并通过 arXiv API 排除 2023 年 10 月 3 日前已公开的预印本；
- 对每篇 target paper，使用 DeepSeek V3 从引用文献中抽取高被引候选，再由两名有经验研究者选择 5 篇可行且合理的 inspiring papers；
- 给定 inspiring papers，要求 idea generation 方法生成研究动机和实验计划；
- 用六类评测比较生成 idea：idea multiple-choice、idea-to-idea matching、idea-to-topic matching、idea competition、novelty assessment、feasibility assessment；
- novelty 通过历史/当代文献相似度和当代影响力估计，feasibility 通过实验步骤相关参考方法的影响力估计。

## 关键数字

| 指标 | 数值 |
|---|---:|
| 数据集规模 | 3,495 篇 AI papers 及其 inspiring papers |
| 时间切分 | target papers 发表于 2023-10-10 之后；arXiv 预印本过滤阈值为 2023-10-03 |
| 覆盖会议 | CVPR 2024、ECCV 2024、ICML 2024、NeurIPS 2024、NAACL 2024、EMNLP 2024、ACL 2024、ICLR 2025 |
| 每篇 target paper 的 inspiring papers | 5 篇，由 DeepSeek V3 候选抽取 + 两名研究者筛选 |
| 评价方法 | 6 类：IMCQ、I2I、I2T、IC、NA、FA |

该基准专门处理 AI research idea generation 的开放式评测问题，核心价值在于用带 ground truth 的论文-启发工作关系缓解知识泄漏和纯主观评分问题。

## 设计哲学

开放式 idea generation 最大问题之一是“看起来新，其实训练集里已有”。AI Idea Bench 的价值在于把 leakage control 放到核心位置。

## 局限性

它聚焦 AI research ideas，不代表 biology、chemistry、materials 等自然科学发现。开放式评分仍难完全客观，且 novelty/feasibility 的量化依赖文献检索、引用量、语义相似度和 LLM judge，不能替代专家对真实科学价值的长期判断。用后续论文作为 ground truth 可以降低泄漏，但也会偏向已经被主流会议接受的研究范式。

## 核心贡献
AI Idea Bench 2025 的核心贡献是为 AI research idea generation 构建了一个带时间切分和真实后续论文参照的评测框架，把开放式科研创意生成拆成可比较的动机匹配、实验计划匹配、新颖性、可行性和方法间竞赛等维度。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Hypothesis Generation 和 Verification。

在 Skill Lifecycle 中，它对应 Verification / benchmark 和 Acquisition / benchmark-derived。

Evidence Role 应标为 **Boundary + Infrastructure**。它提醒我们，idea generation skill 必须控制文献泄漏和时间泄漏，否则“新颖性”结论不可靠。
