# Structured Data Catalog Round 29 Closeout

日期：2026-07-06

## 本轮目标

补 taxonomy owner 的独立初始化入口，落实长期方案里“taxonomy vocabulary 不应由日常 export 初始化，而应走专门命令”的要求。

## 本轮实现

### 1. 新增 taxonomy owner init 命令

新增：

- `scripts/init_classification_code_index.py`

作用：

- 从当前 taxonomy code map 与 master owner 中的 legacy `Secondary class` 种子生成
  - `Data/classification_code_index.json`
- 保持 taxonomy owner 初始化与日常 export 分离

### 2. 当前初始化逻辑

primary terms：

- 从现有 formal module / general bucket code map 生成
- 当前会生成：
  - `12` 个 primary terms
  - 包括单独的 `01.04` general-method bucket

secondary terms：

- 从 `Paper_Lists/agent_master_paper_list.md` 中当前出现的合法 `Secondary class` 去重生成
- 当前初始化出的 secondary term：
  - `status = needs_review`
  - `review_status = unreviewed`
  - `source = legacy_secondary_class_seed_init`

### 3. 安全行为

默认：

- 若 `Data/classification_code_index.json` 已存在，则拒绝覆盖

支持：

- `--overwrite`
- `--dry-run`
- `--updated-at`
- `--updated-by`

这保证 taxonomy owner 初始化不会被日常流程悄悄触发，也不会无意覆盖现有 owner 文件。

### 4. README 同步

更新：

- `Data/README.md`

补充说明：

- `init_classification_code_index.py` 是 taxonomy owner 的显式初始化入口
- taxonomy owner 初始化与 daily export 严格分离

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/init_classification_code_index.py" --dry-run
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- taxonomy init dry-run 成功
- export 成功
- check 成功
- build 成功

dry-run 关键输出：

- `Prepared classification_code_index payload with 12 primary_terms and 40 secondary_terms.`
- `Dry run preview only; existing Data/classification_code_index.json would be left unchanged without --overwrite.`

额外 spot check：

- 当前 master 中可收集到的合法 secondary codes：`40`
- 当前 owner 文件中已有 secondary terms：`36`
- dry-run 暴露出的 owner 覆盖缺口：
  - `05.03`
  - `10.04`
  - `11.03`
  - `11.04`

本轮没有覆盖现有 taxonomy owner 文件，只新增初始化命令并用 dry-run 暴露这一差距。

## 本轮结论

本轮把 taxonomy owner 的初始化链补齐了。现在 taxonomy vocabulary 已经不只是“有维护 helper”，还具备了与日常 export 分离的显式 init 命令；同时 dry-run 也帮助定位出当前 owner 对 master legacy secondary class 的覆盖缺口，为后续 taxonomy owner 补齐提供了直接线索。
