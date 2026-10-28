# jiaming-review：合并与复核交接

本分支提交的是分类审计工具、审计快照和文档，不是已经人工确认的分类修订。合并不会自动改动正式分类。

## 本次修改

- 重写英文 README，保留中文项目说明，增加数据入口、分类边界、复现命令和证据限制。
- 发布逐篇无头 Codex 审计 runner、task prompt 和输出 JSON schema，模型唯一允许值为 `gpt-6.1-sol`。
- 发布分类差异分流脚本，以及 2026-10-27 轮次的 summary、difference 和 triage 快照。
- 用 `.gitignore` 明确允许发布的审计资产。逐篇原始响应、CLI 日志和本轮 PDF 缓存不在本次提交中；仓库既有的 Git LFS 论文资产不变。
- 正式 owner 文件、论文收录状态和分类台账未修改。

## 已完成和未完成

| 项目 | 状态 |
|---|---|
| 核心论文数 | 663；全量结构化记录 1,133 条 |
| 本轮模型结果 | 663 篇完成 |
| 全文证据 | 491 篇 `pdf_full_text` |
| 笔记证据 | 172 篇 `note_only`，不能视作全文已核查 |
| 比较差异 | 1,743 行，涉及 639 篇论文；行数不等于错误数 |
| 人工裁决与正式写回 | 尚未由本轮快照完成；`writeback_performed=false` |

## 合并后如何接续

1. 阅读 README 的 scope/classification 说明、`Data/field_ownership_matrix.md` 和 `skills/asd-single-paper-classification-workflow/SKILL.md`。后续相对路径以 `Autonomous Scientific Discovery/` 为根目录。
2. 保留已提交的日期快照。工作时复制 `manual_review_triage.csv` 到新目录，填写 `review_status`、`human_decision`、`reviewer_notes`，不要用重新生成报告的命令覆盖人工决定。
3. 按 `paper_id` 逐篇打开原论文。优先解决 `source_limited_manual_review`：补齐主文全文和可定位页码；不要把笔记转述直接升级为一手证据。
4. 对照 CSV 中的 `evidence` 与原论文的实验、对象和结果；检查一级、二级、三级标签的增删。多学科按实际科学对象分别判断，taxonomy 缺口应显式保留，不能用不相干代码填满。
5. 原始 `results/ASD-####.json` 保留在本地研究工作区，未随本分支发布。GitHub 上的差异 CSV 含证据节选，但不是全文阅读记录；需要完整模型理由时找回原始结果，或以新目录重跑该论文。
6. 逐条记录证据页码、裁决理由及复核人。仅对确认的改变更新 owner 文件，并追加 `Data/change_log.jsonl`；不要只改派生 CSV、SQLite 或 `papers.jsonl`。
7. 在完整研究工作区运行正式管线，检查通过后再单独提交分类更正。模型建议与人工决定应保持可追溯。

## 小批量复跑

安装 Python 3.11+、已认证的 Codex CLI 和 `pdftotext`。从项目目录运行：

```bash
cd "Autonomous Scientific Discovery"
python3.11 scripts/audit_classifications_with_codex.py \
  --run-dir Coverage_Check/jiaming_review_followup \
  --model gpt-6.1-sol --paper-id ASD-0001 --jobs 1
python3.11 scripts/triage_classification_differences.py \
  --run-dir Coverage_Check/jiaming_review_followup
```

`ASD-0001` 是示例，换成待查 `paper_id`。`--pdf-override /absolute/path/paper.pdf` 可为单篇指定完整 PDF；`--context-file PATH` 或 `--context-dir PATH` 可附加上下文。先验证一篇，再使用 `--limit N` 或移除单篇限制扩大范围。不要改用其他模型。

## 正式数据写回顺序

遵循字段 owner 表：论文与模块事实在 master/progress 中维护；二三级映射在 `paper_module_taxonomy_assignments.jsonl` 中维护；学科码生命周期在 `discipline_code_assignments.jsonl` 中维护；词表变更在 `classification_code_index.json` 中维护。然后执行：

```bash
python3.11 scripts/run_structured_data_pipeline.py
```

此管线依次 export → check → build。任何 ERROR 都应修复 owner 根因；来源不足保留为待查，不要平衡填充或强行更正。

## 本次验证和已知限制

- 两个新脚本通过 Python 3.11 编译及 `--help` 检查；模型参数只接受 `gpt-6.1-sol`。
- 已核对审计 JSON/CSV 的行数、唯一论文 ID、差异类型计数与证据 JSON，并验证英文和中文 README 的本地文件链接；均通过。
- 原有 `check_data_consistency.py` 在原始 GitHub checkout 中因缺少派生文件 `Data/taxonomy_index.json` 中断，不能据此宣称完整数据一致性检查已通过。
- 若要完成全量一致性检查，应在具备原始 owner、笔记、证据与派生资产的研究工作区运行正式管线，并检查生成报告；本分支不通过复制过期派生文件来掩盖缺失。
