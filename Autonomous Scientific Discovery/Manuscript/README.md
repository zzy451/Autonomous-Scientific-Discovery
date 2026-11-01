# Agent for Science 英文综述源文件

同步日期：2026-11-01。本目录是 Overleaf 英文正文的 GitHub 快照，正文、参考文献、模板及六幅图与本次 Overleaf 发布包一致。后续正文修改应先整合到 Overleaf 工作副本，再同步此快照。

当前版本包含 10 个主章节、42 个小节、6 幅图和 15 张表；正文实际引用 56 条文献，统一 BibTeX 库共 1052 条。参考文献单独保存在 `references.bib`，`main.tex` 仅通过 `\bibliography{references}` 调用。英文稿使用 pdfLaTeX/BibTeX 编译，本地最终页数见 `Coverage_Check/core_tag_alignment_2026-11-01/final_verification.json`；不同 TeX 环境的分页可能略有差异。

## 编译

安装含所需宏包的 TeX Live 或 MiKTeX，以及 Python 3。从本目录运行：

```text
python build_manuscript.py
```

输出为 `build/main.pdf`。编译只依赖本目录，使用已提交图表，不需要重新生成图表或下载文献 PDF。GitHub 的 PDF 资源由 Git LFS 管理，克隆后先运行 `git lfs pull`。

## 图表复现

安装 `matplotlib` 和 `numpy`，从本目录运行：

```text
python scripts/build_framework_figures.py
python scripts/build_landscape_figures.py
```

脚本默认只生成英文图。全景图读取本目录 `data/corpus_landscape_records_2026-11-01.json` 和 `data/core_classification_snapshot_2026-11-01.json` 中的冻结输入，并校验 662 篇核心工作及 935 项非互斥领域归属。正文、图表和当前核心库统一采用2026-11-01分类快照；检索截止日期仍为2026-10-22。旧的2026-10-29冻结文件保留为历史输入，不再驱动当前图形。案例图的数据位于 `data/illustrative_domain_profiles.json`；所选 11 个案例用于定性比较，不能据此估计全库频率。可用 `--chinese-output <本地中文稿目录>` 额外生成中文图，中文字体需要 Microsoft YaHei。

## 补充分析

- [核心库与编码覆盖入口](../Coverage_Check/core_tag_alignment_2026-11-01/README.md)：662篇清单、核心BibTeX、引用桥、逐篇覆盖矩阵、笔记来源索引与待核队列；区分字段有值、词表符合、笔记对齐和独立原文核查。
- [检索来源附录](../Coverage_Check/core_tag_alignment_2026-11-01/search_provenance_appendix.md)：整理45项可恢复历史检索记录及无法重建的边界，不反推完整筛选分母。
- [此前正文原文核查](../Coverage_Check/core_tag_alignment_2026-11-01/manuscript_source_checks.md)：保留六项案例的原文位置与推断限制；第8节当前论证与证据以本轮修订索引为准。

- [第7.1—7.3节跨学科修订记录](analysis/section7_cross_domain_revision_2026-11-01.md)：将知识、数据、反馈与验证的论证扩展至计算、物理天文、地球环境、生命医学、工程、任务系统及社会研究。
- [学科覆盖差异的深化分析](analysis/domain_coverage_imbalance_deepened_2026-10-31.md)：对应正文第 7 节，分析各学科的对象、模态、可观测性、干预及验证条件。
- [科研决策、学科条件与科学增量](analysis/decision_delegation_and_scientific_gains_2026-11-01.md)：对应第8.1–8.3节，记录决策分工、全部11个学科的约束与委托关系，以及含明确基线和终点的比较证据；替代原流程阶段说明。
- [同类任务比较、知识形成与迁移边界](analysis/task_comparisons_discovery_and_transfer_2026-11-01.md)：本日后续修订，记录新增10篇正文引文、独立文献库修正及原文定位；扩展同任务对照、输出转化为知识的过程，以及跨器件、数据集和任务测试的实际边界。
- [自适应决策如何影响科学证据](analysis/adaptive_decisions_and_scientific_evidence_2026-11-01.md)：第8.4节的原文证据及推导条件；分析性质优化与机制辨识、采样分布与推断有效性，以及测量模型和停止决策的科学含义。新增统计方法背景独立于Agent核心库。
- [补充信息清单](analysis/gpt_supplement_information_checklist_2026-10-31.md)：保留原始规划属性，不能当作所有条目均已核实的声明。

中文阅读版、完整编译 PDF、临时草稿、备份和本地验收图留在本地，不属于该发布快照。
