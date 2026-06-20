# `01.04` 与 `11.07` 跟进复核报告

> Historical note 2026-06-20：本报告形成于当前“放松领域实验覆盖”口径完全固化之前。报告中关于 `cross-domain demo`、`主对象`、`核心贡献`、`暂保持 01.04` 的判断只作为历史背景；本轮 451 篇多模块复核必须以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准，逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。只要对象层证据可识别，即可记录对应 `01–11` 模块，不要求该模块构成论文核心贡献。

生成日期：`2026-06-18`  
审计目标：继续压缩高风险 `01.04` confirmed core，并对 `01.04 / 11.07` 边界样本做更强证据复核。

## 1. 本轮开始前状态

- confirmed included + classified count：`484`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当时主要压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - scientific image / data / workflow tooling 是否被过宽计入 `01.04` core

## 2. 本轮已落地改动

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0834 | AiSciVision: A Framework for Specializing Large Multimodal Models in Scientific Image Classification | `to_read / 01` | `background_only / 01` | 降级为背景 | 当前摘要把论文定义为 niche scientific domains 中的 multimodal image-classification / interpretation workflow framework，虽是 agentic scientific tooling，但不足以继续作为稳定 primary discovery-agent study 计入 confirmed core。 |
| ASD-0849 | OmniScientist: Toward a Co-evolving Ecosystem of Human and AI Scientists | `to_read / 01` | `to_read / 11` | 主类改判 | 当前摘要明确强调 human-AI scientist ecosystem、contribution attribution、peer review、structured scientific knowledge network、open scientific evaluation infrastructure，因此 primary object 已偏向 scientific knowledge production / scientific system itself，应归 `11.07` 而非 `01.04`。 |

## 3. 这次改动说明了什么

### 3.1 `01.04 / 具体学科`

- `AiSciVision` 说明：即便是多领域 scientific workflow，如果论文主体只是 classification / interpretation / specialization tooling，也不应轻易占用 confirmed core。
- 这类 paper 仍可作为 `01.04` 背景支持文献保留，因为它们有助于刻画通用 scientific-agent tooling 的边界，但不应抬高核心覆盖。

### 3.2 `01.04 / 11.07`

- `OmniScientist` 是这条边界上的关键样本。
- 它虽然保留了通用科研能力平台外观，但如果论文把重点放在：
  - AI scientists 与 human scientists 的 co-evolving ecosystem
  - contribution attribution
  - peer review
  - scientific knowledge networks
  - open scientific evaluation
  那么 primary object 就已经转向 scientific knowledge production itself，应归 `11.07`。

## 4. 当前仍需继续盯住的样本

| ID | 题名 | 当前处理 | 风险说明 |
|---|---|---|---|
| ASD-0837 | VESTA | 保留 `to_read / 01.04` | astronomy task 很显眼，但当前摘要仍更像通用 statistical-tool agent workflow。 |
| ASD-0844 | Science Earth | 保留 `to_read / 01.04` | case study 覆盖 physics / biology，但当前主对象仍更像 coordination runtime。 |
| ASD-0845 | SciDER | 保留 `to_read / 01.04` | data-centric end-to-end research automation 强，但仍需继续判断是否属于稳定 core 还是 infrastructure-heavy platform。 |
| ASD-0848 | PaperOrchestra | 保留 `to_read / 11.07` | scientific manuscript production object 明确，但仍偏 framework / evaluation。 |
| ASD-0855 | Automating Scientific Evaluation | 保留 `to_read / 11.07` | peer-review object 明确，但也是 framework-heavy 样本。 |

## 5. 当前最新状态

- confirmed included + classified count：`483`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 51`
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
