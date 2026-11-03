# 六类决策机制分类：GitHub 发布说明

发布日期：2026-11-03。对应 2026-11-01 冻结核心库的 662 篇论文。

## 已发布内容

- 最终结果：Excel、CSV、JSONL、中文分组列表、中文汇总报告和领域 × 机制统计。
- 判定口径：操作定义、边界裁决、15 篇暂定复核队列。
- 审阅轨迹：三个分片的原始审阅、主控覆盖记录，以及 76 篇独立交叉复核记录。
- 汇总与校验：类别统计、源文件完整性检查、交付与原文摘录校验记录。
- 输入与脚本：三个冻结输入包、分片清单、汇总和核验脚本，以及分类时的来源哈希和文件清单。

临时的 PDF 全文抽取缓存、辅助脚本和中间定位文件留在本地。论文的既有笔记和 PDF 仍通过主仓库的 `Notes/` 与 `Reference_PDF/` 查找。

## 如何读取

先看 [README.md](README.md)，逐篇查看使用 [Excel](classification_results_662.xlsx) 或 [CSV](classification_results_662.csv)。`paper_id` 是与核心清单、笔记及引用桥关联的键。每篇只有 D1—D6 中一个主标签；置信度和暂定状态是独立字段。

本次结果不回写原主表、原结构化数据、原笔记或正文。旧覆盖矩阵反映 11 月 1 日状态，新六类分类反映 11 月 3 日增量；二者应通过 ID 关联使用。

## 复核与重建

`reviewer_A/B/C.jsonl` 保留初审，`controller_review.jsonl` 保留主控覆盖。最终结果由输入包、初审和主控覆盖共同形成。独立交叉复核见 `scratch/A/cross_review.jsonl` 与 `scratch/C/cross_review_A_D6.jsonl`。

`assemble_results.py` 可从保留记录重建派生结果，但会写入本目录，复核时应在副本中运行。源文件完整性检查中的时间戳和文件清单描述分类当时的本地工作区；克隆后的文件时间戳不同，不应解释为论文内容遭到改写。

`verify_deliverables.py` 检查最终表和原文摘录，需要 Python、PyMuPDF、openpyxl 及已获取实际内容的归档 PDF。83 条直接原文摘录中有 1 条来自未随本包发布的历史 HTML 缓存；新克隆环境应根据该条记录的 `source_url` 和 `primary_source_locator` 补取来源。保留的 `deliverable_verification.json` 是分类完成时的核验记录，不能替代新环境重新获取来源后的检查。
