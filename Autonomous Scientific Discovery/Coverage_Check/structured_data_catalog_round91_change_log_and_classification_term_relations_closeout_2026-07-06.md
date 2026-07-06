# Structured Data Catalog Round 91 Closeout

日期：2026-07-06

## 本轮目标

继续沿 SQLite 实体层推进 owner / taxonomy / paper 关系，把 change log 与 taxonomy term 的关系也尽量正式落地，而不只停留在脚本约定层。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `change_log` 外键

新增：

- `change_log.paper_id REFERENCES papers(paper_id)`

这样 `Data/change_log.jsonl` 导入 SQLite 后，不再只是“看起来像某篇论文的审计记录”，而是在数据库层明确绑定到真实 paper 记录。

### 2. `classification_terms` 关系与约束

新增：

- `classification_terms.parent_primary_code REFERENCES taxonomy_index(code)`

新增 `CHECK`：

- `term_level IN ('primary', 'secondary')`
- `primary` term 必须 `parent_primary_code IS NULL`
- `secondary` term 必须 `parent_primary_code IS NOT NULL`

这让 taxonomy owner 的 term-level 语义在数据库层也更清晰。

### 3. build 自检扩展

扩展 `validate_reference_owner_foreign_keys()`，新增检查：

- `change_log.paper_id -> papers(paper_id)`
- `classification_terms.parent_primary_code -> taxonomy_index(code)`
- `classification_terms` 的 `term_level` CHECK 约束存在

## 失败尝试与回退

本轮曾尝试把：

- `classification_terms.taxonomy_code -> taxonomy_index(code)`

也做成外键，但当前 `classification_terms` 同时承载 primary 与 secondary terms，而 `taxonomy_index` 只覆盖一级模块与 `01.04`，不覆盖所有 secondary code，因此这条外键在当前方案落地阶段并不语义等价。已明确回退，避免引入错误约束。

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
change_log:
  paper_id -> papers(paper_id)

classification_terms:
  parent_primary_code -> taxonomy_index(code)
  CHECK(term_level primary/secondary semantics)
```

## 产出判断

本轮把：

- owner 审计链中的 `change_log`
- taxonomy vocabulary 中的 `classification_terms`

都进一步接入了数据库关系层，使 structured data 底座更接近长期方案里“owner facts -> derived layer -> SQLite analysis layer”之间的正式映射。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
