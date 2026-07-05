# Structured Data Catalog Round 22 Closeout

日期：2026-07-06

## 本轮目标

落实长期方案 PDF / 资料证据层中仍未落地的 `source_checked_at`，把它接进现有 derived export / check / build 链路，而不改动四类事实源边界。

## 本轮实现

### 1. 新增 `source_checked_at` 派生逻辑

更新：

- `scripts/export_structured_data.py`

新增字段：

- `source_checked_at`

当前派生规则：

- 优先从 `Remarks` 中提取最近一次带 source/evidence 语义的日期片段
  - 例如 `checked`
  - `rechecked`
  - `archived`
  - `reopened`
  - `text-checked`
  - `official`
  - `HTML`
  - `PDF`
- 如果 `first_hand_sources_checked` 非空但没有命中更强的局部语义窗口：
  - 退回 `Remarks` 中最近日期
- 如果仍拿不到，但已有 evidence / PDF review 痕迹且 change log 存在最近审查日期：
  - 退回 `last_reviewed_at`
- 若都没有：
  - 保持空字符串

这一定义把 `source_checked_at` 明确为 derived review-timing proxy，不把它升级成新的 owner fact。

### 2. 接入 analysis / registry / SQLite

更新：

- `scripts/export_structured_data.py`
- `scripts/build_analysis_db.py`

新增接入位置：

- `Data/papers.jsonl`
- `Data/papers.csv`
- SQLite `papers`
- `Data/registry/pdf_archive_registry.jsonl`
- SQLite `pdf_evidence_status`
- `Data/registry/asset_manifest.jsonl`
- SQLite `paper_assets`

约束：

- `note` 资产行的 `source_checked_at` 固定为空字符串
- `primary_pdf` 资产行镜像论文级 `source_checked_at`
- `pdf_evidence_status.source_checked_at` 与 `papers.source_checked_at` 保持一致

### 3. 接入 checker

更新：

- `scripts/check_data_consistency.py`

新增检查：

- `papers.jsonl.source_checked_at` 必须是字符串
- 非空时必须符合 `YYYY-MM-DD`
- 必须与 checker 端按相同规则重算出的期望值一致
- `pdf_archive_registry.source_checked_at` 必须与 `papers.jsonl` 对齐
- `asset_manifest`
  - `note` 行必须为空
  - `primary_pdf` 行必须与 `papers.jsonl` 对齐

### 4. 文档同步

更新：

- `Data/field_ownership_matrix.md`
- `Data/README.md`
- `Data/field_dictionary.md`

补充内容：

- `source_checked_at` 当前属于 derived evidence-layer field
- 它来源于 progress + remarks provenance + change-log fallback
- 不能手工回写成新的事实源

## 本轮验证

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

额外 spot check：

- `papers.jsonl` 中非空 `source_checked_at` 记录数：`422`
- SQLite `papers` 已包含 `source_checked_at`
- SQLite `pdf_evidence_status` 已包含 `source_checked_at`
- SQLite `paper_assets` 已包含 `source_checked_at`
- `pdf_evidence_status` 中非空 `source_checked_at` 记录数：`422`
- `primary_pdf` 资产行中非空 `source_checked_at` 记录数：`422`

示例：

- `ASD-0006`
  - `source_checked_at = 2026-07-03`
  - 对应 `Remarks` 中最近一次 source review 片段为：
    - `Phase6FollowupR10Approx2026-07-03: locally archived bioRxiv PDF reopened and text-checked`

## 本轮结论

本轮把 `source_checked_at` 从方案里的“待补 evidence-layer 字段”推进成了实际可导出、可校验、可入库的结构化字段。当前它仍然是 derived proxy，不会篡改 progress owner；但后续做 PDF/source review 覆盖率分析、source-limited 跟踪、证据时序抽样时，已经不需要只靠人工读 remarks 了。
