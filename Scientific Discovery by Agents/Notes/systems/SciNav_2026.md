# SciNav 2026

## 基本信息
- **论文**: SciNav: A General Agent Framework for Scientific Coding Tasks
- **作者**: Tianshu Zhang, Huan Sun
- **年份**: 2026
- **来源**: ICLR 2026; arXiv:2603.20256
- **关键词**: system, scientific-coding, code-agent, benchmark

## 核心思想
大量科学任务需要写代码、运行实验、调试错误和解释输出。通用 code agent 往往面向软件工程，而 scientific coding tasks 有更强的领域约束、实验语义和结果解释需求。

SciNav 要解决的问题是：如何为 scientific coding tasks 构建通用 agent framework，使模型能在多候选方案中探索、执行和选择更可靠的 scientific code。

## 方法细节
SciNav 使用 guided search over coding solutions。

核心机制包括：

1. 根据科学任务生成多个解决方案；
2. 构建 top-K tree search；
3. 运行候选代码并收集反馈；
4. 使用 relative judgment 比较不同候选；
5. 选择更优路径并继续调试。

## 关键结果

1. SciNav 在 **ScienceAgentBench** 和 **DA-Code** 两类 scientific coding benchmark 上验证，覆盖不同任务类型、难度水平和 base models。
2. 在 ScienceAgentBench 上，相比最强 baseline Self-Debug，SciNav 最高取得 **24%** success rate 相对增益和 **7.8** 个 absolute points 的 valid execution rate 提升；相比 OpenHands，success rate 相对增益为 **22.9%**。
3. 在 DA-Code 上，SciNav 在 data manipulation 与 statistical analysis 任务上取得 **29** 个 absolute points 提升，平均提升 **13** 个 absolute points，并在不同难度层级上有 **10%--23%** absolute gain。
4. 相比 random selection 和 LLM absolute scoring，relative judgment-guided top-K search 更能区分候选方案质量，并在 constrained search budgets 下提升 scientific coding 解题质量。

## 与综述的关联

在 Scientific Workflow 中，SciNav 覆盖 Execution、Result Analysis 和 Verification。

在 Skill Lifecycle 中，它对应 Representation / code skill、Composition / search tree、Execution / code run 和 Verification / relative judgment。

Evidence Role 应标为 **Direct**。SciNav 补足 scientific coding 这一中间层：它位于纯工具调用和完整科学发现之间，是很多 scientific agent 实际落地的执行核心。

## 局限性

SciNav 仍是 coding task framework，不直接验证真实科学发现。relative judgment 的可靠性和科学领域泛化需要进一步核查。

## 核心贡献

SciNav 的核心贡献是将 scientific coding tasks 组织为可搜索、可执行、可比较的 agent workflow，为科研代码执行 skill 提供机制样本。
