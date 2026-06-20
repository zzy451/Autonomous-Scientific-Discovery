# `01.04` 高风险 confirmed core 清理跟进报告

> Historical note 2026-06-20：本报告形成于当前“放松领域实验覆盖”口径完全固化之前。报告中关于 `primary discovery-agent study`、`主对象`、`核心贡献`、`暂保持 01.04` 的判断只作为历史背景；本轮 451 篇多模块复核必须以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准，逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。只要对象层证据可识别，即可记录对应 `01–11` 模块，不要求该模块构成论文核心贡献。

生成日期：`2026-06-18`  
审计目标：继续压缩 `01.04` 中被过宽计入 confirmed core 的 infrastructure / protocol / data-workflow / research-platform 记录，避免把通用 scientific-agent 基础设施误当成稳定 primary discovery-agent study。

## 1. 本轮开始前状态

- confirmed included + classified count：`485`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当时主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `01.04` 内部的 data / protocol / orchestration / lab-runtime infrastructure 是否被过宽算入 core

## 2. 本轮新增落地改动

| ID | 题名 | 原状态 | 新状态 | 处理理由 |
|---|---|---|---|---|
| ASD-0847 | Claw AI Lab: An Autonomous Multi-Agent Research Team | `to_read` | `background_only` | 论文把重点放在 lab-native autonomous research platform、monitoring、artifact inspection、rollback / resume、research modes 与 dashboard/control surface，更像 interactive autonomous-research infrastructure，而不是稳定 primary scientific-discovery system study。 |

## 3. 与上一轮一起看，当前已经清出去的高风险 `01.04` core

| ID | 题名 | 当前状态 | 清理方向 |
|---|---|---|---|
| ASD-0835 | SciDataCopilot | `background_only` | scientific-data preparation / ingestion / multimodal integration infrastructure |
| ASD-0846 | SCP | `background_only` | global protocol / orchestration / lifecycle-management infrastructure |
| ASD-0847 | Claw AI Lab | `background_only` | lab-native autonomous-research platform / control infrastructure |

这三条的共同点是：

- 都是通用 scientific-agent infrastructure
- 都强调 orchestration、resource integration、control surface、monitoring、protocol、data readiness 或 lab runtime
- 都缺少“围绕单一 scientific object 形成稳定 primary discovery contribution”的证据

因此它们作为 `01.04` 背景支持文献是有价值的，但继续计入 confirmed core 会抬高 `01` 类核心覆盖，扭曲后续综述主体。

## 4. 本轮明确保留但继续盯住的样本

| ID | 题名 | 当前处理 | 当前判断 |
|---|---|---|---|
| ASD-0844 | Science Earth | 保留 `to_read / 01.04` | 当前证据仍更支持 heterogeneous scientific-agent runtime / coordination substrate，而不是单一学科对象论文。 |
| ASD-0834 | AiSciVision | 保留 `to_read / 01.04` | 多学科 scientific image classification specialization framework，当前仍可视作 domain-spanning general scientific workflow。 |
| ASD-0837 | VESTA | 保留 `to_read / 01.04` | 目前更像通用 statistical-tool agent workflow，尽管落到 astronomy task。 |
| ASD-0845 | SciDER | 保留 `to_read / 01.04` | data-centric end-to-end researcher 方向成立，但仍是高风险 general scientific-agent system。 |
| ASD-0849 | OmniScientist | 保留 `to_read / 01.04` | 覆盖 publication / evaluation，但主对象仍更像通用科研能力生态平台，而不是 knowledge production object 本身。 |

## 5. 当前阶段判断

- `01.04` 不是不稳定，而是 confirmed core 的进入标准过去偏松。
- 真正需要继续清理的不是所有 `01.04`，而是其中的：
  - data-prep infrastructure
  - protocol / orchestration layer
  - dashboard / lab-runtime control platform
  - review / roadmap / perspective
  - benchmark-heavy general workflow paper

## 6. 当前最新状态

- confirmed included + classified count：`484`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `01.04` 内部 infrastructure vs stable core system
  - `05 / 10`
  - `03 / 04`

## 7. 当前结论

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
