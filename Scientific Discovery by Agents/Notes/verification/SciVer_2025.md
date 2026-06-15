# SciVer 2025

## 基本信息
- **论文**: SCIVER: Evaluating Foundation Models for Multimodal Scientific Claim Verification
- **作者**: Chengye Wang, Yifei Shen, Zexi Kuang, Arman Cohan, Yilun Zhao
- **年份**: 2025
- **来源**: ACL 2025 Long Papers; https://aclanthology.org/2025.acl-long.420/
- **关键词**: benchmark, scientific-claim-verification, multimodal-reasoning, evidence-retrieval, scientific-literature

## 核心思想
SCIVER 评测 foundation models 在 **multimodal scientific claim verification** 中的能力：给定一篇科学论文的上下文，包括文本段落、表格和图表，模型需要判断一个 claim 是 entailed 还是 refuted，并依赖正确的支持证据进行推理。

## 评测目标
SCIVER 评测 foundation models 在 **multimodal scientific claim verification** 中的能力：给定一篇科学论文的上下文，包括文本段落、表格和图表，模型需要判断一个 claim 是 entailed 还是 refuted，并依赖正确的支持证据进行推理。

它补足了 SciFact、SciFact-Open、OpenScholar 等主要偏文本或检索型科学验证工作的盲区：真实论文中的科学结论常常需要同时读段落、表格、图和图表 caption，而不是只看文本句子或单个表格。

## 基准设计
- **数据规模**：3,000 个 expert-annotated examples，来自 1,113 篇科学论文。
- **论文来源**：2024-09-01 到 2024-11-15 之间 arXiv 上的计算机科学论文，优先选择 comments 中显示被同行评审会议/期刊接收的论文。
- **划分**：validation 1,000 条，test 2,000 条；test 集来自 786 篇论文，validation 来自 327 篇论文。
- **标签**：二分类 entailment label：`entailed` 或 `refuted`。validation 中 entailed/refuted 为 505/495，test 中为 995/1005。
- **四类 reasoning subsets**：direct reasoning、parallel reasoning、sequential reasoning、analytical reasoning。
- **多模态上下文**：每条样例包含文本段落、表格、图表；test 集平均文本 567.4 words、0.54 个表格、0.95 个图表。
- **支持证据标注**：每条样例平均约 2.62 个 supporting evidence pieces，由专家标注相关段落、表格和图表。
- **标注者**：18 名具备相关领域知识的 CS graduate students，每人至少有 2 篇 peer-reviewed publications，并经过 2 小时个别培训。
- **质量控制**：第二位专家标注 supporting evidence；若与初始标注不一致，由第三位专家仲裁。entailment label inter-annotator agreement 为 **94.0%**。最终验证阶段有 **232** 条初始样例被修订。
- **模型评测**：评测 21 个开源和闭源多模态模型，使用 CoT prompt，主指标为 accuracy。

## 关键数字

| 指标 | 数字/结论 | 说明 |
|------|-----------|------|
| 数据规模 | 3,000 examples / 1,113 papers | expert-annotated |
| 验证/测试集 | 1,000 / 2,000 | test 来自 786 篇论文 |
| reasoning subsets | 4 类 | direct, parallel, sequential, analytical |
| supporting evidence | 平均 2.62 个 | 单个 evidence 可以是表格、图或段落 |
| 标注一致性 | 94.0% | entailment label annotation |
| 人类专家准确率 | 93.8% | 40 条抽样 claim，两名专家 |
| 最强模型 | o4-mini：77.7% test accuracy | 仍显著低于人类专家 |
| GPT-4.1 | Table 3: 73.9% test accuracy；正文讨论处另称 73.2% CoT accuracy | Analytical reasoning：正文称 70.8%，Table 3 行报告为 73.8%；均低于人类 analytical 90.0% |
| 最强开源模型 | Mistral-Small-3.1-24B：71.3% test accuracy | 开源模型仍整体落后闭源前沿模型 |
| 错误类型：证据检索失败 | 32% | Qwen2.5-VL-72B 错误分析 |
| 错误类型：视觉元素误读 | 21% | 表格/图表解释错误 |
| 错误类型：多步推理失败 | 17% | 不能连接中间推理步骤 |
| 错误类型：过度依赖文本 | 12% | 忽略表格和图 |
| 错误类型：领域误解 | 10% | 错误套用领域知识或记忆 |
| RAG 改进 | Qwen2.5-VL-72B 70.2% -> 75.3% | 使用 OpenAI embedding 检索 top-5 evidence |
| ToolEval? | 不适用 | SCIVER 是 claim verification benchmark，不是 tool-use 评测 |

## 设计哲学

SCIVER 的设计哲学是把科学验证从“文本事实核查”推进到“论文级多模态证据整合”。它强调模型必须先定位相关 evidence，再综合段落、表格、图表中的信息，最后判断 claim 与论文证据是否一致。

这与真实科研 agent 的 verification 需求高度一致：如果 agent 只能读摘要或文本段落，就容易漏掉表格中的关键数值、图中的趋势、caption 中的实验设定，进而产生错误结论。SCIVER 因此是科学发现 Agent 验证能力的重要边界测试。

## 局限性

- 数据主要来自计算机科学 arXiv 论文，不能直接代表生物、化学、材料、医学等实验科学论文。
- 当前多模态元素主要是文本段落、表格和图表，不显式覆盖方程、显微图像、实验图像或复杂科学仪器输出。
- 依赖专家标注，质量高但成本高，扩展到更大规模或更多学科较难。
- 任务是 context-grounded verification，不评测开放域检索阶段的完整难度；RAG 分析只是补充实验。
- 表格和图表被作为截图输入，模型在结构化解析、坐标轴理解、数值读取方面的失败仍可能与视觉输入方式有关。

## 核心贡献
SciVer 2025 的核心贡献是将科学输出的验证、审查或风险识别具体化为可分析的任务，为本综述的 verification / governance 章节提供约束性证据。

## 与综述的关联

SCIVER 在我们的框架中属于 **Boundary + Verification evidence**。它不是科学发现系统，但为“agent 生成科学结论后如何验证”提供了明确基准，尤其强调多模态证据整合。

在 Scientific Workflow 中，它覆盖 Verification 和 Result Analysis；在 Skill Lifecycle 中，它对应 Verification / benchmark、Retrieval / evidence、Execution / multimodal interpretation。

它对综述的关键启示是：科学发现 Agent 的 verification skill 不能只包括 citation check 或文本 claim check，还必须包括表格读取、图表理解、多证据合成和多步推理。当前最强模型 o4-mini 的 test accuracy 为 77.7%，与人类专家 93.8% 仍有约 16.1 个百分点差距，说明“自动验证科学结论”仍是显著瓶颈。
