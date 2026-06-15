# Song et al. 2025 - A Multiagent-Driven Robotic AI Chemist Enabling Autonomous Chemical Research On Demand

**论文信息**
- 标题：A Multiagent-Driven Robotic AI Chemist Enabling Autonomous Chemical Research On Demand
- 作者：Tao Song, Man Luo, Xiaolong Zhang, et al.
- 年份：2025
- 来源 / venue：Journal of the American Chemical Society
- DOI / URL：https://doi.org/10.1021/jacs.4c17738
- 当前状态：candidate；core priority；full-text evidence pending

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | ACS DOI page / seed survey ref 237 | 标题明确为 multiagent-driven robotic AI chemist，任务是 autonomous chemical research on demand | 高 |
| 科学对象归类 | `03` 化学科学 | 标题与 JACS venue | 面向化学研究、机器人化学实验和化学发现 | 高 |
| 验证方式 | 机器人实验 | 标题与 JACS article metadata | robotic AI chemist 指向自动实验平台 | 中 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- 判断依据：multiagent-driven + robotic AI chemist + autonomous chemical research。
- Agent 行动闭环：初步判断包括任务规划、多 Agent 协作、机器人实验执行和实验结果反馈；需全文复核。
- 纳入置信度：高。

## 2. 科学领域归类

- 一级类：`03` 化学科学
- 二级类：`03.04` 分子设计与化学空间探索，或 `03.03` 合成、反应与催化，待全文确定。
- 四级专题：机器人化学实验 Agent / 自动化化学研究
- 归类理由：研究对象是化学实验与化学发现，不按机器人或多 Agent 方法归入工程或计算机科学。

## 3. Agent 系统与科研流程角色

- Agent 类型：Multi-Agent System；Robot / Embodied Agent；Hybrid Agent。
- 科研流程角色：实验设计、实验执行、数据分析、结果解释、闭环实验。
- 自主能力：计划生成、工具/设备调用、多 Agent 协作、环境交互、闭环实验。

## 4. 方法设计

初步 pipeline：

1. 用户或系统提出化学研究需求。
2. 多 Agent 系统拆分为规划、实验、分析等角色。
3. 机器人平台执行化学实验。
4. 系统读取实验结果并进行分析。
5. 根据结果迭代下一轮实验或输出研究结论。

## 5. 实验与验证

- 验证方式：机器人实验，具体实验任务需全文补充。
- 科学贡献类型：experimental_discovery；system_platform。
- 证据强度：待全文确认，预计为 `experimentally_validated`。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 可放入章节：化学科学中的机器人化学家、自动化实验 Agent、闭环化学研究。
- 需要与 Boiko 2023 Coscientist、ChemCrow、A-Lab、closed-loop organic laser emitters 并列比较。

## 7. 后续精读任务

- 补充系统架构图、Agent 分工、机器人平台组成。
- 补充具体化学任务和实验结果。
- 判断是否更适合 `03.03` 还是 `03.04`。
