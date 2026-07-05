# Estlin et al. 2014 - Automated Targeting for the MSL Rover ChemCam Spectrometer

**论文信息**
- 标题：Automated Targeting for the MSL Rover ChemCam Spectrometer
- 作者：Tara Estlin; Gary Doran; Benjamin Bornstein; Reena Francis; Daniel Gaines; Michael Burl; S. Johnstone; Vijesh Verma
- 年份：2014
- 来源 / venue：i-SAIRAS 2014
- DOI / arXiv / URL：https://ai.jpl.nasa.gov/public/documents/papers/estlin-isairas2014-automated.pdf
- PDF / 本地文件路径：当前笔记基于官方 PDF（https://ai.jpl.nasa.gov/public/documents/papers/estlin-isairas2014-automated.pdf）；未见本地归档 PDF
- 论文类型：系统论文 / rover instrument-targeting autonomy
- 当前状态：已读 / 已纳入；2026-07-05 note-harmonization override completed
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Phase6NoteRevisionR26 harmonization override - 2026-07-05

- Final classification: `scientific_object_modules=05;10`; `object_coverage_mode=multi_module`; `primary_module_for_filing=10`; `general_method_bucket=none`.
- Source status: official JPL PDF checked at `https://ai.jpl.nasa.gov/public/documents/papers/estlin-isairas2014-automated.pdf`; no local archive path is currently confirmed in the workspace; authoritative note state remains `source_limited=no`.
- Override note: this note is already read and included in the confirmed core. Older `to_read` or single-module shorthand below should be treated as stale legacy text superseded by the frozen `05;10` reading.

## Evidence Log

## 2026-06-20 relaxed multi-module revision

```text
scientific_object_modules: 05;10
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 10
first_hand_sources_checked: JPL PDF; JPL AEGIS project page
classification_evidence_source_level: first_hand_full_text
module_assignment_evidence: `05` is supported by Mars rocks, soil, geological targets, and ChemCam geochemical surveying; `10` is supported by rover / ChemCam autonomous targeting and mission-science operations.
multi_module_object_coverage_note: The old 10-only boundary treated geology as mission input; the relaxed rule counts the geological / geochemical targets themselves as `05` object coverage.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official PDF abstract | onboard 图像分析、候选目标检测、follow-up targeting | 高 |
| 科学对象归类 | `05;10` | abstract / official PDF | 论文同时覆盖 Mars rocks、soil、geologic / geochemical targets，以及 rover autonomous targeting / ChemCam mission-science workflow | 高 |
| 方法流程 | 多步闭环 | abstract | image analysis -> candidate detection -> target selection -> ChemCam follow-up | 高 |
| 实验验证 | 任务级场景 | official PDF | 面向 MSL Curiosity ChemCam mission workflow | 高 |
| 边界判断 | `10` 为 filing-primary，并补记 `05` | object-first reading | rover / ChemCam targeting autonomy 仍是 filing 主线，但 geological / geochemical targets 已构成独立 `05` 对象覆盖 | 高 |

## 0. 摘要翻译

本文介绍 AEGIS 在 MSL Curiosity 的 ChemCam 仪器上的自动选靶能力。系统在车载图像中检测科学特征，依据科学家设定的目标选择后续测量目标，并在无需等待地面通信的情况下为 ChemCam 生成自动 follow-up observation。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：明确科研目标、多步感知-筛选-执行流程、真实任务集成
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：图像分析、目标排序、仪器 follow-up 选择

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：10
- 二级类：10.02
- 三级类：rover autonomous instrument targeting
- 四级专题：rover ChemCam autonomous targeting agents
- 四级专题是否为新增：否
- 归类理由：稳定对象既包括 rover mission-science autonomy，也包括被识别和测量的 Mars geological / geochemical targets；本记录继续以 `10` 为 filing-primary
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：MSL rover mission-science targeting loop，以及由 ChemCam 跟进的 Mars geological / geochemical targets
- 最终科学问题：漫游车如何机载识别科学目标并自动触发 ChemCam follow-up
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：图像算法只是手段；对象证据同时落在任务闭环中的 autonomous targeting 与 Mars geological / geochemical targets 上

### 2.3 容易混淆的边界

- 可能误归类到：05
- 最终判定：保留 10.02
- 判定理由：rocks and soil 是测量对象，但论文真正研究的是 targeting autonomy
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：rover targeting agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：中
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：中
- 反馈迭代：部分是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

## 4. 方法设计

- 机载分析 Navcam/RMI 等图像，生成候选目标。
- 依据 scientist-specified objectives 进行排序和筛选。
- 自动驱动 ChemCam 指向与 follow-up measurement。

## 5. 实验与验证

- 验证方式：mission workflow integration
- 关键结果：支持无地面延迟的 onboard target selection
- 证据强度：official PDF strong

## 6. 与已有工作的关系

- 属于 OASIS -> AEGIS -> SuperCam 的 rover science autonomy 谱系。
- 相比泛化行星科学论文，更像任务级 instrument-targeting 系统论文。

## 7. 局限性与风险

- 当前笔记未展开定量表现细节。
- 主类风险很低，主要剩余任务是谱系和 deployment 细节补充。

## 8. 对综述写作的价值

- 可作为 `10.02` 中 ChemCam / rover targeting 子脉络的中间节点。
- 有助于支撑 `05 / 10` 边界中的 mission-autonomy 判断。

## 9. 总结

该文稳定归入 `10.02`：它研究的是 rover autonomous targeting，而不是地质测量对象本身。
