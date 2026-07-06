# Structured Data Catalog Round 106 Closeout

日期：2026-07-06

## 本轮目标

继续把 taxonomy registry 从“code/label 覆盖正确”推进到“结构字段也受约束”。此前 `taxonomy_registry.json` 在 check 层主要校验：

- `taxonomy_code` 覆盖
- `kind`
- `labels.display`

但像 `zh_label`、`en_label`、`sort_order`、`dir_name`、`parent_module_code` 这些由 export 派生的结构字段还没有被显式校验。本轮补齐这部分。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 扩展 `taxonomy_registry` 必填字段

本轮将以下字段纳入 `require_row_fields()`：

- `zh_label`
- `en_label`
- `sort_order`
- `dir_name`
- `parent_module_code`

这让 taxonomy registry 不再只有最小字段存在性检查，而是要求完整派生结构同时存在。

### 2. `en_label` 与 display label 对齐校验

新增：

- `en_label` 必须等于 `taxonomy_index.json code_to_label[code]`
- `labels.display` 必须与 `en_label` 一致

这样 taxonomy registry 的英文标签不再允许和 display label 或 `taxonomy_index.json` 静默漂移。

### 3. `sort_order`、`dir_name`、`parent_module_code` 结构语义校验

新增规则：

- formal module 的 `sort_order` 必须等于模块号 `* 10`
- `01.04` general bucket 的 `sort_order` 必须为 `14`
- formal module 的 `parent_module_code` 必须为空字符串
- `01.04` 的 `parent_module_code` 必须为 `01`
- `dir_name` 必须非空、不可含空格，并且前缀必须和 taxonomy code 对应
  - formal module：`<code>_`
  - `01.04`：`01_04_`

### 4. `zh_label` 非空校验

新增：

- `zh_label` 必须是非空字符串

这一步不强行把中文标签内容硬编码到 check 里，但至少保证 taxonomy registry 的中英文标签层都不是空壳。

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

本轮把 taxonomy registry 从“code/label 快照”继续推进成“结构字段受约束的 taxonomy 派生层”。这更符合方案里 index / registry 需要支撑导航、排序、目录映射和后续分析的要求，也减少了 taxonomy registry 在排序、目录名和父级关系上的静默漂移空间。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 alias registry、taxonomy/analysis 交界、以及 SQLite / JSONL / CSV 三层尚未完全对齐的细项逐轮推进。
