# McNaughton et al. 2024 - CACTUS: Chemistry Agent Connecting Tool Usage to Science

**论文信息**
- 标题：CACTUS: Chemistry Agent Connecting Tool Usage to Science
- 作者：Andrew D. McNaughton, Gautham Ramalaxmi, Agustin Kruel, Carter R. Knutson, Rohith A. Varikoti, Neeraj Kumar
- 年份：2024
- 来源 / venue：ACS Omega；arXiv preprint
- DOI / arXiv / URL：https://doi.org/10.1021/acsomega.4c08408；https://arxiv.org/abs/2405.00972
- PDF / 本地文件路径：临时读取 arXiv PDF；未写入 `Reference_PDF`
- 论文类型：系统论文 / 化学工具调用 Agent / benchmark
- 当前状态：已读 / 已纳入
- 阅读日期：2026-06-16
- 笔记作者：Codex

## Evidence Log

Evidence level: arXiv PDF full text + ACS/PubMed metadata.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，LangChain MRKL / ReAct 化学工具 Agent | Abstract; Sec. 2.1; Fig. 1 | CACTUS 使用 tools、LLMChain 和 zero-shot agent class，按 planning-action-execution-observation 选择工具 | 高 |
| 科学对象归类 | `03` 化学科学，分子性质、cheminformatics、drug-like assessment | Abstract; Sec. 2.2; Table 1 | 集成 RDKit、PubChem、ChEMBL、ZINC 等工具，回答分子性质和 drug-likeness 问题 | 高 |
| 方法流程 | 用户问题 - ReAct 推理 - 选择化学工具 - 执行 - observation - 输出答案 | Fig. 1; Sec. 2.1-2.4 | 工具集合包含 10 个分子描述符/过滤器/ADME 相关工具 | 高 |
| 实验验证 | benchmark 验证，1000 个 cheminformatics 问题；无湿实验 | Sec. 2.4; Sec. 3; Fig. 2-4 | 比较多种 7B open-source LLM、prompt 和硬件配置，正确/错误计分 | 高 |
| 科学贡献 | 开源小模型可部署化学工具 Agent，科学发现贡献为工具平台 | Conclusion; Code Availability | 可辅助分子 property prediction、similarity search、drug-likeness assessment；尚未报告新分子实验发现 | 高 |

## 0. 摘要翻译

CACTUS 是一个 LLM-based chemistry agent，将开源 LLM 与 cheminformatics 工具结合，用于化学和分子发现问题求解。系统评估了 Gemma-7B、Falcon-7B、MPT-7B、Llama2-7B、Mistral-7B 等模型在数千个化学问题上的表现，并分析了 domain prompt 和硬件部署的影响。作者认为 CACTUS 可以支持 molecular property prediction、similarity searching 和 drug-likeness assessment，并为自动化发现平台提供工具调用基础。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：CACTUS 使用 LangChain MRKL / zero-shot ReAct agent，根据用户问题决定工具选择和工具调用顺序。
- 判定置信度：高。
- 是否面向明确科研目标：是，cheminformatics 和 molecular discovery。
- 是否具有多步行动过程：是，planning、action、execution、observation、final answer。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是，ReAct planning 阶段。
  - 工具调用：是，核心能力。
  - 反馈迭代：弱到中，observation 参与回答，但不是深度闭环优化。
  - 自主决策：是，自动选择工具。
  - 多 Agent 协作：否。
- 在科研流程中承担的明确角色：化学性质查询、分子筛选、分子发现辅助工具。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否。
- 是否只是单次问答、摘要或分类：否，Agent 会调用外部工具。
- 是否缺少行动闭环：有基本 ReAct 行动闭环，但缺少实验反馈闭环。
- 若排除，排除理由：不适用。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`03` 化学科学。
- 二级类：`03.04` 化学信息学、分子发现与化学 Agent。
- 三级类：cheminformatics 工具调用和分子性质评估。
- 四级专题：Chemistry agents / molecular discovery。
- 四级专题是否为新增：否。
- 归类理由：系统围绕分子结构、分子描述符、ADME、drug-likeness 和化学数据工具。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：小分子、分子描述符、药物相似性、ADME/毒性过滤。
- 最终科学问题：如何用 LLM Agent 调用 cheminformatics 工具辅助分子发现。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LangChain/ReAct 是技术实现，主对象为化学分子。

### 2.3 容易混淆的边界

- 可能误归类到：`07` 医学与健康科学；`01.04` 通用科研 Agent。
- 最终判定：`03`。
- 判定理由：虽然提到 drug discovery，但任务本身是化学信息学与分子性质评估，不以临床/治疗转化为核心验证。
- 是否需要二次复核：否。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：部分，访问 PubChem/ChEMBL/ZINC 等。
- Multi-Agent System：否。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：否。
- Hybrid Agent：是。
- 其他：MRKL / ReAct chemistry agent。

### 3.2 科研流程角色

- 文献检索与阅读：否。
- 知识抽取与组织：弱。
- 科学问题提出：否。
- 假设生成：弱，future outlook 中讨论。
- 实验设计：弱，主要是未来潜力。
- 仿真建模：否。
- 工具调用与代码执行：核心。
- 实验执行：否。
- 数据分析：核心，分子属性/过滤器。
- 结果解释：中。
- 证据评估与验证：benchmark。
- 论文写作：否。
- 端到端科研流程自动化：弱。

### 3.3 自主能力

- 任务分解：中。
- 计划生成：中。
- 工具调用：强。
- 记忆与状态维护：弱。
- 反馈迭代：中。
- 自主决策：中。
- 多 Agent 协作：否。
- 环境交互：与化学 Python 工具和数据库交互。
- 闭环实验：否。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：否。
- 仿真驱动：否。
- 多模态：否。
- 多尺度建模：否。
- 高通量筛选：潜在应用，本文非核心。
- 知识图谱：否。
- 数字孪生：否。
- 机器人平台：否。
- 其他：开源小模型部署。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：普通 LLM 缺乏访问实时/专业化学数据与工具的能力，难以可靠处理分子发现问题。
- 现有科研流程或方法的痛点：cheminformatics 工具分散且需要专业编程；LLM 单独回答可能幻觉。
- 核心假设或直觉：将开源 LLM 与 RDKit、数据库和过滤器工具结合，可以让小模型成为可部署的分子发现助手。

### 4.2 系统流程

1. 输入：用户自然语言化学问题，通常涉及 SMILES。
2. 任务分解 / 规划：LLMChain 和 ReAct prompt 分析问题。
3. 工具、数据库、模型或实验平台调用：调用分子量、LogP、TPSA、QED、SA、BOILED-Egg、drug-likeness、PAINS、Brenk 等工具。
4. 中间结果反馈：工具输出作为 observation。
5. 决策或迭代：Agent 根据 observation 组织最终答案；复杂迭代有限。
6. 输出：分子性质、过滤结果或解释。

### 4.3 系统组件

- Agent 核心：LangChain custom MRKL agent / zero-shot ReAct agent。
- 工具 / API / 数据库：RDKit、SciPy、PubChem、ChEMBL、ZINC、10 个当前工具。
- 记忆或状态模块：ReAct 轨迹。
- 规划器：LLMChain prompt + zero-shot agent class。
- 评估器 / verifier：benchmark 正确答案。
- 人类反馈或专家介入：无在线 HITL。
- 实验平台或仿真环境：无。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：核心。
- 仿真验证：否。
- 高通量计算：否。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：未作为主验证。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：qualitative 500 questions、quantitative 500 questions、combined 1000 questions。
- 任务设置：回答分子性质、ADME、过滤器等 cheminformatics 问题。
- 对比基线：多个 7B/小型开源 LLM，minimal prompt 与 domain prompt，A100/V100/RTX 2080 Ti 等部署条件。
- 评价指标：accuracy、推理时间/硬件效率。
- 关键结果：CACTUS 显著优于 baseline LLM；Gemma-7B 和 Mistral-7B 表现突出；小模型在消费级硬件上仍有可用性。
- 是否有消融实验：有 prompt 和硬件/模型设置比较。
- 是否有失败案例或负结果：讨论了本地推理速度、prompt engineering 和部署挑战。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：否。
- 科学贡献是否经过验证：通过化学问题 benchmark 验证工具问答能力。
- 贡献强度判断：中。
- 科学贡献类型：系统平台 / benchmark。
- 证据强度：benchmark。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不只是训练分子性质模型，而是让 LLM 自主选择和调用化学工具。
- 与已有 Agent / 科研智能系统的区别：比 ChemCrow 更强调开源小模型和可部署性；后续 ChemAgent/ChemAmp 将它作为工具来源或比较对象。
- 与同一科学领域其他 Agent 文献的关系：可作为化学工具 Agent 早期代表，与 ChemCrow、ChemAgent、ChemAmp、ChemGraph 构成工具调用路线。
- 主要创新点：开源 LLM + cheminformatics 工具的可部署 Agent；系统性硬件/模型/prompt 评估。

## 7. 局限性与风险

- Agent 自主性不足：主要处理用户给定问题，不主动提出研究计划。
- 科学验证不足：没有真实实验发现。
- 泛化性不足：当前输入主要依赖 SMILES，工具数量有限。
- 工具链依赖：依赖 RDKit/数据库和模型服务。
- 数据泄漏或 benchmark 偏差：benchmark 为作者构建，需外部复现。
- 成本、可复现性或安全风险：药物筛选建议不能脱离专家和实验验证。

## 8. 对综述写作的价值

- 可放入哪个章节：化学工具调用 Agent；开源小模型科研 Agent。
- 可支撑哪个论点：Agent 的关键价值之一是把 LLM 连接到可靠专业工具，而非让模型凭记忆回答。
- 可用于哪个表格或图：化学 Agent 工具池表；验证强度表。
- 适合作为代表性案例吗：适合作为早期化学工具 Agent 案例。
- 推荐引用强度：普通引用。
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1；Table 1-2；Sec. 3。
- 需要与哪些论文并列比较：ChemCrow、ChemAgent、ChemAmp、ChemToolAgent。

## 9. 总结

### 9.1 一句话概括

开源 LLM 驱动的分子性质工具调用 Agent。

### 9.2 速记版 pipeline

1. 用户输入分子问题。
2. ReAct Agent 判断应调用的工具。
3. 执行 RDKit/数据库/过滤器工具。
4. 读取 observation。
5. 生成化学解释或答案。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：03 化学科学
二级类：03.04
三级类：cheminformatics 工具调用和分子性质评估
四级专题：Chemistry agents / molecular discovery
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：工具调用与代码执行; 数据分析; 结果解释
自主能力：计划生成; 工具调用; 自主决策; 环境交互
验证方式：benchmark
交叉属性：计算驱动; 数据驱动
科学贡献类型：系统平台; benchmark
证据强度：benchmark
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
