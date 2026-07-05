# Structured Data Catalog Round 42 Closeout

日期：2026-07-06

## 本轮目标

把 `paper_modules` / `workflow_mirror_paper_modules` / `mixed_scope_paper_modules` 这组刚完成语义重构的 build outputs，变成 `build_analysis_db.py` 自己会主动校验的对象，而不是只靠 README / field dictionary 解释其边界。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 为 module CSV surfaces 增加 build-time 自校验

在 `build_analysis_db.py` 中新增：

- `MODULE_ROW_FIELDNAMES`
- `assert_build_condition(...)`
- `normalize_module_csv_row(...)`
- `load_csv_rows(...)`
- `validate_module_csv_outputs(...)`

当前 build 在写出 CSV 后会回读并校验：

- `paper_modules.csv`
- `canonical_paper_modules.csv`
- `workflow_mirror_paper_modules.csv`
- `mixed_scope_paper_modules.csv`

确保它们分别精确匹配预期的：

- canonical rows
- canonical alias rows
- workflow rows
- mixed-scope union rows

并且保证：

- `paper_modules.csv == canonical_paper_modules.csv`

### 2. 为 SQLite module surfaces 增加 build-time 自校验

新增：

- `validate_sqlite_module_surfaces(...)`

当前 build 完成 SQLite 写入后，会主动查询并校验：

- `paper_modules`
- `workflow_mirror_paper_modules`
- `mixed_scope_paper_modules`
- `canonical_paper_modules`
- `module_assignment_counts`
- `canonical_module_assignment_counts`
- `workflow_mirror_module_assignment_counts`
- `mixed_scope_module_assignment_counts`

当前约束包括：

- `paper_modules` row count 必须等于 canonical rows
- `workflow_mirror_paper_modules` row count 必须等于 workflow rows
- `mixed_scope_paper_modules` row count 必须等于 canonical + workflow rows
- `paper_modules` 只允许 `assignment_scope = scientific_object_modules`
- `workflow_mirror_paper_modules` 只允许 `assignment_scope = final_modules_or_bucket`
- `mixed_scope_paper_modules` 必须暴露 canonical + workflow scope 的并集
- canonical / workflow / mixed-scope count views 必须分别与预期 row counts 一致

### 3. README 同步

在 `Data/README.md` 中补充说明：

- `build_analysis_db.py` 现在会主动校验 module-surface split
- `paper_modules` / `paper_modules.csv` 必须保持 canonical-only
- `workflow_mirror_paper_modules` 必须保持 workflow-only
- `mixed_scope_*` 必须保持显式 compatibility union

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

build 产出的 module surfaces 当前通过自校验，保持：

- `paper_modules rows = 843`
- `workflow_mirror_paper_modules rows = 592`
- `mixed_scope_paper_modules rows = 1435`

## 本轮结论

这一轮把 module relation 这组对象从“语义上已经理顺”推进到了“build 时会主动验证边界”。这样如果以后有人在 `build_analysis_db.py` 里又把 canonical/workflow/mixed-scope 关系改乱，不需要等到人工读 README 才发现，构建阶段就会直接失败。
