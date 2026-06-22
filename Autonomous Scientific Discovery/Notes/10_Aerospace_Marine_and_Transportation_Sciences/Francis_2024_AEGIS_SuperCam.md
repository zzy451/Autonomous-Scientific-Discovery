# Francis et al. 2024 - AEGIS Autonomous Targeting for the SuperCam Instrument on the Mars 2020 Perseverance Rover

**论文信息**
- 标题：AEGIS Autonomous Targeting for the SuperCam Instrument on the Mars 2020 Perseverance Rover
- 作者：Raymond Francis; Tara Estlin; Michael Burl; Gary Doran; Steve Chien; Daniel Gaines; et al.
- 年份：2024
- 来源 / venue：i-SAIRAS 2024
- DOI / arXiv / URL：https://ai.jpl.nasa.gov/public/documents/papers/francis-isairas-2024.pdf
- PDF / 本地文件路径：本轮复核已核对官方 JPL PDF（https://ai.jpl.nasa.gov/public/documents/papers/francis-isairas-2024.pdf）；未见本地归档 PDF
- 论文类型：部署论文 / rover mission-science autonomy
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-22 final adjudication refresh

```text
scientific_object_modules: 05;10
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 10
first_hand_sources_checked: official JPL PDF `francis-isairas-2024.pdf`; JPL AEGIS project page
classification_evidence_source_level: first_hand_full_text
note_revision_required: no
module_assignment_evidence: `05` is supported by Jezero crater rock and geochemical targets selected and measured through SuperCam; `10` is supported by Perseverance rover mission-science autonomy, autonomous targeting, and onboard instrument operations.
multi_module_object_coverage_note: Authoritative classification is `05;10` with `primary_module_for_filing=10`. This note remains under the `10` folder only as a filing convenience and does not negate the parallel `05` coverage.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official PDF abstract | autonomously select targets for science instruments, without Earth in the loop | 高 |
| 科学对象归类 | `05;10`（primary=`10`） | official PDF abstract + deployment framing | Jezero crater rock / geochemical targets提供 `05` 覆盖，Perseverance mission-science targeting 与仪器自主运行提供 `10` 覆盖 | 高 |
| 方法流程 | 多步闭环 | abstract | 图像输入 -> target selection -> SuperCam action -> operational integration | 高 |
| 实验验证 | 真实火星部署 | official PDF | 已在 Perseverance 上完成大量 targets | 高 |
| 边界判断 | 保持 `05;10` 多模块，主展示/落盘为 `10` | object-first reading | 论文主轴仍是 rover mission-science autonomy，但官方 PDF 直接支持 Jezero crater 岩石与地球化学目标，因此不能再写成 `10` 单模块 | 高 |

## 0. 摘要翻译

本文报告 AEGIS 在 Mars 2020 Perseverance rover 的 SuperCam 仪器上的部署与使用表现。系统可在没有地球人工回路的条件下自动为科学仪器选择观测目标，并已在火星上完成大规模常规使用。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备真实 mission-science 目标、多步感知与决策、在位执行和部署反馈
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：候选目标识别、选靶、观测执行、任务集成

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`05;10`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`10`
- Primary module for filing 说明：仅用于笔记落盘、排序和展示；本 note 留在 `10` 目录只是 filing convenience，不覆盖 `05` 并行覆盖事实。
- 主展示模块一级类：10
- 主展示模块二级类：10.02
- 主展示模块三级类：Mars rover mission-science autonomous targeting
- 主展示模块四级专题：Perseverance SuperCam autonomous targeting agents
- 其他覆盖模块及对应层级路径：`05` -> 行星地质 / 地球化学目标观测
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：`05` 来自 Jezero crater rocks 与 geochemical SuperCam targets；`10` 来自 Perseverance rover autonomous targeting、instrument sequencing 与 mission-science operations
- 归类理由：adjudicated 口径要求把具体行星岩石/地球化学目标记为 `05`，同时把 rover mission-science autonomy 记为 `10`，其中 `10` 是主展示/落盘模块
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：Perseverance rover mission-science autonomous targeting，以及被其直接选中的 Jezero crater 岩石/地球化学目标
- 最终科学问题：如何让漫游车在任务流程中自主筛选并执行高价值 SuperCam 观测，同时获得具体行星地质/地球化学对象观测
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：AEGIS 是手段，归类应由官方 PDF 中实际覆盖的科学对象决定，而不是由算法名或 note 所在目录决定

### 2.3 容易混淆的边界

- 可能误归类到：仅 `10` 或仅 `05`
- 最终判定：记录为 `05;10`，primary=`10`
- 判定理由：若只看 autonomy rollout，容易漏掉 Jezero crater rocks / geochemical targets 对 `05` 的直接支持；若只看行星地质对象，又会漏掉论文对 rover mission-science autonomy 的主轴。当前 note 存放目录只是 filing convenience，不是唯一分类事实。
- 多模块覆盖说明：`05` 来自具体目标对象覆盖，`10` 来自航天任务自治覆盖，两者并行成立
- 01.04 判定说明：不适用；论文具有明确具体科学对象与真实任务部署
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：Mars rover targeting agent

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
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：中
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：中
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

## 4. 方法设计

- 从 rover 图像中识别候选科学目标。
- 自动为 SuperCam 选择目标并与 uplink plan 对接。
- 在真实火星任务环境中持续迭代部署策略。

## 5. 实验与验证

- 验证方式：real-world deployment
- 关键结果：已完成大量在位 targets selection
- 证据强度：高

## 6. 与已有工作的关系

- 是 AEGIS 谱系在 Perseverance 平台上的延伸。
- 与 2014 ChemCam、2015 MSL integration 记录构成连续 deployment chain。

## 7. 局限性与风险

- 主要剩余工作是补充更多 quantitative mission statistics。
- 主类方向稳定，剩余风险更多是 deployment-detail completeness。

## 8. 对综述写作的价值

- 是 `10.02` 中真实火星部署的强案例，同时可放入 `05/10` 多模块边界对照表。
- 可作为 mission-science autonomy 从 Opportunity/Curiosity 演进到 Perseverance 的关键节点，并补充 Jezero 行星地质/地球化学目标覆盖。

## 9. 总结

### 9.1 一句话概括

Perseverance SuperCam 自主选靶同时覆盖行星地质目标与航天任务自治。

### 9.2 速记版 pipeline

1. 读取 rover 图像与任务约束
2. 自主识别候选 Jezero 科学目标
3. 选择并执行 SuperCam 观测
4. 将结果并入 Perseverance mission-science workflow

### 9.3 标注字段汇总

```text
是否纳入：to_read
科学对象模块：05;10
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：10
是否进入 01.04 存放区：否
主展示模块一级类：10
主展示模块二级类：10.02
主展示模块三级类：Mars rover mission-science autonomous targeting
主展示模块四级专题：Perseverance SuperCam autonomous targeting agents
其他覆盖模块及对应层级路径：05 -> 行星地质 / 地球化学目标观测
module_assignment_evidence：05 来自 Jezero crater rocks / geochemical SuperCam targets；10 来自 Perseverance rover mission-science autonomy 与 instrument targeting
multi_module_object_coverage_note：本 note 留在 10 目录仅为 filing convenience；authoritative classification 是 05;10，primary=10
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：data_analysis; experiment_execution; workflow_orchestration; feedback_iteration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：real_world_deployment
交叉属性：computation_driven; data_driven; robotic_platform
科学贡献类型：system_platform; mission_science_planning
证据强度：high_primary_pdf
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
