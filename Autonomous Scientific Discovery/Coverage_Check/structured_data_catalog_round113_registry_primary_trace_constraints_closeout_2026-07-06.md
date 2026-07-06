# Structured Data Catalog Round 113 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 中与 `primary_filing_policy` 直接对应的 primary-trace 三元关系正式压进 SQLite schema 和 build 自检。

对应方案要求：

- active current row 应显式保留可解释的 `primary_module_confidence`
- active current row 应显式保留可解释的 `primary_module_assignment_rule`
- `manual_override` 必须有 `primary_module_override_reason`
- 非 `manual_override` 不应残留 override reason
- pure general-method current row 不应携带 primary filing trace

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 active current row 的 primary trace 语义

为 SQLite `discipline_local_code_registry` 新增：

- `assignment_status = 'active_code'` 时：
  - `primary_module_confidence` 必须非空
  - `primary_module_assignment_rule` 必须非空

这让 current snapshot 的 active row 必须携带完整 primary-filing trace。

### 2. 收紧 manual-override / override-reason 关系

新增：

- `primary_module_assignment_rule = 'manual_override'` 时：
  - `primary_module_override_reason` 必须非空

- `primary_module_assignment_rule <> 'manual_override'` 时：
  - `primary_module_override_reason` 必须为空

这把 override reason 的使用边界正式锁死，避免 reason 漂移成泛用文本槽位。

### 3. 收紧 pure general-method row 的 primary-trace 语义

在已有 general-method current row 约束上继续加严：

- `assignment_status = 'non_discipline_general_method'` 时：
  - `primary_module_confidence` 必须为空
  - `primary_module_assignment_rule` 必须为空
  - `primary_module_override_reason` 必须为空

这样 pure general-method row 在 current snapshot 中就不会残留 formal filing trace。

### 4. build 自检补充 primary-trace 查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 查询级自检：

- active row 缺失 `primary_module_confidence / primary_module_assignment_rule`
- `manual_override` 缺失 override reason
- 非 `manual_override` 错误携带 override reason
- general-method row 错误携带 primary trace

任一出现即直接中止 build。

### 5. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查上述 primary-trace 约束片段已经真实写入 `discipline_local_code_registry` 建表 SQL 中，而不是只依赖运行时查询。

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
  - active row 缺 primary trace 数为 `0`
  - `manual_override` 缺 override reason 数为 `0`
  - 非 `manual_override` 错误携带 override reason 数为 `0`
  - general-method row 错误携带 primary trace 数为 `0`

## 产出判断

本轮把 registry current snapshot 中最关键的 primary-filing trace 字段从“存在即可”推进成了“必须按 policy 成组一致出现”，这让 current snapshot 对后续写作与人工审查更可靠。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
