# Perplexity Skills Guide 2026

## 基本信息
- **论文**: Designing, Refining, and Maintaining Agent Skills at Perplexity
- **作者**: Perplexity Research Team
- **年份**: 2026
- **来源**: https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity (published 27 May 2026)
- **关键词**: skill-engineering, agent-infrastructure, skill-management, progressive-loading, routing

## 核心思想
Perplexity 分享了其 Agent 技能工程实践框架。将 Skill 定义为包含 SKILL.md 的目录（而非文件），通过渐进式加载（Index → Load → Runtime 三层次）控制 Token 成本，并提供从构建、迭代到维护的完整方法论。

## 方法细节
- **Skill 的四个维度定义**：
  - 目录结构：hub-and-spoke 架构，SKILL.md 为中心，scripts/、references/、assets/、config/ 为辐条。
  - 格式规范：name + description（路由触发而非文档） + depends 依赖机制。
  - 可调用性：运行时通过 load_skill() 渐进加载到隔离沙箱。
  - 渐进式三级 Token 预算：Index（~100 token/skill，所有用户承担）→ Load（~5000 token/skill）→ Runtime（无上限，仅显式调用时加载）。
- **构建流程（6步）**：先写 Evals → 写 Description（最难；建议以 "Load when..." 开头，50 words or fewer）→ 写 Body（跳过模型已知内容，聚焦 gotcha）→ 利用层级结构 → 迭代 → 发布。
- **维护飞轮**：以追加为主，gotcha 随时间增长；Agent 失败→加 gotcha，路由错→收紧 description 并加 negative eval，漏加载→加关键词和 positive eval；若 system prompt 变化，要检查 skill 之间的竞争或重复。
- **Eval 体系**：加载精确率/召回率、渐进加载、端到端任务完成、跨模型测试（GPT/Claude Opus/Sonnet）。

## 关键结果
- 提出“技能工程”概念，将 Agent 能力的组织和管理系统化。
- 渐进加载机制有效平衡了 Token 成本与上下文丰富度。
- 路由描述的质量（“Load when...”）是技能系统成败的关键，微小措辞变化可产生巨大影响。
- 核心理念：“good documentation for humans is most often bad documentation for models” — 需要为模型而非人类编写 Skill。
- 文章用美国税务技能的例子说明渐进式加载的收益：索引只暴露简短描述，真正需要时才加载 `SKILL.md`，再按需读取 1945 年以后的税率表等细节资源，避免把大量无关背景塞进上下文。
- 警示：LLM 无法可靠地编写其自身受益的程序性知识，不建议自动生成 Skill。

## 局限性
- 这是一份工程实践指南，不是同行评审论文或系统性实验评测。
- 技能效果高度依赖人工编写的 description、gotcha 和 eval；自动生成技能反而被文章明确警示。
- Perplexity 语境中的 skill 偏产品化工程机制，不能直接等同于可执行科研 protocol 或经过实验验证的科学技能。

## 核心贡献
Perplexity Skills Guide 2026 的核心贡献是把 Agent Skill 明确定义为“可渐进加载的目录化上下文工程单元”，并给出 description 路由、hub-and-spoke 结构、eval-first 开发和 append-mostly 维护的工程方法论。

## 与综述的关联
- 提供了 Agent 技能管理的工程实践，可直接指导科学发现 Agent 的技能体系建设。
- 科学发现 Agent 需要管理大量领域特定技能（如数据分析、文献检索、实验设计），Perplexity 的层级化和渐进加载方案具有直接可迁移性。
- Eval 驱动的开发模式为科学发现 Agent 的技能加载、文件读取和端到端任务完成评测提供方法论参考。
- “append-mostly”维护策略适用于科学发现 Agent 知识的持续积累和更新，但对变化过快的外部工具或数据库，原文反而建议不要写成 Skill，以免产生 drift。
