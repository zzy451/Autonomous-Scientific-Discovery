# ASD 结构化数据字段字典

日期：2026-07-01

本文档定义 `Autonomous Scientific Discovery/Data/` 及其配套分析层的正式字段含义。目标是让后续查询、统计、补档、清洗、作图、数据库使用都基于同一套字段语义。

## 1. 使用原则

1. 唯一事实源仍然是 `Paper_Lists/agent_master_paper_list.md` 和 `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`。
2. `Data/` 中的 JSON、CSV、SQLite 都是派生层，应通过脚本重建，不应手改来修正事实。
3. `ASD-xxxx` 是唯一永久主键。
4. 正式 scientific-object 分类用数组保存。
5. `01.04` 是独立 general-method bucket，不属于正式 `01-11` scientific-object module 数组。

## 2. 文件级说明

当前 `Data/` 目录中的核心文件分为四类：

### 2.1 主记录层

- `papers.jsonl`
- `papers.csv`
- SQLite `papers` 表

这一层以“一篇论文一条记录”为原则。

### 2.2 taxonomy 层

- `taxonomy_index.json`
- SQLite `taxonomy_index` 表

这一层负责保存分类代码与分类名称的映射。

### 2.3 清单层

- `pdf_manifest.json`
- `missing_pdf_manifest.json`
- `note_manifest.json`
- SQLite `pdf_inventory`
- SQLite `missing_pdf_inventory`
- SQLite `note_inventory`

这一层负责 PDF、缺失 PDF、note 的审计和查询。

### 2.4 分析展开层

- `paper_modules.csv`
- SQLite `paper_modules`
- SQLite `module_assignment_counts` 视图

这一层负责把多模块数组展开成多行，便于统计与分析。

## 3. `papers.jsonl` / `papers.csv` / SQLite `papers` 主字段

### 3.1 主键与基础元数据

`paper_id`
: 永久唯一论文 ID，例如 `ASD-0001`。

`title`
: 论文标题。

`authors`
: 作者字段，保持 master 原始文本。

`year`
: 年份字段，保持 master 原始文本。

`source`
: 来源或 venue 信息，保持 master 原始文本。

`doi_or_url`
: master 中 `DOI / arXiv / URL` 原字段原样保存。

`doi`
: 从 `doi_or_url` 解析出的 DOI。

`url`
: 从 `doi_or_url` 保留的 URL 或原始链接文本。

`arxiv_id`
: 从 arXiv 链接中解析出的 arXiv ID；无则为空。

### 3.2 路径与存在性字段

`pdf_path`
: 正式 PDF 路径。优先取 progress 中 `pdf_path`，否则回退到 master 中 `PDF path`。

`pdf_exists`
: 布尔字段。表示 `pdf_path` 是否指向当前本地真实存在的文件。

`note_path`
: 正式 note 路径。优先取 progress 中 `note_path`，否则回退到 master 中 `Note path`。

`note_exists`
: 布尔字段。表示 `note_path` 是否指向当前本地真实存在的文件。

### 3.3 纳入与筛选字段

`is_agent`
: master 原始 `Is Agent` 字段。

`inclusion_status`
: master 原始 `Inclusion status` 字段，例如 `candidate`、`to_read`、`included`、`excluded`、`needs_review`、`background_only`。

`exclusion_reason`
: 排除原因，保持 master 原始文本。

`active_confirmed_core`
: 导出时的关键布尔字段。当前逻辑为：

1. `inclusion_status` 必须是 `to_read` 或 `included`
2. 同时必须满足：
   - `scientific_object_modules` 非空，或
   - `general_method_bucket != "none"`

这就是当前结构化层中“active confirmed core”的程序定义。

### 3.4 旧分类兼容字段

`legacy_main_class`
: master 的 `Main class` 原字段。

`legacy_secondary_class`
: master 的 `Secondary class` 原字段。

`legacy_tertiary_class`
: master 的 `Tertiary class` 原字段。

`fourth_level_topic`
: master 的 `Fourth-level topic` 原字段。

`new_fourth_level`
: master 的 `New fourth-level` 原字段。

这些字段保留用于兼容、回溯和比对，不应再被当作唯一正式分类依据。

### 3.5 标签数组字段

`agent_type_raw`
: master 原始 `Agent type` 字符串。

`agent_type`
: 由 `agent_type_raw` 按分号拆分得到的数组。

`research_workflow_role_raw`
: master 原始 `Research workflow role` 字符串。

`research_workflow_role`
: 由 `research_workflow_role_raw` 拆分得到的数组。

`validation_type_raw`
: master 原始 `Validation type` 字符串。

`validation_type`
: 由 `validation_type_raw` 拆分得到的数组。

`scientific_contribution_type_raw`
: master 原始 `Scientific contribution type` 字符串。

`scientific_contribution_type`
: 由 `scientific_contribution_type_raw` 拆分得到的数组。

这些数组在 JSON 与 SQLite 中保留真实多值语义，在 CSV 中会被压平成分号连接字符串。

### 3.6 证据与优先级字段

`evidence_strength`
: master 中的证据强度字段。

`citation_priority`
: master 中的 citation priority 字段。

`remarks`
: master 原始备注全文，也是当前若干结构化字段的解析来源之一。

`first_hand_sources_checked`
: 从 `remarks` 里的 `first_hand_sources_checked=` 解析出来的字段，表示已检查的一手来源线索。

### 3.7 正式分类字段

`scientific_object_modules`
: 正式 scientific-object module 数组，只允许 `01-11` 正式模块代码。

规则：

1. 若 `remarks` 中存在 `scientific_object_modules=`，优先使用其解析结果。
2. 若无该字段且不是 `01.04` general bucket，则可从 `legacy_main_class` 做保守回填。
3. 如果处于 `01.04` general-method bucket，则该数组应为空。

`general_method_bucket`
: 通用方法桶字段。当前 canonical 值为：

`01.04_general_asd_methods_without_concrete_object_experiments`

若不属于 general-method bucket，则值为 `none`。

`object_coverage_mode`
: 对象覆盖模式。当前常见值包括：

- `single_module`
- `multi_module`
- `general_method_without_concrete_object_experiments`

也允许保留从 `remarks` 中直接解析出的原始模式值。

`primary_module_for_filing`
: 归档主模块，仅用于 note/PDF/目录管理便利，不代表完整分类事实。

`final_modules_or_bucket_raw`
: progress 文件中的 `final_modules_or_bucket` 原始字符串。

`final_modules_or_bucket`
: 从 `final_modules_or_bucket_raw` 按分号拆分得到的数组。

说明：

1. 该字段更接近当前 reaudit 过程中的最终裁定口径。
2. 它可以包含正式模块，也可以包含 general bucket。
3. 它与 `scientific_object_modules` 不完全等价，后者更偏向结构化 formal module 数组。

### 3.8 progress 派生字段

`progress_title`
: progress 文件中的标题字段。

`pdf_status`
: progress 正式 PDF 状态字段。

`evidence_status`
: progress 正式证据状态字段。

`note_status`
: progress 中的 note 状态字段。

`master_status`
: progress 中的 master 对齐状态字段。

`source_limited`
: progress 中的来源受限字段。当前导出时会转成小写文本。

`batch`
: progress 中所属批次。

`closed`
: progress 中关闭状态字段。

### 3.9 导出追踪字段

`exported_at`
: 本轮导出 UTC 时间戳，用于追踪快照生成时间。

## 4. `taxonomy_index.json` / SQLite `taxonomy_index`

### 4.1 JSON 结构

`taxonomy_index.json` 当前保存两个映射：

`code_to_label`
: 分类代码到分类名称的映射。

`label_to_code`
: 分类名称到分类代码的反向映射。

### 4.2 SQLite 结构

SQLite `taxonomy_index` 表字段：

`code`
: 分类代码，例如 `04` 或 `01.04`。

`label`
: 分类名称。

`kind`
: 分类种类。

当前值包括：

- `formal_module`
- `general_bucket`

## 5. `pdf_manifest.json` / SQLite `pdf_inventory`

这一层只记录当前本地真实存在的 PDF。

`paper_id`
: 对应论文 ID。

`title`
: 论文标题。

`pdf_path`
: 当前本地 PDF 路径。

`sha256`
: PDF 文件内容哈希，用于校验和审计。

`primary_module_for_filing`
: PDF 当前归档主模块。

`scientific_object_modules`
: 对应论文的正式模块数组。

`pdf_status`
: progress 正式 PDF 状态。

`evidence_status`
: progress 正式证据状态。

`active_confirmed_core`
: 是否属于当前 active confirmed core。

## 6. `missing_pdf_manifest.json` / SQLite `missing_pdf_inventory`

这一层记录当前 active confirmed core 里“没有本地 PDF，但仍可索引”的论文。

`paper_id`
: 对应论文 ID。

`title`
: 论文标题。

`doi`
: DOI。

`url`
: URL。

`pdf_status`
: progress 正式 PDF 状态。

`evidence_status`
: progress 正式证据状态。

`source_limited`
: 来源受限状态。

`access_note`
: 当前导出直接复用 `remarks`，用于补充说明为什么暂无本地 PDF 或当前证据情况。

注意：

这一层不是“文献缺失清单”，而是“无本地 PDF 但可索引清单”。

## 7. `note_manifest.json` / SQLite `note_inventory`

这一层记录 note 的存在性与纳入状态。

`paper_id`
: 对应论文 ID。

`title`
: 论文标题。

`note_path`
: note 路径。

`note_exists`
: note 文件是否真实存在。

`active_confirmed_core`
: 是否属于当前 active confirmed core。

`inclusion_status`
: 当前纳入状态。

## 8. `paper_modules.csv` / SQLite `paper_modules`

这一层是把数组字段展开后的多对多关系表。

`paper_id`
: 对应论文 ID。

`title`
: 论文标题。

`assignment_scope`
: 当前展开的是哪一组分类。

当前值包括：

- `scientific_object_modules`
- `final_modules_or_bucket`

`module_code`
: 单个模块代码或 bucket 代码。

`module_kind`
: 模块类别。

当前值包括：

- `formal_module`
- `general_bucket`

`sort_order`
: 在原数组中的顺序，从 `1` 开始。

`active_confirmed_core`
: 该论文是否属于当前 active confirmed core。

## 9. SQLite 额外视图与元数据

### 9.1 `metadata`

用于记录数据库层的整体快照信息。

当前关键键包括：

- `schema_version`
- `papers_jsonl_sha256`
- `papers_record_count`
- `active_confirmed_core_count`
- `active_local_pdf_count`
- `active_no_local_pdf_count`

### 9.2 视图

`active_confirmed_core_papers`
: `papers` 表中过滤 `active_confirmed_core = 1` 的视图。

`active_missing_local_pdf`
: 当前 active confirmed core 中 `pdf_exists = 0` 的视图。

`module_assignment_counts`
: 按 `assignment_scope + module_code` 聚合后的计数视图。

字段包括：

- `assignment_scope`
- `module_code`
- `paper_count`
- `active_confirmed_core_count`

## 10. CSV 与 JSON / SQLite 的差异

为了避免误解，必须注意：

1. JSON 中的数组字段在 `papers.csv` 中会被压平成分号连接字符串。
2. SQLite 中的数组字段以 `*_json` 文本列保存 JSON 数组。
3. `paper_modules.csv` 与 SQLite `paper_modules` 是真正用于多对多统计的展开层。
4. 如果做严格统计，优先使用 SQLite 或 JSON，不要只依赖 CSV 字符串拆分。

## 11. 当前推荐用法

### 11.1 查单篇论文

优先查：

- `papers.jsonl`
- SQLite `papers`

### 11.2 查某模块全部论文

优先查：

- `paper_modules.csv`
- SQLite `paper_modules`

### 11.3 查无本地 PDF 的 confirmed core

优先查：

- `missing_pdf_manifest.json`
- SQLite `missing_pdf_inventory`
- SQLite `active_missing_local_pdf`

### 11.4 做正式统计

优先查：

- SQLite `metadata`
- SQLite `module_assignment_counts`
- SQLite `papers`

## 12. 后续扩展规则

后续如果新增字段，必须同时满足：

1. 先定义语义，再落脚本。
2. 更新本文档。
3. 若会进入 CSV/SQLite，也要同步说明其存储形式。
4. 不允许出现“脚本里有字段、文档里没有定义”的长期漂移状态。
