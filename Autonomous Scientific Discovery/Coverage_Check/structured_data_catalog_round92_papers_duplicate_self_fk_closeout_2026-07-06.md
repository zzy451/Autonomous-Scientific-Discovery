# Structured Data Catalog Round 92 Closeout

日期：2026-07-06

## 本轮目标

继续把 `papers` 主表内部的结构关系正式落到 SQLite 层，让已结构化的 duplicate linkage 不再只是普通字符串字段。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 新增 `papers.duplicate_of` 自引用外键

新增：

- `duplicate_of REFERENCES papers(paper_id) DEFERRABLE INITIALLY DEFERRED`

这让：

- `papers.record_status = duplicate`
- `papers.duplicate_of = ASD-xxxx`

不再只是“看起来像指向另一篇论文”，而是在数据库层正式绑定到 `papers.paper_id`。

之所以使用 `DEFERRABLE INITIALLY DEFERRED`，是因为 duplicate paper 可能在批量插入过程中引用后面才写入的 paper row；延迟到事务提交时检查，更符合当前 bulk build 方式。

### 2. blank-to-null 规范化

在 `papers` 的 SQLite 期望行和插入行中，对 `duplicate_of` 使用 `blank_to_none()`，避免空字符串误触外键失败。

### 3. build 自检扩展

扩展 `validate_core_analysis_foreign_keys()`：

- 检查 `papers` 是否存在：
  - `duplicate_of -> papers(paper_id)` 自引用外键

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

`PRAGMA foreign_key_list(papers)` 当前包含：

```text
duplicate_of -> papers(paper_id)
primary_module_for_filing -> taxonomy_index(code)
```

当前 `duplicate_of` 非空记录数为 `31`，全部与现有 `ASD-xxxx` paper IDs 兼容。

## 产出判断

本轮把 `papers` 主表里最明确的内部关系字段之一正式推进为数据库约束，让 duplicate linkage 从“派生字段”进一步升级为“关系字段”。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
