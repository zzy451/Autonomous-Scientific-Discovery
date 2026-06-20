> Historical note 2026-06-20: 本文件是旧口径 / 过渡口径下的历史审计记录，仅可作为背景线索。本轮 451 篇 confirmed 文献的多模块分类以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准；不得用本文中的 legacy single-primary、primary object 或 core-contribution 判断覆盖当前“可识别具体科学对象实验 / 验证 / benchmark task / case study / reported result 即可入对应模块”的规则。

# 500 篇核心样本分类审计报告（边界与低覆盖类聚焦）

生成日期：2026-06-18  
审计范围：`Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 当前 500 条 confirmed included + classified 记录，以及相关边界/对照样本。  
执行口径：按 `asd-literature-search-workflow`、`review_scope_and_classification_policy.md`、`domain_classification_rules.md`、`science_domain_taxonomy.md` 进行。

## 1. 本轮审计后的最新状态

- confirmed included + classified count：`500`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 本轮主要边界压力点：
  - `08 / 06`：植物基因组学、植物表型、植物科学发现与一般生命科学对象之间的边界
  - `05 / 10`：任务平台搭载的 Earth observation / environment science 与 mission-science autonomy 之间的边界
  - `01.03 / 01.04`：科学规律/方程发现 vs 通用科研 Agent 工作流
  - `01.04 / 11.07`：通用科研能力平台 vs scientific knowledge production itself

## 2. `needs_review` 处理结果

### 2.1 ASD-0836

- ID：`ASD-0836`
- 题名：`Reframing Discovery Trade-Off in Plant Genomics Through Autonomous Agents`
- 原状态：`needs_review`
- 原主类：`08`
- 本轮处理：改为 `background_only`，不进入 confirmed core count

判定理由：

- 当前可得证据显示，这篇 `Preprints.org` 记录更像面向 plant genomics autonomous agents 的综述/议程/benchmark 型文本，而不是已经完成多步科研工作流并给出明确 scientific discovery validation 的核心 Agent 系统论文。
- 现有元数据更支持“capability framing / benchmark agenda / review-style discussion”，而不是一个已被验证的 plant-genomics scientific-Agent workflow。
- 按项目规则，不能因为题名中有 `autonomous agents`、`discovery`、`plant genomics` 就放宽纳入标准；核心纳入仍要求明确科研目标、多步行动过程、Agent 能力与科研流程角色四项同时成立，并有足够证据支持。

结论：

- 该记录已经从 `needs_review` 收口，不再保留悬而未决状态。
- 由于它仍与 `08/06` 边界有关，保留在列表中作为 `08` 低覆盖类的边界对照样本是合理的。

## 3. `08` 类薄弱样本逐篇判断

当前 confirmed `08` 仅有 3 篇，数量仍然偏低，但这不足以单独说明一级类有问题；更可能说明在当前严格 Agent 标准下，农业/食品方向的核心 Agent 文献确实稀缺。

### 3.1 ASD-0510

- 题名：`A conversational multi-agent AI system for automated plant phenotyping`
- 当前归类：`08`
- 保持不变

理由：

- 研究对象是 plant phenotyping，属于作物/植物生产与农业表型测量对象，而不是一般生命机制研究。
- 该系统是面向具体 plant phenotyping workflow 的多 Agent 系统，不是通用植物知识助手。
- 即便方法上接近生命科学数据分析，其最终对象仍更接近农业对象与农学测量场景，因此留在 `08` 稳定。

审计意见：

- 这是当前 `08` 中最稳的 confirmed 样本之一。
- 该类样本支持 `08` 不是空壳类，但规模确实小。

### 3.2 ASD-0634

- 题名：`Aleks: AI powered Multi Agent System for Autonomous Scientific Discovery via Data-Driven Approaches in Plant Science`
- 当前归类：`08`
- 保持不变，但证据强度低于 ASD-0510

理由：

- 题名中的 `Plant Science` 容易把它推向 `06`，但当前摘要级证据显示其对象是 plant-science discovery，而非一般分子/细胞/基因机制方法论文。
- 只要研究对象稳定落在作物、植物生产、植物科学应用对象上，按项目规则可优先保留在 `08`。
- 目前没有足够证据要求把它改判为 `06`；相反，它是当前 `08/06` 边界最需要保留的压力测试样本之一。

审计意见：

- 维持 `08` 合理，但建议后续如果有全文，应重点核对其科学对象究竟是 plant production / crop-oriented discovery，还是一般 genomics / systems biology。
- 当前可作为 `08` confirmed，但不是最高置信样本。

### 3.3 ASD-0695

- 题名：`FoodPuzzle: Developing Large Language Model Agents as Flavor Scientists`
- 当前归类：`08`
- 保持不变

理由：

- 虽然该论文与 flavor molecules、知识检索、假设生成有关，容易与 `03` 化学或 `06` 生命科学发生方法层面的接近，但其最终对象是 flavor science / food science。
- 按对象优先规则，食品科学明确属于 `08.05`，不应因为涉及分子或风味知识而外移到 `03` 或 `06`。
- 该论文更像 food-science scientific-agent，而不是一般 flavor QA 或 food recommendation 系统，因此当前放入 confirmed `08` 可以成立。

审计意见：

- 该样本说明 `08` 的稀缺并不只来自农业，也可能来自食品科学方向 core-Agent 论文稀少。
- 这是 `08` 中最容易被方法错觉带偏的样本之一，但目前保留在 `08.05` 是对的。

## 4. 边界类问题清单

### 4.1 `08 / 06`

结论：

- 当前最需要严格防止的是“只要涉及植物、基因组、表型，就自动并入 `06`”。
- `08` 应保留给作物、农学、食品、林业、畜牧、水产及其生产/测量/加工/安全对象。
- `06` 应保留给一般生命机制、组学、细胞、蛋白质、生态等对象。

本轮判断：

- `ASD-0510` 稳定留在 `08`
- `ASD-0634` 暂留 `08`，但属边界高压样本
- `ASD-0836` 不升 core，转 `background_only`
- 经典功能基因组 Robot Scientist 论文如 `ASD-0501` 仍应留在 `06`，因为其对象是 functional genomics，不是农业生产对象

审计含义：

- `08` 的问题主要不是“归错太多到 `06`”，而是“真正满足当前 Agent 纳入标准的 `08` core paper 本来就少”。

### 4.2 `05 / 10`

本轮复核样本：

- `ASD-0852`、`ASD-0853`、`ASD-0854`、`ASD-0858` 保持 `10`
- `ASD-0859`、`ASD-0860`、`ASD-0861` 保持 `05`

结论：

- 若核心是 rover / spacecraft / mission science autonomy / onboard science operation，则归 `10`。
- 若平台只是搭载体，而研究对象是 volcanism、cryosphere、flood、Earth observation science，则归 `05`。

本轮审计认为这条硬规则有效，且足以稳定当前 `05/10` 边界。

### 4.3 `01.03 / 01.04`

本轮复核样本：

- `ASD-0857`、`ASD-0868`、`ASD-0869`、`ASD-0870` 保持 `01.03`
- `ASD-0069`、`ASD-0018`、`ASD-0013`、`ASD-0032`、`ASD-0059`、`ASD-0060` 保持 `01.04`

结论：

- 以科学规律、符号方程、一般系统规律、equation discovery 为对象的，留在 `01.03`。
- 以通用科研 Agent、通用 scientific workflow、general discovery platform 为对象的，留在 `01.04`。

补充意见：

- `ASD-0059` 这类“通用 hypothesis-generation framework”容易被误认为 scientific-law discovery，但当前证据仍更支持 `01.04`，因为其目标是跨域 hypothesis generation workflow，而不是一类稳定的规律/方程对象。

### 4.4 `01.04 / 11.07`

本轮复核样本：

- `ASD-0848`、`ASD-0855` 保持 `11.07`
- `ASD-0849` 保持 `01.04`

结论：

- scientific peer review、paper writing、scientific evaluation、claim verification、publishing workflow，本体上是 scientific knowledge production，归 `11.07`。
- 覆盖 ideation、experiment、publication、evaluation 的通用科研能力生态，如果重点仍是“科研 Agent 能力平台”，则归 `01.04`。

审计意见：

- 当前这条边界可以工作，但后续会继续承压，因为很多 2025-2026 新论文都在把通用科研平台与 publishing/review 机制混在一起写。
- 现阶段不需要改单一级类，只需要在报告和注释中把“对象是科研能力平台”与“对象是科学知识生产本身”区分得更明确。

### 4.5 `02 / 10`

本轮未发现需要系统调整的强证据。

- high-energy physics、astronomy、gravitational-wave analysis 这类对象稳定落在 `02`
- rover / mission operation / spacecraft-science autonomy 稳定落在 `10`

因此本轮无需额外扩大到全面复查 `02/10` 边界。

## 5. 是否已有足够证据说明一级分类需要调整

结论：

**当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。**

支撑理由：

- `05 / 10` 边界在 mission-object 区分下表现稳定。
- `01.03 / 01.04` 与 `01.04 / 11.07` 虽然持续承压，但目前仍可通过对象优先规则稳定裁决。
- `08` 的低覆盖更像真实稀缺性与严格纳入标准共同作用的结果，而不是一级类划分本身失效。
- 本轮唯一 `needs_review` 已成功收口，未出现大规模“无法安放”的 confirmed 论文簇。

## 6. 审计后的工作建议

- 后续若继续做分类压测，优先继续补看 `08/06` 边界，不要为了平衡数量而放宽 `08`。
- `08` 方向优先寻找真正面向 crop science、plant phenotyping、food science、breeding、agricultural experiment workflow 的 Agent 论文，而不是一般农业助手或农业问答系统。
- `01.04 / 11.07` 方向建议继续保留少量“知识生产对象”高代表样本，用于稳定 peer review / publishing / reproducibility 子分支口径。
- `05 / 10` 当前规则可直接沿用，不建议再做无目标扩审。
