# Structured Data Catalog Round 110 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 作为“当前 active snapshot”应有的最外层范围边界进一步压进 SQLite schema 和 build 自检。

对应方案要求：

- `discipline_local_code_registry` 是 current snapshot
- current snapshot 只服务 active confirmed-core 论文
- current snapshot 中的 note/path 冗余展示字段应保持可用，不能退化成空壳记录

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 registry 的 active-snapshot 范围边界

为 SQLite `discipline_local_code_registry` 表新增 / 收紧以下约束：

- `active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core = 1)`

这让 registry 在 schema 层明确只承载 active confirmed-core 当前快照，而不是泛化成混合状态表。

### 2. 收紧 registry 的 `note_path` 语义

为 `discipline_local_code_registry` 新增：

- `note_path TEXT NOT NULL CHECK (trim(note_path) <> '')`

这样 derived current snapshot 至少要保留可用的 note 导航入口，不再允许出现空白 note-path 快照行。

### 3. build 自检补充 current-snapshot scope 查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 查询级自检：

- `active_confirmed_core <> 1`
- `note_path` 为空或纯空白

任一出现即直接中止 build。

### 4. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查上述 registry scope 约束片段已经真实写入 SQLite 建表 SQL 中，而不是只依赖运行时查询。

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
  - `active_confirmed_core <> 1` 的行数为 `0`
  - 空白 `note_path` 的行数为 `0`

## 产出判断

本轮把 registry 作为“active current snapshot”的最外层范围边界进一步锁死，使它更符合方案中“当前展示快照”而不是“泛化 registry 容器”的定位。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
