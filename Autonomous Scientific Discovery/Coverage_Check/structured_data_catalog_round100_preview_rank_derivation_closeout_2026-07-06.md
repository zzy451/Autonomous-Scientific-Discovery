# Structured Data Catalog Round 100 Closeout

日期：2026-07-06

## 本轮目标

按已冻结方案继续推进 preview 阶段实现，只处理 `export_structured_data.py` 的最小必要收口，确认：

- preview 继续只读 `master`、`progress`、`Data/classification_code_index.json`
- `pending_secondary` 不生成假 code
- `non_discipline_general_method` 不生成普通 `MM-SS-NNN` code
- `discipline_local_rank` 严格作为派生字段，不独立维护

## 本轮修改

修改：

- `scripts/export_structured_data.py`

### 1. 收紧 preview 中的 `discipline_local_rank` 生成方式

对 `build_discipline_initial_assignment_preview()` 的 active proposal 分支做了最小修改：

- 先生成 `proposed_discipline_local_code`
- 再通过 `parse_discipline_local_rank(proposed_code)` 派生 `discipline_local_rank`

这样 preview 阶段的 rank 也不再以独立计数值写入，而是显式从 proposed code 解析得到，和长期方案中“`discipline_local_rank` 只能从 code 派生”的规则保持一致。

### 2. 脚本现状核对

本轮同步核对了三支脚本当前结构：

- `scripts/export_structured_data.py`
- `scripts/check_data_consistency.py`
- `scripts/build_analysis_db.py`

结论：

- preview 逻辑已经按当前方案落在 `export_structured_data.py`
- `check_data_consistency.py` 已覆盖 preview 的关键语义校验
- `build_analysis_db.py` 本轮不需要为 preview 阶段再做额外改动

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

关键产出：

- `discipline_code_initial_assignment_preview.csv` 成功导出
- 导出 preview 行数：447
- 执行定义审计结果：`PASS=12`，`FAIL=0`

## 产出判断

本轮没有扩展第二阶段 owner 账本逻辑，也没有让日常 export 覆盖 `classification_code_index.json` 或 `discipline_code_assignments.jsonl`。修改只聚焦在 preview 生成的派生语义收紧，并确认当前 preview 流程已经可以稳定跑通。

## 后续状态

当前 preview 阶段无新增代码阻塞；下一步可以继续在既有治理边界内推进后续实现。
