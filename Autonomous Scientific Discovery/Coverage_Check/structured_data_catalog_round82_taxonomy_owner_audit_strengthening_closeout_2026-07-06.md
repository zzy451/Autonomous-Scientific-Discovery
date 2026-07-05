# Structured Data Catalog Round 82 Closeout

日期：2026-07-06

## 本轮目标

继续把 execution audit 往长期方案的 taxonomy owner 要求靠拢，补强 `classification_code_index.json` 的结构与下游镜像校验。

## 本轮修改

修改：

- `scripts/audit_execution_definition.py`

本轮补强内容：

1. 第 4 项
   - 不再只检查 `classification_code_index.json` 是否存在及带少数顶层键
   - 现在要求：
     - `primary_terms` 非空
     - `secondary_terms` 非空
     - `primary_terms` 每项包含：
       - `primary_code`
       - `label`
       - `definition`
       - `include`
       - `exclude`
       - `status`
       - `source`
     - `secondary_terms` 每项包含：
       - `secondary_code`
       - `parent_primary_code`
       - `label`
       - `definition`
       - `include`
       - `exclude`
       - `status`
       - `source`
       - `review_status`

2. 第 7 项
   - 不再只做 taxonomy owner 文件存在性确认
   - 现在要求：
     - `classification_code_index.json` 存在
     - SQLite `classification_terms` 行数必须等于
       - `len(primary_terms) + len(secondary_terms)`
   - 当前验证结果为：
     - `classification_terms = 52`

## 验证

运行：

```bash
python "Autonomous Scientific Discovery/scripts/run_structured_data_pipeline.py" --with-execution-audit
```

结果：

- `export_structured_data.py` 通过
- `check_data_consistency.py` 通过
- `build_analysis_db.py` 通过
- `audit_execution_definition.py` 通过

执行定义审计结果：

- `PASS=12`
- `FAIL=0`

本轮后，第 4 / 7 项当前输出分别为：

> classification_code_index.json exists and exposes non-empty taxonomy-owner primary/secondary term structures with definition/include/exclude/status/source fields.

> classification_code_index.json is present as taxonomy vocabulary owner and mirrors into SQLite classification_terms=52.

## 产出判断

本轮让 taxonomy owner 的 execution audit 证据从“存在性”升级为：

- owner 词表结构完整
- downstream SQLite vocabulary mirror 对齐

这更接近长期方案里对 taxonomy vocabulary owner 的正式要求。

## 后续状态

当前无代码级阻塞，可继续沿剩余证据较弱的执行定义条目推进。
