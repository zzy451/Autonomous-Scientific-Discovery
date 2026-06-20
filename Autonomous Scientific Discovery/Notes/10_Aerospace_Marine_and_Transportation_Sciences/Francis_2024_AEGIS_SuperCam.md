# Francis et al. 2024 - AEGIS Autonomous Targeting for the SuperCam Instrument on the Mars 2020 Perseverance Rover

**论文信息**
- 标题：AEGIS Autonomous Targeting for the SuperCam Instrument on the Mars 2020 Perseverance Rover
- 作者：Raymond Francis; Tara Estlin; Michael Burl; Gary Doran; Steve Chien; Daniel Gaines; et al.
- 年份：2024
- 来源 / venue：i-SAIRAS 2024
- DOI / arXiv / URL：https://ai.jpl.nasa.gov/public/documents/papers/francis-isairas-2024.pdf
- PDF / 本地文件路径：当前笔记基于官方 PDF
- 论文类型：部署论文 / rover mission-science autonomy
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official PDF abstract | autonomously select targets for science instruments, without Earth in the loop | 高 |
| 科学对象归类 | `10.02` | abstract + deployment framing | 对象是 Mars rover autonomous science targeting / mission operations | 高 |
| 方法流程 | 多步闭环 | abstract | 图像输入 -> target selection -> SuperCam action -> operational integration | 高 |
| 实验验证 | 真实火星部署 | official PDF | 已在 Perseverance 上完成大量 targets | 高 |
| 边界判断 | 不转 `05` | object-first reading | Jezero crater geology 只是任务背景，不是论文最终对象 | 高 |

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

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：Mars rover mission-science autonomous targeting
- 四级专题：Perseverance SuperCam autonomous targeting agents
- 四级专题是否为新增：否
- 归类理由：对象稳定落在 rover mission-science autonomy
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：Perseverance rover mission-science operations
- 最终科学问题：漫游车如何机载完成 SuperCam 自动选靶并嵌入 mission workflow
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：AEGIS 是手段，论文核心是任务中 autonomous targeting 的部署与表现

### 2.3 容易混淆的边界

- 可能误归类到：05
- 最终判定：保留 10.02
- 判定理由：火星地质只是场景背景，论文研究中心是 autonomy rollout
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

- 是 `10.02` 中真实火星部署的强案例。
- 可作为 mission-science autonomy 从 Opportunity/Curiosity 演进到 Perseverance 的关键节点。

## 9. 总结

该文稳定属于 `10.02`，因为它研究的是火星车 mission-science autonomous targeting 的真实部署，而不是行星地质对象本身。
