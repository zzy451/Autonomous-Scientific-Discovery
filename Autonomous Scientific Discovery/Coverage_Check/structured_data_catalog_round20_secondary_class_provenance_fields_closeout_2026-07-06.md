# Structured Data Catalog Round 20 Closeout

日期：2026-07-06

## 本轮目标

落实长期方案中二级位 provenance 相关字段，把 `secondary_class_source / secondary_class_confidence / secondary_class_review_status` 真正接进结构化数据层，而不再只停留在方案文本和 taxonomy owner 里。

## 本轮实现

### 1. 在 papers 导出层新增 secondary-class provenance 字段

更新：

- `scripts/export_structured_data.py`

新增导出字段：

- `secondary_class_source`
- `secondary_class_confidence`
- `secondary_class_review_status`

当前派生逻辑：

- 若 `legacy_secondary_class` 为空：
  - 三个字段均为空
- 若 taxonomy owner 中存在对应 secondary term：
  - `secondary_class_source`
    - 根据 term `source` 派生：
      - `manual_override`
      - `normalized`
      - 否则回到 `legacy`
  - `secondary_class_confidence`
    - `active + reviewed` -> `high`
    - `needs_review` 或 `unreviewed / needs_split / needs_merge` -> `low`
    - 其余 -> `medium`
  - `secondary_class_review_status`
    - 直接镜像 taxonomy owner 的 `review_status`
- 若 taxonomy owner 中暂时没有对应 term：
  - `secondary_class_source = legacy`
  - `secondary_class_confidence = low`
  - `secondary_class_review_status = unreviewed`

### 2. 接入 discipline registry / CSV / SQLite

更新：

- `scripts/export_structured_data.py`
- `scripts/build_analysis_db.py`

新增接入位置：

- `papers.jsonl`
- `papers.csv`
- SQLite `papers`
- `discipline_local_code_registry.jsonl`
- `discipline_local_code_registry.csv`
- SQLite `discipline_local_code_registry`

这样 secondary-class provenance 已经同时进入 per-paper snapshot 和 discipline-local current snapshot。

### 3. 接入 checker

更新：

- `scripts/check_data_consistency.py`

新增检查：

- `secondary_class_source` 必须是字符串
- `secondary_class_confidence` 必须是字符串
- `secondary_class_review_status` 必须是字符串
- 若 `legacy_secondary_class` 非空：
  - `secondary_class_source` 必须属于：
    - `legacy`
    - `normalized`
    - `manual_override`
  - `secondary_class_confidence` 必须属于：
    - `high`
    - `medium`
    - `low`
  - `secondary_class_review_status` 必须属于：
    - `unreviewed`
    - `reviewed`
    - `needs_split`
    - `needs_merge`
- 若 `legacy_secondary_class` 为空：
  - 这三项都必须为空
- `discipline_local_code_registry` 中这三项必须与 `papers` snapshot 一致

### 4. 文档同步

更新：

- `Data/field_dictionary.md`

新增说明：

- `papers.jsonl` 中新增的 secondary-class provenance 字段
- discipline registry 中对应的冗余镜像字段
- 它们属于二级位 provenance trace，而不是新的 taxonomy owner facts

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- export 成功
- check 成功
- build 成功

spot check：

- `papers.csv` 已包含：
  - `secondary_class_source`
  - `secondary_class_confidence`
  - `secondary_class_review_status`
- `discipline_local_code_registry.csv` 也已包含相同字段

示例：

- `ASD-0001`
  - `legacy_secondary_class = 04.04`
  - `secondary_class_source = legacy`
  - `secondary_class_confidence = low`
  - `secondary_class_review_status = unreviewed`

## 本轮结论

本轮把二级位 provenance 从“只能间接去 taxonomy owner 里看”推进到了“在 papers snapshot、discipline registry、CSV 和 SQLite 里直接可见”的状态。这样后续做二级位 review、split / merge 规划、pending secondary 排查时，不再需要只靠 `legacy_secondary_class` 一个字段做弱推断。
