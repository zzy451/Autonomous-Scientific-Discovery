# Structured Data Catalog Round 89 Closeout

日期：2026-07-06

## 本轮目标

继续把 SQLite 从“能查”推进到“关系更完整”，把多张 analysis / registry 表正式连回 `papers(paper_id)`，而不只依赖脚本层 join 约定。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 新增 `paper_id -> papers(paper_id)` 外键

以下表现在都显式声明了到 `papers(paper_id)` 的外键：

- `paper_modules`
- `workflow_mirror_paper_modules`
- `paper_general_method_buckets`
- `pdf_evidence_status`
- `paper_assets`
- `notes`
- `pdf_inventory`
- `missing_pdf_inventory`
- `note_inventory`

这让 canonical module rows、workflow mirror rows、general-method bucket rows、PDF/source evidence rows、asset rows、notes rows 和 inventory rows 都在数据库层具备显式 paper 级关系约束。

### 2. build 自检扩展

新增 `validate_core_analysis_foreign_keys()`：

- 对上面 9 张表逐一执行 `PRAGMA foreign_key_list(...)`
- 检查是否都存在：
  - `paper_id -> papers(paper_id)`

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

以下表的 `PRAGMA foreign_key_list(...)` 结果均包含：

```text
papers.paper_id <- <table>.paper_id
```

表名单：

- `paper_modules`
- `workflow_mirror_paper_modules`
- `paper_general_method_buckets`
- `pdf_evidence_status`
- `paper_assets`
- `notes`
- `pdf_inventory`
- `missing_pdf_inventory`
- `note_inventory`

## 产出判断

本轮进一步把 analysis / registry 层与 `papers` 主表之间的数据库关系硬化下来，使更多“按 paper 组织的一对多或一对一派生表”具备显式外键，而不再只靠脚本假设关系成立。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
