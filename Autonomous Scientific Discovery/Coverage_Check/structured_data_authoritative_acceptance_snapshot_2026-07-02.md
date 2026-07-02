# ASD 结构化数据 authoritative 快照验收记录

日期：2026-07-02

本文档是对当前 ASD 结构化数据快照的正式验收记录，对应执行方案：

- `Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md`

本次验收目标是确认：当前 `Data/` 快照是否忠实反映 authoritative pair，且是否已经满足 Phase 3B 的最小收口要求。

## 1. 验收对象

authoritative pair：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

派生层：

- `Data/papers.jsonl`
- `Data/taxonomy_index.json`
- `Data/pdf_manifest.json`
- `Data/missing_pdf_manifest.json`
- `Data/note_manifest.json`
- `Data/registry/`
- `Data/papers.csv`
- `Data/paper_modules.csv`
- `Data/papers.sqlite`

执行链路：

1. `python "Autonomous Scientific Discovery/scripts/export_structured_data.py"`
2. `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
3. `python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"`

## 2. 快照标识

- `schema_version`: `2026-07-01`
- `papers_jsonl_sha256`: `7c91964551a1005a86d7db31b46001c511ea5129337c4bc8487ba0c397bc7028`
- `papers_record_count`: `871`

以上快照标识来自：

- `Data/papers.sqlite` metadata
- `query_analysis_db.py summary`

## 3. 本轮主控修正

本轮对 progress workflow mirror 做了 3 处对齐修正：

1. `ASD-0613`: `02;04 -> 02`
2. `ASD-0715`: `06;07 -> 07;06`
3. `ASD-0838`: `03;04 -> 03`

修正原因：

- `ASD-0613` 与 `ASD-0838` 属于 mirror 对 canonical classification 的语义漂移。
- `ASD-0715` 属于 mirror 与 canonical classification 的顺序漂移。

修正后，本轮 `workflow mirror drift` 已清零。

## 4. 验收 checklist

### 4.1 Baseline

| 检查项 | 证据来源 | 结果 | 通过标准 |
|---|---|---|---|
| 记录总量是否稳定 | `query_analysis_db.py summary` | 通过 | `papers_record_count = 871` |
| confirmed-core 是否稳定 | `check_data_consistency.py`；`query_analysis_db.py summary` | 通过 | `active_confirmed_core_count = 447` |
| 本地真 PDF 数量是否稳定 | `check_data_consistency.py`；`query_analysis_db.py summary` | 通过 | `active_local_pdf_count = 421` |
| 无本地 PDF 但可索引数量是否稳定 | `check_data_consistency.py`；`query_analysis_db.py summary` | 通过 | `active_no_local_pdf_count = 26` |
| 快照是否具有可追踪身份 | `papers.sqlite` metadata | 通过 | 具备 `schema_version + papers_jsonl_sha256` |

### 4.2 Classification

| 检查项 | 证据来源 | 结果 | 通过标准 |
|---|---|---|---|
| canonical classification 事实源是否明确 | `Data/README.md`；`Data/field_dictionary.md` | 通过 | formal classification 由 master/progress 派生，不以 mirror 替代 |
| `01.04` 是否严格停留在独立 bucket | `Data/field_dictionary.md`；`check_data_consistency.py` | 通过 | `01.04` 不进入 `scientific_object_modules` |
| multi-module 是否未被 filing 字段压扁 | `check_data_consistency.py`；`papers.jsonl` | 通过 | `scientific_object_modules` 保留完整数组，`primary_module_for_filing` 仅作 filing convenience |
| canonical / mirror 边界是否可审计 | `Data/README.md`；`check_data_consistency.py` | 通过 | `final_modules_or_bucket` 仍作为 workflow mirror 单独保留 |
| workflow mirror drift 是否清零 | `check_data_consistency.py` | 通过 | total = `0`；semantic = `0`；order = `0` |

### 4.3 PDF Evidence

| 检查项 | 证据来源 | 结果 | 通过标准 |
|---|---|---|---|
| active local PDF 集是否正确 | `pdf_manifest.json`；`pdf_archive_registry.jsonl`；`check_data_consistency.py` | 通过 | active local PDF = `421` |
| active no-local-PDF 集是否正确 | `missing_pdf_manifest.json`；`check_data_consistency.py` | 通过 | active no-local-PDF = `26` 且 ID 集与 baseline 一致 |
| PDF 真值是否不被 `pdf_path` 非空替代 | `Data/README.md`；`check_data_consistency.py` | 通过 | 以 `pdf_exists + 本地文件存在` 为准 |
| 本地 PDF 是否可回溯 | `pdf_manifest.json` | 通过 | 本地存在的 PDF 均有 `sha256` |
| 缺失 PDF 是否仍保留为有效 confirmed-core 记录 | `missing_pdf_manifest.json`；`query_analysis_db.py missing-pdf` | 通过 | 26 篇保持为有效记录，不视为条目丢失 |

### 4.4 Registry / Analysis Boundary

| 检查项 | 证据来源 | 结果 | 通过标准 |
|---|---|---|---|
| registry 是否明确为派生层 | `Data/README.md`；`Data/field_dictionary.md` | 通过 | registry 不是第三事实源 |
| analysis 是否明确为消费层 | `Data/README.md` | 通过 | `jsonl/csv/sqlite` 不能替代事实修复 |
| registry 与 analysis 是否从同一 canonical classification 派生 | `check_data_consistency.py` | 通过 | registry coverage、assignment、asset、PDF 信息与 `papers.jsonl` 一致 |
| taxonomy 语义是否统一 | `taxonomy_index.json`；`registry/taxonomy_registry.json`；`check_data_consistency.py` | 通过 | formal `01-11` + 独立 `01.04` 完整覆盖 |
| 默认统计是否未混入 mirror drift | `check_data_consistency.py`；`build_analysis_db.py`；`query_analysis_db.py` | 通过 | mirror 仍可审计，但本轮 drift 已清零 |

### 4.5 CI / Regen Discipline

| 检查项 | 证据来源 | 结果 | 通过标准 |
|---|---|---|---|
| 再生顺序是否明确 | `Data/README.md` | 通过 | 固定为 `export -> check -> build` |
| 严格校验是否为最低门槛 | `Data/README.md`；`check_data_consistency.py` | 通过 | `check_data_consistency.py` 严格模式通过 |
| 派生层禁止手改规则是否明确 | `Data/README.md`；`Data/field_dictionary.md` | 通过 | 不允许手改派生层替代事实修复 |
| authoritative pair 变化后是否有 CI guard | `.github/workflows/structured-data-guard.yml` | 通过 | 未重建派生层的提交会被阻断 |
| baseline 变更是否需要显式说明 | `structured_data_post_phase2_execution_plan_2026-07-02.md` | 通过 | baseline 变更必须单独说明，不允许静默漂移 |

## 5. 验收命令结果摘要

### `check_data_consistency.py`

```text
papers.jsonl records: 871
active confirmed-core: 447
active local PDFs: 421
active no-local-PDF: 26
workflow mirror drift count (progress final_modules_or_bucket vs canonical derived classification): 0
workflow mirror semantic drift count: 0
workflow mirror order drift count: 0
All structured-data consistency checks passed.
```

### `query_analysis_db.py summary`

```text
schema_version: 2026-07-01
papers_jsonl_sha256: 7c91964551a1005a86d7db31b46001c511ea5129337c4bc8487ba0c397bc7028
papers_record_count: 871
active_confirmed_core_count: 447
active_local_pdf_count: 421
active_no_local_pdf_count: 26
```

## 6. 本轮结论

本轮 authoritative 快照验收结论为：`通过`。

具体含义是：

1. 当前 authoritative baseline `447 / 421 / 26` 已经再次通过严格校验。
2. canonical classification、PDF evidence、registry/analysis boundary、CI/regen discipline 均已达到当前 Phase 3B 最低要求。
3. 本轮之前存在的 `2` 条语义漂移和 `1` 条顺序漂移已全部在 progress workflow mirror 中收平。
4. 当前结构化快照已经可以作为后续 Phase 4 分析口径固化的直接起点。

## 7. 保留意见与下一步

虽然本轮验收已通过，但后续仍应继续推进以下工作：

1. 把默认查询与默认统计进一步显式收紧到 canonical-only。
2. 补面向协作者的简明 SOP，固定 baseline 更新纪律。
3. 在后续有新一轮 reclassification / note writeback 时，持续保证 workflow mirror 不重新偏离 canonical classification。
