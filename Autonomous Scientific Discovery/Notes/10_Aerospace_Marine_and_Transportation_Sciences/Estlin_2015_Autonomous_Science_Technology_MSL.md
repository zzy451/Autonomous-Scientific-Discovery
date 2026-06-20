# Estlin et al. 2015 - Developing Autonomous Science Technology for the MSL Rover Mission

**论文信息**
- 标题：Developing Autonomous Science Technology for the MSL Rover Mission
- 作者：Tara Estlin; Gary Doran; Michael Burl; Reena Francis; Daniel Gaines; et al.
- 年份：2015
- 来源 / venue：IJCAI 2015 Workshop / JPL paper
- DOI / arXiv / URL：https://ai.jpl.nasa.gov/public/documents/papers/estlin-ijcai2015-autonomous.pdf
- PDF / 本地文件路径：当前笔记基于官方 PDF
- 论文类型：系统扩展摘要 / rover mission-science autonomy integration
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
module_assignment_evidence: `05` is supported by rocks, soil, veins, concretions, and geologically relevant MSL / ChemCam targets; `10` is supported by autonomous rover science technology, targeting, and mission integration.
multi_module_object_coverage_note: The relaxed rule treats the Mars geology objects as countable `05` coverage while preserving `10` as the filing module for rover mission-science autonomy.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official PDF abstract | automated science data collection by a planetary rover | 高 |
| 科学对象归类 | `10.02` | title + abstract | 研究对象是 MSL rover mission autonomy technology | 高 |
| 方法流程 | 多步闭环 | abstract | onboard target selection + pointing refinement + flight software integration | 高 |
| 实验验证 | 官方任务集成 | official PDF | 从 Opportunity 延伸到 Curiosity/ChemCam | 中高 |
| 边界判断 | 不转 `05` | object-first reading | 论文主轴是 autonomy technology，不是地质对象研究 | 高 |

## 0. 摘要翻译

本文总结面向 MSL Curiosity 的自主科学技术开发工作，重点介绍 AEGIS 如何从 Opportunity 的车载选靶经验演进到 Curiosity/ChemCam 平台，支持自动科学目标发现、精细指向与 flight software 集成。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：围绕明确 mission-science 目标执行多步识别、筛选、指向与系统集成
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：自动选靶、pointing refinement、flight software integration

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：MSL rover mission-science autonomy integration
- 四级专题：rover mission-science autonomy technology stacks
- 四级专题是否为新增：否
- 归类理由：稳定对象是 rover mission-science autonomy technology
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：MSL rover mission-science autonomy stack
- 最终科学问题：如何把自动选靶与任务技术集成进 Curiosity mission workflow
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：自动图像分析只是手段，主对象是 autonomous science technology integration

### 2.3 容易混淆的边界

- 可能误归类到：05
- 最终判定：保留 10.02
- 判定理由：rocks and soil 是测量对象，论文本体是 mission-science autonomy technology
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
- 其他：rover science integration agent

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
- 反馈迭代：部分是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

## 4. 方法设计

- 从导航或显微图像中识别候选科学目标。
- 生成 targeting / pointing action。
- 把自主科学能力集成进 rover flight software。

## 5. 实验与验证

- 验证方式：mission integration and lineage transfer
- 平台：Opportunity -> Curiosity / ChemCam
- 证据强度：high primary PDF

## 6. 与已有工作的关系

- 是 AEGIS 谱系中的集成过渡文献。
- 连接 Opportunity 早期部署与后续 Curiosity / Perseverance 任务应用。

## 7. 局限性与风险

- 更像扩展摘要，细粒度结果不如正式部署论文完整。
- 主要风险是谱系重叠，不是主类误判。

## 8. 对综述写作的价值

- 适合在 `10.02` 任务自主谱系中用作中间衔接节点。
- 支持“mission-science autonomy 持续从原型走向 flight integration”的论点。

## 9. 总结

这篇论文稳定属于 `10.02`，其核心对象是 MSL rover mission-science autonomy technology integration。
