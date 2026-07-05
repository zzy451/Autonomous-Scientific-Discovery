# Structured Data Catalog Round 46 Closeout

日期：2026-07-06

## 本轮目标

把 `papers.jsonl -> papers.csv / SQLite papers` 这条最核心的 analysis surface 也纳入 `build_analysis_db.py` 的 build-time fidelity checks，避免核心快照只是在 build 中被写出，却没有被主动核对。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 新增 papers CSV fidelity check

在 `build_analysis_db.py` 中新增：

- `normalize_papers_csv_row(...)`
- `validate_papers_outputs(...)`

当前 build 完成后会回读：

- `Data/papers.csv`

并验证它是否逐行忠实反映当前：

- `Data/papers.jsonl`

### 2. 新增 SQLite `papers` fidelity check

`validate_papers_outputs(...)` 同时会：

- 查询 SQLite `papers`
- 按 `paper_id` 排序
- 与当前 `papers.jsonl` 逐字段比对

当前覆盖字段就是 `papers` 表的完整写入面，包括：

- 基础 bibliographic fields
- canonical classification fields
- primary filing trace fields
- workflow mirror fields
- lifecycle fields
- exported timestamp

也就是说，SQLite `papers` 现在不再只是“插入成功”，而是会被 build 阶段逐字段验证是否忠实反映 JSONL snapshot。

### 3. 把新校验接入主构建流程

本轮把：

- `validate_papers_outputs(papers)`

接入 `main()`，位置在：

- `build_sqlite(...)` 之后
- module / registry / auxiliary / owner-loaded self-validation hooks 之前

这样 `papers` 这条核心 analysis surface 已经成为真实 build gate。

### 4. README 同步

在 `Data/README.md` 中补充说明：

- `build_analysis_db.py` 现在还会自检：
  - `papers.csv`
  - SQLite `papers`

是否忠实反映当前 `papers.jsonl`

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

这说明当前：

- `papers.jsonl = 871` 行
- `papers.csv = 871` 行
- SQLite `papers = 871` 行

并且 build-time fidelity check 通过，没有发生 CSV / SQLite 对 JSONL snapshot 的字段漂移。

## 本轮结论

这一轮把最核心的 analysis snapshot 也正式拉进了 build gate。到这里，`build_analysis_db.py` 已经不只是验证外围 tables，而是开始系统性验证：

- 核心 `papers` surface
- module surfaces
- discipline registry surfaces
- auxiliary analysis tables
- owner-loaded / inventory tables

都没有在当前 run 中发生写入漂移。
