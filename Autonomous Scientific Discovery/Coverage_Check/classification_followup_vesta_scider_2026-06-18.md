# `VESTA` 与 `SciDER` 跟进复核报告

生成日期：`2026-06-18`  
审计目标：继续收紧 `01.04` 高风险 confirmed core，并对 `VESTA` 与 `SciDER` 这两个仍在尾段保留的 general-workflow 样本做进一步裁决。

## 1. 本轮开始前状态

- confirmed included + classified count：`483`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当时主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - benchmark-heavy scientific workflow papers 是否被过宽算入 core

## 2. 本轮已落地改动

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0837 | VESTA: Visual Exploration with Statistical Tool Agents | `to_read / 01` | `background_only / 01` | 降级为背景 | 当前摘要把论文核心定义为 quantitative model refinement 的 statistical-tool agent framework，并以 DAWN benchmark 为中心，只是在后段落到 astronomy task，因此更像 general scientific-modeling workflow / benchmark paper，而不是稳定 primary discovery-agent study。 |

## 3. 本轮明确保留但继续观察

| ID | 题名 | 当前处理 | 当前判断 |
|---|---|---|---|
| ASD-0845 | SciDER: Scientific Data-centric End-to-end Researcher | 保留 `to_read / 01.04` | 当前摘要仍更像强 general scientific-agent system，而不只是 data preparation / orchestration substrate；现阶段证据还不足以像 `SciDataCopilot` 那样直接降为背景。 |

## 4. 这次裁决说明了什么

- `VESTA` 说明：即使有 real astronomy tasks，只要论文主体仍以 benchmark / general modeling workflow / statistical-tooling 为中心，就不应继续占用 confirmed core。
- `SciDER` 暂时保留，则说明我们并不是机械地把所有 data-centric 或 workflow-centric 论文都降级；只有当它们明显更像基础设施、protocol、benchmark 或 control platform 时才收口。

## 5. 当前最新状态

- confirmed included + classified count：`482`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 50`
  - `02: 31`
  - `03: 71`
  - `04: 100`
  - `05: 25`
  - `06: 56`
  - `07: 51`
  - `08: 3`
  - `09: 36`
  - `10: 27`
  - `11: 32`

## 6. 当前结论

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
