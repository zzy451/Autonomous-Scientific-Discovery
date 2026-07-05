# Structured Data Catalog Round 43 Closeout

日期：2026-07-06

## 本轮目标

把 `discipline_local_code_registry` 这组 derived outputs 从“会写出 JSONL / CSV / SQLite”推进到“build 阶段会主动验证 CSV / SQLite 忠实反映当前 JSONL snapshot”，减少 registry 三层再次漂移的风险。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 为 registry CSV 增加 build-time 自校验

在 `build_analysis_db.py` 中新增：

- `normalize_discipline_local_code_registry_csv_row(...)`
- `validate_discipline_local_code_registry_outputs(...)`

当前 build 在写出 `discipline_local_code_registry.csv` 后，会回读 CSV 并校验它与当前 JSONL snapshot 的逐行结果一致。

### 2. 为 SQLite `discipline_local_code_registry` 增加 build-time 自校验

`validate_discipline_local_code_registry_outputs(...)` 同时会：

- 连接 `papers.sqlite`
- 查询 SQLite `discipline_local_code_registry`
- 按 `paper_id` 排序后，与当前 JSONL snapshot 逐字段比对

校验字段覆盖：

- `paper_id`
- `assignment_id`
- `discipline_local_code`
- `discipline_local_rank`
- `discipline_display_order`
- `assignment_status`
- `assigned_at`
- `assigned_by`
- `retired_at`
- `redirected_to_code`
- `assignment_reason`
- `pending_reason`
- `primary_module_for_filing`
- `primary_module_confidence`
- `primary_module_assignment_rule`
- `primary_module_override_reason`
- `primary_taxonomy_code_2lvl`
- `legacy_secondary_class`
- `secondary_class_source`
- `secondary_class_confidence`
- `secondary_class_review_status`
- `scientific_object_modules_json`
- `general_method_bucket`
- `title`
- `note_path`
- `pdf_path`
- `active_confirmed_core`
- `is_derived_snapshot`
- `generated_at`
- `generated_by`
- `source_commit`
- `worktree_dirty`

### 3. README 同步

在 `Data/README.md` 中补充说明：

- `build_analysis_db.py` 现在不仅自检 module surfaces
- 也会检查：
  - `discipline_local_code_registry.csv`
  - SQLite `discipline_local_code_registry`

是否忠实反映当前 JSONL snapshot

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- `export` 成功
- `check` 成功
- `build` 成功

这说明当前 registry 三层关系仍然一致：

- `discipline_local_code_registry.jsonl = 447` 行
- `discipline_local_code_registry.csv = 447` 行
- SQLite `discipline_local_code_registry = 447` 行

## 本轮结论

这一轮把 `discipline_local_code_registry` 从“有多层派生面”推进到了“多层派生面之间会在 build 阶段主动互相校验”。这样后续如果 JSONL / CSV / SQLite 之间任何一层发生字段次序、布尔编码、列表序列化或行覆盖漂移，不需要等人工 spot check，build 就会直接失败。
