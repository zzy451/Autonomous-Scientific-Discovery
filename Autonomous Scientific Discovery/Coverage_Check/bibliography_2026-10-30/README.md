# 统一 BibTeX 文献库（2026-10-30）

`Agent_for_Science_Review_Overleaf/references.bib` 是当前综述的统一文献数据库。它收录核心库 663 条记录、背景/综述记录 381 条，以及分类体系与项目政策等来源；去重后共 1051 个 BibTeX 条目。正文已经改为 `\bibliography{references}`，不再在 `main.tex` 或 `references.tex` 中手写 `thebibliography`。

正文引用使用条目的键，例如 `\cite{asd0001}`、`\cite{feng2026}`、`\cite{projecttaxonomy}`。全部数据库条目都会保留，但参考文献表只输出正文实际引用的条目，这是 BibTeX 的正常行为；需要列出某个未在正文出现的条目时，再在正文加入相应引用。

书目信息优先来自本地 `Data/papers.jsonl` 和原有手写条目；随后用 Crossref、arXiv 的公开记录按 DOI、arXiv 编号或标题/年份进行保守核对。在线查询结果、匹配审计和缓存位于本目录的 `online_metadata/`、`online_lookup_audit.json` 和 `online_overrides.json`。没有可靠匹配时保留本地信息，不用猜测补写作者或页码。

本次生成统计：BibTeX 条目 1051；核心记录 663；背景记录 381；正文引用键 44。当前仍有部分原始记录作者缩写、年份格式或标识符不完整，详见 `build_report.json` 和 `paper_citation_keys.csv`。这些标记用于后续书目清理，不影响已验证的引用键解析。

## 重新生成

```text
D:/python/python.exe Autonomous Scientific Discovery/scripts/enrich_review_bibliography.py --cached-only
D:/python/python.exe Autonomous Scientific Discovery/scripts/build_review_bibliography.py
D:/python/python.exe Agent_for_Science_Review_Overleaf/build_manuscript.py
```

`build_manuscript.py` 会依次运行 pdfLaTeX、BibTeX 和两次 pdfLaTeX，并在发现未解析引用时失败。原手写版本保存在 `Coverage_Check/bibliography_2026-10-30/references_handwritten_original.tex`。
