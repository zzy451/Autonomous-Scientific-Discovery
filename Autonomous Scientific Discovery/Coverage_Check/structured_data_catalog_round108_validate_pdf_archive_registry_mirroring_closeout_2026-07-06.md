# Structured Data Catalog Round 108 Closeout

日期：2026-07-06

## 本轮目标

继续把 evidence-derived registry 从“语义合理”推进到“镜像字段也必须严格对回 `papers.jsonl`”。本轮聚焦 `Data/registry/pdf_archive_registry.jsonl`，补齐它与 paper snapshot 之间的逐字段一致性校验。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 扩展 `pdf_archive_registry` 必填字段

本轮将以下字段纳入 `require_row_fields()`：

- `asset_id`
- `asset_role`
- `title`
- `pdf_path`
- `pdf_exists`
- `pdf_status`
- `evidence_status`
- `pdf_evidence_type`
- `pdf_check_status`
- `is_main_text`
- `is_supplementary`
- `source_limited`
- `source_checked_at`
- `primary_module_for_filing`
- `scientific_object_modules`
- `general_method_bucket`
- `active_confirmed_core`
- `exported_at`

这样 `pdf_archive_registry` 不再只是“有 paper_id 和几个状态列”的表，而是要求整组核心 evidence / mirror 字段都存在。

### 2. `pdf_archive_registry` 逐字段镜像校验

新增以下对 `papers.jsonl` 的严格对齐检查：

- `asset_id == <paper_id>:primary_pdf`
- `asset_role == primary_pdf`
- `title`
- `source_limited`
- `primary_module_for_filing`
- `scientific_object_modules`
- `general_method_bucket`
- `active_confirmed_core`
- `exported_at`

此前这张表已经校验：

- `pdf_status`
- `evidence_status`
- `source_checked_at`
- `pdf_path`

本轮之后，它从 evidence 状态表进一步提升成“evidence + paper mirror”双重约束的 registry。

### 3. `pdf_archive_registry` 的派生身份字段正式锁定

`pdf_archive_registry` 中的：

- `asset_id`
- `asset_role`

之前并未显式验证是否真符合 export 规则。现在它们也被纳入 check：

- 每行都必须是该 paper 的 `primary_pdf` 资产身份

这减少了 asset identity 静默漂移的空间。

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

## 产出判断

本轮把 `pdf_archive_registry.jsonl` 从“证据状态表”继续推进成“受约束的 primary PDF snapshot registry”。这更符合长期方案里 PDF / 证据层需要和 paper snapshot、路径、模块映射一起稳定联动的要求。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 `asset_manifest.jsonl` 的镜像字段、asset identity 语义、以及 SQLite / registry 交界处剩余未显式化的约束逐轮推进。
