# `01.04` 中 SDL core 残余样本第二轮收口报告

生成日期：`2026-06-18`  
审计目标：继续压缩 `01.04` 中仍被保留为 confirmed core 的 self-driving-lab optimization / orchestration 残余样本，并修正当前 source trail 明显不稳的记录。

## 1. 本轮开始前基线

- confirmed included + classified count：`477`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当时主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `05 / 10`
  - `08 / 06`
  - `01.04` 内 remaining SDL / benchmark / scientific-coding core 样本是否仍有过宽保留

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0384 | Chimera: enabling hierarchy based multi-objective optimization for self-driving laboratories | `to_read / 01` | `background_only / 01` | 降级为背景 | Chemical Science 摘要将其核心定义为 general-purpose multi-objective optimization / achievement scalarizing function，用于 SDL decision loops；它更像优化基础设施，而不是稳定的 confirmed core discovery-Agent paper。 |
| ASD-0593 | AutoDSL: Automated self-driving laboratory with large language model agents | `to_read / 01` | `background_only / 01` | 降级为背景 | 当前主列表 DOI 直接解析到无关论文 `Search-o1`，source trail 明显不稳；在正确 primary source 未恢复前，不适合继续保留 confirmed core。 |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前主类 | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| ASD-0089 | ResearchCodeAgent: An LLM Multi-Agent System for Automated Codification of Research Methodologies | `01` | 本地 full note 证据较强，显示其不仅是 benchmark，而是明确的多 Agent research-method codification system。 | 是 |
| ASD-0100 | SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers | `01` | benchmark 属性很强，但同时带有 `Sci-Reproducer` dual-agent framework；当前证据尚不足以下调。 | 是 |
| ASD-0528 | AutoSciLab: A Self-Driving Laboratory for Interpretable Scientific Discovery | `01` | 仍是 general SDL 样本，但当前没有足够强的摘要 / 正文证据支撑本轮直接降级。 | 是 |

## 4. 边界问题清单

### 4.1 `SDL optimization primitive` 不应自动算作 ASD 核心系统

`Chimera` 说明，哪怕一篇论文被频繁嵌入 self-driving-lab 叙事中，只要它本体主要是 general optimization primitive、scalarization function 或 multi-objective search component，就更适合作为 `01.04` 背景基础设施，而不是 confirmed core。

### 4.2 source trail 不稳的 `01.04` 条目必须从严

`AutoDSL` 当前最直接的问题不是边界解释，而是来源本身不稳：主列表 DOI 指向 unrelated paper。  
在 correct primary source 未恢复前，继续把它放在 confirmed core 会直接降低主列表可信度，因此本轮先降为 `background_only` 是更保守也更稳妥的处理。

### 4.3 `01.04` 剩余压力逐渐集中到少量“scientific coding / reproduction”样本

经过连续几轮清理后，`01.04` 剩余高风险 core 已明显收缩，当前更需要精查的是：

- scientific coding
- paper-to-code reproduction
- benchmark + dual-agent framework 混合样本
- 少量 title-level SDL general systems

## 5. 本轮后统计

- confirmed included + classified count：`475`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 46`
  - `02: 31`
  - `03: 71`
  - `04: 100`
  - `05: 25`
  - `06: 56`
  - `07: 51`
  - `08: 3`
  - `09: 36`
  - `10: 24`
  - `11: 32`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `05 / 10`
  - `08 / 06`
  - `01.04` 内 remaining scientific-coding / reproduction / title-level SDL core 样本是否仍有少量过宽保留

## 6. 结论

这轮进一步说明，`01.04` 的收口已经从“大块 infrastructure 清理”进入“少量残余样本精修”阶段。当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
