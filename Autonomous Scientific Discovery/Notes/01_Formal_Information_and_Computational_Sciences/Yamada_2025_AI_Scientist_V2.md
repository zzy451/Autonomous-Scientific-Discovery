# Yamada 2025 - The AI Scientist-v2

**论文信息**
- 标题：The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
- 作者：Yamada et al.
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2504.08066
- PDF / 本地文件路径：`Reference_PDF/01_Formal_Information_and_Computational_Sciences/Yamada_2025_AI_Scientist_V2.pdf`
- 论文类型：系统论文 / automated scientific discovery agent
- 当前状态：已读 / 已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

## 2026-06-20 relaxed round-2 multi-module revision

- Round decision: update the relaxed overlay from independent `01.04` to `scientific_object_modules=01`.
- Source checked in this round: arXiv abstract page for `2504.08066`.
- Reason: under the current object-coverage rule, the paper is not only a general ASD workflow. It reports concrete formal/computational research activity: ML hypothesis generation, code experiment execution, data analysis, paper generation, and workshop peer review of AI-generated ML manuscripts.
- Current filing note: legacy `Main class` / `Secondary class` remain unchanged until schema migration, but old `01.04`-only language is superseded for relaxed-counting purposes.
- general_method_bucket: `none`; `primary_module_for_filing=01`; `object_coverage_mode=single_module`.

证据级别：full-text（arXiv PDF 已读取并抽取文本）。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 纳入；端到端自动科研 Agent | Abstract; Fig. 1; Sec. 3 | 系统生成假设、设计并执行实验、分析/可视化数据、撰写论文、自动 review/refine | 高 |
| 科学对象归类 | `01` 形式、信息与计算科学 | Abstract; Fig. 1-2; Sec. 3-4 | 具体对象是 machine learning research tasks、code experiments、AI-generated ML manuscripts 与 workshop review evidence，不再接受仅按独立 `01.04` 处理 | 高 |
| 方法流程 | idea generation -> agentic tree search experiments -> VLM feedback -> manuscript/review | Fig. 1-2; Sec. 3 | Experiment manager agent 管理四阶段实验，节点生成代码、执行、可视化、debug、replicate/aggregate | 高 |
| 实验验证 | ICLR workshop peer review + internal analysis | Sec. 4; extracted lines 367-406 | 三篇 AI 生成稿提交 ICBINB workshop，其中一篇平均 6.33/10，达到 workshop acceptance threshold | 高 |
| 科学贡献 | workshop-level fully AI-generated paper milestone | Abstract; Sec. 4; Limitations | 证明端到端 AI 科研系统能产生接近 workshop 接收水平的机器学习论文 | 高 |

## 0. 摘要翻译

论文提出 The AI Scientist-v2，一个基于 agentic tree search 的自动科学发现框架。系统能从广泛主题生成研究假设，设计和执行代码实验，分析和可视化结果，撰写完整论文，并通过 AI reviewer 与 VLM feedback 进行改进。相较 v1，v2 去掉人工代码模板依赖，引入 experiment manager agent 和树搜索实验探索。作者将三篇完全由系统生成的论文提交到 ICLR 2025 workshop peer review，其中一篇获得足以超过 workshop 接收阈值的平均评分。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：端到端多阶段 Agent 系统，包含规划、代码执行、实验反馈、VLM 评估、论文写作和 review。
- 判定置信度：高。
- 是否面向明确科研目标：是，自动机器学习/AI 研究发现与论文生成。
- 是否具有多步行动过程：是。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是。
  - 工具调用：是，Python interpreter、代码库、Semantic Scholar、VLM、reviewer。
  - 反馈迭代：是，tree search、debug、replication、review refinement。
  - 自主决策：是，experiment manager 选择 best node 和下一阶段。
  - 多 Agent 协作：包含 experiment manager / reviewer / VLM 等角色，系统层面多组件协作。
- 在科研流程中承担的明确角色：假设生成、实验设计、代码执行、数据分析、图表生成、论文写作、同行评议模拟。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，是科研流程自动化系统。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：01 形式、信息与计算科学。
- 二级类：01.02 计算机科学 / 人工智能与机器学习研究自动化。
- 三级类：01.02.12 / 01.02.13 人工智能与机器学习研究。
- 四级专题：AI/ML research automation agents。
- 四级专题是否为新增：否。
- 归类理由：主对象是自动科研系统本身和机器学习研究自动化能力。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：自动科学发现系统、AI/ML 研究流程、科研论文生成。
- 最终科学问题：Agent 能否自主产生足以通过 workshop peer review 的科学论文。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：归入 `01` 不是因为用了 LLM，而是因为论文实际实验对象是 AI/ML 代码实验、机器学习研究任务与可执行计算研究流程。

### 2.3 容易混淆的边界

- 可能误归类到：AI/机器学习具体方法方向；11.07 科学系统研究。
- 最终判定：`01`。
- 判定理由：论文虽然系统感很强，但其验证对象并非“无对象通用方法”，而是具体的机器学习研究任务、代码实验和 AI 生成论文评审结果。
- 是否需要二次复核：低。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，idea generation 使用 Semantic Scholar。
- Multi-Agent System：系统含多个 Agent 角色/组件，可标记。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：peer review 阶段有人类评审，但生成流程不依赖人工。
- Hybrid Agent：是。
- 其他：agentic tree search research agent。

### 3.2 科研流程角色

- 文献检索与阅读：是。
- 知识抽取与组织：是。
- 科学问题提出：是。
- 假设生成：是。
- 实验设计：是。
- 仿真建模：机器学习实验。
- 工具调用与代码执行：是。
- 实验执行：是，代码实验。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：是，replication/aggregation/review。
- 论文写作：是。
- 端到端科研流程自动化：是。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：tree nodes、checkpoints、experiment manager state。
- 反馈迭代：是。
- 自主决策：是。
- 多 Agent 协作：是。
- 环境交互：代码环境、数据集、VLM feedback。
- 闭环实验：计算实验闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：计算实验。
- 仿真驱动：否。
- 多模态：是，VLM 反馈图表。
- 多尺度建模：否。
- 高通量筛选：并行实验节点，非化学高通量。
- 知识图谱：否。
- 数字孪生：否。
- 机器人平台：否。
- 其他：agentic tree search、automated peer review。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：AI Scientist-v1 依赖人工模板、实验线性且探索浅，无法支撑更深的开放科研探索。
- 现有科研流程或方法的痛点：自动科研需要非线性探索、debug、replication、aggregation 和论文质量反馈。
- 核心假设或直觉：将科研实验建模为树搜索，让 Agent 并行探索、选择、复制和聚合节点，可提高研究质量。

### 4.2 系统流程

1. 输入：topic-specific prompt 或 workshop 范围主题。
2. 任务分解 / 规划：生成初始 idea；experiment manager 分四阶段管理 feasibility、baseline、main experiment、ablation/robustness 等。
3. 工具、数据库、模型或实验平台调用：Semantic Scholar、Python interpreter、dataset/codebase、VLM、AI reviewer。
4. 中间结果反馈：代码执行错误、实验指标、图像/VLM 反馈、reviewer feedback。
5. 决策或迭代：tree search 中选择 best node、debug buggy node、生成 child nodes、replicate 和 aggregate。
6. 输出：完整科学论文、图表、代码、实验数据和 review/refinement 记录。

### 4.3 系统组件

- Agent 核心：idea generation、Experiment Progress Manager、LLM code/plan generator、AI reviewer、VLM feedback module。
- 工具 / API / 数据库：Semantic Scholar、Python interpreter、ML datasets/codebases、LaTeX/paper writer。
- 记忆或状态模块：tree nodes、experiment scripts、metrics、summaries、stage checkpoints。
- 规划器：agentic tree search + experiment manager。
- 评估器 / verifier：VLM figure checks、AI reviewer、human workshop reviewers、replication/aggregation nodes。
- 人类反馈或专家介入：正式 peer review；系统生成后人工 workshop 评审。
- 实验平台或仿真环境：机器学习代码实验环境。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：系统内部评估和 workshop review。
- 仿真验证：否。
- 高通量计算：并行代码实验。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：否。
- 真实场景部署：真实 ICLR workshop peer review 流程。
- 专家评估：是，workshop reviewers。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：机器学习研究任务与 ICBINB workshop 主题；三篇 AI 生成论文。
- 任务设置：从 broad topical prompts 到完整论文生成并提交 peer review。
- 对比基线：v1 对比和人类 workshop acceptance threshold。
- 评价指标：review scores、acceptance threshold、内部质量分析。
- 关键结果：一篇平均 6.33/10，超过 workshop 平均接收阈值；reviewers 也指出 caption 错误、实验不足、dataset overlap 等问题。
- 是否有消融实验：系统论文中有内部分析，需复核是否严格消融。
- 是否有失败案例或负结果：明确讨论生成稿存在不准确、实验深度不足和伦理/透明性问题。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：生成机器学习研究假设和 workshop-level 实验论文；科学贡献主要是系统平台与自动科研能力证明。
- 科学贡献是否经过验证：通过正式 workshop peer review 和人类评价。
- 贡献强度判断：中-强，作为自动科研能力里程碑强；作为具体科学发现中等。
- 科学贡献类型：系统平台 / 假设 / 设计 / 计算实验 / 论文写作。
- 证据强度：真实 peer review / benchmark。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：它自动生成研究、代码实验和论文，而不是解决单个科学预测任务。
- 与已有 Agent / 科研智能系统的区别：相较 v1 去除人工模板，使用 agentic tree search 和 VLM feedback。
- 与同一科学领域其他 Agent 文献的关系：可与 AI Scientist-v1、InternAgent、Agent Laboratory、CodeScientist 比较。
- 主要创新点：workshop-level AI-generated paper、tree-search experimentation、peer-review based validation。

## 7. 局限性与风险

- Agent 自主性不足：主题范围和计算环境仍被设定；科学质量仍停留 workshop level。
- 科学验证不足：AI 生成研究中存在不准确、caption 错误、实验广度不足、dataset overlap。
- 泛化性不足：主要在机器学习研究领域验证。
- 工具链依赖：代码环境、LLM、VLM、reviewer prompt 和计算资源。
- 数据泄漏或 benchmark 偏差：ML 代码/数据集可能存在训练语料和公开 benchmark 污染。
- 成本、可复现性或安全风险：自动论文生成的伦理、审稿透明度、低质量论文规模化、研究诚信风险。

## 8. 对综述写作的价值

- 可放入哪个章节：通用科研 Agent；AI scientist 系统；论文写作与同行评议闭环。
- 可支撑哪个论点：Agent 科研自动化已从任务辅助推进到完整论文生成与真实评审测试。
- 可用于哪个表格或图：端到端科研 pipeline；验证方式“真实 peer review”案例。
- 适合作为代表性案例吗：非常适合，但需同时强调局限和伦理风险。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1、Fig. 2、Table 1、Sec. 4、Limitations & Ethical Considerations。
- 需要与哪些论文并列比较：AI Scientist-v1、InternAgent、Agent Laboratory、ResearchAgent。

## 9. 总结

### 9.1 一句话概括

树搜索驱动的端到端 AI 科学家。

### 9.2 速记版 pipeline

1. 生成研究想法。
2. 树搜索规划和运行代码实验。
3. VLM 检查图表和结果。
4. 写成完整论文。
5. AI reviewer/人类审稿反馈质量。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01 形式、信息与计算科学
二级类：01.02 计算机科学 / 人工智能与机器学习研究自动化
三级类：01.02.12 / 01.02.13
四级专题：AI/ML research automation agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：文献检索与阅读; 科学问题提出; 假设生成; 实验设计; 工具调用与代码执行; 实验执行; 数据分析; 结果解释; 证据评估与验证; 论文写作; 端到端科研流程自动化
自主能力：任务分解; 计划生成; 工具调用; 记忆与状态维护; 反馈迭代; 自主决策; 多 Agent 协作; 环境交互; 闭环实验
验证方式：benchmark; 真实 peer review; 专家评估
交叉属性：计算驱动; 数据驱动; 多模态; agentic tree search
科学贡献类型：系统平台; 假设; 设计; 计算实验; 论文写作
证据强度：全文 PDF，高
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
