# Structured Data Catalog Round 35 Closeout

日期：2026-07-06

## 本轮目标

把长期方案里“日常 export / build 不得覆盖 owner fact source”的要求进一步做成运行时 guardrail，而不是只靠约定或 code review 记忆来保证。

## 本轮实现

更新：

- `scripts/export_structured_data.py`
- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 为 `export_structured_data.py` 增加 owner-path guardrail

当前在真正写文件前，会显式检查 export 目标路径集合是否与以下 owner fact source 冲突：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/classification_code_index.json`
- `Data/discipline_code_assignments.jsonl`
- `Data/change_log.jsonl`

若未来脚本被改坏，试图把输出写到这些路径上，会直接抛错并终止，而不是静默覆盖。

### 2. 为 `build_analysis_db.py` 增加 owner-path guardrail

当前在真正写 CSV / SQLite 之前，也会显式检查 build 目标路径集合，避免误写：

- `Data/classification_code_index.json`
- `Data/discipline_code_assignments.jsonl`
- `Data/change_log.jsonl`

### 3. README 同步

更新：

- `Data/README.md`

补充说明：

- `export_structured_data.py` 与 `build_analysis_db.py` 现在都带有 runtime owner-path guardrail
- 若未来有人误改脚本让它们输出到 owner fact source，命令会直接失败

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- export 成功
- check 成功
- build 成功

这说明：

- 当前 guardrail 不会误伤现有合法输出路径
- 现有 derived rebuild 流程保持正常

## 本轮结论

本轮把“不要覆盖 owner 文件”从文档纪律推进成了脚本级防线。这样即使以后维护时有人误改输出目标，export/build 也会先把问题拦下来，而不是等 owner 文件被污染后再靠 checker 或 git diff 追查。
