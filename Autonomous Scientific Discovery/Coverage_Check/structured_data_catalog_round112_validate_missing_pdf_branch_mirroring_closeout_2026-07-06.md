# Structured Data Catalog Round 112 Closeout

日期：2026-07-06

## 本轮目标

继续收口 no-local-PDF 这一支的派生层。此前：

- `missing_pdf_manifest.json` 主要只校 paper_id 覆盖
- `missing_pdf_inventory` 也只是把 manifest 装进 SQLite

但还没有把它们和 `papers.jsonl` 的逐字段镜像关系、以及最小的数据形状约束正式锁死。本轮补齐这部分。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`
- `scripts/build_analysis_db.py`

### 1. `missing_pdf_manifest.json` 逐字段镜像校验

在 `check_data_consistency.py` 中新增：

- `title == papers.title`
- `doi == papers.doi`
- `url == papers.url`
- `pdf_status == papers.pdf_status`
- `evidence_status == papers.evidence_status`
- `source_limited == papers.source_limited`
- `access_note == papers.remarks`

并额外要求：

- `access_note` 必须非空白

这样 `missing_pdf_manifest` 不再只是“active no-local-PDF paper_id 列表”，而是正式成为 papers snapshot 的 no-local-PDF 分支镜像。

### 2. `missing_pdf_inventory` SQLite 原生约束

在 `build_analysis_db.py` 中为 `missing_pdf_inventory` 新增：

- `source_limited` 值域约束：`'', 'no', 'yes'`
- `access_note` 非空白约束：`trim(access_note) <> ''`

这两条约束都和当前导出数据一致，而且直接对应这张 inventory 表的长期用途：

- `source_limited` 必须可解释
- `access_note` 不能退化成空壳占位

### 3. build 自检同步覆盖 `missing_pdf_inventory`

`validate_evidence_sqlite_constraints()` 现已读取并检查：

- `missing_pdf_inventory` 的上述两个约束片段是否真实写入 `sqlite_master`

所以这部分不是“只在建表 SQL 里写了”，而是 build 自检也会再次核验。

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

本轮把 no-local-PDF 这一支从“分流名单”推进成“受约束的镜像分支”。这符合长期方案里 PDF / evidence 层需要同时支撑：

- 本地 PDF 已归档分支
- 无本地 PDF 但有结构化可核查证据分支

且两支都要可回连、可审计、可稳定导出。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite 自检细项、discipline/analysis 边缘语义、以及少量仍未显式量化的 derived metadata 约束逐轮推进。
