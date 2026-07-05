# Structured Data Catalog Round 26 Closeout

日期：2026-07-06

## 本轮目标

补 taxonomy vocabulary owner 维护流程里的审计闭环缺口：此前 `manage_classification_code_index.py` 可以直接改 `Data/classification_code_index.json`，但不会为受影响论文留下 `change_log` 审计痕迹。

## 本轮实现

### 1. 增强 taxonomy owner helper

更新：

- `scripts/manage_classification_code_index.py`

新增能力：

- `--append-change-log`
- `--change-reason`
- `--changed-by`
- `--related-commit`
- `--paper-id`（repeatable）

### 2. 二级 taxonomy term 变更可自动推导受影响论文

对于 `upsert-secondary`：

- 如果没有显式传 `--paper-id`
- helper 会自动从 master 中查找：
  - `Secondary class == 当前 secondary_code`

并生成 impacted paper list。

这让 taxonomy owner 改动不再只停留在 term 文件级别，而能回连到当前受影响的论文记录。

### 3. 支持按 paper 追加 `change_log`

当使用：

```bash
--append-change-log
```

时，helper 会为每个 impacted paper 计划或追加一条：

- `change_type = taxonomy_owner_<action>`
- `old_value.term_before`
- `new_value.term_after`
- `reason`
- `related_commit`

当前设计：

- `upsert-secondary`
  - 可自动推导 impacted paper list
- `sync` / `upsert-primary`
  - 若要写 `change_log`，需要显式提供 `--paper-id`

这样能避免把过宽的一级 term 变化盲目扩散成不可控审计噪音。

### 4. README 同步

更新：

- `Data/README.md`

补充说明：

- `manage_classification_code_index.py` 现在可以为受影响论文追加 audit rows
- taxonomy owner 变更对 derived paper-level provenance 的影响可以进入 `Data/change_log.jsonl`

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/manage_classification_code_index.py" upsert-secondary --secondary-code 04.04 --review-status reviewed --dry-run --append-change-log --change-reason "preview taxonomy owner audit integration"
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- taxonomy helper dry-run 成功
- export 成功
- check 成功
- build 成功

dry-run 关键输出：

- `Action: update_secondary 04.04`
- `Impacted paper_ids: 113`
- `Planned change_log rows: 113`
- `Dry run only; no files written.`

这说明：

- impacted paper 推导已经接通
- change_log row 生成逻辑已经接通
- dry-run 不会污染 owner 文件或 change_log

## 本轮结论

本轮把 taxonomy owner maintenance 从“能改 owner 文件”推进到了“能预览并记录受影响论文审计链”的状态。这样后续二级 taxonomy 的 review/status/source 变化，不再只能靠 git diff 看 term 文件本身，而可以有 paper-level audit trail 对齐长期方案里的治理要求。
