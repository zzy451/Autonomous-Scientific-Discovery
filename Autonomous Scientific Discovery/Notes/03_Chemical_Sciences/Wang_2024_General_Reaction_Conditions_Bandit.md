# Wang et al. 2024 - Identifying general reaction conditions by bandit optimization

**论文信息**
- 标题：Identifying general reaction conditions by bandit optimization
- 作者：Wang et al.
- 年份：2024
- 来源 / venue：Nature
- DOI / arXiv / URL：https://doi.org/10.1038/s41586-024-07021-y
- PDF / 本地文件路径：本轮基于官方摘要页与 reviewer 一手证据；未保存本地 PDF
- 论文类型：研究论文 / reaction-optimization agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official abstract / reviewer evidence | bandit optimization 结合实验反馈，持续采样更优反应条件 | 高 |
| 科学对象归类 | `03.03` | official abstract / reviewer evidence | 研究对象是 generally applicable reaction conditions | 高 |
| 方法流程 | 实验反馈驱动搜索 | official abstract / reviewer evidence | 模型根据实验结果选择下一轮条件采样 | 高 |
| 实验验证 | 真实实验 | official abstract / reviewer evidence | 在三类真实反应上验证并高效找到 general conditions | 高 |
| 边界判断 | 不应归 `01.04` | official abstract / reviewer evidence | 产出是反应条件知识而不是通用 benchmark | 高 |

## 0. 摘要翻译

本文利用 bandit optimization 和实验反馈来寻找更具普适性的反应条件。相比传统经验或大规模枚举搜索，系统在较小实验预算下就能识别出泛化性更强的条件组合。论文的科学对象是具体反应条件发现，因此稳定属于化学科学。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：明确科研目标、多步条件选择、实验反馈和自主采样决策
- 判定置信度：高
- 在科研流程中承担的明确角色：experimental_design；experiment_execution；feedback_iteration
- 是否仍需进一步全文复核：不影响一级类判断

## 2. 科学领域归类

- 一级类：03
- 二级类：03.03
- 三级类：reaction-condition discovery
- 四级专题：Reaction-condition optimization via bandit loop
- 最终科学研究对象：反应条件及其一般性
- 最终科学问题：如何用 bandit-guided 实验闭环高效找到更通用的反应条件
- 容易混淆的边界：`01.04`
- 最终判定：保留 `03.03`
- 判定理由：产出是化学反应条件知识，而不是无对象 scientific-agent benchmark

## 3. Agent 系统与科研流程角色

- Agent 类型标签：Planning Agent；Hybrid Agent
- 科研流程角色：experimental_design；experiment_execution；feedback_iteration
- 自主能力：planning；feedback_iteration；autonomous_decision_making；closed_loop_experimentation
- 交叉属性标签：experiment_driven；high_throughput_screening

## 4. 方法设计

1. 模型为目标反应选择下一批条件。
2. 实验执行并测量结果。
3. 系统根据反馈更新 bandit 策略。
4. 再次采样更有潜力的条件。
5. 输出更一般化的反应条件知识。

## 5. 实验与验证

- 验证方式：experimentally_validated
- 数据、任务与指标：三类真实反应中的条件搜索任务
- 关键结果：在较小实验比例内找到 generally applicable conditions
- 科学贡献类型：experimental_optimization；knowledge_discovery
- 证据强度：experimentally_validated

## 6. 与已有工作的关系

- 与一般 BO/optimization 工作不同，这篇更强调“general conditions”发现。
- 与通用 research-agent 评测不同，直接产出是化学条件知识。
- 是 confirmed-core 中非常稳的 `03` 类样本。

## 7. 局限性与风险

- 更细的反应家族范围仍可在全文中补足。
- 主风险不在主类，而在后续如何放入化学子主题比较。
- 纳入与对象归类当前都很稳。

## 8. 对综述写作的价值

- 适合放入化学反应条件优化与知识发现部分。
- 可支撑“Agent 已能以较小实验预算发现更通用反应条件”这一论点。
- 推荐引用强度：core

## 9. 总结

### 9.1 一句话概括

bandit-guided 闭环实验高效找到更通用的反应条件。

### 9.2 速记版 pipeline

1. 选反应条件
2. 做实验
3. 看反馈
4. 更新 bandit
5. 找到 general conditions

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：03
二级类：03.03
三级类：reaction-condition discovery
四级专题：Reaction-condition optimization via bandit loop
Agent 类型：Planning Agent; Hybrid Agent
科研流程角色：experimental_design; experiment_execution; feedback_iteration
自主能力：planning; feedback_iteration; autonomous_decision_making; closed_loop_experimentation
验证方式：experimentally_validated
交叉属性：experiment_driven; high_throughput_screening
科学贡献类型：experimental_optimization; knowledge_discovery
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
