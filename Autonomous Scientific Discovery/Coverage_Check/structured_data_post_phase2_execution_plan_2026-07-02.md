# ASD 结构化数据后续执行总方案（接续 Phase 1-2）

日期：2026-07-02
适用范围：`Autonomous Scientific Discovery` 447 篇 active confirmed-core 主线
当前定位：本文件是 Phase 1-2 完成后的统一执行总方案，后续所有 structured-data 推进默认以此为准，避免长上下文中的计划漂移、口径漂移和事实源漂移。

## 1. 当前共识

### 1.1 已完成阶段

- `Phase 1`：总方案与治理方向冻结，已完成。
- `Phase 2`：结构化导出、校验、分析数据库、GitHub 协作底座，已完成。

### 1.2 当前 authoritative baseline

截至 `2026-07-02`，当前默认基线是：

- active confirmed-core：`447`
- active local PDF：`422`
- active no-local-PDF：`25`
- workflow mirror semantic drift：`0`
- workflow mirror order drift：`0`
- canonical active `01.04` general-method bucket count：`9`

### 1.3 Authoritative pair

结构化事实层只有两份文件：

1. `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md`
2. `Autonomous Scientific Discovery/Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

`Data/`、registry、CSV、SQLite、manifest、notes、PDF 目录都不是第三事实源。

### 1.4 当前最重要的判断

447 篇主线的下一步，不是继续扩量，也不是先加更多分析花活，而是先把前两阶段搭好的系统收口成一套长期稳定、可审计、可协作的治理体系。

后续顺序固定为：

1. `Phase 3A` authoritative 语义冻结
2. `Phase 3B` authoritative baseline 验收
3. `Phase 4` canonical-only 分析口径固化
4. `Phase 5` 协作 SOP 与 baseline 更新纪律固化
5. `Phase 6` 面向综述生产的并行增强

顺序不能反。否则后面的统计、图表、note 队列和 GitHub 协作会重新围绕不同口径漂移。

## 2. 本轮多 Agent 审核收口

本轮已经完成“先讨论、再审阅、再收口”的多 Agent 过程，主结论如下。

### 2.1 审核结论 A：Phase 3A 还需要把这些点写死

- `note_path` 与 `pdf_path` 不是纯单源 ownership，而是当前导出规则下的优先级解析结果。
- canonical classification 的导出，不是直接读单一字段，而是按 remarks 结构化 token 优先，再回退到 legacy class。
- `general_method_bucket` 的结构化精确字面值必须写死，不能只写成口头上的 `01.04`。
- `final_modules_or_bucket` 的镜像语法、分隔符和顺序语义必须写进文档。
- `pdf_status` / `evidence_status` 当前应被定义为 workflow label，而不是未声明的“隐形闭集枚举”。

### 2.2 审核结论 B：Phase 3B baseline 已可支撑，但要加 caveat

- `447 / 422 / 25 / drift 0` 这组 baseline 可以被当前导出工件充分支撑。
- canonical `01.04` active count 当前是 `9`，不是旧摘要里的 `10`。
- `01.04` 与 formal `01-11` 已在 canonical 机器层分离干净。
- master 的 legacy `Main class / Secondary class` 视觉层还没完全迁移完成，所以正式验收必须明确：
  - canonical authority 看结构化导出和脚本校验
  - 不能把 legacy 行内显示直接当作最终分类真值

## 3. 后续阶段总路线

## 3.1 `Phase 3A` authoritative 语义冻结

### 目标

把“文档口径”和“脚本真实决议规则”彻底对齐，明确字段 ownership、导出优先级、canonical 与 mirror 的边界，以及允许值和精确字面值。

### 本阶段必须写死的内容

- authoritative pair 内各字段的 ownership 和 export-resolution 规则
- canonical classification derivation rule
- `scientific_object_modules` / `general_method_bucket` / `object_coverage_mode` / `primary_module_for_filing` 的精确定义
- `final_modules_or_bucket` 的镜像语法和顺序审计语义
- `pdf_path` 不等于本地真 PDF
- `pdf_status` / `evidence_status` / `source_limited` 的 authoritative 解释

### 本阶段产出

- `Coverage_Check/structured_data_authoritative_semantics_freeze_2026-07-02.md`
- `Data/README.md`
- `Data/field_dictionary.md`

### 本阶段验收标准

- 任意协作者都能说清某个字段该先改 master、progress，还是根本不能手改派生层。
- 任意协作者都能说清 canonical classification 与 workflow mirror 的区别。
- 项目内不再存在把 `01.04` 当 formal module、把 `primary_module_for_filing` 当完整分类、把 `pdf_path` 非空当作 PDF 真值的解释空间。

### 当前状态

- 状态：`进行中`
- 本轮动作：补齐 ownership matrix、fallback 规则、exact literal spec、mirror 语法说明

## 3.2 `Phase 3B` authoritative baseline 验收

### 目标

把 `447 / 422 / 25 / drift 0 / canonical 01.04 = 9` 正式写成可复核的 acceptance checklist，而不是只留在上下文对话里。

### 本阶段必须确认的检查项

- active confirmed-core = `447`
- active local PDF = `422`
- active no-local-PDF = `25`
- `422 + 25 = 447`
- `missing_pdf_manifest.json` 的 25 条都可索引，且都有 DOI
- canonical `01.04` bucket = `9`
- `01.04` 没有漏进 formal `scientific_object_modules`
- canonical assignments 在 `papers.jsonl` / `paper_modules.csv` / registry / SQLite 之间零漂移
- semantic drift = `0`
- order drift = `0`

### 本阶段产出

- `Coverage_Check/structured_data_authoritative_acceptance_checklist_447_2026-07-02.md`

### 本阶段验收 caveat

- baseline 验收通过，不等于 legacy 行级 schema migration 已完成
- 正式验收必须显式写明：canonical authority 不来自 legacy `Main class / Secondary class`

### 当前状态

- 状态：`进行中`
- 本轮动作：把 baseline 证据、spot-check 样本和 caveat 写进 checklist

## 3.3 `Phase 4` canonical-only 分析口径固化

### 目标

把分析体系固定成默认 canonical-only，确保后续统计、图表、综述正文都不会误用 workflow mirror。

### 本阶段要做什么

- 固定 record-level count 与 expanded assignment count 的区分
- 固定 `01.04` 独立统计，不并入 formal `01-11`
- 固定默认查询走 canonical classification
- 保留单独的 mirror-audit 命令和视图
- 给高频分析问题建立固定模板

### 建议固定的查询模板

- formal module distribution
- multi-module paper distribution
- canonical `01.04` bucket summary
- overall PDF coverage summary
- per-module PDF coverage
- boundary cases / bucket audit / source-limited inventory

### 产出

- `query_analysis_db.py` 的 canonical-only 说明与固定输出口径
- `Data/README.md` 中的分析使用规范

### 验收标准

- 相同问题不会因为读取 JSONL、CSV 或 SQLite 而得出不同语义的答案
- `01.04`、`11.07`、multi-module 在统计展示中都可解释、可复核

## 3.4 `Phase 5` 协作 SOP 与 baseline 更新纪律固化

### 目标

把“先改事实层，再导出派生层”的工作法固定成项目级纪律。

### 本阶段要做什么

- 明确哪些文件永远不能手改来修事实
- 固定 PR 前的 `export -> check -> build` 流程
- 固定 baseline 变更时的说明格式、批准责任和影响文件范围
- 固定 canonical / mirror / registry / analysis 四层职责

### 产出

- 面向协作者的简明 SOP
- baseline 更新规则
- 红线文件清单

### 验收标准

- 协作者能独立判断“新增、改类、补 PDF、改 note path”第一落点在哪一层
- CI 能阻断 authoritative pair 已改但派生层未重建的提交

## 3.5 `Phase 6` 面向综述生产的并行增强

### 目标

在 authoritative 口径和分析口径都稳定后，再启动真正值得并行化的生产队列。

### 合适的并行队列

- `note_revision_queue`
- `full_text_followup_queue`
- `representative_paper_pool`
- `module_coverage_pool`
- `boundary_case_pool`

### 原则

- 子 Agent 默认只读生成候选清单和证据包
- Main Controller 决定哪些内容正式写回 authoritative pair
- 若进入 note writeback，仍遵守单 note 单 owner、master/progress 单写

## 4. Main Controller 与子 Agent 的固定边界

### Main Controller 单写

- `agent_master_paper_list.md`
- progress 文件
- 正式治理方案
- baseline 验收文件
- 最终统计口径说明
- round report / commit / merge

### 子 Agent 默认只读

- 审核脚本与文档语义
- spot-check registry / manifests / SQLite
- 生成 drift、boundary、follow-up 队列
- 对 note writeback 轮次提出建议

### 非法操作

- 子 Agent 改 `agent_master_paper_list.md`
- 子 Agent 改 progress / report
- 把 `Data/*.json*`、`*.csv`、`*.sqlite` 手改当事实修复

## 5. 当前最容易发生的漂移

1. 把 `final_modules_or_bucket` 当 canonical classification source。
2. 把 `primary_module_for_filing` 当单主类事实。
3. 把 `01.04` 混回 formal `01-11` 统计。
4. 把 `pdf_path` 非空、读过全文、或 note 中“看过全文”误当作 PDF 真值。
5. 把 registry / analysis 层当纠错入口。
6. 把 legacy `Main class / Secondary class` 视觉显示当作最终分类 authority。
7. 在 authoritative 验收前继续扩展功能和并行任务。

## 6. 这份总方案之后的直接动作

1. 完成 `Phase 3A` 文档收口，把 ownership、fallback、literal、mirror 语法写严。
2. 完成 `Phase 3B` baseline checklist，把 `447 / 422 / 25 / 9 / drift 0` 写成正式验收记录。
3. 跑 `export -> check -> build` 验证当前收口文档没有引入口径漂移。
4. 提交本轮变更，作为 Phase 3AB-R1 的正式落地。
5. 下一轮进入 `Phase 4`，固化 canonical-only 查询与统计语义。

## 7. Definition of Done

当下面条件都满足时，可以认为 structured-data 后续治理主线进入稳定态：

1. authoritative pair 的 ownership、fallback 和解析优先级都已写死。
2. canonical classification 与 workflow mirror 的边界已固定。
3. baseline `447 / 422 / 25 / canonical 01.04 = 9 / drift 0` 已正式验收。
4. 默认查询和默认统计都以 canonical-only 为准。
5. baseline 更新纪律和 PR/CI 纪律已固定。
6. 后续 note 队列、全文跟进、综述写作支持都统一建立在这套口径上。
