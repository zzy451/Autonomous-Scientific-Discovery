# Structured Data Catalog Round 45 Closeout

日期：2026-07-06

## 本轮目标

把 SQLite 中仍属于“直接载入型”的几张表也纳入 build-time fidelity checks，避免它们虽然来自 owner/manifest source，但写入 SQLite 后没有被主动核对。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 新增 owner-loaded / inventory table 自校验

在 `build_analysis_db.py` 中新增：

- `validate_owner_loaded_and_inventory_tables(...)`

当前 build 完成后，会主动回查并校验以下 SQLite tables：

- `change_log`
- `classification_terms`
- `discipline_code_assignments`
- `pdf_inventory`
- `missing_pdf_inventory`
- `note_inventory`

### 2. 每张表的当前对齐来源

build 当前校验的来源关系是：

- `change_log` <- `Data/change_log.jsonl`
- `classification_terms` <- `build_classification_term_rows(classification_code_index)`
- `discipline_code_assignments` <- `Data/discipline_code_assignments.jsonl`
- `pdf_inventory` <- `Data/pdf_manifest.json`
- `missing_pdf_inventory` <- `Data/missing_pdf_manifest.json`
- `note_inventory` <- `Data/note_manifest.json`

这些表现在不再只是“插入成功就算完成”，而是会在当前 run 中逐字段和预期 source rows 比对。

### 3. 把新校验接入主构建流程

本轮不只是新增 helper，也把它接入了 `main()`：

- 在 `build_sqlite(...)` 完成后执行
- 和前几轮的 module/registry/auxiliary self-validation hooks 一起成为真实 build gate

### 4. README 同步

在 `Data/README.md` 中补充说明：

- `build_analysis_db.py` 现在还会自检：
  - `classification_terms`
  - `discipline_code_assignments`
  - `change_log`
  - `pdf_inventory`
  - `missing_pdf_inventory`
  - `note_inventory`

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

说明当前 SQLite 中这组 direct-load / inventory tables 也已经通过 build-time fidelity checks，没有发生 source-row 漂移。

## 本轮结论

这一轮把 SQLite 里最后一批“明显是载入型、但还没被 build 主动核对”的表也拉进了 self-validation 范围。这样 `build_analysis_db.py` 现在不只是验证 module/registry/analysis tables，也开始系统性验证 owner-loaded 与 inventory tables 的写入忠实性，离“关键 derived / loaded surfaces 都有 gate”又近了一步。
