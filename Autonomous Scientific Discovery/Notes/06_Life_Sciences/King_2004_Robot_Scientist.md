# King et al. 2004 - Functional genomic hypothesis generation and experimentation by a robot scientist

**论文信息**
- 标题：Functional genomic hypothesis generation and experimentation by a robot scientist
- 作者：Ross D. King et al.
- 年份：2004
- 来源 / venue：Nature
- DOI / arXiv / URL：https://doi.org/10.1038/nature02236
- PDF / 本地文件路径：基于 Nature 页面可得摘要/图题等一手证据整理
- 论文类型：系统论文 / 经典 Robot Scientist
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Nature Abstract | 自动生成假设、设计实验、机器人执行、解释结果并循环重复 | 高 |
| 多步闭环 | 是 | Nature Abstract | 明确存在 repeated cycle，不是单次预测 | 高 |
| 科学对象归类 | `06` | Nature Abstract | 研究 yeast gene function、deletion mutants、芳香族氨基酸合成通路 | 高 |
| 不是 `01.04` | 是 | Nature Abstract | 有稳定具体的功能基因组学对象 | 高 |
| 验证方式 | 真实湿实验 / 机器人实验 | Nature Abstract + 图题 | 真实 biological experiments，且实验选择优于 cheapest/random | 中高 |

## 0. 摘要翻译

这是一篇经典 Robot Scientist 论文。系统自动提出解释观测的假设、设计检验实验、由实验机器人执行实验、解释结果并剔除与数据不符的假设，然后继续下一轮循环。具体应用在酵母功能基因组学，利用 deletion mutants 与 auxotrophic growth experiments 推断芳香族氨基酸合成通路中的基因功能。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：四条最低纳入标准全部满足，且是具身实验 Agent 的历史锚点
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：不突出
- 在科研流程中承担的明确角色：假设生成、实验设计、实验执行、结果解释、证据筛选

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.03
- 三级类：functional genomics
- 四级专题：Robot-scientist functional genomics
- 四级专题是否为新增：否
- 归类理由：具体对象是 yeast gene function 与功能基因组学，而不是通用 autonomous science 平台本体
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：酵母基因功能、缺失突变体、生物代谢通路
- 最终科学问题：如何自动生成并验证 gene-function hypotheses
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：即使它是经典 Robot Scientist，也不能因此盖过其稳定的生命科学对象

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：06
- 判定理由：已有明确具体对象时，应离开 `01.04`
- 是否需要二次复核：需要补全文深度，但不是为改主类

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- Planning Agent：是
- Tool-using Agent：是
- Robot / Embodied Agent：是
- Hybrid Agent：是

### 3.2 科研流程角色

- 假设生成：是
- 实验设计：是
- 实验执行：是
- 数据分析：是
- 证据评估与验证：是

### 3.3 自主能力

- 任务分解：部分
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是
- 环境交互：是
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 机器人平台：是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：把科学方法中的假设提出、实验设计与验证流程自动化
- 现有科研流程或方法的痛点：手工实验筛选慢、知识检验效率低
- 核心假设或直觉：机器人系统可自动进行 hypothesis-test cycle

### 4.2 系统流程

1. 输入：关于基因功能的背景观测与候选假设
2. 任务分解 / 规划：选择最能区分假设的实验
3. 工具、数据库、模型或实验平台调用：实验机器人执行 biological experiments
4. 中间结果反馈：记录 growth / phenotype 等结果
5. 决策或迭代：剔除不符假设并继续下一轮
6. 输出：更稳定的 gene-function 解释

### 4.3 系统组件

- Agent 核心：Robot Scientist
- 工具 / API / 数据库：实验机器人与生物实验流程
- 规划器：实验选择机制
- 评估器 / verifier：实验结果与假设的一致性比较
- 实验平台或仿真环境：真实 biological experimentation

## 5. 实验与验证

### 5.1 验证方式

- 湿实验：是
- 机器人实验：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：yeast deletion mutants 与代谢通路实验
- 任务设置：gene-function hypothesis testing
- 对比基线：随机或 cheapest 实验选择
- 关键结果：真实 biological experiments 支持系统有效筛选假设

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，至少在功能基因组学问题上形成自动化科学检验贡献
- 科学贡献是否经过验证：是
- 贡献强度判断：强
- 科学贡献类型：experimental_discovery; system_platform
- 证据强度：experimentally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：这是具身实验 Agent，不是离线预测模型
- 与已有 Agent / 科研智能系统的区别：历史锚点地位非常明确
- 与同一科学领域其他 Agent 文献的关系：是生命科学方向的谱系源头之一
- 主要创新点：把假设-实验-验证闭环自动化

## 7. 局限性与风险

- Agent 自主性不足：当前笔记的一手证据深度仍主要来自摘要与图题
- 科学验证不足：主类不受影响，但方法细节仍可补强
- 泛化性不足：应用场景相对窄
- 成本、可复现性或安全风险：真实实验平台成本高

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学 / 历史锚点
- 可支撑哪个论点：经典 Robot Scientist 不是通用平台噪音，而是稳定生命科学对象论文
- 可用于哪个表格或图：历史谱系图、具身实验 Agent 表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用

## 9. 总结

### 9.1 一句话概括

功能基因组学中的经典 Robot Scientist 闭环。

### 9.2 速记版 pipeline

1. 生成基因功能假设
2. 设计区分性实验
3. 机器人执行实验
4. 解释结果并淘汰假设
5. 进入下一轮

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：06
二级类：06.03
三级类：functional genomics
四级专题：Robot-scientist functional genomics
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：hypothesis_generation; experimental_design; experiment_execution; evidence_assessment_and_validation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：wet_lab_experiment; robotic_experiment
交叉属性：computation_driven; data_driven; experiment_driven; robotic_platform
科学贡献类型：experimental_discovery; system_platform
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
