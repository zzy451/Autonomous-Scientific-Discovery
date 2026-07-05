# Structured Data Catalog Round 41 Closeout

日期：2026-07-06

## 本轮目标

把上一轮新加的 preview checker 约束追回到字段词典层，确保 `field_dictionary.md` 也把 `discipline_code_initial_assignment_preview.csv` 当作正式的 derived review surface 来定义，而不是只在 README 和脚本里存在。

## 本轮实现

更新：

- `Data/field_dictionary.md`

### 1. 补进 preview 文件

在 analysis 层文件清单中新增：

- `discipline_code_initial_assignment_preview.csv`

这样 `field_dictionary.md` 终于和当前实际导出层保持一致。

### 2. 新增 preview 语义小节

新增：

- `4.2C discipline_code_initial_assignment_preview.csv`

明确它的定位：

- 初始 discipline code 冻结前的 derived review surface
- 主要服务于：
  - secondary 缺失审查
  - 多模块主排架位审查
  - pure general-method 审查
  - source-limited 审查
  - legacy secondary 异常审查

### 3. 把 preview 的关键约束写进词典

在词典里明确：

- 它从 `master + progress + classification_code_index.json` 派生
- 它不是 owner fact source
- paper coverage 应与 `active_confirmed_core` 精确一致
- `pending_secondary` / `non_discipline_general_method` 不得生成假 `MM-SS-NNN` code
- `discipline_local_rank` 只能从 `proposed_discipline_local_code` 派生
- `active_code` proposal 组内按 `paper_id` 排序生成稳定 `NNN`

同时把当前已在 `check_data_consistency.py` 中落地的约束也写清楚：

- current-snapshot coverage
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

其中 preview 相关基线保持：

- `discipline_code_initial_assignment_preview.csv = 447` 行
- `active_confirmed_core = 447`

说明词典同步后，preview 的 current-snapshot 约束与现有导出/检查逻辑仍然一致。

## 本轮结论

这一轮不新增新的行为逻辑，而是把 preview 这一关键 derived review surface 从“README + checker 已知”推进到“字段词典也正式定义”。这样当前关于 preview 的解释已经在：

- `README`
- `field_dictionary`
- `check_data_consistency.py`

三处对齐，减少后续继续推进时再次出现词义漂移的风险。
