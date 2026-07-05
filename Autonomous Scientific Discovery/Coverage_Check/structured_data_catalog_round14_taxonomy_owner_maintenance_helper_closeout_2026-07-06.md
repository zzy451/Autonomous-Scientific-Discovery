# Structured Data Catalog Round 14 Closeout

日期：2026-07-06

## 本轮目标

补齐 taxonomy vocabulary owner 的正式维护入口，使 `Data/classification_code_index.json` 不再只依赖手工编辑，而是和 discipline ledger 一样有明确的 owner-maintenance helper。

## 本轮实现

### 1. 新增 taxonomy owner 维护脚本

新增：

- `scripts/manage_classification_code_index.py`

能力范围：

- `sync`
  - 从 `primary_terms` / `secondary_terms` 重建：
    - `primary_code_to_label`
    - `secondary_code_to_label`
    - `label_to_primary_code`
    - `label_to_secondary_code`
  - 规范 term 排序
  - 若当前 owner 文件已对齐，则不会无谓写盘
- `upsert-primary`
  - 显式新增或更新一级 taxonomy term
- `upsert-secondary`
  - 显式新增或更新二级 taxonomy term

这意味着 taxonomy vocabulary 的维护已经从“只能直接手工改 owner JSON”推进到“有专门 owner helper，且 helper 会自动同步 mapping dict”。

### 2. 写前校验

新脚本在写入前会执行：

- taxonomy payload 语义检查
  - 一级 / 二级 code 唯一
  - 一级 / 二级 label 唯一
  - `secondary_code` 与 `parent_primary_code` 必须匹配
  - 二级 term 的 parent 必须存在于 primary terms
- schema 校验
  - 复用 `classification_code_index.schema.json`

因此 taxonomy owner 的维护路径现在也带上了“helper 内部校验 + 全局 check 校验”双保险。

### 3. 文档同步

更新：

- `Data/README.md`
- `Data/field_dictionary.md`

同步内容：

- 明确 `scripts/manage_classification_code_index.py` 是 taxonomy owner 的正式维护入口
- 强调日常 export 仍然只能读取 `classification_code_index.json`，不能覆盖它

## 本轮验证

### 1. 帮助输出

执行：

```bash
python "Autonomous Scientific Discovery/scripts/manage_classification_code_index.py" --help
```

结果：

- 帮助输出正常
- 已暴露：
  - `sync`
  - `upsert-primary`
  - `upsert-secondary`

### 2. dry-run: sync

执行：

```bash
python "Autonomous Scientific Discovery/scripts/manage_classification_code_index.py" sync --updated-at 2026-07-06 --updated-by codex --dry-run
```

结果：

- 当前 owner 文件已对齐
- 输出 `No owner changes required for classification_code_index.json.`

### 3. dry-run: secondary term update

执行：

```bash
python "Autonomous Scientific Discovery/scripts/manage_classification_code_index.py" ^
  upsert-secondary ^
  --secondary-code 04.04 ^
  --review-status reviewed ^
  --updated-at 2026-07-06 ^
  --updated-by codex ^
  --dry-run
```

结果：

- 成功模拟一次二级 taxonomy term 的 owner 更新
- 未写盘，符合 dry-run 预期

### 4. 全链验证

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

当前主链状态：

- `papers.jsonl` records: 871
- `active confirmed-core`: 447
- `active local PDFs`: 422
- `active no-local-PDF`: 25
- `discipline_code_assignments` rows: 447
- `discipline_local_code_registry` rows: 447

## 本轮结论

本轮把 taxonomy vocabulary owner 从“已有 owner 文件、已有 schema、已有 checker，但缺少正式维护入口”的状态，推进到了“已有专门 owner helper，可显式 sync / upsert taxonomy terms，并自动同步 mapping dict”的状态。这样四类事实源里两个 `Data/` owner 文件现在都已经有明确的脚本化维护入口。
