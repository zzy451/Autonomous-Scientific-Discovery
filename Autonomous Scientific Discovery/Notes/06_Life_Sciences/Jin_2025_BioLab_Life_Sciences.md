# Jin et al. 2025 - BioLab: End-to-End Autonomous Life Sciences Research with Multi-Agents System Integrating Biological Foundation Models

## 2026-06-24 confirmed-core full reaudit revision

```text
paper_id: ASD-0745
final_agent_inclusion: yes
supported_modules: 06;07
primary_module_for_filing: 06
source_limited: yes
safety_access_status: preprint-access-block-403-crossref-abstract-only
first_hand_sources_checked: Crossref DOI metadata / abstract for 10.1101/2025.09.03.674085
pdf_archive_status: no local PDF archived; bioRxiv landing/PDF returned 403 in this environment
adjudication_note: abstract-level first-hand evidence supports autonomous life-science research with experimentally validated antibody optimization; land as 06 primary with 07 secondary, not 01.04
```

**论文信息**
- 标题：BioLab: End-to-End Autonomous Life Sciences Research with Multi-Agents System Integrating Biological Foundation Models
- 作者：Ruofan Jin; Yucheng Guo; Yuanhao Qu; Ming Yang; Chun Shang; Qirong Yang; Linlin Chao; Yi Zhou; Ruilai Xu; Ziyao Xu; Ruhong Zhou; Zaixi Zhang; Mengdi Wang; Xiaoming Zhang; Le Cong
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / URL：https://doi.org/10.1101/2025.09.03.674085
- PDF / 本地文件路径：本地未归档 PDF；bioRxiv landing/PDF 在本轮环境下返回 `403`
- first-hand source checked：Crossref DOI metadata / abstract
- 论文类型：研究论文 / end-to-end life-science multi-agent system
- 当前状态：confirmed-core full reaudit landed；`source_limited = yes`
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| first-hand source checked | Crossref abstract only | Crossref DOI metadata | 当前一手证据来自 DOI abstract / metadata，而非 preprint full text | 高 |
| access / source status | `source_limited = yes` | Crossref; controller adjudication | bioRxiv landing/PDF 在本环境 `403`，无本地 PDF | 高 |
| Agent 纳入 | `yes` | Crossref abstract | `BioLab` 被明确写成 end-to-end biological research 的 multi-agent system | 高 |
| 科学对象归类 | `06;07`，其中 `06` 为 primary | Crossref abstract | 06 由 DNA/RNA/protein/cell/chemical life-science tasks 支撑；07 由 macrophage-targeting antibody design、PD-1 / pembrolizumab optimization、IC50 assays 与功能验证支撑 | 高 |
| 边界判断 | 不应回流到 `01.04` | object-first adjudication | 广覆盖平台感不等于领域无关；对象与验证都落在生命科学/生物医学内部 | 高 |
| 实验验证 | computational-to-experimental closed loop | Crossref abstract | 从 target mining 到 multi-objective antibody optimization，再到 IC50 与 functional assays 验证 | 高 |

## 0. 摘要翻译

`BioLab` 是一个面向生命科学研究的端到端 multi-agent system。Crossref 摘要显示，它整合了八个协作 agents、retrieval-augmented memory 以及覆盖 DNA、RNA、protein、cell 和 chemical 五个生物尺度的 219 个 xBio-Tools。除标准推理 benchmark 外，它还自主完成了 de novo macrophage-targeting antibody design，并把 computational pipeline 接到了实验验证上。因此本轮不再把它写成 `01.04` 边界漂移样本，而是稳定为 `06;07`，其中 06 为 primary、07 为 secondary。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 协作、规划、推理、批评/修正、工具调用与闭环验证
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 在科研流程中承担的明确角色：目标挖掘、研究规划、工具调度、优化、实验验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- primary module：06
- secondary supported module：07
- 二级类：06.03（primary filing context）
- 三级类：end-to-end life-science discovery workflow with therapeutic-antibody coverage
- 归类理由：系统主轴仍是生命科学研究自动化，但 abstract 已给出 concrete biomedical antibody optimization 与实验验证，因此 07 需要保留
- 归类置信度：中高（source-limited but concrete）

### 2.2 对象优先判定

- 06 侧对象：DNA/RNA/protein/cell/chemical-scale life-science tasks
- 07 侧对象：macrophage-targeting antibody design；PD-1 / pembrolizumab optimization；IC50 与 functional assays
- 为什么不是 `01.04`：存在 concrete biological / biomedical objects、专门工具链和对象级实验验证

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 `06;07`，其中 `06` 为 primary
- 判定理由：平台感很强，但对象与验证不是领域无关方法学

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Hybrid Agent：是
- 其他：biological foundation-model orchestration system

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：是
- 假设生成：是
- 实验设计：是
- 工具调用与代码执行：是
- 数据分析：是
- 证据评估与验证：是
- 端到端科研流程自动化：是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该系统：把分散的生命科学工具、foundation models 和验证流程接成端到端研究系统
- 现有流程痛点：多尺度任务切换成本高，in silico prediction 与 wet-lab validation 脱节
- 核心方法：八个协作 agents + Memory Agent + 219 个 xBio-Tools + 多种生物基础模型

### 4.2 系统流程

1. 接收 life-science research task
2. Planner / Reasoner / Critic / Memory 等 agents 协作分解任务
3. 调用跨五个 biological scales 的 xBio-Tools
4. 在中间结果上持续检错、保留状态并迭代优化
5. 对 antibody case 从 target mining 推进到 multi-objective optimization
6. 将 computational design 接到 experimental validation

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- computational validation：是
- 湿实验：是
- 闭环实验验证：是

### 5.2 数据、任务与指标

- life-science coverage：DNA / RNA / protein / cell / chemical scales
- biomedical coverage：macrophage-targeting antibody design；PD-1 / pembrolizumab optimization
- 关键结果：Pem-MOO-1 与 Pem-MOO-2 的 IC50 为 0.01-0.016 nM，优于 parental pembrolizumab 的 0.027 nM；functional assays 支持 improved pathway blockade

### 5.3 科学贡献

- 科学贡献类型：system_platform; life_science_discovery; therapeutic_antibody_optimization
- 贡献强度判断：中高
- 证据强度：crossref_abstract_only_but_concrete_multi_module

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 biological model，而是端到端多 Agent 科研系统
- 与纯 life-science 平台样本的区别：本轮需要把 concrete biomedical antibody evidence 写进 07，而不是只停在 06 或退回 01.04
- 与边界样本的关系：它说明“广覆盖平台”也可以因 concrete object validation 稳定获得多模块支持

## 7. 局限性与风险

- source-limited：当前只有 Crossref 摘要级一手证据
- access 限制：bioRxiv landing/PDF 在本环境 `403`，无本地 PDF
- 全文细节待补：多尺度任务是否都达到 antibody case 同等深度仍待后续全文核对
- 表述风险：虽然 abstract 已足以支撑 `06;07`，但不应把每个 biological scale 的实验深度写得超过现有证据

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学主章节，同时在 07 医学生物对象覆盖处并列提及
- 可支撑哪个论点：广覆盖 multi-agent 平台只要具备 concrete object experiments 与 biomedical validation，就不应回流 `01.04`
- 适合作为代表性案例吗：是，但需保留 `source_limited = yes`
- 推荐引用强度：核心引用，并注明基于 Crossref abstract-level first-hand evidence

## 9. 总结

### 9.1 一句话概括

`BioLab` 是一个端到端生命科学 multi-agent system，现有一手摘要级证据已经足以把它稳住为 `06;07`，其中 06 为 primary、07 为 secondary，而不是 `01.04`。

### 9.2 标注字段汇总

```text
是否纳入：yes
supported_modules：06;07
primary_module_for_filing：06
二级类：06.03
三级类：end-to-end life-science discovery workflow with therapeutic-antibody coverage
source_limited：yes
safety_access_status：preprint-access-block-403-crossref-abstract-only
first_hand_sources_checked：Crossref DOI metadata / abstract only
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：hypothesis_generation; workflow_orchestration; tool_use_and_code_execution; evidence_assessment_and_validation
验证方式：benchmark; computational_validation; wet_lab_validation
科学贡献类型：system_platform; life_science_discovery; therapeutic_antibody_optimization
证据强度：crossref_abstract_only_but_concrete_multi_module
纳入置信度：high_source_limited
推荐引用强度：core_with_source_limit_note
```
