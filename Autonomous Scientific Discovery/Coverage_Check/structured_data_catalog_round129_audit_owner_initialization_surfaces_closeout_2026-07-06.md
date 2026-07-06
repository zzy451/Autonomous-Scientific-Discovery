# structured_data_catalog_round129_audit_owner_initialization_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把 owner initialization 这条线补成 execution audit 的正式证明项，重点落实方案里“taxonomy / discipline ledger 的初始化必须是显式命令，不能混入日常 export”的要求。

本轮不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 扩展 `scripts/audit_execution_definition.py`

新增 `Item 26`，把两条 owner initialization surface 纳入 execution audit：

- `scripts/init_discipline_code_assignments.py`
- `scripts/init_classification_code_index.py`

本项检查包含两层：

1. 静态面
   - 脚本存在
   - 各自保留 `--dry-run` / `--overwrite`
   - 脚本描述中明确“这是显式初始化，不是 daily export”
   - `Data/README.md` 继续把这两个脚本列为 owner-maintenance / initialization entry points

2. 运行面
   - execution audit 内部实际调用两条命令的 `--dry-run`
   - 验证 dry-run 成功返回
   - 验证输出中明确显示 preview / prepared summary
   - 验证 dry-run 不写 owner 文件

### 2. Windows 编码兼容兜底

由于当前环境下子进程 dry-run 输出可能混有非 UTF-8 控制台编码，本轮顺手把 execution audit 内部的子进程输出读取改成：

- `encoding="utf-8"`
- `errors="replace"`

并对 `stdout/stderr` 做空值兜底，避免 Windows 编码差异把 audit 本身打断。

这属于 execution audit 的运行稳定性修复，不改变长期方案语义。

### 3. 刷新 derived outputs

重新执行 canonical pipeline 后，刷新了：

- `Coverage_Check/structured_data_execution_definition_audit_latest.md`
- `Data/papers.jsonl`
- `Data/papers.csv`
- `Data/papers.sqlite`
- `Data/discipline_local_code_registry.jsonl`
- `Data/discipline_local_code_registry.csv`
- `Data/registry/*.jsonl`
- `Data/registry/taxonomy_registry.json`

本轮没有改动以下 owner fact source：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

## 验证

运行：

```powershell
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

结果：

- `export -> check -> build -> execution-audit` 全流程通过
- `check_data_consistency.py` 通过
- `audit_execution_definition.py` 输出：
  - `pass=26`
  - `fail=0`

本轮新增直接证明的是：

- discipline-code owner 初始化命令可 dry-run
- taxonomy owner 初始化命令可 dry-run
- 两条初始化链仍然保持“显式初始化，不是日常 export”的边界

## 结论

本轮把长期方案里“owner 初始化必须单独执行、不能混入 daily export”这条治理要求推进成了程序化可证明状态。现在 execution audit 不只证明 owner maintenance helper、change_log、guardrail、query surface，也开始直接证明 owner initialization command 自身可运行、可 preview、可隔离于日常导出流程。
