# Structured Data Catalog Round 103 Closeout

日期：2026-07-06

## 本轮目标

继续加固 derived snapshot metadata 的真实性校验。此前 `discipline_local_code_registry.jsonl` 已经检查：

- `source_commit` 全表统一
- `source_commit` 格式是 40 位十六进制 hash

但还没有进一步核对它是否真的等于当前仓库 `HEAD`。本轮把这条真实性约束前移到 `check_data_consistency.py`。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 新增当前仓库 `HEAD` 读取辅助函数

新增：

- `get_git_head_commit()`

作用：

- 在项目根目录执行 `git rev-parse HEAD`
- 读取当前仓库真实的 commit id

如果环境异常导致无法读取，则回退为空字符串，不会引入与事实源无关的额外写入。

### 2. `discipline_local_code_registry` 的 `source_commit` 真实性校验

在 `validate_discipline_local_code_registry()` 中新增：

- 当当前仓库 `HEAD` 可读取时，`discipline_local_code_registry.source_commit` 必须与之完全一致

这让 registry snapshot metadata 从：

- “字段格式合法”

进一步提升为：

- “字段值真实对应当前导出时的 git commit 基线”

也更符合方案里对 derived snapshot metadata 的要求：

- `source_commit`
- `generated_at`
- `generated_by`
- `worktree_dirty`

不能只是表面存在，而要具备可核验性。

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

本轮没有扩需求，也没有修改 owner fact source；只是把 registry derived snapshot metadata 的一条“真实性”校验正式落到 check 阶段。这样 `source_commit` 不再只是长得像 commit，而是必须能回连到当前仓库状态。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 derived metadata、一致性前移校验、SQLite/CSV/JSONL 三层对齐这些剩余细项逐轮推进。
