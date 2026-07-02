# ASD structured-data authoritative acceptance checklist

日期：2026-07-02
范围：`Phase 3B` baseline acceptance
基线对象：当前 active confirmed-core `447`

本文档是 `Phase6FollowupR5` 之后的第一次正式 structured-data acceptance checklist。它不替代脚本，而是把“哪些证据证明当前快照已经足够正式可依赖”写成 controller 可重复执行的检查表。

本次验收针对的是 authoritative baseline 是否成立，不等价于“legacy row-level schema migration 已完成”。

## 1. 执行命令

本轮验收使用的串行命令：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" bucket-0104-summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" boundary-cases
```

## 2. 验收结论

本轮结论：`PASS`

当前可正式接受的 baseline 是：

- active confirmed-core: `447`
- active local PDF: `421`
- active no-local-PDF: `26`
- canonical active `01.04` bucket: `9`
- workflow mirror semantic drift: `0`
- workflow mirror order drift: `0`

本轮 acceptance caveat：

- legacy `Main class / Secondary class` 视觉显示仍可能滞后于 canonical overlay
- 因此正式验收 authority 依赖结构化导出、registry、SQLite 与 consistency checks，而不是依赖 legacy 列本身的肉眼显示

## 3. Checklist

| 验收项 | 证据 | 结果 | 说明 |
|---|---|---|---|
| authoritative pair 可正常导出 | `export_structured_data.py` 成功执行 | PASS | registry 与 analysis 层已从 master/progress 重建 |
| strict consistency 可通过 | `check_data_consistency.py` 输出 `All structured-data consistency checks passed.` | PASS | 当前未发现结构一致性错误 |
| active confirmed-core = `447` | `check_data_consistency.py`; `query_analysis_db.py summary` | PASS | 与项目当前 confirmed-core 基线一致 |
| active local PDF = `421` | `check_data_consistency.py`; `query_analysis_db.py summary` | PASS | 以真实本地可读 PDF 为准，而不是只看 `pdf_path` |
| active no-local-PDF = `26` | `check_data_consistency.py`; `query_analysis_db.py summary`; `missing_pdf_manifest.json` | PASS | 当前 26 篇仍无本地真 PDF |
| 26 篇无本地 PDF 但可索引 | `missing_pdf_manifest.json` | PASS | `26/26` 均有 DOI，无“条目找不到”问题 |
| `01.04` 与 formal `01-11` 分离 | `papers.jsonl`; `taxonomy_registry.json`; `bucket-0104-summary` | PASS | active confirmed-core 中 canonical `01.04` bucket 当前为 `9`；`scientific_object_modules` 中 `01.04` leak 数量为 `0` |
| canonical 与 mirror 默认区分成立 | `README.md`; `field_dictionary.md`; SQLite canonical views | PASS | 默认查询说明已明确 canonical-only；mirror 只用于 audit |
| workflow mirror semantic drift = `0` | `check_data_consistency.py` | PASS | 当前没有 canonical-vs-final 的语义漂移 |
| workflow mirror order drift = `0` | `check_data_consistency.py` | PASS | 当前没有顺序漂移 |
| acceptable mirror 被单独识别 | `query_analysis_db.py bucket-0104-summary` | PASS | `acceptable_mirror_count = 9`，全部来自 canonical `01.04` bucket records |
| paper_modules / SQLite / registry 都从同一 canonical classification 派生 | `classification_assignments.jsonl`; `paper_modules.csv`; `papers.sqlite`; `check_data_consistency.py` | PASS | 当前脚本已验证 registry assignments 与 `papers.jsonl` 的 canonical facts 覆盖一致 |
| legacy 视觉列不作为最终 acceptance authority | master schema note; canonical exports; spot-check samples | PASS | 当前验收显式接受“legacy 行显示仍未完全迁移”，但不接受把它当 canonical 真值 |

## 4. Baseline evidence notes

### 4.1 Confirmed-core baseline

`query_analysis_db.py summary` 与 `check_data_consistency.py` 一致确认：

- `papers_record_count = 871`
- `active_confirmed_core_count = 447`
- `active_local_pdf_count = 421`
- `active_no_local_pdf_count = 26`

### 4.2 Missing-PDF baseline

`missing_pdf_manifest.json` 当前有 `26` 行，且 `26/26` 都有 DOI。

这意味着当前缺的是“本地真 PDF”，不是“文献条目不可索引”。

### 4.3 `01.04` bucket baseline

当前 active confirmed-core 中 canonical `01.04` bucket count = `9`。

当前 9 篇是：

- `ASD-0006`
- `ASD-0040`
- `ASD-0053`
- `ASD-0059`
- `ASD-0111`
- `ASD-0145`
- `ASD-0530`
- `ASD-0541`
- `ASD-0553`

同时：

- active confirmed-core 中 `scientific_object_modules` 含 `01.04` 的记录数 = `0`
- active confirmed-core 中：
  - formal-module 论文数 = `438`
  - general-bucket 论文数 = `9`
  - `both = 0`
  - `neither = 0`
- `query_analysis_db.py bucket-0104-summary` 显示：
  - `bucket_related_papers = 9`
  - `acceptable_mirror_count = 9`
  - `bucket_replaced_by_formal_modules_count = 0`
  - `bucket_added_in_final_count = 0`

### 4.4 Drift split

当前 drift split 为：

- semantic drift: `0`
- order drift: `0`
- acceptable mirror: `9`

这里的 `acceptable mirror` 不是错误，而是 canonical `01.04` bucket 在 workflow mirror 中被正确保留为 `01.04` 的可接受镜像差异类。

### 4.5 Spot-check evidence

为避免后续只停留在“样本 ID 名单”层，本轮保留以下 4 个代表性 spot-check 样本，直接展示当前关键字段现值。

#### 样本 A：真 `01.04` bucket

`ASD-0006`

- `legacy_main_class = 01`
- `legacy_secondary_class = 01.04`
- `scientific_object_modules = []`
- `general_method_bucket = 01.04_general_asd_methods_without_concrete_object_experiments`
- `object_coverage_mode = general_method_without_concrete_object_experiments`
- `final_modules_or_bucket = ["01.04"]`
- `pdf_exists = true`，且 `pdf_manifest.json` 中有对应 `sha256`

该样本证明：canonical `01.04` 是独立 bucket，而不是 formal `01-11` 模块的别名；同时它也说明 `01.04` bucket record 可以拥有本地真 PDF，但仍不进入 `scientific_object_modules`。

#### 样本 B：legacy 显示滞后，但 canonical 已正确转 formal modules

`ASD-0868`

- `legacy_main_class = 01`
- `legacy_secondary_class = 01.04`
- `scientific_object_modules = ["02"]`
- `general_method_bucket = none`
- `object_coverage_mode = single_module`
- `primary_module_for_filing = 02`
- `final_modules_or_bucket = ["02"]`
- `pdf_exists = true`

该样本证明：legacy `Main class / Secondary class` 的视觉显示不能被当作最终 acceptance authority；当前 authoritative acceptance 必须看 canonical overlay 导出的 formal modules。

#### 样本 C：代表性 multi-module record，且未被 filing 字段压扁

`ASD-0866`

- `scientific_object_modules = ["03", "04", "06", "07", "09"]`
- `general_method_bucket = none`
- `object_coverage_mode = multi_module`
- `primary_module_for_filing = 07`
- `final_modules_or_bucket = ["03", "04", "06", "07", "09"]`
- `pdf_exists = true`

该样本证明：`primary_module_for_filing` 只是 filing convenience；即使 filing 主模块是 `07`，canonical 仍保留完整的多模块数组，不会被压扁成单主类。

#### 样本 D：无本地 PDF，但可索引且仍是有效 confirmed-core

`ASD-0005`

- `scientific_object_modules = ["03", "04"]`
- `general_method_bucket = none`
- `pdf_path = ""`
- `pdf_exists = false`
- `pdf_status = publisher_pdf_gated`
- `evidence_status = first_hand_abstract_plus_official_supporting_info`
- `source_limited = yes`
- `doi = 10.1021/jacs.4c17738`
- `missing_pdf_manifest.json` 中存在对应记录

该样本证明：当前 `26` 篇 no-local-PDF 记录缺的是“本地真 PDF”，不是“文献条目不可索引”；因此 accepted baseline 中的 no-local-PDF 集是可追踪、可解释、且仍属于有效 confirmed-core 的。

## 5. 本轮特别备注

1. 当前 machine-verified `01.04` active confirmed-core count 是 `9`，因此验收应以当前脚本快照为准，不应继续引用旧的人工作业摘要数字。
2. 当前 baseline 已足以支撑 `447 / 421 / 26 / 9 / drift 0` 的正式 acceptance。
3. 这次验收通过不意味着后续不再补全文；它只表示当前结构化快照已和 authoritative pair 对齐，且 drift 已经清零。
4. 当前最值得保留的 spot-check 样本已经在 `4.5 Spot-check evidence` 中展开，覆盖了：
   - 真 `01.04` bucket
   - legacy 显示滞后但 canonical 已正确
   - 代表性 multi-module
   - 无本地 PDF 但可索引
