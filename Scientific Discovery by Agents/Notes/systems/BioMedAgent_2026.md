# BioMedAgent 2026

## 基本信息
- **论文**: Empowering AI Data Scientists Using a Multi-Agent LLM Framework with Self-Evolving Capabilities for Autonomous, Tool-Aware Biomedical Data Analyses
- **作者**: Dechao Bu, Jingbo Sun, Kun Li, Zihao He, Wei Huang, Jinlin Hu, Shanshan Zhang, Shuangshuang Lei, Peipei Huo, Zhihao Wang, et al.
- **年份**: 2026
- **来源**: Nature Biomedical Engineering, doi:10.1038/s41551-026-01634-6; PubMed:41912700; code:https://github.com/BOBQWERA/BioMedAgent
- **关键词**: biomedical-data-analysis, multi-agent, tool-aware-agent, self-evolving, bioinformatics

## 核心思想
BioMedAgent 关注的是生物医学数据分析中的 agent 自动化：生物医学研究者常需要跨 bioinformatics、AI、统计、编程和可视化工具完成多步分析，但 Galaxy、Seven Bridges 等平台依赖预定义 workflow，对自然语言任务输入和可读报告支持不足。通用 LLM 虽然具备语言理解能力，但在复杂生物医学分析中容易卡在任务规划、工具选择、代码执行和多步推理上。

论文的目标是让没有专门计算或生物信息学训练的生物医学专业人员，通过自然语言发起任务，由 multi-agent framework 自动规划、调用工具、执行分析并生成结果。

## 方法细节
BioMedAgent 是一个 LLM-powered multi-agent framework，强调 **tool-aware biomedical data analysis** 和 **self-evolving capabilities**。公开摘要和代码说明中明确提到两个核心算法：

- **Interactive Exploration (IE)**：用于多 agent 协作式规划、编码和执行，让系统在任务执行过程中探索可行路径。
- **Memory Retrieval (MR)**：用于利用已有经验和工具信息，提高后续任务中的规划与工具调用能力。

系统支持自然语言任务输入，并通过多个 agent 协作完成 planning、coding、execution。代码仓库中的 `tool_info.json` 记录了工具的名称、描述、输入和输出 schema，当前公开配置包含 **65 个工具**，覆盖机器学习、统计分析、组学处理、变异分析、图像分割、可视化等任务。例如工具包括 AdaBoost 分类、BAM-to-VCF、Mutect2、BWA/Samtools/Sambamba、BasicUNet 细胞分割等。

README 还说明，用户可以通过补充工具代码和文档扩展工具集合，BioMedAgent 会自动感知新工具并在新问题中使用。这一点使它更接近“可扩展 tool skill library”，而不是固定流程脚本。

## 关键结果

1. **BioMed-AQA benchmark**  
   作者构建 BioMed-AQA，用于评估 LLM applications 在 biomedical analyses 中的能力。该 benchmark 包含 **327 个 manually curated bioinformatic analyses questions**，覆盖五类任务：omics analyses、precision medicine support analyses、machine learning、statistical analyses、data visualization。

2. **总体成功率 77%**  
   BioMedAgent 在 BioMed-AQA 上达到 **77% average success rate**，超过两种 OpenAI web agent applications 和一种本地 agent application；这些对照也基于 GPT-4o-mini。

3. **优于 ChatGPT-4o application**  
   README 和 PubMed 摘要均报告，BioMedAgent 超过使用更大模型的 ChatGPT-4o application；ChatGPT-4o application 的成功率为 **47%**。

4. **外部泛化到 BixBench**  
   PubMed 摘要指出 BioMedAgent generalized robustly to the external **BixBench** dataset，但公开摘要中没有给出具体分项数字；这一点应作为泛化证据记录，但不能过度解读为已覆盖所有生物医学分析场景。

5. **真实任务类型覆盖较宽**  
   摘要称系统能 autonomously perform cross-omics analysis、machine-learning model construction and bioinformatics protocol generation。README demo 覆盖 machine learning、statistics t-test、QQ plot、survival plot、violin plot 和 omics。

## 与综述的关联

BioMedAgent 是科学发现 Agent 中 **Result Analysis + Execution + Evolution** 的直接证据。它不主要提出新假设，也不直接执行湿实验；它补足的是科学发现流程中经常被低估的一段：如何把自然语言研究问题转成可执行的数据分析 workflow。

在 Scientific Workflow 中，它覆盖 Result Analysis、Execution、Synthesis，并通过报告生成间接支持 Knowledge Grounding。  

在 Skill Lifecycle 中，它对应：

- Representation：工具文档、输入输出 schema 和分析 workflow 可视为 tool/protocol skill。
- Retrieval：Memory Retrieval 和工具文档检索支持复用已有经验。
- Composition：multi-agent planning 将多个工具组合成分析链。
- Execution：代码运行、统计分析、组学处理和可视化。
- Evolution：self-evolving capabilities 和历史经验复用。
- Verification：BioMed-AQA success rate 与外部 BixBench 泛化，但仍不是严格的生物实验验证。

Evidence Role 应标为 **Direct**。它直接支持“科学 Agent 的技能不只在假设生成和实验设计，也包括数据分析工具链的自动组织与执行”。

## 局限性

- 公开摘要和代码说明没有给出完整分项表格，77% 和 47% 是核心可定位数字，但各类别、各 baseline 的细粒度表现需以后续全文或补充材料核对。
- 系统主要面向计算型 biomedical data analysis，不等同于湿实验自动化或真实药物/机制发现。
- BioMed-AQA 是作者新构建 benchmark，外部独立复现和跨实验室验证仍需观察。
- 工具调用依赖本地环境、Docker 镜像和工具文档质量；新工具“自动感知”仍取决于用户是否提供清晰 schema 和可执行代码。
- 成功率评价可能受任务定义、答案标注和执行环境影响，不能直接与普通 QA benchmark 的准确率等同。

## 核心贡献

BioMedAgent 的核心贡献是把 biomedical data analysis 表示为可由 multi-agent 自动规划、检索、组合和执行的工具链任务，并用 BioMed-AQA 量化显示其在自然语言驱动的生物医学分析中显著优于通用 LLM agent 应用。
