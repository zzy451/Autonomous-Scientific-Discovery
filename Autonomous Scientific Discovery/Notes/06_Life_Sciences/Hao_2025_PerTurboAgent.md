# Hao et al. 2025 - PerTurboAgent: An LLM-based Agent for Designing Iterative Perturb-Seq Experiments

**论文信息**
- 标题：PerTurboAgent: An LLM-based Agent for Designing Iterative Perturb-Seq Experiments
- 作者：Minsheng Hao, yongju lee, Hanchen Wang, Gabriele Scalia, Aviv Regev
- 年份：2025
- 来源 / venue：Proceedings of Machine Learning Research, Machine Learning in Computational Biology
- DOI / arXiv / URL：https://proceedings.mlr.press/v311/hao25b.html
- PDF / 本地文件路径：PMLR PDF 链接存在，但本次 GitHub raw 下载失败；基于 PMLR HTML 摘要/元数据记录
- 证据级别：abstract+metadata
- 论文类型：系统论文
- 当前状态：已读摘要 / 已纳入 / 待全文复核
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 纳入 | PMLR Abstract | LLM-based agent 通过 self-directed data analysis 和 knowledge retrieval 设计 iterative Perturb-seq 实验 | 中 |
| 科学对象归类 | `06.03` functional genomics / perturb-seq | PMLR Abstract | 科学对象是 genetic interventions 对 cell phenotypes / RNA profiles 的影响，以及基因调控机制和 drug targets | 高 |
| 方法流程 | 数据分析 + 知识检索 + 基因 panel 预测 + 顺序实验设计 | PMLR Abstract | 系统分析数据、整合知识、使用统计工具、预测 outcomes、prioritize perturbations | 中 |
| 实验验证 | genome-scale data 上评估候选基因识别 | PMLR Abstract | 评估识别扰动后影响 gene expression 的 genes，优于 agent-based 和 active learning strategies | 中 |
| 科学贡献 | sequential perturbation experiment design | PMLR Abstract | 为有限实验资源下的 Perturb-seq 轮次设计提供可解释高效方法 | 中 |

## 0. 摘要翻译

论文关注如何设计迭代式 Perturb-seq 实验，以有限资源最大化对基因扰动和细胞表型关系的认识。作者提出 PerTurboAgent，一个基于 LLM 的 Agent，用于分析已有扰动数据、检索知识、使用统计工具、预测未测扰动效果并优先选择下一轮候选基因 panel。PMLR 摘要称系统在 genome-scale 数据上优于已有 agent-based 和 active learning 策略。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：题名和摘要明确称 LLM-based Agent；系统进行 self-directed data analysis、knowledge retrieval、statistical tool use 和候选 perturbation prioritization。
- 判定置信度：中，因未能读取完整 PDF。
- 是否面向明确科研目标：是，设计 sequential Perturb-seq experiments，理解基因调控机制并识别药物靶点。
- 是否具有多步行动过程：是，摘要描述分析、检索、预测、优先级排序和迭代实验设计。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：有，设计下一轮 Perturb-seq。
  - 工具调用：有，统计工具与知识检索。
  - 反馈迭代：有，Perturb-seq 后续轮次检验预测并 refine model。
  - 自主决策：有，优先选择 gene panels。
  - 多 Agent 协作：未见证据。
- 在科研流程中承担的明确角色：实验设计者、数据分析者、知识检索者、候选基因优先级排序者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：不是，摘要明确为 Agent 式实验设计系统。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：摘要显示有 sequential experimental design，但真实实验闭环细节待全文复核。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`06` 生命科学
- 二级类：`06.03` 组学、生物信息学与系统生物学
- 三级类：functional genomics / perturbation biology
- 四级专题：Biology / omics research agents
- 四级专题是否为新增：否
- 归类理由：最终对象是基因扰动、细胞表型、RNA profiles 和基因调控网络。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：基因、扰动组合、细胞表型、单细胞表达谱。
- 最终科学问题：如何在无法穷尽所有扰动组合时，优先设计下一轮 Perturb-seq 实验。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM Agent 是实现方式，科学目标属于 functional genomics。

### 2.3 容易混淆的边界

- 可能误归类到：`07` 药物发现。
- 最终判定：`06.03`。
- 判定理由：虽提到 drug targets，但主要任务是 Perturb-seq 实验设计和基因调控机制发现，不是药物候选优化或临床转化。
- 是否需要二次复核：是，需读取 PMLR PDF 以核对系统组件、数据集和指标。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是。
- Multi-Agent System：未见证据。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：未见证据。
- Hybrid Agent：是。
- 其他：active experimental design agent。

### 3.2 科研流程角色

- 文献检索与阅读：知识检索，是否文献检索待复核。
- 知识抽取与组织：整合先验知识。
- 科学问题提出：不突出。
- 假设生成：预测未测扰动效果。
- 实验设计：核心角色。
- 仿真建模：预测模型。
- 工具调用与代码执行：统计工具。
- 实验执行：设计实验，不确定是否执行真实 Perturb-seq。
- 数据分析：核心角色。
- 结果解释：可能有。
- 证据评估与验证：基于 genome-scale data benchmark。
- 论文写作：否。
- 端到端科研流程自动化：部分，偏实验设计环节。

### 3.3 自主能力

- 任务分解：可能有，待复核。
- 计划生成：有。
- 工具调用：有。
- 记忆与状态维护：迭代实验设计暗含状态更新，待复核。
- 反馈迭代：有。
- 自主决策：有。
- 多 Agent 协作：未见。
- 环境交互：数据库/统计工具。
- 闭环实验：概念上有 sequential loop；真实闭环待复核。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：是。
- 仿真驱动：部分。
- 多模态：否。
- 多尺度建模：细胞/基因层面。
- 高通量筛选：Perturb-seq 高通量扰动。
- 知识图谱：未见。
- 数字孪生：否。
- 机器人平台：否。
- 其他：active learning / sequential design。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：Perturb-seq 能测量大量遗传干预对细胞 RNA profile 的影响，但组合扰动无法穷尽，需要智能设计下一轮实验。
- 现有科研流程或方法的痛点：实验资源有限；设计需要数据分析、先验知识、统计工具、预测和优先级排序的综合能力。
- 核心假设或直觉：LLM Agent 可把数据分析与知识检索结合，生成更有效且可理解的 gene panels。

### 4.2 系统流程

1. 输入：已有 Perturb-seq / genome-scale perturbation 数据、先验生物知识、实验设计目标。
2. 任务分解 / 规划：Agent 分析哪些基因/模块值得下一轮测试。
3. 工具、数据库、模型或实验平台调用：统计工具、知识检索资源、预测模型。
4. 中间结果反馈：利用已测扰动数据和预测结果更新设计。
5. 决策或迭代：选择 candidate gene panels，供下一轮 Perturb-seq 检验。
6. 输出：优先扰动基因列表 / gene panels / sequential experiment design。

### 4.3 系统组件

- Agent 核心：LLM-based PerTurboAgent。
- 工具 / API / 数据库：统计分析工具、知识检索资源，细节待全文复核。
- 记忆或状态模块：迭代实验历史，待复核。
- 规划器：实验设计与优先级排序。
- 评估器 / verifier：genome-scale data benchmark。
- 人类反馈或专家介入：待复核。
- 实验平台或仿真环境：Perturb-seq 数据/实验设计，是否真实执行待复核。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：有，genome-scale data 上评估。
- 仿真验证：可能有。
- 高通量计算：有。
- 机器人实验：否。
- 湿实验：未从摘要确认。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：未见。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：genome-scale perturbation / expression 数据。
- 任务设置：识别扰动后影响 gene expression 的 genes，并设计 sequential perturbation experiments。
- 对比基线：existing agent-based and active learning strategies。
- 评价指标：摘要未给具体指标，待全文复核。
- 关键结果：PMLR 摘要称 PerTurboAgent 超过既有 agent-based 和 active learning 策略。
- 是否有消融实验：待复核。
- 是否有失败案例或负结果：待复核。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献是实验设计策略；是否产生具体基因模块发现待复核。
- 科学贡献是否经过验证：基于已有 genome-scale 数据验证；真实 wet-lab 证据未确认。
- 贡献强度判断：中。
- 科学贡献类型：实验设计 / 预测 / 系统平台。
- 证据强度：摘要/元数据为主，中低；需全文 PDF 复核。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 active learning 模型，而是 Agent 式整合数据分析、知识检索和实验优先级决策。
- 与已有 Agent / 科研智能系统的区别：聚焦 Perturb-seq sequential design。
- 与同一科学领域其他 Agent 文献的关系：可与 BioDiscoveryAgent、GeneAgent、SpatialAgent 比较。
- 主要创新点：把 LLM Agent 用于 sequential perturbation panel design。

## 7. 局限性与风险

- Agent 自主性不足：完整自主流程和人工介入情况待复核。
- 科学验证不足：未确认是否有新一轮湿实验。
- 泛化性不足：可能依赖特定 perturbation 数据和基因调控先验。
- 工具链依赖：统计工具、知识库和 Perturb-seq 数据质量。
- 数据泄漏或 benchmark 偏差：若使用公开 genome-scale 数据，需确认训练/测试分离。
- 成本、可复现性或安全风险：高通量实验设计若错误会浪费实验资源。

## 8. 对综述写作的价值

- 可放入哪个章节：生命科学 Agent / 实验设计 Agent / perturbation biology。
- 可支撑哪个论点：Agent 可以承担高通量生物实验的下一轮设计与资源分配。
- 可用于哪个表格或图：sequential experimental design pipeline。
- 适合作为代表性案例吗：需要全文复核后决定；目前可作为 Perturb-seq Agent 案例。
- 推荐引用强度：普通引用，全文确认后可升核心。
- 需要在正文中特别引用的页码 / 图 / 表：PMLR abstract；待补 PDF figure/table。
- 需要与哪些论文并列比较：BioDiscoveryAgent、CRISPR-GPT、GeneAgent、SpatialAgent。

## 9. 总结

### 9.1 一句话概括

Perturb-seq 顺序实验设计 Agent。

### 9.2 速记版 pipeline

1. 读取已有扰动表达数据。
2. 检索生物知识并调用统计工具。
3. 预测未测基因扰动效果。
4. 排序下一轮候选 gene panels。
5. 支持迭代式 Perturb-seq 设计。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：06 生命科学
二级类：06.03 组学、生物信息学与系统生物学
三级类：functional genomics / Perturb-seq
四级专题：Biology / omics research agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：知识抽取与组织; 实验设计; 数据分析; 证据评估与验证
自主能力：计划生成; 工具调用; 反馈迭代; 自主决策
验证方式：benchmark; 高通量计算; genome-scale data evaluation
交叉属性：数据驱动; 实验驱动; 高通量筛选
科学贡献类型：实验设计; 预测; 系统平台
证据强度：PMLR HTML 摘要/元数据，中低，待全文复核
归类置信度：高
纳入置信度：中
推荐引用强度：普通引用
```
