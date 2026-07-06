# Structured Data Catalog Round 104 Closeout

日期：2026-07-06

## 本轮目标

继续加固 derived registry metadata 的一致性。当前多个 `Data/registry/*` 派生文件已经携带 `exported_at`，但此前 `check_data_consistency.py` 还没有统一验证这些 registry 的导出时间是否：

- 字段存在
- 全表一致
- 与 `papers.jsonl` 的导出快照时间一致

本轮把这条约束正式前移到 `check` 阶段。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 新增通用 registry `exported_at` 校验辅助函数

新增：

- `assert_registry_exported_at(path, rows, expected_exported_at)`

作用：

- 要求 registry 行包含 `exported_at`
- 要求同一 registry 文件的 `exported_at` 全表统一
- 要求其值与 `papers.jsonl exported_at` 完全一致

### 2. 对行式 registry 统一启用 `exported_at` 对齐检查

本轮将以下派生 registry 全部纳入统一校验：

- `Data/registry/paper_registry.jsonl`
- `Data/registry/paper_identifier_aliases.jsonl`
- `Data/registry/classification_assignments.jsonl`
- `Data/registry/pdf_archive_registry.jsonl`
- `Data/registry/asset_manifest.jsonl`

这让这些 derived registry 不再只是“各自带了一个时间戳”，而是必须共同指向与 `papers.jsonl` 相同的导出快照基线。

### 3. 补 `taxonomy_registry.json` 顶层 `exported_at` 校验

`taxonomy_registry.json` 不是 JSONL，而是带顶层对象的 JSON 文件。此前只校验了 `taxonomy_terms` 内容与 `taxonomy_index.json` 的 code/label/kind 对齐，但还没有核对其顶层：

- `exported_at`

本轮新增：

- `taxonomy_registry.json` 必须是 JSON object
- 其顶层 `exported_at` 必须与 `papers.jsonl exported_at` 一致

这样 taxonomy registry 的 snapshot metadata 也被纳入统一时点约束。

## 验证

运行：

```bash
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

结果：

- `export_structured_data.py` 通过
- `check_data_consistency.py` 通过
- `build_analysis_db.py` 通过
- `audit_execution_definition.py` 通过

执行定义审计结果：

- `PASS=12`
- `FAIL=0`

## 产出判断

本轮没有修改事实源，也没有扩展第二阶段需求；只是把 derived registry 层原本较松散的 `exported_at` 元数据统一收紧到同一个 export snapshot。这样 paper registry、assignment registry、PDF registry、asset registry 与 taxonomy registry 都更接近“可验证的同批次导出结果”，而不是各自独立漂移的派生文件。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 derived metadata、registry/build/check 三层对齐、以及剩余未显式化的执行语义逐轮推进。
