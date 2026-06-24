# Herisson et al. 2024 - Operate a Cell-Free Biofoundry using Large Language Models

## 2026-06-24 confirmed-core full reaudit revision

```text
paper_id: ASD-0596
final_agent_inclusion: yes-borderline
supported_modules: 06
primary_module_for_filing: 06
source_limited: no
safety_access_status: official-full-text-available; preprint-safety-block-nonblocking
first_hand_sources_checked: PMC full text https://pmc.ncbi.nlm.nih.gov/articles/PMC12529354/ ; Crossref metadata for preprint 10.1101/2024.10.28.619828 and VOR 10.1016/j.isci.2025.113599
pdf_archive_status: local PMC PDF archived this round at Reference_PDF/06_Life_Sciences/Herisson_2024_Operate_CellFree_Biofoundry_LLMs.pdf
adjudication_note: strong cell-free biofoundry object coverage and reported optimization gains, but the LLM should be written as workflow-heavy / design-stage code generation, not a strong runtime LLM lab agent
```

**论文信息**
- 标题：`Operate a Cell-Free Biofoundry using Large Language Models`（preprint title）；VOR / PMC title 为 `An AI-driven workflow for the accelerated optimization of cell-free protein synthesis`
- 作者：J. Herisson; A. N. Hoang; A. El-Sawah; M. M. Khalil; J.-L. Faulon
- 年份：2024（preprint） / 2025（VOR）
- 来源 / venue：bioRxiv preprint；iScience VOR；PMC official full text available
- DOI / URL：https://doi.org/10.1101/2024.10.28.619828 ; https://doi.org/10.1016/j.isci.2025.113599 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12529354/
- PDF / 本地文件路径：`Reference_PDF/06_Life_Sciences/Herisson_2024_Operate_CellFree_Biofoundry_LLMs.pdf`（本轮自 PMC 官方 PDF 归档）；preprint 路线在本轮为 safety-blocked 但不影响判定
- first-hand source checked：PMC 全文；Crossref preprint/VOR metadata
- 论文类型：biofoundry workflow paper / CFPS optimization study
- 当前状态：confirmed-core full reaudit landed；`yes-borderline`
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| first-hand source checked | PMC 全文 + Crossref metadata | PMC; Crossref | 本轮不再仅依赖摘要页；official full text 已可用 | 高 |
| access / source status | `source_limited = no` | PMC; controller adjudication | 官方全文可访问；preprint route safety-blocked 为 nonblocking；本地已归档 PMC PDF | 高 |
| Agent 纳入 | `yes-borderline` | PMC 全文; Crossref preprint abstract | 论文确有自动化 DBTL、active learning、实验反馈与真实优化收益，但 LLM 更像设计阶段代码生成器 | 高 |
| 科学对象归类 | `06` | PMC 全文 | 直接科学对象是 cell-free protein synthesis / protein expression optimization，而不是通用科研方法学 | 高 |
| LLM 角色 | workflow-heavy / design-stage code generation | Crossref preprint abstract; PMC full text | workflow components 由 ChatGPT-4 编码生成；不应写成强 runtime LLM lab agent | 高 |
| 实验验证 | real wet-lab / biofoundry optimization | Crossref preprint abstract; PMC full text | colicin M 约提升 9 倍，colicin E1 约提升 3 倍 | 高 |

## 0. 摘要翻译

这项工作面向 cell-free protein synthesis 的实验优化，目标是提升 colicin M 和 colicin E1 的表达产量。系统把自动化 `DBTL` 循环、active learning、实验编排和数据分析接到同一条 biofoundry workflow 上，并报告了真实产量提升。需要明确的是，题目虽然强调 LLM，但本轮一手证据更支持把它写成“LLM 参与工作流代码生成与设计阶段搭建”的案例，而不是强运行时科研 Agent。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是，但属于 `yes-borderline`
- 判断依据：存在明确科研目标、多步实验迭代、active learning 反馈和自动化执行
- 关键限定：LLM 的证据更像 design-stage / workflow-construction role，不应夸写成强 runtime LLM lab agent
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 在科研流程中承担的明确角色：实验编排、条件更新、自动分析、biofoundry 执行

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除；但需保留 borderline wording，避免把 LLM runtime autonomy 说得过强

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.03
- 三级类：cell-free biofoundry / protein expression optimization
- 四级专题：LLM-assisted cell-free biofoundry optimization
- 归类理由：最终科学对象稳定落在 CFPS 与蛋白表达优化
- primary_module_for_filing：06
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：CFPS、生物制造流程、蛋白表达产量优化
- 最终科学问题：如何用自动化 DBTL 与 active learning 提升 cell-free protein synthesis 效率
- 为什么不是 `01.04`：这里有明确生命科学对象、具体实验任务和已报告的优化结果

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：不回流到 `01.04`，保留 06
- 边界真正所在：不是对象分类，而是 Agent 强度与 LLM 运行时角色表述

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：部分是
- Planning Agent：部分是
- Tool-using Agent：是
- Multi-Agent System：未见稳定证据
- Robot / Embodied Agent：是
- Hybrid Agent：是
- 其他：AL-driven biofoundry workflow

### 3.2 科研流程角色

- 实验设计：是
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 端到端科研流程自动化：部分是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该系统：CFPS 优化需要频繁试验与反馈，人工构建 DBTL 工作流效率有限
- 现有流程痛点：实验、数据分析与条件更新碎片化
- 核心方法：把 active learning、实验编排与 biofoundry workflow 连起来加速条件搜索

### 4.2 本轮应使用的表述

- 可以写：`workflow-heavy`、`design-stage code generation`、`LLM-assisted workflow construction`
- 不应写：`strong runtime LLM lab agent`

## 5. 实验与验证

### 5.1 验证方式

- 机器人实验：是
- 湿实验：是
- 真实场景部署：实验室真实 biofoundry 平台

### 5.2 数据、任务与指标

- 实验对象：colicin M 与 colicin E1 的 CFPS 优化
- 任务设置：自动化 DBTL 条件优化
- 评价指标：蛋白表达提升倍数
- 关键结果：colicin M 约提升 9 倍；colicin E1 约提升 3 倍

### 5.3 科学贡献

- 科学贡献类型：system_platform; experimental_optimization
- 贡献强度判断：中高
- 证据强度：official_full_text_supported

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次预测，而是连接真实 CFPS 工作流的自动实验迭代
- 与强 Agent 样本的区别：LLM 在运行时的自主科研主体性没有被本轮证据写强
- 与同领域样本的关系：可与 biofoundry / protein-engineering 子群并列，但不应拿它当最强 LLM lab-agent 代表

## 7. 局限性与风险

- Agent 自主性表述风险：若把 ChatGPT-4 写成运行时核心 Agent，会高估证据
- 工具链依赖：强依赖 biofoundry 与自动化执行
- 泛化性不足：当前案例集中在特定 CFPS / 蛋白表达任务
- PDF / archive 风险：preprint 路线仍为 safety-blocked，但官方 PMC PDF 已完成本地归档
- access note：preprint 路线 safety-blocked，但官方全文已足够支撑本轮落地

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学 / biofoundry / synthetic biology
- 可支撑哪个论点：并非所有标题带 LLM 的实验系统都应被写成强 runtime 科研 Agent
- 适合作为代表性案例吗：适合作为 `yes-borderline` 边界样本
- 推荐引用强度：标准引用，可配合“workflow-heavy”限定语

## 9. 总结

### 9.1 一句话概括

这是一个面向 CFPS 优化的自动化 biofoundry 工作流案例，科学对象覆盖很扎实，但 LLM 主要体现为 workflow-heavy / design-stage code generation，而不是强 runtime LLM lab agent。

### 9.2 标注字段汇总

```text
是否纳入：yes-borderline
主类：06
二级类：06.03
三级类：cell-free biofoundry / protein expression optimization
primary_module_for_filing：06
source_limited：no
safety_access_status：official-full-text-available; preprint-safety-block-nonblocking
first_hand_sources_checked：PMC full text; Crossref preprint/VOR metadata
Agent 类型：LLM Agent; Tool-using Agent; Planning Agent; Hybrid Agent
科研流程角色：experimental_design; tool_use_and_code_execution; experiment_execution; data_analysis; evidence_assessment_and_validation
验证方式：robotic_experiment; wet_lab_experiment
科学贡献类型：system_platform; experimental_optimization
证据强度：official_full_text_supported
纳入置信度：medium_high_borderline
推荐引用强度：standard
```
