# Structured Data Catalog Round 48 Closeout

日期：2026-07-06

## 本轮目标

把 SQLite `analysis_object_scope_registry` 也纳入 `build_analysis_db.py` 的 build-time fidelity checks，避免这张声明型对象表虽然决定了 SQLite 内各对象的 scope/use 解释，却还没有被主动核对。

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 把 object-scope rows 抽成显式 builder

在 `build_analysis_db.py` 中新增：

- `build_analysis_object_scope_rows()`

它统一返回当前 build 要插入 `analysis_object_scope_registry` 的声明行，而不是把长列表只埋在 `executemany(...)` 调用里。

### 2. 新增 `analysis_object_scope_registry` 自校验

新增：

- `validate_analysis_object_scope_registry()`

当前 build 完成后会：

- 读取 SQLite `analysis_object_scope_registry`
- 按 `object_name` 排序
- 与 `build_analysis_object_scope_rows()` 逐行比对

这样如果以后有人修改了 SQLite object-scope 声明，却没有同步这张注册表，build 会直接失败。

### 3. 把新校验接入主构建流程

本轮把：

- `validate_analysis_object_scope_registry()`

接入 `main()`，与当前已启用的：

- `papers`
- module surfaces
- discipline registry
- auxiliary analysis tables
- owner-loaded / inventory tables
- metadata / summary tables

一起成为真实 build gate。

### 4. README 同步

在 `Data/README.md` 中补充说明：

- `analysis_object_scope_registry` 现在也会被 build 自检
- 它必须忠实反映当前 build 脚本里声明的 object-scope rows

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

说明当前 `analysis_object_scope_registry` 已经通过 build-time fidelity check，没有发生 object_name / scope_class / default_usage / warning 漂移。

## 本轮结论

这一轮把 SQLite 内部“对象语义注册表”本身也纳入了 build gate。这样现在不只是数据表和 counts 被核对，连“SQLite 中每个对象应该如何被解释”的声明层也开始被主动验证，减少后续继续推进时出现 object-scope 文义漂移的风险。
