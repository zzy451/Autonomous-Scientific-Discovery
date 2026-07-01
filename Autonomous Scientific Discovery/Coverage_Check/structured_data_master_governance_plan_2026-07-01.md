# ASD 结构化数据与仓库治理总方案

日期：2026-07-01

本文档用于正式锁定 `Autonomous Scientific Discovery` 项目后续的结构化数据、分类存储、PDF 归档、GitHub 同步与增删改查规则，避免长上下文协作中的计划漂移。

## 1. 目标

本方案要解决的不是“再写一份说明”，而是把当前综述项目正式转成一套可持续维护的数据体系：

1. 让每篇论文都有稳定唯一身份。
2. 让分类结果以程序可读的数组和索引形式保存。
3. 让 PDF、note、master、统计文件之间的主从关系固定下来。
4. 让后续分析、查询、补档、复核、GitHub 同步都走统一流程。
5. 让未来即使分类调整、note 挪动、PDF 重命名，主数据也不会混乱。

## 2. 当前已完成事项

截至 2026-07-01，以下基础设施已经完成：

### 2.1 结构化导出层

已建立脚本与基础导出文件：

- `scripts/export_structured_data.py`
- `scripts/check_data_consistency.py`
- `Data/papers.jsonl`
- `Data/taxonomy_index.json`
- `Data/pdf_manifest.json`
- `Data/missing_pdf_manifest.json`
- `Data/note_manifest.json`

### 2.2 分析层

已建立面向查询与统计的分析输出：

- `scripts/build_analysis_db.py`
- `scripts/query_analysis_db.py`
- `Data/papers.csv`
- `Data/paper_modules.csv`
- `Data/papers.sqlite`

### 2.3 GitHub / PDF 归档

已完成：

- 根目录 `.gitattributes` 与 `.gitignore` 调整
- `*.pdf` 通过 Git LFS 管理
- `Reference_PDF/` 已推送到远端分支 `codex-analysis-db-and-pdfs-2026-07-01`

这意味着“分类数据库化 + PDF 仓库化”的第一阶段已经不是计划，而是已经有实际落地结果。

## 3. 当前 authoritative 状态

当前正式口径固定如下：

- 唯一主索引：`Paper_Lists/agent_master_paper_list.md`
- 进度与 PDF 证据正式字段：`Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- 当前 confirmed core：`447`
- 当前有本地真 PDF：`421`
- 当前无本地 PDF：`26`
- 当前 `pdf_path` 已填但文件损坏/缺失：`0`
- 当前分类体系：`01-11` scientific-object modules + 独立 `01.04` general-method bucket

必须继续遵守：

1. 不能用 `Notes/` 平铺扫描替代 master 做主统计。
2. 不能把“读过全文”直接等同于“有本地 PDF 证据”。
3. 分类必须按具体 scientific-object experiment / validation / benchmark / case-study / reported result。
4. 有多个具体 scientific object 证据时允许 multi-module。
5. `01.04` 只用于没有具体 scientific-object 证据的通用方法论文。

## 4. 主键与身份设计

### 4.1 永久主键

项目永久唯一身份号固定为：

```text
ASD-0001
ASD-0002
...
```

`ASD-xxxx` 是唯一主键，后续不得改成按分类生成的新主键。

原因很明确：

1. 同一论文未来可能从单模块改成多模块。
2. 同一论文的 `primary_module_for_filing` 可能变化。
3. PDF 路径、note 路径、归档目录都可能变化。
4. 如果把分类码做主键，后续重分类会破坏引用稳定性。

### 4.2 分类码的定位

你学长提到的类似 `0101abc` 的编码，可以保留为辅助字段，但不能替代 `ASD-xxxx`。

推荐做法：

- `paper_id`: 永久主键，例如 `ASD-0312`
- `primary_module_for_filing`: 归档主目录，例如 `04`
- `filing_call_number`: 可选展示/排序码，例如 `04-127`
- `scientific_object_modules`: 正式分类数组，例如 `["03", "04"]`

也就是说：

- `ASD-xxxx` 解决“唯一识别”
- 分类码解决“展示、排序、归档便利”

## 5. 数据主从关系

后续必须固定以下主从结构：

### 5.1 唯一事实源

唯一事实源是：

1. `Paper_Lists/agent_master_paper_list.md`
2. `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

其中：

- master 负责论文身份、纳入状态、分类结果、note 路径等主数据
- progress 负责 `pdf_status`、`pdf_path`、`evidence_status` 等正式证据状态

### 5.2 派生层

以下都属于派生文件，不允许人工当作独立事实源长期手改：

- `Data/papers.jsonl`
- `Data/taxonomy_index.json`
- `Data/pdf_manifest.json`
- `Data/missing_pdf_manifest.json`
- `Data/note_manifest.json`
- `Data/papers.csv`
- `Data/paper_modules.csv`
- `Data/papers.sqlite`

这些文件应当通过脚本从 master/progress 重建。

### 5.3 辅助证据层

以下是支持层，不是主索引：

- `Notes/`
- `Reference_PDF/`
- `Coverage_Check/` 下的 audit/report/plan

它们可以提供证据、说明、归档与复核痕迹，但不能越级覆盖 master/progress 的正式状态。

## 6. 正式结构化模型

### 6.1 论文主表

`Data/papers.jsonl` / `Data/papers.csv` / SQLite `papers` 表，应以“一篇论文一条记录”为核心。

每条记录至少应保留：

- `paper_id`
- `title`
- `year`
- `doi`
- `url`
- `inclusion_status`
- `scientific_object_modules`
- `general_method_bucket`
- `object_coverage_mode`
- `primary_module_for_filing`
- `final_modules_or_bucket`
- `note_path`
- `pdf_status`
- `pdf_path`
- `evidence_status`
- `remarks`

### 6.2 分类数组

正式分类必须是数组，而不是只存一个字符串。

示例：

```json
{
  "paper_id": "ASD-0123",
  "scientific_object_modules": ["03", "04"],
  "general_method_bucket": "none",
  "primary_module_for_filing": "04"
}
```

如果论文是通用方法而无具体 scientific object 证据，则：

```json
{
  "paper_id": "ASD-0456",
  "scientific_object_modules": [],
  "general_method_bucket": "01.04",
  "primary_module_for_filing": "01"
}
```

### 6.3 taxonomy index

必须保存“数字 <-> 分类名”的双向对应。

当前最少要保证：

- `code_to_label`
- `label_to_code`

并且建议未来扩展：

- `code`
- `english_label`
- `chinese_label`
- `is_formal_module`
- `is_general_method_bucket`
- `parent_code`
- `filing_dir_name`

这样后面无论做网页、数据库、统计图还是脚本查询，都不会再依赖手写映射。

### 6.4 多对多分析表

为了后续分析方便，继续保留一张“展开后的模块关系表”：

- `Data/paper_modules.csv`
- SQLite `paper_module_assignments` 或等效表

一篇多模块论文会在这张表里拆成多行，方便做：

- 每模块论文数
- 多模块组合统计
- 交叉学科分析
- PDF 覆盖按模块统计

## 7. PDF 治理规则

### 7.1 PDF 身份关系

PDF 不再是松散文件集合，而应和 `paper_id` 绑定。

正式关系通过 `pdf_manifest.json` 表达，至少应包含：

- `paper_id`
- `pdf_path`
- `pdf_status`
- `sha256`
- `primary_module_for_filing`
- `scientific_object_modules`

### 7.2 目录与命名

当前不强制把所有 PDF 重命名成分类码形式。

保留现有 descriptive filename 更稳妥，例如：

`Zhou_2025_MAPPS.pdf`

真正的绑定关系交给 manifest，而不是把语义硬编码到文件名里。

### 7.3 无本地 PDF 的 26 篇

这 26 篇必须被正式视为：

- `无本地 PDF`
- `但有 DOI / 可索引`
- `不是文献条目缺失`

因此它们必须持续存在于 `missing_pdf_manifest.json` 中，而不是被误记成“漏收录”。

## 8. GitHub 与仓库管理规则

### 8.1 仓库中应保存什么

GitHub 仓库中应稳定保存：

- master 与政策文件
- `Coverage_Check/` 下的计划、报告、治理文件
- `Data/` 下的结构化导出与分析结果
- `scripts/` 下的导出、校验、查询脚本
- `Reference_PDF/` 及其 LFS 记录

### 8.2 不应怎么做

后续不要：

1. 手工编辑 JSON/CSV/SQLite 来纠正分类。
2. 以 note 所在目录作为唯一分类事实。
3. 以 `pdf_path` 非空直接等同于“本地真 PDF 存在”。
4. 在不同脚本里各自维护不同版本的 taxonomy 映射。

## 9. 标准操作流程

后续所有增删改查，统一遵守这个顺序：

### 9.1 增

新增论文时：

1. 先进入 `agent_master_paper_list.md`
2. 分配新的 `ASD-xxxx`
3. 记录纳入状态、分类结果、note 路径等
4. 若有 PDF，再更新 progress 的 `pdf_status/pdf_path/evidence_status`
5. 再运行导出与校验脚本重建 `Data/`

### 9.2 删

删除或排除论文时：

1. 先在 master 改正式状态
2. 若 PDF 或 note 需要同步处理，再做归档层清理
3. 再重建 `Data/`

不能只删 note 或只删 PDF 而不改 master。

### 9.3 改

修改分类、修正 PDF 状态、调整 note 路径时：

1. 先改 master/progress
2. 再运行导出脚本
3. 再运行一致性检查
4. 最后才提交 Git

### 9.4 查

查询时优先级如下：

1. 需要正式口径：查 master/progress
2. 需要批量分析：查 `papers.sqlite`
3. 需要轻量筛选：查 `papers.csv` / `paper_modules.csv`
4. 需要单篇详情：查 `papers.jsonl`

## 10. 后续执行阶段

### Phase A：规则冻结

本阶段目标：

- 确认 `ASD-xxxx` 为永久主键
- 确认分类结果用数组表达
- 确认 taxonomy index 为统一映射源
- 确认 master/progress 为唯一事实源

### Phase B：数据层稳定化

本阶段目标：

- 把现有导出脚本与分析脚本视为正式基础设施
- 进一步明确字段字典和异常值处理
- 保证每次导出结果可重现

### Phase C：查询与统计固化

本阶段目标：

- 补齐常用查询命令
- 固化 record-level count 与 expanded module count 两套统计
- 固化 `01.04` 独立统计
- 固化无本地 PDF 26 篇的专门查询

### Phase D：治理与协作

本阶段目标：

- 在多人协作中统一“先改 master/progress，再导出 Data”的工作法
- 避免不同人手工维护不同版本的分类数据
- 把 GitHub 分支、PR、LFS 上传流程稳定下来

## 11. 近期下一步

在本方案写入仓库后，建议下一步按以下顺序继续：

1. 检查并补强 `Data/README.md`，让使用者知道如何从 master 重建数据层。
2. 审查 `query_analysis_db.py` 的统计语义，明确 `scientific_object_modules` 与 `final_modules_or_bucket` 两种口径的区别。
3. 补一个面向日常使用的字段字典文档，固定每个导出字段的定义。
4. 在不打扰当前主审计脏工作树的前提下，单独提交这份治理文档。

## 12. 核心结论

从现在开始，这个项目的数据管理逻辑应固定为：

1. `ASD-xxxx` 是唯一永久身份号。
2. `agent_master_paper_list.md` 是唯一主索引。
3. 分类结果必须以数组保存，而不是单值硬编码。
4. `01.04` 是独立 general-method bucket，不并入正式 scientific-object module 数组。
5. `Data/` 是从 master/progress 可重建的结构化派生层。
6. `Reference_PDF/` 与 PDF manifest 一起构成可审计的 PDF 归档层。
7. 后续所有增删改查，都应围绕这套结构继续扩展，而不是再回到“手工目录管理 + 手工统计”的模式。
