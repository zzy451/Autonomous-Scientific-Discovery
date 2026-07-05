# Structured Data Catalog Round 47 Closeout

日期：2026-07-06

## 本轮目标

把 SQLite 里的元信息与基础 summary surfaces 也纳入 `build_analysis_db.py` 的 build-time fidelity checks，避免它们虽然是 build 核心对象，但还没有被主动核对。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 新增 metadata / summary table 自校验

在 `build_analysis_db.py` 中新增：

- `validate_metadata_and_summary_tables(...)`

当前 build 完成后会主动回查并校验：

- `taxonomy_index`
- `metadata`
- `active_confirmed_core_papers`
- `active_missing_local_pdf`

### 2. 当前对齐逻辑

校验来源分别是：

- `taxonomy_index`
  - 来自当前加载的 `taxonomy_index.json` code/label map
- `metadata`
  - 来自本轮 build 时实际计算的：
    - `schema_version`
    - `papers_jsonl_sha256`
    - `papers_record_count`
    - `active_confirmed_core_count`
    - `active_local_pdf_count`
    - `active_no_local_pdf_count`
- `active_confirmed_core_papers`
  - 必须与 `papers` 中 `active_confirmed_core = true` 的行数一致
- `active_missing_local_pdf`
  - 必须与当前 active 且 `pdf_exists = false` 的行数一致

### 3. 把新校验接入主构建流程

本轮把：

- `validate_metadata_and_summary_tables(...)`

接入 `main()`，与前几轮已经启用的：

- `papers`
- module surfaces
- discipline registry
- auxiliary analysis tables
- owner-loaded / inventory tables

一起成为真实 build gate。

### 4. README 同步

在 `Data/README.md` 中补充说明：

- `build_analysis_db.py` 现在还会自检：
  - `taxonomy_index`
  - `metadata`
  - `active_confirmed_core_papers`
  - `active_missing_local_pdf`

是否与当前 build inputs 和 active-record counts 保持一致。

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

说明当前元信息与 summary surfaces 也已经通过 build-time fidelity checks，没有发生：

- taxonomy code/label drift
- metadata count drift
- active view count drift

## 本轮结论

这一轮把 SQLite 里最基础的元信息 / summary objects 也纳入了 build gate。这样 `build_analysis_db.py` 现在不仅验证数据表本身，还开始系统性验证：

- 元信息表
- 基础计数视图
- owner-loaded tables
- derived analysis tables

都和当前输入事实保持一致。
