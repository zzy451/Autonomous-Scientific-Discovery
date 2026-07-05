# Ke et al. 2025 - BioDisco: Multi-agent hypothesis generation with dual-mode evidence, iterative feedback and temporal evaluation

## 2026-07-05 Phase6NoteRevisionR25 harmonization

- Frozen landing decision: scientific_object_modules=06;07; object_coverage_mode=multi_module; primary_module_for_filing=07; general_method_bucket=none; source_limited=no.
- Current note-status rule: treat this record as already included / landed under the current authoritative pair; older to_read, pending, conservative-hold, or stale single-module / 01.04 shorthand below is superseded by this harmonization.
- Current PDF/source rule: the authoritative local archived PDF is Reference_PDF\07_Medical_and_Health_Sciences\Ke_2025_BioDisco.pdf; older pending, abstract-only, no-local-PDF, or stale source_limited=yes wording below is superseded by this harmonization.
## 2026-06-22 Batch21Partial1 final adjudication writeback

- `scientific_object_modules`: `06;07`
- `object_coverage_mode`: `multi_module`
- `has_concrete_object_experiments`: `yes`
- `general_method_bucket`: `none`
- `primary_module_for_filing`: `07`
- `first_hand_sources_checked`: arXiv abstract page `2508.01285`; arXiv PDF `https://arxiv.org/pdf/2508.01285`; ar5iv full text `2508.01285v2`; official GitHub `yujingke/BioDisco`; official PyPI `biodisco`
- `classification_evidence_source_level`: `first_hand_full_text`
- `note_revision_required`: `no`
- `module_assignment_evidence`: `07` is supported by explicit biomedical hypothesis-generation framing plus cardiovascular disease and NSCLC immunotherapy expert-evaluation domains; `06` is additionally supported by full-text benchmark and case evidence around genes, proteins, biological pathways, cell mechanisms, vascular smooth muscle cells, macrophages, and CD8+ T-cell exhaustion.
- `multi_module_object_coverage_note`: this note now lands the final `06;07` judgment. The older single-`07` wording was too narrow because the full text and official project artifacts also contain independent life-science object coverage beyond disease-centric evaluation.

**论文信息**
- 标题：BioDisco: Multi-agent hypothesis generation with dual-mode evidence, iterative feedback and temporal evaluation
- 作者：Yujing Ke; Kevin George; Kathan Pandya; David Blumenthal; Maximilian Sprang; Gerrit Grossmann; Sebastian Vollmer; David Antony Selby
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2508.01285
- PDF / 本地文件路径：本轮核对 arXiv abstract page、arXiv PDF `https://arxiv.org/pdf/2508.01285`、ar5iv full text `2508.01285v2`、official GitHub `https://github.com/yujingke/BioDisco` 与 PyPI `https://pypi.org/project/biodisco/`；未确认本地归档 PDF。
- 论文类型：系统论文 / biomedical hypothesis-generation agents
- 当前状态：to_read
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abs; Fig. 1; Methods | 多个 agents 组织知识图谱、文献检索、候选假设生成、critic scoring 与迭代 refinement | 高 |
| 科学对象归类 | `06;07`，primary=`07` | Introduction; Experiments; case studies | 论文把任务直接定义为 biomedical hypothesis generation，但 full text 与官方项目页同时覆盖基因、蛋白、通路和细胞机制对象 | 高 |
| 不进入 `01.04` | 是 | 全文任务定义与评测 | 不是通用 scientific-agent substrate；它围绕 biomedical evidence space 做具体任务、评测和 expert ranking | 高 |
| 方法流程 | dual-mode evidence + feedback loop | Fig. 1; Methods | planner 统筹 KG / literature evidence retrieval、hypothesis drafting、internal scoring、critic feedback 和 temporal evaluation | 高 |
| 实验验证 | temporal evaluation + expert evaluation | Results; evaluation sections | 使用 TruthHypo relation tasks、时间切分评测、人类专家成对比较与 Bradley-Terry ranking | 高 |

## 0. 摘要翻译

BioDisco 是一个面向 biomedical hypothesis generation 的多 Agent 系统。它把文献证据与 biomedical knowledge graph 证据并行接入，再通过内部评分和反馈循环逐步修正候选假设。论文不仅做时间切分评测，还用专家成对比较与 Bradley-Terry 排名评估假设质量。对象上，它的主展示模块仍是疾病机制、治疗靶点与转化医学问题，因此 primary filing 维持在 `07`；但全文与官方项目材料也清楚覆盖了基因、蛋白、通路和细胞机制层面的生命科学对象，所以本轮补记 `06`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统包含多 Agent 分工、检索与知识图谱工具调用、反馈迭代、内部打分与自主筛选
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：文献检索、知识组织、假设生成、证据比较、假设排序与迭代 refinement

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`06;07`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`07`
- Primary module for filing 说明：仅用于落盘与章节展示，不覆盖 `06;07` 的并行对象事实。
- 主展示模块一级类：`07`
- 主展示模块二级类：`07.04`
- 主展示模块三级类：biomedical hypothesis discovery
- 主展示模块四级专题：Therapeutic-target and disease-mechanism hypothesis agents
- 其他覆盖模块及对应层级路径：`06` 生命科学 -> genes / proteins / pathways / cell mechanisms
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：
  - `07`：biomedical hypothesis generation 是论文主任务表述；心血管疾病与 NSCLC immunotherapy 是最强评测与专家评估场景。
  - `06`：全文和官方项目页明确涉及 genes, proteins, pathways, gene-gene / chemical-gene relations、vascular smooth muscle cells、macrophages、CD8+ T-cell exhaustion 等生命科学对象。
- 归类理由：该系统以 biomedical discovery 为主轴，因此 primary=`07` 不变；但全文对象证据已超出纯疾病转化层，必须补记 `06` 才与当前 relaxed multi-module 规则一致。
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：biomedical hypotheses，同时覆盖疾病机制、治疗靶点、基因关系、蛋白与通路机制
- 最终科学问题：如何用双证据多 Agent 系统自动生成、修正并排序有价值的 biomedical hypotheses
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：KG + literature + critic loop 是方法实现，分类应跟随其实际检验的 biological / biomedical objects

### 2.3 容易混淆的边界

- 可能误归类到：仅 `07`，或退回 `01.04`
- 最终判定：`06;07`，primary=`07`
- 判定理由：疾病与治疗转化场景仍是论文最强主线，所以 `07` 保持 primary；但 genes / proteins / pathways / cells 的明示对象覆盖已经满足 `06` 的并行记录条件，因此不能继续写成单 `07`。
- 多模块覆盖说明：`07` 由 disease / therapeutic-target evaluation 支撑；`06` 由 molecular / cellular mechanism evidence 与 relation benchmark 支撑。
- `01.04` 判定说明：有明确 biomedical objects、relation tasks、专家评估与案例，不属于无具体对象实验的通用科研方法。
- 是否需要二次复核：否；当前分类判断不因缺全文而待复核。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：biomedical KG + literature dual-evidence agents

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：部分是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：是
- 数字孪生：否
- 机器人平台：否
- 其他：literature-grounded hypothesis discovery

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：biomedical hypothesis discovery 依赖异构证据整合，人工筛选效率低且稳定性差
- 现有科研流程或方法的痛点：单一路径的文献检索或 KG 推理都难以稳定生成高质量假设
- 核心假设或直觉：双证据输入与 critic feedback loop 可以同时提升假设的新颖性、可解释性与重要性

### 4.2 系统流程

1. 输入：biomedical research topic / discovery target
2. 任务分解 / 规划：planner 组织问题表述与证据检索策略
3. 工具、数据库、模型或实验平台调用：knowledge-graph retrieval、literature retrieval、hypothesis drafting、internal scoring
4. 中间结果反馈：critics 比较候选假设并给出 refinement 信号
5. 决策或迭代：系统保留高分假设、修正低分假设并继续搜索
6. 输出：带有评分与证据支持的 biomedical hypotheses

### 4.3 系统组件

- Agent 核心：planner + generators + critics
- 工具 / API / 数据库：biomedical knowledge graph、literature retrieval stack
- 记忆或状态模块：evidence context 与 scoring history
- 规划器：有
- 评估器 / verifier：internal critic scoring、human expert pairwise comparison、Bradley-Terry ranking
- 人类反馈或专家介入：用于终局质量评估
- 实验平台或仿真环境：temporal split evaluation over held-out future findings

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：TruthHypo 相关 benchmark relation tasks 与未来发现时间切分评测
- 任务设置：依据双证据生成并排序 biomedical hypotheses
- 对比基线：paired comparison baselines 与 ranking baselines
- 评价指标：novelty、importance、expert preference、Bradley-Terry score
- 关键结果：系统在 temporal evaluation 与 human expert evaluation 中表现稳定，并在疾病与机制相关场景中显示较强生成质量
- 是否有消融实验：有模块级 ablation 与 evidence-mode comparison
- 是否有失败案例或负结果：仍受 KG 与 literature coverage 限制

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：能提出新的 biomedical hypotheses，但仍主要停留在计算与专家评估层
- 科学贡献是否经过验证：部分是
- 贡献强度判断：中
- 科学贡献类型：假设 / 系统平台
- 证据强度：专家确认

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次 hypothesis drafting，而是把 KG、文献、critic 与 temporal evaluation 组成完整 discovery workflow
- 与已有 Agent / 科研智能系统的区别：强调 dual-mode evidence 和可量化的 temporal / expert evaluation
- 与同一科学领域其他 Agent 文献的关系：可与 disease-target discovery agents、life-science mechanism agents 以及通用 research-agent systems 比较
- 主要创新点：dual-evidence hypothesis generation、internal feedback loop、temporal evaluation

## 7. 局限性与风险

- Agent 自主性不足：高度依赖外部 KG 与检索栈
- 科学验证不足：缺少湿实验或临床闭环确认
- 泛化性不足：不同 biomedical subdomains 的迁移性仍待持续验证
- 工具链依赖：知识图谱完备度与文献检索质量直接影响表现
- 数据泄漏或 benchmark 偏差：需要继续审视 temporal split 与 relation benchmark 的构造方式
- 成本、可复现性或安全风险：专家评估成本较高，生产环境部署门槛较高

## 8. 对综述写作的价值

- 可放入哪个章节：`07.04` biomedical hypothesis-generation agents；同时可在 `06 / 07` 边界讨论中作为多模块样本
- 可支撑哪个论点：biomedical hypothesis agent 往往同时覆盖机制层生命科学对象，应按对象证据记录多模块，而不是只保留临床/药学主线
- 可用于哪个表格或图：hypothesis-generation agent 对比表；KG + literature dual-evidence workflow 图
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：Figure 1；temporal evaluation / expert evaluation sections；cardiovascular 与 NSCLC case discussions
- 需要与哪些论文并列比较：K-Dense Analyst；Talk2Biomodels；疾病靶点发现 agents；mechanism-discovery agents

## 9. 总结

### 9.1 一句话概括

双证据多 Agent 生物医学假设生成系统，同时覆盖机制层生命科学对象。

### 9.2 速记版 pipeline

1. 输入 biomedical 问题
2. 并行检索 KG 和文献证据
3. 生成候选假设
4. critics 打分并迭代修正
5. 输出排序后的 hypotheses

### 9.3 标注字段汇总

```text
是否纳入：to_read
科学对象模块：06;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：07
是否进入 01.04 存放区：否
主展示模块一级类：07
主展示模块二级类：07.04
主展示模块三级类：biomedical hypothesis discovery
主展示模块四级专题：Therapeutic-target and disease-mechanism hypothesis agents
其他覆盖模块及对应层级路径：06 -> genes / proteins / pathways / cell mechanisms
module_assignment_evidence：07 由 cardiovascular disease 与 NSCLC immunotherapy 评测支撑；06 由 genes、proteins、pathways、vascular smooth muscle cells、macrophages、CD8+ T-cell exhaustion 等对象证据支撑
multi_module_object_coverage_note：旧单 07 表述已更新为 06;07，保留 07 作为 primary filing
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; knowledge_graph
科学贡献类型：hypothesis; system_platform
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
