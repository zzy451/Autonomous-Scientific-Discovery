# `class 10` 谱系去膨胀复核报告

生成日期：`2026-06-18`  
审计目标：继续压缩 `10` 类中同系统谱系重复占用 confirmed core 的记录，区分“真正独立的 mission-science Agent 主论文”与“同一系统的项目页、经验总结、部署综述或运行汇报”。

## 1. 本轮开始前基线

- confirmed included + classified count：`482`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当时主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `05 / 10`
  - `08 / 06`
  - `class 10` 同系统 mission-science lineage 是否被重复计入 confirmed core

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0646 | The EO-1 Autonomous Science Agent | `to_read / 10` | `background_only / 10` | 降级为背景 | 当前保留的规范来源更像 JPL project-page / lineage anchor，而不是一篇独立、可与其他 EO-1 主论文并列的 primary mission-science paper。 |
| ASD-0720 | Lessons Learned from Autonomous Sciencecraft Experiment | `to_read / 10` | `background_only / 10` | 降级为背景 | 论文重点是 deployment retrospective 与 lessons learned，适合作为 EO-1 / ASE 系统运行经验背景，不宜继续占用 confirmed core。 |
| ASD-0732 | Enhancing Science and Automating Operations Using Onboard Autonomy | `to_read / 10` | `background_only / 10` | 降级为背景 | 当前证据更支持其为同一 autonomy stack 的 mission-operations summary，而非独立的 primary Agent-system study。 |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前主类 | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| ASD-0852 | Autonomous science for an ExoMars Rover-like mission | `10` | 主题明确是 rover-like mission science autonomy，具备独立 mission-science Agent 贡献，保留 confirmed core 合理。 | 否 |
| ASD-0853 | Onboard Autonomous Rover Science | `10` | 主题明确是 onboard rover-science target selection、analysis 与 adaptive execution，仍是 clean `10` 类主论文。 | 否 |
| ASD-0854 | Enabling Autonomous Science for a Mars Rover | `10` | 核心对象仍是 Mars rover mission-science autonomy，而不是一般部署总结。 | 否 |
| ASD-0858 | Incorporating AEGIS autonomous science into Mars Science Laboratory rover mission operations | `10` | 虽然带有 operations 色彩，但核心仍是将 autonomous science 纳入真实 rover mission constraints，当前证据足以保留为 confirmed core。 | 是 |
| ASD-0859 | Monitoring active volcanism with the Autonomous Sciencecraft Experiment on EO-1 | `05` | 虽搭载 mission platform，但研究对象是 volcano monitoring，自然过程对象优先，保留 `05` 合理。 | 否 |
| ASD-0860 | Autonomous detection of cryospheric change with hyperion on-board Earth Observing-1 | `05` | 研究对象是 cryosphere change，属于 Earth-system monitoring，不应因为在 EO-1 上就移入 `10`。 | 否 |
| ASD-0861 | Flood detection and monitoring with the Autonomous Sciencecraft Experiment onboard EO-1 | `05` | 研究对象是 flood monitoring，符合 `05 / 10` 既定边界规则。 | 否 |

## 4. 边界问题清单

### 4.1 `05 / 10` 边界本轮进一步稳定

本轮复核继续支持已采用的硬规则：如果论文运行在卫星、航天器或 mission platform 上，但 primary scientific object 是火山、洪水、冰冻圈等 Earth natural process，则仍应归 `05`；只有当论文核心研究对象是 rover / spacecraft / mission-science autonomy 本身时，才归 `10`。

### 4.2 `class 10` 的真实压力点不是一级分类错误，而是谱系重复记账

`10` 类目前更大的问题不是“地球过程论文被误分到 10”，而是同一 EO-1 / ASE / onboard autonomy 系统的 project page、deployment summary、lessons-learned、operations write-up 容易同时占用 confirmed core。  
这类记录应优先去膨胀，而不是机械保留。

### 4.3 仍需谨慎对待 mission-operations 论文

像 `ASD-0858` 这类 mission-operations paper，虽然目前保留在 confirmed core，但它们与 deployment-summary 边界较近。后续若拿到更强全文证据，应继续核对其是否真的提供独立 scientific-agent contribution，而不仅是工程接入说明。

## 5. 本轮后统计

- confirmed included + classified count：`479`
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
  - `10: 24`
  - `11: 32`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `05 / 10`
  - `08 / 06`
  - `class 10` 中 remaining mission-operations core 样本是否还存在少量谱系膨胀

## 6. 结论

本轮最重要的结果不是改写 `05 / 10` 一级边界，而是确认 `class 10` 中确实存在同系统 lineage inflation，需要把 project-page anchor、经验总结和运行汇报从 confirmed core 中剥离出来。  
当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
