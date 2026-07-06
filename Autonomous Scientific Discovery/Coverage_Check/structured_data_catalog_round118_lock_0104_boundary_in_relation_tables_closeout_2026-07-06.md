# Structured Data Catalog Round 118 Closeout

日期：2026-07-06

## 本轮目标

继续把 `01.04` general-method bucket 的边界从“导出逻辑事实上这样做”推进到“SQLite 关系表原生写死”。本轮聚焦两张关系表：

- `paper_modules`
- `workflow_mirror_paper_modules`

这和长期方案中“`01.04` 只能在 general-method lane，不进入 formal scientific_object_modules”的规则直接对应。

## 本轮修改

修改：
- `scripts/build_analysis_db.py`

### 1. `paper_modules` 原生拒绝 `01.04`

本轮为 `paper_modules` 新增：

- `CHECK (module_code <> '01.04')`

这把 canonical formal-module 关系表里禁止混入 general bucket 的边界正式写进了 SQLite。

此前虽然：

- `paper_modules` 行集已经由导出逻辑保证来自 `scientific_object_modules`
- build 也会检查 `paper_modules` 不应含 general_bucket rows

但现在更进一步，SQLite 本身也会拒绝 `01.04` 进入 canonical modules 关系表。

### 2. `workflow_mirror_paper_modules` 锁定 `module_code` 与 `module_kind` 配对关系

本轮新增：

- `(module_code = '01.04' AND module_kind = 'general_bucket') OR (module_code <> '01.04' AND module_kind = 'formal_module')`

这样 workflow mirror 表中的 bucket/formal module 分流不再只依赖导出逻辑，而是数据库结构层也会强制：

- 只有 `01.04` 才能是 `general_bucket`
- 其他 code 都必须是 `formal_module`

### 3. build 自检同步覆盖

`validate_relation_table_constraints()` 已同步检查：

- `paper_modules` 中的 `module_code <> '01.04'`
- `workflow_mirror_paper_modules` 中 `module_code` 与 `module_kind` 的配对约束

因此这轮依然是：

- 建表
- build 自检

两层一起收口。

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

本轮把 `01.04` 的 formal/general-method 边界进一步从“脚本层正确”推进成“关系表结构层也正确”。这和长期方案里：

- `01.04` 只属于 `general_method_bucket`
- 不进入 formal scientific_object_modules

的硬边界完全一致。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite guardrails、少量尚未显式量化的 derived metadata / mirror 语义，以及长期方案与当前执行定义之间剩余的小闭环项逐轮推进。
