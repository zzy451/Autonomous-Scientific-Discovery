# Structured Data Catalog Round 28 Closeout

日期：2026-07-06

## 本轮目标

补上 master owner 的专用维护入口，让论文与分类事实源 `Paper_Lists/agent_master_paper_list.md` 不再主要依赖手工改 markdown 表格。

## 本轮实现

### 1. 新增 master owner helper

新增：

- `scripts/manage_master_paper_list.py`

作用：

- 更新 `Paper_Lists/agent_master_paper_list.md` 中单篇论文的一行
- 只改显式传入的字段
- 同步计划或追加一条 `Data/change_log.jsonl`

### 2. 当前支持的更新方式

使用：

```bash
--paper-id ASD-xxxx
--set column=value
```

其中 `--set` 可重复，允许更新 master owner 中除 `ID` 之外的列，例如：

- `Paper title`
- `Authors`
- `Year`
- `Source`
- `DOI / arXiv / URL`
- `PDF path`
- `Is Agent`
- `Inclusion status`
- `Exclusion reason`
- `Main class`
- `Secondary class`
- `Tertiary class`
- `Fourth-level topic`
- `New fourth-level`
- `Agent type`
- `Research workflow role`
- `Validation type`
- `Scientific contribution type`
- `Evidence strength`
- `Citation priority`
- `Note path`
- `Remarks`

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
- 不写 master owner 文件
- 不写 `change_log.jsonl`

### 4. README 同步

更新：

- `Data/README.md`

补充说明：

- `manage_master_paper_list.py` 是 paper/classification owner 的维护入口
- 论文与分类事实变更应通过该脚本完成，而不是手工回写 derived outputs

## 本轮验证

执行 dry-run 预演：

```bash
python "Autonomous Scientific Discovery/scripts/manage_master_paper_list.py" --paper-id ASD-0001 --set "Citation priority=standard" --set "Main class=04" --reason "preview master owner helper" --dry-run
```

结果：

- 正确识别只需变更：
  - `Citation priority`
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

本轮把 master owner 也补成了有专用维护脚本的治理对象。至此，四类事实源相关的核心 owner 里，master、progress、discipline-code ledger、taxonomy owner 都已经有明确的 owner-maintenance 入口，不再主要依赖手工直接编辑。
