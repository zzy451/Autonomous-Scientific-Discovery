# Roohani et al. 2024 - BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments

**论文信息**
- 标题：BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments
- 作者：Roohani et al.
- 年份：2024
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2405.17631
- PDF / 本地文件路径：`Reference_PDF/06_Life_Sciences/Roohani_2024_BioDiscoveryAgent.pdf`
- 论文类型：生命科学闭环实验设计 Agent
- 当前状态：已读，已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，设计 genetic perturbation experiments 的闭环 LLM Agent | PDF p.1 Abstract；p.2 Fig.1 | designs new experiments, reasons about outcomes, navigates hypothesis space；closed-loop experiment design | 高 |
| 科学对象归类 | `06` 生命科学，基因扰动 / functional genomics | PDF p.1 Abstract/Introduction | designing genetic perturbation experiments；find subset of genes that produce phenotype | 高 |
| 方法流程 | 每轮根据历史实验结果选择下一批基因，配合文献、代码和 critique 工具 | PDF p.2-3 method | prompt includes task and experimental results；tools for biomedical literature, code, critique | 高 |
| 实验验证 | 六个数据集、含未公开数据、与 Bayesian optimization baseline 对比 | PDF p.1 Abstract；results | 21% improvement；46% more hits on non-essential genes；combinatorial perturbation >2x random | 高 |
| 科学贡献 | 无需训练专用 ML 模型的可解释基因扰动实验设计 Agent | PDF p.2 contribution | uses biological knowledge and previous results to design perturbation experiments | 高 |

## 0. 摘要翻译

BioDiscoveryAgent 是一个用于设计 genetic perturbation experiments 的 LLM Agent。它在闭环设置中根据已有实验结果选择下一轮待扰动基因，推理实验结果，并用工具搜索生物医学文献、执行代码分析数据、让另一个 Agent 评价预测。作者在六个数据集上评估，包含一个未公开数据集以降低训练污染风险；Claude 3.5 Sonnet 版本相较专门训练的 Bayesian optimization baseline 平均多发现 21% hits，在只预测 non-essential genes 的困难任务上多 46%，组合扰动预测超过随机 baseline 两倍以上。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：明确是 AI agent；具备 closed-loop experiment design、工具调用、反馈迭代和 agent critique。
- 判定置信度：高。
- 是否面向明确科研目标：是，寻找导致目标 phenotype 的基因扰动集合。
- 是否具有多步行动过程：是，多轮实验设计。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是。
  - 工具调用：是，文献搜索、代码执行、critique agent。
  - 反馈迭代：是，每轮纳入 past experimental results。
  - 自主决策：是，选择下一轮基因。
  - 多 Agent 协作：部分，使用另一个 Agent critique。
- 在科研流程中承担的明确角色：实验设计者、结果解释者、基因候选选择者、假设空间搜索者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，它不训练专用 ML 模型，而用 Agent 闭环设计实验。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`06` 生命科学。
- 二级类：`06.03` 生物技术相关科学。
- 三级类：`06.03.01` 基因组学 / functional genomics。
- 四级专题：Biology / omics research agents。
- 四级专题是否为新增：否。
- 归类理由：核心对象是基因、基因扰动和细胞 phenotype，而不是药物开发终点。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：蛋白编码基因、单基因/组合扰动、细胞 phenotype。
- 最终科学问题：如何高效设计 CRISPR / genetic perturbation experiment 来找到目标 phenotype 相关基因。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM Agent 是方法，生物实验设计是对象和贡献。

### 2.3 容易混淆的边界

- 可能误归类到：`07` 医学与健康科学。
- 最终判定：`06`。
- 判定理由：虽然 introduction 提到 drug targets，但实验对象是 functional genomics / perturbation design，不直接验证治疗或药物转化。
- 是否需要二次复核：低优先级。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，生物医学文献搜索。
- Multi-Agent System：部分，critique agent。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：可解释并支持人类反馈，但验证中主要自主。
- Hybrid Agent：是。
- 其他：closed-loop biological experiment design agent。

### 3.2 科研流程角色

- 文献检索与阅读：是。
- 知识抽取与组织：是。
- 科学问题提出：弱。
- 假设生成：是，提出基因扰动假设。
- 实验设计：是。
- 仿真建模：否。
- 工具调用与代码执行：是。
- 实验执行：通过离线 benchmark 模拟实验结果，不是真实执行。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：是。
- 论文写作：否。
- 端到端科研流程自动化：部分，覆盖设计-反馈-下一轮设计。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：是，跨轮保存结果。
- 反馈迭代：是。
- 自主决策：是。
- 多 Agent 协作：部分。
- 环境交互：文献、代码、实验结果 oracle / dataset。
- 闭环实验：是，计算/离线闭环实验设计。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：是，围绕实验设计。
- 仿真驱动：离线实验模拟。
- 多模态：否。
- 多尺度建模：否。
- 高通量筛选：是，基因扰动筛选。
- 知识图谱：否。
- 数字孪生：否。
- 机器人平台：否。
- 其他：CRISPR perturbation、functional genomics。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：穷举基因扰动昂贵，传统 Bayesian optimization 需训练专用模型且可解释性不足。
- 现有科研流程或方法的痛点：小数据、实验代价高、模型难解释、不能充分利用文献知识。
- 核心假设或直觉：LLM 的生物知识与工具调用能力可在少轮实验中更好选择基因扰动。

### 4.2 系统流程

1. 输入：目标 phenotype、候选基因集合、历史实验结果。
2. 任务分解 / 规划：Agent 生成 reflection、research plan、solution。
3. 工具、数据库、模型或实验平台调用：检索生物医学文献，运行代码分析数据，调用 critique agent。
4. 中间结果反馈：每轮将 perturbation outcome 纳入 prompt。
5. 决策或迭代：选择下一批单基因或组合基因扰动。
6. 输出：下一轮实验候选基因及可解释理由。

### 4.3 系统组件

- Agent 核心：Claude 3.5 Sonnet 等 LLM。
- 工具 / API / 数据库：biomedical literature search、code execution、gene list summarization、agent critique。
- 记忆或状态模块：past experimental results。
- 规划器：prompt-driven planning。
- 评估器 / verifier：offline datasets / hit rate。
- 人类反馈或专家介入：框架支持解释和反馈。
- 实验平台或仿真环境：六个 perturbation datasets。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是。
- 仿真验证：离线实验模拟。
- 高通量计算：是。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：未见为主验证。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：六个 genetic perturbation datasets，含未公开数据集。
- 任务设置：单基因扰动、non-essential gene 难任务、组合基因扰动。
- 对比基线：Bayesian optimization baselines、random baseline。
- 评价指标：experimental hits / relevant perturbation prediction。
- 关键结果：平均 21% improvement；non-essential gene 任务 46% more hits；组合扰动预测超过随机两倍。
- 是否有消融实验：有工具和 agent critique 相关分析。
- 是否有失败案例或负结果：需进一步提取；总体强调仍需实验部署。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献为扰动实验设计方法；候选基因选择可能形成实验假设。
- 科学贡献是否经过验证：离线数据验证，未见湿实验验证。
- 贡献强度判断：中。
- 科学贡献类型：实验设计 / 假设 / 系统平台。
- 证据强度：benchmark / 离线实验数据支持。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不用训练单一预测模型，而是 Agent 利用文献、代码、历史结果闭环设计实验。
- 与已有 Agent / 科研智能系统的区别：专注 genetic perturbation experiment design，科学对象清晰。
- 与同一科学领域其他 Agent 文献的关系：可与 SpatialAgent、GeneAgent、PerturboAgent、OmniCellAgent 比较。
- 主要创新点：LLM-only + tools 的闭环生物实验设计，在小数据条件优于 BO baseline。

## 7. 局限性与风险

- Agent 自主性不足：没有连接真实实验平台。
- 科学验证不足：未做湿实验闭环。
- 泛化性不足：不同生物系统和 phenotype 的可迁移性待验证。
- 工具链依赖：文献搜索、代码执行和 prompt 质量影响结果。
- 数据泄漏或 benchmark 偏差：作者用未公开数据降低风险，但公开数据仍可能污染。
- 成本、可复现性或安全风险：基因扰动建议需专家和伦理审查。

## 8. 对综述写作的价值

- 可放入哪个章节：生命科学 / functional genomics Agent。
- 可支撑哪个论点：Agent 的核心价值之一是把文献知识与实验反馈结合用于闭环实验设计。
- 可用于哪个表格或图：生命科学闭环实验设计 pipeline；工具调用与反馈迭代表。
- 适合作为代表性案例吗：适合。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：PDF p.1 Abstract；Fig.1 closed-loop design；结果表。
- 需要与哪些论文并列比较：SpatialAgent、PerturboAgent、GeneAgent、CellVoyager。

## 9. 总结

### 9.1 一句话概括

闭环基因扰动设计 Agent。

### 9.2 速记版 pipeline

1. 输入 phenotype 和候选基因。
2. Agent 查看历史实验结果。
3. 检索文献并运行数据分析。
4. 选择下一轮扰动基因。
5. 用实验反馈继续迭代。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：06 生命科学
二级类：06.03 生物技术相关科学
三级类：06.03.01 基因组学 / functional genomics
四级专题：Biology / omics research agents
Agent 类型：LLM Agent；Planning Agent；Tool-using Agent；Retrieval-augmented Agent；Hybrid Agent；部分 Multi-Agent
科研流程角色：文献检索与阅读；知识抽取与组织；假设生成；实验设计；工具调用与代码执行；数据分析；结果解释；证据评估与验证
自主能力：任务分解；计划生成；工具调用；记忆与状态维护；反馈迭代；自主决策；闭环实验
验证方式：benchmark；离线实验数据；高通量计算
交叉属性：计算驱动；数据驱动；实验驱动；高通量筛选
科学贡献类型：实验设计；假设；系统平台
证据强度：全文 PDF 高
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
