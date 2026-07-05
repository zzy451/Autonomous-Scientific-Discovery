# Structured Data Catalog Round 30 Closeout

日期：2026-07-06

## 本轮目标

把上一轮 dry-run 暴露出来的 taxonomy owner 覆盖缺口真正补齐：当前 master 中已有合法 legacy `Secondary class`，但 `Data/classification_code_index.json` 还缺少以下 4 个 secondary terms：

- `05.03`
- `10.04`
- `11.03`
- `11.04`

## 本轮实现

### 1. 使用 taxonomy owner helper 正式补齐缺失 secondary terms

使用：

- `scripts/manage_classification_code_index.py`

正式新增：

- `05.03`
- `10.04`
- `11.03`
- `11.04`

当前写入语义与已有 legacy seed term 保持一致：

- `label = Legacy secondary filing term <code>`
- `status = needs_review`
- `review_status = unreviewed`
- `source = legacy_secondary_class_seed_2026-07-06`

这一步没有把它们伪装成已经 canonicalized 的二级 taxonomy，只是先补齐 owner coverage。

### 2. 同步 paper-level 审计链

本轮新增 secondary term 时，同时使用 helper 的：

- `--append-change-log`

为受影响论文追加了 `Data/change_log.jsonl` 审计行。

本轮新增的 change_log 类型为：

- `taxonomy_owner_add_secondary`

受影响论文数量：

- `05.03` -> `1`
- `10.04` -> `2`
- `11.03` -> `8`
- `11.04` -> `2`

合计：

- `13` 条 `change_log` rows

### 3. 派生层已同步重建

由于 owner taxonomy 与 `change_log` 都发生了真实变化，本轮同步刷新了：

- `papers.jsonl`
- `papers.csv`
- `discipline_local_code_registry.jsonl`
- `discipline_local_code_registry.csv`
- `registry/*`
- `papers.sqlite`
- `integrity_check_report.md`

其中受影响论文的 `last_reviewed_at / last_reviewed_by` 也会通过现有 change-log-derived lane 自动更新。

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- export 成功
- check 成功
- build 成功

额外 spot check：

- 当前 master 中合法 secondary codes 全部已被 taxonomy owner 覆盖：
  - `missing_from_owner = []`
- `Data/change_log.jsonl` 当前共有：
  - `13` 行
- 当前新增的 `change_type` 为：
  - `taxonomy_owner_add_secondary`

## 本轮结论

本轮把 taxonomy owner 从“能够初始化/维护”进一步推进到了“对当前 master legacy secondary class 全覆盖”的状态。这样现阶段的二级位 owner 已经不再明显缺项，后续 review/merge/split 工作可以在完整覆盖的基础上推进，而不是先补洞。
