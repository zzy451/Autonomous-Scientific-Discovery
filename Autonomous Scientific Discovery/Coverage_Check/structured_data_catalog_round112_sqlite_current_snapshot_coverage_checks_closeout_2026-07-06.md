# Structured Data Catalog Round 112 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 discipline current snapshot 在 SQLite 内部的覆盖关系也纳入 build 自检，而不只依赖 JSONL 与 checker 侧的外部一致性判断。

对应方案要求：

- `discipline_code_assignments` 的 current snapshot 应完整覆盖 active confirmed-core 论文
- `discipline_local_code_registry` 应与 current snapshot 一一对应
- active papers、current ledger rows、registry rows 这三层关系必须形成闭环

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. build 自检补充 SQLite current-snapshot 覆盖查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 内部覆盖关系检查：

- active confirmed-core 论文数
- current discipline assignment 数
  - `assignment_status IN ('active_code', 'pending_secondary', 'non_discipline_general_method')`
- `discipline_local_code_registry` 行数

并显式检查以下违规计数必须为 `0`：

- active paper 缺 current assignment
- current assignment 指向 non-active paper
- current assignment 缺 registry row
- registry row 指向 non-current 或缺失 assignment

### 2. 从“导出镜像一致”推进到“SQLite 内部闭环一致”

本轮没有新增 schema 字段，但把当前 discipline 快照三层关系从：

- “JSONL / CSV / SQLite 导出一致”

推进到：

- “SQLite 内部自身也能证明 active papers / current assignments / registry rows 三者是闭环一致的”

这让 build 对 current snapshot 的验证更接近真正的数据库一致性检查，而不只是外部文件比对。

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
  - active confirmed-core 论文数：`447`
  - current discipline assignment 数：`447`
  - registry row 数：`447`
  - active paper 缺 current assignment：`0`
  - current assignment 指向 non-active paper：`0`
  - current assignment 缺 registry row：`0`
  - registry row 指向 non-current / 缺失 assignment：`0`

## 产出判断

本轮把 discipline current snapshot 从“导出文件互相一致”进一步推进到“SQLite 内部可自证覆盖闭环一致”，这对后续继续增强 current snapshot / ledger / papers 三层关系很有价值。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
