# Structured Data Catalog Round 113 Closeout

日期：2026-07-06

## 本轮目标

继续把 manifest 层从“coverage / existence 清单”推进到“严格 mirror 的 derived snapshot”。本轮聚焦：

- `Data/pdf_manifest.json`
- `Data/note_manifest.json`

把它们和 `papers.jsonl` 的逐字段对应关系正式显式化。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. `pdf_manifest.json` 逐字段镜像校验

本轮新增：

- `title == papers.title`
- `pdf_path == papers.pdf_path`
- `primary_module_for_filing == papers.primary_module_for_filing`
- `scientific_object_modules == papers.scientific_object_modules`
- `pdf_status == papers.pdf_status`
- `evidence_status == papers.evidence_status`
- `active_confirmed_core == papers.active_confirmed_core`

同时保留并加强：

- `pdf_path` 必须真实存在
- `sha256` 不得为空
- `sha256` 必须是 64 位小写十六进制

这样 `pdf_manifest` 不再只是“本地 PDF 文件列表”，而是正式成为 papers snapshot 在本地 PDF 分支上的精确镜像。

### 2. `note_manifest.json` 逐字段镜像校验

本轮新增：

- `title == papers.title`
- `note_path == papers.note_path`
- `note_exists == papers.note_exists`
- `active_confirmed_core == papers.active_confirmed_core`
- `inclusion_status == papers.inclusion_status`

此前 `note_manifest` 主要只有 `paper_id` 覆盖检查；本轮之后，它也被提升成真正的 derived note snapshot，而不是松散的路径表。

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

本轮把 note / PDF manifest 这两个最基础的文件清单层也纳入了 exact mirroring discipline。这样从：

- `papers.jsonl`
- 到 registry
- 到 manifest
- 到 SQLite inventory

这一串 derived layer 之间的对齐程度又更完整了一步。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite 自检细项、少量尚未显式化的 metadata / mirror 语义，以及执行定义与长期方案之间还未完全闭合的边缘项逐轮推进。
