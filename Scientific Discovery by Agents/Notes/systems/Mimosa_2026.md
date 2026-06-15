# Mimosa 2026

## 基本信息

- **论文**: Mimosa Framework: Toward Evolving Multi-Agent Systems for Scientific Research
- **年份**: 2026
- **来源**: arXiv:2603.28986
- **系统名称**: Mimosa Framework
- **关键词**: evolving multi-agent systems, scientific research workflow, meta-orchestrator, workflow topology, judge feedback

## 一句话总结

Mimosa 是一个面向科学研究任务的 evolving multi-agent framework：它不是固定写死科研流程，而是由 meta-orchestrator 根据任务生成 task-specific workflow topology，调度多个 code-generating agents，并通过 judge feedback 对工作流和中间产物进行迭代改进。

## 研究问题

许多 agentic science 系统把科研流程固定为若干预设角色，例如 planner、coder、critic 或 reviewer。Mimosa 关注的问题是：科学任务差异很大，系统能否根据任务自动形成更合适的多智能体工作流，而不是依赖人工预设拓扑。

因此，Mimosa 的价值不主要在某一个科学发现案例，而在于补充本文的 **harness / workflow evolution** 证据：演化对象不是单个答案，而是支撑科研执行的 agentic harness。

## 系统架构

Mimosa 的核心是一个层级式多智能体框架：

| 组件 | 作用 |
|---|---|
| Meta-orchestrator | 根据研究任务生成和调整 workflow topology |
| Code-generating agents | 生成实验/分析代码或任务解法 |
| Judge / evaluation module | 对结果进行评分、反馈和 refinement |
| Iterative controller | 基于反馈更新后续尝试 |

这种结构使 Mimosa 更接近 `X4: 层级式多智能体`，而不是普通 X2 固定角色团队。

## 关键机制

### 1. Task-specific workflow topology

Mimosa 将 workflow topology 视为可调整对象。不同科研任务可以触发不同 agent 组织方式，这与本文所说的 harness evolution 直接相关。

### 2. Judge feedback 驱动迭代

系统使用 judge feedback 评价候选执行结果，并将反馈用于 refinement。这说明优化对象不仅包括输出代码或答案，也包括后续 agent 调度和工作流配置。

### 3. 科学任务执行

Mimosa 的实验主要围绕 scientific research benchmark / ScienceAgentBench 类型任务展开，强调科学任务中的代码生成、执行和评估。

## XYZ 分类

建议分类为：

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | meta-orchestrator 调度多个 task agents，体现层级式多智能体 |
| Y | `Y5` | workflow topology / harness 本身可被生成、调整和反馈改进 |
| Z | `Z3,Z4,Z5,Z7,Z8` | 覆盖实验/代码设计、执行、结果评估、验证和迭代 |

建议放入 **ASD 相关系统**，而不是严格 ASD 系统：它是强 workflow/harness 证据，但是否完成真实科学发现闭环仍需逐任务判断。

## 对综述的价值

Mimosa 可以补当前矩阵中缺失的 `X4-Y5-*` 坐标。它使第 5 章的 harness evolution 不只依赖 Science Earth、Kosmos 或一般 memory/skill 系统，而有一个更直接的层级多智能体 workflow-evolution 案例。

## 局限性

- 主要证据来自 benchmark 式科学任务，不等同于真实实验室发现。
- workflow evolution 是否带来稳定的科学质量提升，需要看更多跨任务消融。
- judge feedback 可能继承 benchmark 偏差，不能替代领域专家或物理验证。

