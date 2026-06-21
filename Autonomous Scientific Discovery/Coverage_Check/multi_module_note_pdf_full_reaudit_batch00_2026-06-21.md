# Batch 00 多模块分类 / Note / PDF 全量复核报告

生成日期：`2026-06-21`  
复核范围：`ASD-0001` - `ASD-0010`  
复核模式：`Batch 00` 试运行；按主列表 confirmed core 平铺索引前 10 条推进

## 1. 本轮开始前基线

- 当前主列表表头基线：confirmed included + classified count = `451`
- 当前主列表表头基线：`needs_review` count = `0`
- 当前主列表表头基线：confirmed `08` count = `3`
- 当前主列表表头基线：expanded module assignment count = `564`
- 当前主列表表头基线：independent `01.04` bucket count = `20`
- 说明：`agent_master_paper_list.md` 的全表头统计仍处在 legacy filing fields + remarks overlay 的过渡阶段；本轮先完成 Batch 00 的 row-level 落地，不强行重写整表头统计块

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原模块或 `01.04` bucket | 本轮状态 / 本轮模块或 `01.04` bucket | primary_module_for_filing | 处理结论 | 理由 |
|---|---|---|---|---|---|---|
| ASD-0001 | Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists | `to_read`; legacy `04` | 保持 `04` | `04` | 保持分类；补归档 PDF path | arXiv 全文确认是材料发现 Agent，分类稳定 |
| ASD-0002 | HealthFlow: A Self-Evolving AI Agent with Meta Planning for Autonomous Healthcare Research | `to_read`; legacy `07` | 保持 `07` | `07` | 保持分类；补归档 PDF path；规范题名 | arXiv 全文确认是医疗研究 Agent，分类稳定 |
| ASD-0003 | CheMatAgent: Enhancing LLMs for Chemistry and Materials Science through Tree-Search Based Tool Learning | `to_read`; legacy `03` | `03;04` overlay 维持；规范题名 | `03` | 补归档 PDF path；题名标准化 | arXiv 全文已支持 `03;04` 多模块，旧单标题 `ChemAgent` 口径收敛到 `CheMatAgent` |
| ASD-0004 | InternAgent: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification | `to_read`; legacy `01/01.04` | `01;03;06;09;10` overlay 维持 | `01` | 补归档 PDF path；清理 note 中旧 `01.04` 叙述 | 原文有 12 个具体对象任务，不能再当作独立 `01.04` |
| ASD-0005 | A Multiagent-Driven Robotic AI Chemist Enabling Autonomous Chemical Research On Demand | `to_read`; legacy `03` | 新接受 `03;04` overlay；`source_limited=yes` | `03` | 重写短 note；主列表 remarks 补 `03;04` 与 source-limited | publisher abstract + official supporting-information page 已足够支持光催化有机反应 `03` + functional materials `04`；主文 PDF 仍受限 |
| ASD-0006 | DORA AI Scientist: Multi-agent Virtual Research Team for Scientific Exploration Discovery and Automated Report Generation | `to_read`; independent `01.04` | 保持 independent `01.04`; `source_limited=yes` | `01` | 主列表补充本轮 source-limited 说明 | Crossref 摘要 + 官方页面仍只稳定支持通用科研工作流 / 报告生成，不支持 `06/07` |
| ASD-0007 | Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents | `to_read`; legacy `04` | 保持 `04` | `04` | 补归档 PDF path；规范 note 头部来源信息 | arXiv 全文确认是材料假设生成框架 |
| ASD-0008 | Accelerating Drug Discovery Through Agentic AI: A Multi-Agent Approach to Laboratory Automation in the DMTA Cycle | `to_read`; legacy `07` | `07;03` overlay 维持 | `07` | 补归档 PDF path | 既有 DMTA/drug-discovery `07`，也有合成化学与 HPLC / purity / yield `03` |
| ASD-0009 | Agent-based learning of materials datasets from the scientific literature | `to_read`; legacy `04`; DOI/URL 缺失 | 保持 `04`；补 DOI/URL | `04` | 补归档 RSC PDF；补 DOI；规范 note 头部来源信息 | RSC 全文 / PDF 可访问，材料对象稳定 |
| ASD-0010 | El Agente: An Autonomous Agent for Quantum Chemistry | `to_read`; legacy `03` | 保持 `03` | `03` | 补归档 PDF path | arXiv 全文确认是量子化学多 Agent 系统 |

## 3. 本轮重点复核但未改动的分类结论

| ID | 题名 | 当前 scientific_object_modules / `01.04` bucket | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| ASD-0001 | Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists | `04` | 一手全文与现有分类一致；本轮主要补 PDF 归档 | 否 |
| ASD-0002 | HealthFlow: A Self-Evolving AI Agent with Meta Planning for Autonomous Healthcare Research | `07` | 一手全文与现有分类一致；benchmark 仍是医疗研究任务，不支持回收到 `01.04` | 否 |
| ASD-0007 | Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents | `04` | 全文是材料假设生成 benchmark / data 论文，但对象归类稳定 | 低优先 |
| ASD-0008 | `07;03` | `07;03` | 现有 relaxed multi-module overlay 已稳；本轮主要补 PDF 归档 | 否 |
| ASD-0009 | `04` | `04` | 对象稳定，但“是否足够强地留在 confirmed core”仍属于后续核心强度问题 | 是 |
| ASD-0010 | `03` | `03` | 全文与现有化学归类一致 | 否 |

## 4. 边界问题清单

`ASD-0005`
当前最重要的 `03 / 04` pilot 样本之一。摘要已经明确给出光催化有机反应与功能材料发现/优化两类对象，足以接受多模块；但主文 PDF 仍受 ACS 访问门控，后续应优先补全文确认二级类细化。

`ASD-0006`
这是典型的 `01.04 / 06 / 07` source-limited 样本。本轮可访问的一手来源仍然只支持通用 scientific exploration / report generation workflow，不支持生命/医学对象模块，因此保持 independent `01.04`；关键不是“要不要强行拉回领域类”，而是等待 bioRxiv 全文可访问时再复核。

`ASD-0009`
主边界不是对象类，而是 core-strength。材料对象非常稳定，但论文更偏材料数据构建 / literature-mining support；是否长期保留在 confirmed core，可在后续整库强度清洗时再处理。

## 5. 本轮后统计

- Batch 00 已处理记录数：`10`
- 成功归档主文 PDF 数：`8`
- source-limited 数：`2`（`ASD-0005`, `ASD-0006`）
- note 改写 / 更新数：`9`
- note 已核对但未文字重写数：`1`（`ASD-0006`）
- master-list row 更新数：`10`
- 当前主列表表头 authoritative baseline 仍为：
  - confirmed included + classified count = `451`
  - `needs_review` count = `0`
  - confirmed `08` count = `3`
  - expanded module assignment count = `564`
  - independent `01.04` bucket count = `20`

## 6. 结论

`Batch 00` 试运行已经验证了当前主控制方案可执行：可以从 `agent_master_paper_list.md` 的 confirmed core 平铺索引直接反查 note，按一手来源补齐 PDF 归档，并在不依赖旧 note 权威性的前提下同步修正 note 与 master-list remarks。

本轮最重要的实质性落点有三项：
- `ASD-0004` 的旧单一 `01.04` 叙述已在 note 层清理，回到 `01;03;06;09;10` 的 relaxed multi-module 理解。
- `ASD-0005` 在 source-limited 条件下被明确接受为 `03;04` 多模块，而不是继续停留在单模块 `03` 的短 stub 状态。
- `ASD-0006` 维持独立 `01.04`，但此次是基于 Crossref 摘要与官方页面的一手 source-limited 复核，而不是旧 note 惯性。

当前没有足够证据支持重构一级分类体系；当前问题仍主要集中在边界解释、source-limited 全文获取，以及 legacy 表头统计与 row-level relaxed overlay 之间的过渡不一致。
