# Structured Data Catalog Round 107 Closeout

日期：2026-07-06

## 本轮目标

继续把 registry derived layer 从“字段长得对”推进到“内容集合也必须严格等于 export 规则推导结果”。本轮聚焦 `Data/registry/paper_identifier_aliases.jsonl`，补齐 DOI / arXiv / URL alias 的精确镜像校验。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 新增 URL 提取辅助函数

新增：

- `extract_urls_from_text()`

逻辑与 `export_structured_data.py` 中 alias 导出使用的 URL 提取规则保持一致：

- 从 `doi_or_url` 文本中提取所有 `http/https` URL
- 做同样的尾部符号清洗
- 保持去重但不引入新排序语义

这样 check 阶段可以按与 export 相同的规则重建期望 alias 集合。

### 2. alias 值 trim 约束

在 `paper_identifier_aliases` 校验中新增：

- `alias_value` 必须已经被去掉首尾空白

这保证 alias registry 中不会留下仅因为空白差异造成的脏别名。

### 3. alias registry 精确集合镜像校验

本轮新增：

- 从 `papers.jsonl` 为每篇论文重建期望 alias 集合
  - `doi` -> `alias_scheme = doi`
  - `arxiv_id` -> `alias_scheme = arxiv_id`
  - `doi_or_url` 中提取出的 URL -> `alias_scheme = url`
- 要求 `paper_identifier_aliases.jsonl` 的实际 `(paper_id, alias_scheme, alias_value)` 集合与该期望集合完全一致

这意味着现在不仅会拦：

- 缺 alias
- 多 alias
- 错 alias

还会拦：

- alias 值被错误清洗
- URL 提取集合和 export 规则不一致

### 4. `paper_identifier_aliases` 从“弱合法性检查”升级为“强镜像校验”

此前 alias registry 主要只检查：

- `paper_id` 存在
- `alias_scheme` 在合法枚举中
- `alias_value` 非空
- `is_primary_key = false`

本轮之后，它已经提升为真正受 `papers.jsonl` 事实派生约束的 identity registry。

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

本轮把 `paper_identifier_aliases.jsonl` 从“别名字段表”推进成了“受 exact set 校验的 papers identity 派生层”。这和方案里 registry 负责提供稳定映射、但不能静默漂移为手工信息堆积层的要求是一致的。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 asset / PDF registry、更细的 SQLite 语义对齐、以及 remaining derived metadata 约束逐轮推进。
