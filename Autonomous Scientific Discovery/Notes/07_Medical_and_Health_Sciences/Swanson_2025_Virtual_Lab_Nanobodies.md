# Swanson et al. 2025 - The Virtual Lab of AI Agents Designs New SARS-CoV-2 Nanobodies

**论文信息**
- 标题：The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies
- 作者：Kyle Swanson, Wesley Wu, Nash L. Bulaong, John E. Pak, James Zou
- 年份：2025 Nature 正式版；2024 bioRxiv 预印本
- 来源 / venue：Nature
- DOI / arXiv / URL：https://doi.org/10.1038/s41586-025-09442-9；bioRxiv DOI：https://doi.org/10.1101/2024.11.11.623004
- PDF / 本地文件路径：本轮已恢复安全官方 Nature full-text HTML 访问；`source_limited=no`；未在项目 PDF 库另存本地 PDF
- 论文类型：研究论文 / 系统论文 / 生物医药发现 Agent
- 当前状态：已读全文 / 已纳入
- 阅读日期：2026-06-16
- 笔记作者：Codex

## Frozen Adjudication Writeback - 2026-06-23

- Source checked: safe official Nature full-text HTML for DOI `10.1038/s41586-025-09442-9`, recovered this round during Batch23Partial1 writeback.
- Final classification: `scientific_object_modules=07;06`; `object_coverage_mode=multi_module`; `primary_module_for_filing=07`; `general_method_bucket=none`.
- Source status: `source_limited=no`. Prior safety-only carry-forward is retired and should no longer be treated as active note status.
- Note update: keep `07` primary for biomedical / therapeutic nanobody discovery while making the additional `06` protein / nanobody life-science coverage explicit.

## 2026-07-05 wording harmonization

- Active source-state wording for this note is now: local archived PDF exists at `Reference_PDF/07_Medical_and_Health_Sciences/Swanson_2025_Virtual_Lab_Nanobodies.pdf` and has been harmonized with the official Nature full text.
- The landed multi-module wording remains `scientific_object_modules=07;06` with `07` as the filing primary.
- Any older wording that sounds like no local PDF, safety-hold, or source-state lag should be treated as retired historical phrasing rather than the current repository state.

## Evidence Log

证据级别：safe official Nature full-text HTML（Batch23Partial1 本轮恢复访问）。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，AI-human multi-agent research collaboration | Abstract；Fig. 1；Methods/Virtual Lab workflow | 系统由 LLM Principal Investigator agent、多个 LLM scientist agents、Scientific Critic 和 human researcher 组成，通过 team/individual meetings 推进研究 | 高 |
| 科学对象归类 | `07` 医学与健康科学，感染病相关 nanobody / therapeutic binder 设计 | Abstract；Introduction；Fig. 2 | 目标是设计能结合 SARS-CoV-2 recent variants 的 nanobody binders，具有抗病毒候选物转化价值 | 高 |
| 方法流程 | 多 Agent 会议 -> 工具选择 -> 工具实现 -> 工作流设计 -> 候选 nanobody 生成 -> 湿实验验证 | Abstract；Fig. 2；Results | Virtual Lab 选择并实现 ESM、AlphaFold-Multimer、Rosetta，设计 92 个 mutant nanobodies | 高 |
| 实验验证 | 有湿实验验证 | Abstract；Results；Fig. 3-5 | 92 个设计进入实验验证；超过 90% 表达且可溶；两个候选对 JN.1 或 KP.3 有改进结合，同时保持 ancestral spike binding | 高 |
| 科学贡献 | 产出实验验证的 SARS-CoV-2 nanobody candidates，并展示 AI-human 多 Agent 开放式科研流程 | Abstract；Discussion | 从多 Agent 科研组织走到真实蛋白候选物验证，是强 ASD 案例 | 高 |

| Frozen adjudication | `07;06`; `source_limited=no` | Batch23Partial1 frozen adjudication | 安全官方 Nature full-text HTML 已恢复；保留 `07` 医学主归档，同时明确 `06` 蛋白 / nanobody 生命科学覆盖 | 高 |

## 0. 摘要翻译

论文提出 Virtual Lab，一种 AI-human research collaboration。系统由一个 LLM Principal Investigator agent 组织多个 LLM scientist agents，通过研究会议解决开放式、跨学科科研问题，并由 human researcher 提供高层反馈。作者将该系统用于设计针对 SARS-CoV-2 近期变体的 nanobody binders。Virtual Lab 自主提出并实现计算设计流程，整合 ESM、AlphaFold-Multimer 和 Rosetta，设计了 92 个新的 nanobodies。湿实验验证显示，一批候选物具有功能性结合谱，其中两个新 nanobodies 对 JN.1 或 KP.3 等近期变体的结合更好，同时保持对 ancestral spike protein 的强结合。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 冻结复核状态：已按 Batch23Partial1 落地；`source_limited=no`，不再沿用旧 safety-only / source-hold 口径。

- 是否属于 Agent 文献：是。
- 判断依据：论文明确构建 PI agent、Scientific Critic、多个 scientist agents 和 human researcher 组成的科研团队；PI agent 能自动创建科学家 Agent；团队会议和个人会议用于提出方向、分解任务、实现工具、设计流程和筛选候选物。
- 判定置信度：高。
- 是否面向明确科研目标：是，设计 SARS-CoV-2 变体 nanobody binders。
- 是否具有多步行动过程：是，team selection、project specification、tools selection、tools implementation、workflow design、candidate generation、experimental validation。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是，PI agent 组织会议和研究阶段。
  - 工具调用：是，流程选择并实现 ESM、AlphaFold-Multimer、Rosetta。
  - 反馈迭代：是，Scientific Critic 对 individual meeting 输出提供反馈，agent 改进答案；实验验证形成设计-验证闭环但非全自动实验闭环。
  - 自主决策：中高，Agent 决定研究方向、工具与设计方案；human researcher 保留高层反馈。
  - 多 Agent 协作：是。
- 在科研流程中承担的明确角色：问题分解、研究方案讨论、计算工具链设计、代码/流程实现、候选物筛选、结果解释。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，贡献不是单个蛋白模型，而是多 Agent 科研流程。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否；但湿实验由人类实验团队执行，不能写成全自动机器人闭环。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- scientific_object_modules：`07;06`
- object_coverage_mode：`multi_module`
- has_concrete_object_experiments：yes
- general_method_bucket：none
- primary_module_for_filing：`07`
- source_limited：no（本轮已恢复安全官方 Nature full-text HTML）

- 一级类：`07` 医学与健康科学。
- 二级类：`07.04` 药物发现、药剂学与治疗转化。
- 三级类：抗体 / nanobody 候选体设计。
- 四级专题：Drug discovery / biomedical agents；可标注 infectious-disease nanobody discovery agents。
- 四级专题是否为新增：否，建议并入 biomedical / drug discovery agents。
- 归类理由：最终对象是 SARS-CoV-2 spike-binding nanobody candidates，面向感染病抗病毒候选物，而不是通用科研 Agent 方法本身。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：SARS-CoV-2 spike/RBD 结合 nanobodies。
- 最终科学问题：多 Agent AI-human 团队能否设计并实验验证对近期 SARS-CoV-2 变体有效的功能性 nanobody。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM、多 Agent 和会议框架是方法；科学贡献落在抗病毒生物医药候选物设计与验证。

### 2.3 容易混淆的边界

- 可能误归类到：`06` 蛋白质设计；`01.04` 通用科研 Agent。
- 最终判定：`07`。
- 判定理由：虽然使用蛋白设计工具，但以病毒变体 binder / therapeutic candidate 为目标，并有湿实验验证。
- 是否需要二次复核：不需要改变主类；若综述章节细分，可与 `06` protein design agents 交叉引用。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：未作为核心机制确认。
- Multi-Agent System：是。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：是。
- Hybrid Agent：是。
- 其他：AI-human scientific collaboration；Scientific Critic agent。

### 3.2 科研流程角色

- 文献检索与阅读：可能有背景知识使用，但不是已确认核心贡献。
- 知识抽取与组织：是，跨免疫学、机器学习、计算生物学组织研究讨论。
- 科学问题提出：是。
- 假设生成：是。
- 实验设计：是，设计候选物和验证策略。
- 仿真建模：是，蛋白结构/结合计算建模。
- 工具调用与代码执行：是。
- 实验执行：湿实验由人类实验团队执行。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：是。
- 论文写作：未确认。
- 端到端科研流程自动化：部分端到端，人类在 loop 中且湿实验非机器人自动化。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：会议记录/阶段输出支持上下文延续，细节见 Methods。
- 反馈迭代：是，Scientific Critic 和 human feedback；实验验证后形成候选物评价。
- 自主决策：中高。
- 多 Agent 协作：是。
- 环境交互：计算工具链与 wet-lab 验证衔接。
- 闭环实验：有设计-湿实验验证链条，但不是全自动闭环实验室。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：是。
- 仿真驱动：是。
- 多模态：蛋白序列、结构、结合实验数据。
- 多尺度建模：蛋白分子层面。
- 高通量筛选：92 个设计的小规模候选筛选。
- 知识图谱：否。
- 数字孪生：否。
- 机器人平台：否。
- 其他：protein design；nanobody engineering。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：展示 LLM Agent 团队能承担开放式、跨学科科研，而不是仅解决单一问答或固定 benchmark。
- 现有科研流程或方法的痛点：nanobody 设计需要免疫学、计算生物学、机器学习和湿实验验证协同，人工组织成本高。
- 核心假设或直觉：给不同 Agent 设定科学角色并通过会议组织协作，可以像虚拟科研团队一样形成可执行研究方案。

### 4.2 系统流程

1. 输入：人类研究者给出 SARS-CoV-2 近期变体 binder 设计目标和高层反馈。
2. 任务分解 / 规划：PI agent 选择团队角色，组织 team meetings 和 individual meetings。
3. 工具、数据库、模型或实验平台调用：选择并实现 ESM、AlphaFold-Multimer、Rosetta 工作流。
4. 中间结果反馈：Scientific Critic 批评 individual meeting 输出，Agent 改进代码和方案；human researcher 提供高层反馈。
5. 决策或迭代：生成并筛选 92 个 mutant nanobody designs。
6. 输出：实验验证的一批 functional SARS-CoV-2 nanobody candidates。

### 4.3 系统组件

- Agent 核心：LLM Principal Investigator、domain scientist agents、Scientific Critic。
- 工具 / API / 数据库：ESM、AlphaFold-Multimer、Rosetta。
- 记忆或状态模块：会议输出和阶段总结。
- 规划器：PI agent。
- 评估器 / verifier：Scientific Critic、计算评分、湿实验 binding validation。
- 人类反馈或专家介入：human researcher 高层反馈；人类实验团队。
- 实验平台或仿真环境：蛋白计算设计管线和 wet-lab binding assays。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：不是纯 benchmark。
- 仿真验证：是，蛋白结构/结合计算。
- 高通量计算：是，候选物计算筛选。
- 机器人实验：否。
- 湿实验：是。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：human researcher / experimental biologists 参与。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：SARS-CoV-2 spike/RBD variants；92 个 designed nanobodies。
- 任务设置：设计对近期变体 JN.1 或 KP.3 具有更好结合，同时保持 ancestral spike binding 的 nanobody。
- 对比基线：原始/既有 nanobody scaffolds 与变体结合表现；具体实验比较见 Fig. 3-5。
- 评价指标：表达与可溶性、binding profiles、对 JN.1/KP.3 与 ancestral spike 的结合。
- 关键结果：超过 90% 表达且可溶；两个新候选物对近期变体有改进结合并保持 ancestral spike binding。
- 是否有消融实验：不是核心。
- 是否有失败案例或负结果：有大量候选物未成为最优 binder；具体失败谱需回看 Fig. 3-5。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，新 nanobody candidates。
- 科学贡献是否经过验证：是，湿实验验证。
- 贡献强度判断：强。
- 科学贡献类型：设计 / 实验发现 / 系统平台。
- 证据强度：实验验证。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个蛋白生成模型，而是多 Agent 组织科研、设计工具链并连接实验验证。
- 与已有 Agent / 科研智能系统的区别：将 multi-agent research meeting workflow 连接到真实生物医药候选物实验验证。
- 与同一科学领域其他 Agent 文献的关系：可与 BioMaster、CellVoyager、SpatialAgent、Coscientist、ChemCrow 等比较工具调用和验证强度。
- 主要创新点：AI-human 多 Agent 科研团队产出 wet-lab validated biomedical candidates。

## 7. 局限性与风险

- source / safety status：本轮已恢复安全官方 Nature full-text HTML；旧 safety-only carry-forward 已退役，但临床转化相关局限仍应保留。

- Agent 自主性不足：human researcher 高层反馈很重要，不能称为完全自主科学家。
- 科学验证不足：有 binding validation，但无体内疗效、安全性、药代、临床验证。
- 泛化性不足：主要展示 SARS-CoV-2 nanobody 案例，跨疾病/靶点泛化待验证。
- 工具链依赖：依赖 ESM、AlphaFold-Multimer、Rosetta 和实验平台质量。
- 数据泄漏或 benchmark 偏差：不属于标准 benchmark，但工具选择和 scaffold 知识可能受既有文献影响。
- 成本、可复现性或安全风险：病原相关蛋白设计需生物安全审查；完整代码和实验条件需复核。

## 8. 对综述写作的价值

- 可放入哪个章节：医学与健康科学中的 biomedical / drug discovery agents；也可作为多 Agent scientific team 的代表案例。
- 可支撑哪个论点：Agent 不只自动化分析，还能组织开放式科学流程并产出实验验证候选物。
- 可用于哪个表格或图：Agent roles vs validation strength；human-in-the-loop multi-agent biomedical discovery。
- 适合作为代表性案例吗：适合，核心引用。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：Abstract；Fig. 1 多 Agent 架构；Fig. 2 nanobody design workflow；Fig. 3-5 实验验证。
- 需要与哪些论文并列比较：Gao_2024_Biomedical_Discovery_AI_Agents、BioMaster、CellVoyager、Coscientist、ChemCrow。

## 9. 总结

- Frozen adjudication summary：该 note 现以 `07;06` 为最终模块结论，`07` 为主归档，且 `source_limited=no`。

### 9.1 一句话概括

多 Agent 虚拟实验室设计并验证新冠 nanobody。

### 9.2 速记版 pipeline

1. PI agent 组建虚拟科研团队。
2. Scientist agents 讨论并选择蛋白设计工具。
3. ESM/AlphaFold-Multimer/Rosetta 生成候选物。
4. 人类团队湿实验验证 binding profiles。
5. 产出 SARS-CoV-2 nanobody candidates。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07 医学与健康科学
二级类：07.04 药物发现、药剂学与治疗转化
三级类：抗体 / nanobody 候选体设计
四级专题：Drug discovery / biomedical agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：科学问题提出; 假设生成; 实验设计; 仿真建模; 工具调用与代码执行; 数据分析; 证据评估与验证
自主能力：任务分解; 计划生成; 工具调用; 反馈迭代; 自主决策; 多 Agent 协作
验证方式：湿实验; 计算验证; 人类反馈
交叉属性：计算驱动; 数据驱动; 实验驱动; 仿真驱动; protein design
科学贡献类型：设计; 实验发现; 系统平台
证据强度：official full-text HTML; 实验验证
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
