# Structured Data Catalog Round 18 Closeout

日期：2026-07-06

## 本轮目标

推进长期方案中的 PDF / 资料证据层，把现有 derived 层再结构化一步，让后续分析能直接区分：

- 主文 PDF
- supplementary PDF
- HTML full text
- abstract / official page 级别证据

以及：

- 是否属于 full-text checked
- 是否仍然 source-limited
- 文件大小等基础资产属性

## 本轮实现

### 1. 在 `pdf_archive_registry` 中新增 derived 证据字段

更新：

- `scripts/export_structured_data.py`

为 `registry/pdf_archive_registry.jsonl` 新增：

- `asset_size_bytes`
- `pdf_evidence_type`
- `pdf_check_status`
- `is_main_text`
- `is_supplementary`

当前派生逻辑是保守版：

- 若状态中出现 supplementary 语义
  - `pdf_evidence_type = supplementary_pdf`
- 若存在本地 PDF 且不是 supplementary-only
  - `pdf_evidence_type = main_pdf`
- 若无本地 PDF，但 evidence 显示 HTML / PMC / public full text
  - `pdf_evidence_type = html_full_text`
- 若无本地 PDF，但 evidence 更接近 official / DOI / metadata / page
  - `pdf_evidence_type = official_page`
- 若无本地 PDF，但 evidence 更接近 project / repo
  - `pdf_evidence_type = project_page`
- 其余回退为
  - `pdf_evidence_type = abstract`

并进一步派生：

- `pdf_check_status`
  - `full_text_checked`
  - `source_limited`
  - `metadata_only`
- `is_main_text`
- `is_supplementary`

### 2. 在 `asset_manifest` 中补资产粒度字段

更新：

- `scripts/export_structured_data.py`

为 `registry/asset_manifest.jsonl` 新增：

- `asset_size_bytes`
- `is_main_text`
- `is_supplementary`

当前规则：

- `note` 资产固定：
  - `is_main_text = false`
  - `is_supplementary = false`
- `primary_pdf` 资产根据 derived `pdf_evidence_type` 派生主文 / supplementary 标记

### 3. 接入 SQLite

更新：

- `scripts/build_analysis_db.py`

新增接入：

- SQLite `pdf_evidence_status`
  - `pdf_evidence_type`
  - `pdf_check_status`
  - `is_main_text`
  - `is_supplementary`
  - `asset_size_bytes`
- SQLite `paper_assets`
  - `asset_size_bytes`
  - `is_main_text`
  - `is_supplementary`

这样证据层增强字段已经进入现有 analysis DB。

### 4. 接入 checker

更新：

- `scripts/check_data_consistency.py`

新增检查：

- `pdf_evidence_type` 必须属于受控枚举
- `pdf_check_status` 必须属于受控枚举
- `is_main_text` / `is_supplementary` 必须为 bool
- 不允许同时为 `true`
- `main_pdf` 必须对应 `is_main_text=true`
- `supplementary_pdf` 必须对应 `is_supplementary=true`
- 若 `pdf_check_status = full_text_checked`
  - 必须来自 full-text 证据类型
- `asset_size_bytes` 若非空则必须是非负整数
- 现有 primary PDF 资产若存在本地文件
  - 必须有 `sha256`
  - 必须有 `asset_size_bytes`

### 5. 文档同步

更新：

- `Data/field_dictionary.md`

新增说明：

- `pdf_archive_registry` 的 derived 证据字段
- `asset_manifest` 的新增资产粒度字段

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

spot check：

- `ASD-0001`
  - `pdf_evidence_type = main_pdf`
  - `pdf_check_status = full_text_checked`
  - `is_main_text = true`
  - `asset_size_bytes = 1832008`
- `ASD-0005`
  - `pdf_evidence_type = official_page`
  - `pdf_check_status = source_limited`
  - `is_main_text = false`
  - `is_supplementary = false`

## 本轮结论

本轮把证据层从“只有 `pdf_status / evidence_status / source_limited`”推进到了“还能直接看 evidence type、check depth、main/supplementary 标记和基础资产大小”的状态。这样后续做 missing PDF、supplementary-only、source-limited frontier、full-text coverage 之类的分析时，不必再反复从自由文本状态名里手工推断。
