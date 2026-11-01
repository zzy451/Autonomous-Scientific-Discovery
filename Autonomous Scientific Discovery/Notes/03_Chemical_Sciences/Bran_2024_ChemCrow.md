# Bran et al. 2024 - Augmenting Large Language Models with Chemistry Tools

## 当前分类（2026-11-01 用户边界裁决）

- 当前纳入状态：`to_read`；主归档：`03`。
- 当前对象模块：`03;04;07`。用户确认化学与材料并行归属；既有药物发现归属保留。
- 本节为当前结论，取代后文及既往补证记录中的材料三级待核状态。

| 模块 | 二级 | 三级 | 当前状态 |
|---|---|---|---|
| 03 | 03.04 分子设计与化学空间探索 | 03.04.01 分子生成与分子设计 | 已确定 |
| 04 | 04.04 能源、电子与器件材料 | 04.04.05 光电材料 | 用户裁定对象边界；代表落点已确定 |
| 07 | 07.04 药学与生物医药 | 07.04.01 药物发现 | 已确定 |

### 模块04裁决依据与范围

- 裁决：用户确认ChemCrow同时保留化学与材料归属；依据色团分子以吸收波长为目标的设计、筛选和合成任务，将其作为分子光学功能材料研究，材料代表位置由04.01暂存细化为04.04.05光电材料。此为03/04对象边界的项目人工裁决，不是新增实验结果。
- 一手证据：本地PDF pp.3–4、19；官方执行notebook对乙腈溶液中的色团建立吸收波长预测，并筛选、合成目标接近369 nm的分子。
- 官方记录：https://raw.githubusercontent.com/ur-whitelab/chemcrow-runs/500104ed9a5d479a8dc4128afc463625ade5a409/chromaphore-rf-369.ipynb。
- 分类解释：材料落点由光学功能对象确定，不因使用随机森林而归入材料计算与材料信息学。化学落点仍表示分子设计与合成，两者并行。
- 证据限度：此处记录分子及溶液尺度的光学性质研究，不扩展为薄膜、器件制备验证或独立实验复现。
- [当前人工裁决与同步报告](../../Coverage_Check/classification_recheck_2026-11-01/corpus_sync_report.md)；[既往补证报告（历史）](../../Coverage_Check/classification_recheck_2026-11-01/completion_report.md)。

## 既有笔记与历史审计记录

## 2026-06-21 archive sync

- Canonical archived PDF: `Reference_PDF/03_Chemical_Sciences/Bran_2024_ChemCrow.pdf`
- Source refresh used in current reaudit: DOI `https://doi.org/10.1038/s42256-024-00832-8`; preprint lineage `https://arxiv.org/abs/2304.05376`
- Current authoritative classification override: `scientific_object_modules = 03;04;07`; `general_method_bucket = none`; `primary_module_for_filing = 03`; `source_limited = no`; `safety_access_status = local_pdf`
- Archive status note: the `04` and `07` support comes from concrete materials-design and drug-discovery task coverage checked in the local PDF, while `03` remains the filing anchor.
- Canonical PDF path for current project use: `Reference_PDF/03_Chemical_Sciences/Bran_2024_ChemCrow.pdf`
- Current reaudit status: included; archived-PDF writeback completed on `2026-06-21`.
- Authoritative note: older sparse body text below should not be read as a single-module-only conclusion. The current note-level classification fact is `03;04;07`, and the current file location is only a filing convenience.

**论文信息**
- 标题：Augmenting large language models with chemistry tools
- 作者：Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, Philippe Schwaller
- 年份：2024
- 来源 / venue：Nature Machine Intelligence
- DOI / URL：https://doi.org/10.1038/s42256-024-00832-8
- 当前状态：已读 / 已纳入；2026-06-21 archived-PDF writeback completed

## Evidence Log

**2026-06-21 archive note**: Project-archived PDF is now available at `Reference_PDF/03_Chemical_Sciences/Bran_2024_ChemCrow.pdf`. Current adjudication treats this note as `03;04;07`: chemistry remains the filing anchor, while materials-design and drug-discovery tasks both have concrete local-PDF support.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，工具增强化学 Agent | Nature Machine Intelligence metadata / seed survey ref 24 | LLM augmented with chemistry tools; known as ChemCrow | 高 |
| 科学对象归类 | `03;04;07`，以 `03` 归档的化学/材料/药物发现交叉任务 | title；local PDF task descriptions | chemistry tools support chemistry problem solving, materials-design tasks, and drug-discovery use cases | 高 |
| 方法机制 | tool-using LLM | title | augmenting LLMs with chemistry tools | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- Agent 行动闭环：工具调用、问题求解、多步化学任务；当前本地 PDF 已支持将其视为具备任务级反馈迭代的工具增强型 Agent。
- 纳入置信度：高。

## 2. 科学领域归类

- 一级类：`03` 化学科学（归档主模块）
- 支持模块：`03;04;07`
- 二级类：`03.04` 分子设计与化学空间探索 / `03.01` 化学信息学；并由材料设计与药物发现任务扩展到 `04;07`
- 四级专题：tool-using chemistry agent
- 归类理由：主对象是化学任务和化学工具链，且已出现材料设计与药物发现任务；本文保留在 `03` 目录仅为归档便利，不按 LLM 工具使用归入 `01`。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Retrieval-augmented Agent。
- 科研流程角色：工具调用、数据查询、结果解释、化学问题求解。
- 自主能力：工具调用、多步行动、任务级反馈迭代。

## 4. 方法设计

初步 pipeline：

1. 用户提出化学问题。
2. LLM Agent 分析任务并选择化学工具。
3. 调用数据库、计算工具或化学工具链。
4. 整合工具输出并生成化学答案。

## 5. 实验与验证

- 验证方式：benchmark / chemistry, materials-design, and drug-discovery task evaluation（local PDF 已核对）。
- 科学贡献类型：system_platform / tool-using chemistry agent with multi-domain task coverage。
- 证据强度：benchmark / computationally validated（local PDF）。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 可作为 tool-using chemistry agent 的代表性早期高影响工作，并可用于说明 `03;04;07` 的跨对象覆盖。
- 需要与 Coscientist 区分：ChemCrow偏工具增强与任务求解，Coscientist偏自治实验和规划执行。

## 7. 后续精读任务

- 列出 ChemCrow 工具集合。
- 细化有机合成、材料设计、药物发现任务分别如何支撑 `03;04;07`。
- 补充具体任务和评价指标表述，用于正文展开而非重新裁定分类。
