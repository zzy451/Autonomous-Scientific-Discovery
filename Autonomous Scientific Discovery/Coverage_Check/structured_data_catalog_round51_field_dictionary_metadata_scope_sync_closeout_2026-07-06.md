# Structured Data Catalog Round 51 Closeout

日期：2026-07-06

## 本轮目标

把已经进入 build gate、而且已经开放 query surface 的两张 SQLite 元信息表，也正式补进 `field_dictionary.md`：

- `metadata`
- `analysis_object_scope_registry`

这样 README、build gate、query surface 与字段词典对它们的解释保持一致。

## 本轮实现

更新：

- `Data/field_dictionary.md`

### 1. 新增 SQLite `metadata` 词典条目

新增：

- `4.6 SQLite metadata`

明确：

- 这是一张 build metadata 表
- 当前包含：
  - `schema_version`
  - `papers_jsonl_sha256`
  - `papers_record_count`
  - `active_confirmed_core_count`
  - `active_local_pdf_count`
  - `active_no_local_pdf_count`
- 它不是 owner fact source
- 当前 `build_analysis_db.py` 已会自检其 rows 是否与本轮 build 输入/计数一致
- 当前 `query_analysis_db.py` 已提供 `metadata` 查询命令

### 2. 新增 SQLite `analysis_object_scope_registry` 词典条目

新增：

- `4.7 SQLite analysis_object_scope_registry`

明确：

- 这是一张 SQLite 对象语义注册表
- 它记录：
  - `object_name`
  - `object_type`
  - `scope_class`
  - `default_usage`
  - `warning`
- 它不是新的事实源，而是对象解释层
- 当前 `build_analysis_db.py` 已会自检：
  - rows 与 build 脚本声明一致
  - 注册表对象真实存在
  - `object_type` 与实际 `table/view` 匹配
- 当前 `query_analysis_db.py` 已提供 `object-scope-registry` 查询命令

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

说明本轮仅同步词典语义，没有破坏现有 build/check/export 流程。

## 本轮结论

这一轮不新增新的导出逻辑，而是把两张已经成熟的 SQLite 元信息表正式纳入字段词典。到这里，`metadata` 和 `analysis_object_scope_registry` 已经同时在：

- build gate
- query surface
- README
- field_dictionary

四处对齐，后续继续推进时不容易再出现“代码里已经有、词典里却没有定义”的漂移。
