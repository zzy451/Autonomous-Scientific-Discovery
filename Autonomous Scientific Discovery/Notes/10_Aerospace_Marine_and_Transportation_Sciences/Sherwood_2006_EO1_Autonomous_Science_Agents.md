# Sherwood et al. 2006 - Autonomous Science Agents and Sensor Webs: EO-1 and Beyond

**论文信息**
- 标题：Autonomous Science Agents and Sensor Webs: EO-1 and Beyond
- 作者：Rob Sherwood; Steve Chien; Daniel Tran; Benjamin Cichy; Rebecca Castano; Ashley Davies; Gregg Rabideau
- 年份：2006
- 来源 / venue：IEEE Aerospace Conference
- DOI / arXiv / URL：https://ai.jpl.nasa.gov/public/papers/sherwood-ieeeaero06-beyond.pdf
- PDF / 本地文件路径：当前笔记基于官方 PDF
- 论文类型：系统论文 / EO-1 mission-science autonomy
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-20 relaxed multi-module revision

```text
scientific_object_modules: 05;10
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 10
first_hand_sources_checked: JPL PDF
classification_evidence_source_level: first_hand_full_text
module_assignment_evidence: `05` is supported by Earth science events including volcanoes, floods, ice, clouds, and crust deformation; `10` is supported by EO-1 spacecraft / sensor-web autonomous science analysis, replanning, and retasking.
multi_module_object_coverage_note: Under the relaxed rule, Earth-science event detection and follow-up are counted as `05` object coverage even though the record remains filed under spacecraft mission-science autonomy.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official PDF abstract | 明确写为 autonomous science agent，含 onboard analysis、planning、robust execution | 高 |
| 科学对象归类 | `10.02` | abstract +正文概述 | 主对象是 EO-1 mission-science operation / sensor-web retasking | 高 |
| 方法流程 | 多步闭环 | abstract | science event detection -> replanning -> retasking -> execution | 高 |
| 实验验证 | 真实平台 | official PDF | 依托 EO-1 与 sensor-web 实际任务环境 | 高 |
| 边界判断 | 不转 `05` | object-first reading | 火山、洪水等只是触发场景，不是论文最终对象 | 高 |

## 0. 摘要翻译

本文描述 EO-1 卫星上的 Autonomous Science Agent 及其向 sensor web 扩展的工作。系统在轨完成科学事件检测、规划与重规划、鲁棒执行以及响应式再观测，从而在通信和资源受限条件下提高科学回报，并与其他卫星和地面传感器形成联动。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确 mission-science 目标，包含多步在轨分析、规划、执行和反馈
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：部分是
- 在科研流程中承担的明确角色：science-event detection、retasking、mission replanning、execution control

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：EO-1 onboard mission-science autonomy
- 四级专题：EO-1 autonomous mission-science agents
- 四级专题是否为新增：否
- 归类理由：对象稳定指向 spacecraft mission autonomy
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：EO-1 spacecraft autonomous mission-science operations
- 最终科学问题：卫星如何在轨检测科学事件并自主重规划观测
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：planning 和 robust execution 只是实现方式，主对象是任务科学自主性

### 2.3 容易混淆的边界

- 可能误归类到：05
- 最终判定：保留 10.02
- 判定理由：火山、洪水等 Earth observation 事件只是触发目标，论文主轴是航天任务重定向和执行控制
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：部分是
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：sensor-web mission agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：中高
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：部分是
- 环境交互：是
- 闭环实验：否

## 4. 方法设计

- 机载分析模块检测科学事件。
- 规划模块依据资源与约束重排观测活动。
- 执行模块完成指向、成像、再观测与数据下传优先级控制。

## 5. 实验与验证

- 验证方式：real-world deployment
- 载体：EO-1 与 autonomous sensor-web use cases
- 证据强度：高

## 6. 与已有工作的关系

- 属于 EO-1 / ASE / sensor-web 经典谱系。
- 可与 `Mission Operations of EO-1`、`Autonomous Earth-Observing Sensorweb` 形成组内比较。

## 7. 局限性与风险

- 与后续同谱系文献存在 lineage overlap，需要在综述中避免重复叙述。
- 主要不是 class risk，而是谱系压缩与代表性取舍。

## 8. 对综述写作的价值

- 是 `10.02` 经典 anchor paper。
- 能支撑 `05 / 10` 边界中“自然过程只是观测触发，论文对象仍是 mission-science autonomy”的判断。

## 9. 总结

这是一篇稳定的 `10.02` 记录：EO-1 自主科学代理的核心对象是航天 mission-science autonomy，而非 Earth process science。
