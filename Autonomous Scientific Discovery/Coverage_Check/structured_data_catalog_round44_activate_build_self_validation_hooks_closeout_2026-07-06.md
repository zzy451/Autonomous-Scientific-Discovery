# Structured Data Catalog Round 44 Closeout

日期：2026-07-06

## 本轮目标

把前几轮已经写进 `build_analysis_db.py` 的 self-validation helper 真正接入 `main()` 构建流程，并补齐 auxiliary analysis tables 的 build-time SQLite fidelity checks，避免“函数写了但构建时其实没执行”的半落实状态。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 激活已有 build self-validation hooks

本轮把以下校验实际接入 `main()`，在 `build_sqlite(...)` 之后立即执行：

- `validate_module_csv_outputs(...)`
- `validate_sqlite_module_surfaces(...)`
- `validate_discipline_local_code_registry_outputs(...)`

这意味着前几轮为 module surfaces 和 discipline registry 写下的自校验，现在不再只是 helper，而是 build 流程的真实 gate。

### 2. 新增 auxiliary analysis tables 的 SQLite fidelity checks

新增：

- `validate_auxiliary_analysis_tables(...)`

当前 build 完成后，会主动校验以下 SQLite tables 是否忠实反映其当前 derived source rows：

- `paper_general_method_buckets`
- `pdf_evidence_status`
- `paper_assets`
- `notes`

对齐来源分别是：

- `paper_general_method_buckets` <- `build_general_method_bucket_rows(papers)`
- `pdf_evidence_status` <- `pdf_archive_registry.jsonl`
- `paper_assets` <- `asset_manifest.jsonl`
- `notes` <- `note_manifest.json`

### 3. README 同步

在 `Data/README.md` 里补充说明：

- `build_analysis_db.py` 现在会真正自检 module split
- 会自检 `discipline_local_code_registry` CSV/SQLite
- 也会自检：
  - `paper_general_method_buckets`
  - `pdf_evidence_status`
  - `paper_assets`
  - `notes`

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- `export` 成功
- `check` 成功
- `build` 成功

这说明本轮真正被调用的 build self-validation hooks 在当前数据集上全部通过，没有打破既有导出语义。

当前关键基线保持：

- `paper_modules rows = 843`
- `workflow_mirror_paper_modules rows = 592`
- `mixed_scope_paper_modules rows = 1435`
- `discipline_local_code_registry rows = 447`

## 本轮结论

这一轮的实质不是新增一个新表，而是把“已经写好的自校验 helper”从代码库里的静态函数，推进成 build 过程中真正执行的 gate，并顺手把另外四张 analysis tables 也纳入同一类 fidelity checks。这样现在 `build_analysis_db.py` 已经不只是生成 outputs，而是在生成后主动验证一批关键 analysis surfaces 没有漂移。
