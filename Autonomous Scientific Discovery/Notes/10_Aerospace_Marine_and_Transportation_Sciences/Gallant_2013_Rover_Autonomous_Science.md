# Gallant et al. 2013 - Rover-Based Autonomous Science by Probabilistic Identification and Evaluation

**论文信息**
- 标题：Rover-Based Autonomous Science by Probabilistic Identification and Evaluation
- 作者：Marc J. Gallant; Alex Ellery; Joshua A. Marshall
- 年份：2013
- 来源 / venue：Journal of Intelligent & Robotic Systems
- DOI / arXiv / URL：https://doi.org/10.1007/s10846-013-9818-6
- PDF / 本地文件路径：当前笔记基于 Springer 官方摘要
- 论文类型：研究论文 / rover mission-science autonomy
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
first_hand_sources_checked: Springer abstract
classification_evidence_source_level: first_hand_abstract_or_landing_page
module_assignment_evidence: `05` is supported by probabilistic identification and evaluation of scientifically valuable planetary surface features; `10` is supported by rover autonomous science, path planning, and mission execution.
multi_module_object_coverage_note: The rover-autonomy contribution remains the filing anchor, but the planetary surface science features are concrete Earth/planetary-environment objects under the relaxed object-coverage rule.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Springer abstract | rover 自主识别科学目标、评估价值并规划路径 | 高 |
| 科学对象归类 | `10.02` | Springer abstract | 研究对象是 rover-based autonomous science，而非某个具体行星过程 | 高 |
| 方法流程 | 多步闭环 | Springer abstract | Bayesian identification -> evaluation -> path planning | 高 |
| 实验验证 | 有实验室和仿真 | Springer abstract | 实验室验证识别与评分算法，仿真比较 solo/scout configurations | 中高 |
| 边界判断 | 不转 `05`/`02` | object-first reading | 面向行星表面科学目标，但论文主轴是任务自主性 | 高 |

## 0. 摘要翻译

本文提出一种面向漫游车自主科学的概率化框架，使科学目标的识别与选择从远程操作员转移到漫游车本体。系统先从图像中识别候选特征，再评估其科学价值，最后规划前往高价值目标的路径，并在实验室与仿真环境中验证方法表现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备明确科研目标、多步感知-判断-规划链条和自主目标选择
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：目标识别、科学价值评估、路径规划

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：rover autonomous science target selection
- 四级专题：rover science-target identification agents
- 四级专题是否为新增：否
- 归类理由：稳定对象是 planetary rover mission-science autonomy
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：rover-based autonomous science workflow
- 最终科学问题：漫游车如何自主识别、评估并前往高科学价值目标
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：Bayesian identification 只是手段，主对象仍是 mission-science autonomy

### 2.3 容易混淆的边界

- 可能误归类到：05、02
- 最终判定：保留 10.02
- 判定理由：科学特征来自行星表面，但论文不研究地质本体，而研究车载自主任务闭环
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
- 其他：probabilistic rover science agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：部分是
- 仿真建模：是
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

- 从图像输入中识别候选科学特征。
- 对候选目标进行概率化科学价值评估。
- 通过路径规划把科学目标选择转化为漫游车行动。

## 5. 实验与验证

- 验证方式：laboratory validation + simulation
- 关键结果：识别、评价与路径规划可组合成 rover autonomous science loop
- 证据强度：abstract-backed but class direction strong

## 6. 与已有工作的关系

- 与 OASIS、AEGIS 属于同一 rover mission-science autonomy 谱系。
- 相比单纯地质分析系统，更强调车载自主决策与任务执行。

## 7. 局限性与风险

- 当前笔记主要依据摘要，细节尚未补足。
- 主要剩余工作是谱系定位与定量结果补充，不是主类重判。

## 8. 对综述写作的价值

- 可作为早期 rover autonomous science 代表样本。
- 能支撑 `05 / 10` 边界讨论中的“对象是任务自主而非自然过程本体”。

## 9. 总结

这篇论文稳定属于 `10.02`，核心贡献在 rover mission-science autonomy，而不在行星地质对象本身。
