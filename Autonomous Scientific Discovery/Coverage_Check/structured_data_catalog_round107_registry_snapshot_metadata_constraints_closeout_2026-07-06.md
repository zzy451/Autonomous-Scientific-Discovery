# Structured Data Catalog Round 107 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 的 snapshot metadata 字段本身也正式压进 SQLite schema 和 build 自检，而不只依赖外层 checker。

对应方案要求：

- registry 是 derived snapshot
- 必须显式携带 `generated_at`
- 必须显式携带 `generated_by`
- 必须显式携带 `source_commit`
- 这些元数据应具有稳定、可审计的格式，而不是松散自由文本

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 registry snapshot metadata 字段格式

为 SQLite `discipline_local_code_registry` 表新增 / 收紧以下 `CHECK`：

- `generated_at` 必须匹配 ISO-like exported timestamp 起始格式：
  - `YYYY-MM-DDT...`

- `generated_by` 必须固定为：
  - `export_structured_data.py`

- `source_commit` 必须：
  - 非空
  - 长度为 `40`
  - 仅包含小写十六进制字符

这样 derived snapshot 的 provenance 字段也进入了结构化约束范围。

### 2. build 自检补充 registry snapshot metadata 查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 查询级自检：

- 空白或格式异常的 `generated_at`
- 非预期的 `generated_by`
- 空白或非法的 `source_commit`

任一出现即直接失败，防止 registry 快照在 provenance 字段上静默漂移。

### 3. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查这些 metadata 约束片段已经真实写入 `discipline_local_code_registry` 建表 SQL 中，而不是只依赖运行时查询。

## 验证

运行：

```bash
python "Autonomous Scientific Discovery/scripts/run_structured_data_pipeline.py" --with-execution-audit
```

结果：

- `export_structured_data.py` 通过
- `check_data_consistency.py` 通过
- `build_analysis_db.py` 通过
- `audit_execution_definition.py` 通过

执行定义审计结果：

- `PASS=12`
- `FAIL=0`

补充核对：

- 当前 `discipline_local_code_registry` 中：
  - 空白 / 非法 `generated_at` 数为 `0`
  - 非预期 `generated_by` 数为 `0`
  - 空白 / 非法 `source_commit` 数为 `0`

## 产出判断

本轮把 registry derived snapshot 的 provenance 元数据也推进成了 SQLite 内生约束，使 `discipline_local_code_registry` 不只是“有这些字段”，而是能对这些字段的格式与来源表达保持稳定。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
