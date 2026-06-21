# 451 篇文献多模块分类、Note 与 PDF 全量复核计划

日期：2026-06-21

## 1. 任务目标

本轮任务是对当前 451 篇 confirmed core 文献重新进行完整复核，并同步完成三件事：

1. 依据论文原文或一手来源，重新判断每篇文献的 relaxed multi-module 分类。
2. 修改对应 note 中仍残留的旧单模块 / 单主类口径，以及缺少原文证据支撑的分类表述。
3. 将每篇文献可合法获取的 PDF 下载并归档到 `Reference_PDF/` 下的相应位置，作为后续复核和写作的本地证据资产。

本轮复核以 `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 中当前 451 篇 confirmed core 文献为平铺主索引展开。`Notes/` 只作为定位对应论文、核对 note path 和后续修订的配套线索层，不作为分类权威。

## 2. 最高证据原则

分类、note 修改和 master-list 更新必须以一手来源为准。

证据优先级：

1. 论文 PDF / full text
2. arXiv / official preprint
3. DOI landing page / publisher page
4. publisher abstract
5. supplementary material
6. official benchmark / project page / official GitHub
7. 旧 note、旧 Coverage_Check 报告、legacy master-list 字段

第 7 类只能作为查找线索，不得作为最终分类依据。若旧 note 与原文证据冲突，应以原文为准并同步修订 note。

如果 PDF 或全文无法合法获取，不硬化中等置信度判断；将该文献标记为 `source_limited`，并写入 full-text follow-up queue。

## 3. 当前多模块分类口径

本轮采用 relaxed multi-module scientific-object coverage rule：

- 论文必须先满足 Agent 最低纳入标准：明确科研目标、多步行动过程、至少一种 Agent 能力、在科研流程中承担明确角色。
- 论文进入哪些 `01-11` scientific-object modules，由其实际研究、实验、验证、benchmark task、case study 或 reported results 覆盖的科学对象决定。
- 只要某一模块有可识别 object-level evidence，即可记录该模块。
- 不要求每个模块都是论文核心科学贡献。
- 不能因为系统通用、平台化、多 Agent 或 workflow 化，就自动退回 `01.04`。
- `01.04` 只作为独立 general-method bucket，用于没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告的 ASD / general research-agent 方法文献。
- `primary_module_for_filing` 只用于 PDF / note 路径和 legacy 展示，不是唯一分类事实。

## 4. 工作入口：按 Master List 中的 451 篇平铺，不按优先级

本轮不按风险优先级、不按领域优先级、不先做容易论文。

主控代理先从 `agent_master_paper_list.md` 中提取固定待复核索引：

```text
agent_master_paper_list.md 中 Inclusion status 为 `to_read` 或 `included` 的当前 451 篇 confirmed core records
```

排序规则：

1. 以 `agent_master_paper_list.md` 中这 451 篇记录的当前行顺序为唯一平铺顺序基准。
2. 逐条读取每篇记录的 `paper ID`、title、status、legacy filing fields、note path、URL / DOI / remarks。
3. 再根据该记录去定位对应 note、PDF 和一手来源。
4. 对缺 note、note path 不一致、title 不一致或 ID 对不上的情况，单独列入 `note_masterlist_alignment_issue`。

每篇待复核论文都必须先在主列表中占有一个明确记录，再去定位它的 note。复核时不能沿用 note 里的旧分类结论，只能用 note 帮助定位 title、DOI、URL、已有引用线索和本地上下文。

## 5. PDF 下载与归档规则

PDF 根目录：

```text
Autonomous Scientific Discovery/Reference_PDF/
```

建议目录结构：

```text
Reference_PDF/
  01_Formal_Information_and_Computational_Sciences/
  01_04_General_Method_Bucket/
  02_Physics_Astronomy_and_Space_Sciences/
  03_Chemical_Sciences/
  04_Materials_Science/
  05_Earth_and_Environmental_Sciences/
  06_Life_Sciences/
  07_Medical_and_Health_Sciences/
  08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/
  09_Engineering_and_Industrial_Technology_Sciences/
  10_Aerospace_Marine_and_Transportation_Sciences/
  11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/
  _source_limited/
```

PDF 存放原则：

- 每篇文献只保存一份 PDF，避免多模块论文重复存储。
- PDF 按 `primary_module_for_filing` 选择目录；这只是归档路径，不代表唯一分类。
- 如果文献进入 `01.04` general-method bucket，则放入 `01_04_General_Method_Bucket/`。
- 如果全文无法合法下载，但有 DOI / publisher page / abstract，则不伪造 PDF；在 batch report 和 note 中记录 `source_limited`。
- 如果只能获得 HTML full text 而无 PDF，记录 HTML 来源 URL，并在 note 中说明 `PDF unavailable; HTML full text checked`。
- 若存在多个版本，优先保存 publisher PDF；若 publisher PDF 不可用，保存 arXiv / official preprint PDF，并在 note 中说明版本。

PDF 命名规则：

```text
FirstAuthor_Year_ShortTitle.pdf
```

如存在重名：

```text
FirstAuthor_Year_ShortTitle_VenueOrID.pdf
```

每篇 note 的 `Evidence Log` 或论文信息区应补充：

```text
PDF path:
First-hand source checked:
PDF version:
```

## 6. 批次设计

总量：451 篇。

建议每批 30 篇，先做一个小规模试运行。

- Batch 00：主列表平铺索引前 10 篇，测试流程、PDF 归档、note 修改深度、master-list 更新方式。
- Batch 01：001-030
- Batch 02：031-060
- Batch 03：061-090
- Batch 04：091-120
- Batch 05：121-150
- Batch 06：151-180
- Batch 07：181-210
- Batch 08：211-240
- Batch 09：241-270
- Batch 10：271-300
- Batch 11：301-330
- Batch 12：331-360
- Batch 13：361-390
- Batch 14：391-420
- Batch 15：421-450
- Batch 16：451 及索引对齐遗漏项

每批必须按主列表中的平铺索引顺序推进，不得因为某些论文看起来更重要、更容易或更有争议而改变顺序。

## 7. Agent 团队组织

默认采用固定多 Agent 小团队。自 `2026-06-21` 起，本节即为 451 篇 confirmed-core full reaudit 的唯一执行口径，覆盖旧的“主控单线写回”为主的做法。核心目标不是把所有动作都塞给 `Main Controller`，而是把取证、独立裁决、note 写回、master/progress/report 单写者收口明确拆开。

### 7.1 标准团队拓扑

- `Main Controller`
  - 只保留最终裁决与单写者职责。
  - 建立平铺批次索引。
  - 按当前主列表行顺序分发任务。
  - 统一 relaxed multi-module 判定口径。
  - 复核 evidence packs 与 `Classification-Reviewer` 的独立裁决。
  - 决定哪些记录本轮立即落地，哪些继续保守挂起。
  - 唯一编辑 `agent_master_paper_list.md`。
  - 唯一重算统计。
  - 唯一更新 progress tracker。
  - 唯一定稿 partial / batch report。
  - 唯一提交 git。

- `Evidence-Agent-A`
  - 负责本轮平铺批次前 1/3 的连续切片。
  - 只读查找一手来源。
  - 提取 Agent 纳入证据、科学对象、object-level experiment / benchmark / case / result 证据。
  - 建议 PDF 最优归档来源与版本。
  - 显式标记 `source_limited` 或安全 / 访问阻塞。

- `Evidence-Agent-B`
  - 负责本轮平铺批次中 1/3 的连续切片。
  - 职责同上。

- `Evidence-Agent-C`
  - 负责本轮平铺批次后 1/3 的连续切片。
  - 职责同上。

- `Classification-Reviewer`
  - 只读，且不以旧 note 结论为权威。
  - 只根据 evidence packs 独立裁决 `supported modules`、`01.04` bucket、`boundary type`、`confidence`。
  - 标记 `note_revision_required`、`master_update_required`、`source_limited`、`safety_access_status`。
  - 输出可直接供 `Main Controller` 决定是否落地的结果。

- `Writeback-Agent-1`
  - 只负责一组互不重叠的 note 文件。
  - 只根据 `Main Controller` 已批准落地的最终裁决写回 note。
  - 可同步刷新 evidence log、PDF path、first-hand source、classification wording、source-limited / safety wording。

- `Writeback-Agent-2`
  - 负责第二组互不重叠的 note 文件。
  - 约束同上。

- `Writeback-Agent-3`
  - 负责第三组互不重叠的 note 文件。
  - 约束同上。

- `PDF-Archive-Agent`（可选）
  - 只负责已批准落地记录的 PDF 下载、归档与可访问性确认。
  - 可写入 `Reference_PDF/` 对应路径。
  - 不得编辑 master list、progress、report 或 note。

### 7.2 权限矩阵与 ownership 纪律

单写者文件：

- `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md`
- `Autonomous Scientific Discovery/Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Autonomous Scientific Discovery/Coverage_Check/` 下的 partial / batch report

允许并行写入的文件：

- `Autonomous Scientific Discovery/Notes/` 下的 note 文件，但同一轮必须严格分配给互不重叠的 `Writeback-Agent-1/2/3`

允许并行落地的空间：

- `Autonomous Scientific Discovery/Reference_PDF/`，但同一篇 paper 的 canonical PDF 在同一轮只能由一个执行者负责落地

硬性纪律：

- `Main Controller` 不再承担默认 note 写回主力，只承担最终收口。
- `Evidence-Agent-A/B/C` 与 `Classification-Reviewer` 默认只读，不得修改项目文件。
- `Writeback-Agent-1/2/3` 不得编辑 `agent_master_paper_list.md`、progress tracker、partial / batch report、git 历史。
- 一个 note 文件在同一轮只能属于一个 `Writeback-Agent`。
- 一个 paper 的 master 条目只有在其 note 写回返回并经 `Main Controller` 复核后，才允许落地 master 更新。
- 如某篇文献因安全性原因不得继续访问，必须显式标记为 `not accessed due to safety`，不得被隐去或伪装成普通 `source_limited`。

### 7.3 发包与回包契约

每个子 Agent 必须收到显式 launch packet，不能依赖隐含上下文。

发给 `Evidence-Agent-A/B/C` 的任务包至少包含：

- 本轮平铺批次中的连续 paper slice
- `paper_id`
- `title`
- `note_path`
- 当前 master 中可见的 DOI / URL / remarks 线索
- “旧 note 只作线索，不是分类权威”的提醒
- “只读，不改项目文件”的明确约束
- evidence output contract

发给 `Classification-Reviewer` 的任务包至少包含：

- 合并后的 evidence packs
- 当前 relaxed multi-module scientific-object coverage rule
- “不得以旧 note 结论为权威”的明确约束
- 需返回可直接支持落地裁决的字段要求

发给 `Writeback-Agent-1/2/3` 的任务包至少包含：

- 已由 `Main Controller` 批准落地的 paper 清单
- 每个 agent 独占的 note 文件清单
- 每篇 paper 的最终裁决字段
- 需要刷新的 note 段落或 section 提示
- PDF path / first-hand source / source-limited / safety 状态
- “不得编辑 master / progress / report”的明确约束

发给 `PDF-Archive-Agent` 的任务包至少包含：

- 已批准落地的 paper 清单
- 推荐 PDF 来源与优先级
- `primary_module_for_filing`
- 目标 `Reference_PDF/` 路径
- “不得编辑 note / master / progress / report”的明确约束

每轮回包时必须检查：

- `Evidence-Agent-A/B/C` 是否逐篇返回 `first_hand_sources_checked`、`recommended_pdf_url_or_status`、`suggested_modules`、`source_limited`、`safety_or_access_note`
- `Classification-Reviewer` 是否逐篇返回 `supported_modules`、`final_01_04_bucket`、`confidence`、`source_limited`、`safety_access_status`
- `Writeback-Agent-1/2/3` 是否返回 owned files、changed files、untouched files、blockers，以及是否完成 archive-sync / classification wording update
- `PDF-Archive-Agent` 是否返回成功归档路径、失败原因、是否属于 safety skip

### 7.4 标准轮次流程与降级规则

标准轮次流程：

1. `Main Controller` 从 `agent_master_paper_list.md` 提取下一批 confirmed core 平铺记录，严格保持当前行顺序。
2. 将本轮批次切成三个连续 slices，发给 `Evidence-Agent-A/B/C` 并行取证。
3. 合并 evidence packs，仅把证据包发给 `Classification-Reviewer` 独立裁决。
4. `Main Controller` 根据证据强度、分类清晰度、写回风险，决定哪些 paper 本轮落地，哪些继续保守挂起。
5. 如本轮 PDF 获取量较大或归档步骤明显拖慢主流程，启动 `PDF-Archive-Agent`；否则由 `Main Controller` 或写回前的单独步骤完成 PDF 落地确认。
6. 把已批准落地的 note 文件拆分给 `Writeback-Agent-1/2/3` 并行写回。
7. `Main Controller` 统一检查 note diffs，再唯一更新 master、progress、report、统计与 git。
8. 本轮结束后关闭本轮全部子 Agent，避免并发槽位被历史 round 长期占用。

落地判定建议：

- 满足一手证据较强、模块判断清晰、note 写回边界明确时，本轮直接落地。
- 只有 abstract / snippet 级证据、模块扩展仍明显依赖推断、或 source-limited 风险过高时，本轮保守挂起，不强行更新 master。

降级规则：

- 并发充足时，使用完整结构：`Evidence-Agent-A/B/C + Classification-Reviewer + Writeback-Agent-1/2/3 + Main Controller`，并按需启用 `PDF-Archive-Agent`。
- 并发稍紧时，优先保留 `Evidence-Agent-A/B/C + Classification-Reviewer + Main Controller`，减少写回并发数，但不取消角色分离。
- 如再降级，可暂时不开 `PDF-Archive-Agent`，由主控或写回前步骤补做 PDF 归档确认。
- 最后才回退到 `Main Controller` 单独写 note；即使降级，也不应回退到“主控吞掉取证、裁决、写回、master 全链路”的旧模式。

推荐同步维护的 orchestration skill：

```text
C:\Users\20683\.codex\skills\asd-reaudit-multi-agent-orchestration\SKILL.md
```

该 skill 应与本节保持同口径；若后续团队拓扑、写回 ownership 或发包回包契约继续演化，必须同步更新计划文件第 7 节与该 skill，避免两套规范漂移。

## 8. 每篇文献的 evidence pack 格式

每篇文献复核时，至少形成以下字段：

```text
paper_id:
title:
note_path:
current_master_status:
current_legacy_class:
first_hand_sources_checked:
pdf_download_status:
pdf_path:
pdf_version:
agent_inclusion_evidence:
concrete_scientific_objects:
object_level_experiments_or_results:
supported_scientific_object_modules:
general_method_bucket:
object_coverage_mode:
primary_module_for_filing:
module_assignment_evidence:
note_sections_to_update:
master_list_changes_needed:
boundary_notes:
confidence:
source_limited_or_fulltext_required:
```

Evidence pack 可以先存在 batch report 中，也可以在大批量执行时临时写入 `Coverage_Check/` 的 batch working file。

## 9. Note 修改要求

每篇 note 至少检查并必要时修改：

- 论文信息
- `Evidence Log`
- 摘要翻译 / 摘要概述
- 是否纳入本综述
- 科学领域归类
- Agent 系统与科研流程角色
- 方法设计
- 实验与验证
- 局限性与风险
- 对综述写作的价值
- 总结

必须重点修正：

- 旧的单主类 / 单模块表述。
- 把 note 存放目录误当分类事实的表述。
- 把 `01.04` 当正式主类的表述。
- 没有原文证据支撑的模块判断。
- 漏记的多模块对象证据。
- 与当前 relaxed multi-module rule 冲突的 boundary discussion。
- 未记录 PDF path / first-hand source checked 的 evidence log。

## 10. Master List 修改要求

每批结束时，主控代理统一更新：

```text
Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md
```

更新内容包括：

- relaxed multi-module overlay / 当前多模块分类视图。
- `Note path`。
- `Remarks`。
- `Evidence strength`。
- `primary_module_for_filing` 对应的 legacy `Main class`，仅在当前表格兼容需要时维护。
- `01.04` bucket 状态。
- source-limited / fulltext-required 标记。

重算并记录：

- confirmed included + classified record count。
- module assignment counts。
- independent `01.04` bucket count。
- PDF downloaded count。
- source-limited count。
- note updated count。
- master-list updated count。

## 11. 每批交付物

每批完成后写中文报告：

```text
Coverage_Check/multi_module_note_pdf_full_reaudit_batchXX_YYYY-MM-DD.md
```

报告内容：

- 本批范围。
- 本批完成篇数。
- PDF 下载成功篇数。
- source-limited 篇数。
- note 修改篇数。
- master-list 修改篇数。
- 每篇文献的最终 supported modules / `01.04` bucket。
- 新增、删除或保持的模块分配。
- 关键边界判断。
- unresolved / full-text follow-up queue。
- 本批后累计进度。

同时维护总进度文件：

```text
Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_YYYY-MM-DD.md
```

总进度表字段：

```text
paper_id | title | note_path | pdf_status | pdf_path | evidence_status | note_status | master_status | final_modules_or_bucket | source_limited | batch | closed
```

## 12. 单篇 closed 标准

一篇文献只有同时满足以下条件，才算本轮 closed：

1. 已检查至少一个一手来源。
2. 已尽力获取并归档 PDF；若不能合法获取，已明确记录 source-limited 原因。
3. 已重新判断 Agent 纳入标准。
4. 已重新判断所有 supported `01-11` modules 或 `01.04` bucket。
5. 已把 PDF path / first-hand source 写入 note。
6. 已修正 note 中旧单模块 / 单主类 / 旧 `01.04` 口径。
7. 已同步 master list。
8. 已在 batch report 中留下 evidence trail。

## 13. Git 纪律

每个 batch 完成后执行：

1. `git status`
2. stage 本批相关文件：
   - updated notes
   - downloaded PDF files
   - updated master list
   - batch report
   - progress file
3. 创建清晰 commit，例如：

```text
reaudit ASD batch XX notes PDFs and multi-module classes
```

4. 再次确认 `git status` 干净。

如果某批仍处于 source-limited 或 evidence collection 未完成状态，不强行提交为 completed batch；可提交为 partial progress，但报告中必须明确未完成原因。

## 14. 建议启动顺序

第一步先执行 `Batch 00`：

1. 从 `agent_master_paper_list.md` 生成当前 451 篇 confirmed core records 的平铺索引。
2. 用该索引反查对应 note 和 note path。
3. 取前 10 篇。
4. 建立 PDF 目录。
5. 对 10 篇执行完整流程。
6. 检查 note 修改深度是否合适。
7. 检查 master-list overlay 更新方式是否稳定。
8. 检查 batch report 是否足够追溯。

`Batch 00` 稳定后，再进入 `Batch 01-16`。

本计划的关键目标不是更快地“看完 451 篇”，而是让每一篇文献都有可追溯的一手证据、稳定的多模块分类、更新后的 note，以及可复用的本地 PDF 证据资产。
