# Gemini for Science 2026

## 基本信息
- **资源**: Gemini for Science: AI experiments and tools for a new era of discovery
- **作者**: Pushmeet Kohli, Yossi Matias
- **年份**: 2026
- **来源**: Google Blog, published 2026-05-19, https://blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/
- **关键词**: research infrastructure, Google Labs, Co-Scientist, AlphaEvolve, ERA, NotebookLM, Science Skills, agentic research

## 核心思想

Gemini for Science 不是单篇系统论文，而是 Google 把多项 agentic science 能力产品化和基础设施化的入口。它把 Co-Scientist、AlphaEvolve、ERA、NotebookLM 和 Science Skills 组织成一组面向科研流程的实验性工具，目标是让研究者在假设生成、计算发现、文献综合和科研技能调用中获得 agentic assistance。

对本综述而言，它的价值在于说明 autonomous scientific discovery 正在从论文 prototype 进入平台化阶段：多智能体假设生成、演化式代码搜索、文献结构化分析、技能包和云端企业部署开始被整合成科研工作台，而不是孤立系统。

## 方法细节

Google Blog 描述了三个 Google Labs experimental tools：

- **Hypothesis Generation**：built with Co-Scientist。研究者定义 research challenge 后，系统使用 multi-agent idea tournament 生成、辩论和评估假设，并强调 claims 要有 clickable citations 支撑。
- **Computational Discovery**：built with AlphaEvolve and ERA。它被描述为 agentic research engine，通过并行生成和评分大量 code variations，帮助研究者测试新的 modeling approaches。
- **Literature Insights**：built with NotebookLM。它搜索科学文献，把结果结构化为带自定义属性的表格，支持基于 curated corpus 的 chat、报告和其他 artifact 生成。

此外，Gemini for Science 还包括 **Science Skills**，作为 Google Antigravity 上的 specialized bundle，整合超过 30 个生命科学数据库和工具。由于这部分涉及生物工具，本综述中只把它作为“skill bundle / agentic platform integration”的基础设施例子，不展开具体生物分析流程。

## 关键结果

这篇 Google Blog 不是评测论文，因此没有给出严格 benchmark。它给出的可引用事实包括：

- Gemini for Science 包括 Hypothesis Generation、Computational Discovery、Literature Insights 三个 Google Labs prototypes。
- Computational Discovery 明确连接 AlphaEvolve 与 ERA，用于生成和评分大量 code variations。
- ERA 和 Co-Scientist 的 Nature research papers 与该产品入口同期发布。
- Google 称其正在通过 Google Cloud 将这些能力带给 enterprise scientific and industrial R&D partners。
- Google 还提到已建立 trusted tester community，并与 ICML、STOC、NeurIPS 等会议探索 agentic peer review 和 scientific validation 工具，如 PAT 和 ScholarPeer。

## 局限性

Gemini for Science 是产品/平台发布，不是 peer-reviewed 系统论文。它可用于说明生态趋势和基础设施方向，但不能作为某个能力达成率、科学发现质量或真实部署效果的强证据。

Blog 中提到的 enterprise preview、trusted tester community 和 partner use cases 需要进一步一手材料支撑，不能直接写成经独立评估的科研发现成果。

Science Skills 涉及生命科学数据库和工具，本综述目前只应写成 skill bundle 和 platform integration，不应展开具体实验或操作细节。

## 核心贡献

Gemini for Science 的核心贡献是把 Co-Scientist、AlphaEvolve、ERA、NotebookLM 和 Science Skills 放进同一个科研基础设施叙事中，展示大厂正在把 agentic science 从单点论文系统推进到平台化、工具化和工作台化。

## 与综述的关联

在 Scientific Workflow 中，它横跨 Knowledge Grounding、Hypothesis Generation、Execution、Result Analysis 和 Synthesis。它不是一个单一发现系统，而是一个 ecosystem layer。

在 Skill Lifecycle 中，它对应：

- **Representation**：Science Skills、research tools、structured literature tables；
- **Retrieval**：Literature Insights 的文献搜索和属性化表格；
- **Composition**：Co-Scientist、AlphaEvolve、ERA、NotebookLM 的工具组合；
- **Execution**：Computational Discovery 中的 code variation generation and scoring；
- **Verification**：clickable citations、trusted tester community、scientific validation pilots。

Evidence Role 应标为 **Infrastructure**。它适合放在综述后半部分的 ecosystem / infrastructure 章节，用来说明 Multi-Agent 和 Evolutionary-Agent Workflow 如何进入实际科研工具链。

## 可引用点

| 点 | 内容 |
|---|---|
| 三个 prototype | Hypothesis Generation, Computational Discovery, Literature Insights |
| 关联论文 | Co-Scientist, ERA, AlphaEvolve |
| 基础设施信号 | Google Labs + Google Cloud + Google Antigravity Science Skills |
| 综述位置 | agentic science ecosystem / research infrastructure |
| 边界 | 产品发布，不是能力评测论文 |

## 写作时避免

- 不要把 Gemini for Science 当成单篇 peer-reviewed system paper。
- 不要把 blog 中的 partner preview 写成独立验证结果。
- 不要展开 Science Skills 的具体生物操作，只保留平台和 skill bundle 视角。
