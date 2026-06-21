# Ghafarollahi and Buehler 2025 - SciAgents

**论文信息**
- 标题：SciAgents: Automating Scientific Discovery Through Bioinspired Multi-Agent Intelligent Graph Reasoning
- 作者：Alireza Ghafarollahi, Markus J. Buehler
- 年份：2025
- 来源 / venue：Advanced Materials
- DOI / URL：https://doi.org/10.1002/adma.202413523；arXiv: https://arxiv.org/abs/2409.05556
- 当前状态：to_read；core priority；2026-06-21 完成 `04 / 06` 边界复核，当前不支持新增 `06`

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract `2409.05556` | multi-agent intelligent graph reasoning; autonomous hypothesis generation; in-situ learning capabilities | 高 |
| 科学对象归类 | `04` 材料科学 | arXiv abstract `2409.05556` | applied to biologically inspired materials; yields material discoveries, design principles, and unexpected material properties | 高 |
| `06` 边界复核 | 不接受 `06` | arXiv abstract `2409.05556`; DOI landing path `10.1002/adma.202413523` | “biologically inspired” 描述的是材料灵感和 biomaterial object family，而不是独立生命科学机制实验；当前可见 case 仍是 advanced materials discovery | 中到高 |
| 方法机制 | 知识图谱 + LLM + 多 Agent | arXiv abstract `2409.05556` | ontological knowledge graphs, LLM suite, data retrieval tools, multi-agent systems | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- Agent 行动闭环：多 Agent 协作、知识图谱推理、假设生成与 refinement。
- 纳入置信度：高。

## 2. 科学领域归类

- 一级类：`04` 材料科学
- 二级类：`04.04` 材料发现
- 四级专题：multi-agent graph reasoning for materials discovery
- 归类理由：原文摘要明确写作 “Applied to biologically inspired materials” 并将输出表述为 material discoveries、design principles 和 unexpected material properties，因此稳定对象是材料发现而不是独立生命科学研究。

### 2.1 边界说明：为何不加 `06`

- 可能误归类到：`06` 生命科学。
- 当前判定：不新增 `06`，维持单模块 `04`。
- 判定理由：现有一手证据只支持 biomaterial / bioinspired material discovery；生物学词汇在这里充当材料组成、自然启发来源或跨学科语义桥梁，而不是单独的细胞、蛋白质、疾病机制或生命过程实验。
- 后续条件：若拿到全文后发现论文报告了独立的蛋白质、细胞、组织或其他生命对象实验 / case study，再重新打开 `04 / 06` 边界。

## 3. Agent 系统与科研流程角色

- Agent 类型：Multi-Agent System；Retrieval-augmented Agent；Hybrid Agent。
- 科研流程角色：知识组织、假设生成、结果解释、证据评估。
- 交叉属性：知识图谱、多 Agent、多模态/多源知识整合。

## 4. 方法设计

初步 pipeline：

1. 构建或调用材料/科学概念知识图谱。
2. 多 Agent 读取并检索相关知识。
3. 通过图推理发现跨领域关系。
4. 生成并批判性改进研究假设。
5. 输出材料发现方向或机制解释。

## 5. 实验与验证

- 验证方式：案例研究与假设生成；当前可见一手证据强调材料发现案例，而非独立生命科学验证。
- 科学贡献类型：hypothesis；explanation；system_platform。
- 证据强度：first-hand abstract / DOI-landing level；全文仍值得后续补读，但当前边界判断已足够支持 `04` 单模块保留。

## 6. 对综述写作的价值

- 推荐引用强度：core。
- 可作为材料科学中“多 Agent + 知识图谱 + 假设生成”的代表性案例。
- 需要与 AtomAgents / alloy design PNAS 论文区分。

## 7. 后续精读任务

- 提取 Agent 角色分工。
- 判断是否产生经验证的新材料发现。
- 记录图谱来源、工具和评价方式。
- 如后续拿到 Wiley 全文，优先复核 case-study 列表是否真的出现独立生命科学对象实验。
