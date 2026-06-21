# Hu et al. 2025 - Electromagnetic metamaterial agent

**论文信息**
- 标题：Electromagnetic metamaterial agent
- 作者：Hu et al.
- 年份：2025
- 来源 / venue：Light: Science & Applications
- DOI / URL：https://doi.org/10.1038/s41377-024-01678-w
- PDF / 本地文件路径：`Reference_PDF/04_Materials_Science/Hu_2025_Electromagnetic_Metamaterial_Agent.pdf`
- First-hand source checked：official Nature HTML；official Nature PDF
- PDF version：publisher PDF
- Source-limited：no
- 当前状态：confirmed core；当前落地为 relaxed multi-module `04;09`，主归档模块为 `04`

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| PDF 归档与来源核对 | 已完成 | official Nature HTML；official Nature PDF | 当前使用 publisher PDF 作为规范归档版本 | 高 |
| Agent 纳入 | 是 | 官方全文 | 论文显式提出具身 `metaAgent`，包含规划、感知、编码、执行与环境反馈链条 | 高 |
| 材料科学覆盖 | `04` | 官方全文 | 核心对象是 electromagnetic metamaterials / programmable metasurfaces 的设计、控制与功能实现 | 高 |
| 工程技术覆盖 | `09` | 官方全文 | 论文将该系统用于 embodied wireless sensing、communications 与 robot-coordination-like task execution，构成工程系统 add-on 证据 | 中高 |
| `01.04` 存放区判断 | `none` | 官方全文 | 该文包含具体超材料对象与工程任务验证，不属于无对象实验的通用方法论文 | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- 判断依据：系统具备明确科研目标、多步任务规划、工具调用、环境交互与实验原型验证。
- 纳入置信度：高。

## 2. 科学领域归类

- scientific_object_modules：`04;09`
- object_coverage_mode：`multi_module`
- general_method_bucket：`none`
- primary_module_for_filing：`04`
- 归类理由：
  - `04`：直接科学对象始终是电磁超材料 / 可编程超表面。
  - `09`：具身无线感知、通信与机器人协同任务提供了明确工程技术 add-on 覆盖。
- 边界说明：文件存放在材料科学目录仅是 filing convenience，不代表排斥 `09` 的对象级覆盖。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Hybrid Agent；Embodied Agent。
- 科研流程角色：design；simulation_modeling；experiment_execution；data_analysis。
- 自主能力：planning；tool_use；feedback_iteration；autonomous_decision_making；environment_interaction。

## 4. 方法设计

1. 接收超材料相关任务与环境状态。
2. 高层控制模块规划任务并拆分执行步骤。
3. 协同感知、编码并控制可编程超表面。
4. 根据反馈动态调整任务执行。
5. 在真实原型任务中完成功能实现。

## 5. 实验与验证

- 材料对象验证：超材料 / 超表面功能实现。
- 工程对象验证：无线感知、通信与机器人协同相关任务。
- 验证方式：experimentally_validated。
- 证据强度：publisher full text；source_limited = no。

## 6. 对综述写作的价值

- 可作为材料 Agent 走向 embodied prototype 的代表案例。
- 同时适合支撑“对象仍是材料，但任务已外溢到工程技术系统”的边界论点。
- 推荐引用强度：standard。

## 7. 总结

### 7.1 一句话概括

具身 Agent 被用于电磁超材料对象，同时覆盖了无线感知、通信与机器人协同等工程任务。

### 7.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：04;09
object_coverage_mode：multi_module
general_method_bucket：none
primary_module_for_filing：04
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent; Embodied Agent
科研流程角色：design; simulation_modeling; experiment_execution; data_analysis
验证方式：experimentally_validated
科学贡献类型：design; system_platform
证据强度：experimentally_validated
归类置信度：medium_high
纳入置信度：高
推荐引用强度：standard
```
