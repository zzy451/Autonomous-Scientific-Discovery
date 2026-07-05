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
- 如果论文主排架位发生变化，旧码不得静默复用，应进入 retired / redirected 状态，并生成新码。
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

### 2.3 authoritative pair 不变

结构化事实层继续只有两份 authoritative 文件：

1. `Paper_Lists/agent_master_paper_list.md`
2. `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

以后新增任何编码导出、索引、CSV、JSONL、SQLite 表，都属于 derived layer，不是新事实源。

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
| `scientific_object_modules`、`general_method_bucket`、`object_coverage_mode`、`primary_module_for_filing` | master-derived canonical lane | 当前由 master remarks / legacy fallback 导出 |
| `legacy_main_class`、`legacy_secondary_class`、`legacy_tertiary_class` | master | 第一阶段二级排架来源 |
| `pdf_status`、`evidence_status`、`source_limited`、`closed` | progress | note 只能解释 |
| `note_path`、`pdf_path` | current export resolution from master / progress | 需要在 field matrix 中固定 fallback 优先级 |
| `discipline_local_code`、`code_status` | generated registry or future code registry | 不手写进 note 作为真值 |

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
- `code_status`
  - 示例：`active` / `retired` / `redirected`
- `assigned_at`
- `retired_at`
- `previous_discipline_local_code`

这层的作用：

- GitHub 目录管理
- 人工查找
- 表格排序
- 章节代表论文编组
- 后续学科统计

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

- `discipline_local_code_registry.jsonl`

作用：

- 做连接层
- 让 analysis / SQL / CSV 不必每次重新解析 markdown

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

### 3.9 GitHub 管理层

GitHub 上最终按以下逻辑管理：

- 主身份仍然按 `ASD-xxxx`
- 目录按 `primary_module_for_filing` 放
- 表格 / registry / index 决定跨目录导航
- PDF 和 note 不要求因为编码升级而立刻全部改名

一句话：

> GitHub 管目录，registry 管映射，数据库管查询，authoritative pair 管事实。

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

- `discipline_local_code` 一旦进入 registry，不因排序、年份、标题或新增论文自动重排。
- 同一 active code 不得指向多篇论文。
- 已分配 code 如果不再适用，应保留历史记录并标记 `retired` 或 `redirected`。
- 如果暂时只需要展示排序，另用 `discipline_display_order`，不污染稳定管理码。

## 4.4 多模块论文如何处理

规则必须写死：

- 多模块事实仍保留在 `scientific_object_modules`
- `discipline_local_code` 只生成一个
- 它跟随 `primary_module_for_filing`
- 二级位优先采用该主排架位下的 `legacy_secondary_class`

例如一篇 `06;07` 多模块论文：

- 事实层：`scientific_object_modules = ["06", "07"]`
- 排架层：`primary_module_for_filing = 06`
- 管理码：例如 `06-03-017`

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

## 5.2 `Data/discipline_local_code_registry.jsonl`

每篇论文一行。

建议字段：

- `paper_id`
- `discipline_local_code`
- `discipline_local_rank`
- `code_status`
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

- registry 自有字段：`paper_id`、`discipline_local_code`、`discipline_local_rank`、`code_status`、`assigned_at`
- 冗余展示字段：`title`、`scientific_object_modules`、`note_path`、`pdf_path`
- 冗余展示字段必须由脚本覆盖生成，并在 README 中标明 `derived_snapshot`

## 5.3 `Data/discipline_local_code_registry.csv`

作用：

- 表格审查
- 人工筛选
- 导出给写作与汇报使用

## 5.4 `SQLite` 新表或视图

建议新增：

- `discipline_local_code_registry`

后续查询可以直接回答：

- 某一级/二级学科下有哪些论文
- 某个排架位下编号顺序是什么
- 某个二级位里哪些论文没有本地 PDF
- 某个二级位里哪些论文是多模块

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
2. 生成：
   - `primary_taxonomy_code_2lvl`
   - `discipline_local_rank`
   - `discipline_local_code`
3. 写出：
   - `classification_code_index.json`
   - `discipline_local_code_registry.jsonl`

注意：

- 第一版可以从当前 row order 生成初始 active code。
- 后续一旦 code registry 落地，新增论文应追加编号，而不是全量重排编号。
- 如果暂时无法实现稳定增量分配，必须在文档中把第一版标为 `initial_assignment`，并在进入人工引用前冻结。

## 6.2 扩展 `build_analysis_db.py`

新增：

- 把 `discipline_local_code_registry` 写入 SQLite
- 导出 `discipline_local_code_registry.csv`

## 6.3 可选扩展查询命令

后续可以在 `query_analysis_db.py` 增加：

- `discipline-code-summary`
- `discipline-code <code>`
- `secondary-class-summary`
- `secondary-class-pdf-coverage`

## 6.4 扩展校验脚本

必须扩展现有 `check_data_consistency.py`，或新增专门完整性检查脚本。

建议检查项：

- `paper_id` 唯一且格式合法
- master 与 progress 可互相回连
- active paper 有 note path，且 note 文件存在
- `pdf_path` 非空时文件存在
- supplementary PDF 不得被标记为 main PDF full-text
- `scientific_object_modules` 合法
- `primary_module_for_filing` 必须属于 `scientific_object_modules`，除非有明确 override reason
- `discipline_local_code` 唯一
- `discipline_local_code` 与 `primary_module_for_filing` / 二级位一致
- `01.04` 不得进入 formal `scientific_object_modules`
- Data 层必须可由 export / build 重建

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
6. 跑：
   - `export`
   - `check`
   - `build`
7. 自动生成该论文的 `discipline_local_code`

新增论文的 code 分配必须遵守：

- 在对应二级位下追加编号
- 不重排既有 active code
- 如果二级位暂不明确，使用可追踪的 temporary / pending 状态，不伪造精确二级码

## 7.2 改分类

1. 改 authoritative pair
2. 不手改 Data
3. 跑：
   - `export`
   - `check`
   - `build`
4. 如果主排架位改变：
   - 旧 `discipline_local_code` 标记为 retired / redirected
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
3. 写 closeout
4. 提交 git
5. 再次确认 worktree 干净

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

## 第二步：冻结编码规则

冻结：

- `ASD-xxxx` 保留为永久主键
- `discipline_local_code` 作为二级管理码
- 管理码格式：`MM-SS-NNN`
- 管理码稳定，不自动重排
- 旧码支持 retired / redirected 状态

## 第三步：做 index

新增：

- `classification_code_index.json`

要求：

- 包含 code-label
- 包含 definition / include / exclude / status / source

## 第四步：做 registry

新增：

- `discipline_local_code_registry.jsonl`
- `discipline_local_code_registry.csv`

## 第五步：扩展校验

新增：

- `discipline_local_code` 唯一性检查
- 路径存在性检查
- 分类合法性检查
- owner / derived layer guardrail

## 第六步：接入 SQLite

新增：

- `discipline_local_code_registry` 表或视图

## 第七步：写文档与查询说明

更新：

- `Data/README.md`
- 必要时补 query 示例

## 第八步：后续再考虑是否升级到更强二级 canonical 层

只有当正文写作和分析稳定需要时，再决定是否把二级位进一步升级为更强事实层。

---

## 10. 明确哪些事情现在不做

为了避免返工，下面这些事情当前不做：

1. 不废弃 `ASD-xxxx`
2. 不把 `0101abc` 这种学科码当作唯一主键
3. 不全库重命名 note / PDF 文件
4. 不手改 `Data/`
5. 不把多模块论文拆成多个永久 ID
6. 不因为想做排架编码，就重做 authoritative pair

---

## 11. 一句话版本

> 我们下一步不是重建数据库，而是在现有 `ASD-xxxx + 分类数组 + registry + SQLite` 底座上，补一层“一级/二级学科排架编码层”，把论文身份、分类事实、排架管理、PDF 归档、索引映射和后续分析彻底接起来。

---

## 12. 执行定义

当下面条件满足时，可以认为“学长说的这套长期结构化管理逻辑”已经落实：

1. 永久主键 `ASD-xxxx` 保持稳定。
2. 每篇论文有结构化分类数组。
3. 每篇论文有结构化资料状态。
4. 一级 / 二级分类码有正式 index 文件。
5. 每篇论文有 `discipline_local_code`。
6. `discipline_local_code_registry` 已导出到 JSONL / CSV / SQLite。
7. 字段归属矩阵已经冻结并被 README 引用。
8. 校验脚本能检查 paper ID、code、路径、分类、PDF/source 状态的基本完整性。
9. 后续任何增删改查都遵守 authoritative pair -> export -> check -> build 的流程。
