# Structured Data Catalog Round 13 Closeout

日期：2026-07-06

## 本轮目标

把已经落地的 owner schema 文件真正接入 check 主链，避免 `Data/schema/*.schema.json` 只停留在文档层而不参与执行。

## 本轮实现

### 1. 在 checker 中接入 schema enforcement

更新：

- `scripts/check_data_consistency.py`

新增能力：

- 读取：
  - `Data/schema/classification_code_index.schema.json`
  - `Data/schema/discipline_code_assignments.schema.json`
- 在现有语义检查前，对以下 owner 文件做 schema 校验：
  - `Data/classification_code_index.json`
  - `Data/discipline_code_assignments.jsonl`

本轮实现的是一个受控的轻量本地 schema validator，覆盖当前仓库实际使用到的 JSON Schema 子集：

- `type`
- `required`
- `properties`
- `additionalProperties`
- `items`
- `enum`
- `const`
- `pattern`
- `minLength`
- `$ref`
- `$defs`
- `allOf`
- `if` / `then`

这意味着：

- taxonomy owner 的字段漂移、缺字段、额外字段、枚举值漂移、日期格式漂移，会在 check 阶段被阻断
- discipline code ledger 的字段漂移、状态枚举漂移、条件字段约束漂移，也会在 check 阶段被阻断

### 2. 文档同步

更新：

- `Data/README.md`

新增说明：

- `Data/schema/*.schema.json` 已经由 `check_data_consistency.py` 强制执行，不再只是静态治理文件

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

本轮确认：

- `classification_code_index.json` 可以通过 schema + 语义双重校验
- `discipline_code_assignments.jsonl` 可以通过 schema + 语义双重校验
- schema enforcement 未破坏现有 derived/export/build 主链

当前主链状态：

- `papers.jsonl` records: 871
- `active confirmed-core`: 447
- `active local PDFs`: 422
- `active no-local-PDF`: 25
- `discipline_code_assignments` rows: 447
- `discipline_local_code_registry` rows: 447

## 本轮结论

本轮把“schema 已存在”推进到了“schema 已执行”。这样后续 owner 文件如果发生字段拼写漂移、状态值漂移、条件字段错配，不会再只靠人工发现，而会直接在 `check_data_consistency.py` 中暴露出来。
