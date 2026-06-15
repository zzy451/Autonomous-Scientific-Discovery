# Yuan et al. 2025 - Dolphin: Moving Towards Closed-loop Auto-research through Thinking, Practice, and Feedback

**论文信息**
- 标题：DOLPHIN: Moving Towards Closed-loop Auto-research through Thinking, Practice, and Feedback
- 作者：Jiakang Yuan, Xiangchao Yan, Shiyang Feng, Bo Zhang, Tao Chen, Botian Shi, Wanli Ouyang, Yu Qiao, Lei Bai, Bowen Zhou
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2501.03916
- PDF / 本地文件路径：arXiv PDF；本次临时读取全文 PDF 文本
- 证据级别：full-text
- 论文类型：系统论文
- 当前状态：已读 / 已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 纳入 | Abstract；Fig. 2；Sec. 3 | Dolphin 是 closed-loop auto-research framework，覆盖 idea generation、experimental verification、results feedback | 高 |
| 科学对象归类 | `01.04` 通用科研智能系统 | Abstract；Sec. 4 | 验证在 ModelNet40、CIFAR-100、SST-2、MLE-bench 等通用 ML/AI 任务上，主贡献是自动科研框架 | 高 |
| 方法流程 | paper ranking + idea refinement + code generation/debugging + feedback | Fig. 2-3；Sec. 3 | 基于相关论文和上轮实验反馈生成 idea，用 traceback-guided local code structure 调试，分析实验结果回馈下一轮 | 高 |
| 实验验证 | 多 benchmark 代码实验 | Sec. 4；Tables 1-2, 7 | 在 3D classification、image classification、sentiment classification 和 MLE-bench 任务上自动生成并验证方法 | 高 |
| 科学贡献 | 闭环自动科研系统 | Abstract；Further analyses | 强调实验结果反馈可减少无效 idea 并提升后续 idea 质量 | 高 |

## 0. 摘要翻译

Dolphin 是一个闭环 LLM 驱动自动科研框架。系统先根据 topic/task attributes 排序相关论文，并结合前一轮实验反馈生成新 idea；随后用代码模板实现 idea，并通过 exception-traceback-guided local code structure 进行调试；最后自动分析实验结果，把成功或失败反馈给下一轮 idea generation。实验在 ModelNet40、CIFAR-100、SST-2 和 MLE-bench 子任务上进行，显示系统能持续改进性能，并在部分任务上提出接近或超过人类设计方法的实现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：Dolphin 具有闭环 research cycle，能检索/排序论文、生成 idea、写代码、调试、运行实验、分析结果并反馈。
- 判定置信度：高。
- 是否面向明确科研目标：是，自动生成和验证 ML/AI research ideas。
- 是否具有多步行动过程：是。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：有，生成实验计划和代码修改。
  - 工具调用：有，代码执行、训练脚本、debugging。
  - 反馈迭代：强，实验结果反馈下一轮。
  - 自主决策：有，筛选 idea、分析 improve/keep/decline。
  - 多 Agent 协作：未作为核心。
- 在科研流程中承担的明确角色：文献筛选者、idea 生成者、代码实验执行者、结果分析者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否，闭环是核心贡献。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`01` 形式、信息与计算科学
- 二级类：`01.04` 科研智能系统与 Autonomous Scientific Discovery
- 三级类：通用自动科研系统 / ML research automation
- 四级专题：General scientific research-agent systems
- 四级专题是否为新增：否
- 归类理由：尽管实验任务是 AI/ML benchmark，论文主要贡献是领域相对通用的 closed-loop auto-research framework。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：自动科研流程、机器学习方法 idea 和代码实验。
- 最终科学问题：LLM Agent 能否在实验反馈闭环中自动改进研究 idea。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：主对象是自动科研系统能力，而非具体模型结构本身。

### 2.3 容易混淆的边界

- 可能误归类到：AI algorithm / ML benchmark。
- 最终判定：`01.04`。
- 判定理由：项目政策中通用科研工作流和 benchmark 归 `01.04`。
- 是否需要二次复核：否。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，paper ranking / retrieval。
- Multi-Agent System：否。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：弱，主要自动。
- Hybrid Agent：是。
- 其他：code-experiment auto-research Agent。

### 3.2 科研流程角色

- 文献检索与阅读：核心。
- 知识抽取与组织：paper ranking / task attributes。
- 科学问题提出：topic 给定，idea 自动生成。
- 假设生成：核心。
- 实验设计：核心。
- 仿真建模：否。
- 工具调用与代码执行：核心。
- 实验执行：代码训练/评估。
- 数据分析：核心。
- 结果解释：有。
- 证据评估与验证：通过 benchmark performance。
- 论文写作：否。
- 端到端科研流程自动化：覆盖 idea-实验-反馈。

### 3.3 自主能力

- 任务分解：有。
- 计划生成：有。
- 工具调用：有。
- 记忆与状态维护：有，feedback memory。
- 反馈迭代：强。
- 自主决策：中到强。
- 多 Agent 协作：无。
- 环境交互：代码环境。
- 闭环实验：强，代码实验闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：benchmark data。
- 实验驱动：代码实验。
- 仿真驱动：否。
- 多模态：图像/3D/文本任务，系统层面多任务。
- 多尺度建模：否。
- 高通量筛选：多 idea / 多 loop。
- 知识图谱：否。
- 数字孪生：否。
- 机器人平台：否。
- 其他：autoML-like research automation。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：已有自动科研工作多缺少实验结果到 idea 生成的反馈闭环，或只用简单/自构数据验证。
- 现有科研流程或方法的痛点：idea 新颖性评价不等于实验有效性；代码生成常因错误失败；人工研究依赖实验反馈迭代。
- 核心假设或直觉：把真实 benchmark 实验结果回馈给 LLM idea generation，可以提升后续 idea 质量和研究效率。

### 4.2 系统流程

1. 输入：研究 topic / task，如 3D classification。
2. 任务分解 / 规划：根据 topic 和 task attributes 检索并排序论文，生成非冗余 idea。
3. 工具、数据库、模型或实验平台调用：代码模板、训练脚本、benchmark 数据、LLM 调试。
4. 中间结果反馈：traceback-guided debugging 提取错误函数、行号和局部代码结构。
5. 决策或迭代：分析实验结果，将 idea 标记为 improve/keep/decline 并存入 memory。
6. 输出：改进后的代码方法、实验结果、下一轮 idea prompt。

### 4.3 系统组件

- Agent 核心：LLM-driven idea generation / debugging / result feedback。
- 工具 / API / 数据库：paper retrieval/ranking、PyTorch codebase、benchmark datasets、AIDE integration。
- 记忆或状态模块：feedback memory。
- 规划器：idea generation prompts and experiment plans。
- 评估器 / verifier：benchmark performance evaluation。
- 人类反馈或专家介入：不突出。
- 实验平台或仿真环境：ML training/evaluation code environment。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：ModelNet40、CIFAR-100、SST-2、MLE-bench 子任务。
- 仿真验证：否。
- 高通量计算：多次训练/代码实验。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：无。
- 真实场景部署：否。
- 专家评估：未突出。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：ModelNet40 3D classification、CIFAR-100 image classification、SST-2 sentiment classification、MLE-bench tasks。
- 任务设置：自动生成模型/方法改进 idea 并实现验证。
- 对比基线：PointNet、WideResNet、BERT-base，以及 AIDE 等代码生成 pipeline。
- 评价指标：OA、mAcc、Accuracy、Kaggle/MLE-bench scores、debug success rate。
- 关键结果：ModelNet40 最高达到 93.9% OA；CIFAR-100 和 SST-2 有性能提升；traceback-local code debugging 提高调试成功率。
- 是否有消融实验：有 paper ranking、feedback loop、debugging 输入方式等分析。
- 是否有失败案例或负结果：有，讨论 idea 生成依赖论文信息、project-level code 限制和需人工批判性评估。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要生成 ML 方法 idea 和代码实现；不是自然科学新发现。
- 科学贡献是否经过验证：通过 benchmark 性能验证。
- 贡献强度判断：中到强，作为自动科研系统强；科学发现外推有限。
- 科学贡献类型：系统平台 / 方法设计 / benchmark performance。
- 证据强度：全文 PDF + benchmark，高。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次算法生成，而是有实验反馈闭环的 auto-research。
- 与已有 Agent / 科研智能系统的区别：比只生成 idea 的系统多了实验执行和结果反馈；比 AI Scientist 强调真实公开 benchmark。
- 与同一科学领域其他 Agent 文献的关系：可与 CodeScientist、AI Scientist、ResearchAgent 对比。
- 主要创新点：task-attribute-guided paper ranking、exception-traceback-guided debugging、results feedback loop。

## 7. 局限性与风险

- Agent 自主性不足：仍依赖给定 topic、模板代码和 benchmark。
- 科学验证不足：评估集中在 ML benchmark，不证明跨科学领域有效。
- 泛化性不足：project-level code 和复杂实验环境仍困难。
- 工具链依赖：代码模板、benchmark、LLM、计算资源。
- 数据泄漏或 benchmark 偏差：LLM 可能见过公开 benchmark/SOTA ideas。
- 成本、可复现性或安全风险：自动代码执行和训练成本较高，生成结果需人工核查。

## 8. 对综述写作的价值

- 可放入哪个章节：通用科研 Agent / closed-loop auto-research / code-experiment agents。
- 可支撑哪个论点：实验反馈闭环是从 AI-assisted research 走向 auto-research 的关键。
- 可用于哪个表格或图：闭环 pipeline、debugging/tool-use 能力表。
- 适合作为代表性案例吗：是。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1-3、Tables 1-2、Table 7、Limitations。
- 需要与哪些论文并列比较：CodeScientist、AI Scientist、AI Scientist-v2、ResearchAgent。

## 9. 总结

### 9.1 一句话概括

实验反馈闭环自动科研框架。

### 9.2 速记版 pipeline

1. 按 topic 检索和排序论文。
2. 生成研究 idea。
3. 写代码并用 traceback 调试。
4. 跑 benchmark 实验。
5. 分析结果并反馈下一轮。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01 形式、信息与计算科学
二级类：01.04 科研智能系统与 Autonomous Scientific Discovery
三级类：通用自动科研系统 / ML research automation
四级专题：General scientific research-agent systems
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：文献检索与阅读; 科学问题提出; 假设生成; 实验设计; 工具调用与代码执行; 实验执行; 数据分析; 证据评估与验证; 端到端科研流程自动化
自主能力：任务分解; 计划生成; 工具调用; 记忆与状态维护; 反馈迭代; 自主决策; 环境交互; 闭环实验
验证方式：benchmark; 代码实验; 消融实验
交叉属性：计算驱动; 数据驱动; 高通量筛选; code execution
科学贡献类型：系统平台; 方法设计; benchmark performance
证据强度：全文 PDF，高
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
