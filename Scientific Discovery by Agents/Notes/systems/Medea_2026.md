# Medea 2026

## 基本信息
- **论文**: Medea: An Omics AI Agent for Therapeutic Discovery
- **作者**: Pengwei Sui et al.
- **年份**: 2026
- **来源**: bioRxiv preprint / PubMed PMID:41648610 / PMCID:PMC12871667, doi:10.64898/2026.01.16.696667
- **关键词**: system, biomedical-agent, omics, therapeutic-discovery, verification

## 核心思想
组学数据可以支持靶点发现、合成致死推理和免疫治疗反应预测，但这些分析通常需要跨数据库、模型、文献和代码执行进行长程推理。普通 agent 容易丢失疾病、细胞类型、患者队列等生物上下文，也常常只生成分析流程而不验证中间结果。

Medea 要解决的问题是：如何让 AI agent 在执行 therapeutic discovery 的组学分析时，显式记录中间决策，并在数据、工具和文献约束下持续验证每一步。

## 方法细节
Medea 接收自然语言形式的 omics objective 和可选实验说明，输出基于工具、数据和文献证据的分析报告，或在证据不足时 abstain。

系统由四个模块组成：

1. **ResearchPlanning**：构建研究计划，并做 context verification 和 integrity verification，确保疾病、细胞类型、队列、工具选择与任务一致。
2. **Analysis**：执行代码和工具调用，包含 pre-run checks 和 post-run verification。它包括 CodeGenerator、AnalysisExecution、CodeDebugger、AnalysisQualityChecker 等组件。
3. **LiteratureReasoning**：检索文献并评估 relevance 和 evidence strength，避免只依赖 LLM parametric memory。
4. **MultiRoundDiscussion**：把数据分析、文献推理和其他模块证据进行多轮讨论与共识整合，生成最终报告或 calibrated abstention。

Medea 使用 20 个工具，覆盖 single-cell 和 bulk transcriptomic datasets、cancer vulnerability maps、pathway knowledge bases、machine learning models 和相关数据库/API。

## 关键结果

1. 论文在 5,679 个 open-ended analyses 上评估 Medea。
2. 三个评测域分别是：
   - target identification：五种疾病和 cell type contexts，共 2,400 个 analyses；
   - synthetic lethality reasoning：七个 cell lines，共 2,385 个 analyses；
   - immunotherapy response prediction：bladder cancer，共 894 个 patient-level analyses。
3. Medea 相比 existing approaches，target identification 最高提升 46%，synthetic lethality 最高提升 22%，immunotherapy response prediction 最高提升 24%。
4. Medea 同时保持低 failure rates 和 calibrated abstention。
5. 消融和对照涉及不同 LLM、tool sets、omics objectives 和 agentic modules，表明提升来自 verification-aware design，而不只是更长流程。

## 与综述的关联

在 Scientific Workflow 中，Medea 覆盖 Knowledge Grounding、Result Analysis、Hypothesis Generation、Verification 和 Synthesis。它把治疗发现中的组学分析组织成可追踪的工具链。

在 Skill Lifecycle 中，它对应：

- Representation：omics analysis skill、tool skill、evidence-strength assessment；
- Retrieval：数据库、文献和模型工具检索；
- Composition：planning、analysis、literature reasoning、discussion 四模块组合；
- Execution：代码执行、数据库/API 调用、模型运行；
- Verification：pre-run/post-run checks、context verification、evidence reconciliation、abstention。

Evidence Role 应标为 **Direct**。Medea 直接支持“scientific agent 的能力来自可验证中间步骤，而不是只来自更自动化的 workflow”。它与 BioMedAgent、CellVoyager 和 GeneAgent 形成一条 biomedical data-analysis agent 证据链。

## 局限性

Medea 目前是 preprint，尚未经过期刊同行评议。评测主要集中在 omics 和治疗发现的计算分析，不等于已完成湿实验验证。系统依赖预定义的 20 个工具和构造好的任务域，迁移到全新疾病、全新数据类型或真实临床决策仍需额外验证。

## 核心贡献

Medea 的核心贡献是把 therapeutic discovery 中的组学分析变成 verification-aware long-horizon agent workflow，通过工具执行、文献证据和多轮共识显著提高开放式治疗发现任务表现。
