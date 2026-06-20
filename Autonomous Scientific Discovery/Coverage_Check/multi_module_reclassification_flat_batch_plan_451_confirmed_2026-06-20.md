# 451 篇 confirmed 文献多模块重分类平铺批次计划

> 日期：2026-06-20  
> 范围：`Paper_Lists/agent_master_paper_list.md` 中当前 `to_read` / `included` 且已有 legacy filing code 的 451 篇 confirmed 文献。  
> 目标：按新口径重新审核每篇文献的科学研究对象模块，允许同一篇文献在有可识别领域实验、验证、benchmark task、case study 或结果报告时进入多个 `01–11` 模块；没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告的 ASD / general research-agent 方法文献进入独立 `01.04` 存放区。  

## 一、当前基线

本计划以 2026-06-20 当前主列表为准：

- `candidate`: 0
- `to_read`: 451
- `background_only`: 370
- `excluded`: 50
- `needs_review`: 0
- legacy confirmed included-and-classified count: 451
- legacy confirmed `08`: 3

legacy confirmed 主类分布如下：

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

说明：上述分布是迁移前的 legacy primary filing 统计，不等于新口径下的最终模块分布。迁移完成后，模块 assignment count 可以大于 451，因为同一篇文献可有多个科学对象模块；record-level confirmed count 仍按文献条数统计。

## 二、统一审核口径

本轮不是扩量，不搜索新论文，不按风险优先抽样，而是对 451 篇 confirmed 文献平铺全量复核。

每篇文献都按以下顺序审核：

1. 是否仍满足 Agent 最低纳入标准。
2. 是否有具体科学对象研究实验、验证、案例研究或对象层结果。
3. 若有具体对象实验、验证、benchmark task、case study 或结果报告，记录所有被覆盖的 `01–11` 科学对象模块。
4. 若只覆盖一个对象模块，不硬凑多模块。
5. 若确实覆盖多个具体对象，并且每个对象都有可识别的实验、验证、benchmark task、case study 或结果证据，则记录为 multi-module；不要求每个模块都构成论文的核心科学贡献。
6. 若没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告，但提出 ASD / general research-agent 方法、通用科研工作流、通用科学发现平台或通用 benchmark，则进入独立 `01.04` 存放区。
7. `primary_module_for_filing` 只作为笔记落盘、排序和展示便利，不覆盖 `scientific_object_modules` 的多模块事实。

固定判定句：

> 一篇文献进入哪些科学模块，由其实际研究和实验覆盖的科学对象决定，而不是由其所使用的算法、Agent 架构、平台名称、发表 venue 或自称通用性决定。

## 三、固定 Agent 团队设计

每一批使用同一套团队，不按领域临时换规则。

| 角色 | 责任 | 是否编辑文件 |
|---|---|---|
| 主控代理 | 读取规则、分派批次、合并 Reviewer 输出、解决冲突、决定最终分类、写审计报告、必要时修改主列表并重算 counts | 是，仅主控可编辑 |
| Reviewer-1 | 审核本批第 1 个子切片，每条记录必须输出一行，不得跳过无变化记录 | 否 |
| Reviewer-2 | 审核本批第 2 个子切片，每条记录必须输出一行，不得跳过无变化记录 | 否 |
| Reviewer-3 | 审核本批第 3 个子切片，每条记录必须输出一行，不得跳过无变化记录 | 否 |
| Reviewer-4 | 审核本批第 4 个子切片，每条记录必须输出一行，不得跳过无变化记录 | 否 |
| 一致性检查员 | 每批合并后检查漏审、重复、输出字段、multi-module 证据、`01.04` 使用、count 口径；可由主控兼任，或在并发允许时另开 Agent | 否 |

执行方式：

- 一次只推进一个百篇级批次。
- 每个百篇级批次再拆成两个 wave；每个 wave 使用 4 个 Reviewer 并行工作，每个 Reviewer 单次默认审核约 14–15 篇。
- 单个 Reviewer 单次审核设置硬上限：原则上不超过 15 篇，不再采用 20 篇以上的大切片。
- 如果某个切片中 `01.04`、`03/04`、`06/07`、`05/10`、`11.07/01.04` 等边界记录明显密集，主控应把该切片继续拆成 8–10 篇的 boundary micro-slice，或要求 Reviewer 先交付前半段后再继续。
- Wave A 完成后，主控先做快速口径校准，再启动 Wave B，避免同一批后半段出现系统性漂移。
- Reviewer 必须只读主列表、规则文件和对应 note；不得修改 `agent_master_paper_list.md`。
- Reviewer 输出建议，不做最终裁决。
- 主控合并后先写批次审计结果；只有高置信、规则一致、证据充分的变更才进入主列表。
- 每个 wave 结束后关闭该 wave Reviewer；每一批结束后再做批次级合并和一致性检查。

质量控制理由：

- 单个 Agent 一次审核 28–29 篇时，后半段容易变成按标题或 legacy 分类做模式匹配，尤其会影响 `01.04`、`03/04`、`06/07`、`05/10`、`11.07/01.04` 等边界。
- 14–15 篇是更稳的单次负载：每条仍能读取 note、核对对象证据、写出简短理由，同时不会把上下文窗口塞得过满。
- 8–10 篇作为边界密集切片的降载方案：它牺牲一部分吞吐量，但能显著降低“看到通用平台就误判 `01.04`”或“看到跨域 demo 就硬凑 multi-module”的风险。
- 外层保留 4 个百篇级批次，保证项目管理和 counts 汇总不碎；内层拆成 micro-batch，保证分类判断质量。

## 四、四个平铺批次

四批按当前主列表 confirmed 记录出现顺序切分，目的是全量覆盖，不代表优先级。

| Batch | 覆盖序号 | 记录数 | ID 边界 | Legacy main 分布 | Legacy `01.04` 数 |
|---|---:|---:|---|---|---:|
| Batch 1 | 1–113 | 113 | `ASD-0001`–`ASD-0154` | `01:21; 02:8; 03:21; 04:21; 06:19; 07:15; 09:7; 11:1` | 20 |
| Batch 2 | 114–226 | 113 | `ASD-0155`–`ASD-0600` | `01:10; 02:2; 03:21; 04:47; 06:14; 07:13; 08:1; 09:4; 11:1` | 8 |
| Batch 3 | 227–339 | 113 | `ASD-0601`–`ASD-0739` | `01:10; 02:3; 03:9; 04:21; 05:11; 06:8; 07:7; 08:2; 09:2; 10:19; 11:21` | 9 |
| Batch 4 | 340–451 | 112 | `ASD-0740`–`ASD-0871` | `01:11; 02:16; 03:9; 04:6; 05:12; 06:10; 07:16; 09:21; 10:4; 11:7` | 9 |

### Batch 1 micro-batches

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 15 | `ASD-0001`–`ASD-0017` |
| A-Reviewer-2 | 14 | `ASD-0018`–`ASD-0034` |
| A-Reviewer-3 | 14 | `ASD-0035`–`ASD-0052` |
| A-Reviewer-4 | 14 | `ASD-0053`–`ASD-0068` |
| B-Reviewer-1 | 14 | `ASD-0069`–`ASD-0090` |
| B-Reviewer-2 | 14 | `ASD-0091`–`ASD-0117` |
| B-Reviewer-3 | 14 | `ASD-0118`–`ASD-0135` |
| B-Reviewer-4 | 14 | `ASD-0136`–`ASD-0154` |

### Batch 2 micro-batches

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 15 | `ASD-0155`–`ASD-0381` |
| A-Reviewer-2 | 14 | `ASD-0385`–`ASD-0447` |
| A-Reviewer-3 | 14 | `ASD-0455`–`ASD-0508` |
| A-Reviewer-4 | 14 | `ASD-0510`–`ASD-0523` |
| B-Reviewer-1 | 14 | `ASD-0524`–`ASD-0541` |
| B-Reviewer-2 | 14 | `ASD-0542`–`ASD-0564` |
| B-Reviewer-3 | 14 | `ASD-0565`–`ASD-0581` |
| B-Reviewer-4 | 14 | `ASD-0582`–`ASD-0600` |

### Batch 3 micro-batches

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 15 | `ASD-0601`–`ASD-0622` |
| A-Reviewer-2 | 14 | `ASD-0623`–`ASD-0636` |
| A-Reviewer-3 | 14 | `ASD-0637`–`ASD-0658` |
| A-Reviewer-4 | 14 | `ASD-0659`–`ASD-0673` |
| B-Reviewer-1 | 14 | `ASD-0674`–`ASD-0691` |
| B-Reviewer-2 | 14 | `ASD-0693`–`ASD-0707` |
| B-Reviewer-3 | 14 | `ASD-0708`–`ASD-0723` |
| B-Reviewer-4 | 14 | `ASD-0724`–`ASD-0739` |

### Batch 4 micro-batches

| Wave-Reviewer | 记录数 | ID 边界 |
|---|---:|---|
| A-Reviewer-1 | 14 | `ASD-0740`–`ASD-0754` |
| A-Reviewer-2 | 14 | `ASD-0755`–`ASD-0769` |
| A-Reviewer-3 | 14 | `ASD-0770`–`ASD-0787` |
| A-Reviewer-4 | 14 | `ASD-0789`–`ASD-0804` |
| B-Reviewer-1 | 14 | `ASD-0805`–`ASD-0818` |
| B-Reviewer-2 | 14 | `ASD-0819`–`ASD-0833` |
| B-Reviewer-3 | 14 | `ASD-0838`–`ASD-0856` |
| B-Reviewer-4 | 14 | `ASD-0857`–`ASD-0871` |

注意：ID 边界不是连续编号保证，因主列表中存在 non-confirmed、background_only、excluded 或历史空缺记录。每批的真实范围以 confirmed 记录的出现序号为准。

## 五、Reviewer 输出字段

每个 Reviewer 输出 TSV 或 Markdown 表，一行一篇，不能省略“无需变化”的记录。

必需字段：

| 字段 | 控制值 / 用途 |
|---|---|
| `paper_id` | ASD 编号 |
| `title` | 主列表标题 |
| `current_status` | 当前 `Inclusion status` |
| `current_legacy_main` | 当前 legacy `Main class` |
| `current_legacy_secondary` | 当前 legacy `Secondary class` |
| `agent_minimum_evidence` | 一句话说明是否满足 Agent 最低标准 |
| `has_concrete_object_experiments` | `yes / no / uncertain` |
| `concrete_scientific_objects` | 具体对象，如 molecule、reaction、material、protein、disease、climate、rover mission、peer review |
| `suggested_scientific_object_modules` | `01–11`，可多选；无具体对象实验时留空 |
| `suggested_general_method_bucket` | `none / 01.04` |
| `object_coverage_mode` | `single_module / multi_module / general_method_without_concrete_object_experiments / uncertain` |
| `primary_module_for_filing` | 单个 `01–11` 或空；只用于展示和笔记路径 |
| `module_assignment_evidence` | 每个建议模块对应的对象实验证据 |
| `multi_module_object_coverage_note` | 若多模块，说明为什么不是单纯 demo 或泛泛跨域 |
| `boundary_type` | 如 `01.04-vs-domain`、`03-vs-04`、`06-vs-07`、`05-vs-10`、`11.07-vs-01.04` |
| `recommended_action` | `keep / add_module / move_primary / move_to_01.04 / demote_or_background_review / main_control_review` |
| `confidence` | `high / medium / low` |
| `full_text_required` | `yes / no` |
| `reviewer_note` | 需要主控注意的证据缺口或争议 |

## 六、Reviewer 统一任务提示词

每个 Reviewer 接收任务时应包含以下固定提示：

```text
你是 Autonomous Scientific Discovery 综述项目的只读分类 Reviewer。
请读取项目规则文件、主列表中分配给你的记录，以及对应 Notes 文件。
你的任务不是扩量搜新论文，也不是修改主列表，而是逐条复核分配记录在新口径下应进入哪些科学对象模块。

统一口径：
1. 先判断是否仍满足 Agent 最低纳入标准。
2. 分类依据是论文实际研究和实验覆盖的科学对象，不是 Agent 技术、平台名称、venue 或自称通用性。
3. 有具体科学对象实验、验证、benchmark task、case study 或结果报告的论文，进入一个或多个 `01–11` 科学对象模块。
4. 只要多个具体科学对象各自有可识别的实验、验证、benchmark task、case study 或结果报告，就建议 multi-module；不要求每个模块构成论文的核心或实质科学贡献。
5. 没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告，只提出 ASD / general research-agent 方法或通用 benchmark 的论文，建议进入独立 `01.04` bucket。
6. 不要因为系统 general / cross-domain / multi-agent 就自动多模块。
7. 不要跳过任何分配记录；每条都输出一行。
8. 不要编辑任何文件。
```

## 七、合并与计数规则

每批合并时，主控按以下规则处理：

- `high` confidence 且证据清楚的 `keep / add_module / move_primary / move_to_01.04` 可以进入批次审计结论。
- `medium` confidence、Reviewer 与主控规则判断不一致、或依赖全文证据的记录，先进入批次问题清单，不强行改表。
- `low` confidence 或 Agent 纳入证据动摇的记录，标为主控复审，不由 Reviewer 直接决定降级。
- `scientific_object_modules` 的模块 assignment count 单独统计，可超过 451。
- record-level confirmed count 继续统计文献条数；若没有降级，仍为 451。
- 独立 `01.04` bucket 单独统计，不计入正式 `01` 对象模块数量。
- `primary_module_for_filing` 只用于兼容 legacy 表格和笔记路径，不作为唯一分类事实。

## 八、批次产物

每批结束至少产出：

1. Reviewer 原始输出汇总表。
2. 主控合并审计报告，写入 `Coverage_Check/`。
3. 若实际修改主列表，则同步记录修改前后 counts。
4. 每批结束后输出：
   - reviewed record count
   - unchanged count
   - add_module count
   - move_primary count
   - move_to_01.04 count
   - demote/background-review candidate count
   - full_text_required count
   - post-batch record-level confirmed count
   - post-batch module assignment counts

## 九、本轮不做的事

- 不新增论文。
- 不按风险优先抽样替代全量复核。
- 不让子 Agent 直接编辑主列表。
- 不为了平衡类别数量放宽 `08` 或任何低覆盖类。
- 不因为文献自称通用、跨学科或平台化就自动多模块。
- 不把 `01.04` 当作正式 `01` 主科学对象模块。
