# Structured Data Catalog Round 39 Closeout

日期：2026-07-06

## 本轮目标

收口上一轮 `paper_modules` canonical realignment 之后遗留的文档漂移，把 `Data/field_dictionary.md` 同步到当前真实对象语义，避免字段词典继续把默认 `paper_modules` 误写成 mixed-scope。

## 本轮实现

更新：

- `Data/field_dictionary.md`

### 1. 同步 analysis 层对象列表

在 analysis 层文件清单中补入：

- `mixed_scope_paper_modules.csv`

这样词典层和当前实际导出层保持一致。

### 2. 修正 SQLite module 关系层语义说明

把旧说明：

- `paper_modules`
- `module_assignment_counts`

同时包含 canonical 与 workflow mirror assignment

改为当前真实状态：

- `paper_modules`
- `module_assignment_counts`

只承载 canonical `scientific_object_modules` assignment。

### 3. 补齐 alias / workflow / mixed-scope 三层边界

在词典中明确：

- `canonical_paper_modules`
- `canonical_module_assignment_counts`

只是兼容 alias；

- `workflow_mirror_paper_modules`
- `workflow_mirror_module_assignment_counts`

是单独 workflow 审计层；

只有下面这些对象才是 explicit mixed-scope compatibility surface：

- `mixed_scope_paper_modules.csv`
- `mixed_scope_paper_modules`
- `mixed_scope_module_assignment_counts`
- `analysis_object_scope_registry`

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

build 输出保持：

- `paper_modules rows = 843`
- `workflow_mirror_paper_modules rows = 592`
- `mixed_scope_paper_modules rows = 1435`

说明当前 canonical / workflow / mixed-scope 三层对象边界仍然一致，没有因为词典同步而引入行为回退。

## 本轮结论

这一轮不新增功能，而是把 `field_dictionary.md` 追回到当前真实实现，补掉“README 已改、build 已改，但字段词典还保留旧 mixed-scope 叙述”的文档层漂移。这样 `README + field_dictionary + build outputs` 三处对 `paper_modules` 的解释终于重新一致。
