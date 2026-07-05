# Naumov 2025 - DORA AI Scientist
## 2026-07-05 Phase6NoteRevisionR22 harmonization

- Frozen landing decision: keep independent `01.04` with `object_coverage_mode=general_method_without_concrete_object_experiments`, `primary_module_for_filing=01`, `general_method_bucket=01.04`, and `source_limited=no`.
- Current PDF state: the local archived bioRxiv PDF at `Reference_PDF/01_Formal_Information_and_Computational_Sciences/Naumov_2025_DORA_AI_Scientist.pdf` has already been reopened and text-checked.
- Note harmonization rule for this file: any older `abstract-only`, `full-text follow-up`, `no local PDF`, or `source-limited` wording below is historical and superseded by the 2026-07-03 local-PDF recheck block.

**论文信息**
- 标题：DORA AI Scientist: Multi-agent Virtual Research Team for Scientific Exploration Discovery and Automated Report Generation
- 作者：Vladimir Naumov, Diana Zagirova, Sha Lin, Yupeng Xie, Wenhao Gou, Anatoly Urban, Nina Tikhonova, Khadija M. Alawi, Mike Durymanov, Fedor Galkin, et al.
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / arXiv / URL：https://doi.org/10.1101/2025.03.06.641840
- PDF / 本地文件路径：`Reference_PDF/01_Formal_Information_and_Computational_Sciences/Naumov_2025_DORA_AI_Scientist.pdf`
- 论文类型：系统论文 / 科研探索与报告生成 Agent
- 当前状态：已复核本地 PDF 全文 / 已纳入 / round-2 边界已关闭为独立 `01.04`
- 阅读日期：2026-06-16
- 笔记作者：Codex

## Evidence Log

## 2026-07-03 Phase6FollowupR10 local PDF recheck

- `first_hand_sources_checked`: local archived bioRxiv PDF `Reference_PDF/01_Formal_Information_and_Computational_Sciences/Naumov_2025_DORA_AI_Scientist.pdf`; DOI `https://doi.org/10.1101/2025.03.06.641840`.
- Current authoritative classification: keep the independent `01.04` general-method bucket with `object_coverage_mode=general_method_without_concrete_object_experiments`; `primary_module_for_filing=01`; `general_method_bucket=01.04`.
- Local-PDF finding: the archived bioRxiv PDF is locally present and readable; this round no longer needs to describe the record as blocked from full-text verification.
- Why this matters: first-page full-text recheck still frames DORA as a multi-agent scientific exploration and automated report-generation system. The reread does not add concrete life-science or biomedical object experiments strong enough for `06` or `07`, but it does clear the old `source_limited` ceiling.

## 2026-06-21 relaxed round-2 boundary closure

- `first_hand_sources_checked`: Crossref DOI abstract for `10.1101/2025.03.06.641840`; official DORA platform `https://dora.insilico.com`; official Insilico blog `https://insilico.com/blog/science42-dora`; official GitHub repository `https://github.com/insilicomedicine/DORA`.
- Accepted relaxed classification: move the record out of legacy `06` filing and keep it in the independent `01.04` bucket with `object_coverage_mode=general_method_without_concrete_object_experiments`; `primary_module_for_filing=01`; `general_method_bucket=01.04`.
- Why: the accessible first-hand evidence consistently frames DORA as a multi-agent scientific exploration, drafting, and report-generation assistant built around templates, workflows, tool/repository access, and publication drafting. It does not verify concrete life-science or biomedical object experiments, benchmark tasks, case studies, or reported results strong enough to support `06` or `07`.
- Note implication: this note should no longer keep the `06 / 07 / 01.04` boundary open by default. Later full text can still enrich task inventory, but the current first-hand evidence base is already sufficient to reject concrete `06` / `07` assignment and close the relaxed-round decision at independent `01.04`.

## 2026-06-20 relaxed round-2 source-limited revision

- Round decision: no master-list classification change in this round.
- Source checked in this round: DOI / bioRxiv landing path for `10.1101/2025.03.06.641840`, but the direct bioRxiv page remained inaccessible through the available route; only source-limited abstract/metadata trails were available.
- Reason: current evidence is still insufficient to decide whether DORA has concrete life-science / biomedical object experiments, should remain filed under `06`, should move to `07`, or should be treated as independent `01.04`.
- Current action: keep in the Round 2 full-text boundary queue with `full_text_required=yes`; do not revise the relaxed overlay from note-only or third-party evidence.

证据级别：abstract+metadata（全文仍不可访问；不能伪装成 full-text。当前所有关于 pipeline、验证和科学对象的判断均为低到中低证据）。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 暂纳入；多 Agent 虚拟研究团队 / report generation workflow | 题名、DOI 元数据、第三方摘要线索 | 标题明确为 multi-agent virtual research team，用于 scientific exploration discovery and automated report generation | 中低 |
| 科学对象归类 | 独立 `01.04` 通用科研 Agent / scientific workflow assistant | Crossref DOI abstract；official platform/blog/repo | 现有一手来源稳定支撑 scientific exploration、workflow orchestration、draft outline 和 automated report generation，但未核实任何 concrete biology / biomedical object experiments | 中高 |
| 方法流程 | 模板/outline -> 多 Agent 分工 -> 文献/数据源检索 -> section/report generation -> 引用/文本后处理 | 第三方摘要线索 | DORA/Draft Outline Research Assistant 似乎支持研究论文、综述、报告等模板化产出 | 低 |
| 实验验证 | 未能核实 | 摘要/元数据层面 | 未确认 benchmark、用户研究、案例、指标或专家评估 | 低 |
| 科学贡献 | 科研探索和自动报告生成平台，而非已确认的新生物发现 | 题名与摘要线索 | 贡献可能是 multi-agent scientific report generation / biomedical research assistance | 低 |

## 0. 摘要翻译

本次仍未能读取 bioRxiv 全文 PDF/HTML，因此以下仅为低证据强度概括。论文提出 DORA AI Scientist，标题称其为一个用于科学探索、发现和自动报告生成的 multi-agent virtual research team。第三方摘要线索显示，DORA 可能通过 Draft Outline Research Assistant 风格的模板化 workflow，将研究主题拆分为章节或任务，由多个 LLM Agent 检索文献/数据源、组织证据、生成报告或论文草稿，并支持用户编辑和再生成。当前无法确认其是否有具体生命科学实验对象、是否专门服务 drug discovery/biomedical research、是否做了系统 benchmark 或专家评估。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：暂定是。
- 判断依据：题名明确称 multi-agent virtual research team；任务涉及 scientific exploration、discovery 和 automated report generation，具备科研流程角色。
- 判定置信度：中低，需全文复核。
- 是否面向明确科研目标：部分是，面向 scientific exploration/discovery；具体科学对象不明确。
- 是否具有多步行动过程：可能有，模板/outline、检索、分章节生成、引用处理、报告生成。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：可能有，outline/template planning。
  - 工具调用：可能有，文献/数据库检索。
  - 反馈迭代：可能有人类编辑和 regeneration。
  - 自主决策：不确定。
  - 多 Agent 协作：题名支持。
- 在科研流程中承担的明确角色：文献检索与组织、报告/论文草稿生成、可能的假设生成和研究设计支持。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，更像科研工作流 Agent。
- 是否只是单次问答、摘要或分类：不确定；若全文显示只是写作模板/摘要工具，核心纳入强度需下降。
- 是否缺少行动闭环：当前证据不足。
- 若排除，排除理由：暂不排除，但必须保留 high-priority full-text review。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`01` 形式、信息与计算科学（作为独立 `01.04` bucket 的 filing path）。
- 二级类：`01.04` 通用科研 Agent / scientific workflow automation。
- 三级类：scientific exploration, drafting, and automated report generation assistant。
- 四级专题：General scientific research-agent systems。
- 四级专题是否为新增：否。
- 归类理由：当前可访问的一手来源都把贡献中心放在多 Agent 科研工作流、资料检索与论文/报告草稿生成上，而不是任何稳定的生命科学或医学对象结果。
- 归类置信度：中高。

### 2.2 对象优先判定

- 最终科学研究对象：通用 scientific exploration / drafting / report-generation workflow capability。
- 最终科学问题：多 Agent 虚拟科研团队能否通过模板化 workflow、工具调用与资料检索辅助科学探索并自动生成研究文稿。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：当前一手来源没有给出 concrete biology / biomedical object experiments，因此不能因为机构背景或 biomedical 语境就继续留在 `06` 或上推 `07`。

### 2.3 容易混淆的边界

- 可能误归类到：`06` 生命科学；`07` 医学与健康科学。
- 最终判定：独立 `01.04`。
- 判定理由：当前可访问的一手证据支持的是科研工作流 / 文稿生成 Agent，而不是 concrete life-science or biomedical object study。
- 是否需要二次复核：否，就当前 `06 / 07 / 01.04` 边界而言已可关闭；后续全文若公开，可补 task inventory，但不是当前分类落地前提。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：可能是。
- Planning Agent：可能是。
- Tool-using Agent：可能是。
- Retrieval-augmented Agent：可能是。
- Multi-Agent System：是，题名支持。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：可能是。
- Hybrid Agent：可能是。
- 其他：research writing/report generation agent。

### 3.2 科研流程角色

- 文献检索与阅读：可能是。
- 知识抽取与组织：可能是。
- 科学问题提出：可能。
- 假设生成：可能。
- 实验设计：可能但未确认。
- 仿真建模：未确认。
- 工具调用与代码执行：未确认代码执行；可能有数据库/API 检索。
- 实验执行：未确认。
- 数据分析：可能但未确认。
- 结果解释：可能。
- 证据评估与验证：未确认。
- 论文写作：是/很可能，题名明确 automated report generation。
- 端到端科研流程自动化：不确定，可能只是报告生成链条。

### 3.3 自主能力

- 任务分解：可能通过 outline/section agents。
- 计划生成：可能。
- 工具调用：可能。
- 记忆与状态维护：不确定。
- 反馈迭代：可能由用户编辑/再生成触发。
- 自主决策：不确定。
- 多 Agent 协作：题名支持。
- 环境交互：可能是文献数据库/内部资源。
- 闭环实验：未证实。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：可能。
- 实验驱动：未证实。
- 仿真驱动：否/未证实。
- 多模态：未证实。
- 多尺度建模：否。
- 高通量筛选：未证实。
- 知识图谱：未证实。
- 数字孪生：否。
- 机器人平台：否。
- 其他：RAG / scientific writing automation，待确认。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：科学探索和报告生成需要整合大量文献、数据、结构化写作和引用管理。
- 现有科研流程或方法的痛点：人工文献分析、章节组织和 manuscript/report drafting 耗时；跨章节一致性和引用准确性难维护。
- 核心假设或直觉：多 Agent 分工和模板化 workflow 可提高科研报告/探索流程效率。

### 4.2 系统流程

1. 输入：研究主题、科学问题或报告/论文模板；具体领域待确认。
2. 任务分解 / 规划：生成 outline 或选择模板，将工作拆成章节/子任务。
3. 工具、数据库、模型或实验平台调用：可能调用 PubMed、arXiv、Google Scholar 或内部数据源；需全文确认。
4. 中间结果反馈：用户可能编辑 outline/section 并触发再生成。
5. 决策或迭代：根据模板、上下文和引用更新草稿。
6. 输出：带引用的研究报告、综述/论文草稿或章节文本。

### 4.3 系统组件

- Agent 核心：generalist LLM agent、section/domain-specific agents（待确认）。
- 工具 / API / 数据库：文献数据库和内部资源，待确认。
- 记忆或状态模块：section context/shared memory，待确认。
- 规划器：outline/template generator，待确认。
- 评估器 / verifier：引用检查/文本后处理，待确认。
- 人类反馈或专家介入：用户选择、编辑和审批，待确认。
- 实验平台或仿真环境：未证实。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：未确认。
- 仿真验证：未确认。
- 高通量计算：未确认。
- 机器人实验：否。
- 湿实验：未确认。
- 临床数据：未确认。
- 真实场景部署：可能是产品/工具场景，未确认。
- 专家评估：未确认。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：未从可访问证据确认。
- 任务设置：科学探索与自动报告生成。
- 对比基线：未确认。
- 评价指标：未确认。
- 关键结果：未确认。
- 是否有消融实验：未确认。
- 是否有失败案例或负结果：未确认。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：当前证据不足；可能主要是系统平台/写作辅助。
- 科学贡献是否经过验证：未确认。
- 贡献强度判断：弱到中，待全文。
- 科学贡献类型：系统平台 / 报告生成 / 可能的假设生成。
- 证据强度：abstract+metadata，低。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一预测模型，而是多 Agent 科研工作流/报告生成系统。
- 与已有 Agent / 科研智能系统的区别：若全文属实，特色是 multi-agent virtual research team 和 automated report generation。
- 与同一科学领域其他 Agent 文献的关系：若归 06，可与 BioMaster、CellVoyager、SpatialAgent 比较；若归 01.04，应与 Agent Laboratory、AI Scientist、ResearchAgent 比较。
- 主要创新点：多 Agent 虚拟科研团队用于科学探索和自动报告生成，待全文核实。

## 7. 局限性与风险

- Agent 自主性不足：可能更像 assistant/copilot，是否能自主完成研究闭环不明。
- 科学验证不足：未确认系统输出经过实验、benchmark 或专家验证。
- 泛化性不足：如果依赖模板和特定数据源，复杂研究问题适应性有限。
- 工具链依赖：可能依赖外部数据库、RAG 和内部资源。
- 数据泄漏或 benchmark 偏差：未确认评测设计。
- 成本、可复现性或安全风险：自动科研写作存在引用幻觉、错误结论和生物医学误导风险。

## 8. 对综述写作的价值

- 可放入哪个章节：暂放生命科学/生物医学科研 Agent；更可能作为 `01.04` 通用科研写作/报告 Agent 边界案例。
- 可支撑哪个论点：多 Agent 可用于科研报告组织和证据整合，但证据强度必须谨慎。
- 可用于哪个表格或图：弱证据/待全文复核表；科研写作 Agent 表。
- 适合作为代表性案例吗：暂不适合作为强代表。
- 推荐引用强度：暂不引用或普通引用，待全文确认。
- 需要在正文中特别引用的页码 / 图 / 表：全文可得后补。
- 需要与哪些论文并列比较：Agent Laboratory、AI Scientist、ResearchAgent、BioMaster、HealthFlow。

## 9. 总结

### 9.1 一句话概括

证据受限的多 Agent 科研报告生成系统。

### 9.2 速记版 pipeline

1. 用户输入研究主题或报告模板。
2. 系统生成 outline 并拆分章节任务。
3. 多 Agent 可能检索资料并生成章节。
4. 系统处理引用和文本一致性。
5. 用户编辑并再生成报告。

### 9.3 标注字段汇总

```text
是否纳入：暂纳入，需全文复核
主类：01（独立 `01.04` bucket 的 filing path）
二级类：01.04 通用科研 Agent
三级类：scientific exploration / drafting / automated report generation
四级专题：General scientific research-agent systems
Agent 类型：LLM Agent?; Planning Agent?; Tool-using Agent?; Retrieval-augmented Agent?; Multi-Agent System; Human-in-the-loop Agent?; Hybrid Agent?
科研流程角色：文献检索与阅读?; 知识抽取与组织?; 假设生成?; 论文/报告写作; 端到端科研流程自动化?
自主能力：任务分解?; 计划生成?; 工具调用?; 反馈迭代?; 多 Agent 协作
验证方式：未确认
交叉属性：计算驱动; RAG?; scientific writing automation
科学贡献类型：系统平台; 报告生成; 假设生成?
证据强度：abstract+metadata，低；全文仍不可访问
归类置信度：中高
纳入置信度：中低
推荐引用强度：暂不引用 / 待全文确认
```
