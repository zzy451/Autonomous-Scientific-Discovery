# 检索来源与可复现边界

本附录整理真实留存的检索记录，不将当前662篇核心工作反推为历史筛选流程。文献广泛收集截止2026-10-22；分类和证据整理快照为2026-11-01。此后对已登记工作的版本核查不构成新增文献检索轮次。

| 环节 | 留存来源与可核查内容 | 局限 |
|---|---|---|
| 种子来源 | 上海人工智能实验室种子综述及其引文网络；主表Remarks保留Source trail，部分条目保留seed reference编号 | 引文扩展并非全部留存逐次查询时间，不能重建完整候选分母 |
| 期刊入口 | Nature、Science及相关期刊；十月第二轮B/C组记录和主控期刊发现记录 | 题名匹配和来源发现有覆盖偏差，期刊入口不等于逐刊穷尽检索 |
| 通用科研方法 | october_round2_A_general.json中的search_log | 旧OpenAlex逐条缓存未完整保留；部分为聚合记录，不能逐条重筛或计算召回率 |
| 化学与材料 | october_round2_B_chem_materials.json及相应日志，保留来源收集、DOI核查与去重过程 | 来源返回数与筛选工作数不同，不能相加作为文献总量 |
| 生命与医学 | october_round2_C_life_health.json及日志，保留时间窗、查询、来源核查和失败 | 平台限流和全文可得性影响判断深度 |
| 形式科学与物理天文 | october_round2_D_formal_physics.json中的searches、citation_expansion；arXiv API和官方检索页记录 | 物理查询返回384条；数学查询受429限流，返回1600/报告6530，属于不完整检索，不能将6530称为已筛工作数 |
| 地球环境、农业、工程与任务系统 | october_round2_E_earth_agri_engineering.json中的search_log、screened_out | 多条查询的返回重叠，且不少为泛AI应用或单步预测，不能直接视为合格Agent工作 |
| 社会与知识系统 | october_round2_f_knowledge.json中的searches及screening_records | MD日志局部编码损坏，使用仍可解析的结构化JSON，不凭乱码重造查询 |
| 去重与版本 | 主表稳定Paper_ID，DOI/arXiv/规范化标题与版本关系；bib审计记录 | 标识符可辅助合并，不能仅因名称相同合并实质不同的后续研究 |
| 纳入与学科归属 | review_scope_and_classification_policy.md、ASD_annotation_schema.md、主表及模块细分owner | 分类规则可复查，不等于所有决定均经独立多评审者全文核实 |

六组JSON中的可恢复查询记录原样抽取至`recoverable_search_records.json`，逐项携带文件路径、SHA-256及JSON位置；记录既包含精确查询也包含历史聚合描述，两者不能当作同等完整的检索日志。主控制表为`Paper_Lists/october_round2_search_control_2026-10-22.md`，结果与失败边界见`Coverage_Check/october_round2_literature_expansion_report_2026-10-22.md`。日期为历史记录原值，不改写为本轮整理日期。

部分原始发现缓存仅在本地工作区`.tmp_asd_pdfs/`保留，包括`round2_journals/harvest_expanded.json`、`october_D_arxiv_api_retrieval.json`与`october_D_official_search_pages.json`。它们不是全部历史检索的完整档案，亦不是稿件编译依赖。公开复现入口保留上述六组已登记记录及其来源指针。

目前可以复现的是：从既有主表与owner重建核心清单、学科归属和编码覆盖，并检查留存的查询记录。无法完整复现的是：所有历史检索、未存档返回、每次人工筛选顺序及真实全体候选分母。因此本文定位为结构化文献映射与定性证据综合，不报告PRISMA筛选流、检索召回率或无实测依据的评审者间一致性指标。
