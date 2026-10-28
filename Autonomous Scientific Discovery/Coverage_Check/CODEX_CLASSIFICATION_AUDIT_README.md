# Codex 逐篇分类审计

`scripts/audit_classifications_with_codex.py` 对每个 `active_confirmed_core` 论文启动一次无头 `codex exec`，固定使用 `gpt-6.1-sol`，把 PDF 全文（优先本地真实 PDF，其次官方 arXiv 或 OpenAlex 列出的开放获取 PDF）和项目分类边界发送给 Codex。若用户配置加载了插件市场，runner 会在单篇子进程中跳过插件同步，并显式恢复 Codex provider、审批策略和 service tier。现有 Note、旧分类和台账只作为比较对象，不作为模型的分类依据。

每篇结果保存在 `results/ASD-####.json`，原始 JSON 和 CLI 日志分别保存在 `raw/`、`logs/`。任务可中断后重新运行，已完成结果会跳过；失败结果记录在 `errors.jsonl`，不会阻止其余论文继续。脚本默认使用只读 Codex 沙箱，并且不写 `papers.jsonl`、分类台账或其他 owner 文件。

示例：

```bash
python3.11 scripts/audit_classifications_with_codex.py \
  --run-dir Coverage_Check/codex_classification_audit_gpt-6.1-sol_2026-10-27 \
  --jobs 4 --reasoning-effort low --timeout 900
```

审计完成后查看：

- `classification_differences.csv`：模型与当前模块、二级/三级码、`01.04` 的差异，以及来源限制。
- `manual_review_queue.csv`：逐条人工复核队列。确认前不要把 `human_decision` 写回正式数据。
- `manual_review_triage.csv`：按复核原因分流后的队列；标记旧代码清理、taxonomy 缺口、来源不足、模型不确定、模块边界和有效代码语义冲突，也标记重复基线比较行。
- `manual_review_triage_summary.json`：分流统计；`writeback_performed` 始终为 `false`。
- `summary.json`：完成/失败数量、证据来源数量和差异类型统计。

生成分流队列：

```bash
python3.11 scripts/triage_classification_differences.py \
  --run-dir Coverage_Check/codex_classification_audit_gpt-6.1-sol_2026-10-27
```

人工复核时必须回到 `results/ASD-####.json` 的 `object_evidence`，检查 PDF 页码/章节中的具体对象和结果；`source_type` 为 `note_only` 或 `metadata_only` 的记录不能视为已逐篇读过全文。分流报告只是复核队列，不代表争议已经裁决。复核完成后，按项目单篇分类流程更新 owner 文件，再运行正式数据管线；审计和分流脚本都不会自动写回分类。
