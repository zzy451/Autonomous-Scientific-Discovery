# Structured Data Catalog Round 52 Closeout

日期：2026-07-06

## 本轮目标

补齐 `analysis_object_scope_registry` 的覆盖范围，把一批已经真实存在、而且很常用的 supporting tables/views 也正式纳入对象语义注册表，而不是只注册较早的一小部分对象。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`

### 1. 扩充 object-scope registry 覆盖范围

在 `build_analysis_object_scope_rows()` 中新增以下对象声明：

- `active_confirmed_core_papers`
- `active_missing_local_pdf`
- `metadata`
- `taxonomy_index`
- `pdf_inventory`
- `missing_pdf_inventory`
- `note_inventory`

### 2. 新增对象的当前语义

本轮补入的对象当前被声明为：

- `active_confirmed_core_papers`
  - `view`
  - `derived_snapshot`
  - active paper convenience subset
- `active_missing_local_pdf`
  - `view`
  - `workflow_status`
  - missing-PDF follow-up subset
- `metadata`
  - `table`
  - `build_metadata`
  - build/run metadata lookup
- `taxonomy_index`
  - `table`
  - `taxonomy_lookup`
  - compact code/label join surface
- `pdf_inventory`
  - `table`
  - `derived_snapshot`
  - local PDF inventory lookup
- `missing_pdf_inventory`
  - `table`
  - `workflow_status`
  - no-local-PDF follow-up lookup
- `note_inventory`
  - `table`
  - `derived_snapshot`
  - note inventory compatibility lookup

### 3. 现有 gate 自动覆盖新对象

因为前几轮已经把 `analysis_object_scope_registry` 纳入 build gate，所以这次扩充不是只改说明文字：

- build 会检查这些新对象的注册行存在
- build 会检查它们在 SQLite 中真实存在
- build 会检查它们的 `object_type` 与实际 `table/view` 类型一致

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" object-scope-registry
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" object-scope-registry
```

结果：

- build 前 query 确认旧 registry 未显示这批 supporting objects
- `export` 成功
- `check` 成功
- `build` 成功
- build 后 query 成功显示新增对象：
  - `active_confirmed_core_papers`
  - `active_missing_local_pdf`
  - `metadata`
  - `taxonomy_index`
  - `pdf_inventory`
  - `missing_pdf_inventory`
  - `note_inventory`

## 本轮结论

这一轮把 object-scope registry 从“只覆盖部分核心对象”推进到了“开始覆盖 supporting metadata / inventory / convenience-view 层”。这样 SQLite 中更大一部分实际存在并被使用的对象，已经拥有统一的 scope class、默认用途和 warning 说明，并且这些说明会被 build gate 主动验证。
