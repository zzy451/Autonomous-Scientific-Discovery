# Structured Data Catalog Round 40 Closeout

日期：2026-07-06

## 本轮目标

把 `Data/discipline_code_initial_assignment_preview.csv` 从“能生成的 derived review sheet”推进到“被 consistency check 显式约束的关键 review surface”，补上它在校验层的硬语义检查。

## 本轮实现

更新：

- `scripts/check_data_consistency.py`
- `Data/README.md`

### 1. 新增 preview 载入与校验

在 `check_data_consistency.py` 中新增：

- `discipline_code_initial_assignment_preview.csv` 路径常量
- CSV 读取 helper
- CSV bool 解析 helper
- `validate_discipline_initial_assignment_preview(...)`

### 2. 校验的核心语义

当前 check 会显式验证 preview 的以下规则：

- preview 文件必须存在
- row count 必须等于 `active_confirmed_core` paper 数
- paper coverage 必须和 `active_confirmed_core` 精确一致
- preview 基础字段必须和 `papers.jsonl` / taxonomy owner 一致：
  - `title`
  - `inclusion_status`
  - `scientific_object_modules`
  - `general_method_bucket`
  - `object_coverage_mode`
  - `primary_module_for_filing`
  - `primary_module_label`
  - `legacy_secondary_class`
  - `secondary_term_*`
  - `source_limited`
  - `pdf_status`
  - `evidence_status`
  - `note_path`
  - `pdf_path`
- pure general-method 记录必须：
  - `proposed_assignment_status = non_discipline_general_method`
  - 不得携带普通 code / rank / secondary proposal
- 缺主排架位、缺/疑似 secondary、secondary-primary mismatch 三类记录必须：
  - `proposed_assignment_status = pending_secondary`
  - `pending_reason` 匹配对应规则
  - 不得生成假 code / rank
- `active_code` 预分配记录必须：
  - secondary proposal 与 `legacy_secondary_class` 一致
  - `proposed_discipline_local_code` 匹配 `MM-SS-NNN`
  - `discipline_local_rank` 只能来自 code 尾部
- 每个 secondary code 组内的 active rows 必须按 `paper_id` 排序后形成稳定顺序号序列
- `review_flags` 至少覆盖当前脚本承诺的关键情形：
  - `multi_module`
  - `source_limited`
  - `primary_module_outside_scientific_object_modules`
  - `secondary_not_in_taxonomy_index`

### 3. README 同步

在 `Data/README.md` 里补充说明：

- `discipline_code_initial_assignment_preview.csv` 现在已经由 `check_data_consistency.py` 验证：
  - current-snapshot paper coverage
  - status branching
  - no-fake-code rules
  - active-code sequence stability

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- `export` 成功
- `check` 成功
- `build` 成功

其中本轮新增的 preview 校验已通过，说明当前 preview 至少满足：

- `447` 行 preview 与 `447` 个 `active_confirmed_core` 记录精确对应
- `pending_secondary` / `non_discipline_general_method` 行未生成假 `MM-SS-NNN` code
- `active_code` 预分配序号仍然与按 `paper_id` 排序的分组顺序一致

## 本轮结论

这一轮把 preview 从“有导出文件”提升到了“有一致性约束的正式 review surface”。这样后续如果 preview 语义、排序或 no-fake-code 规则发生漂移，就不会再只靠人工肉眼发现，而会在 `check_data_consistency.py` 阶段直接报错。
