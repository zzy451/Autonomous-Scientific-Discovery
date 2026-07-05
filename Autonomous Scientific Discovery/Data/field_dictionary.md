# ASD Structured Data Field Dictionary
日期: 2026-07-02

本文档定义 `Autonomous Scientific Discovery/Data/` 中 registry 层与 analysis 层的关键文件和字段语义。

## 1. 层级与原则

1. 当前结构化系统有四类事实源:
   - `Paper_Lists/agent_master_paper_list.md`: 论文元数据与分类事实
   - `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`: PDF/source/evidence 核查事实
   - `Data/discipline_code_assignments.jsonl`: 稳定学科管理码 assignment 事实
   - `Data/classification_code_index.json`: taxonomy vocabulary 事实
2. `ASD-xxxx` 是唯一永久主键。任何派生层都必须以 `paper_id` 作为稳定关联键。
3. `01.04` 只表示 general bucket:
   - 它可以出现在 `general_method_bucket`
   - 它可以出现在 registry 的 `taxonomy_code = "01.04"` 行
   - 它不能进入 formal `scientific_object_modules` 数组
4. registry 层是规范化派生层，不是事实源，不允许人工维护来“修正” owner files。
5. analysis 层是面向查询、统计、表格和数据库消费的派生层。若 analysis 或 registry 与 owner files 冲突，先修 owner，再重建。

## 2. 文件层级

### 2.1 事实层

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

前两份仍是论文内容与核查状态的 authoritative pair；后两份分别只拥有 discipline-local code assignment 和 taxonomy vocabulary facts。

### 2.2 Registry 层

- `registry/paper_registry.jsonl`
- `registry/paper_identifier_aliases.jsonl`
- `registry/taxonomy_registry.json`
- `registry/classification_assignments.jsonl`
- `registry/pdf_archive_registry.jsonl`
- `registry/asset_manifest.jsonl`

这些文件都由脚本生成，目标是把事实层规范化成稳定、可连接、可校验的数据表。

### 2.3 Analysis 层

- `papers.jsonl`
- `taxonomy_index.json`
- `classification_code_index.json`
- `discipline_code_assignments.jsonl`
- `discipline_local_code_registry.jsonl`
- `discipline_local_code_registry.csv`
- `pdf_manifest.json`
- `missing_pdf_manifest.json`
- `note_manifest.json`
- `papers.csv`
- `paper_modules.csv`
- `canonical_paper_modules.csv`
- `workflow_mirror_paper_modules.csv`
- `papers.sqlite`

除 `classification_code_index.json` 和 `discipline_code_assignments.jsonl` 两个 owner 文件外，analysis 层用于脚本消费、人工 spot check、统计和 SQL 查询；它不是新的事实口径。

在 SQLite 中，当前还保留两类 compatibility mixed-scope 对象：

- `paper_modules`
- `module_assignment_counts`

它们同时包含 canonical 与 workflow mirror assignment 信息，默认只应用于 inspection / compatibility，而不是 canonical-only 统计。正式统计优先使用：

- `canonical_paper_modules`
- `workflow_mirror_paper_modules`
- `canonical_module_assignment_counts`
- `workflow_mirror_module_assignment_counts`
- `analysis_object_scope_registry`

### 2.4 Phase 3A authoritative freeze clarifications

为避免长上下文协作中再次出现字段 ownership 与语义漂移，当前冻结以下解释:

- `agent_master_paper_list.md` 负责:
  - `paper_id`
  - 论文元信息主记录
  - `inclusion_status`
  - legacy filing fields
  - remarks 中承载的 canonical classification overlay
- `note_path` 在治理上仍由 master 主 ownership，但当前导出解析规则是:
  - `progress.note_path or master.Note path`
- canonical structured classification 从 master remarks 解析得到:
  - `scientific_object_modules`
  - `general_method_bucket`
  - `object_coverage_mode`
  - `primary_module_for_filing`
- 当前 canonical 导出优先级是:
  - remarks 结构化 token
  - unresolved legacy `01 / 01.04` -> 独立 general bucket
  - legacy `Main class` formal fallback
- `multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md` 负责:
  - `pdf_status`
  - `evidence_status`
  - `note_status`
  - `master_status`
  - `final_modules_or_bucket`
  - `source_limited`
  - `batch`
  - `closed`
- `pdf_path` 在治理上仍由 progress 主 ownership，但当前导出解析规则是:
  - `progress.pdf_path or master.PDF path`
- `final_modules_or_bucket` 只是 workflow mirror，不是 canonical classification fact。它可以用于审计 canonical-vs-mirror 一致性，但默认统计不应以它取代 `scientific_object_modules + general_method_bucket`。
- `final_modules_or_bucket` 当前镜像语法是:
  - 分号分隔列表
  - formal `01-11` + 可选 `01.04`
  - 保留顺序，用于 `order_drift` 审计
- `pdf_path` 只是 authoritative pair 中声明的路径字段，不自动等于“本地真 PDF 已验证存在”。本地 PDF 真值必须结合导出后的 `pdf_exists` / `pdf_manifest.json` / 实际文件可读性判断。
- `source_limited` 当前冻结为三态解释:
  - `yes`: 当前 record 仍受来源或全文可得性限制
  - `no`: 当前 record 没有 source-limited 限制
  - 空字符串: 仅表示该 record 当前没有进入 progress 驱动工作流，不应对 active confirmed-core 统计作积极解释
- `object_coverage_mode` 当前只允许:
  - `single_module`
  - `multi_module`
  - `general_method_without_concrete_object_experiments`
- `general_method_bucket` 当前只允许:
  - `none`
  - `01.04_general_asd_methods_without_concrete_object_experiments`
- 结构化输入若写 bare `01.04`，导出会归一化为上述 canonical 长字面值
- `scientific_object_modules` 只允许 formal `01-11`，不得出现 `01.04`。
- `primary_module_for_filing` 只是 filing / display convenience；它可以与 legacy main class 对齐，但不能压扁多模块 canonical classification。
- `evidence_status` 是一手来源层级的描述性 provenance 字段，不是“证据强度分数”；当前冻结为 workflow label 字段，而非正式闭集枚举。
- `pdf_status` 是 PDF 可得性 /归档工作流字段，不是单独的本地文件真值字段；当前冻结为 workflow label 字段，而非正式闭集枚举。

## 3. Registry 文件与关键字段

### 3.1 `registry/paper_registry.jsonl`

定位: 一篇论文一行的规范化 paper registry。

关键字段:

- `paper_id`: 永久主键，格式固定为 `ASD-xxxx`。
- `title`: 论文标题。
- `authors`: 作者字符串。
- `year`: 年份原始文本。
- `source`: 来源或 venue 原始文本。
- `source_locator_raw`: 原始 DOI / arXiv / URL 文本。
- `note_path`: 当前导出的 note 路径。
- `note_exists`: note 是否在本地存在。
- `pdf_path`: 当前导出的主 PDF 路径。
- `pdf_exists`: 主 PDF 是否在本地存在。
- `scientific_object_modules`: formal scientific-object module 数组，只允许 `01-11`。
- `general_method_bucket`: general bucket；当前合法值为 `none` 或 `01.04` 对应的 canonical bucket。
- `object_coverage_mode`: 当前对象覆盖模式。
- `primary_module_for_filing`: 归档主模块，仅用于目录和 filing 便利。
- `classification_display_code`: 面向展示的分类代码，不替代完整分类事实。
- `active_confirmed_core`: 当前结构化导出的 active confirmed-core 布尔标记。
- `pdf_status`, `evidence_status`, `note_status`, `master_status`, `source_limited`, `batch`, `closed`: progress 层工作流字段的规范化派生结果。
- `exported_at`: 本次导出的 UTC 时间戳。

约束:

- `paper_id` 集合必须与 `papers.jsonl` 完全一致。
- `scientific_object_modules` 内不能出现 `01.04`。
- 当 `general_method_bucket != "none"` 时，formal `scientific_object_modules` 必须为空。

### 3.2 `registry/taxonomy_registry.json`

定位: 分类术语 registry。当前文件是一个 JSON 对象，而不是 JSONL。

顶层字段:

- `exported_at`: 导出时间戳。
- `taxonomy_terms`: 术语数组。

`taxonomy_terms` 单行关键字段:

- `taxonomy_code`: 分类代码，如 `04` 或 `01.04`。
- `kind`: 当前只允许 `formal_module` 或 `general_bucket`。
- `labels.display`: 展示标签。
- `sort_order`: 排序权重。
- `dir_name`: 对应目录名。
- `parent_module_code`: 父模块代码；`01.04` 当前挂在 `01` 下。

约束:

- 必须覆盖 formal `01-11` 加 `01.04`。
- `01.04` 的 `kind` 必须是 `general_bucket`。
- 其余 `01-11` 的 `kind` 必须是 `formal_module`。

### 3.2A `registry/paper_identifier_aliases.jsonl`

定位: 论文永久主键之外的稳定查找别名 registry。

关键字段:

- `paper_id`: 关联论文主键。
- `alias_scheme`: 当前只允许 `doi`、`arxiv_id`、`url`。
- `alias_value`: 对应 scheme 的值。
- `is_primary_key`: 当前必须为 `false`，因为永久主键仍只允许 `ASD-xxxx`。
- `exported_at`: 导出时间戳。

约束:

- 该文件只保存真正的外部查找标识或稳定 locator。
- 不要把 `primary_module_for_filing`、展示号、分类显示码、目录路径之类会随重分类变化的字段塞进来。
- 它是 lookup convenience registry，不是新的事实层，也不定义主键。

### 3.3 `registry/classification_assignments.jsonl`

定位: 一篇论文到一个 taxonomy term 的一行 assignment，属于 exploded registry。

关键字段:

- `paper_id`: 关联论文主键。
- `taxonomy_code`: 被分配的 taxonomy 代码。
- `assignment_kind`: 当前只允许 `formal_module` 或 `general_bucket`。
- `assignment_source`: 当前来源字段；formal assignment 来自 `scientific_object_modules`，general assignment 来自 `general_method_bucket`。
- `assignment_order`: 在原始数组或 bucket 表达中的顺序。formal module 从 1 开始；general bucket 当前固定为 1。
- `is_primary_filing`: 该 assignment 是否同时等于 `primary_module_for_filing`。
- `primary_module_for_filing`: 归档主模块镜像字段。
- `object_coverage_mode`: 当前对象覆盖模式镜像字段。
- `active_confirmed_core`: 该论文当前是否属于 active confirmed core。
- `exported_at`: 导出时间戳。

约束:

- formal module assignment 必须满足:
  - `assignment_kind = "formal_module"`
  - `assignment_source = "scientific_object_modules"`
  - `taxonomy_code` 只能在 `01-11`
- general bucket assignment 必须满足:
  - `assignment_kind = "general_bucket"`
  - `assignment_source = "general_method_bucket"`
  - `taxonomy_code = "01.04"`
- 它表达的是 `papers.jsonl` 中 `scientific_object_modules + general_method_bucket` 的规范化展开，不允许自成新的分类事实源。

### 3.4 `registry/pdf_archive_registry.jsonl`

定位: 以论文为粒度的 PDF 归档与可用性 registry。

关键字段:

- `paper_id`: 关联论文主键。
- `title`: 标题镜像字段。
- `pdf_path`: 主 PDF 路径；无本地 PDF 时可为空字符串。
- `pdf_exists`: 本地是否存在可读主 PDF。
- `sha256`: 本地 PDF 哈希；无本地 PDF 时可为空字符串。
- `asset_size_bytes`: 本地 PDF 文件大小；无本地文件时可为空。
- `pdf_status`: progress 派生的 PDF 状态。
- `evidence_status`: progress 派生的证据状态。
- `pdf_evidence_type`: derived 证据类型，如 `main_pdf` / `supplementary_pdf` / `html_full_text` / `abstract` / `official_page` / `project_page`。
- `pdf_check_status`: derived 核查深度状态，如 `full_text_checked` / `source_limited` / `metadata_only`。
- `is_main_text`: 当前 PDF 证据是否为主文全文。
- `is_supplementary`: 当前 PDF 证据是否为 supplementary。
- `source_limited`: 来源受限标记。
- `primary_module_for_filing`: 归档主模块镜像字段。
- `scientific_object_modules`: formal module 数组镜像字段。
- `general_method_bucket`: general bucket 镜像字段。
- `active_confirmed_core`: 是否属于当前 active confirmed core。
- `exported_at`: 导出时间戳。

约束:

- 对 active confirmed-core 论文，`pdf_exists = true` 的集合必须与 active local PDF 口径一致。
- 对 active confirmed-core 论文，`pdf_exists = false` 的集合必须与 active no-local PDF 口径一致。
- 它只规范化导出 PDF 可用性，不替代 progress 对 `pdf_status` 的事实拥有权。

### 3.5 `registry/asset_manifest.jsonl`

定位: 统一资产清单。当前至少覆盖 note 和 primary PDF。

关键字段:

- `paper_id`: 关联论文主键。
- `title`: 标题镜像字段。
- `asset_type`: 当前至少包含 `note` 和 `primary_pdf`。
- `path`: 资产路径。对缺失 primary PDF 可为空字符串。
- `exists`: 本地文件是否存在。
- `sha256`: 文件哈希；缺失文件时可为空字符串。
- `asset_size_bytes`: 文件大小；缺失文件时可为空。
- `asset_status`: 对 note 通常承接 `note_status`，对 PDF 通常承接 `pdf_status`。
- `is_main_text`: 对 PDF 资产记录，是否为主文全文。
- `is_supplementary`: 对 PDF 资产记录，是否为 supplementary。
- `source_limited`: 来源受限标记。
- `exported_at`: 导出时间戳。

约束:

- 每个 `paper_id` 至少应有一条 `note` 记录和一条 `primary_pdf` 记录。
- `note` 记录必须与 `papers.jsonl` 的 `note_path` / `note_exists` 对齐。
- `primary_pdf` 记录必须与 `papers.jsonl` 的 `pdf_path` / `pdf_exists` 对齐。

## 4. Analysis 层文件简表

### 4.1 `papers.jsonl`

定位: 面向脚本和逐篇检查的分析层快照。

重点字段:

- `paper_id`
- `scientific_object_modules`
- `general_method_bucket`
- `final_modules_or_bucket`
- `primary_module_for_filing`
- `pdf_path`, `pdf_exists`
- `note_path`, `note_exists`
- `active_confirmed_core`

说明:

- 它保留 per-paper 视角，适合逐条检查。
- 它不是新的事实层，只是比 registry 更接近“整篇论文一行”的分析表示。
- `final_modules_or_bucket` 在这里应被理解为 progress workflow mirror，而不是 canonical classification source。

### 4.2 `taxonomy_index.json`

定位: analysis 层使用的 taxonomy 映射。

关键字段:

- `code_to_label`
- `label_to_code`

它与 registry `taxonomy_registry.json` 表达同一套 taxonomy，只是更偏分析/查询消费。

### 4.2A `classification_code_index.json`

定位: taxonomy vocabulary owner，负责一级 / 二级分类术语的 label、definition、include / exclude boundary、status 和 source。

关键字段:

- `schema_version`
- `updated_at`
- `updated_by`
- `primary_code_to_label`
- `secondary_code_to_label`
- `label_to_primary_code`
- `label_to_secondary_code`
- `primary_terms`
- `secondary_terms`

约束:

- `01.04` 是 general-method bucket，不是 formal module。
- 二级 term 可先为空，后续从 legacy secondary class 归纳后补。
- 它不是 derived snapshot；分类术语定义变更必须从这里开始。
- 日常 export 只能读取它来校验 taxonomy term，不得覆盖它。
- 若需维护 taxonomy vocabulary，应使用显式 owner helper（当前为 `scripts/manage_classification_code_index.py`），而不是手工去改 derived registry / SQLite。

### 4.2AA canonical classification trace fields

定位: `master-derived canonical lane` 的结构化来源追踪字段，当前导出到 `papers.jsonl` / `papers.csv` / SQLite `papers`。

关键字段:

- `classification_source_field`
- `classification_source_confidence`
- `classification_parser_rule`

当前语义:

- `classification_source_field`
  - 当前 canonical classification 主要来自哪个 owner 字段面
  - 现阶段常见值:
    - `Remarks`
    - `Main class`
    - `Main class;Secondary class`
- `classification_source_confidence`
  - 当前 parser 对 canonical classification lane 来源的置信度
  - 现阶段受控值:
    - `high`
    - `medium`
    - `low`
- `classification_parser_rule`
  - 当前 canonical classification lane 采用的推导规则
  - 现阶段受控值:
    - `structured_remark_token`
    - `legacy_general_method_fallback`
    - `legacy_main_class_fallback`
    - `needs_review`

约束:

- 它们是 trace fields，不是新的事实 owner。
- 它们只解释 canonical classification 如何从 owner facts 推导出来。
- 若未来 master 出现显式 canonical columns，可在不改变 trace 字段职责的前提下扩展 parser rule 枚举。

### 4.2AB primary filing trace fields

定位: `primary_filing_policy` 的结构化派生 trace 字段，当前导出到 `papers.jsonl` / `papers.csv` / SQLite `papers`，并冗余进入 `discipline_local_code_registry`。

关键字段:

- `primary_module_confidence`
- `primary_module_assignment_rule`
- `primary_module_override_reason`

当前语义:

- `primary_module_confidence`
  - 当前 `primary_module_for_filing` 的派生置信度
  - 现阶段受控值:
    - `high`
    - `medium`
    - `low`
- `primary_module_assignment_rule`
  - 当前 `primary_module_for_filing` 使用的推导 / 归档规则
  - 现阶段受控值:
    - `main_scientific_object`
    - `main_validation_object`
    - `direct_contribution_target`
    - `substantive_application_object`
    - `manual_override`
- `primary_module_override_reason`
  - 当当前排架位需要 override / fallback 解释时，记录派生原因

当前导出层已使用的派生模式:

- 单模块 formal record:
  - `primary_module_confidence = high`
  - `primary_module_assignment_rule = main_scientific_object`
- 多模块且由显式 `Remarks` 主排架 token 支撑:
  - `primary_module_assignment_rule = manual_override`
  - `primary_module_override_reason = structured_remark_primary_module_for_filing`
- 多模块且退回 legacy main-class 解释:
  - `primary_module_assignment_rule = manual_override`
  - `primary_module_override_reason = legacy_main_class_fallback_for_multi_module`

约束:

- 它们是 derived trace fields，不是新的 owner fact。
- pure `01.04` general-method-only 记录不应携带这三个字段的非空值。
- 单模块 record 不应凭空出现 override reason。

### 4.2B `discipline_code_assignments.jsonl`

定位: 稳定 discipline-local code assignment 当前状态账本。

关键字段:

- `assignment_id`
- `paper_id`
- `discipline_local_code`
- `primary_taxonomy_code_2lvl`
- `assignment_status`
- `assigned_at`
- `assigned_by`
- `retired_at`
- `redirected_to_code`
- `assignment_reason`
- `pending_reason`
- `source_primary_module_for_filing`
- `source_legacy_secondary_class`
- `schema_version`

约束:

- `assignment_id` 使用 `DCA-000001` 递增格式，不重排、不复用。
- `active_code` / `retired_code` / `redirected_code` 必须有非空 `discipline_local_code`。
- `pending_secondary` / `non_discipline_general_method` 必须有空 `discipline_local_code`。
- 同一 `paper_id` 最多一条 `active_code`。
- 它不是 derived snapshot，不得由 export 覆盖重建。

### 4.2C `discipline_local_code_registry.jsonl`

定位: discipline code owner ledger 的当前快照层，供 CSV / SQLite / review 排序使用。

关键字段:

- `paper_id`
- `assignment_id`
- `discipline_local_code`
- `discipline_local_rank`
- `discipline_display_order`
- `assignment_status`

约束:

- `discipline_local_rank = parse_NNN(discipline_local_code)`，只能派生，不允许人工维护。
- `discipline_display_order` 是 derived 排序字段，用于展示 / CSV / review 排序，不拥有稳定管理码事实。
- registry 是 derived snapshot，不能手工回写成为事实源。

### 4.3 `pdf_manifest.json`

定位: 当前本地真实存在的主 PDF 清单。

关键字段:

- `paper_id`
- `pdf_path`
- `sha256`
- `primary_module_for_filing`
- `scientific_object_modules`
- `pdf_status`
- `active_confirmed_core`

### 4.4 `missing_pdf_manifest.json`

定位: active confirmed core 中暂无本地 PDF 的论文清单。

关键字段:

- `paper_id`
- `doi`
- `url`
- `pdf_status`
- `evidence_status`
- `source_limited`
- `access_note`

### 4.5 `note_manifest.json`

定位: note 路径与存在性清单。

关键字段:

- `paper_id`
- `note_path`
- `note_exists`
- `active_confirmed_core`
- `inclusion_status`

## 5. 非协商一致性规则

1. `ASD-xxxx` 是唯一永久主键。
2. `01.04` 只能作为 general bucket，不进入 formal module 数组。
3. master + progress 是论文内容与核查状态事实层；`discipline_code_assignments.jsonl` 与 `classification_code_index.json` 是 Data 内的 owner 例外。
4. registry 与普通 analysis outputs 都不能演化成手工维护的事实源。
5. 日常 export 只生成 derived outputs，不得覆盖 `discipline_code_assignments.jsonl` 或 `classification_code_index.json`。
6. 任何结构化变更都应先改对应 owner file，再跑导出和一致性校验。
