# Structured Data Catalog Round 50 Closeout

日期：2026-07-06

## 本轮目标

把已经被 build gate 保护住的两个 SQLite inspection surface 正式开放给 `query_analysis_db.py`：

- `metadata`
- `analysis_object_scope_registry`

这样它们不再只是“存在且被自检”，而是可以被协作者直接查询、检查和复用。

## 本轮实现

更新：

- `scripts/query_analysis_db.py`
- `Data/README.md`

### 1. 新增 `metadata` 查询命令

新增：

- `metadata_summary(conn)`
- CLI 命令：
  - `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" metadata`

当前输出：

- SQLite `metadata` 表中的所有 `key / value`

适合快速检查：

- 当前 build 的 schema version
- `papers_jsonl_sha256`
- active counts
- active missing-PDF counts

### 2. 新增 `object-scope-registry` 查询命令

新增：

- `object_scope_registry(conn)`
- CLI 命令：
  - `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" object-scope-registry`

当前输出：

- `analysis_object_scope_registry` 全表

适合直接检查：

- SQLite 中各对象的 `object_type`
- `scope_class`
- `default_usage`
- `warning`

### 3. README 同步

在 `Data/README.md` 中补充：

- `metadata` 的示例命令
- `object-scope-registry` 的示例命令
- 两者在 `Operational notes` 中的语义说明

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" metadata
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" object-scope-registry
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- `metadata` 正常输出当前 build metadata：
  - `papers_record_count = 871`
  - `active_confirmed_core_count = 447`
  - `active_local_pdf_count = 422`
  - `active_no_local_pdf_count = 25`
- `object-scope-registry` 正常列出当前 SQLite object semantics registry
- `export` 成功
- `check` 成功
- `build` 成功

## 本轮结论

这一轮把两张已经被 build 自检保护的 SQLite 元信息表，正式提升为可查询的 inspection surface。这样当前的结构化层不仅在内部被验证，而且协作者也可以直接用命令看到：

- 本轮 build 的 metadata 是什么
- SQLite 中每个对象被声明成什么语义和默认用途
