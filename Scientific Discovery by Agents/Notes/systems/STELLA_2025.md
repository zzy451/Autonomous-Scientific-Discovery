# STELLA 2025

## 基本信息
- **论文**: STELLA: Self-Evolving LLM Agent for Biomedical Research
- **作者**: Ruofan Jin, Zaixi Zhang, Mengdi Wang, Le Cong
- **年份**: 2025
- **来源**: arXiv:2507.02004
- **关键词**: system, biomedical-agent, tool-use, self-evolving, skill-evolution

## 核心思想
Biomedical research agents 需要在不断变化的工具、数据库和任务需求中保持能力更新。固定工具集和静态 prompt 很难覆盖不断扩展的 biomedical analysis 需求。

STELLA 要解决的问题是：如何构建一个能够发现、组织和复用工具，并从任务经验中自我演化的 biomedical research agent。

## 方法细节
STELLA 强调 self-evolving workflow，核心由 **Dynamic Tool Ocean** 与 **Knowledge Evolution** 两部分支撑：前者负责工具发现、选择和创建，后者把任务经验沉淀为可复用模板。

核心组件包括：

1. **Dynamic Tool Ocean**：允许系统维护和扩展可用工具池；
2. **Tool Creation Agent**：在现有工具不足时生成或包装新工具；
3. **template library / Knowledge Evolution**：保存可复用的任务解决模板；
4. **tool discovery / selection**：根据 biomedical task 选择合适工具；
5. **experience accumulation**：从已完成任务中沉淀可复用流程；
6. **iterative solving**：根据结果和失败反馈更新后续执行。

## 关键结果

1. STELLA 在 biomedical benchmarks 上达到 state-of-the-art accuracy。
2. 公开摘要报告其在 Humanity's Last Exam: Biomedicine 上约 **26%**，在 LAB-Bench: DBQA 上约 **54%**，在 LAB-Bench: LitQA 上约 **63%**。
3. 相比 leading models，STELLA 最高提升约 **6 percentage points**。
4. 论文强调 STELLA 的表现会随 experience 系统性提升，例如在 Humanity's Last Exam benchmark 上，accuracy 随 trials 增加接近翻倍。

## 与综述的关联

在 Scientific Workflow 中，STELLA 覆盖 Knowledge Grounding、Execution、Result Analysis 和 Evolution。

在 Skill Lifecycle 中，它对应 Acquisition / tool discovery、Retrieval / tool selection、Composition / tool-chain 和 Evolution / template update。

Evidence Role 应标为 **Direct**。它直接补足我们框架中最薄弱的 Evolution 维度：scientific agent 如何维护动态工具池和任务模板。

## 局限性

STELLA 仍是 arXiv 候选，需要核查 benchmark 覆盖、工具池质量和 self-evolution 是否真正超过简单经验缓存。它主要面向 biomedical research，不代表所有科学领域。

## 核心贡献

STELLA 的核心贡献是把 biomedical research agent 的能力建模为可演化工具池和模板库，提供 scientific skill evolution 的直接候选证据。
