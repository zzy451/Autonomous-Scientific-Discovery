# Structured Data Catalog Round 105 Closeout

日期：2026-07-06

## 本轮目标

继续把 derived registry 的语义从“只有 coverage 检查”推进到“字段镜像也必须严格对齐事实派生快照”。本轮聚焦 `Data/registry/paper_registry.jsonl`，补齐它和 `papers.jsonl` 之间的逐字段一致性校验。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 扩展 `paper_registry` 必填字段检查

此前 `paper_registry.jsonl` 在 registry 层几乎只检查了：

- `paper_id` 存在
- `paper_id` 唯一
- `paper_id` 覆盖与 `papers.jsonl` 一致

本轮把 `require_row_fields()` 扩展到 paper registry 的整组核心镜像字段，包括：

- 文献信息：`title`、`authors`、`year`、`source`
- 路径 / 存在性：`note_path`、`note_exists`、`pdf_path`、`pdf_exists`
- legacy class 与 object 分类：`legacy_*`、`scientific_object_modules`、`general_method_bucket`
- 派生状态：`object_coverage_mode`、`primary_module_for_filing`
- 工作流状态：`pdf_status`、`evidence_status`、`note_status`、`master_status`
- 生命周期/批次相关：`active_confirmed_core`、`source_limited`、`batch`、`closed`
- metadata：`exported_at`

### 2. `paper_registry` 逐字段镜像校验

本轮新增 `paper_registry` 每行对 `papers.jsonl` 的字段值核对，要求下列字段必须逐项一致：

- `title`
- `authors`
- `year`
- `source`
- `source_locator_raw == papers.doi_or_url`
- 以及其余镜像字段，如 `note_path`、`pdf_path`、`scientific_object_modules`、`pdf_status`、`evidence_status`、`exported_at` 等

这样 `paper_registry.jsonl` 不再只是“有一行这个 paper”，而是必须忠实镜像 `papers.jsonl` 的对应派生字段。

### 3. `classification_display_code` 派生语义校验

`paper_registry.jsonl` 里还有一个之前未显式校验的派生字段：

- `classification_display_code`

本轮新增规则：

- 若 `general_method_bucket != none`，必须为 `01.04`
- 否则若 `scientific_object_modules` 非空，必须为模块列表的 `;` 连接结果
- 否则必须为空字符串

这一步把 paper registry 中的展示分类码也正式纳入派生一致性检查。

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

本轮把 `paper_registry.jsonl` 从“身份覆盖表”进一步推进成“受约束的 papers 镜像层”。这和方案里 registry 作为 derived layer、但又必须可追溯可校验的要求是一致的，也减少了 `paper_registry` 字段静默漂移的空间。

## 后续状态

当前无新的代码级阻塞点；可以继续沿其余 registry / SQLite / metadata 交界处尚未显式化的约束逐轮推进。
