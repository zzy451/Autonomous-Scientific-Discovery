# Structured Data Catalog Round 90 Closeout

日期：2026-07-06

## 本轮目标

继续把 SQLite 中的核心 analysis / query surfaces 与 taxonomy index 建立真实数据库关系，而不只让 code 字段停留在裸字符串层。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 新增 taxonomy 外键

以下字段现在显式声明为 `REFERENCES taxonomy_index(code)`：

1. `papers.primary_module_for_filing`
2. `paper_modules.module_code`
3. `workflow_mirror_paper_modules.module_code`
4. `pdf_evidence_status.primary_module_for_filing`
5. `pdf_inventory.primary_module_for_filing`

这让：

- `papers` 的主排架一级模块
- canonical / workflow mirror module rows 的 module code
- PDF evidence / local PDF inventory 中的一级主排架模块

都在数据库层正式受 taxonomy index 约束。

### 2. blank-to-null 兼容

由于 `papers` / `pdf_evidence_status` / `pdf_inventory` 中的 `primary_module_for_filing` 对 general-method-only 记录可能为空，SQLite 插入和期望值比较阶段都继续使用 `blank_to_none()` 规范化，避免空字符串误触外键失败。

### 3. build 自检扩展

扩展 `validate_core_analysis_foreign_keys()`，新增检查：

- `papers.primary_module_for_filing -> taxonomy_index(code)`
- `paper_modules.module_code -> taxonomy_index(code)`
- `workflow_mirror_paper_modules.module_code -> taxonomy_index(code)`
- `pdf_evidence_status.primary_module_for_filing -> taxonomy_index(code)`
- `pdf_inventory.primary_module_for_filing -> taxonomy_index(code)`

### 4. 明确未强行加的外键

本轮曾尝试把 `paper_general_method_buckets.general_method_bucket` 直接连到 `taxonomy_index(code)`，但当前该字段存的是完整 canonical bucket 字符串，而不是短 code，因此这条外键在现状下并不语义等价。已明确回退，避免引入错误约束。

## 验证

运行：

```bash
python "Autonomous Scientific Discovery/scripts/run_structured_data_pipeline.py" --with-execution-audit
```

结果：

- `export_structured_data.py` 通过
- `check_data_consistency.py` 通过
- `build_analysis_db.py` 通过
- `audit_execution_definition.py` 通过

执行定义审计结果：

- `PASS=12`
- `FAIL=0`

额外 SQLite 证据：

```text
papers:
  primary_module_for_filing -> taxonomy_index(code)

paper_modules:
  module_code -> taxonomy_index(code)
  paper_id -> papers(paper_id)

workflow_mirror_paper_modules:
  module_code -> taxonomy_index(code)
  paper_id -> papers(paper_id)

pdf_evidence_status:
  primary_module_for_filing -> taxonomy_index(code)
  paper_id -> papers(paper_id)

pdf_inventory:
  primary_module_for_filing -> taxonomy_index(code)
  paper_id -> papers(paper_id)
```

## 产出判断

本轮把一批核心 code 字段从“字符串上像分类码”推进为“数据库层真受 taxonomy index 约束”，让主排架一级模块和 module assignment code 的结构关系更加正式。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
