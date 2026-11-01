# 核心库标签对齐与编码覆盖（2026-11-01）

本轮沿用既有 annotation schema、主表和笔记。覆盖矩阵是派生盘点，不另设分类事实源。空值表示未记录；旧扩展值保留原文进入核查队列，不表示该能力不存在。

核心工作662篇，正式领域660篇，独立通用方法桶2篇；学科归属935项，二级933项，三级931项。笔记662份，本地PDF635份。

| 副标签字段 | 主表有值 | 全部词元符合既有schema | 本轮逐字段笔记对齐 |
|---|---:|---:|---:|
| agent_type | 648 | 581 | 143 |
| research_workflow_role | 652 | 261 | 144 |
| validation_type | 649 | 326 | 107 |
| scientific_contribution_type | 660 | 242 | 128 |

词表符合不等于原文核实；本轮笔记对齐不冒充独立全文复核。自主能力与交叉属性在既有笔记内，其原始值和行号见note_tag_source_index.csv，不能因主表无专栏而报告为零覆盖。

六类科研角色是既有13个细标签的正文聚合，映射见role_aggregation_mapping.json。六种决策机制、协作拓扑、科学贡献归因与人类决策职责尚未完成全库编码；11个目的性案例仅支持定性比较。

ASD-0547/04、ASD-0919/05、ASD-0919/11、ASD-0925/02仍缺三级；其中0919/05与0925/02也缺二级。既有证据不足，本轮保持原判。

入口：core_corpus_manifest.csv/jsonl（662行）、core_references.bib（662条）、core_reference_bridge.csv、coding_coverage_matrix.csv、tag_evidence_review_queue.csv。详细变更证据见applied_changes.json与reviewer_*.json。

清单、矩阵与检索索引等派生输出可运行 scripts/build_core_evidence_package.py 从当前owner和留存审阅记录重建；reviewer文件及原文核查记录保留为本轮证据。核心成员或快照变化时须另建日期包，不能把本日期作为后续变动的隐式容器。
