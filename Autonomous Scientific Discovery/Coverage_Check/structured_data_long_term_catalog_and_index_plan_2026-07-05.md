# ASD 长期分类编码、索引与资料管理执行方案

日期：2026-07-05  
适用范围：`Autonomous Scientific Discovery` 全库长期维护、后续分析、GitHub 管理、综述写作支撑  
定位：把“每篇论文分配唯一身份号、分类标签、PDF 归档、分类 index 对应、数据库化管理、支持增删改查”的要求，落实成一套可以长期遵循的项目方案。

---

## 1. 目标

本方案要解决的不是“这轮怎么临时整理一下文件”，而是建立一套以后都能持续使用的结构化管理体系。

长期目标有六个：

1. 每篇论文有稳定永久的唯一身份标识。
2. 每篇论文的科学分类以结构化字段保存，而不是散落在 note 文本里。
3. 每篇论文有可追踪的 PDF / HTML / abstract / official-page 证据状态。
4. 分类码、学科名、文件路径、PDF、note、统计数据库之间可以稳定互相映射。
5. 后续任何分析、筛选、查询、统计、表格、图表、综述写作都从同一套结构化底座出发。
6. 以后新增论文、改分类、补 PDF、改 note、导出数据，都遵守固定流程，避免漂移。

---

## 2. 核心原则

### 2.1 永久主键与学科管理码分离

必须区分两种 ID：

1. **永久主键**
   - 当前继续使用 `ASD-xxxx`
   - 这是论文的稳定身份号
   - 一旦分配，不因分类变化、目录变化、文件名变化而改变

2. **学科管理码**
   - 新增一套“排架 / 管理 / 展示”编码
   - 示例：`04-03-001`
   - 用于学科目录、表格排序、GitHub 组织、写作排架
   - 这套码一旦分配，应保持稳定，不随排序重建
   - 它**不是**永久主键

一句话：

> `ASD-xxxx` 是身份；`04-03-001` 之类的是排架位置。

补充规则：

- `discipline_local_code` 是稳定管理码，不是临时 display rank。
- 新增论文默认在对应二级位下追加最大编号 + 1。
- 如果论文主排架位发生变化，旧码不得静默复用，应进入 `retired_code` / `redirected_code` 状态，并生成新码。
- 如果只是为了临时排序，应使用 `discipline_display_order`，不能复用 `discipline_local_code` 这个字段名。

### 2.2 分类事实与排架展示分离

必须区分两种分类：

1. **事实分类**
   - 论文真正属于哪些科学对象模块
   - 当前由 `scientific_object_modules` 和 `general_method_bucket` 表示
   - 允许多模块

2. **排架展示分类**
   - 论文主要放在哪个学科目录下管理
   - 当前由 `primary_module_for_filing` 和后续新增的二级排架码表示
   - 一篇论文只能有一个主排架位

一句话：

> 事实分类可以多选，排架位置只能有一个。

### 2.3 四类事实源与 derived layer 分离

后续必须区分四类事实源，而不是让 derived registry 承担事实源角色。

1. **文献与分类事实源**
   - `Paper_Lists/agent_master_paper_list.md`
   - 负责论文元数据、纳入状态、科学对象分类、legacy class、主排架位等内容事实。

2. **资料与核查事实源**
   - `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
   - 负责 PDF / HTML / abstract / official-page 证据状态、source-limited 状态、progress closeout 状态。

3. **系统管理码事实源**
   - `Data/discipline_code_assignments.jsonl`
   - 负责稳定 `discipline_local_code` 的分配历史、active_code / retired_code / redirected_code / pending_secondary / non_discipline_general_method 状态。
   - 它只管理“排架管理码”，不覆盖论文元数据、分类事实或资料核查事实。

4. **taxonomy vocabulary 事实源**
   - `Data/classification_code_index.json`
   - 负责一级 / 二级分类词表、定义、纳入边界、排除边界、状态和来源。
   - 它管理“分类术语定义”，不管理某篇论文具体分到哪里。

一句话：

> master 和 progress 仍是论文内容与核查状态的 authoritative pair；`discipline_code_assignments.jsonl` 是稳定管理码账本；`classification_code_index.json` 是 taxonomy vocabulary owner；registry / CSV / SQLite 是 derived layer。

以后新增任何展示 registry、index、CSV、SQLite 表，都属于 derived layer；只有明确列入字段归属矩阵的账本文件才能成为特定字段的 owner。

### 2.4 字段归属必须先写死

在实现任何新增编码导出前，必须先维护一份字段归属矩阵。

建议文件：

```text
Data/field_ownership_matrix.md
```

最低要求：

- 每个核心字段只能有一个 owner
- registry / CSV / SQLite 只能派生，不可手工成为事实源
- note 可以解释事实，但不能覆盖 master / progress
- 字段冲突时，必须回到 owner 文件修正，再重新 export

初始 ownership 原则：

| 字段类型 | 唯一 owner | 说明 |
|---|---|---|
| `paper_id`、title、authors、year、venue、DOI / URL | master | note / registry 只能引用 |
| `scientific_object_modules`、`general_method_bucket`、`object_coverage_mode`、`primary_module_for_filing` | master-derived canonical lane | source file 必须是 master；field matrix 中要写清 source columns / structured remark tokens / fallback order / source confidence |
| `legacy_main_class`、`legacy_secondary_class`、`legacy_tertiary_class` | master | 第一阶段二级排架来源 |
| `pdf_status`、`evidence_status`、`source_limited`、`closed` | progress | note 只能解释 |
| `note_path`、`pdf_path` | current export resolution from master / progress | 需要在 field matrix 中固定 fallback 优先级 |
| `discipline_local_code`、`assignment_status`、`assigned_at`、`retired_at`、`redirected_to_code` | `Data/discipline_code_assignments.jsonl` | 稳定管理码账本，不由 export 每次重排生成 |
| taxonomy term label、definition、include / exclude boundary、term status、term source | `Data/classification_code_index.json` | taxonomy vocabulary owner，不是普通 derived index |

`master-derived canonical lane` 必须在 `Data/field_ownership_matrix.md` 中具体化为：

```text
source_file: Paper_Lists/agent_master_paper_list.md
fallback_order:
  1. explicit canonical field
  2. structured remark token
  3. legacy class fallback
  4. mark as needs_review
required_trace_fields:
  - source_field
  - source_confidence
  - parser_rule
```

### 2.5 找不到 PDF 时不硬啃

后续仍严格遵守当前规则：

- 实在找不到主文 PDF，就不要反复浪费时间
- 只要 HTML / abstract / official page / supplementary 足以证明文献真实存在且可索引，就允许保留 `source_limited=yes`
- 不伪装成 full text checked
- 不因为资料受限就乱改分类

---

## 3. 我们最终要落实的对象

你学长说的那段话，落实下来，实际上要做的是下面这九层。

### 3.1 永久论文主键层

继续使用：

- `paper_id = ASD-0001 ... ASD-9999`

要求：

- 永久不变
- 全项目唯一
- 出现在 master、progress、notes、Data、SQLite、导出表、Git 提交说明中

### 3.2 科学对象分类事实层

继续使用当前 canonical 字段：

- `scientific_object_modules`
- `general_method_bucket`
- `object_coverage_mode`
- `primary_module_for_filing`

要求：

- `scientific_object_modules` 用数组保存
- `01.04` 继续只放在 `general_method_bucket`
- 不把 `primary_module_for_filing` 误当作完整分类事实

### 3.3 二级学科排架层

新增一个更适合目录管理与分析的二级学科层。

建议字段：

- `primary_taxonomy_code_2lvl`
  - 示例：`04.03`
- `discipline_local_code`
  - 示例：`04-03-001`
- `discipline_local_rank`
  - 示例：`001`
- `assignment_status`
  - 示例：`active_code` / `retired_code` / `redirected_code` / `pending_secondary` / `non_discipline_general_method`
- `assigned_at`
- `retired_at`
- `previous_discipline_local_code`
- `redirected_to_code`
- `assignment_reason`
- `pending_reason`

这层的作用：

- GitHub 目录管理
- 人工查找
- 表格排序
- 章节代表论文编组
- 后续学科统计

这层必须拆成两种文件角色：

- 稳定账本：`Data/discipline_code_assignments.jsonl`
- 派生展示：`Data/discipline_local_code_registry.jsonl` / `.csv` / SQLite table

### 3.4 PDF / 资料证据层

每篇论文都要有结构化资料状态：

- 是否有本地 PDF
- PDF 是主文还是 supplementary
- 是否只核对了 abstract / HTML / official page
- 是否 `source_limited=yes`
- PDF / source 证据类型
- 是否全文核对

要求：

- 继续以 progress 为主导
- 不把 `pdf_path` 非空误当作“已读全文”
- supplementary PDF 必须显式标注为 supplementary

建议逐步补充的派生字段：

- `pdf_evidence_type`
  - `main_pdf`
  - `supplementary_pdf`
  - `html_full_text`
  - `abstract`
  - `official_page`
  - `project_page`
- `pdf_check_status`
  - `full_text_checked`
  - `source_limited`
  - `metadata_only`
- `asset_sha256`
- `asset_size_bytes`
- `asset_type`
- `is_main_text`
- `is_supplementary`
- `source_checked_at`

### 3.5 Note 层

每篇论文继续保留一份 note。

note 的职责：

- 保存人工解释
- 保存分类依据
- 保存证据日志
- 保存对综述写作的价值判断

note 不是数据库，但必须和数据库字段一致。

### 3.6 Registry 层

我们已经有：

- `paper_registry.jsonl`
- `classification_assignments.jsonl`
- `paper_identifier_aliases.jsonl`
- `pdf_archive_registry.jsonl`
- `asset_manifest.jsonl`

后续新增：

- `discipline_code_assignments.jsonl`
- `discipline_local_code_registry.jsonl`

作用：

- `discipline_code_assignments.jsonl` 做稳定 code 分配账本
- `discipline_local_code_registry.jsonl` 做连接层和展示快照
- 让 analysis / SQL / CSV 不必每次重新解析 markdown

重要边界：

- `discipline_code_assignments.jsonl` 可以人工审查和增量维护，但不能保存论文分类事实。
- `discipline_local_code_registry.jsonl` 每次 export 可覆盖重建，不能手工当成事实源。

### 3.7 Index 层

必须有两套 index。

1. **永久 taxonomy index**
   - 数字和一级分类 / 特殊 bucket 的映射
   - 已有：`taxonomy_index.json`

2. **扩展学科编码 index**
   - 一级、二级、排架码的映射
   - 将新增：
     - `classification_code_index.json`
   - 不能只保存 code-label 映射，还应保存定义、纳入边界、排除边界、状态和来源

### 3.8 Analysis 层

继续用：

- `papers.jsonl`
- `papers.csv`
- `canonical_paper_modules.csv`
- `papers.sqlite`

并新增：

- `discipline_local_code_registry.csv`

作用：

- 后续做统计、筛选、SQL 查询、图表、章节抽样

SQLite 至少应区分以下表：

- `papers`
- `paper_modules`
- `paper_general_method_buckets`
- `discipline_code_assignments`
- `discipline_local_code_registry`
- `classification_terms`
- `pdf_evidence_status`
- `paper_assets`
- `notes`

其中 `paper_modules` 必须是多对多关系表，不能只把数组塞进 `papers` 的一个字符串字段。

### 3.9 GitHub 管理层

GitHub 上最终按以下逻辑管理：

- 主身份仍然按 `ASD-xxxx`
- 目录按 `primary_module_for_filing` 放
- 表格 / registry / index 决定跨目录导航
- PDF 和 note 不要求因为编码升级而立刻全部改名

一句话：

> GitHub 管目录，registry 管映射，数据库管查询，四类事实源管真值。

---

## 4. 编码体系设计

## 4.1 一级科学对象码

继续沿用：

- `01` 形式、信息与计算科学
- `02` 物理学、天文学与宇宙科学
- `03` 化学科学
- `04` 材料科学
- `05` 地球与环境科学
- `06` 生命科学
- `07` 医学与健康科学
- `08` 农业、食品、林业、畜牧与渔业科学
- `09` 工程与工业技术科学
- `10` 航空、航天、海洋与交通科学
- `11` 社会、行为、经济与知识系统科学
- `01.04` 独立 general-method bucket

## 4.2 二级学科码

建议把当前已有的 legacy `Secondary class` 作为第一阶段二级位来源。

例如：

- `04.03`
- `11.07`
- `06.03`

这意味着：

- 第一阶段不重新发明完整二级树
- 直接把现有仓库里已经稳定使用的二级位显式结构化导出
- 同时必须显式标注这些二级位仍是 `legacy` 来源，不得伪装成已完全 canonical 的规范二级 taxonomy

建议新增字段：

- `secondary_class_source`
  - `legacy`
  - `normalized`
  - `manual_override`
- `secondary_class_confidence`
  - `high`
  - `medium`
  - `low`
- `secondary_class_review_status`
  - `unreviewed`
  - `reviewed`
  - `needs_split`
  - `needs_merge`

## 4.3 学科管理码

建议格式：

```text
MM-SS-NNN
```

其中：

- `MM` = 一级模块，例如 `04`
- `SS` = 二级位，例如 `03`
- `NNN` = 该二级位下顺序号，例如 `001`

示例：

- `04-03-001`
- `11-07-013`
- `06-03-042`

稳定性规则：

- `discipline_local_code` 一旦进入 `Data/discipline_code_assignments.jsonl`，不因排序、年份、标题或新增论文自动重排。
- 同一 active code 不得指向多篇论文。
- 已分配 code 如果不再适用，应保留历史记录并标记 `retired_code` 或 `redirected_code`。
- 如果暂时只需要展示排序，另用 `discipline_display_order`，不污染稳定管理码。
- export 脚本不能“凭空重算稳定 code”，只能读取账本并生成 derived registry。

## 4.4 多模块论文如何处理

规则必须写死：

- 多模块事实仍保留在 `scientific_object_modules`
- `discipline_local_code` 只分配一个 active code
- 它跟随 `primary_module_for_filing`
- 二级位优先采用该主排架位下的 `legacy_secondary_class`

例如一篇 `06;07` 多模块论文：

- 事实层：`scientific_object_modules = ["06", "07"]`
- 排架层：`primary_module_for_filing = 06`
- 管理码：例如 `06-03-017`

## 4.5 主排架位选择规则

`primary_module_for_filing` 的判定优先级必须固定，尤其用于多模块论文。

建议优先级：

1. 论文实际解决的科学对象问题。
2. 实验验证、benchmark task 或 case study 的主要对象。
3. 论文贡献最直接服务的学科对象。
4. 如果是通用平台 / 方法论文，以最实质的应用对象为准。
5. 如果仍无法判断，标记 `primary_module_confidence=low`，并写入 `primary_module_override_reason`。

建议派生 / 记录字段：

- `primary_module_confidence`
- `primary_module_assignment_rule`
- `primary_module_override_reason`

## 4.6 pending code 规则

如果二级位不明确，禁止生成看起来像真实分类的假 code。

标准记录：

```text
primary_taxonomy_code_2lvl = null
discipline_local_code = null
assignment_status = pending_secondary
pending_reason = "missing_or_uncertain_secondary_class"
```

禁止使用：

```text
04-00-001
MM-XX-PENDING
```

如果只是为了展示排序，应使用 `discipline_display_order`，不要污染稳定管理码。

## 4.7 pure general-method 论文规则

如果论文只有：

```text
general_method_bucket = 01.04
scientific_object_modules = []
```

则第一阶段不强行塞入 formal `01`，也不分配普通 `MM-SS-NNN` 管理码。

标准记录：

```text
primary_taxonomy_code_2lvl = null
discipline_local_code = null
assignment_status = non_discipline_general_method
pending_reason = null
```

后续如果确实需要为 general-method-only 论文建立单独排架，可另行设计 `GM-xx-NNN` 或 `general_method_registry`，但当前阶段不急于引入，避免污染科学对象分类体系。

---

## 5. 要新增的结构化文件

## 5.1 `Data/classification_code_index.json`

作用：

- 保存一级码、二级码、学科名、目录名、显示顺序、逆向映射

建议结构：

```json
{
  "primary_code_to_label": {},
  "secondary_code_to_label": {},
  "label_to_primary_code": {},
  "label_to_secondary_code": {},
  "secondary_terms": [
    {
      "secondary_code": "04.03",
      "parent_primary_code": "04",
      "label": "",
      "definition": "",
      "include": [],
      "exclude": [],
      "status": "active",
      "source": "legacy_secondary_class"
    }
  ]
}
```

## 5.2 `Data/discipline_code_assignments.jsonl`

作用：

- 保存稳定 `discipline_local_code` 的分配历史
- 防止每次 export 重排导致 code drift
- 支持 active_code / retired_code / redirected_code / pending_secondary / non_discipline_general_method 状态

每个 code assignment 一行。

建议字段：

- `assignment_id`
- `paper_id`
- `discipline_local_code`
- `primary_taxonomy_code_2lvl`
- `assignment_status`
  - `active_code`
  - `retired_code`
  - `redirected_code`
  - `pending_secondary`
  - `non_discipline_general_method`
- `assigned_at`
- `assigned_by`
- `retired_at`
- `redirected_to_code`
- `assignment_reason`
- `pending_reason`
- `source_primary_module_for_filing`
- `source_legacy_secondary_class`
- `schema_version`

示例：

```json
{
  "assignment_id": "DCA-000001",
  "paper_id": "ASD-0123",
  "discipline_local_code": "04-03-017",
  "primary_taxonomy_code_2lvl": "04.03",
  "assignment_status": "active_code",
  "assigned_at": "2026-07-05",
  "assigned_by": "codex",
  "retired_at": null,
  "redirected_to_code": null,
  "assignment_reason": "initial_assignment",
  "pending_reason": null,
  "source_primary_module_for_filing": "04",
  "source_legacy_secondary_class": "04.03",
  "schema_version": 1
}
```

这个文件不是普通 derived file。它是系统管理码当前状态账本，可以增量维护，但修改必须经过 check，并在 git 中留下可审计记录。

状态语义：

- `discipline_code_assignments.jsonl` 采用“当前状态账本 + `Data/change_log.jsonl` 辅助审计”，不是复杂事件溯源。
- 一篇论文可以有多行 assignment 历史记录。
- 同一篇论文最多只能有一条 `assignment_status=active_code`。
- `active_code` / `retired_code` / `redirected_code` 必须有非空 `discipline_local_code`。
- `pending_secondary` / `non_discipline_general_method` 必须有空 `discipline_local_code`。
- `redirected_to_code` 指向目标 active `discipline_local_code`，不指向 `paper_id`。
- 旧 code 不删除；主排架位改变时旧行改为 `retired_code` 或 `redirected_code`，再新增一条 active assignment。

## 5.3 `Data/discipline_code_assignment_policy.md`

作用：

- 单独规定 code 如何初始分配
- 如何追加编号
- 如何 retired_code / redirected_code
- 如何处理 pending secondary
- 如何处理 pure general-method records
- 如何防止 code reuse

## 5.4 `Data/primary_filing_policy.md`

作用：

- 单独规定多模块论文如何选择 `primary_module_for_filing`
- 保存主排架位选择优先级、confidence、override reason 规则

## 5.5 `Data/discipline_code_initial_assignment_preview.csv`

作用：

- 在正式冻结 `discipline_code_assignments.jsonl` 之前，先生成初始 code 分配预览
- 支持人工审查 secondary class 缺失、多模块主排架位、general-method-only、source_limited、legacy class 异常
- 避免一开始就把大量错误写进长期账本，减少后续 retired_code / redirected_code 噪音

流程：

1. 生成 preview。
2. 人工审查。
3. 回到 master / progress / classification index 修正源事实。
4. 再生成正式 `discipline_code_assignments.jsonl`。
5. 冻结 `initial_assignment`。

## 5.6 `Data/schema/*.schema.json`

建议新增：

- `Data/schema/discipline_code_assignments.schema.json`
- `Data/schema/classification_code_index.schema.json`

作用：

- 校验 JSONL / JSON 字段名、必填字段、枚举值和 schema version
- 防止 `assignment_status`、`redirected_to_code` 等字段发生拼写漂移

## 5.7 `Data/check_policy.md`

作用：

- 定义 check severity：`ERROR` / `WARNING` / `INFO`
- 明确哪些问题阻断 build / commit，哪些进入 backlog，哪些只记录状态

## 5.8 `Data/discipline_local_code_registry.jsonl`

每篇论文一行。

建议字段：

- `paper_id`
- `discipline_local_code`
- `discipline_local_rank`
- `assignment_status`
- `assigned_at`
- `retired_at`
- `previous_discipline_local_code`
- `primary_module_for_filing`
- `primary_taxonomy_code_2lvl`
- `legacy_secondary_class`
- `scientific_object_modules`
- `general_method_bucket`
- `title`
- `note_path`
- `pdf_path`
- `active_confirmed_core`

字段分层要求：

- code assignment 字段来自 `Data/discipline_code_assignments.jsonl`
- `discipline_local_rank = parse_NNN(discipline_local_code)`，只能派生，不允许人工维护
- 冗余展示字段：`title`、`scientific_object_modules`、`note_path`、`pdf_path`
- 冗余展示字段必须由脚本覆盖生成，并在 README 中标明 `derived_snapshot`
- registry 应包含 `is_derived_snapshot=true`、`generated_at`、`generated_by`、`source_commit`

`discipline_local_code_registry.jsonl` 是 derived snapshot，可以由 export 覆盖重建，不得手工当作事实源。

## 5.9 `Data/discipline_local_code_registry.csv`

作用：

- 表格审查
- 人工筛选
- 导出给写作与汇报使用

## 5.10 `SQLite` 新表或视图

建议至少新增 / 明确：

- `papers`
- `paper_modules`
- `paper_general_method_buckets`
- `discipline_code_assignments`
- `discipline_local_code_registry`
- `classification_terms`
- `pdf_evidence_status`
- `paper_assets`
- `notes`

后续查询可以直接回答：

- 某一级/二级学科下有哪些论文
- 某个排架位下编号顺序是什么
- 某个二级位里哪些论文没有本地 PDF
- 某个二级位里哪些论文是多模块

其中关键关系表：

```text
paper_modules(
  paper_id,
  module_code,
  is_primary_for_filing,
  confidence,
  source
)
```

以及：

```text
discipline_code_assignments(
  assignment_id,
  paper_id,
  discipline_local_code,
  primary_taxonomy_code_2lvl,
  assignment_status,
  assigned_at,
  retired_at,
  redirected_to_code,
  assignment_reason
)
```

---

## 6. 要新增的脚本能力

## 6.1 扩展 `export_structured_data.py`

新增导出逻辑：

1. 读取每篇论文的：
   - `paper_id`
   - `scientific_object_modules`
   - `general_method_bucket`
   - `primary_module_for_filing`
   - `legacy_secondary_class`
2. 读取稳定 code 账本：
   - `Data/discipline_code_assignments.jsonl`
3. 生成 derived snapshot：
   - `primary_taxonomy_code_2lvl`
   - `discipline_local_rank`
   - `discipline_local_code`
   - `discipline_display_order`
4. 写出：
   - `classification_code_index.json`
   - `discipline_local_code_registry.jsonl`

注意：

- 第一版必须先生成 `Data/discipline_code_initial_assignment_preview.csv`。
- preview 经人工审查并修正源事实后，才允许写入一次性 `initial_assignment` 账本。
- `initial_assignment` 写入 `Data/discipline_code_assignments.jsonl` 后即冻结，不再由 export 全量重排。
- 后续新增论文应在对应二级位下追加最大编号 + 1。
- 如果二级位不明确，写入 `pending_secondary`，不生成假 code。
- 如果是 pure general-method-only，写入 `non_discipline_general_method`，不生成普通学科 code。
- export 只读取 code assignment ledger 并生成 registry，不直接决定稳定 code 历史。
- export 应读取 `classification_code_index.json` 校验 taxonomy term 合法性。
- export 写出的 registry 应标记 `is_derived_snapshot=true`、`generated_at`、`generated_by`、`source_commit`。

## 6.2 扩展 `build_analysis_db.py`

新增：

- 把 `discipline_code_assignments` 写入 SQLite
- 把 `discipline_local_code_registry` 写入 SQLite
- 导出 `discipline_local_code_registry.csv`
- 明确生成 `paper_modules` 多对多表
- 明确生成 `paper_general_method_buckets` 表
- 明确生成 `pdf_evidence_status`、`paper_assets`、`notes` 表或视图

SQLite 逻辑约束：

- `papers.paper_id` 是 primary key
- `paper_modules` 使用 `(paper_id, module_code)` 作为 primary key
- `discipline_code_assignments.assignment_id` 是 primary key
- `active_code` 的 `discipline_local_code` 全库唯一
- 同一 `paper_id` 最多一条 `active_code`
- `pending_secondary` 与 `non_discipline_general_method` 的 `discipline_local_code` 必须为 null

SQLite 对复杂约束支持有限时，由 `check_data_consistency.py` 强制执行。

## 6.3 可选扩展查询命令

后续可以在 `query_analysis_db.py` 增加：

- `discipline-code-summary`
- `discipline-code <code>`
- `secondary-class-summary`
- `secondary-class-pdf-coverage`

## 6.4 扩展校验脚本

必须扩展现有 `check_data_consistency.py`，或新增专门完整性检查脚本。

check report 必须区分 severity：

- `ERROR`：必须修复，否则不能 build / commit
- `WARNING`：可暂时保留，但必须进入 backlog
- `INFO`：只记录状态，不阻断流程

建议检查项：

ERROR 示例：

- `paper_id` 重复或格式非法
- master 与 progress 无法回连
- active paper 缺 note path 或 note 文件不存在
- `pdf_path` 非空但文件不存在
- supplementary PDF 被标记为 main PDF full-text
- `scientific_object_modules` 非法
- `primary_module_for_filing` 不属于 `scientific_object_modules` 且没有明确 override reason
- `assignment_status=active_code` 的 `discipline_local_code` 重复
- 同一 `paper_id` 有多条 `active_code`
- `retired_code` 被复用
- `redirected_code` 的 `redirected_to_code` 未指向合法 active code
- `pending_secondary` 有普通 `MM-SS-NNN` code
- `non_discipline_general_method` 有普通 `MM-SS-NNN` code
- `discipline_code_assignments.jsonl` 中的 `paper_id` 无法回连 master
- `01.04` 进入 formal `scientific_object_modules`
- derived Data 层不能由 export / build 重建
- `discipline_code_assignments.jsonl` 被 export 覆盖重建

WARNING 示例：

- `secondary_class_confidence=low`
- `primary_module_confidence=low`
- `source_limited=yes`
- missing PDF but has official page
- pending secondary 记录需要人工补二级位

INFO 示例：

- `background_only`
- `non_discipline_general_method`
- supplementary-only source state

建议输出：

```text
Data/integrity_check_report.md
```

## 6.5 变更审计

长期建议新增轻量变更日志：

```text
Data/change_log.jsonl
```

最低字段：

- `change_id`
- `paper_id`
- `changed_at`
- `changed_by`
- `change_type`
- `old_value`
- `new_value`
- `reason`
- `related_commit`

第一阶段不必覆盖所有字段，但分类改变、PDF/source 状态改变、record status 改变应优先记录。

## 6.6 生命周期状态

长期维护还需要显式生命周期字段。

建议逐步结构化：

- `record_status`
  - `candidate`
  - `active_confirmed_core`
  - `background_only`
  - `excluded`
  - `duplicate`
  - `retired`
- `inclusion_decision`
- `exclusion_reason`
- `duplicate_of`
- `last_reviewed_at`
- `last_reviewed_by`

当前可以先由现有 `inclusion_status` 与 `active_confirmed_core` 派生，后续再决定是否升级为 authoritative 字段。

---

## 7. 长期执行流程

以后长期维护按下面流程。

## 7.1 新增论文

1. 在 master 新增论文行
2. 分配新的 `ASD-xxxx`
3. 指定初始 note path、primary module、secondary class
4. 建 note
5. 建 progress 行
6. 如果是初始全库分配阶段，先进入 `Data/discipline_code_initial_assignment_preview.csv`
7. 如果是日常新增阶段，在 `Data/discipline_code_assignments.jsonl` 增量追加 code assignment
8. 跑：
   - `export`
   - `check`
   - `build`
9. 由 export 生成该论文的 derived registry / CSV / SQLite 记录

新增论文的 code 分配必须遵守：

- 在对应二级位下追加编号
- 不重排既有 active code
- 如果二级位暂不明确，使用 `assignment_status=pending_secondary`，不伪造精确二级码
- 如果是 pure general-method-only，使用 `assignment_status=non_discipline_general_method`，不分配普通学科 code

## 7.2 改分类

1. 改对应事实源：
   - 论文 / 分类事实改 master
   - PDF / source 状态改 progress
   - 稳定 code 历史改 `discipline_code_assignments.jsonl`
2. 不手改 derived Data；若需要改 code 历史，只改 `discipline_code_assignments.jsonl` 并保留理由
3. 跑：
   - `export`
   - `check`
   - `build`
4. 如果主排架位改变：
   - 旧 `discipline_local_code` 标记为 `retired_code` / `redirected_code`
   - 新主排架位分配新 code
   - 保留变更理由
5. 如果只是事实多模块数组微调、主排架位不变，原 `discipline_local_code` 保持不变

## 7.3 补 PDF

1. 补 `Reference_PDF/`
2. 改 progress 的 PDF / evidence 状态
3. 必要时刷新 note
4. 跑：
   - `export`
   - `check`
   - `build`

## 7.4 改 note

1. 先确认是否会影响 authoritative facts
2. 如果只是 wording / evidence log，同步 note 即可
3. 如果影响分类 / source state，必须先改 master 或 progress

## 7.5 提交纪律

每轮结束后：

1. `git status`
2. `export -> check -> build`
3. 如果涉及 code，确认 `discipline_code_assignments.jsonl` 的 diff 可解释
4. 写 closeout
5. 提交 git
6. 再次确认 worktree 干净

---

## 8. GitHub 管理建议

## 8.1 目录管理

继续按一级目录放：

- `Notes/01_*`
- `Notes/02_*`
- ...
- `Reference_PDF/01_*`
- ...

## 8.2 文件名管理

当前不建议立刻做全库重命名。

原因：

- 会污染 Git 历史
- 成本高
- 分析收益低

长期建议：

- 保留当前 note / PDF 文件名风格
- 用 registry 和 index 负责“编号到文件”的映射

## 8.3 GitHub 导航层

以后如果需要更强导航，可以再补：

- `Paper_Lists/by_discipline_code.md`
- `Data/discipline_local_code_registry.csv`
- 自动生成的学科目录索引页

---

## 9. 我们下一步按什么顺序落实

这是推荐执行顺序。

## 第一步：写字段归属矩阵

新增：

- `Data/field_ownership_matrix.md`

先定 owner，再写脚本。

## 第二步：写 code assignment policy 与 primary filing policy

新增：

- `Data/discipline_code_assignment_policy.md`
- `Data/primary_filing_policy.md`

先把 code 增量分配、retired_code / redirected_code、pending、general-method-only、主排架位选择规则写死。

## 第三步：写 schema 与 check policy

新增：

- `Data/schema/discipline_code_assignments.schema.json`
- `Data/schema/classification_code_index.schema.json`
- `Data/check_policy.md`

先锁定 assignment schema、taxonomy index schema、ERROR / WARNING / INFO 规则。

## 第四步：冻结编码规则

冻结：

- `ASD-xxxx` 保留为永久主键
- `discipline_local_code` 作为二级管理码
- 管理码格式：`MM-SS-NNN`
- 管理码稳定，不自动重排
- 旧码支持 retired_code / redirected_code 状态
- pending secondary 与 non-discipline general-method 不生成普通学科 code
- `code_status` 不再使用，统一使用 `assignment_status`

## 第五步：生成 initial assignment preview

新增：

- `Data/discipline_code_initial_assignment_preview.csv`

先审查 preview，重点看 secondary class 缺失、多模块主排架位、general-method-only、source_limited、legacy class 异常。

## 第六步：创建稳定 code assignment ledger

新增：

- `Data/discipline_code_assignments.jsonl`

第一版只做 `initial_assignment`，完成后冻结，后续新增论文只追加，不重排旧 code。

## 第七步：做 index

新增：

- `classification_code_index.json`

要求：

- 包含 code-label
- 包含 definition / include / exclude / status / source

## 第八步：做 registry

新增：

- `discipline_local_code_registry.jsonl`
- `discipline_local_code_registry.csv`

它们从 master + progress + `discipline_code_assignments.jsonl` 派生，可覆盖重建。

## 第九步：扩展校验

新增：

- `discipline_local_code` 唯一性检查
- code ledger active_code / retired_code / redirected_code / pending_secondary 检查
- `assignment_status` 语义检查
- ERROR / WARNING / INFO severity
- 路径存在性检查
- 分类合法性检查
- owner / derived layer guardrail

## 第十步：接入 SQLite

新增或明确：

- `papers`
- `paper_modules`
- `paper_general_method_buckets`
- `discipline_code_assignments`
- `discipline_local_code_registry`
- `pdf_evidence_status`
- `paper_assets`
- `notes`

## 第十一步：小批量试运行

先选 20-30 篇覆盖不同边界：

- 单模块
- 多模块
- 缺 PDF
- supplementary-only
- source_limited
- pure general-method
- pending secondary

小批量 check report 稳定后，再跑全库。

## 第十二步：写文档与查询说明

更新：

- `Data/README.md`
- 必要时补 query 示例

## 第十三步：后续再考虑是否升级到更强二级 canonical 层

只有当正文写作和分析稳定需要时，再决定是否把二级位进一步升级为更强事实层。

---

## 10. 明确哪些事情现在不做

为了避免返工，下面这些事情当前不做：

1. 不废弃 `ASD-xxxx`
2. 不把 `0101abc` 这种学科码当作唯一主键
3. 不全库重命名 note / PDF 文件
4. 不手改 derived `Data/` 文件；`discipline_code_assignments.jsonl` 作为账本只能按 policy 增量维护
5. 不把多模块论文拆成多个永久 ID
6. 不因为想做排架编码，就重做 master / progress 中的论文事实
7. 不让 derived registry 承担稳定 code 事实源角色
8. 不为 pending secondary 生成 `04-00-001` 这类假精确 code
9. 不把 pure `01.04` general-method-only 论文强行塞进 formal scientific-object module

---

## 11. 一句话版本

> 我们下一步不是重建数据库，而是在现有 `ASD-xxxx + 分类数组 + registry + SQLite` 底座上，先补稳定 `discipline_code_assignments.jsonl` 账本，再派生“一级/二级学科排架编码层”，把论文身份、分类事实、排架管理、PDF 归档、索引映射和后续分析彻底接起来。

---

## 12. 执行定义

当下面条件满足时，可以认为“学长说的这套长期结构化管理逻辑”已经落实：

1. 永久主键 `ASD-xxxx` 保持稳定。
2. 每篇论文有结构化分类数组。
3. 每篇论文有结构化资料状态。
4. 一级 / 二级分类码有正式 index 文件。
5. 每篇论文有 code assignment record；符合学科排架条件的论文有 active `discipline_local_code`。
6. 稳定 code assignment 已进入 `Data/discipline_code_assignments.jsonl`，且 active_code / retired_code / redirected_code / pending_secondary / non_discipline_general_method 状态可审计。
7. `classification_code_index.json` 被明确为 taxonomy vocabulary owner。
8. `discipline_code_initial_assignment_preview.csv` 已在正式账本冻结前完成审查。
9. `discipline_local_code_registry` 已从账本导出到 JSONL / CSV / SQLite，并标记 derived snapshot metadata。
10. 字段归属矩阵、schema 和 check policy 已经冻结并被 README 引用。
11. 校验脚本能按 ERROR / WARNING / INFO 检查 paper ID、code、路径、分类、PDF/source 状态的基本完整性。
12. 后续任何增删改查都遵守 owner fact source -> export -> check -> build 的流程。
