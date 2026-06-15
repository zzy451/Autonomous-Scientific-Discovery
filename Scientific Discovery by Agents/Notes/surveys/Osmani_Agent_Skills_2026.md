# Osmani Agent Skills 2026

## 基本信息
- **论文**: Addy Osmani's Agent Skills — 生产级工程技能库
- **作者**: Addy Osmani (Engineering Leader on Google Chrome / Head of Chrome Developer Experience)
- **年份**: 2026
- **来源**: https://github.com/addyosmani/agent-skills
- **关键词**: 工程技能, AI编程智能体, 软件工程实践, 技能工作流, Google 工程文化

## 核心思想
Addy Osmani（Google Chrome engineering leader，《Software Engineering at Google》作者之一）创建的"生产级工程技能库"，为 AI 编程智能体提供结构化的工程纪律工作流。核心哲学：AI 编程智能体默认走捷径（跳过规格、测试、评审），这些技能将 Google 工程文化的严谨性——包括 Google 工程实践指南与《Software Engineering at Google》中的核心原则——编码为可复用的分步流程。仓库 README 明确给出 Claude Code、Cursor、Gemini CLI、Windsurf、OpenCode、GitHub Copilot、Kiro 和 Codex/Other Agents 的接入方式；GitHub star 数会变化，不应作为稳定证据。

## 方法细节
- **规模与 Meta**：仓库包含 23 个 skills（22 个生命周期技能 + 1 个 `using-agent-skills` meta-skill）。`using-agent-skills` 用于识别当前任务阶段并匹配对应技能。
- **Define（定义）**：`interview-me`（一问一答式需求访谈，直至 95% 置信度）、`idea-refine`（发散-收敛思维，将模糊想法具体化）、`spec-driven-development`（代码前先写 PRD，覆盖目标/命令/结构/代码风格/测试/边界）。
- **Plan（规划）**：`planning-and-task-breakdown`——将规格分解为可验证的小任务，明确依赖关系与验收标准。
- **Build（构建）**：`incremental-implementation`（薄垂直切片，Feature Flag，安全回滚）、`test-driven-development`（Red-Green-Refactor，测试金字塔 80/15/5，DAMP over DRY，Beyonce Rule）、`context-engineering`（上下文打包与 MCP 集成）、`source-driven-development`（基于官方文档而非猜测）、`doubt-driven-development`（对抗性审视每个非平凡决策）、`frontend-ui-engineering`（WCAG 2.1 AA 无障碍标准）、`api-and-interface-design`（Hyrum's Law，契约优先，One-Version Rule）。
- **Verify（验证）**：`browser-testing-with-devtools`（Chrome DevTools MCP 实时调试）、`debugging-and-error-recovery`（五步排查：复现-定位-缩小-修复-防护）。
- **Review（评审）**：`code-review-and-quality`（五维评审，变更大小 ~100 行，严重性标注 Nit/Optional/FYI）、`code-simplification`（Chesterton's Fence 原则）、`security-and-hardening`（OWASP Top 10，三层边界体系）、`performance-optimization`（Core Web Vitals 测量优先）。
- **Ship（发布）**：`git-workflow-and-versioning`（Trunk-Based Development，原子提交）、`ci-cd-and-automation`（Shift Left，Faster is Safer）、`deprecation-and-migration`（Code-as-Liability 思维）、`documentation-and-adrs`（Architecture Decision Records）、`shipping-and-launch`（Feature Flag 生命周期，分阶段发布）。

## 关键结果
- **反合理化表（Anti-Rationalization）**：每个技能包含 AI 常见"走捷径"借口的系统性反驳。例如，TDD 技能针对"I'll add tests later"（测试永远不会有"稍后"）、增量实现技能针对"This change is too small to flag"（小变更可能引发级联故障）。这种"预判+反驳"的设计使技能不仅是指导文档，更像是带有执行强制力的工程流程。
- **验证不可协商（Verification is non-negotiable）**：每个技能以具体证据要求收尾——测试通过、构建成功、运行时数据、性能指标。"看起来没问题"从不是充分条件。这一原则直接对治 AI 智能体在复杂任务中的"表面完成"问题。
- **7 个斜杠命令 + 自动激活**：`/spec`（定义）→ `/plan`（规划）→ `/build`（构建）→ `/test`（验证）→ `/review`（评审）→ `/code-simplify`（简化）→ `/ship`（发布）一键激活对应技能链。此外，技能也基于上下文自动激活——设计 API 时自动触发 `api-and-interface-design`，构建 UI 时自动触发 `frontend-ui-engineering`。
- **3 个专业 Personas**：`code-reviewer`（高级工程师视角，五维评审）、`test-engineer`（QA 专家，覆盖率分析 + Prove-It 模式）、`security-auditor`（安全审计工程师，OWASP 评估 + 威胁建模）。
- **4 个参考清单**：测试模式（结构/命名/Mock/反模式）、安全清单（Pre-commit 检查/认证/输入验证/OWASP Top 10）、性能清单（Core Web Vitals 目标/前后端清单）、无障碍清单（键盘导航/屏幕阅读器/ARIA）。

## Google 工程文化的嵌入
技能直接编码了 Google 工程实践的核心原则，源自《Software Engineering at Google》与 Google 工程实践指南：
- API 设计中的 **Hyrum's Law**："当 API 有足够多用户时，契约中的任何东西都不重要——所有可观察行为都会被人依赖。"
- 测试中的 **Beyonce Rule** + 测试金字塔（80% 单元/15% 集成/5% E2E）+ DAMP (Descriptive And Meaningful Phrases) over DRY。
- 代码评审中的 **变更大小规范**（~100 行/次）+ 评审速度标准（< 24h 初评）+ 严重性标注（Nit/Optional/FYI）。
- 简化中的 **Chesterton's Fence**：不理解为什么存在之前不要移除。
- CI/CD 中的 **Shift Left**（质量左移）+ **Faster is Safer**（更快发布更安全）原则。
- Git 中的 **Trunk-Based Development** + 原子提交 + commit-as-save-point 模式。
- 将"代码视为负债"（Code-as-Liability）的弃用迁移技能，包含 compulsory vs advisory deprecation 分类。

## 局限性
- 该工作是工程技能库和实践文档，不是同行评审论文；GitHub stars 和平台适配情况只能说明社区关注度，不能直接证明技能对科研任务有效。
- 技能内容主要面向软件工程，迁移到科学发现时还需要补充实验设计、统计检验、数据治理、实验安全和领域工具链约束。
- 其工作流强调人类工程纪律的编码化，尚未证明 agent 能在长期自主运行中稳定选择、组合和更新这些技能。

## 核心贡献
Osmani Agent Skills 的核心贡献是把生产级软件工程纪律拆成可复用、可触发、可审查的 agent skill，为科学发现 agent 如何避免“跳过规格、测试和评审”提供了可迁移的工程模板。

## 与综述的关联
- 科学发现智能体的"工程最佳实践"——科研系统面临相同的代码质量、实验可复现性、安全合规挑战。Osmani 的技能方法论（规格先行、增量构建、独立验证、弃用管理）可直接推广至 AI-Researcher 等系统的实验代码生成环节。
- 与 Anthropic Skills（平台实现）、Agent Skills Spec（跨平台标准）、GStack（工程编排）共同构成技能生态的工业实践维度——从标准规范到生产级应用。
- 反合理化表的设计模式为科学发现智能体提供了"防走捷径"的模板——科研智能体同样会在实验设计、数据分析、论文写作中走捷径，针对性的反合理化表可强制执行科学严谨性。
