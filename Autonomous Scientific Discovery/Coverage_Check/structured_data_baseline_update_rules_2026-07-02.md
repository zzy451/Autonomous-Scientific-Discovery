# ASD structured-data baseline 更新规则

日期：2026-07-02
对应阶段：`structured_data_post_phase2_execution_plan_2026-07-02.md` 的 `Phase 5`

本文档定义什么算 baseline 更新、谁可以批准、更新时必须附带什么证据，以及哪些伴随文档必须同步更新。

## 1. baseline update 的定义

以下任一情况都视为 baseline 更新：

- `active_confirmed_core` 数量变化
- `active_local_pdf` 数量变化
- `active_no_local_pdf` 数量变化
- canonical `01.04` bucket 数量变化
- active confirmed-core 成员集合变化
- canonical classification 规则变化，导致 expanded assignment 语义变化
- `workflow mirror semantic drift` 的正式 accepted 值变化

以下通常不算 baseline 更新：

- 纯文档润色
- 纯 CI 文案或注释调整
- 不影响 accepted baseline 的 query / README 表述增强
- 纯 mirror 顺序修正，且 accepted drift baseline 不变

当前 live accepted baseline 以：

- `Coverage_Check/structured_data_authoritative_acceptance_checklist_447_2026-07-02.md`

或其后继 dated acceptance checklist 为准。

`structured_data_authoritative_semantics_freeze_2026-07-02.md` 负责冻结字段语义和 ownership，不负责维护 live baseline 数字。

## 2. 批准权与写入权

- baseline 更新必须由 Main Controller 收口
- 子 Agent 可以只读审查、出证据、做 spot-check
- 子 Agent 不得直接改 master / progress / report 来完成 baseline 更新

## 3. baseline 更新的起点

baseline 更新只能从 authoritative pair 发起：

1. `agent_master_paper_list.md`
2. `multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

不得从以下层倒推修正 baseline：

- `Data/`
- registry
- CSV
- SQLite
- manifest

## 4. baseline 更新 PR 必须附带的证据

若 PR 改变 accepted baseline，必须在 PR 模板中补齐：

- old baseline
- new baseline
- approval by
- snapshot id：`schema_version` / `papers_jsonl_sha256`
- canonical-only semantics reconfirmed：`yes`
- `check_data_consistency.py` 关键输出
- 至少一个 `query_analysis_db.py` baseline 命令输出

推荐最小命令集：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" analysis-baseline
```

## 5. baseline 更新时必须同步的文件

至少同步以下内容：

- authoritative pair 中被改动的事实层文件
- 对应的 regenerated `Data/` outputs
- 当前 baseline acceptance 主记录：
  - `Coverage_Check/structured_data_authoritative_acceptance_checklist_447_2026-07-02.md`

`structured_data_authoritative_acceptance_snapshot_2026-07-02.md` 可保留为历史验收记录，但 baseline 更新的默认同步目标应以上述 acceptance checklist 或其后继 dated checklist 为准。

若 baseline 数值变化影响 master 顶部摘要，也必须同步修正 master 摘要。

## 6. baseline 更新 PR 的范围约束

baseline 更新 PR 应尽量单主题、单目的。

不建议把以下内容混在一个 baseline PR 里：

- 无关的样式修复
- 大规模脚本重构
- 与 baseline 无关的治理文档润色

## 7. 审查重点

reviewer 至少要检查：

- canonical / mirror 是否混用
- `01.04` 是否仍保持独立 bucket
- PDF 口径是否仍以本地真 PDF 为准
- accepted baseline 数字与 active ID 集是否一致
- regenerated outputs 是否齐全
- `workflow mirror drift` 是否被重新解释并说明

## 8. 合并与回滚

- 若 PR 缺少 baseline 证据包，即使 CI 通过，也不应合并
- 若已合并后发现 baseline 口径错误，回滚也必须从 authoritative pair 发起，而不是手改 `Data/`

## 9. 记录规则

每次 baseline 更新都应留下可追溯的日期化记录，至少能回答：

- 谁批准
- 为什么改
- old baseline 是什么
- new baseline 是什么
- 影响了哪些 authoritative files 和 derived outputs
