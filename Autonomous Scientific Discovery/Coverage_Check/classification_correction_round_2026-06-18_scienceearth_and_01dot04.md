# 分类纠错报告：Science Earth 与 `01.04` 高风险样本复核

生成日期：2026-06-18  
审计触发：用户指出 `Science Earth` 做了物理和生物相关实验，但当前主列表将其归入 `01`，要求复核 500 篇 confirmed 文献的分类错误风险。  
执行口径：按 `asd-literature-search-workflow`、`review_scope_and_classification_policy.md`、`domain_classification_rules.md`、`science_domain_taxonomy.md` 进行。

## 1. 本轮纠错后的最新状态

- confirmed included + classified count：`498`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当前主要边界压力点：
  - `01.04` 通用科研基础设施 / protocol / runtime 与具体学科对象论文的分界
  - review/roadmap/perspective 是否被误计入 confirmed core
  - `01.04` 中“跨学科案例展示”与“真正 domain-free scientific-agent system”之间的边界

## 2. 关于 `Science Earth` 的复核结论

### 2.1 记录信息

- ID：`ASD-0844`
- 题名：`Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery`
- 当前主类：`01 / 01.04`
- 本轮处理：**暂不改类，保留在 `01.04`**

### 2.2 用户质疑点

用户指出该论文做了物理和生物相关实验，因此怀疑它不应归入 `01`。

### 2.3 本轮复核依据

本轮核到的关键证据是：

- 论文确实包含两个具体 case：
  - 物理：Kuramoto synchronization
  - 生物：single-cell pan-cancer biology
- 但论文对自身对象的界定并不是“提出一个物理发现系统”或“提出一个生命科学发现系统”，而是把主对象定义为异构 scientific-agent coordination substrate / runtime / protocol。
- 论文明确区分了：
  - 本文承载的方法协议与协调层
  - companion papers 承载具体 scientific results

### 2.4 结论

虽然 `Science Earth` 使用了物理与生物案例，但这些案例在当前论文里更像“验证通用 scientific runtime 的跨域演示”，而不是本论文的主科学对象本体。

因此，按项目的对象优先规则，这篇论文目前更接近：

- 通用科研 Agent 运行时
- scientific coordination substrate
- domain-spanning research infrastructure

而不是：

- `02` 物理学论文
- `06` 生命科学论文
- 或 `05` 地球与环境科学论文

本轮判断：

- `Science Earth` **暂时留在 `01.04` 是合理的**
- 但它应被标记为 `01.04` 中的高风险边界样本，后续如 companion papers 被纳入，应分别按具体科学对象归类，而不是继续跟着 `Science Earth` 一起放在 `01`

## 3. 本轮确认的真实误分

本轮没有把 `Science Earth` 改类，但顺着这条线查出了两条更明确的误分：它们属于 review/roadmap/perspective，却被算进了 confirmed core。

### 3.1 ASD-0426

- 题名：`Towards Robot Scientists for autonomous scientific discovery`
- 原状态：`to_read`
- 原主类：`01 / 01.04`
- 本轮处理：改为 `background_only`

理由：

- 该文是对 Robot Scientist 概念、组件与原型系统的回顾/展望型文章，不是当前轮次应计入 confirmed core 的 primary system paper。
- 主列表此前把它从“基础性概念/背景”提升为 core confirmed，证据不足。

### 3.2 ASD-0527

- 题名：`Toward self-driving laboratory 2.0 for chemistry and materials discovery`
- 原状态：`to_read`
- 原主类：`01 / 01.04`
- 本轮处理：改为 `background_only`

理由：

- 该文由 publisher 标为 `Review Article`
- 摘要也明确是 chemistry/materials SDL 2.0 的 roadmap / vision / review，而不是单一 primary Agent study
- 因此应保留为 taxonomy/background supporting literature，而不应继续计入 confirmed core

## 4. 本轮纠错带来的计数变化

变更前：

- confirmed included + classified：`500`
- `01` 类 confirmed：`61`

变更后：

- confirmed included + classified：`498`
- `01` 类 confirmed：`59`

其余一级类 confirmed 数暂不变。

## 5. 当前仍需细审的 `01.04` 高风险样本

本轮识别出以下记录应作为下一批优先复核对象：

- `ASD-0373` `ChemOS: An orchestration software to democratize autonomous discovery`
- `ASD-0834` `AiSciVision: A Framework for Specializing Large Multimodal Models in Scientific Image Classification`
- `ASD-0837` `VESTA: Visual Exploration with Statistical Tool Agents`
- `ASD-0846` `SCP: Accelerating Discovery with a Global Web of Autonomous Scientific Agents`

这些记录的共同风险是：

- 题名或实验里带有具体学科线索
- 但主列表把它们判成 `01.04`
- 需要进一步确认它们究竟是：
  - 通用 scientific workflow / runtime / orchestration paper
  - 还是已经有稳定具体 scientific object 的领域论文

## 6. 当前阶段结论

### 6.1 关于 `Science Earth`

本轮结论不是“用户担心错了”，而是：

- 这个质疑非常有价值
- 但具体到 `Science Earth`，目前证据更支持它仍留在 `01.04`

### 6.2 关于整批 500 篇

用户指出的这个问题确实暴露出一类系统性风险：

- 过去把一部分“通用系统 / review / roadmap / protocol”放进 `01.04 confirmed` 时，标准有时偏松

本轮已经确认并修正了其中 2 条。

### 6.3 当前建议

下一轮不建议盲目全量重扫 498 篇，而建议继续按“高风险误分批次”推进：

1. 先清理 `01.04` 中 review/roadmap/protocol 型论文是否被误计入 confirmed
2. 再复核 `01.04` 中带具体领域实验的 domain-spanning 样本
3. 最后再扩展到 `11.07`、`05/10`、`06/07` 等次高风险边界
> 时间节点说明：本报告记录的是 `2026-06-18` 这一轮纠错中的中间快照。当时 confirmed included + classified 从 `500` 因两条降级而变为 `498`。此后同口径又继续收紧：`2026-06-18` 全库总结为 `478`，`2026-06-19` 跟进后进一步变为 `477`。因此，`498` 不是当前权威计数，只是该轮纠错落地后的阶段性数字。
