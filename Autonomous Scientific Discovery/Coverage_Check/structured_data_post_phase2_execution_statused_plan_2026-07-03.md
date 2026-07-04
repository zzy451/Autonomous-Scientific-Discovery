# ASD structured-data 后续执行方案（承接 Phase 1-2，并固化当前阶段状态）

日期：2026-07-03
适用范围：`Autonomous Scientific Discovery` 当前 `447` 篇 active confirmed-core 主线
文档定位：本文件明确回答“现在这条方案是不是接着前两阶段走”的问题。答案是：**是**。本文件不是另起炉灶，而是把 `Phase 1-2` 之后已经实际落地的阶段成果、当前真实执行位置、以及后续继续推进的固定路径写成一份可直接执行的 controller-facing 方案，避免长上下文导致计划漂移。

## 1. 当前总判断

我们现在走的是同一条连续主线：

- `Phase 1`：总方案与治理方向冻结，已完成
- `Phase 2`：结构化导出、校验、分析数据库、GitHub 协作底座，已完成
- 此后不是重新规划，而是沿着既定主线继续推进后续阶段

换句话说，当前工作不是“再讨论要不要做 structured-data”，而是：

1. 已把 structured-data 底座搭好
2. 已把 authoritative 口径收紧
3. 已进入真实 `Phase 6` 生产执行

## 2. 当前 authoritative baseline

截至 `2026-07-03`，当前稳定 baseline 仍然是：

- active confirmed-core：`447`
- active local PDF：`422`
- active no-local-PDF：`25`
- active canonical `01.04` bucket：`9`
- workflow mirror semantic drift：`0`
- workflow mirror order drift：`0`

当前 authoritative pair 仍然只有这两份：

1. `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md`
2. `Autonomous Scientific Discovery/Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

硬规则不变：

- 所有推进、统计、复核、缺失检查都必须以 master 为准
- 不能用 `Notes/` 平铺扫描代替 master
- 子 Agent 不能修改 master
- 子 Agent 不能修改 progress / report
- authoritative baseline 改动后，必须回到 `export -> check -> build`

## 3. 已完成阶段状态表

### 3.1 `Phase 1`

已完成内容：

- 总方案主线冻结
- single-writer authoritative discipline 明确
- multi-agent 基本治理方向明确

当前作用：

- 仍然有效，作为后续所有阶段的治理前提

### 3.2 `Phase 2`

已完成内容：

- 结构化导出脚本落地
- 数据一致性校验脚本落地
- SQLite 分析库与查询 CLI 落地
- GitHub 协作底座、PR/CI 纪律落地

当前作用：

- 已成为后续所有 baseline 验证和统计分析的默认工具链

### 3.3 `Phase 3A`

已完成落地：

- `Coverage_Check/structured_data_authoritative_semantics_freeze_2026-07-02.md`

当前作用：

- authoritative pair 与结构化导出层之间的语义映射已冻结
- `pdf_path`、`pdf_status`、`evidence_status`、`scientific_object_modules`、`general_method_bucket`、`primary_module_for_filing` 的解释边界已经写死

### 3.4 `Phase 3B`

已完成落地：

- `Coverage_Check/structured_data_authoritative_acceptance_checklist_447_2026-07-02.md`
- `Coverage_Check/structured_data_authoritative_acceptance_snapshot_2026-07-02.md`

当前作用：

- `447 / 422 / 25 / 9 / drift 0` 已形成正式验收记录
- 后续所有 round 都必须把这个 baseline 当成回归检查基线

### 3.5 `Phase 4`

当前判断：

- canonical-only 分析口径已经实质进入当前脚本和分析层
- 这部分不再是主线阻塞项

已落地支撑：

- `scripts/build_analysis_db.py`
- `scripts/query_analysis_db.py`
- `Data/README.md`

执行口径：

- 默认分析口径看 canonical classification
- workflow mirror 只用于审计和对齐，不作为默认分析 truth

### 3.6 `Phase 5`

当前判断：

- 协作 SOP 与 baseline 更新纪律已经进入仓库机制
- 当前也不再是主线阻塞项

已落地支撑：

- `.github/workflows/structured-data-guard.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `CODEOWNERS`

执行口径：

- authoritative 文件发生改动后，必须跑 `export -> check -> build`
- 不能手改 `Data/` 来倒逼事实层

### 3.7 `Phase 6`

当前判断：

- **我们现在就在真实 `Phase 6`**
- 当前主线已经从“方案设计”切到“基于稳定 baseline 的并行生产执行”

## 4. 当前已经完成的 Phase 6 关键节点

### 4.1 Queue refresh 已完成

已完成文件：

- `Coverage_Check/structured_data_phase6_queue_refresh_after_round5_closeout_2026-07-02.md`
- `Coverage_Check/structured_data_phase6_queue_refresh_after_round6_closeout_2026-07-03.md`
- `Coverage_Check/structured_data_phase6_queue_refresh_after_round8_closeout_2026-07-03.md`
- `Coverage_Check/structured_data_phase6_queue_refresh_after_round12_closeout_2026-07-04.md`

这一步已经确认：

- 刷新后的队列和 authoritative pair 对齐
- baseline 仍然稳定为 `447 / 422 / 25 / drift 0`
- follow-up queue 已从 stale pre-R5 anchors 刷到 post-R12 authoritative 状态

### 4.2 Note revision round 1 已完成

已完成文件：

- `Coverage_Check/structured_data_phase6_note_revision_round1_plan_447_2026-07-02.md`
- `Coverage_Check/structured_data_phase6_note_revision_round1_landing_decision_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_note_revision_round1_closeout_2026-07-02.md`

本轮真实结论：

- 这是 note-only wording harmonization 轮次
- read-only agents 成功返回了可用建议
- writeback agent 没有按理想方式返回完整 completion packet
- controller 没有假装“agent 正常完成”，而是诚实记录失败，并在 worktree 中人工复核已出现的 note diff 后接受落地

这一点必须保留为正式事实，后续不能把这一轮误写成“标准成功 writeback-agent round”

### 4.3 Follow-up rounds 6-12 已完成

已完成文件族：

- `Coverage_Check/structured_data_phase6_followup_round6_*_2026-07-03.*`
- `Coverage_Check/structured_data_phase6_followup_round7_*_2026-07-03.*`
- `Coverage_Check/structured_data_phase6_followup_round8_*_2026-07-03.*`
- `Coverage_Check/structured_data_phase6_followup_round9_*_2026-07-03.*`
- `Coverage_Check/structured_data_phase6_followup_round10_*_2026-07-03.*`
- `Coverage_Check/structured_data_phase6_followup_round11_*_2026-07-04.*`
- `Coverage_Check/structured_data_phase6_followup_round12_*_2026-07-04.*`

当前已经确认的真实推进包括：

- `R6`：`ASD-0381` 获得 evidence-state 升级并移出高压 `source_limited=yes` frontier
- `R7`：完成一次完整 evidence-only conservative-hold round，没有假装产生 authoritative landing
- `R8`：`ASD-0735` 获得本地合法可读 PDF 并 landed，baseline 从 `421 / 26` 前进到 `422 / 25`
- `R8` 同时对 `ASD-0572`、`ASD-0727` 做了 note-only refresh，对 `ASD-0859`、`ASD-0860`、`ASD-0861` 保持保守挂起
- `R9`：完成一次 fresh bounded six-paper evidence-only conservative-hold round，并为后续 note harmonization 提供更强一手来源链
- `note revision round 3`：对 `ASD-0536`、`ASD-0617`、`ASD-0855` 做了 note-only harmonization，authoritative pair 未改
- `R10Approx`：在无真实子 Agent 的环境里，用并行工具保持角色边界，完成 6 篇 follow-up，其中 `ASD-0006`、`ASD-0090`、`ASD-0687`、`ASD-0506` 获得 authoritative landing，4 篇的 `source_limited=yes -> no` 与 `evidence_status -> first_hand_full_text` 被正式落地
- `R11Approx`：完成下一组 fresh six-paper evidence-only conservative-hold round；对 `ASD-0005`、`ASD-0158`、`ASD-0097`、`ASD-0112`、`ASD-0603`、`ASD-0569` 补强了 publisher/preprint/XML/license 级一手来源链，但没有夸大为已读全文或已获本地 PDF
- `R12Approx`：完成下一组 local-PDF source-limited 清压 round；`ASD-0507`、`ASD-0684`、`ASD-0084`、`ASD-0666`、`ASD-0667`、`ASD-0653` 全部获得 authoritative landing，6 篇的 `source_limited=yes -> no` 与 `evidence_status -> first_hand_full_text` 被正式落地，并已同步刷新 post-R12 Phase 6 队列

## 5. 当前 Phase 6 的真实位置

当前最重要的状态不是“继续写治理文档”，而是：

- 已完成 queue refresh
- 已完成 note revision rounds `1-3`
- 已完成 bounded follow-up rounds `R6-R12`
- `R12Approx` 后的 authoritative 与派生层已经重新导出、校验、建库并刷新 Phase 6 队列
- 当前队列已经不再把 `ASD-0507`、`ASD-0684`、`ASD-0084`、`ASD-0666`、`ASD-0667`、`ASD-0653` 继续错误暴露为 local-PDF source-limited pressure
- 当前自然下一步是：**继续在 post-R12 queue 上，以 freshness override 选择下一组 bounded round；优先处理仍未落地的 no-local-PDF / non-full-text frontier**

也就是说，我们现在不是停留在 `Phase 1-2`，也不是停留在 `Phase 3-5`，而是已经进入 `Phase 6` 的连续执行段。

这里要额外写死一个纪律：

- `full_text_followup_queue` 只负责暴露 follow-up pressure
- queue 不是 authoritative work-selection truth
- 任何下一轮 launch 都必须先由 controller 基于当前 master 状态重新冻结 round packet
- 旧的 round1 slice / packet 文件不能被不经检查地直接复用成新的 launch truth

## 6. 当前后续主线路径

后续固定按下面这条路径走，不再反复改口：

1. 保持 authoritative baseline 稳定
2. 用 `Phase 6` 队列识别 follow-up pressure，但不把队列本身当 authority
3. 先做 read-only evidence round
4. 再做 read-only classification review
5. 再由 controller 决定是否进入 note writeback
6. 如需 authoritative 落地，再由 controller 单写 master / progress / closeout
7. round 结束后提交 git、清空 worktree、关闭全部 round agents

## 7. 下一轮 controller 候选 focus set

本节不是“已经对齐现有 packet 文件的正式 launch packet”，而是：

- controller 基于当前 refreshed queue 提取出的**候选 focus set**
- 用于说明下一轮最自然的 follow-up 方向
- 不能替代正式的 round packet 冻结动作

按照当前 `R11Approx` 已处理完的 frontier，下一轮 controller 更自然的候选方向不再是重复 `R11Approx` 的 6 篇，而是二选一：

1. 继续下一个 fresh non-safety follow-up set
2. 转入 bounded note-only harmonization，对 `R11Approx` 中如果有 wording value 但没有 authority delta 的记录做保守 note refresh

但在正式 launch 前，controller 还必须先做下面四步：

1. 回到当前 `agent_master_paper_list.md` 核对这 6 篇的 live row state
2. 为这一轮新建 round-specific packet 文件，而不是直接沿用旧的 round1 slices
3. 明确写出 non-overlapping ownership
4. 在 round packet 中把这些 paper 组织成新的 controller-approved bounded slice

当前这样写的原因也要说明白：

- refreshed queue 已经反映 post-R8 事实
- 但 queue 仍然是 recency-blind，不能直接把 same-day re-evidenced rows 当作 launch truth
- 所以下一轮应基于 refreshed queue 加 controller freshness override 重新发包，而不是把历史 packet 或 score-only top rows 直接当成当前 truth

如果 controller 继续做 fresh evidence round，建议重新基于当前 queue 和 freshness override 再冻结新 packet，而不要直接复用 `R11Approx` 的这 6 篇。

这只是候选 ownership 草案，不等于已落地 packet 文件。

这一轮的目标应明确为：

- 刷新 first-hand source status
- 确认 local PDF / no-local-PDF / source-limited 状态
- 补强 object-level evidence
- 重新检查模块锚点是否仍稳定
- 为后续 note-only 或 authoritative landing 提供证据基础

## 8. 下一轮固定组织方式与发包纪律

### 8.1 子 Agent 角色

- `Evidence-Agent-A/B/C`：只读收集证据，不改任何项目文件
- `Classification-Reviewer`：只读审阅**合并后的 evidence packs**，不改任何项目文件；不得把旧 note 结论当 authority
- `Writeback-Agent-*`：只有在 controller 冻结 landing subset 后才可启动，且只能修改自己拥有的 note
- `PDF-Archive-Agent`：只有当本轮确实需要落地新的 PDF archive write 时才启动；可以写 `Reference_PDF/`，但不能修改 note / master / progress / report

### 8.2 Controller 单写职责

以下内容始终只能由 controller 处理：

- `agent_master_paper_list.md`
- progress 文件
- round closeout / report
- 最终 git commit
- baseline recount
- round packet 的最终冻结

### 8.3 绝对禁止

- 子 Agent 修改 master
- 子 Agent 修改 progress
- 子 Agent 修改 round report
- 子 Agent 把旧 note 结论当成最终分类 authority
- 未冻结 landing subset 就提前启动 writeback
- 未完成 note writeback 就先写 master
- 一个 note 文件被多个 writeback agents 同轮共写
- 未明确 archive ownership 就写入 `Reference_PDF/`

### 8.4 发包与回包最低契约

每个 evidence agent 的 launch packet 至少要写清：

- round label
- owned paper list
- `paper_id`
- `title`
- `note_path`
- DOI / URL / remarks leads
- “只读，不改项目文件”
- 必须返回 evidence contract 字段

每个 evidence agent 的回包至少要含有：

- `paper_id`
- `first_hand_sources_checked`
- `local_pdf_found`
- `recommended_pdf_url_or_status`
- `concrete_scientific_objects`
- `concrete_object_evidence`
- `suggested_modules`
- `suggested_01_04_bucket`
- `primary_module_for_filing`
- `confidence`
- `source_limited`
- `safety_or_access_note`

`Classification-Reviewer` 的 launch packet必须明确：

- 只基于 merged evidence packs 裁决
- 旧 note、旧 report、legacy fields 只作线索
- 必须返回 supported modules / `01.04` / confidence / source-limited / note revision need / master update need

`Writeback-Agent-*` 的 launch packet必须明确：

- 只处理 approved landing subset
- one note file, one owner
- 不能按同一 note 的 section 拆分双写
- 必须回报 changed / untouched / blocker

### 8.5 writeback 失败时的前向纪律

如果写回 agent 再次没有按要求返回 completion packet：

- 不得假装该 agent 正常完成
- controller 可以检查已经出现的 owned note diff
- 只有在 diff ownership 清晰、内容可复核、且 closeout 明确记录“agent non-return but controller-reviewed landing”时，才允许保守接住
- 该轮 closeout 必须显式标明不是标准成功 writeback-agent return
- 如 ownership 不清、diff 不完整或有越权文件，本轮不得推进 authoritative landing

## 9. 下一轮完成定义

下一轮 bounded follow-up round 只有在以下条件同时满足时才算完成：

1. evidence agents 全部返回 per-paper evidence rows
2. classification reviewer 返回独立裁决 rows
3. controller 写出 landing / hold decision
4. 如有 writeback，writeback ownership 明确，且每个 landed note 都有可审阅 diff
5. controller 已检查每个 writeback note diff
6. controller 已确认没有子 Agent 修改 master / progress / report
7. controller 只对 owned note writeback 完成的 paper 才允许进入 authoritative landing 集
8. conservative hold papers 没有被误计入 landed statistics
9. 如本轮涉及 PDF archive write，archive ownership 和 note wording 已对齐
10. 如 authoritative pair 被修改，已执行 `export -> check -> build`
11. 即使是 note-only round，也已确认只改了允许文件，且未引入 master / progress drift
12. 已写 closeout 文件
13. 已提交 git
14. worktree 再次干净
15. 本轮 agent 全部关闭

## 10. 这份方案之后不该再发生的漂移

后续不要再把下面几件事说混：

1. 不要把“承接 `Phase 1-2`”误解成“我们现在还停留在前两阶段”
2. 不要把当前 `Phase 6` 执行线重新改写成治理文档阶段
3. 不要把 queue / pool / packet 文件误当作 authoritative truth
4. 不要把 note round 和 authoritative round 混写
5. 不要把“agent 失败但 controller 人工接住并复核落地”的轮次，误写成“agent 正常完成”

## 11. 当前一句话版本

**是的，这份方案就是承接我们已经完成的 `Phase 1-2` 继续往下走；而且按当前仓库真实状态，我们已经不在前两阶段本身，而是在稳定 baseline 上执行 `Phase 6` 的后续轮次。**
