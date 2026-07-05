# Structured Data Catalog Round 19 Closeout

日期：2026-07-06

## 本轮目标

落实长期方案中已经明确提出、但当前尚未落地的 `discipline_display_order` 字段，把“稳定管理码”和“展示排序字段”彻底拆开。

## 本轮实现

### 1. 在 discipline registry 中新增 `discipline_display_order`

更新：

- `scripts/export_structured_data.py`

为 `discipline_local_code_registry` 新增：

- `discipline_display_order`

当前派生规则：

- `assignment_status = active_code`
  - `discipline_display_order = discipline_local_code`
- `assignment_status = pending_secondary`
  - `discipline_display_order = <primary_module>-<secondary_or_ZZ>-PENDING-<paper_id>`
- `assignment_status = non_discipline_general_method`
  - `discipline_display_order = GM-PENDING-<paper_id>`

这意味着：

- 稳定管理码仍由 `discipline_local_code` owner 控制
- 展示 / 排序用途单独走 `discipline_display_order`
- pending/general-method 记录也能在 CSV / SQLite 中稳定排序，而不需要伪造普通学科 code

### 2. 接入 CSV / SQLite

更新：

- `scripts/build_analysis_db.py`

新增接入：

- `discipline_local_code_registry.csv`
- SQLite `discipline_local_code_registry`

这样 display-order 字段已经贯通到 review 和 query 层。

### 3. 接入 checker

更新：

- `scripts/check_data_consistency.py`

新增检查：

- `active_code`
  - `discipline_display_order` 必须等于 `discipline_local_code`
- `pending_secondary`
  - `discipline_display_order` 必须带 `PENDING`，并以当前 `primary_module_for_filing` 为前缀
- `non_discipline_general_method`
  - `discipline_display_order` 必须以 `GM-PENDING-` 开头

### 4. 文档同步

更新：

- `Data/field_dictionary.md`

新增内容：

- `discipline_local_code_registry` 段落
- `discipline_display_order` 字段语义
- 它是 derived 排序字段，不拥有稳定管理码事实

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

- `ASD-0001`
  - `discipline_local_code = 04-04-001`
  - `discipline_display_order = 04-04-001`
- `ASD-0006`
  - `assignment_status = non_discipline_general_method`
  - `discipline_display_order = GM-PENDING-ASD-0006`

## 本轮结论

本轮把 `discipline_display_order` 从方案文本推进到了实际字段、实际 CSV / SQLite 输出和实际 checker gate。这样后续展示排序、表格 review 和 pending/general-method 记录编排，不再需要借用或污染稳定管理码字段。
