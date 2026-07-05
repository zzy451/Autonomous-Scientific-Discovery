# Structured Data Catalog Round 87 Closeout

日期：2026-07-06

## 本轮目标

继续把 discipline 相关结构从“有表、有约束”推进到“有关系”，把 SQLite 中的 discipline ledger / registry 与 `papers`、assignment ledger 的外键关系真实落地。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 新增外键关系

在 SQLite schema 中新增：

1. `discipline_code_assignments`
   - `paper_id REFERENCES papers(paper_id)`

2. `discipline_local_code_registry`
   - `paper_id REFERENCES papers(paper_id)`
   - `assignment_id REFERENCES discipline_code_assignments(assignment_id)`

这让 discipline ledger / registry 不再只是“字段上看起来能 join”，而是在 SQLite 层显式声明了和主表、账本表的关系。

### 2. build 自检扩展

扩展 `validate_discipline_sqlite_constraints()`：

- 通过 `PRAGMA foreign_key_list(discipline_code_assignments)` 检查：
  - 是否存在到 `papers(paper_id)` 的外键

- 通过 `PRAGMA foreign_key_list(discipline_local_code_registry)` 检查：
  - 是否存在到 `papers(paper_id)` 的外键
  - 是否存在到 `discipline_code_assignments(assignment_id)` 的外键

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

额外 SQLite 证据：

```text
discipline_code_assignments fks:
  papers.paper_id <- discipline_code_assignments.paper_id

discipline_local_code_registry fks:
  discipline_code_assignments.assignment_id <- discipline_local_code_registry.assignment_id
  papers.paper_id <- discipline_local_code_registry.paper_id
```

## 产出判断

本轮进一步把 discipline 相关关系落进了 SQLite 实体层，使：

- ledger 与 `papers`
- registry 与 `papers`
- registry 与 ledger

都具备显式数据库关系约束。这比单纯依赖脚本 join 或 review 约定更接近长期方案里“数据库管查询、关系稳定可追踪”的要求。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
