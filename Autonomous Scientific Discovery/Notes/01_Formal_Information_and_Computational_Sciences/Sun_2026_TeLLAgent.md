# Sun et al. 2026 - TeLLAgent: a dual-agent framework for reliable scientific discovery with tool-enhanced LLMs

**论文信息**
- 标题：TeLLAgent: a dual-agent framework for reliable scientific discovery with tool-enhanced LLMs
- 作者：Sun et al.
- 年份：2026
- 来源 / venue：Chemical Science
- DOI / arXiv / URL：https://doi.org/10.1039/d5sc09883a
- PDF / 本地文件路径：本轮已核对 RSC DOI 页面 full abstract；官方 OA PDF 可用，但本轮未归档本地 PDF
- 论文类型：系统论文 / Agent 论文
- 当前状态：已读（本轮核对一手来源）；主列表流程状态仍可保持 `to_read`
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | RSC DOI `10.1039/d5sc09883a` full abstract | supervisor-executor dual-agent framework + self-correction loop + 30 tools，满足明确 Agent 工作流 | 高 |
| 科学对象归类 | `03;04`，primary `04` | RSC DOI `10.1039/d5sc09883a` full abstract | 论文不是纯 `01.04` 平台展示；abstract 明确给出 end-to-end organic-solar-cell material discovery，从 molecular design / property prediction 到 synthesis / validation | 高 |
| 方法流程 | 规划-执行-纠错 | RSC DOI `10.1039/d5sc09883a` full abstract | global planning agent 与 local execution agent 形成可迭代科研流程 | 高 |
| 实验验证 | benchmark + synthesis / validation | RSC DOI `10.1039/d5sc09883a` full abstract | 识别出 quasi-macromolecular acceptor，并给出 synthesis 与器件验证结果，PCE 达到 `16.44%` | 高 |
| 边界判断 | 不再维持 `01.04`-only authority；应落地 `03;04` | RSC DOI `10.1039/d5sc09883a` full abstract | concrete molecule / material discovery evidence 已足以推翻旧的 `01.04`-only 写法；primary filing 取 `04` | 高 |

## 0. 摘要翻译

TeLLAgent 是一个由 supervisor 与 executor 构成的双 Agent 科学发现框架，结合 30 个专用工具和 self-correction loop，提高 tool-enhanced LLM scientific discovery 的可靠性。按本轮 RSC full abstract 复核，它不仅有 benchmark，还明确覆盖 organic solar-cell material discovery 的分子设计、性质预测、候选选择、合成与器件验证，因此应更新为 `03;04`，primary `04`，而不是维持 `01.04`-only authority。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：具备规划、执行、工具调用、反馈纠错和明确科研流程角色
- 判定置信度：高

## 2. 科学领域归类

- scientific_object_modules：`03;04`
- object_coverage_mode：`multi_module`
- has_concrete_object_experiments：`yes`
- general_method_bucket：`none`
- primary_module_for_filing：`04`
- 归类理由：organic solar-cell material discovery 提供了明确的材料对象验证，因此 primary 取 `04`；分子设计、候选结构与合成语义同时支持 `03`
- 边界说明：旧的 `01.04`-only authority 已不再成立；当前正确写法是 `03;04`
- 归类置信度：高

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent
- 科研流程角色：knowledge_extraction_and_organization; hypothesis_generation; tool_use_and_code_execution; data_analysis; evidence_assessment_and_validation; end_to_end_research_automation

## 4. 方法设计

系统将全局规划与局部执行拆分为双 Agent 结构，通过工具调用和自纠错流程推进科学发现任务，并把 end-to-end organic-solar-cell discovery 作为核心对象验证。

## 5. 实验与验证

- 验证方式：benchmark
- 关键验证：organic solar-cell material discovery；candidate synthesis；device validation
- 科学贡献类型：design; experimental_discovery; system_platform
- 证据强度：`experimentally_validated`

## 6. 与已有工作的关系

它与纯 `01.04` 通用科研 Agent 的区别在于：这里已有 concrete chemistry / materials discovery outcome，而不是仅有平台化 benchmark。

## 7. 局限性与风险

- 本轮未新增本地 PDF 归档
- 当前写回主要依据 RSC full abstract；但对于 `03;04` 与 primary `04` 的判断已足够稳定

## 8. 对综述写作的价值

- 可放入章节：`04` 主章节，并作为 `03/04` 边界样本
- 可支撑论点：通用 dual-agent framework 只要已经对具体 molecules / materials 做了发现、合成和验证，就不应继续停留在 `01.04`

## 9. 总结

### 9.1 一句话概括

面向有机太阳能材料发现的双 Agent 科研系统。

### 9.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：03;04
object_coverage_mode：multi_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：04
first_hand_sources_checked：RSC DOI 10.1039/d5sc09883a full abstract; official OA PDF available but not archived locally in this round
local_pdf_archived_this_round：no
归类置信度：高
推荐引用强度：core
```
