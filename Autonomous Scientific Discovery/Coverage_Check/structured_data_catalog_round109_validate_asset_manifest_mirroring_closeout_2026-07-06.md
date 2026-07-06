# Structured Data Catalog Round 109 Closeout

日期：2026-07-06

## 本轮目标

继续把 `asset_manifest.jsonl` 从“资产存在性表”推进到“受约束的资产镜像层”。此前它已经检查了 note / primary_pdf 的路径、存在性和部分 source 字段，但还没有把资产身份字段、状态字段、`source_limited` 和 `exported_at` 一并锁死。本轮补齐这部分。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 扩展 `asset_manifest` 必填字段

本轮将以下字段纳入 `require_row_fields()`：

- `asset_id`
- `paper_id`
- `title`
- `asset_type`
- `path`
- `exists`
- `sha256`
- `asset_size_bytes`
- `asset_status`
- `is_main_text`
- `is_supplementary`
- `source_limited`
- `source_checked_at`
- `exported_at`

这让 asset manifest 不再只是“有 path / exists 就行”的资产清单，而是要求完整资产镜像字段同时存在。

### 2. 锁定资产身份语义

新增：

- `asset_id` 必须严格等于 `<paper_id>:<asset_type>`
- `asset_type` 只允许 `note` 或 `primary_pdf`
- 全表 `(paper_id, asset_type)` 集合必须严格等于“每篇论文各一条 `note` 和一条 `primary_pdf`”

这一步把 asset manifest 的资产身份从“隐含约定”提升为正式一致性规则。

### 3. `asset_manifest` 逐字段镜像校验

对 note 资产新增检查：

- `title == papers.title`
- `asset_status == papers.note_status`
- `source_limited == papers.source_limited`
- `exported_at == papers.exported_at`

对 `primary_pdf` 资产新增检查：

- `asset_status == papers.pdf_status`
- `source_limited == papers.source_limited`
- `exported_at == papers.exported_at`

此前已检查的：

- `path`
- `exists`
- `source_checked_at`
- `is_main_text`
- `is_supplementary`

本轮之后，asset manifest 已经从“路径层派生表”进一步推进成“身份 + 状态 + 路径 + metadata”四位一体的 derived snapshot。

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

本轮把 `asset_manifest.jsonl` 的资产身份和镜像元数据层正式锁定，减少了资产 registry 在 `asset_id`、`asset_status`、`source_limited`、`exported_at` 等字段上的静默漂移空间。这和长期方案里 asset / PDF / note 需要可追踪、可映射、可校验的要求一致。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 SQLite 自检细项、remaining registry metadata、以及执行定义尚未显式量化的边缘约束逐轮推进。
