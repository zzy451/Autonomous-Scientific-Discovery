# Structured Data Catalog Round 116 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 对 `papers` 的关键镜像字段一致性也推进到 SQLite 内部自检层，而不只依赖外层 JSONL/CSV 比对或 checker。

对应方案要求：

- registry 是 current snapshot 展示层
- 其中来自 `papers` 的冗余展示字段必须稳定镜像当前 `papers` 表
- 不能出现 registry snapshot 与当前 `papers` 事实层在关键字段上漂移的情况

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. build 自检补充 registry -> papers 映射一致性查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 内部查询，直接比较 registry 当前快照与 `papers` 表中的以下字段：

- `primary_module_for_filing`
- `primary_module_confidence`
- `primary_module_assignment_rule`
- `primary_module_override_reason`
- `legacy_secondary_class`
- `secondary_class_source`
- `secondary_class_confidence`
- `secondary_class_review_status`
- `general_method_bucket`
- `title`
- `note_path`
- `pdf_path`
- `active_confirmed_core`

如果 registry 中这些镜像字段和 `papers` 表当前值不一致，build 直接失败。

### 2. 从“registry 对 ledger 一致”推进到“registry 同时对 ledger 与 papers 一致”

上一轮已经补了：

- registry -> ledger 的 assignment 映射与镜像字段一致性

本轮继续推进为：

- registry -> ledger 一致
- registry -> papers 一致

这样 current snapshot 现在不只对账本自证一致，也对 paper facts 自证一致。

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
  - registry -> papers 关键镜像字段漂移数为 `0`

## 产出判断

本轮把 registry current snapshot 的内部一致性从“对 ledger 自证”进一步推进到“同时对 ledger 和 papers 双侧自证”，使 SQLite 内部的 current snapshot 关系更接近真正的 derived presentation layer 闭环。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
