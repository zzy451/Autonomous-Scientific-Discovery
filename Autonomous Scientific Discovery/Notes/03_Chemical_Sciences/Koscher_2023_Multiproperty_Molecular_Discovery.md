# Koscher et al. 2023 - Autonomous, multiproperty-driven molecular discovery: From predictions to measurements and back

**论文信息**
- 标题：Autonomous, multiproperty-driven molecular discovery: From predictions to measurements and back
- 作者：Koscher et al.
- 年份：2023
- 来源 / venue：Science
- DOI / arXiv / URL：https://doi.org/10.1126/science.adi1407
- PDF / 本地文件路径：本轮基于官方摘要页与 reviewer 一手证据；未保存本地 PDF
- 论文类型：研究论文 / closed-loop molecular discovery
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official abstract / reviewer evidence | 平台自动完成 design-make-test-analyze cycles，并跨轮回训模型 | 高 |
| 科学对象归类 | `03.04` | official abstract / reviewer evidence | 研究对象是 dye-like molecules 的多属性分子发现 | 高 |
| 方法流程 | 预测-合成-测量-回训 | official abstract / reviewer evidence | 从 predictions 到 measurements 再回到模型形成闭环 | 高 |
| 实验验证 | 真实实验 | official abstract / reviewer evidence | 自动实现数百个未报道分子，并发现高性能分子 | 高 |
| 边界判断 | 保持 `03` | official abstract / reviewer evidence | 直接设计和验证的是分子属性而非材料器件层 | 高 |

## 0. 摘要翻译

这篇工作展示了一个围绕多属性目标的自治分子发现平台。系统在预测、合成、测量和模型回训之间形成闭环，自动探索新的染料样分子，并找到性能优异的候选。虽然应用背景可能与材料器件相关，但其直接对象始终是分子，因此应保留在化学科学。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：具备明确科研目标、多步闭环、自动实验执行、反馈回训和端到端发现流程
- 判定置信度：高
- 在科研流程中承担的明确角色：hypothesis_generation；experimental_design；experiment_execution；data_analysis；feedback_iteration
- 是否仍需进一步全文复核：不影响一级类判断

## 2. 科学领域归类

- 一级类：03
- 二级类：03.04
- 三级类：multiproperty molecular discovery
- 四级专题：Multiproperty molecular discovery loop
- 最终科学研究对象：dye-like molecules 及其多属性表现
- 最终科学问题：如何通过自治闭环在多属性约束下发现新分子
- 容易混淆的边界：`04`
- 最终判定：保留 `03.04`
- 判定理由：被直接设计、合成和测量的是分子，而不是器件材料层

## 3. Agent 系统与科研流程角色

- Agent 类型标签：Planning Agent；Hybrid Agent
- 科研流程角色：hypothesis_generation；experimental_design；experiment_execution；data_analysis；feedback_iteration
- 自主能力：planning；feedback_iteration；autonomous_decision_making；closed_loop_experimentation
- 交叉属性标签：experiment_driven；computation_driven

## 4. 方法设计

1. 模型提出多属性分子候选。
2. 系统执行自动合成与测量。
3. 汇总实验结果并更新模型。
4. 进入下一轮设计。
5. 输出新的高性能分子和更优多属性解。

## 5. 实验与验证

- 验证方式：experimentally_validated
- 数据、任务与指标：多属性分子发现与真实合成/测量任务
- 关键结果：自动实现数百个未报道分子，并进一步发现 top-performing molecules
- 科学贡献类型：experimental_discovery；experimental_optimization
- 证据强度：experimentally_validated

## 6. 与已有工作的关系

- 与一般分子生成模型不同，这里是完整的 design-make-test-analyze loop。
- 与材料发现工作不同，对象并未上移到材料器件层。
- 是 `03.04` 分子发现子类中的强代表样本。

## 7. 局限性与风险

- 仍可在全文中补更细的分子家族和评价属性。
- 主风险不在一级类，而在化学内部子主题组织。
- confirmed-core 强度很高。

## 8. 对综述写作的价值

- 适合放入闭环分子发现与多属性设计部分。
- 可支撑“Agent 已能完成从预测到测量再回训的真实分子发现闭环”这一论点。
- 推荐引用强度：core

## 9. 总结

### 9.1 一句话概括

自治闭环平台完成多属性分子发现并生成未报道分子。

### 9.2 速记版 pipeline

1. 提出分子候选
2. 自动合成和测量
3. 回传结果
4. 更新模型
5. 再发现更优分子

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：03
二级类：03.04
三级类：multiproperty molecular discovery
四级专题：Multiproperty molecular discovery loop
Agent 类型：Planning Agent; Hybrid Agent
科研流程角色：hypothesis_generation; experimental_design; experiment_execution; data_analysis; feedback_iteration
自主能力：planning; feedback_iteration; autonomous_decision_making; closed_loop_experimentation
验证方式：experimentally_validated
交叉属性：experiment_driven; computation_driven
科学贡献类型：experimental_discovery; experimental_optimization
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
