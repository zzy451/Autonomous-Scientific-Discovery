# Zhang 2025 - OriGene

**论文信息**
- 标题：OriGene: A self-evolving virtual disease biologist automating therapeutic target discovery
- 作者：Zhang et al.
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / arXiv / URL：https://www.biorxiv.org/content/10.1101/2025.06.03.657658v1 ; https://gentel-lab.github.io/OriGene-Homepage/
- PDF / 本地文件路径：本轮依据官方主页与 bioRxiv PDF 链接信息
- 论文类型：系统论文 / 疾病机制与治疗靶点发现
- 当前状态：已读 / confirmed core 复核后继续保留 `07`
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Homepage abstract | virtual disease biologist, self-evolving, target nomination | 高 |
| 科学对象归类 | `07` | Homepage abstract | therapeutic target discovery, disease mechanism inference | 高 |
| 方法流程 | 多 Agent / 多证据整合 | Homepage description | 融合 disease ontologies, literature, networks, multi-omics | 高 |
| 实验验证 | 疾病案例与下游验证 | Homepage case studies | HCC, CRC, organoid, tumor fragments, humanized mouse model | 高 |
| 边界判断 | `07 > 06` | Homepage abstract / cases | biological evidence 是支撑层，最终对象是疾病导向靶点发现 | 高 |

## 0. 摘要翻译

OriGene 被描述为一个自演化的虚拟 disease biologist，用于自动化 therapeutic target discovery。系统围绕疾病机制推断、候选靶点提名与治疗假设生成展开，整合疾病本体、文献、多组学与功能网络证据，并在具体疾病场景下展示候选靶点的提名与验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备多步目标分解、证据整合、目标提名、批判与自演化机制
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：疾病机制推断者、证据整合者、治疗靶点提名者

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：07.04.01
- 四级专题：Disease-mechanism and therapeutic-target discovery agents
- 四级专题是否为新增：否
- 归类理由：最终输出是疾病相关 therapeutic target nomination 与验证
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：疾病机制与治疗靶点
- 最终科学问题：如何自动推断 disease mechanism 并提名可验证的 therapeutic targets
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：多组学与网络只是证据来源，不改变其疾病与治疗导向对象

### 2.3 容易混淆的边界

- 可能误归类到：06
- 最终判定：07
- 判定理由：虽然使用组学、网络与一般生物学证据，但最终对象不是生命机制本体，而是疾病语境下的治疗靶点发现
- 是否需要二次复核：需要，用于补全文与 wet-lab/validation 细节，不是为了改主类

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：可能有
- Hybrid Agent：是
- 其他：Self-evolving disease biologist

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分
- 假设生成：是
- 实验设计：部分
- 仿真建模：部分
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：较强

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：以知识与分析工具为主
- 闭环实验：弱到中

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：部分
- 仿真驱动：部分
- 多模态：部分
- 多尺度建模：是
- 高通量筛选：否
- 知识图谱：部分
- 数字孪生：否
- 机器人平台：否
- 其他：multi-omics integration

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：治疗靶点发现成本高、证据碎片化、人工整合慢
- 现有科研流程或方法的痛点：跨文献、网络、组学证据难统一处理
- 核心假设或直觉：自演化多 Agent 可以迭代整合疾病证据并更稳定地生成 target hypotheses

### 4.2 系统流程

1. 输入：疾病问题与候选生物对象
2. 任务分解 / 规划：拆为证据检索、机制推断、target nomination
3. 工具、数据库、模型或实验平台调用：disease ontologies, literature, networks, omics evidence
4. 中间结果反馈：多证据交叉核验与迭代排序
5. 决策或迭代：筛选并更新 therapeutic targets
6. 输出：疾病相关 target nomination 与治疗假设

### 4.3 系统组件

- Agent 核心：OriGene
- 工具 / API / 数据库：文献、disease ontologies、多组学与网络资源
- 记忆或状态模块：疾病上下文与证据积累
- 规划器：target discovery workflow
- 评估器 / verifier：下游病例与实验验证证据
- 人类反馈或专家介入：存在但不是主卖点
- 实验平台或仿真环境：案例层下游 wet-lab / disease validation

## 5. 实验与验证

### 5.1 验证方式

- benchmark：部分
- 仿真验证：部分
- 高通量计算：可能有
- 机器人实验：否
- 湿实验：是
- 临床数据：部分疾病语境
- 真实场景部署：否
- 专家评估：可能有

### 5.2 数据、任务与指标

- 数据集 / 实验对象：HCC, CRC 等疾病案例
- 任务设置：disease mechanism inference 与 therapeutic target nomination
- 对比基线：官方主页未完全展开
- 评价指标：候选靶点质量与下游验证支持
- 关键结果：给出可验证 target，并展示 organoid / mouse 等验证语境
- 是否有消融实验：待补全文
- 是否有失败案例或负结果：待补全文

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，以疾病相关靶点提名和机制假设为主
- 科学贡献是否经过验证：是，至少有病例与实验支撑
- 贡献强度判断：中到强
- 科学贡献类型：hypothesis
- 证据强度：expert_confirmed

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个预测器，而是完整的 disease-biologist Agent workflow
- 与已有 Agent / 科研智能系统的区别：最终对象稳定落在 therapeutic target discovery
- 与同一科学领域其他 Agent 文献的关系：可与 HealthFlow, DrugAgent, Robin 对照
- 主要创新点：自演化 disease-biologist 式 target discovery

## 7. 局限性与风险

- Agent 自主性不足：wet-lab 闭环程度需全文核实
- 科学验证不足：需要更完整 benchmark 与负例信息
- 泛化性不足：当前以疾病案例展示为主
- 工具链依赖：依赖高质量 disease knowledge 与 multi-omics evidence
- 数据泄漏或 benchmark 偏差：待全文核查
- 成本、可复现性或安全风险：疾病靶点评估需要强专家介入

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学 / therapeutic target discovery agents
- 可支撑哪个论点：多组学证据并不自动把论文归入 06，最终对象仍可能稳定落在 07
- 可用于哪个表格或图：06 / 07 边界案例表
- 适合作为代表性案例吗：适合
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：官方主页摘要与 disease case summary
- 需要与哪些论文并列比较：BioResearcher, PerTurboAgent, Robin

## 9. 总结

### 9.1 一句话概括

面向疾病机制与治疗靶点发现的虚拟 disease biologist。

### 9.2 速记版 pipeline

1. 读取疾病问题
2. 检索并整合文献、多组学与网络证据
3. 推断机制并提名候选靶点
4. 迭代排序与批判
5. 输出治疗假设与 target list

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：07.04.01
四级专题：Disease-mechanism and therapeutic-target discovery agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：wet_lab_experiment; expert_evaluation
交叉属性：computation_driven; data_driven; multiscale_modeling
科学贡献类型：hypothesis
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
