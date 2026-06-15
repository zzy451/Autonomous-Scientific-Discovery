# LiveIdeaBench 2026

## 基本信息
- **论文**: Evaluating LLMs' Divergent Thinking Capabilities for Scientific Idea Generation with Minimal Context
- **作者**: Kai Ruan, Xuan Wang, Jixiang Hong, Peng Wang, Yang Liu, Hao Sun
- **年份**: 2026
- **来源**: Nature Communications, doi:10.1038/s41467-026-70245-1; arXiv:2412.17596v4
- **关键词**: benchmark, scientific-ideation, divergent-thinking, llm-as-judge, creativity-evaluation

## 核心思想
LiveIdeaBench 评测 LLM 在科学 idea generation 中的 **divergent thinking** 能力：模型只收到一个科学关键词，需要在极少上下文下生成原创、可行、清晰且多样的科学想法。

## 评测目标
LiveIdeaBench 评测 LLM 在科学 idea generation 中的 **divergent thinking** 能力：模型只收到一个科学关键词，需要在极少上下文下生成原创、可行、清晰且多样的科学想法。

它刻意不同于 GPQA、MMLU、LiveBench 等偏向“有唯一正确答案”的 convergent-thinking 基准，也不同于 ResearchAgent、Co-Scientist 这类给定文献和工具链的系统。它测的是模型在最小提示下能否产生科学概念跳跃，而不是完整科研流程、文献 groundedness 或实验验证能力。

## 基准设计
- **题目来源**：1,180 个 high-impact scientific keywords，覆盖 22 个科学领域；关键词库按月更新，以保持与当前科学趋势和前沿概念对齐。
- **模型范围**：基于 2025 年 3 月 LiveBench 结果选取 41 个 state-of-the-art LLM，覆盖 Anthropic、OpenAI、Google、Qwen、DeepSeek、Meta、Mistral、Amazon、StepFun、xAI、Microsoft 等模型。
- **生成方式**：每个模型根据单个 keyword 生成约 100 词以内的科学 idea；超过 200 词的回答会被排除。
- **评价维度**：借鉴 Guilford 的 divergent production 理论，评测 originality、feasibility、clarity、fluency、flexibility 五个维度。
- **LLM-as-a-judge**：由 LiveBench 前 10 模型组成动态 judge panel，单一机构最多占 2 个 judge；评价某个模型输出时，该模型不能作为自己的 judge。originality、feasibility、clarity 每个 idea 由 3 个随机 judge 评分。
- **fluency 计算**：比较同一模型在同一 keyword 下生成 idea 的差异性，用 A/B/C/D 等级衡量 idea 是否真正不同，而不是表面改写。
- **拒答处理**：对安全策略导致的拒答，先检测 refusal，再用 academic-context fallback prompt 二次尝试，避免强安全对齐模型被简单惩罚。
- **人类验证**：在 PDE 领域抽取 11 个模型生成的 22 个 idea，由 6 名 PDE 专家盲评 originality、feasibility、clarity，并与 LLM judge panel 对比。

## 关键数字

| 指标 | 数字/结论 | 说明 |
|------|-----------|------|
| 科学关键词 | 1,180 | 覆盖 22 个科学领域，按月更新 |
| 评测模型 | 41 | 基于 2025 年 3 月 LiveBench 的顶级模型集合 |
| Judge panel | Top 10 LiveBench 模型 | 单一机构最多 2 个 judge，避免自评 |
| 单个 idea judge 数 | 3 | originality、feasibility、clarity 由 3 个随机 judge 平均 |
| 最高平均分 | claude-3.7-sonnet:thinking：7.22 | Supplementary Table 3；deepseek-r1 为 7.18，claude-3.7-sonnet 为 7.12 |
| QwQ-32B-preview | LiveIdeaBench 第 8/41 | 尽管一般智能分数较低，但科学 ideation 表现接近强闭源模型 |
| LiveIdeaBench vs LiveBench | Pearson r = 0.357, p = 0.038, r2 = 0.127 | 一般智能只能弱预测科学 idea generation |
| idea 长度 vs 质量 | Spearman rho = 0.089, r2 = 0.008 | 更长推理/更长 idea 不等于更高质量 |
| 人类专家验证 | 22 个 PDE ideas，6 名专家 | 专家盲评，与 LLM judge 对比 |
| 专家一致性 | originality ICC = 0.823；clarity ICC = 0.782；feasibility ICC = 0.453 | 新颖性和清晰度较一致，可行性争议大 |
| 计算环境影响 | 总计约 5027.45 kWh，3074.07 kgCO2eq | Supplementary Table 4，闭源模型为估计值 |

## 设计哲学

LiveIdeaBench 的核心哲学是：科学创造力不能只用“解题能力”或“通用智能”替代评估。它把科学 idea generation 视为一种相对独立的发散思维能力，强调从稀疏刺激中生成多样、原创、可行的概念。

这使它成为 ResearchAgent、Co-Scientist、AI Scientist 等系统论文的必要补充：系统论文常展示 agent 生成了看似合理的研究方向，而 LiveIdeaBench 提醒我们必须单独评测模型的 ideation profile，并区分 originality、feasibility、clarity、fluency、flexibility 的不同 trade-off。

## 局限性

- 单关键词 prompt 只评测最小上下文下的发散思维，不评测文献检索、引用准确性、实验设计细节或真实验证。
- LLM-as-a-judge 可能有偏差；动态 judge panel 也会降低跨时间复现性，因为 judge 模型会更新。
- 闭源模型依赖 API，模型版本可能在未公开说明下变化，影响可复现性。
- aligned models 可能产生 sycophancy，导致绝对分数偏高、分数区间压缩，因此相对排名比绝对分数更可靠。
- 安全对齐与创造性评测存在张力：某些模型会拒绝 ecotoxicology 等敏感关键词，fallback prompt 只能部分缓解。
- judge 模型若不理解真正前沿或专业概念，可能误判 originality 或 feasibility；作者建议未来可引入 RAG 来增强 judge。
- 人类专家验证只覆盖 PDE 一个领域，且 feasibility 的专家一致性较低，说明“简短 idea 是否可行”本身很难可靠评估。

## 核心贡献
LiveIdeaBench 2026 的核心贡献是为科学 idea generation 中的 divergent thinking 建立动态基准，用 1,180 个高影响力科学关键词、41 个模型和多模型 judge panel 分别评估 originality、feasibility、clarity、fluency 与 flexibility，并显示科学 ideation 能力不能由通用 benchmark 分数强预测。

## 与综述的关联

LiveIdeaBench 在我们的框架中属于 **Boundary evidence**。它不证明 agent 能完成科学发现，但能约束“LLM/agent 能提出好科学想法”的 claim：idea generation 是可测能力，而且与一般推理、数学、代码能力并不等价。

在 Scientific Workflow 中，它主要覆盖 Hypothesis Generation 和 Verification；在 Skill Lifecycle 中，它对应 benchmark-derived verification，并为后续筛选 hypothesis-generation skill 提供评价标准。

对综述写作最重要的启示是：Skill-driven scientific discovery 不能只看系统是否会调用工具和写流程，还必须区分不同模型/agent 在 scientific ideation 上的能力剖面。一个模型可能善于解题但不善于提出新想法，也可能一般智能分数不高但在发散式科学 ideation 上表现突出。
