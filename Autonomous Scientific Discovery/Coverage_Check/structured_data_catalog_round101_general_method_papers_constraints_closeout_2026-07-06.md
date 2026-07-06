# Structured Data Catalog Round 101 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 pure `01.04` general-method-only 论文的核心语义从“当前数据恰好满足”推进到“SQLite `papers` 表显式强制满足”。

对应的方案约束是：

- `01.04` 只能进入 `general_method_bucket`
- pure general-method-only 记录不进入 formal `scientific_object_modules`
- pure general-method-only 记录不强行分配 `primary_module_for_filing`

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `papers` 表新增 pure general-method cross-field `CHECK`

把以下联动语义正式写入 SQLite：

1. 如果 `general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'`
   则必须同时满足：
   - `scientific_object_modules_json = '[]'`
   - `object_coverage_mode = 'general_method_without_concrete_object_experiments'`
   - `primary_module_for_filing IS NULL`

2. 如果 `object_coverage_mode = 'general_method_without_concrete_object_experiments'`
   则必须同时满足：
   - `general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'`
   - `scientific_object_modules_json = '[]'`
   - `primary_module_for_filing IS NULL`

这样 `papers` 表本身就能拒绝把 pure general-method 记录错误地混进 formal scientific-object lane。

### 2. build 自检补充 general-method 语义检查

在 `validate_papers_outputs()` 中新增 SQLite 查询级自检：

- build 完成后显式统计是否存在违反上述联动语义的 `papers` 行
- 若存在则直接报错中止

### 3. `papers` 表约束文本校验收紧

`validate_papers_sqlite_constraints()` 现在会先对 `sqlite_master` 里的建表 SQL 做空白归一化，再检查关键约束片段，避免因为换行或空格格式差异导致误判。

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

- 当前 `papers.sqlite` 中 `general_method_bucket = 01.04...` 的记录数为 `169`
- 违反本轮新增联动语义的记录数为 `0`

## 产出判断

本轮把 pure general-method-only 的数据库层边界进一步锁死，使方案里的 `01.04` 特殊 bucket 规则不再只依赖 export 习惯或人工理解，而是被 `papers` 表约束和 build 自检共同强制执行。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
