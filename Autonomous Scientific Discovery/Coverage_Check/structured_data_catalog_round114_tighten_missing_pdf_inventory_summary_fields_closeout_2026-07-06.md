# Structured Data Catalog Round 114 Closeout

日期：2026-07-06

## 本轮目标

继续沿 no-local-PDF 分支做 SQLite 原生收口。上一轮已经把：

- `missing_pdf_manifest.json` 的逐字段镜像关系
- `missing_pdf_inventory` 的 `source_limited` / `access_note`

锁进了 check / build。当前数据里 `missing_pdf_inventory` 的其余摘要字段也已经全表稳定非空，所以本轮进一步把这些字段也正式下沉为 SQLite 约束。

## 本轮修改

修改：
- `scripts/build_analysis_db.py`

### 1. `missing_pdf_inventory` 新增非空白字段约束

本轮为 `missing_pdf_inventory` 新增：

- `doi` 非空白：`trim(doi) <> ''`
- `url` 非空白：`trim(url) <> ''`
- `pdf_status` 非空白：`trim(pdf_status) <> ''`
- `evidence_status` 非空白：`trim(evidence_status) <> ''`

这些规则与当前 `Data/missing_pdf_manifest.json` 的 25 条 no-local-PDF 记录完全一致，属于把“已经成立的稳定事实”进一步写进 SQLite 结构本身。

### 2. build 自检同步覆盖新约束

`validate_evidence_sqlite_constraints()` 已同步要求 `sqlite_master` 中真实出现上述四条约束片段。

因此这一步不是只改了建表 SQL，而是把：

- 建表
- build 自检

两层一起收口。

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

本轮把 `missing_pdf_inventory` 从“有一条 no-local-PDF 摘要记录”继续推进成“摘要字段完整且受结构约束的 inventory 表”。这样 no-local-PDF 分支的 SQLite 承载层和已有的 JSON/manifest 镜像收口更一致，也更接近长期方案里 analysis DB 应有的正式数据模型。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite guardrails、少量尚未显式写死的 derived metadata 语义、以及执行定义与长期方案间剩余的边缘闭环项逐轮推进。
