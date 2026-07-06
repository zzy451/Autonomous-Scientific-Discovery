# Structured Data Catalog Round 114 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 对 `discipline_code_assignments` 的映射一致性也推进到 SQLite 内部自检层，而不只依赖外层 JSONL/CSV 比对或 checker。

对应方案要求：

- registry 是 discipline ledger 的 current snapshot 展示层
- registry 中镜像自 ledger 的字段必须稳定一致
- `assignment_id` 与 `paper_id` 的映射不能串行

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. build 自检补充 registry -> ledger 映射一致性查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 内部一致性检查：

- `discipline_local_code_registry.assignment_id` 对应的 `discipline_code_assignments.paper_id` 必须与 registry 的 `paper_id` 一致

也就是：

- 不允许 registry 把某个 assignment 挂到错误的 paper 上

### 2. build 自检补充 registry 镜像账本字段漂移检查

在同一查询中新增以下镜像字段的 SQLite 内部比对：

- `assignment_status`
- `discipline_local_code`
- `primary_taxonomy_code_2lvl`
- `assigned_at`
- `assigned_by`
- `retired_at`
- `redirected_to_code`
- `assignment_reason`
- `pending_reason`

如果 registry 当前快照中这些账本镜像字段与 `discipline_code_assignments` 对应行不一致，build 直接失败。

### 3. 从“覆盖闭环”推进到“映射与字段双闭环”

上一轮已经检查：

- active papers
- current assignments
- registry rows

这三层数量/覆盖关系是否闭环。

本轮继续推进为：

- 数量闭环
- `assignment_id -> paper_id` 映射闭环
- 镜像账本字段一致性闭环

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

- 当前 SQLite 中：
  - registry `assignment_id -> paper_id` 串行数为 `0`
  - registry 镜像账本字段漂移数为 `0`

## 产出判断

本轮把 registry 与 ledger 的关系从“有外键、数量对得上”进一步推进到“assignment 映射和镜像字段在 SQLite 内部也能自证一致”，让 current snapshot 的数据库内生一致性更强。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
