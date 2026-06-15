# RD-Agent 2025

## 基本信息

- **论文**: RD-Agent: Automating Data-Driven AI Research and Development
- **年份**: 2025
- **来源**: arXiv:2505.14738
- **系统名称**: RD-Agent
- **关键词**: data science, research agent, developer agent, exploration traces, code implementation, performance feedback

## 摘要要点

RD-Agent 面向 data-driven AI R&D，将 Researcher 与 Developer 两个 agents 组织成研究-实现-评估闭环。Researcher 负责 idea generation 和 experiment proposal，Developer 负责代码实现和运行，系统通过 exploration traces、代码结果和性能反馈合并推进下一轮研究。

## 方法动机

数据科学研发通常需要在想法、实现、实验结果和下一轮改进之间往返。单 agent 容易在 ideation 和 engineering 之间混淆职责。RD-Agent 的动机是把 research thinking 和 development execution 分开，让 idea 可以被快速实现、评估和演化。

## 方法设计

流程包括：

1. Researcher 根据任务、历史结果和数据上下文提出研究想法。
2. Developer 将想法转成代码、pipeline 或实验脚本。
3. 系统执行代码并获得性能指标。
4. 结果、错误和代码 diff 被写入 exploration traces。
5. Researcher 基于 traces 生成下一批想法。
6. 多条 traces 可以并行探索并被合并，保留更优方向。

这是一种 artifact-level evolution：演化对象是 idea-code-performance trace，而不是 agent memory 本身。

## 实验与结果

论文展示 RD-Agent 可用于数据科学和 AI R&D 场景，通过 researcher/developer 协作和性能反馈不断改进解决方案。其贡献在于把研究想法和代码执行连成自动研发循环。

## 局限性

- 更偏 AI/data science R&D，不是传统自然科学实验系统。
- 结果依赖 benchmark、执行环境和自动评估指标。
- 若评估指标片面，演化可能朝 benchmark overfitting 方向收敛。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | Researcher 与 Developer 是固定异质角色 |
| Y | `Y4` | exploration traces、实现和性能反馈推动 artifact evolution |
| Z | `Z2,Z3,Z4,Z5,Z7,Z8` | 覆盖 idea、代码设计、执行、分析、验证和迭代 |

## 对综述的价值

RD-Agent 可作为 code/notebook substrate 中 artifact evolution 的证据，说明多智能体 ASD 可以把 idea generation 与 executable research artifact 绑定起来。

