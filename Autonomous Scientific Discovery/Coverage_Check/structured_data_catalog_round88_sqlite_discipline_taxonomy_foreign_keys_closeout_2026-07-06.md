# Structured Data Catalog Round 88 Closeout

日期：2026-07-06

## 本轮目标

继续把 discipline 相关结构与 taxonomy vocabulary 的关系推进到 SQLite 层，不只是 discipline 表彼此相连，还要让主排架一级模块字段在数据库中受 `taxonomy_index` 约束。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 新增 taxonomy 外键

在 SQLite schema 中新增：

1. `discipline_code_assignments`
   - `source_primary_module_for_filing REFERENCES taxonomy_index(code)`

2. `discipline_local_code_registry`
   - `primary_module_for_filing REFERENCES taxonomy_index(code)`

这样 discipline ledger / registry 中的一 级主排架模块字段不再只是裸字符串，而是在数据库层明确受 taxonomy index 约束。

### 2. blank-to-null 兼容

由于 `discipline_local_code_registry.jsonl` 中的 general-method 行当前 `primary_module_for_filing` 可能是空字符串，SQLite 插入阶段继续使用 `blank_to_none()` 做规范化，确保空值在外键语义下按 `NULL` 处理，而不是写入非法空字符串。

### 3. build 自检扩展

扩展 `validate_discipline_sqlite_constraints()`：

- 检查 `discipline_code_assignments` 是否存在：
  - `source_primary_module_for_filing -> taxonomy_index(code)` 外键

- 检查 `discipline_local_code_registry` 是否存在：
  - `primary_module_for_filing -> taxonomy_index(code)` 外键

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
discipline_code_assignments foreign keys:
  source_primary_module_for_filing -> taxonomy_index(code)
  paper_id -> papers(paper_id)

discipline_local_code_registry foreign keys:
  primary_module_for_filing -> taxonomy_index(code)
  assignment_id -> discipline_code_assignments(assignment_id)
  paper_id -> papers(paper_id)
```

## 产出判断

本轮把 discipline 结构与 taxonomy index 的一级模块关系也推进到了 SQLite 实体层。现在：

- ledger 与 papers 相连
- registry 与 papers / ledger 相连
- ledger / registry 的主排架模块字段也与 taxonomy index 相连

这让数据库层的结构关系更接近长期方案中“taxonomy vocabulary owner -> registry / SQLite derived layer”的映射要求。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
