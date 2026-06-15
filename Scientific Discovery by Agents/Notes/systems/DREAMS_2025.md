# DREAMS 2025

## 基本信息

- **论文**: DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Screening
- **年份**: 2025
- **来源**: arXiv:2507.14267
- **系统名称**: DREAMS
- **关键词**: DFT simulation, materials screening, hierarchical multi-agent, HPC scheduling, convergence error handling

## 摘要要点

DREAMS 是面向 DFT simulation 的 hierarchical multi-agent framework。系统结合 central LLM planner agent 与 domain-specific LLM agents，分别处理 atomistic structure generation、systematic DFT convergence testing、HPC scheduling 和 error handling。论文特别强调 convergence error handling agent 用于提高 DFT 计算鲁棒性。

## 方法动机

DFT 是材料发现的重要执行基底，但真实 DFT 工作流涉及结构准备、参数选择、收敛测试、HPC 作业调度、输出解析和失败修复。单个 LLM 很容易在长流程中遗漏步骤或无法处理收敛错误。DREAMS 的目标是用层级式 agent 结构把这些专业步骤组织起来。

## 方法设计

流程可以概括为：

1. 用户给出材料筛选或 DFT 任务。
2. central planner 将任务拆成结构生成、计算设置、收敛测试、HPC 调度和结果分析。
3. domain agents 分别生成结构、准备 DFT 输入、提交/监控 HPC 作业。
4. convergence / error-handling agent 读取输入输出文件，诊断失败原因并建议参数调整。
5. planner 根据执行反馈插入缺失步骤或重新规划。
6. 最终汇总计算结果和筛选判断。

DREAMS 的关键是把 DFT pipeline 中的错误恢复纳入 agent workflow，而不是只做一次性脚本生成。

## 实验与结果

论文展示 DREAMS 能在 DFT simulation 场景中组织多步计算，并通过专门 convergence error handling 提升对计算挑战的鲁棒性。公开项目页也强调 supervisor、DFT、HPC 和 convergence agents 通过共享 Canvas 协同。

## 局限性

- 主要覆盖 DFT simulation，不是完整 wet-lab materials discovery。
- 反思机制集中在计算失败与收敛问题，不是广义 hypothesis evolution。
- 结果可靠性仍取决于 DFT 参数、势函数/泛函选择和领域专家解释。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | central planner 调度结构生成、DFT、HPC 和 error-handling agents |
| Y | `Y1` | 执行反馈、收敛诊断和重规划属于反思/自我修正 |
| Z | `Z3,Z4,Z5,Z7,Z8` | 覆盖仿真设计、执行、结果分析、计算检查和迭代 |

## 对综述的价值

DREAMS 可作为 simulation substrate 中层级式多智能体的证据，说明 ASD 的执行层需要专门 agents 处理 HPC、收敛错误和计算 provenance。

