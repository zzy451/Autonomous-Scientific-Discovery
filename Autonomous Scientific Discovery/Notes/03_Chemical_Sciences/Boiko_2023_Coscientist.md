# Boiko et al. 2023 - Autonomous Chemical Research with Large Language Models

**论文信息**
- 标题：Autonomous chemical research with large language models
- 作者：Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes
- 年份：2023
- 来源 / venue：Nature
- DOI / URL：https://doi.org/10.1038/s41586-023-06792-0
- PDF / 本地文件路径：`Reference_PDF/03_Chemical_Sciences/Boiko_2023_Coscientist.pdf`
- First-hand source checked：本地归档 publisher PDF 全文（项目树外 canonical copy）；Nature 落地页 / 标题信息
- PDF version：publisher PDF local canonical copy
- Source-limited：no
- 当前状态：confirmed core；已按当前 relaxed object-coverage 规则落地为稳定 `03` 记录

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| PDF 归档与来源核对 | 已完成 | 本地归档 PDF；Nature 落地页 | 项目内已有规范化 PDF 路径，可作为后续复核与写作引用版本 | 高 |
| Agent 纳入 | 是 | 本地 PDF 全文；Nature 文章页面 | Coscientist 围绕化学研究目标执行多步任务，包含文献检索、方案设计、工具调用与实验相关行动链 | 高 |
| 科学对象归类 | `03` 化学科学 | 本地 PDF 全文 | 核心对象始终是化学实验、反应条件与分子/反应层面的化学研究任务 | 高 |
| `01.04` 存放区判断 | `none` | 本地 PDF 全文 | 论文包含明确化学对象实验与实验级验证，不属于无具体对象实验的通用方法论文 | 高 |
| 实验与验证 | 化学实验 / 反应优化 | 本地 PDF 全文 | 报告了真实化学任务验证，包括 palladium-catalysed cross-coupling 优化等实验场景 | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- 判断依据：系统围绕明确化学研究目标执行多步任务，具备规划、工具调用、实验设计与结果反馈。
- 纳入置信度：高。
- 当前口径说明：不再使用旧 note 中的 `candidate` / `full-text pending` 表述；该文已是稳定的 confirmed-core 纳入记录。

## 2. 科学领域归类

- scientific_object_modules：`03`
- object_coverage_mode：`single_module`
- general_method_bucket：`none`
- primary_module_for_filing：`03`
- 归类理由：论文的稳定对象是化学反应、实验设计与实验优化，不存在需要扩展到材料、医学或独立 `01.04` 存放区的当前证据。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Planning Agent；Hybrid Agent。
- 科研流程角色：文献检索与阅读；实验设计；工具调用与代码执行；实验执行；结果解释。
- 自主能力：任务分解；计划生成；工具调用；反馈迭代；闭环实验。

## 4. 方法设计

1. 接收化学研究目标。
2. 规划子任务并检索外部化学知识。
3. 调用化学工具与实验接口。
4. 设计并推进化学实验任务。
5. 根据实验结果生成下一步建议或结论。

## 5. 实验与验证

- 验证方式：化学实验验证。
- 科学贡献类型：system_platform；experimental_discovery；experimental_optimization。
- 证据强度：experimentally_validated。
- 当前落地说明：该文应作为稳定 `03` 化学科学代表案例使用，而不是继续保留“待全文确认”的过渡表述。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 可作为 LLM-driven autonomous chemical research 的高影响力代表案例。
- 适合支撑“Agent 已从化学工具使用走向真实实验组织与执行”的论点。

## 7. 总结

### 7.1 一句话概括

多步 LLM Agent 被用于真实化学研究任务，并在化学实验优化中得到验证。

### 7.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：03
object_coverage_mode：single_module
general_method_bucket：none
primary_module_for_filing：03
Agent 类型：LLM Agent; Tool-using Agent; Planning Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; experimental_design; tool_use_and_code_execution; experiment_execution; result_interpretation
验证方式：wet_lab_experiment
科学贡献类型：system_platform; experimental_discovery; experimental_optimization
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
