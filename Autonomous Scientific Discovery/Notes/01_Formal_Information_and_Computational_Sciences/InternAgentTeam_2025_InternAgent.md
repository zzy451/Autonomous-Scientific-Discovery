# InternAgent Team 2025 - InternAgent

**论文信息**
- 标题：InternAgent: When Agent Becomes the Scientist - Building Closed-loop System from Hypothesis to Verification
- 作者：InternAgent Team, Shanghai Artificial Intelligence Laboratory
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2505.16938
- PDF / 本地文件路径：临时阅读 PDF：`%TEMP%/asd_note_sources/ASD-0004_NovelSeek.pdf`
- 论文类型：系统论文 / general scientific research-agent system
- 当前状态：已读 / 已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

## 2026-06-20 relaxed round-2 multi-module revision

- Round decision: update the relaxed overlay from independent `01.04` to `scientific_object_modules=01;03;06;09;10`.
- Source checked in this round: arXiv abstract page and ar5iv HTML for `2505.16938`.
- Reason: the paper reports 12 concrete task evaluations rather than only an object-free workflow demo. These include AI/CV/NLP/geometric-VLM tasks (`01`), reaction yield prediction and molecular dynamics (`03`), transcription perturbation and enhancer activity prediction (`06`), power-flow / transformer-temperature engineering data (`09`), and autonomous-driving point-cloud detection (`10`).
- Current filing note: legacy `Main class` / `Secondary class` remain unchanged until schema migration, but the old note wording that treats this as `01.04` only is superseded for relaxed-counting purposes.
- general_method_bucket: `none`; `primary_module_for_filing=01`; `object_coverage_mode=multi_module`.

证据级别：full-text（arXiv PDF 已读取并抽取文本）。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 纳入；统一闭环多 Agent 科研框架 | Abstract; Sec. 1-2; Fig. 1-2 | 系统覆盖想法生成、方法构建、实验执行、结果反馈、人机交互和多 Agent 协作 | 高 |
| 科学对象归类 | 01.04 通用科研 Agent | 主清单；Abstract; Fig. 1 | 论文强调 12 类科学研究任务和通用 ASR 框架，主要验证通用科研流程能力 | 中-高 |
| 方法流程 | hypothesis 到 verification 的闭环 | Sec. 2; extracted lines 121-129, 245-252 | 从 proposal/idea 到 methodology、code implementation、多轮实验规划和执行 | 高 |
| 实验验证 | 多个 AI/计算机视觉/自动驾驶等任务 + 人类研究 | Sec. 1; Sec. 3+ | 论文称在 12 个科学研究任务中验证，并邀请专家评估 idea novelty 与研究效率 | 中 |
| 科学贡献 | 通用端到端科研 Agent 框架 | Contributions | 可作为通用科研 Agent 自动化从假设到实验验证的案例 | 高 |

## 0. 摘要翻译

论文提出 InternAgent，一个统一闭环多 Agent 科研框架，目标是让 Agent 从“研究辅助”进一步承担科学家式工作。系统覆盖自进化 idea generation、idea-to-methodology construction、多轮实验规划与执行、结果反馈和人类专家交互。论文在多类 AI/计算机视觉相关研究任务中验证，展示其可自动生成研究想法、代码、实验和报告，并通过专家评估研究想法的新颖性和系统效率。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：多 Agent 框架、任务分工、自动实验执行、反馈和人类交互明确。
- 判定置信度：高。
- 是否面向明确科研目标：是，自动科学研究/自动化科研任务。
- 是否具有多步行动过程：是。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是。
  - 工具调用：是，代码生成与实验执行。
  - 反馈迭代：是，closed-loop feedback。
  - 自主决策：部分具备。
  - 多 Agent 协作：是。
- 在科研流程中承担的明确角色：假设/想法生成、方法构建、代码实现、实验执行、反馈评估、报告整理。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，重点是通用科研 Agent 框架。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：01 形式、信息与计算科学。
- 二级类：01.04 科研智能系统与 Autonomous Scientific Discovery。
- 三级类：通用科研 Agent 系统。
- 四级专题：General scientific research-agent systems。
- 四级专题是否为新增：否。
- 归类理由：主清单归 01；论文对象是通用科研自动化系统而非某一自然科学对象。
- 归类置信度：中-高。

### 2.2 对象优先判定

- 最终科学研究对象：科研流程与通用自动科研系统。
- 最终科学问题：Agent 能否从研究想法到实验验证执行端到端科研。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：不是因为 LLM 或多 Agent 归 01，而是因为研究对象本身是通用科研自动化能力。

### 2.3 容易混淆的边界

- 可能误归类到：特定 AI/计算机视觉任务子领域；主清单标题还写作 NovelSeek。
- 最终判定：01.04。
- 判定理由：系统目标和贡献是通用 closed-loop ASR framework；验证任务多样且偏 AI 实验。
- 是否需要二次复核：是。主清单元数据中 “NovelSeek” 与 arXiv PDF 实际 “InternAgent” 不一致，需要人工复核并决定是否改清单。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：可能有文献检索，证据中等。
- Multi-Agent System：是。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：是。
- Hybrid Agent：是。
- 其他：closed-loop AI research agent。

### 3.2 科研流程角色

- 文献检索与阅读：是。
- 知识抽取与组织：是。
- 科学问题提出：是。
- 假设生成：是。
- 实验设计：是。
- 仿真建模：部分，视任务而定。
- 工具调用与代码执行：是。
- 实验执行：是，主要为计算实验。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：是。
- 论文写作：报告生成/文档生成相关。
- 端到端科研流程自动化：是。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：项目/代码结构理解与进度追踪，证据中等。
- 反馈迭代：是。
- 自主决策：中等。
- 多 Agent 协作：是。
- 环境交互：代码库和实验环境。
- 闭环实验：是，计算实验闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：计算实验驱动。
- 仿真驱动：部分。
- 多模态：验证任务中可能涉及视觉，非核心标签。
- 多尺度建模：否。
- 高通量筛选：否。
- 知识图谱：否。
- 数字孪生：否。
- 机器人平台：否。
- 其他：AI research automation。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：现有自动科研系统难以从 idea 到实验验证形成可扩展闭环。
- 现有科研流程或方法的痛点：需要跨文献理解、方法设计、代码实现、实验执行和结果反馈的连续协作。
- 核心假设或直觉：将专门 Agent 组织成闭环团队并加入人类专家交互，可提升自动科研任务完成度。

### 4.2 系统流程

1. 输入：粗略研究方向、proposal 或任务目标。
2. 任务分解 / 规划：系统拆解 idea generation、methodology construction、实验模块和评估。
3. 工具、数据库、模型或实验平台调用：检索文献、分析代码库、生成/修改代码、运行实验。
4. 中间结果反馈：实验结果、专家反馈和其他 Agent 评价回流。
5. 决策或迭代：多轮实验规划与执行，修正方法模块。
6. 输出：研究想法、方法、代码、实验结果和报告。

### 4.3 系统组件

- Agent 核心：Idea Innovation Agent、Assessment Agent、代码/项目理解相关 Agent、实验规划执行 Agent 等。
- 工具 / API / 数据库：文献检索、GitHub/代码库、Python AST/static analysis、实验运行环境。
- 记忆或状态模块：项目结构、实验进展和反馈记录。
- 规划器：多 Agent 协同规划。
- 评估器 / verifier：Assessment Agent、专家评价、实验结果。
- 人类反馈或专家介入：有。
- 实验平台或仿真环境：计算实验环境。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：多任务系统评估，是否标准 benchmark 需复核。
- 仿真验证：部分计算实验。
- 高通量计算：否。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：是。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：12 个科学研究任务，示例包括 AI for Science、图像分割、3D 自动驾驶、大型视觉语言模型微调等。
- 任务设置：从 idea 到方法和代码实现，再到实验验证。
- 对比基线：人类研究效率/专家评分及任务基线代码，需全文表格复核。
- 评价指标：任务性能提升、idea novelty 专家评分、研究效率。
- 关键结果：论文称在多个任务中取得性能增益，并开源 baseline 与 Agent 生成代码。
- 是否有消融实验：需复核。
- 是否有失败案例或负结果：需复核详细失败分析。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献是通用科研 Agent 系统和自动生成的 AI/计算实验结果。
- 科学贡献是否经过验证：通过多任务实验和专家评估，强度中等。
- 贡献强度判断：中。
- 科学贡献类型：系统平台 / 假设 / 设计 / 计算实验。
- 证据强度：计算 benchmark / 专家评估。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不解决单一科学预测任务，而组织多 Agent 完成从想法到验证的科研流程。
- 与已有 Agent / 科研智能系统的区别：强调 closed-loop、human-interactive feedback 和多任务可扩展性。
- 与同一科学领域其他 Agent 文献的关系：可与 AI Scientist、AI Scientist-v2、Agent Laboratory、CodeScientist 并列。
- 主要创新点：统一闭环多 Agent 科研框架和多任务验证。

## 7. 局限性与风险

- Agent 自主性不足：仍依赖人类专家反馈，且验证多在计算任务。
- 科学验证不足：缺少自然科学湿实验或真实实验室发现。
- 泛化性不足：验证任务偏 AI/计算机视觉，能否泛化到化学/生命/医学需复核。
- 工具链依赖：高度依赖代码库、实验环境和 LLM 能力。
- 数据泄漏或 benchmark 偏差：AI 任务可能受公开代码/论文污染影响。
- 成本、可复现性或安全风险：自动代码修改和实验执行存在错误传播风险。

## 8. 对综述写作的价值

- 可放入哪个章节：通用科研 Agent；端到端科研自动化。
- 可支撑哪个论点：科研 Agent 可覆盖 hypothesis-method-experiment-feedback 的完整链条。
- 可用于哪个表格或图：通用科研 Agent pipeline 图；自动化程度对比。
- 适合作为代表性案例吗：适合，但需注明元数据复核。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1、Fig. 2、12 tasks 描述、human study。
- 需要与哪些论文并列比较：AI Scientist-v1/v2、Agent Laboratory、ResearchAgent、CodeScientist。

## 9. 总结

### 9.1 一句话概括

从假设到验证的通用闭环科研 Agent。

### 9.2 速记版 pipeline

1. 输入研究主题或初始想法。
2. 多 Agent 生成和评估 idea。
3. 构建方法并理解代码。
4. 自动写代码和运行实验。
5. 基于结果和专家反馈迭代。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01 形式、信息与计算科学
二级类：01.04
三级类：科研智能系统与 ASD
四级专题：General scientific research-agent systems
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：文献检索与阅读; 科学问题提出; 假设生成; 实验设计; 工具调用与代码执行; 实验执行; 数据分析; 论文写作; 端到端科研流程自动化
自主能力：任务分解; 计划生成; 工具调用; 反馈迭代; 自主决策; 多 Agent 协作; 闭环实验
验证方式：benchmark; 计算实验; 专家评估
交叉属性：计算驱动; 数据驱动
科学贡献类型：系统平台; 假设; 设计; 计算实验
证据强度：全文 PDF，高；分类置信度中-高
归类置信度：中-高
纳入置信度：高
推荐引用强度：核心引用
```
