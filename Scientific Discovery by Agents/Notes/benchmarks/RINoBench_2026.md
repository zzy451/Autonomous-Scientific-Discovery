# RINoBench 2026

## 基本信息
- **论文**: Is this Idea Novel? An Automated Benchmark for Judgment of Research Ideas
- **作者**: Tim Schopf and Michael Färber
- **年份**: 2026
- **来源**: arXiv:2603.10303
- **关键词**: benchmark, hypothesis-generation, novelty-evaluation, llm-judge

## 核心思想
RINoBench 评测模型能否判断研究想法的新颖性。科学 idea generation 不只需要生成想法，还需要判断它是否只是已有工作的变体、是否真正扩展文献边界。

## 评测目标
RINoBench 评测模型能否判断研究想法的新颖性。科学 idea generation 不只需要生成想法，还需要判断它是否只是已有工作的变体、是否真正扩展文献边界。

## 基准设计
RINoBench 是面向 research idea novelty judgment 的 benchmark。它把任务定义为：给定一个 research idea 及其 related works，模型需要依据 1-5 分 novelty rubric 给出新颖性分数，并写出基于相关文献比较的文本理由。

核心设计包括：

- 从 OpenReview 收集 ICLR 2022 和 ICLR 2023 的公开投稿及评审，共 6,410 篇论文；
- 只保留 reviewer 在 "Technical Novelty and Significance" 与 "Empirical Novelty and Significance" 上分歧不超过 1 分的投稿，得到 3,535 篇高一致性样本；
- 用标题、摘要和 reviewer summaries 抽取论文背后的 concise research idea，并将 reviewer novelty 评分聚合到 1-5 分 rubric；
- 最终数据集包含 1,381 个 research ideas，每个 idea 配有 novelty score、human-authored/synthesized textual justification，以及平均 25.23 篇 related works 的标题和摘要；
- 采用分层 80:20 train-test split，得到 1,104 个训练样本和 277 个测试样本；
- 评估包含 novelty score metrics（macro-F1、各类别 F1、MAE）和 textual justification metrics（alignment、known/novelty aspects 的 recall、additional ratio、hallucination rate），合计 9 个自动指标。

## 关键数字

| 指标 | 数值 |
|---|---:|
| research ideas | 1,381 |
| train / test | 1,104 / 277 |
| 原始 ICLR 投稿 | 6,410 |
| 高一致性过滤后论文 | 3,535 |
| 平均 related works | 25.23 |
| automated evaluation metrics | 9 |
| 最佳 macro-F1 | GPT-5: 17.2；o3: 16.2 |

## 设计哲学

RINoBench 的核心设计哲学是把“新颖性判断”从主观印象变成可重复评测任务。论文发现 LLM 生成的 reasoning 可能接近 human rationales，但最终 novelty judgments 仍明显偏离 human gold judgments；模型还倾向于回避极端判断，几乎不把 idea 判为“完全不新颖”或“高度新颖”，而是集中在中间档位。

## 局限性

RINoBench 评估的是 novelty judgment，不评估 idea 的实验可行性、严谨性、社会价值、可复现性或真实发现成功。数据只来自 ICLR 2022/2023，反映的是机器学习会议的审稿文化和 novelty 标准，不能直接代表其他学科。human novelty labels 本身也可能受领域覆盖、评审偏见和时间窗口影响。

## 核心贡献
RINoBench 2026 的核心贡献是为 research idea novelty judgment 构建首个大规模、可自动评价的 benchmark，把新颖性分数预测和文本理由评价统一到同一框架中，并显示“理由看似合理”并不等同于“新颖性判断准确”。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Hypothesis Generation 和 Verification。

在 Skill Lifecycle 中，它对应 Verification / benchmark 和 Retrieval / literature-aware judgment。

Evidence Role 应标为 **Boundary**。它约束“LLM 能解释为什么新颖”与“LLM 真能准确判断新颖”之间的差距，是 hypothesis-generation skill 的关键边界证据。
