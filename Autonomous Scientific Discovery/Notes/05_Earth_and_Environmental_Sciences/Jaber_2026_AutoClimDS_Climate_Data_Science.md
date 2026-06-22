# Jaber et al. 2026 - AutoClimDS: Climate Data Science Agentic AI -- A Knowledge Graph is All You Need

## 2026-06-22 final adjudication sync

```text
scientific_object_modules: 05
object_coverage_mode: single_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 05
first_hand_sources_checked: Amazon Science preprint PDF / DOI landing page
classification_evidence_source_level: first_hand_full_text
source_limited: no
safety_flag: none
module_assignment_evidence: the checked preprint PDF directly reports a New York City sea-level climate-data case study executed through the AutoClimDS agent workflow, so the object evidence remains climate / Earth-system analysis rather than a domain-general research-agent runtime
multi_module_object_coverage_note: no additional module is needed under the relaxed rule because the demonstrated scientific object remains climate-data science throughout the workflow
note_revision_required: no
```

**论文信息**
- 标题：AutoClimDS: Climate Data Science Agentic AI -- A Knowledge Graph is All You Need
- 作者：Ahmed Jaber; Wangshu Zhu; Ayon Roy; Candace Agonafir; Linnia Hawkins; Karthick Jayavelu; Justin Downes; Sameer Mohamed; Tian Zheng
- 年份：2026
- 来源 / venue：IEEE CAI 2026 / arXiv
- DOI / arXiv / URL：https://doi.org/10.1109/CAI68641.2026.11536364
- PDF / 本地文件路径：本轮按 Amazon Science preprint PDF 与 DOI 落地页复核；当前未在 workspace 中确认到本地归档 PDF
- 论文类型：研究论文 / climate-data-science agentic workflow
- 当前状态：to_read
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | preprint PDF abstract / system overview | 系统将自然语言任务解析、数据发现、数据获取、预处理、分析与结果回传串成多步 climate-data agent workflow | 高 |
| 科学对象归类 | `05` | preprint PDF case study / task description | 本轮关键证据是 NYC sea-level climate case study 直接由 AutoClimDS workflow 执行，科学对象始终是气候与地球系统数据分析 | 高 |
| 方法流程 | climate query -> KG grounding -> dataset discovery -> acquisition -> preprocessing -> analysis -> output | preprint PDF method / workflow figure | 核心系统依赖 climate knowledge graph、数据接口与分析步骤编排，而不是通用科研代理壳层 | 高 |
| 边界判定 | 不进入 `01.04` | preprint PDF full text + DOI page | 即使平台感较强，已对具体 climate-data object 做了可识别 case study 与结果展示，按规则应留在 `05` | 高 |
| 实验验证 | 计算验证 / case-study validation | preprint PDF results / conclusion | 论文强调可复现已发表气候分析，并以 NYC sea-level 分析展示端到端执行 | 中高 |

## 0. 摘要翻译

论文提出 `AutoClimDS`，把 climate knowledge graph、数据接口与 agentic workflow 结合起来，让用户可以通过自然语言提出气候数据科学任务，再由系统自动完成数据发现、数据获取、预处理、分析和结果生成。与仅提供通用问答或代码补全的系统不同，这个工作把数据源、术语、分析路径和输出都绑在 climate-data science 场景中。本轮复核最关键的证据是 preprint PDF 直接给出了 New York City sea-level case study，说明它不是没有对象实验的通用科研 Agent，而是面向具体地球与环境科学对象的代理式分析系统。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕明确的 climate-data science 目标，执行多步任务分解、知识图谱检索、数据发现、工具调用、分析与结果返回
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未强调
- 在科研流程中承担的明确角色：知识组织、数据发现、工具调用、数据分析、结果解释、端到端科研流程自动化

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`05`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`05`
- Primary module for filing 说明：仅用于笔记落盘、排序和展示，不覆盖对象归类事实
- 主展示模块一级类：05
- 主展示模块二级类：05.02
- 主展示模块三级类：climate data science / sea-level and Earth-system analysis
- 主展示模块四级专题：climate-data-science agentic systems
- 其他覆盖模块及对应层级路径：无
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：`05` 来自 preprint PDF 直接展示的 NYC sea-level climate-data case study，以及围绕气候与地球系统数据源的端到端分析
- 归类理由：论文的稳定对象不是领域无关科研流程，而是气候数据、气候指标与 Earth-system analytical workflow
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：climate datasets、sea-level indicators、Earth-system analytical workflows
- 最终科学问题：如何让 Agent 自动完成面向气候数据科学任务的数据发现、获取、处理、分析和结果输出
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：knowledge graph、agentic orchestration 与 CAI / arXiv venue 都只是实现与发表载体，不能覆盖其稳定的气候科学对象

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `05` only
- 判定理由：本轮裁决明确依赖 Amazon Science preprint PDF 中直接落地的 NYC sea-level case study；只要已经对具体 climate-data object 做了可识别 case study，就不能回退到独立 `01.04`
- 多模块覆盖说明：未见需要独立计入其他对象模块的实验覆盖；论文所有关键对象证据都稳定落在地球与环境科学
- 01.04 判定说明：不属于 `01.04_general_asd_methods_without_concrete_object_experiments`
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：knowledge-graph-enabled climate workflow agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：否
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
- 多 Agent 协作：否
- 环境交互：否
- 闭环实验：否，以数据分析闭环为主

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：部分是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：是
- 数字孪生：否
- 机器人平台：否
- 其他：cloud-native data access

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低 climate-data science 的工具门槛并提升气候分析可复现性
- 现有科研流程或方法的痛点：数据源碎片化、访问方式异构、预处理链条复杂、分析复现成本高
- 核心假设或直觉：如果把 climate datasets、metadata、tools 和 workflows 编码进知识图谱并交由 Agent 调度，就能更稳定地完成气候分析任务

### 4.2 系统流程

1. 输入：自然语言形式的 climate-data science 任务
2. 任务分解 / 规划：解析问题并定位相关气候对象、指标与数据源
3. 工具、数据库、模型或实验平台调用：调用 climate KG、数据门户、API 与分析组件
4. 中间结果反馈：检查数据获取与预处理是否满足后续分析要求
5. 决策或迭代：根据中间结果调整数据选择、处理步骤或分析路径
6. 输出：可追溯的 climate analysis 结果与 case-study 输出

### 4.3 系统组件

- Agent 核心：AutoClimDS agentic workflow
- 工具 / API / 数据库：climate knowledge graph、climate data portals、analysis tools
- 记忆或状态模块：knowledge graph as structured scientific memory
- 规划器：query interpretation and workflow orchestration
- 评估器 / verifier：case-study execution validity and output checking
- 人类反馈或专家介入：允许用户指定目标与解释输出
- 实验平台或仿真环境：cloud-native climate data analysis environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：climate and Earth-system datasets，含 NYC sea-level case-study object
- 任务设置：从自然语言请求出发，自动完成 climate-data discovery、acquisition、preprocessing、analysis 与结果生成
- 对比基线：general-purpose assistant / generic LLM workflow
- 评价指标：是否能找到合适数据、执行可追溯流程并输出有效 climate analysis
- 关键结果：系统能围绕气候对象执行端到端流程，并展示 NYC sea-level climate-data case study
- 是否有消融实验：当前笔记未展开
- 是否有失败案例或负结果：当前笔记未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏向提供气候数据科学工作流能力与对象绑定的案例执行
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; climate_science_discovery
- 证据强度：computationally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单纯气候预测模型，而是围绕气候数据发现与分析的 agentic workflow
- 与已有 Agent / 科研智能系统的区别：突出 climate knowledge graph 作为领域记忆与流程约束
- 与同一科学领域其他 Agent 文献的关系：可与 CMIP-Forge、PANGAEA-GPT、OpenEarth Agent 等 climate-data / Earth-system agent 文献并列
- 主要创新点：把 climate KG、数据源和分析链条收束到面向具体气候对象的端到端代理执行中

## 7. 局限性与风险

- Agent 自主性不足：内部决策细节仍不如实验型 self-driving lab 那样强闭环
- 科学验证不足：更偏 case-study execution 与 workflow reproducibility，而非新自然规律发现
- 泛化性不足：跨更多气候任务的稳定性仍需更多全文细节
- 工具链依赖：高度依赖 climate KG 与外部数据门户
- 数据泄漏或 benchmark 偏差：当前公开材料不足以细评
- 成本、可复现性或安全风险：云端数据访问与长期接口稳定性仍需关注

## 8. 对综述写作的价值

- 可放入哪个章节：05 地球与环境科学中的 climate-data-science agents
- 可支撑哪个论点：平台感很强的科研 Agent 只要已经对具体气候对象做了可识别 case study，就不应退回 `01.04`
- 可用于哪个表格或图：`05 / 01.04` 边界案例表；地球环境 Agent 工作流对比表
- 适合作为代表性案例吗：是
- 推荐引用强度：标准引用
- 需要在正文中特别引用的页码 / 图 / 表：preprint PDF 中 NYC sea-level case-study 所在结果段落
- 需要与哪些论文并列比较：Pantiukhin_2026_CMIP_Forge; Zhao_2026_OpenEarth_Agent; Zhang_2026_TianJi_Environ_Atmospheric_Research

## 9. 总结

### 9.1 一句话概括

面向 NYC 海平面案例的气候数据科学 Agent。

### 9.2 速记版 pipeline

1. 读取气候研究请求
2. 用知识图谱定位数据与指标
3. 自动获取并处理气候数据
4. 执行分析并返回 case-study 结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
科学对象模块：05
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：05
是否进入 01.04 存放区：no
主展示模块一级类：05
主展示模块二级类：05.02
主展示模块三级类：climate data science / sea-level and Earth-system analysis
主展示模块四级专题：climate-data-science agentic systems
其他覆盖模块及对应层级路径：none
module_assignment_evidence：Amazon Science preprint PDF directly includes a NYC sea-level climate-data case study executed through the AutoClimDS workflow
multi_module_object_coverage_note：single-module 05 is sufficient because the demonstrated scientific object remains climate-data science throughout
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; knowledge_graph
科学贡献类型：system_platform; climate_science_discovery
证据强度：computationally_validated
归类置信度：high
纳入置信度：high
推荐引用强度：standard
```
