# McCammon et al. 2026 - Autonomous seeking and mapping coral reef biodiversity hotspots with a multimodal AUV

## 2026-06-24 confirmed-core full reaudit revision

```text
paper_id: ASD-0724
final_agent_inclusion: yes
supported_modules: 06
primary_module_for_filing: 06
source_limited: yes
safety_access_status: doi-access-block-403-crossref-abstract-only
first_hand_sources_checked: Crossref DOI metadata / abstract for 10.1126/scirobotics.adx9939
pdf_archive_status: no local PDF archived; official Science landing/PDF returned 403 in this environment
metadata_note: legacy note lead "Brennan C. Phillips et al." is stale; official DOI metadata identifies the record under Seth McCammon et al.; note filepath remains unchanged for continuity only
adjudication_note: official DOI abstract directly supports biodiversity-hotspot seeking, mapping, and self-validation; keep 06, not 05 or 01.04
```

**论文信息**
- 标题：Autonomous seeking and mapping coral reef biodiversity hotspots with a multimodal AUV
- 作者：Seth McCammon; Levi Cai; Daniel Yang; John Walsh; John D. Cast; T. Aran Mooney; Yogesh Girdhar
- 年份：2026
- 来源 / venue：Science Robotics
- DOI / URL：https://doi.org/10.1126/scirobotics.adx9939
- PDF / 本地文件路径：本地未归档 PDF；Science landing/PDF 在本轮环境下为 `403`，因此当前笔记只能基于 Crossref 一手摘要级元数据
- first-hand source checked：Crossref DOI metadata / abstract
- 论文类型：研究论文 / embodied biodiversity-mapping agent
- 当前状态：confirmed-core full reaudit landed；`source_limited = yes`
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| metadata correction | 旧 lead 已修正为 `Seth McCammon et al.` | Crossref author metadata | note 文件名保留旧 lead 仅为路径连续性，paper-info 以 DOI metadata 为准 | 高 |
| first-hand source checked | Crossref abstract only | Crossref DOI metadata | 当前一手证据来自 DOI abstract / metadata，而非正文 | 高 |
| access / source status | `source_limited = yes` | Crossref; controller adjudication | Science landing/PDF 在本环境返回 `403`，无本地 PDF | 高 |
| Agent 纳入 | `yes` | Crossref abstract | 系统自主寻访并绘制 coral reef biodiversity hotspots，存在明确环境交互和任务闭环 | 中高 |
| 科学对象归类 | `06` | Crossref abstract | 研究对象是 biodiversity hotspots，而不是海洋物理过程或通用 AUV 平台 | 中高 |
| 关键科学动作 | hotspot seeking + mapping + self-validation | Crossref abstract | 使用 passive acoustics 与 visual sensing 定位热点，并用共定位多模态数据自验证热点显著性 | 中高 |
| 边界判断 | 不应改到 `05` 或 `01.04` | object-first adjudication | 平台位于海洋环境中不改变其生命科学对象归属 | 中高 |

## 0. 摘要翻译

Crossref 摘要显示，这篇论文针对 coral reef biodiversity hotspots 的发现与制图提出了一个 multimodal AUV 框架。它在真实加勒比海珊瑚礁案例中结合被动声学和视觉感知，自主寻找生物热点，并利用共定位多模态数据对热点显著性进行自验证。就本轮裁决而言，这已经足以稳住其生命科学对象覆盖，因此保留在 06，而不是 05 或 01.04。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确科研目标，具有环境交互、自主搜索、定位、制图与自验证
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 在科研流程中承担的明确角色：野外观测执行、热点发现、空间映射、自验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.02
- 三级类：marine biodiversity discovery
- 四级专题：autonomous marine-biodiversity hotspot mapping
- primary_module_for_filing：06
- 归类理由：最终科学对象是 coral reef biodiversity hotspots
- 归类置信度：中高（abstract-level first-hand only）

### 2.2 对象优先判定

- 最终科学研究对象：coral reef biodiversity hotspots
- 最终科学问题：如何在复杂海洋环境中自主寻找、定位并绘制生物多样性热点
- 为什么不是 05：海洋环境是运行场景，不是最终科学对象
- 为什么不是 01.04：存在明确生命科学对象、实地任务和对象级验证叙述

### 2.3 容易混淆的边界

- 可能误归类到：05；01.04
- 最终判定：保持 06
- 判定理由：object-first rule 以 biodiversity discovery 为核心

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Robot / Embodied Agent：是
- Hybrid Agent：是
- 其他：multimodal AUV science agent

### 3.2 科研流程角色

- 实验设计：部分是
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 证据评估与验证：是
- 端到端科研流程自动化：部分是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该系统：扩展对 coral reef biodiversity 的高分辨率自主调查能力
- 现有流程痛点：人工海洋野外调查成本高、覆盖不足、响应慢
- 核心方法：用多模态 AUV 将搜索、定位、制图与自验证合到同一闭环

### 4.2 系统流程

1. 输入海洋环境中的多模态信号
2. 自主决定搜索与接近策略
3. 结合被动声学和视觉感知定位热点
4. 用共定位多模态数据自验证热点显著性
5. 输出 biodiversity hotspot map

## 5. 实验与验证

### 5.1 验证方式

- 机器人实验：是
- 真实场景部署：是
- field deployment：是

### 5.2 数据、任务与指标

- 实验对象：healthy Caribbean reef 中的 coral reef biodiversity hotspot
- 任务设置：autonomous seeking, localization, mapping, self-validation
- 关键结果：AUV 定位到围绕 large `Dendrogyra` pillar coral 的 biological hotspot，并用共定位多模态数据自验证其 prominence

### 5.3 科学贡献

- 科学贡献类型：system_platform; biodiversity_discovery
- 贡献强度判断：中高
- 证据强度：crossref_abstract_only_real_world_case

## 6. 与已有工作的关系

- 与普通离线生态建模的区别：这里是具身自主野外观测系统
- 与海洋过程研究的区别：核心不是海洋物理过程，而是 biodiversity hotspot discovery
- 与边界案例的关系：是稳住 `06 / 05` 边界的重要对象优先样本

## 7. 局限性与风险

- source-limited：当前只有 Crossref 摘要级一手证据
- access 限制：Science landing/PDF 在本环境 `403`，无本地 PDF
- 细节不可见：更细粒度决策模块、评价指标与失败案例仍待全文
- 泛化性风险：不同海域与生态区的可迁移性仍需全文核对

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学 / biodiversity discovery / ecological field agents
- 可支撑哪个论点：海洋平台承载的 Agent 不会自动进入 05；关键仍看最终科学对象
- 适合作为代表性案例吗：是，但要保留 `source_limited = yes`
- 推荐引用强度：核心引用，但正文最好注明基于 DOI abstract-level first-hand evidence

## 9. 总结

### 9.1 一句话概括

这是一篇以 coral reef biodiversity hotspots 为对象的 multimodal AUV 自主寻访与制图论文，基于 DOI 摘要已经足以支持纳入 06，但当前仍是 `source_limited = yes`。

### 9.2 标注字段汇总

```text
是否纳入：yes
主类：06
二级类：06.02
三级类：marine biodiversity discovery
primary_module_for_filing：06
source_limited：yes
safety_access_status：doi-access-block-403-crossref-abstract-only
first_hand_sources_checked：Crossref DOI metadata / abstract only
Agent 类型：Robot / Embodied Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：experiment_execution; data_analysis; evidence_assessment_and_validation
验证方式：robotic_experiment; real_world_deployment; field_deployment
科学贡献类型：system_platform; biodiversity_discovery
证据强度：crossref_abstract_only_real_world_case
纳入置信度：medium_high_source_limited
推荐引用强度：core_with_source_limit_note
```
