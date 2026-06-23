# Tan et al. 2026 - Self-evolving AI agents for protein discovery and directed evolution

**论文信息**
- 标题：Self-evolving AI agents for protein discovery and directed evolution
- 作者：Yang Tan; Lingrong Zhang; Mingchen Li; Yuanxi Yu; Bozitao Zhong; Bingxin Zhou; Nanqing Dong; Liang Hong
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2603.27303
- PDF / 本地文件路径：当前写回以 arXiv abstract (`2603.27303`) 作为一手来源；本地未归档 PDF
- 论文类型：研究论文 / protein-engineering multi-agent system
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 论文将 `VenusFactory2` 界定为面向 protein discovery and directed evolution 的 self-evolving AI agents | 高 |
| 科学对象归类 | `06.03` | arXiv abstract | 直接对象是 protein discovery、directed evolution 与 protein-engineering tasks，而不是领域无关 research-agent benchmark | 高 |
| 方法流程 | natural-language demand -> dynamic workflow synthesis -> protein optimization | arXiv abstract | 系统会根据蛋白研究需求动态组织 workflows，而不是单次回答 | 高 |
| 边界判断 | 不应改到 `01.04` | object-first rule | 尽管平台感很强，但资源、任务和示例都稳定锚定在 protein engineering | 高 |
| 验证方式 | computational / workflow validation | abstract / repo | 当前主要是 protein-engineering workflow 级验证，后续需全文加强 case-depth 判断 | 中高 |

## 0. 摘要翻译

论文提出一个名为 `VenusFactory2` 的 self-evolving AI agent 系统，用于蛋白发现与定向进化。它并不是一个泛化到任意学科的科研 Agent 平台，因为系统要解决的具体问题、内置技能和示例任务都集中在 protein engineering，如稳定性优化、功能设计、突变筛选和数据库搜索。因此它应保留在 `06.03`，而不是回退到 `01.04`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在自然语言科研需求理解、workflow synthesis、工具调用和后续优化组织
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：蛋白设计、优化流程组织、工具调用、实验前计算筛选

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.03
- 三级类：protein discovery / directed evolution
- 四级专题：Self-evolving protein-discovery and directed-evolution agents
- 四级专题是否为新增：否
- 归类理由：最终科学对象是 protein engineering 和 directed evolution，不是领域无关科研能力平台
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：proteins, mutations, stability/function optimization tasks
- 最终科学问题：如何让 Agent 更自主地组织蛋白发现与优化流程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：self-evolving agent infrastructure 只是手段，稳定对象仍是蛋白工程问题

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 06.03
- 判定理由：如果仓库和论文案例是跨学科通用科研 workflow，应考虑 `01.04`；但当前一手摘要和官方仓库都强调 protein engineering
- 是否需要二次复核：需要，以确认全文中的具体蛋白发现案例强度

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：protein-engineering workflow agents

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：部分是
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：否
- 闭环实验：否，主要是研究 workflow orchestration

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：部分是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：部分是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：protein engineering tool ecosystem

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：提高蛋白发现与定向进化流程的自动化程度
- 现有科研流程或方法的痛点：蛋白优化流程复杂，跨数据库、模型和工具的衔接成本高
- 核心假设或直觉：self-evolving agents 可以根据研究需求动态合成更合适的蛋白工程 workflow

### 4.2 系统流程

1. 输入：自然语言形式的 protein-engineering research demand
2. 任务分解 / 规划：系统动态生成合适的工作流
3. 工具、数据库、模型或实验平台调用：调用与蛋白设计、搜索、优化相关的工具和资源
4. 中间结果反馈：根据中间结果重组后续步骤
5. 决策或迭代：继续执行蛋白发现或优化任务
6. 输出：服务于 protein discovery / directed evolution 的候选与分析结论

### 4.3 系统组件

- Agent 核心：VenusFactory2
- 工具 / API / 数据库：protein engineering skills and resources
- 记忆或状态模块：dynamic workflow state
- 规划器：workflow synthesis mechanism
- 评估器 / verifier：task outcome checks within protein workflows
- 人类反馈或专家介入：当前公开证据未完全展开
- 实验平台或仿真环境：protein-engineering computational ecosystem

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：部分是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：protein discovery and engineering tasks
- 任务设置：stability/function/mutation design/database search and optimization
- 对比基线：当前公开证据未展开
- 评价指标：workflow execution quality and protein-task effectiveness
- 关键结果：系统能够围绕蛋白工程任务动态组织和执行 workflow
- 是否有消融实验：当前笔记未展开
- 是否有失败案例或负结果：未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏向蛋白研究 workflow 自动化
- 科学贡献是否经过验证：有任务级验证迹象
- 贡献强度判断：中
- 科学贡献类型：system_platform; protein_discovery
- 证据强度：high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一蛋白预测模型，而是多 Agent 蛋白研究系统
- 与已有 Agent / 科研智能系统的区别：强调 self-evolving workflow synthesis
- 与同一科学领域其他 Agent 文献的关系：可与 BioLab、CASSIA、CellForge、Talk2Biomodels 对照
- 主要创新点：把 workflow synthesis 明确放到 protein discovery 和 directed evolution 上

## 7. 局限性与风险

- Agent 自主性不足：平台感较强，需全文确认真实案例深度
- 科学验证不足：目前仍主要依赖摘要和仓库级证据
- 泛化性不足：跨不同蛋白家族和任务类型的稳定性需确认
- 工具链依赖：强依赖蛋白工程工具生态
- 数据泄漏或 benchmark 偏差：当前证据不足以细评
- 成本、可复现性或安全风险：workflow 复现性待进一步核实

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学中的 protein-engineering agents
- 可支撑哪个论点：平台感很强的生命科学 Agent，只要对象稳定锚定在蛋白工程，就不应轻易退回 `01.04`
- 可用于哪个表格或图：`06.03 / 01.04` 边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：标准到核心之间
- 需要在正文中特别引用的页码 / 图 / 表：后续全文补充
- 需要与哪些论文并列比较：Jin_2025_BioLab_Life_Sciences; Singh_2025_Autonomous_Enzyme_Engineering

## 9. 总结

### 9.1 一句话概括

Self-evolving 多 Agent 系统自治组织蛋白发现与定向进化流程。

### 9.2 速记版 pipeline

1. 接收蛋白研究需求
2. 动态合成 workflow
3. 调用蛋白工程工具
4. 迭代输出发现或优化结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：06
二级类：06.03
三级类：protein discovery / directed evolution
四级专题：Self-evolving protein-discovery and directed-evolution agents
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; workflow_orchestration; tool_use_and_code_execution; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; protein_discovery
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：标准引用
```
## 2026-06-24 writeback adjudication

- `scientific_object_modules`: `06`
- `object_coverage_mode`: `single_module`
- `primary_module_for_filing`: `06`
- `general_method_bucket`: `none`
- `first_hand_sources_checked`: arXiv abstract `2603.27303`
- `classification_evidence_source_level`: `first_hand_abstract_or_landing_page`
- `source_limited`: `no`
- `note_revision_required`: `no`

This writeback keeps the protein-engineering and directed-evolution object framing explicit. The current first-hand basis is the arXiv abstract; no local PDF is archived, but the frozen adjudication does not treat this note as source-limited.
