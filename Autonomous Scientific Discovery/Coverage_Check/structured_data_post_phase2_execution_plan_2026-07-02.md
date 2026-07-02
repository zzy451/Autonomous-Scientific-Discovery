# ASD 结构化数据后续执行方案（Phase 1-2 已完成后）

日期：2026-07-02

本文档用于在 `Autonomous Scientific Discovery` 项目中正式锁定“前两阶段已经完成之后”的后续主线，避免长上下文协作中再次出现目标漂移、统计口径漂移和事实源漂移。

## 1. 本文档解决什么问题

截至目前，项目已经不再处于“要不要做结构化数据”的讨论阶段，而是已经进入“如何把现有结构化体系变成长期稳定治理体系”的阶段。

本方案只回答三个问题：

1. 前两阶段到底已经完成了什么。
2. 447 篇 confirmed-core 主线接下来最合适先做什么。
3. 后续哪些动作必须由 Main Controller 单写，哪些动作适合继续多 Agent 并行。

## 2. 当前已确认完成的部分

### 2.1 已完成的阶段

- Phase 1：方案冻结，已完成。
- Phase 2：结构化导出与分析基础设施，已完成。

### 2.2 已落地的文件与机制

已存在并投入使用的关键文件包括：

- `Coverage_Check/structured_data_master_governance_plan_2026-07-01.md`
- `Coverage_Check/structured_data_github_management_plan_2026-06-30.md`
- `Data/README.md`
- `Data/field_dictionary.md`
- `scripts/export_structured_data.py`
- `scripts/check_data_consistency.py`
- `scripts/build_analysis_db.py`
- `scripts/query_analysis_db.py`
- `.github/workflows/structured-data-guard.yml`
- `CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`

### 2.3 当前机器可验证状态

以 `2026-07-02` 本地校验结果为准：

- `check_data_consistency.py` 严格模式可通过。
- 当前 `papers.jsonl` 记录总数为 `871`。
- 当前 active confirmed-core 为 `447`。
- 当前 active local PDF 为 `421`。
- 当前 active no-local-PDF 为 `26`。
- 当前 `workflow mirror drift count` 为 `3`。

这意味着：

1. authoritative baseline 已经重新对齐。
2. 导出、校验、构库、查询这条链路已经跑通。
3. 接下来不应再把主线放在“继续搭新基础设施”，而应转到“把现有体系收口成正式治理规范”。

## 3. 当前最合适的主线判断

从现在开始，447 篇 confirmed-core 主线最合适的下一步不是继续扩量，也不是先做更多新查询功能，而是先完成下面这个顺序：

1. authoritative 语义收口
2. authoritative 快照验收
3. 分析口径固化
4. 协作纪律固化
5. 面向综述写作的并行增强

顺序不能反。

如果跳过前两步，后面的统计分析、图表、GitHub 协作和多 Agent 复核都会围绕不同口径漂移。

## 4. 后续阶段路径

### Phase 3A：Authoritative 语义收口

### 目标

把结构化层从“能导出”推进到“正式可依赖”，优先锁定字段定义、统计语义、事实源 ownership 和镜像层边界。

### 当前基础

这一步并不是从零开始。`Data/README.md`、`Data/field_dictionary.md` 和现有脚本已经完成了大部分骨架，但还需要把它们作为正式执行口径彻底固定下来。

### 必须锁死的内容

- `agent_master_paper_list.md` 与 progress 文件的字段 ownership。
- `scientific_object_modules` 是 canonical formal module array。
- `general_method_bucket` 承担独立 `01.04` bucket。
- `primary_module_for_filing` 只用于 filing / display。
- `final_modules_or_bucket` 只是 workflow mirror，不是 canonical classification fact。
- `pdf_status`、`pdf_path`、`evidence_status` 的 authoritative 解释。
- `source_limited`、`object_coverage_mode`、`general_method_bucket` 的允许值与语义。

### 产出

- 正式字段字典冻结版。
- 正式统计口径说明。
- authoritative pair ownership 说明。
- canonical classification 与 workflow mirror 的边界说明。

### 验收标准

- 任意协作者都能判断一个字段应先改 master 还是先改 progress。
- 任意统计结果都能说清自己是按 canonical classification 还是按 workflow mirror 统计。
- 项目内不再存在把 `01.04` 当 formal module、把 `primary_module_for_filing` 当完整分类、把 `pdf_path` 非空当作真 PDF 存在的解释空间。

### 写入权限

- Main Controller：单写正式规则文档、字段字典冻结版、最终口径说明。
- 子 Agent：只读审查现有脚本、README、查询语义是否有歧义，返回差异清单，不直接改 authoritative 规则。

### Phase 3B：Authoritative 快照验收

### 目标

对当前 `Data/` 快照做一次正式验收，确认现有结构化导出确实忠实反映 authoritative pair。

### 重点检查项

- active confirmed-core 是否稳定为 `447`
- active local PDF 是否稳定为 `421`
- active no-local-PDF 是否稳定为 `26`
- `01.04` 是否完全留在独立 bucket，不进入 formal module array
- 多模块论文是否未被 `primary_module_for_filing` 压扁
- registry layer 与 analysis layer 是否都从同一 canonical classification 派生
- `workflow mirror drift` 是否被单独标记、单独解释

### 产出

- 一份正式 acceptance checklist。
- 一份 baseline 核对结论。
- 一份 drift 清单，至少区分：
  - 语义漂移
  - 顺序漂移
  - 可接受镜像差异

### 验收标准

- baseline `447 / 421 / 26` 再次被脚本和人工 spot-check 双重确认。
- canonical classification 与 mirror classification 的差异被显式列出，而不是混入默认统计。
- `check_data_consistency.py` 继续严格通过。

### 写入权限

- Main Controller：单写最终验收结论与基线说明。
- 子 Agent：可并行做只读 spot-check，例如 PDF manifest 核对、taxonomy 核对、multi-module spot-check、missing-PDF 清单核对。

### Phase 4：分析口径固化

### 目标

把当前查询和统计体系固定成可长期复用的分析基线，确保后续正文写作、图表统计和方法比较都依赖同一套口径。

### 必须完成的事情

- 明确 record-level count 与 expanded module count 的区别。
- 明确 `01.04` 独立统计，不并入 formal `01-11`。
- 明确默认查询必须走 canonical classification，不默认走 workflow mirror。
- 给常用分析问题建立固定模板。

### 建议固定的分析问题模板

- formal module 分布
- multi-module 论文分布
- `01.04` general-method bucket 盘点
- `421 / 26` PDF 覆盖状态
- 按模块的 PDF 覆盖率
- `11.07`、`01.04`、multi-module 边界论文清单

### 产出

- 查询语义说明。
- 固定 summary 指标表头。
- canonical-only 与 mirror-audit-only 的查询区分规则。

### 验收标准

- 同一问题不会因改用 `papers.jsonl`、`paper_modules.csv` 或 `papers.sqlite` 而得到语义不同的答案。
- `01.04`、`11.07`、multi-module 在统计展示中可解释、可复核。
- 后续正文写作可以直接复用这些指标定义。

### 写入权限

- Main Controller：单写正式指标名、默认统计口径和最终查询语义。
- 子 Agent：只读提出常用查询需求、发现易误读指标、做结果 spot-check。

### Phase 5：协作与 GitHub 纪律固化

### 目标

把“先改事实层，再导出派生层”的工作法固定成长期协作规则，防止重新回到手工目录管理和手工统计模式。

### 必须锁死的纪律

- authoritative pair 仍然只有：
  - `Paper_Lists/agent_master_paper_list.md`
  - `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- registry layer 不是第三事实源。
- analysis layer 不是纠错入口。
- PR 必须遵循：
  - `export_structured_data.py`
  - `check_data_consistency.py`
  - `build_analysis_db.py`
- 禁止把 `Data/*.json*`、`*.csv`、`*.sqlite` 的手改当成事实修复。
- baseline 变更必须显式说明是谁批准、为什么变、变了哪些文件。

### 产出

- 面向协作者的简明 SOP。
- baseline 更新规则。
- “哪些文件绝不能手改”的红线清单。
- canonical / mirror / registry / analysis 的职责图。

### 验收标准

- 协作者可以独立判断新增、改类、补 PDF、改 note path 时，第一落点应在哪一层。
- CI 能阻断 authoritative pair 已变但派生层未重建的提交。
- 团队不会再把 note、CSV、SQLite 或 manifest 当作最终事实源。

### 写入权限

- Main Controller：单写正式 SOP、baseline 更新规则和合并口径。
- 子 Agent：只读起草检查表、误操作案例和协作提示文本。

### Phase 6：面向综述生产的并行增强

### 目标

在 authoritative 层和分析层稳定之后，再启动真正有价值的并行工作，为综述正文、表格和图谱生产服务。

### 合适的并行对象

- `note_revision_queue`
- `full_text_followup_queue`
- `representative_paper_pool`
- `module_coverage_pool`
- `boundary_case_pool`

### 这些队列的用途

- 找出仍保留旧单模块、旧 `01.04`、旧单主类表述的 note
- 找出 `source_limited`、`notes_only`、多模块证据不足的条目
- 为正文中的代表性论文、模块覆盖图和边界讨论提前准备证据池

### 验收标准

- 每个队列都有明确触发条件。
- 每个队列都能回链到具体 `paper_id`、具体字段和具体证据缺口。
- 子 Agent 继续只读做建议单，不直接越级修改 authoritative pair。

### 写入权限

- Main Controller：决定采纳哪些建议，何时真正写回 authoritative pair。
- 子 Agent：按模块、ID 区间或任务切片做只读复核和候选建议。

## 5. Main Controller 与子 Agent 的固定边界

后续继续采用“主控收口、子代理只读审查或分工建议”的结构。

Main Controller 固定单写：

- `agent_master_paper_list.md`
- progress 文件
- 正式治理方案
- baseline 结论
- 最终统计口径
- 最终 PR / commit / merge

子 Agent 固定只读或有限责任：

- 只读审查脚本语义
- 只读 spot-check manifests / registry / SQLite
- 只读整理 drift 清单
- 只读整理 note revision queue / follow-up queue
- 若未来进入 note writeback 轮次，再按严格 ownership 拆分 note 编辑，但仍不得改 master / progress / report

## 6. 当前阶段最容易漂移的风险点

1. 把 `final_modules_or_bucket` 当成正式分类事实源。
2. 把 `primary_module_for_filing` 当成单主类。
3. 把 `01.04` 混回 formal `01-11` 模块统计。
4. 把 `pdf_path` 非空、读过全文或 note 中“已核对”误当作本地真 PDF 证据。
5. 把 registry / analysis layer 当作手工纠错入口。
6. 把 `workflow mirror drift` 混成普通统计差异，不区分语义漂移和顺序漂移。
7. 把新增功能优先级排在 authoritative 验收之前。

## 7. 后续完成定义（Definition of Done）

当以下条件全部满足时，可以认为“结构化数据后续治理阶段”真正进入稳定运行态：

1. authoritative pair 的字段 ownership 已正式写清并被团队遵守。
2. canonical classification 与 workflow mirror 的边界已固定，默认统计只认 canonical。
3. `workflow mirror drift` 已清零，或至少被拆分为可审计的零语义漂移与零顺序漂移。
4. baseline `447 / 421 / 26` 的变更条件、批准方式和 PR 说明方式已固定。
5. `check_data_consistency.py` 与 CI 能持续阻断未重建派生层、手改 Data 和 canonical / mirror 混用。
6. 协作者有一份可直接执行的 SOP，知道每类修改先落在哪一层。
7. 447 篇 confirmed-core 的统计、查询、抽样和综述写作支持都统一建立在这套口径上。

## 8. 本文档后的建议直接动作

写完本文件后，建议按下面顺序推进下一轮实际工作：

1. 以本文件为准，补一轮 authoritative acceptance checklist。
2. 单独处理 `workflow mirror drift`，把语义漂移和顺序漂移拆开。
3. 将默认查询与默认统计显式降噪为 canonical-only。
4. 补面向协作者的简明 SOP，明确 baseline 更新纪律。
5. 在上述内容稳定后，再继续大批量并行做 note revision queue 和内容生产准备。
