# Structured Data Catalog Round 37 Closeout

日期：2026-07-06

## 本轮目标

补齐长期方案第 12 步里“文档与查询说明”的当前缺口，把已经实现但尚未在 `Data/README.md` 中正式暴露的 discipline / taxonomy / asset / note 查询入口，以及 initial preview 文件角色，写成可直接执行的操作面说明。

## 本轮实现

更新：

- `Data/README.md`

### 1. 补充 initial preview 文件角色

在 `Typical file roles` 中新增：

- `discipline_code_initial_assignment_preview.csv`

并明确它的职责：

- 它是从 `master + progress + taxonomy owner` 派生的初始分配审查表
- 它用于冻结或维护 `discipline_code_assignments.jsonl` 前的人工审查
- 它不是 owner fact source，发现问题应回到 owner 文件修正后重新 export，而不是手改 preview

### 2. 把已实现的 discipline / taxonomy 查询入口写入 README

新增可直接执行的 `query_analysis_db.py` 示例：

- `discipline-code-summary`
- `discipline-code <code>`
- `secondary-class-summary`
- `secondary-class-pdf-coverage`
- `classification-terms --level secondary`
- `general-method-buckets`
- `paper-assets --asset-type primary_pdf`
- `notes --missing-only`

### 3. 补充这些查询面的解释边界

在 `Operational notes` 中补充说明：

- `discipline-code-summary` 是 ledger-derived current snapshot summary
- `discipline-code` 用于追踪单个 code 的 current / historical lifecycle context
- `secondary-class-*` 是面向二级排架与 PDF 覆盖审查的 review surface
- `classification-terms` 直接反映 taxonomy vocabulary owner
- `general-method-buckets` 走专门 relation table，不依赖 mixed-scope module 表推断
- `paper-assets` / `notes` 用于资产与 note 缺失审查

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-code-summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" classification-terms --level secondary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" notes --missing-only
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- 新增文档化的 3 个抽样查询命令均可正常运行
- `discipline-code-summary` 返回当前 snapshot 统计：
  - `current_registry_row_count = 447`
  - `active_code_count = 423`
  - `pending_secondary_count = 15`
  - `non_discipline_general_method_count = 9`
- `classification-terms --level secondary` 正常列出当前 secondary taxonomy owner terms
- `notes --missing-only` 在 active confirmed-core 范围内返回 `No rows found`
- `export` 成功
- `check` 成功
- `build` 成功

## 本轮结论

这一轮没有再扩展新的 owner 事实或新功能，而是把已经落地的 discipline-code / taxonomy / asset / note 查询面正式补进 README，并把 initial preview 的 derived 身份写清楚。这样当前结构化层不只是“代码里能做”，而是“仓库文档里已经明确告诉协作者怎么用、哪些文件是 review surface、哪些不是事实源”。
