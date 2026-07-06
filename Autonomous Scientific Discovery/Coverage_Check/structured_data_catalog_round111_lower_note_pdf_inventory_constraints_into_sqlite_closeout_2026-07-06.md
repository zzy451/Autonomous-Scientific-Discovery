# Structured Data Catalog Round 111 Closeout

日期：2026-07-06

## 本轮目标

继续把 analysis DB 中的 inventory / note 相关表从“承接导出结果”推进成“自身带原生约束的查询层”。本轮聚焦：

- `notes`
- `note_inventory`
- `pdf_inventory`

把已经在现有导出产物中成立的路径与摘要字段语义，进一步下沉到 SQLite。

## 本轮修改

修改：
- `scripts/build_analysis_db.py`

### 1. `pdf_inventory` SQLite 约束增强

本轮新增 / 固化：

- `pdf_path` 必须非空白
- `sha256` 必须为 64 位小写十六进制

这两条规则都和当前 `pdf_manifest.json` 的事实保持一致，只是现在进一步写进了 SQLite 表结构本身。

### 2. `notes` / `note_inventory` 的 active-only `note_path` 约束

初版尝试把 `note_path` 设为全表非空后，build 立刻暴露了真实数据语义：

- `note_manifest` 覆盖全库 871 条记录
- 其中有 396 条非 active 记录的 `note_path` 为空
- active confirmed-core 记录中为空的数量是 0

因此本轮把约束修正为更符合项目现状与方案要求的形式：

- `active_confirmed_core = 1` 时，`note_path` 必须非空白

这样：

- active confirmed-core 行继续被严格约束
- background / excluded / 非活跃行不会被错误当成违规

### 3. build 自检同步更新

`validate_evidence_sqlite_constraints()` 已同步检查：

- `notes` / `note_inventory` 中 active-only 的 `note_path` 约束片段
- `pdf_inventory` 的 `pdf_path` 非空白与 `sha256` 形状约束片段

所以这些规则不只在建表 SQL 中出现，也会在 build 自检时被再次核验。

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

本轮把 note / PDF inventory 这条线继续往“数据库自身可兜底”推进了一步，而且没有假设全库所有记录都已经达到 active-core 的完备度。约束强度现在更贴近真实工作流阶段：

- active confirmed-core 严格
- 非活跃记录不过度误伤

这和长期方案里“owner fact source + derived analysis DB + 明确语义边界”的方向一致。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite guardrails、build 自检覆盖面、以及少量还未显式化的 derived-layer 边缘语义逐轮推进。
