# Structured Data Catalog Round 102 Closeout

日期：2026-07-06

## 本轮目标

继续把 discipline preview 的导出语义前移到 `check_data_consistency.py`。这一轮聚焦 `Data/discipline_code_initial_assignment_preview.csv` 的 `review_flags`，把它从“部分 flag 存在即可”收紧成“整组 flag 必须精确匹配 export 规则推导结果”。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. `review_flags` 去重校验

在 `validate_discipline_initial_assignment_preview()` 中新增：

- `review_flags` 不允许重复值

如果 preview 某行因为导出漂移或人工污染出现重复 flag，现在会在 check 阶段直接失败。

### 2. `review_flags` 精确集合匹配

此前只检查了少数几类 flag 是否“该有时存在”，例如：

- `multi_module`
- `source_limited`
- `primary_module_outside_scientific_object_modules`
- `secondary_not_in_taxonomy_index`

本轮把检查提升为整组精确匹配。`check_data_consistency.py` 现在会按和 export 同样的规则重新推导 `expected_review_flags`，并要求 preview 行中的 `review_flags` 集合与之完全一致。

覆盖的 flag 规则包括：

- `multi_module`
- `source_limited`
- `primary_module_outside_scientific_object_modules`
- `secondary_not_in_taxonomy_index`
- `secondary_term_status_<status>`
- `secondary_term_review_<review_status>`
- `general_method_secondary_not_01_04`
- `missing_primary_module_for_filing`
- `missing_or_uncertain_secondary_class`
- `secondary_primary_mismatch`

这样可以防止两类问题：

- 应有的 review flag 漏掉
- 不应有的 review flag 被多写、错写或残留

### 3. preview 人工审查层语义进一步和 export 对齐

这一步没有改 preview 的生成逻辑，也没有扩展第二阶段功能；只是把现有 preview 的人工审查辅助字段正式纳入一致性校验，让：

- export 生成的 review 提示
- check 阶段的约束

保持一一对应。

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

本轮把 preview 审查层的 `review_flags` 从“宽松提示字段”继续收紧为“有精确语义边界的 derived field”。这让 initial assignment preview 更接近方案里要求的正式审查工件，而不是仅供人工大致参考的松散表格。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 preview / registry / SQLite 三层之间仍未完全前移的纪律逐轮补齐。
