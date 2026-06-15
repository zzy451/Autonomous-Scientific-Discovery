# Naumov 2025 - DORA AI Scientist

**论文信息**
- 标题：DORA AI Scientist: Multi-agent Virtual Research Team for Scientific Exploration Discovery and Automated Report Generation
- 作者：Vladimir Naumov, Diana Zagirova, Sha Lin, Yupeng Xie, Wenhao Gou, Anatoly Urban, Nina Tikhonova, Khadija M. Alawi, Mike Durymanov, Fedor Galkin, et al.
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / arXiv / URL：https://doi.org/10.1101/2025.03.06.641840
- PDF / 本地文件路径：未获得可读全文；bioRxiv PDF 下载受站点挑战阻断
- 论文类型：系统论文 / biomedical research assistant
- 当前状态：待读全文 / 已纳入但需复核
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

证据级别：abstract+metadata（bioRxiv/PDF 访问受限，未完成全文阅读；note 内所有判断按低证据强度处理）。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 暂纳入；多 Agent 虚拟研究团队 | bioRxiv metadata; ResearchGate 摘要页；Moonlight 第三方摘要 | 介绍 DORA/Draft Outline Research Assistant，使用多个模板和 workflow 进行自动/半自动研究与报告生成 | 低-中 |
| 科学对象归类 | 主清单归 06 生命科学 | 主清单 ASD-0006；Insilico Medicine/Science42 传播材料称 drug discovery and biomedical research | 领域可能为生命科学/生物医学，也可能偏 07 医学或 01 通用科研系统 | 低 |
| 方法流程 | 模板选择、数据源接入、section agent 生成、引用检索和文本后处理 | 第三方摘要 | 用户选择模板和研究输入，DORA 调用 PubMed/ArXiv/Google Scholar/内部资源，分 section 生成报告 | 低 |
| 实验验证 | 未从全文核实 | 元数据/摘要层面 | 只确认有 preprint，未确认 benchmark、案例和指标细节 | 低 |
| 科学贡献 | 多 Agent 科研写作/探索助手 | 元数据/第三方摘要 | 可能贡献在 biomedical research automation 和 report generation | 低 |

## 0. 摘要翻译

证据限制说明：本次未能读取 bioRxiv 全文 PDF，以下为基于 bioRxiv/ResearchGate 元数据和第三方摘要的低证据强度概括。论文提出 DORA（Draft Outline Research Assistant），一个多 Agent 虚拟研究团队，用于科学探索、发现和自动报告生成。系统似乎提供研究论文、综述、报告等模板，并通过通用与领域特定 LLM Agent、外部数据库和内部资源，支持假设生成、文献分析、数据收集、实验/研究设计和 manuscript/report drafting。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：暂定是。
- 判断依据：题名与元数据明确称 multi-agent virtual research team；第三方摘要描述多个 section/domain-specific Agent 和 workflow。
- 判定置信度：中偏低，需全文复核。
- 是否面向明确科研目标：是，科学探索、biomedical/drug discovery research 和报告生成。
- 是否具有多步行动过程：从模板、数据源、文献/数据处理到报告生成，低证据强度支持。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：可能有，证据低。
  - 工具调用：可能调用 PubMed、ArXiv、Google Scholar、内部数据源，证据低。
  - 反馈迭代：可能支持用户编辑和 section regeneration，证据低。
  - 自主决策：不确定。
  - 多 Agent 协作：题名和摘要层面明确。
- 在科研流程中承担的明确角色：文献检索、数据/证据组织、报告/论文草稿生成，可能包括假设生成和实验设计。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，更像科研工作流 Agent。
- 是否只是单次问答、摘要或分类：不确定；若全文显示只是写作工具，核心纳入强度需下降。
- 是否缺少行动闭环：当前证据不足。
- 若排除，排除理由：暂不排除，但需要人工全文复核。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06 生命科学。
- 二级类：06.03 生物信息学 / 组学 / 生物医学研究 Agent。
- 三级类：biomedical research automation。
- 四级专题：Biology / omics research agents。
- 四级专题是否为新增：否。
- 归类理由：按用户要求和主清单主类写入 06；元数据和传播材料显示与 biomedical/drug discovery research 相关。
- 归类置信度：低。

### 2.2 对象优先判定

- 最终科学研究对象：当前证据显示为生物医学/药物发现相关研究任务，但不清楚是否有具体生命科学对象。
- 最终科学问题：多 Agent 能否帮助进行科学探索与自动报告生成。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：主清单暂按生命科学对象归类；若全文显示领域无关，应改为 01.04。

### 2.3 容易混淆的边界

- 可能误归类到：01.04 通用科研 Agent；07 医学与健康科学。
- 最终判定：暂按主清单 06。
- 判定理由：任务明确要求根据主清单主类落目录；当前无法修改主清单。
- 是否需要二次复核：是，高优先级。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是，证据中等。
- Planning Agent：可能。
- Tool-using Agent：可能。
- Retrieval-augmented Agent：可能，文献/引用检索是核心。
- Multi-Agent System：是。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：可能，用户模板选择和编辑。
- Hybrid Agent：是。
- 其他：research writing/report generation agent。

### 3.2 科研流程角色

- 文献检索与阅读：是，低-中证据。
- 知识抽取与组织：是，低-中证据。
- 科学问题提出：可能。
- 假设生成：可能。
- 实验设计：可能。
- 仿真建模：未证实。
- 工具调用与代码执行：未证实代码执行；数据库/API 调用可能。
- 实验执行：未证实。
- 数据分析：可能。
- 结果解释：可能。
- 证据评估与验证：引用检索/证据定位可能。
- 论文写作：是。
- 端到端科研流程自动化：部分，需全文确认。

### 3.3 自主能力

- 任务分解：可能通过模板和 section agent 实现。
- 计划生成：不确定。
- 工具调用：可能。
- 记忆与状态维护：可能通过 section/context memory。
- 反馈迭代：可能由用户编辑/再生成触发。
- 自主决策：不确定。
- 多 Agent 协作：是。
- 环境交互：文献数据库/内部资源。
- 闭环实验：未证实。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：可能。
- 实验驱动：未证实。
- 仿真驱动：否。
- 多模态：未证实。
- 多尺度建模：否。
- 高通量筛选：未证实。
- 知识图谱：未证实。
- 数字孪生：否。
- 机器人平台：否。
- 其他：RAG、科研写作自动化。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：科研探索和报告生成需要大量文献/数据整合、章节组织和引用管理，适合由多 Agent 辅助。
- 现有科研流程或方法的痛点：手动文献分析和 manuscript drafting 耗时，跨章节一致性和引用准确性难维护。
- 核心假设或直觉：以模板化 workflow 和分工 Agent 管理科研报告结构，可提高 biomedical research drafting 效率。

### 4.2 系统流程

1. 输入：研究主题、疾病/基因/药物等 biomedical 输入，或文档模板。
2. 任务分解 / 规划：选择或配置论文、综述、报告等模板，拆成章节任务。
3. 工具、数据库、模型或实验平台调用：可能调用 PubMed、ArXiv、Google Scholar、内部数据源和 RAG。
4. 中间结果反馈：用户可编辑 outline/section，系统可能重新生成相关章节。
5. 决策或迭代：按模板和上下文更新草稿。
6. 输出：研究报告、论文草稿或带引用的章节文本。

### 4.3 系统组件

- Agent 核心：generalist LLM agent、section/domain-specific agents。
- 工具 / API / 数据库：PubMed、ArXiv、Google Scholar、内部资源，证据低。
- 记忆或状态模块：section context/shared memory，证据低。
- 规划器：模板和 outline generation。
- 评估器 / verifier：引用检索/文本后处理，证据低。
- 人类反馈或专家介入：用户选择、编辑和审批。
- 实验平台或仿真环境：未证实。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：未证实。
- 仿真验证：未证实。
- 高通量计算：未证实。
- 机器人实验：否。
- 湿实验：未证实。
- 临床数据：未证实。
- 真实场景部署：可能是产品/工具场景，未证实。
- 专家评估：未证实。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：未从全文确认。
- 任务设置：科学探索与自动报告生成。
- 对比基线：未确认。
- 评价指标：未确认。
- 关键结果：未确认。
- 是否有消融实验：未确认。
- 是否有失败案例或负结果：未确认。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：当前证据不足，可能主要是系统平台/写作助手。
- 科学贡献是否经过验证：未能确认。
- 贡献强度判断：弱到中，待全文复核。
- 科学贡献类型：系统平台 / 报告生成 / 可能的假设生成。
- 证据强度：元数据与第三方摘要。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一预测模型，而是多 Agent 研究流程和报告生成系统。
- 与已有 Agent / 科研智能系统的区别：若全文属实，特色是模板化科研写作与 biomedical 数据源整合。
- 与同一科学领域其他 Agent 文献的关系：可与 STELLA、Biomni、HealthFlow、GeneAgent 比较，但需确认其发现/分析深度。
- 主要创新点：多 Agent 虚拟研究团队与自动报告生成。

## 7. 局限性与风险

- Agent 自主性不足：当前更像 assistant/copilot，是否能自主完成研究闭环不明。
- 科学验证不足：未确认系统输出经过实验或专家验证。
- 泛化性不足：模板和数据源依赖可能限制复杂研究问题。
- 工具链依赖：依赖外部数据库、RAG 和内部资源。
- 数据泄漏或 benchmark 偏差：未确认。
- 成本、可复现性或安全风险：生物医学写作中引用错误、幻觉和错误结论风险高。

## 8. 对综述写作的价值

- 可放入哪个章节：生命科学/生物医学研究 Agent，或通用科研写作 Agent 的边界案例。
- 可支撑哪个论点：多 Agent 可用于科研报告组织和生物医学证据整合，但证据强度需谨慎。
- 可用于哪个表格或图：低证据强度/待全文复核表；科研写作 Agent 表。
- 适合作为代表性案例吗：暂不适合作为强代表，适合作为待复核案例。
- 推荐引用强度：普通引用 / 待复核。
- 需要在正文中特别引用的页码 / 图 / 表：需全文后补。
- 需要与哪些论文并列比较：HealthFlow、STELLA、Biomni、Agent Laboratory。

## 9. 总结

### 9.1 一句话概括

证据受限的生物医学多 Agent 报告助手。

### 9.2 速记版 pipeline

1. 用户选择科研文档模板。
2. 输入主题或生物医学对象。
3. 多 Agent 检索资料并生成章节。
4. 系统补引用和润色文本。
5. 用户编辑并再生成报告。

### 9.3 标注字段汇总

```text
是否纳入：暂纳入，需全文复核
主类：06 生命科学（按主清单）
二级类：06.03
三级类：生物医学研究 Agent
四级专题：Biology / omics research agents
Agent 类型：LLM Agent; Retrieval-augmented Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：文献检索与阅读; 知识抽取与组织; 假设生成?; 实验设计?; 论文写作; 端到端科研流程自动化?
自主能力：任务分解?; 工具调用?; 记忆与状态维护?; 反馈迭代?; 多 Agent 协作
验证方式：未确认
交叉属性：计算驱动; 数据驱动?; RAG
科学贡献类型：系统平台; 报告生成; 假设生成?
证据强度：元数据/第三方摘要，低
归类置信度：低
纳入置信度：中偏低
推荐引用强度：普通引用 / 待复核
```
