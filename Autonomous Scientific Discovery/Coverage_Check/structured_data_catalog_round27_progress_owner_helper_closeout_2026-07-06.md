# Structured Data Catalog Round 27 Closeout

日期：2026-07-06

## 本轮目标

补上 progress owner 的专用维护入口，让 PDF/source/evidence workflow 状态更新不再只能靠手工改 markdown 表格或事后手补 `change_log`。

## 本轮实现

### 1. 新增 progress owner helper

新增：

- `scripts/manage_progress_tracking.py`

作用：

- 更新 `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md` 中单篇论文的一行
- 只改显式传入的字段
- 同步计划或追加一条 `Data/change_log.jsonl`

### 2. 当前支持的更新方式

使用：

```bash
--paper-id ASD-xxxx
--set column=value
```

其中 `--set` 可重复，允许更新 progress owner 中除 `paper_id` 之外的列，例如：

- `title`
- `note_path`
- `pdf_status`
- `pdf_path`
- `evidence_status`
- `note_status`
- `master_status`
- `final_modules_or_bucket`
- `source_limited`
- `batch`
- `closed`

### 3. 审计行为

helper 默认准备一条 `change_log` row，记录：

- `paper_id`
- `change_type`
- `old_value`
- `new_value`
- `reason`
- `related_commit`

支持：

- `--reason`
- `--changed-at`
- `--changed-by`
- `--related-commit`
- `--change-type`

`--dry-run` 时：

- 只显示变更字段
- 只显示计划写入的 `change_log` row
- 不写 progress owner 文件
- 不写 `change_log.jsonl`

### 4. README 同步

更新：

- `Data/README.md`

补充说明：

- `manage_progress_tracking.py` 是 progress owner 的维护入口
- PDF/source/evidence workflow 状态更新应通过该脚本完成，而不是手工回写 derived registry

## 本轮验证

执行 dry-run 预演：

```bash
python "Autonomous Scientific Discovery/scripts/manage_progress_tracking.py" --paper-id ASD-0001 --set source_limited=yes --set pdf_status=archived_pdf --reason "preview progress owner helper" --dry-run
```

结果：

- 正确识别只需变更：
  - `source_limited`
- 正确输出 old/new 值
- 正确预演一条 `change_log` row
- `Dry run only; no files written.`

随后执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- export 成功
- check 成功
- build 成功

## 本轮结论

本轮把 progress owner 从“只能人工编辑的 markdown 表”推进成了“有专用 owner-maintenance helper 的治理对象”。这条链正对应长期方案里优先要求记录审计的 PDF/source 状态变更，也能减少以后手工改 progress 表时漏记 `change_log` 的风险。
