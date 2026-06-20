# 451 篇 confirmed 文献多模块重分类本轮审查计划（放松实验覆盖口径）

> 日期：2026-06-20  
> 本文件自含本轮执行口径、批次切分与 Agent 审核组织方式。  
> 本轮性质：在上一轮平铺批次计划基础上，明确采用更放松的“领域实验覆盖”口径重新审查 451 篇 confirmed 文献。  
> 本轮不扩量，不新增论文，不搜索新文献；只复核已收录 confirmed 文献在多模块体系下应进入哪些科学对象模块。  

## 一、核心结论

本轮采用以下硬口径：

> 只要一篇文献对某一科学领域中的具体对象做了可识别的实验、验证、benchmark task、case study 或结果报告，就可以把该文献归入对应科学模块；不要求该模块必须构成论文的核心科学贡献，也不因系统自称 general / platform / workflow 而否定已有对象实验证据。

因此，本轮审查时不能再使用旧口径：

- 不能因为论文主语是 general research-agent platform，就自动留在 `01.04`。
- 不能因为某些案例只是 demo，就不逐项检查其是否构成具体科学对象实验、验证、benchmark task、case study 或结果报告。
- 不能要求每个被记录模块都是论文的 primary scientific object。
- 不能把 `01.04` 当作正式 `01` 主科学对象模块。

但同时仍要避免另一个方向的过度扩张：

- 不能因为论文自称 cross-domain 就自动多模块。
- 不能因为标题、背景、引言、应用愿景中提到某领域，就归入该领域。
- 不能把纯抽象能力评测、通用 workflow 测试、无对象的 benchmark 直接当作具体科学对象实验。

## 二、当前基线

以当前 `Paper_Lists/agent_master_paper_list.md` 头部为准：

| 指标 | 当前值 |
|---|---:|
| `candidate` | 0 |
| `to_read` | 451 |
| `background_only` | 370 |
| `excluded` | 50 |
| `needs_review` | 0 |
| legacy confirmed included-and-classified count | 451 |

legacy confirmed 主类分布仍只作为迁移前 filing baseline，不等于本轮结束后的模块 assignment count。

| Legacy main class | Count |
|---|---:|
| `01` | 52 |
| `02` | 29 |
| `03` | 60 |
| `04` | 95 |
| `05` | 23 |
| `06` | 51 |
| `07` | 51 |
| `08` | 3 |
| `09` | 34 |
| `10` | 23 |
| `11` | 30 |

本轮结束后需要区分两类统计：

- record-level confirmed count：仍按文献条数统计；若无降级，仍为 `451`。
- module assignment count：按 `scientific_object_modules` 展开统计，同一文献可贡献多个模块，因此总数可以大于 `451`。
- independent `01.04` bucket count：单独统计，不并入正式 `01` 对象模块。

## 三、本轮分类判定顺序

每篇文献都按以下顺序复核：

1. 判断是否仍满足 Agent 最低纳入标准。
2. 必须尽最大可能回到原文或一手来源确认分类证据；本地 Notes、legacy 主列表字段和旧 Coverage_Check 报告只能作为定位线索，不能作为最终分类依据。
3. 判断是否存在具体科学对象实验、验证、benchmark task、case study 或结果报告。
4. 如果存在，逐项列出对象，例如 molecule、reaction、material、protein、cell、disease、climate、astronomical object、engineering system、transport system、scientific peer review。
5. 将每个有证据支持的对象映射到 `01-11` 正式科学对象模块。
6. 若多个模块均有对象层证据，记录为 multi-module；不要求每个模块都是论文的主贡献。
7. 若没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告，但论文提出 ASD / general research-agent / general scientific workflow / general benchmark，则进入独立 `01.04` bucket。
8. 若研究对象是 scientific knowledge production itself，例如 scientific peer review、scientific publishing、scientific claims verification、science-of-science analytics，则优先归入 `11.07`。

证据优先级与 note 同步规则：

- 第一优先：论文 full text / PDF、arXiv 或正式出版页面、DOI landing page、publisher abstract、supplementary material、官方 benchmark / project page。
- 第二优先：主列表、已有 Notes、旧 Coverage_Check 报告。它们只能帮助定位证据、识别旧口径残留和找到待复核问题，不能单独决定多模块分类。
- 如果 Notes 中仍写着旧的单模块、单主类、核心贡献优先、或“demo 不计模块”等旧口径表述，而原文 / 一手来源证据支持新的多模块或 `01.04` 迁移判断，应在本轮报告中标记 `note_revision_required = yes`，并由主控在确认分类后同步修改对应 note。
- 后续执行不再采用“先只写审计报告、以后再统一修 note”的默认做法。凡是主控已经确认的 high-confidence 分类变化，应同时写入分类审计结论和对应 Notes；medium / low 或仍需全文的记录只进入复核队列，不抢先修 note。
- 如果无法接触原文或权威摘要，则不得把中等置信判断写成高置信分类；应标记 `full_text_required = yes`。

## 四、Agent 团队设计

本轮沿用上一轮固定小团队，不临时按领域改变规则。

| 角色 | 责任 | 是否编辑文件 |
|---|---|---|
| 主控代理 | 读取规则、分派批次、合并 Reviewer 输出、解决冲突、决定最终分类、写审计报告、必要时修改主列表并重算 counts | 是，仅主控可编辑 |
| Reviewer-1 | 审核本 wave 第 1 个子切片；每条记录输出一行 | 否 |
| Reviewer-2 | 审核本 wave 第 2 个子切片；每条记录输出一行 | 否 |
| Reviewer-3 | 审核本 wave 第 3 个子切片；每条记录输出一行 | 否 |
| Reviewer-4 | 审核本 wave 第 4 个子切片；每条记录输出一行 | 否 |
| 一致性检查员 | 每批合并后检查漏审、重复、字段完整性、multi-module 证据、`01.04` 使用、count 口径；可由主控兼任 | 否 |

执行纪律：

- 子 Agent 只读，不修改 `agent_master_paper_list.md`。
- 每个 Reviewer 单次审核原则上不超过 15 篇。
- 每个 wave 完成后先做口径校准，再启动下一 wave。
- 每个 wave Reviewer 完成并合并后应关闭，避免占用并发槽位。
- 主控只合并高置信、证据清楚、规则一致的变更；中低置信或需要全文的记录进入批次报告。

## 五、四个平铺批次

四批按当前主列表 confirmed 记录出现顺序切分，目标是全量覆盖，不代表优先级。

| Batch | 覆盖序号 | 记录数 | ID 边界 | Legacy main 分布 | Legacy `01.04` 数 |
|---|---:|---:|---|---|---:|
| Batch 1 | 1-113 | 113 | `ASD-0001`-`ASD-0154` | `01:21; 02:8; 03:21; 04:21; 06:19; 07:15; 09:7; 11:1` | 20 |
| Batch 2 | 114-226 | 113 | `ASD-0155`-`ASD-0600` | `01:10; 02:2; 03:21; 04:47; 06:14; 07:13; 08:1; 09:4; 11:1` | 8 |
| Batch 3 | 227-339 | 113 | `ASD-0601`-`ASD-0739` | `01:10; 02:3; 03:9; 04:21; 05:11; 06:8; 07:7; 08:2; 09:2; 10:19; 11:21` | 9 |
| Batch 4 | 340-451 | 112 | `ASD-0740`-`ASD-0871` | `01:11; 02:16; 03:9; 04:6; 05:12; 06:10; 07:16; 09:21; 10:4; 11:7` | 9 |

## 六、micro-batches

### Batch 1

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 15 | `ASD-0001`-`ASD-0017` |
| A-Reviewer-2 | 14 | `ASD-0018`-`ASD-0034` |
| A-Reviewer-3 | 14 | `ASD-0035`-`ASD-0052` |
| A-Reviewer-4 | 14 | `ASD-0053`-`ASD-0068` |
| B-Reviewer-1 | 14 | `ASD-0069`-`ASD-0090` |
| B-Reviewer-2 | 14 | `ASD-0091`-`ASD-0117` |
| B-Reviewer-3 | 14 | `ASD-0118`-`ASD-0135` |
| B-Reviewer-4 | 14 | `ASD-0136`-`ASD-0154` |

### Batch 2

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 15 | `ASD-0155`-`ASD-0381` |
| A-Reviewer-2 | 14 | `ASD-0385`-`ASD-0447` |
| A-Reviewer-3 | 14 | `ASD-0455`-`ASD-0508` |
| A-Reviewer-4 | 14 | `ASD-0510`-`ASD-0523` |
| B-Reviewer-1 | 14 | `ASD-0524`-`ASD-0541` |
| B-Reviewer-2 | 14 | `ASD-0542`-`ASD-0564` |
| B-Reviewer-3 | 14 | `ASD-0565`-`ASD-0581` |
| B-Reviewer-4 | 14 | `ASD-0582`-`ASD-0600` |

### Batch 3

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 15 | `ASD-0601`-`ASD-0622` |
| A-Reviewer-2 | 14 | `ASD-0623`-`ASD-0636` |
| A-Reviewer-3 | 14 | `ASD-0637`-`ASD-0658` |
| A-Reviewer-4 | 14 | `ASD-0659`-`ASD-0673` |
| B-Reviewer-1 | 14 | `ASD-0674`-`ASD-0691` |
| B-Reviewer-2 | 14 | `ASD-0693`-`ASD-0707` |
| B-Reviewer-3 | 14 | `ASD-0708`-`ASD-0723` |
| B-Reviewer-4 | 14 | `ASD-0724`-`ASD-0739` |

### Batch 4

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 14 | `ASD-0740`-`ASD-0754` |
| A-Reviewer-2 | 14 | `ASD-0755`-`ASD-0769` |
| A-Reviewer-3 | 14 | `ASD-0770`-`ASD-0787` |
| A-Reviewer-4 | 14 | `ASD-0789`-`ASD-0804` |
| B-Reviewer-1 | 14 | `ASD-0805`-`ASD-0818` |
| B-Reviewer-2 | 14 | `ASD-0819`-`ASD-0833` |
| B-Reviewer-3 | 14 | `ASD-0838`-`ASD-0856` |
| B-Reviewer-4 | 14 | `ASD-0857`-`ASD-0871` |

注意：ID 边界不是连续编号保证，因主列表中存在 non-confirmed、background_only、excluded 或历史空缺记录。每批真实范围以 confirmed 记录出现序号为准。

## 七、Reviewer 输出字段

每个 Reviewer 输出 TSV 或 Markdown 表，一行一篇，不得省略“无变化”记录。

| 字段 | 控制值 / 用途 |
|---|---|
| `paper_id` | ASD 编号 |
| `title` | 主列表标题 |
| `current_status` | 当前 `Inclusion status` |
| `current_legacy_main` | 当前 legacy `Main class` |
| `current_legacy_secondary` | 当前 legacy `Secondary class` |
| `agent_minimum_evidence` | 一句话说明是否满足 Agent 最低标准 |
| `has_concrete_object_experiments` | `yes / no / uncertain` |
| `concrete_scientific_objects` | 具体对象 |
| `suggested_scientific_object_modules` | `01-11`，可多选；无具体对象实验时留空 |
| `suggested_general_method_bucket` | `none / 01.04` |
| `object_coverage_mode` | `single_module / multi_module / general_method_without_concrete_object_experiments / uncertain` |
| `primary_module_for_filing` | 单个 `01-11` 或空；仅用于展示和笔记路径 |
| `module_assignment_evidence` | 每个建议模块对应的对象实验证据 |
| `multi_module_object_coverage_note` | 若多模块，说明每个模块的对象层证据 |
| `boundary_type` | 如 `01.04-vs-domain`、`03-vs-04`、`06-vs-07`、`05-vs-10`、`11.07-vs-01.04` |
| `recommended_action` | `keep / add_module / move_primary / move_to_01.04 / demote_or_background_review / main_control_review` |
| `confidence` | `high / medium / low` |
| `full_text_required` | `yes / no` |
| `first_hand_sources_checked` | 已核对的一手来源，例如 PDF、arXiv、DOI page、publisher abstract、official project page；若仅看 note，必须写明 `notes_only` |
| `note_revision_required` | `yes / no`；若已有 note 使用旧单模块表述或与原文证据不一致，标 `yes` |
| `reviewer_note` | 证据缺口或争议 |

## 八、Reviewer 统一任务提示词

```text
你是 Autonomous Scientific Discovery 综述项目的只读分类 Reviewer。
请读取项目规则文件、主列表中分配给你的记录，以及对应 Notes 文件。
你的任务不是扩量搜新论文，也不是修改主列表，而是逐条复核分配记录在本轮放松口径下应进入哪些科学对象模块。
不能完全参考本地 Notes；Notes 很可能仍是旧单模块表述，只能作为定位线索。请最大程度核对原文、PDF、arXiv / DOI / publisher 页面、官方项目页或权威摘要，并在输出中写明 `first_hand_sources_checked`。若只看了 note，必须写 `notes_only`，且不能给出 high confidence 分类变化。若原文证据支持新增模块、`01.04` 迁移或推翻旧 note 表述，请标记 `note_revision_required = yes`，并说明 note 中哪类旧口径需要修订。

统一口径：
1. 先判断是否仍满足 Agent 最低纳入标准。
2. 分类依据是论文实际研究和实验覆盖的科学对象，不是 Agent 技术、平台名称、venue 或自称通用性。
3. 只要论文对某一科学领域中的具体对象做了可识别的实验、验证、benchmark task、case study 或结果报告，就可以建议进入对应 `01-11` 科学对象模块。
4. 如果多个具体科学对象各自有可识别证据，就建议 multi-module；不要求每个模块构成论文核心贡献。
5. 如果没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告，只提出 ASD / general research-agent 方法或通用 benchmark，才建议进入独立 `01.04` bucket。
6. 不要因为系统 general / cross-domain / multi-agent 就自动多模块；必须逐项写出对象层证据。
7. 不要跳过任何分配记录；每条都输出一行。
8. 不要编辑任何文件。
```

## 九、合并与计数规则

- `high` confidence 且证据清楚的 `keep / add_module / move_primary / move_to_01.04` 可进入批次审计结论。
- `medium` confidence、Reviewer 与主控判断不一致、或依赖全文证据的记录，进入批次问题清单，不强行改表。
- `low` confidence 或 Agent 纳入证据动摇的记录，标为主控复审，不由 Reviewer 直接决定降级。
- `scientific_object_modules` 的 module assignment count 单独统计，可超过 `451`。
- record-level confirmed count 继续统计文献条数。
- 独立 `01.04` bucket 单独统计，不计入正式 `01` 对象模块数量。
- `primary_module_for_filing` 只用于兼容 legacy 表格和笔记路径，不作为唯一分类事实。
- 主控合并时，high-confidence 且已有一手证据支持的分类变化，应同步更新对应 `Notes/` 中的分类、对象证据和 multi-module 表述；如果主列表 schema 尚未迁移，分类事实可先写入审计报告与 note 元数据 / 分类段落，legacy `Main class` 字段暂不强行覆盖。
- 若某条记录的分类判断仍依赖 Notes、旧报告或 metadata-only 摘要，则必须留在复核队列；不得因为 note 旧表述看似稳定就直接沿用单模块结论。

## 十、本轮优先留意的旧口径残留样本

以下样本不是优先级抽样，而是在全量复核中需要特别防止被旧口径误锁在 `01.04`：

| ID | 标题 / 简称 | 本轮复核重点 |
|---|---|---|
| `ASD-0844` | `Science Earth` | 若确有生命科学、物理 / 复杂系统、地球环境等 case 或结果，应按对象证据记录相应模块 |
| `ASD-0447` | `An autonomous portable platform for universal chemical synthesis` | 核对是否存在具体化学合成对象实验；若有，应记录 `03` |
| `ASD-0254` | `From intention to implementation: automating biomedical research via llms` | 核对 biomedical workflow 是否含具体生物医学对象实验 / case |
| `ASD-0553` | `ToolsGenie 2.0` | 核对 bioinformatics / biology tasks 是否只是通用工具生成，还是有具体对象结果 |
| `ASD-0554` | `BioAgent` | 核对 translational bioinformatics / biomedical 对象覆盖 |
| `ASD-0660` | `S1-NexusAgent` | 核对是否有具体对象实验覆盖多个模块 |
| `ASD-0673` | `Harnessing AtomisticSkills for Agentic Atomistic Research` | 核对 atomistic research 是否支持 `02`、`03` 或 `04` |
| `ASD-0868` | `Think like a Scientist` | 核对 physics-guided equation discovery 是否有物理对象任务 |
| `ASD-0869` | `STRIDE` | 核对 symbolic-regression benchmark 是否有具体物理 / 系统对象 |
| `ASD-0870` | `SR-Scientist` | 核对 cross-discipline equation-discovery datasets 是否支持具体对象模块 |

## 十一、本轮产物

每个 wave 至少产出：

- Reviewer 原始输出汇总表。
- 主控口径校准记录。
- 已确认分类变化对应的 note 修订清单；若未修订，必须说明是因为仍需全文 / 一手来源复核，而不是因为暂时保留旧 note 口径。

每个 batch 至少产出：

- 主控合并审计报告，写入 `Coverage_Check/`。
- reviewed record count。
- unchanged count。
- add_module count。
- move_primary count。
- move_to_01.04 count。
- demote/background-review candidate count。
- full_text_required count。
- post-batch record-level confirmed count。
- post-batch module assignment counts。
- independent `01.04` bucket count。
- note update count 与 note revision queue；已确认的 high-confidence 变更应尽量在同一 batch 内同步修订 note。

若实际修改项目文件，每轮结束后按 skill 中 `Git Discipline` 执行：`git status`、提交相关变更、再确认工作树干净。
