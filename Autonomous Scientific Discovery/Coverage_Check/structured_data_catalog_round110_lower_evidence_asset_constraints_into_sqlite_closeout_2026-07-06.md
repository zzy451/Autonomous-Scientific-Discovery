# Structured Data Catalog Round 110 Closeout

日期：2026-07-06

## 本轮目标

继续把已经在 JSONL `check` 层成立的 evidence / asset 语义，往 SQLite 原生约束层再下沉一小步，让 `build_analysis_db.py` 产出的分析数据库本身也更接近正式数据模型，而不只是被动承接导出结果。

## 本轮修改

修改：
- `scripts/build_analysis_db.py`

### 1. 强化 `pdf_evidence_status` SQLite `CHECK`

本轮新增 / 固化：

- `asset_size_bytes IS NULL OR asset_size_bytes >= 0`
- `source_checked_at` 必须为空或 `YYYY-MM-DD`
- `pdf_evidence_type = main_pdf` 时必须满足 `pdf_exists = 1`

这些规则和当前 export / check 已经成立的语义一致，只是现在进一步下沉到了 SQLite 表结构层。

### 2. 强化 `paper_assets` SQLite `CHECK`

本轮新增 / 固化：

- `asset_id = paper_id || ':' || asset_type`
- `asset_size_bytes IS NULL OR asset_size_bytes >= 0`
- `source_checked_at` 必须为空或 `YYYY-MM-DD`
- `exported_at` 必须为空或 ISO-like `YYYY-MM-DDT...`
- `asset_type = note` 时 `source_checked_at` 必须为空

这让 asset manifest 在 SQLite 中也不再只是平铺的一张表，而是具备了资产身份与时间字段的原生结构约束。

### 3. 修复 evidence SQLite 约束自检的匹配方式

本轮还补了一处 build 自检收口：

- `validate_evidence_sqlite_constraints()` 改为对建表 SQL 做空白规范化后再匹配约束片段

原因是新增的多行 `CHECK` 约束在 SQLite `sqlite_master` 中会带换行与空格差异，若继续用原始字符串匹配，会出现“约束实际存在，但自检误判缺失”的假阳性。

这不是功能扩展，而是让 build 自检方式和前面 discipline / papers 约束检查保持一致。

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

本轮把 evidence / asset 这条线从“JSONL 派生层严格”继续推进成“JSONL 严格 + SQLite 原生兜底”。这和长期方案里 analysis DB 不是松散缓存，而是正式查询与约束承载层的方向一致。

## 后续状态

当前无新的代码级阻塞点；可以继续沿其余 SQLite 约束、build 自检覆盖面、以及 remaining derived-layer 边缘语义逐轮推进。
