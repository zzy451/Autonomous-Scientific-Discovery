# Kang and Kim 2023 - ChatMOF

## 2026-06-22 archive sync

- Canonical PDF path: `Reference_PDF/04_Materials_Science/Kang_2023_ChatMOF.pdf`
- First-hand source checked this round: Nature HTML full text + publisher PDF link checked + arXiv abstract
- PDF version: archived publisher PDF
- Source-limited: no
- Final adjudication: `scientific_object_modules=04`; `object_coverage_mode=single_module`; `primary_module_for_filing=04`; `general_method_bucket=none`; `confidence=high`

**论文信息**
- 标题：ChatMOF: an artificial intelligence system for predicting and generating metal-organic frameworks using large language models
- 作者：Yeonghun Kang, Jihan Kim
- 年份：2024（arXiv 预印本为 2023）
- 来源 / venue：Nature Communications 15, 4705 (2024)
- DOI / arXiv / URL：https://doi.org/10.1038/s41467-024-48998-4；https://www.nature.com/articles/s41467-024-48998-4；https://arxiv.org/abs/2308.01423
- PDF / 本地文件路径：`Reference_PDF/04_Materials_Science/Kang_2023_ChatMOF.pdf`
- First-hand source checked：Nature HTML full text；publisher PDF link checked；arXiv abstract
- PDF version：archived publisher PDF
- Source-limited：no
- 论文类型：研究论文 / MOF 材料发现 Agent
- 当前状态：confirmed core；当前落地为 `04`
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| PDF 归档与来源核对 | 已完成 | Nature article page；publisher PDF link；项目本地 PDF | 当前使用项目归档的 publisher PDF，来源描述已从旧的 arXiv-only / no-local-PDF 表述更新 | 高 |
| Agent 纳入 | 是 | Nature HTML Introduction / Methods | ChatMOF 由 agent、toolkit、evaluator 组成，按 objective-driven 多步流程执行 search、prediction、generation | 高 |
| 材料对象覆盖 | `04` | Nature HTML Fig. 1 说明；正文方法与结果 | 直接对象始终是 metal-organic frameworks 的结构、性质、检索与生成 | 高 |
| 方法流程 | 自治材料工作流 | Nature HTML 方法部分 | 系统接收文本目标后进行规划、工具选择、性质预测、合成方法检索与结构生成 | 高 |
| 实验验证 | 计算任务验证 | Nature HTML 结果与 Fig. 6 | search、prediction、generation 三类任务均报告准确率，generation task 也给出性能统计 | 高 |
| `01.04` 存放区判断 | `none` | Nature HTML 全文 | 论文不是通用 scientific-agent shell，而是明确围绕 MOF 材料对象构建与评估 | 高 |

## 0. 摘要翻译

ChatMOF 是一个面向金属有机框架材料的自治 AI 系统。它使用大语言模型作为中心协调器，把用户的自然语言需求转化为 MOF 相关的多步任务，包括材料信息检索、性质预测、合成方法调取以及新结构生成。论文将 ChatMOF 拆成 agent、toolkit 和 evaluator 三个核心部分，并在 search、prediction、generation 三类任务上评估其性能，展示了大模型代理在 MOF 材料设计与发现中的可行性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：存在明确科研目标、多步规划、工具调用、结果观察与 evaluator 反馈。
- 纳入置信度：高。
- 是否面向明确科研目标：是，面向 MOF 对象的材料检索、性质预测与结构生成。
- 是否具有多步行动过程：是。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是。
  - 工具调用：是，toolkit 包含数据库、预测与生成工具。
  - 反馈迭代：是，agent 与 evaluator 形成任务闭环。
  - 自主决策：中高。
  - 多 Agent 协作：否，核心是单 agent 协调多工具。
- 在科研流程中承担的明确角色：材料信息检索、性质预测、结构生成、候选评估。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不适用。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- scientific_object_modules：`04`
- object_coverage_mode：`single_module`
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- general_method_bucket：`none`
- primary_module_for_filing：`04`
- 主展示模块一级类：`04` 材料科学
- 主展示模块二级类：`04.03` 多孔材料 / 功能材料
- 主展示模块三级类：MOF / porous materials design
- 每个模块的对象实验证据：MOF 结构检索、性质预测、结构生成与合成方法调取均直接指向金属有机框架材料对象。
- 归类理由：被搜索、预测、生成和评估的对象始终是 MOF 材料结构与性质；即使系统会调取 synthesis methods，也没有把论文重心转移到一般化学反应路线优化。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：metal-organic frameworks 的结构、性质与生成设计。
- 最终科学问题：如何把自然语言材料需求转化为 MOF 检索、预测与生成工作流。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：GPT-4 / GPT-3.5 只是方法组件，归类应看被直接研究和验证的材料对象。

### 2.3 容易混淆的边界

- 可能误归类到：`03` 化学科学。
- 最终判定：保留 `04`。
- 判定理由：论文核心对象是框架材料结构与材料性质，而不是具体反应路线或分子合成过程。
- 多模块覆盖说明：当前没有足够对象级证据支持增记 `03`；合成方法检索仍服务于 MOF 材料对象。
- `01.04` 判定说明：不成立。
- 是否需要二次复核：否，当前分类已稳定。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Hybrid Agent
- 科研流程角色：materials_design；prediction；knowledge_retrieval；data_analysis
- 自主能力：planning；tool_use；feedback_iteration；autonomous_decision_making

## 4. 方法设计

1. 接收自然语言形式的 MOF 需求或问题。
2. Agent 解析目标并规划后续步骤。
3. 调用 toolkit 完成检索、性质预测、结构生成或合成方法调用。
4. evaluator 检查结果并向 agent 返回反馈。
5. 输出满足条件的材料信息或候选 MOF 结构。

## 5. 实验与验证

- 验证方式：benchmark；simulation_validation
- 数据、任务与指标：search、prediction、generation 三类 MOF 任务
- 关键结果：search 与 prediction 准确率较高，generation task 也给出可观表现
- 科学贡献类型：design；prediction；system_platform
- 证据强度：first_hand_full_text

## 6. 与已有工作的关系

- 与普通 MOF 预测模型不同：这里强调 agent 组织下的“检索-预测-生成-评估”工作流。
- 与 self-driving lab 材料系统不同：该文主要是计算 / 信息工作流而非机器人实验平台。
- 与同域材料 Agent 的关系：可作为 MOF / porous materials 方向的代表材料 Agent 样本。

## 7. 局限性与风险

- 科学验证仍以计算任务为主，缺少真实实验闭环。
- 系统性能受底层大模型与数据库质量影响明显。
- 当前主要风险在 discovery strength，而不是模块误判。

## 8. 对综述写作的价值

- 可放入哪个章节：MOF / porous materials agents。
- 可支撑哪个论点：材料对象明确时，即便系统外观上像通用聊天代理，也应保留在 `04`。
- 推荐引用强度：standard。

## 9. 总结

### 9.1 一句话概括

ChatMOF 是一个围绕 MOF 材料对象执行检索、预测与生成的稳定 `04` 材料 Agent。

### 9.2 速记版 pipeline

1. 接收 MOF 相关自然语言目标。
2. Agent 规划任务。
3. 调用 toolkit 检索、预测或生成。
4. evaluator 反馈检查。
5. 输出材料答案或候选结构。

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：04
object_coverage_mode：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
primary_module_for_filing：04
是否进入 01.04 存放区：否
module_assignment_evidence：MOF structure/property retrieval, prediction, generation, synthesis-method retrieval
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：knowledge_retrieval; materials_design; prediction; data_analysis
验证方式：benchmark; simulation_validation
科学贡献类型：design; prediction; system_platform
证据强度：first_hand_full_text
归类置信度：high
纳入置信度：high
推荐引用强度：standard
```
