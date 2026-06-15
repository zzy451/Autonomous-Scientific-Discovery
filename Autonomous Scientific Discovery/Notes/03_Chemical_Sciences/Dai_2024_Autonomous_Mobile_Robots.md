# Dai et al. 2024 - Autonomous Mobile Robots for Exploratory Synthetic Chemistry

**论文信息**
- 标题：Autonomous mobile robots for exploratory synthetic chemistry
- 作者：Tianwei Dai, Sriram Vijayakrishnan, Filip T. Szczypinski, et al.
- 年份：2024
- 来源 / venue：Nature
- DOI / URL：https://doi.org/10.1038/s41586-024-08173-7
- 当前状态：candidate；core priority；full-text evidence pending

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，偏机器人/自治实验 | Nature / PubMed metadata | autonomous mobile robots for exploratory synthetic chemistry | 高 |
| 科学对象归类 | `03` 化学科学 | Nature title and abstract metadata | synthetic chemistry is the scientific object | 高 |
| 验证方式 | 机器人实验 | Nature metadata | modular robotic system for chemical synthesis | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- Agent 行动闭环：移动机器人执行合成、分析和决策，具体反馈机制需全文确认。
- 纳入置信度：高。

## 2. 科学领域归类

- 一级类：`03` 化学科学
- 二级类：`03.03` 合成、反应与催化
- 四级专题：autonomous mobile robots for synthetic chemistry
- 归类理由：研究对象是合成化学，不按机器人硬件归入工程类。

## 3. Agent 系统与科研流程角色

- Agent 类型：Robot / Embodied Agent；Planning Agent。
- 科研流程角色：实验执行、实验规划、数据分析、闭环探索。
- 自主能力：环境交互、工具/设备调用、反馈迭代。

## 4. 方法设计

初步 pipeline：

1. 系统选择探索性合成任务。
2. 移动机器人在不同实验站点之间转移样品。
3. 自动化合成与分析平台产生结果。
4. 系统根据预设标准或分析结果决定下一步实验。

## 5. 实验与验证

- 验证方式：真实机器人实验。
- 科学贡献类型：system_platform；experimental_discovery。
- 证据强度：experimentally_validated。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 可作为化学中 embodied Agent / robotic scientist 路线代表。
- 需要与 Boiko Coscientist 和 Song robotic AI chemist 区分：本论文重点是移动机器人自治实验平台。

## 7. 后续精读任务

- 补充机器人平台结构、任务数量、决策算法和结果指标。
- 判断是否满足我们 Agent 标准中的计划/反馈/自主决策。
