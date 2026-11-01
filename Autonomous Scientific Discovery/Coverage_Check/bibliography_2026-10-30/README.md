# 统一 BibTeX 文献库（2026-10-30）

`Manuscript/references.bib`（本地 Overleaf 工作副本为 `Agent_for_Science_Review_Overleaf/references.bib`） 是当前综述的统一文献数据库。它收录核心库 663 条记录、背景/综述记录 381 条，以及分类体系与项目政策等来源；去重后共 1051 个 BibTeX 条目。正文已经改为 `\bibliography{references}`，不再在 `main.tex` 或 `references.tex` 中手写 `thebibliography`。

正文引用使用条目的键，例如 `\cite{asd0001}`、`\cite{feng2026}`、`\cite{projecttaxonomy}`。全部数据库条目都会保留，但参考文献表只输出正文实际引用的条目，这是 BibTeX 的正常行为；需要列出某个未在正文出现的条目时，再在正文加入相应引用。

书目信息优先来自本地 `Data/papers.jsonl` 和原有手写条目；随后用 Crossref、arXiv 的公开记录按 DOI、arXiv 编号或标题/年份进行保守核对。本次公开保留生成器需要的 `online_overrides.json`、`online_metadata/extra_sources.json`、原手写条目和经过裁定的覆盖文件；完整在线查询缓存与中间结果保留在本地。全库核查结果和最终覆盖文件见相邻的 `bibliography_full_audit_2026-10-31/`，正文版本裁定见 `manuscript_evidence_audit_2026-10-30/audited_bibliography_overrides.json`。没有可靠匹配时保留本地信息，不用猜测补写作者或页码。

本次生成统计：BibTeX 条目 1051；核心记录 663；背景记录 381；正文引用键 44。当前仍有部分原始记录作者缩写、年份格式或标识符不完整，详见 `build_report.json` 和 `paper_citation_keys.csv`。这些标记用于后续书目清理，不影响已验证的引用键解析。

## 重新生成

```text
python "Autonomous Scientific Discovery/scripts/build_review_bibliography.py"
python "Autonomous Scientific Discovery/Manuscript/build_manuscript.py"
```

`build_manuscript.py` 会依次运行 pdfLaTeX、BibTeX 和两次 pdfLaTeX，并在发现未解析引用时失败。原手写版本保存在 `Coverage_Check/bibliography_2026-10-30/references_handwritten_original.tex`。

生成器优先更新本地 Overleaf 工作副本；该目录不存在时更新仓库内的 `Manuscript/` 快照。重新生成后，应检查与已裁定书目的差异，再同步英文正文和中文阅读版。2026-10-31 核查报告中的 43 个引用键是当时的历史状态；本次正文快照实际使用 44 个引用键。
