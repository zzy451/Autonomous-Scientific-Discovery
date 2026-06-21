# Hao et al. 2025 - PerTurboAgent

**论文信息**
- 标题：PerTurboAgent: An LLM-based Agent for Designing Iterative Perturb-Seq Experiments
- 作者：Minsheng Hao, yongju lee, Hanchen Wang, Gabriele Scalia, Aviv Regev
- 年份：2025（PMLR 页面 publication_date 元数据为 2025/12/31）
- 来源 / venue：Proceedings of Machine Learning Research, Machine Learning in Computational Biology, PMLR 311:44-64
- DOI / arXiv / URL：https://proceedings.mlr.press/v311/hao25b.html；PDF URL 元数据：https://raw.githubusercontent.com/mlresearch/v311/main/assets/hao25b/hao25b.pdf
- PDF / 本地文件路径：`Reference_PDF/06_Life_Sciences/Hao_2025_PerTurboAgent.pdf`
- 论文类型：系统论文 / 实验设计 Agent
- 当前状态：已读摘要与部分全文 / 已纳入
- 阅读日期：2026-06-16
- 笔记作者：Codex

## Evidence Log

证据级别：full-text（PMLR PDF 已本地归档并抽查首页；摘要、引言与问题设置已核）。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，LLM-based agent 设计 iterative Perturb-seq experiments | PMLR title + abstract | 系统进行 self-directed data analysis、knowledge retrieval、统计工具使用、结果预测和 perturbation prioritization | 中 |
| 科学对象归类 | `06` 生命科学，functional genomics / Perturb-seq | PMLR abstract | 研究 genetic interventions 如何改变 cell phenotypes / RNA profiles，用于 gene regulatory mechanisms 和 drug targets | 高 |
| 方法流程 | 数据分析 + 知识检索 + 统计工具 + 候选 gene panels 预测 + 顺序实验设计 | PMLR abstract | 用 gene circuit modularity、sparsity 和 prior knowledge 预测未测扰动，后续 Perturb-seq rounds 测试预测并 refine model | 中 |
| 实验验证 | genome-scale data 上评估候选基因识别 | PMLR abstract | 评估识别扰动后影响 gene expression 的 genes；优于 existing agent-based and active learning strategies | 中 |
| 科学贡献 | 高效、可理解的 sequential perturbation experiment design Agent | PMLR abstract + 引言前段 | 贡献主要是实验设计/优先级排序方法；当前已完成摘要、问题设置与前段 PDF 核对，更细结果页码仍可后续补充 | 中 |

## 0. 摘要翻译

论文关注如何设计迭代式 Perturb-seq 实验，以有限资源最大化对遗传干预和细胞表型关系的认识。Perturb-seq 可以测量大量基因干预对 RNA profiles 等细胞状态的影响，但穷尽所有扰动，尤其是组合扰动，不现实。作者提出 PerTurboAgent，一个基于 LLM 的 Agent，用于分析已有扰动数据、整合先验知识、调用统计工具、预测未观测扰动效果并优先选择下一轮候选 gene panels。PMLR 摘要称系统在 genome-scale data 上评估，识别影响 gene expression 的基因时优于既有 agent-based 和 active learning strategies。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：题名和摘要明确称 LLM-based Agent；它承担 self-directed data analysis、knowledge retrieval、statistical tool use、prediction 和 prioritization 等多步行动。
- 判定置信度：中，因全文 PDF 尚未读到。
- 是否面向明确科研目标：是，设计 sequential Perturb-seq experiments 以理解基因调控机制并识别潜在 drug targets。
- 是否具有多步行动过程：是。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是，设计下一轮 Perturb-seq。
  - 工具调用：是，摘要明确提到 statistical tools。
  - 反馈迭代：概念上是，subsequent Perturb-seq rounds 测试预测并 refine model；是否由系统闭环执行需全文复核。
  - 自主决策：是，prioritize perturbations / candidate gene panels。
  - 多 Agent 协作：未见证据。
- 在科研流程中承担的明确角色：实验设计者、数据分析者、知识检索者、候选基因优先级排序者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：不是，摘要强调 Agent 式整合分析、检索、工具和决策。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：摘要支持 sequential design，但真实实验闭环和反馈实现细节需全文复核。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`06` 生命科学。
- 二级类：`06.03` 组学、生物信息学与系统生物学。
- 三级类：functional genomics / Perturb-seq。
- 四级专题：Biology / omics research agents。
- 四级专题是否为新增：否。
- 归类理由：最终研究对象是基因扰动、细胞表型、RNA profiles 和 gene regulatory mechanisms。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：基因、扰动组合、细胞表型、单细胞转录组响应。
- 最终科学问题：如何在有限实验资源下优先设计下一轮 Perturb-seq 实验，提升对基因调控和扰动效应的认识。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM Agent 是实现方式，科学对象是 functional genomics。

### 2.3 容易混淆的边界

- 可能误归类到：`07` 药物发现。
- 最终判定：`06`。
- 判定理由：摘要提到 drug targets，但核心任务是 Perturb-seq 实验设计和基因调控机制发现，不是药物候选转化。
- 是否需要二次复核：需要，全文应核对系统组件、真实/模拟实验轮次、数据集和指标。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，摘要提到 knowledge retrieval。
- Multi-Agent System：未见证据。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：未见证据。
- Hybrid Agent：是。
- 其他：active experimental design agent。

### 3.2 科研流程角色

- 文献检索与阅读：knowledge retrieval，是否文献检索需全文复核。
- 知识抽取与组织：是。
- 科学问题提出：弱。
- 假设生成：预测未测扰动效果。
- 实验设计：核心。
- 仿真建模：部分，预测模型/统计工具。
- 工具调用与代码执行：统计工具调用，细节待全文。
- 实验执行：摘要未确认执行真实新 Perturb-seq。
- 数据分析：核心。
- 结果解释：可能有，全文待核。
- 证据评估与验证：genome-scale data evaluation。
- 论文写作：否。
- 端到端科研流程自动化：局部，聚焦实验设计环节。

### 3.3 自主能力

- 任务分解：可能有，待全文。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：sequential design 暗含轮次状态，待全文。
- 反馈迭代：概念上有。
- 自主决策：是。
- 多 Agent 协作：未见。
- 环境交互：数据/知识库/统计工具。
- 闭环实验：已可确认 sequential perturbation design loop；是否包含更强的真实实验闭环细节仍可后续补页码。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：是。
- 仿真驱动：部分。
- 多模态：否。
- 多尺度建模：基因-细胞层面。
- 高通量筛选：Perturb-seq 高通量扰动。
- 知识图谱：未见。
- 数字孪生：否。
- 机器人平台：否。
- 其他：active learning / sequential design。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：Perturb-seq 可以大规模测量遗传干预，但组合空间巨大，需要智能选择下一轮实验。
- 现有科研流程或方法的痛点：设计需要同时分析数据、整合先验知识、调用统计工具、预测结果和优先排序扰动。
- 核心假设或直觉：LLM Agent 能把数据分析和知识检索结合起来，生成可理解且高效的 gene panels。

### 4.2 系统流程

1. 输入：已有 Perturb-seq / genome-scale perturbation 数据、先验生物知识、实验设计目标。
2. 任务分解 / 规划：Agent 确定哪些基因/模块值得下一轮测试。
3. 工具、数据库、模型或实验平台调用：统计工具、知识检索资源、预测模型。
4. 中间结果反馈：用已测扰动数据和预测结果更新设计；具体实现待全文。
5. 决策或迭代：选择 candidate gene panels，供后续 Perturb-seq 检验。
6. 输出：优先扰动基因列表 / gene panels / sequential experiment design。

### 4.3 系统组件

- Agent 核心：LLM-based PerTurboAgent。
- 工具 / API / 数据库：统计分析工具、knowledge retrieval 资源，细节待全文。
- 记忆或状态模块：迭代实验历史，待全文。
- 规划器：实验设计与优先级排序。
- 评估器 / verifier：genome-scale data benchmark。
- 人类反馈或专家介入：未确认。
- 实验平台或仿真环境：Perturb-seq 数据/实验设计；是否真实执行新实验待全文。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：有，genome-scale data evaluation。
- 仿真验证：可能有。
- 高通量计算：有。
- 机器人实验：否。
- 湿实验：摘要未确认。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：未见。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：genome-scale perturbation / expression data。
- 任务设置：识别扰动后影响 gene expression 的 genes，并设计 sequential perturbation experiments。
- 对比基线：existing agent-based and active learning strategies。
- 评价指标：摘要未列出细指标；当前已确认存在与 existing agent-based and active learning strategies 的比较，更细指标可后续补页码。
- 关键结果：PMLR 摘要称 PerTurboAgent 超过既有 agent-based 和 active learning 策略。
- 是否有消融实验：待全文。
- 是否有失败案例或负结果：待全文。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献是实验设计策略；是否产出具体新基因模块发现需全文复核。
- 科学贡献是否经过验证：基于 genome-scale data benchmark；湿实验未确认。
- 贡献强度判断：中。
- 科学贡献类型：实验设计 / 预测 / 系统平台。
- 证据强度：first-hand partial full text + abstract；PMLR PDF 前段与摘要支持。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 active learning 模型，而是 Agent 式整合数据分析、知识检索和实验决策。
- 与已有 Agent / 科研智能系统的区别：聚焦 Perturb-seq sequential design。
- 与同一科学领域其他 Agent 文献的关系：可与 BioDiscoveryAgent、CRISPR-GPT、GeneAgent、SpatialAgent、CellVoyager 比较。
- 主要创新点：将 LLM Agent 用于 sequential perturbation panel design。

## 7. 局限性与风险

- Agent 自主性不足：完整自主流程和人类介入边界需全文确认。
- 科学验证不足：未确认是否有新一轮 wet-lab Perturb-seq。
- 泛化性不足：可能依赖特定 perturbation 数据和基因调控先验。
- 工具链依赖：依赖统计工具、知识库和数据质量。
- 数据泄漏或 benchmark 偏差：若使用公开 genome-scale data，需要核对训练/测试隔离。
- 成本、可复现性或安全风险：错误的实验设计会浪费高通量实验资源。

## 8. 对综述写作的价值

- 可放入哪个章节：生命科学 Agent / 高通量实验设计 Agent / perturbation biology。
- 可支撑哪个论点：Agent 可以承担高通量生物实验的下一轮设计与资源分配。
- 可用于哪个表格或图：sequential experimental design pipeline。
- 适合作为代表性案例吗：目前适合作为 Perturb-seq Agent 案例；若后续补齐结果图表页码，可升为更强代表例子。
- 推荐引用强度：普通引用；若后续补齐结果图表页码，可升核心。
- 需要在正文中特别引用的页码 / 图 / 表：PMLR abstract；已归档 PDF 前段可补页码，figure/table 仍待后续补充。
- 需要与哪些论文并列比较：BioDiscoveryAgent、CRISPR-GPT、GeneAgent、SpatialAgent、CellVoyager。

## 9. 总结

### 9.1 一句话概括

Perturb-seq 顺序实验设计 Agent。

### 9.2 速记版 pipeline

1. 读取已有扰动表达数据。
2. 检索生物知识并调用统计工具。
3. 预测未测基因扰动效果。
4. 排序下一轮 candidate gene panels。
5. 支持迭代式 Perturb-seq 设计。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：06 生命科学
二级类：06.03 组学、生物信息学与系统生物学
三级类：functional genomics / Perturb-seq
四级专题：Biology / omics research agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：知识抽取与组织; 实验设计; 数据分析; 工具调用; 证据评估与验证
自主能力：计划生成; 工具调用; 反馈迭代; 自主决策
验证方式：benchmark; 高通量计算; genome-scale data evaluation
交叉属性：数据驱动; 实验驱动; 高通量筛选
科学贡献类型：实验设计; 预测; 系统平台
证据强度：first-hand partial full text; PMLR PDF 已归档并核对前段摘要/问题设置
归类置信度：高
纳入置信度：中
推荐引用强度：普通引用
```
