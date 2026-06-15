# PANGAEA-GPT 2026

## 基本信息

- **论文**: A Hierarchical Multi-Agent System for Autonomous Discovery in Geoscientific Data Archives
- **年份**: 2026
- **来源**: arXiv:2602.21351
- **系统名称**: PANGAEA-GPT
- **关键词**: hierarchical multi-agent, geoscientific data archives, supervisor-worker topology, sandboxed code execution, execution feedback

## 摘要要点

PANGAEA-GPT 面向地球科学数据档案中的 autonomous discovery。系统采用 Supervisor-Worker topology、data-type-aware routing 和 sandboxed deterministic code execution，把地球科学数据检索、代码执行、结果分析和反馈修正组织成层级式多智能体工作流。

## 方法动机

地球科学数据档案通常包含异构数据类型、复杂元数据、不同空间/时间尺度和多步分析流程。普通 LLM 难以可靠完成数据定位、数据类型识别、代码生成、执行和结果解释。PANGAEA-GPT 的目标是用层级式 agent workflow 将这些任务拆开，并通过受控执行环境降低错误风险。

## 方法设计

系统结构包括：

1. Supervisor 接收用户科学问题或数据分析需求。
2. Supervisor 识别数据类型、任务类型和需要调用的 worker。
3. Worker agents 面向不同 geoscientific data types 或分析任务执行操作。
4. 系统在 sandbox 中运行 deterministic code，避免非受控执行。
5. 执行结果和错误信息返回给 Supervisor。
6. Supervisor 根据反馈修正计划、重新路由或要求 worker 重新执行。
7. 最终输出数据分析结果、图表或解释。

与普通 RAG 问答不同，PANGAEA-GPT 的关键在于执行：它把地球科学数据发现放进可运行、可反馈的 code execution loop。

## 与其他方法的区别

| 方法类型 | 局限 | PANGAEA-GPT 的特点 |
|---|---|---|
| 单 agent 数据问答 | 容易只停留在文本解释 | 增加 sandboxed code execution |
| 通用数据分析 agent | 不理解 geoscience 数据类型 | 加入 data-type-aware routing |
| 固定 pipeline | 难以适应开放查询 | Supervisor 动态分配 worker |

## 实验与结果

论文展示系统可在 geoscientific data archives 上完成数据查询、执行和分析任务。其关键证据是 supervisor-worker routing、deterministic execution 和 execution-feedback self-correction 能提升地球科学数据分析任务的可控性。

## 局限性

- 它偏数据发现与分析，不是完整假设到实验的闭环。
- `Y1` 主要来自 execution feedback 和 self-correction，不应写成 artifact evolution。
- 地球科学贡献需要结合具体 case 和专家验证，不应只凭代码执行判断。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | Supervisor-Worker 是明确层级式多智能体结构 |
| Y | `Y1` | 主要机制是 execution-feedback self-correction |
| Z | `Z1,Z4,Z5,Z7` | 覆盖数据 grounding、执行、分析和验证 |

## 对综述的价值

PANGAEA-GPT 可补 `X4-Y1` 区域，说明层级多智能体也适用于地球科学数据档案中的检索、执行和分析。它适合第 4 章 supervisor-worker coordination 和第 6 章 code/data execution substrate。

