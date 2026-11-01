# Agent for Science 英文综述源文件

同步日期：2026-11-01。本目录是 Overleaf 英文正文的 GitHub 快照，正文、参考文献、模板及六幅图与本次 Overleaf 发布包一致。后续正文修改应先整合到 Overleaf 工作副本，再同步此快照。

当前版本包含 10 个主章节、42 个小节、6 幅图和 14 张表；正文实际引用 44 条文献，统一 BibTeX 库共 1051 条。英文稿在本地使用 pdfLaTeX/BibTeX 编译为 32 页；不同 TeX 环境的分页可能略有差异。

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

- [第7.1—7.3节跨学科修订记录](analysis/section7_cross_domain_revision_2026-11-01.md)：将知识、数据、反馈与验证的论证扩展至计算、物理天文、地球环境、生命医学、工程、任务系统及社会研究。
- [学科覆盖差异的深化分析](analysis/domain_coverage_imbalance_deepened_2026-10-31.md)：对应正文第 7 节，分析各学科的对象、模态、可观测性、干预及验证条件。
- [共同科研流程与智能体参与](analysis/shared_research_workflow_and_agent_participation_2026-11-01.md)：对应第 8.1、8.3 节及结论，区分阶段覆盖、操作权限、自适应控制和科学判断。
- [补充信息清单](analysis/gpt_supplement_information_checklist_2026-10-31.md)：保留原始规划属性，不能当作所有条目均已核实的声明。

中文阅读版、完整编译 PDF、临时草稿、备份和本地验收图留在本地，不属于该发布快照。
