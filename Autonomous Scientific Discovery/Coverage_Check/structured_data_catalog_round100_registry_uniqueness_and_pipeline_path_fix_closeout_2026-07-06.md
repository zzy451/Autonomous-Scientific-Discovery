# Structured Data Catalog Round 100 Closeout

日期：2026-07-06

## 本轮目标

继续沿着 discipline current snapshot 这一条线做最小必要加固，把 `discipline_local_code_registry` 当前快照层自己的唯一性约束正式下沉到 SQLite，同时修复 Windows 中文路径下结构化管线对子脚本的调用稳定性问题。

## 本轮修改

修改：
- `scripts/build_analysis_db.py`
- `scripts/run_structured_data_pipeline.py`

### 1. `discipline_local_code_registry` 唯一性索引落地

在 `scripts/build_analysis_db.py` 中新增：

- `discipline_local_code_registry_assignment_id_unique`
  - 对 `discipline_local_code_registry(assignment_id)` 建唯一索引
- `discipline_local_code_registry_active_code_unique`
  - 对 `discipline_local_code_registry(discipline_local_code)` 建 partial unique index
  - 仅约束 `assignment_status = 'active_code'`

这一步把 current snapshot 层此前主要依赖语义检查维持的两条事实直接固化进 SQLite：

- 每条 registry 行只能对应一个唯一 `assignment_id`
- active snapshot 中的 `discipline_local_code` 不能重复

这和现有方案里“registry 是 current snapshot，但不能漂移为松散展示层”的执行方向一致，也和 ledger 侧已有的 active-code 唯一性形成对称约束。

### 2. build 自检扩展到 registry 索引存在性

扩展 `validate_discipline_sqlite_constraints()`：

- 读取 `discipline_code_assignments` 与 `discipline_local_code_registry` 两张 discipline 表的索引定义
- 显式检查上述两个 registry 索引真实存在于 `sqlite_master`
- 若索引缺失或 partial 条件异常，build 直接失败

这样这两条约束不只是在建库 SQL 中“写了”，而且在 build 自检阶段会被再次核验。

### 3. 修复中文路径下管线对子脚本的调用方式

在 `scripts/run_structured_data_pipeline.py` 中，把：

- 绝对子脚本路径调用

改为：

- 在项目根目录 `cwd=ROOT` 下使用相对路径 `scripts/<name>.py`

原因是当前项目位于中文目录 `C:\Users\20683\Desktop\综述\...` 下，Windows 环境中使用绝对脚本路径调用子脚本时会出现偶发的 `OSError: [Errno 22] Invalid argument`。本轮修复后，结构化总管线恢复稳定可复跑状态。

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

本轮还额外核对了当前 registry 快照与新增唯一性索引的兼容性：

- `discipline_local_code_registry` 总行数：447
- `distinct assignment_id`：447
- `active_code` 行数：423
- `distinct active discipline_local_code`：423
- `active_code` 且 `discipline_local_code IS NULL`：0

说明现有数据满足新索引，不需要回退或补脏数据修复。

## 产出判断

本轮把 discipline current snapshot 这一层从“有语义检查”继续推进到“有原生唯一性索引 + build 自检”，并顺手修复了中文路径下总管线的稳定性问题。当前结构化流水线仍保持：

- owner fact source 未被日常 export 覆盖
- preview / registry / CSV / SQLite 正常派生
- Section 12 执行定义审计继续全通过

## 后续状态

当前无新的代码级阻塞点；本轮完成后可继续沿 SQLite 约束、自检覆盖面和执行定义剩余细项逐轮推进。
