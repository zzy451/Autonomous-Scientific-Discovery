# PR #1 证据复核与正式数据修改记录（2026-10-28）

## 1. 本地备份

PR #1（`Publish gpt-6.1-sol classification audit and review handoff`，head `411cfe90d08c9571df84c9a1f61dd9e8a14485f2`）已保存至：

`Section_Scratch/PR_1_backup_2026-10-28/`

其中包括 `pr_1.patch`、`pr_1_head.bundle`、`pr_1_head.zip`、PR 元数据、提交树快照，以及 Git 备份引用 `refs/backup/pr-1-jiaming-review`。修改前的正式 owner 文件另存于 `pre_modification_owner_snapshot/`。

## 2. PR 审计结果的性质

PR 提供的是逐篇模型审计快照，不是已经确认的分类更正。快照包含 663 篇核心论文、1,743 条差异记录，涉及 639 篇论文。差异类型如下：

| 差异类型 | 条数 |
|---|---:|
| tertiary_code_mismatch | 560 |
| secondary_code_mismatch | 495 |
| source_or_model_review_required | 327 |
| module_added_by_audit | 247 |
| module_missing_in_audit | 109 |
| general_method_bucket_mismatch | 5 |

原始审计使用了 491 篇全文和 172 篇仅笔记记录；仅笔记记录不能替代论文全文证据。因此本次没有批量复制 PR 的模型标签，而是逐条以本地全文、现行词表和对象优先规则复核。

## 3. 已确认并写回的修改

### ASD-0001 — MAPPS

- 证据：`Reference_PDF/04_Materials_Science/Zhou_2025_MAPPS.pdf`，第 2 页第 2 节及实验表格。
- 原文对象：crystal generation、crystal structure prediction、property-guided generation；评估晶体结构有效性、稳定性、匹配率和带隙等材料性质。
- 原分类：`04.04`；PR 审计建议：`04.02`。
- 正式结论：`04.02 结构材料与无机材料`，主表三级类补为 `04.02.05 晶体材料`。
- 已同步修改：
  - `Paper_Lists/agent_master_paper_list.md`
  - `Data/paper_module_taxonomy_assignments.jsonl`（模块侧保留 `04.02`；模块 owner 当前仅允许 06/07 写入三级码）
  - `Data/discipline_code_assignments.jsonl`（旧 `04-04-001` 关闭并重定向，新当前码 `04-02-016`）
  - `Notes/04_Materials_Science/Zhou_2025_MAPPS.md`
  - `Data/change_log.jsonl`

## 4. 明确拒绝直接采用的模型建议

- ASD-0053：模型把无具体科学对象的通用科研 Agent 从 `01.04` 移出；按照项目规则，通用方法桶应保留，不能仅因有 toy ML 评测就新增科学对象模块。
- ASD-0600：模型建议增加模块 01，但论文的主要对象是化学合成执行；具体化学对象证据应留在 03，不能因存在解析器或通用工具评测而添加 01。
- ASD-0093：模型建议增加多个材料、生物等模块；目前证据只支持化学合成与相关分子对象，缺少独立对象实验，暂不写回。
- ASD-0428、ASD-0734：PR 将已有 `03.03` 三级信息与其快照中的空值比较；现行词表仍有 `03.03` 下的有效三级词条，不能据此删除现有三级分类。

以上条目保留在 PR 快照和后续人工复核队列中，没有修改正式 owner 文件。

## 5. 管线验证

已运行：

```text
python scripts/run_structured_data_pipeline.py
```

`export -> check -> build` 全部通过。当前一致性统计仍为 1,133 条结构化记录、663 篇 active confirmed-core、595 篇本地 PDF；分类修改没有改变核心库数量。

## 6. 后续复核边界

其余 PR 差异需要逐篇打开全文并记录页码、对象、实验或验证结果后再决定。模型建议、来源不足和词表缺口均不自动写回；只有证据达到项目规则要求的条目才进入 owner 文件。

## 7. 本轮追加的三项修改

在继续核对 PR 的全文证据后，又确认并写回 3 篇材料科学论文：

| 论文 | 原分类 | 新分类 | 证据依据 |
|---|---|---|---|
| ASD-0007 Kumbhar 2025 | 04.04 | 04.01 | MATDESIGN/ACCELMAT 面向一般材料设计目标、约束和方法假设，没有能源、电子或器件对象 |
| ASD-0016 Szymanski 2023 A-Lab | 04.04 | 04.02 / 04.02.03 | 真实固态无机粉末合成，目标为氧化物、磷酸盐和无机化合物 |
| ASD-0065 Ni 2024 MatPilot | 04.04 | 04.02 / 04.02.04 | 能源储存陶瓷与固相烧结流程是明确材料对象 |

本轮累计正式写回 4 篇（包括 ASD-0001）。新增 3 个当前学科代码，旧代码均保留为 redirected 历史记录；核心库仍为 663 篇。

## 8. 后续分块复核结果

继续核对 PR 后，又确认以下 10 篇可以根据全文或结构化阅读记录写回：

| 论文 | 新分类 | 主要证据 |
|---|---|---|
| ASD-0013 | 01.02 / 01.02.13 | AI Scientist v2 的 ML 假设、代码实验和 ML 论文对象 |
| ASD-0018 | 01.02 / 01.02.12 | Agent Laboratory 的 MLE-Bench 和具体 ML 代码实验 |
| ASD-0051 | 06.03 / 06.03.01 | GeneAgent 的 gene-set discovery 与 functional genomics |
| ASD-0126 | 06.03 / 06.03.01 | BioAgents 的 bioinformatics/genomics workflow |
| ASD-0290 | 03.03 / 03.03.03 | catalysts、adsorption energies、reaction barriers 与 pathways |
| ASD-0370 | 06.03 / 06.03.06 | protein fitness landscape 与蛋白质工程 |
| ASD-0389 | 04.03 / 04.03.02 | 手性无机钙钛矿纳米晶 |
| ASD-0390 | 04.03 | 环氧树脂配方与粘接强度 |
| ASD-0505 | 04.02 / 04.02.03 | 固态无机材料形成和相选择 |
| ASD-0535 | 04.02 / 04.02.03 | 无机晶体材料设计 |

其中 ASD-0013/0018/0051/0126/0370/0612/0666/0667/0674 也修正了旧学科代码台账；所有修改均保留旧代码的历史重定向记录。

目前已完成对 PR 涉及范围 ASD-0001–0900 的分块证据审计；ASD-0901–1133 正在继续核对。PR 中大量 `tertiary_code_mismatch` 是过时词表与现行三级词条的空值比较，不能作为删除依据；大量 `module_added_by_audit` 只是工具、benchmark 或案例载体，也未自动扩展模块。

## 9. 全量审计边界与状态

ASD-0001–1133 的全部 PR 差异行已经完成分块分流，覆盖 1,743 行、639 篇论文。其中 1,280 行来自全文审计，463 行来自仅笔记审计。分流结论包括：接受并写回、根据现有全文裁决拒绝、以及因仅笔记/缺页码/边界不明确而待补证据。

这表示全部意见都已有处理状态，但不等于 1,743 行全部重新逐页阅读。对全文中明确且与现行词表一致的 18 篇论文已写入 owner 文件；其余意见已保留在 PR 快照和分块报告中，待补全文或专门边界复核后再决定。这样避免把模型快照中的空值比较误当作分类错误。

本地回溯提交：

- `d943b11` — 首批材料分类证据修正
- `3fec2d5` — 追加 PR 证据分类修正与全量复核报告
- `9ca7c40` — 刷新结构化派生数据

以上提交均只存在本地，未推送 GitHub。
