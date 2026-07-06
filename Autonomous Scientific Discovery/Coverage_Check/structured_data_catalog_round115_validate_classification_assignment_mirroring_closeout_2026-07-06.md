# Structured Data Catalog Round 115 Closeout

日期：2026-07-06

## 本轮目标

继续把 registry layer 从“coverage 正确”推进到“镜像字段也必须严格对回 `papers.jsonl`”。本轮聚焦：

- `Data/registry/classification_assignments.jsonl`

此前这张表已经检查：

- `paper_id` / `taxonomy_code` 覆盖
- `assignment_kind`
- `assignment_source`
- `assignment_order`
- formal module 与 `01.04` general bucket 的基本分流语义

但它自己带出的 snapshot 字段和 filing 语义还没有被完整显式校验。本轮补齐这部分。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 扩展 `classification_assignments` 必填字段

新增要求以下字段必须存在：

- `assignment_order`
- `is_primary_filing`
- `primary_module_for_filing`
- `object_coverage_mode`
- `active_confirmed_core`
- `exported_at`

这样 classification assignment registry 不再只是“paper-taxonomy 映射对”，而是要求完整 snapshot 字段一起存在。

### 2. `classification_assignments` 逐字段镜像校验

新增：

- `primary_module_for_filing == papers.primary_module_for_filing`
- `object_coverage_mode == papers.object_coverage_mode`
- `active_confirmed_core == papers.active_confirmed_core`
- `exported_at == papers.exported_at`

这让 assignment registry 正式与 paper snapshot 的 filing / coverage / export metadata 对齐。

### 3. `is_primary_filing` 语义显式锁定

新增规则：

- `assignment_source = scientific_object_modules` 时
  - `is_primary_filing == (taxonomy_code == primary_module_for_filing)`
- `assignment_source = general_method_bucket` 时
  - `is_primary_filing` 必须为 `false`

这一步把 previously implicit 的 primary-filing 标记规则正式写死，减少了 classification assignment registry 在主排架标记上的静默漂移空间。

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

本轮把 `classification_assignments.jsonl` 从“assignment coverage 表”进一步推进成“受 filing / coverage / snapshot 元数据共同约束的 derived registry”。这和长期方案里分类事实、排架事实、分析层映射之间要保持稳定联动的要求是一致的。

## 后续状态

当前无新的代码级阻塞点；可以继续沿少量尚未显式写死的 registry / SQLite 边缘语义，以及执行定义和长期方案之间剩余的小闭环项逐轮推进。
