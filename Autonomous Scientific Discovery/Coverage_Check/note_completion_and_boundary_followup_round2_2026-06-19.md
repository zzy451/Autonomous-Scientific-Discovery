# 高风险缺 note 批次补齐后分类跟进报告

> Historical note 2026-06-20：本报告形成于当前“放松领域实验覆盖”口径完全固化之前。报告中关于 `cross-domain demo`、`主对象`、`核心贡献`、`暂保持 01.04` 的判断只作为历史背景；本轮 451 篇多模块复核必须以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准，逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。只要对象层证据可识别，即可记录对应 `01–11` 模块，不要求该模块构成论文核心贡献。

生成日期：`2026-06-19`  
审计范围：`high_risk_missing_note_batch_49_manifest_2026-06-18.md` 中已落地 note 的 `51` 条记录，以及其中若干高压边界样本  
审计模式：note 补齐后的小范围分类收口 / 边界解释固化

## 1. 本轮开始前基线

- confirmed included + classified count：`478`
- needs_review count：`0`
- confirmed `08` count：`3`
- 当前已确认的高风险缺 note 目标批次：`51` 条
- 该批次当前已有 `Note path` 的记录数：`51 / 51`
- confirmed core 中当前仍缺少 `Note path` 的记录数：`350`
- 主要边界压力点：
  - `01.04 / 01.02`
  - `01.04 / 11.07`
  - `03 / 04`
  - `07 / 01.04`
  - `08` 稀缺样本的“保守纳入”与“避免放宽标准”

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原分类 | 新状态 / 新分类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| `ASD-0738` | `AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery` | `to_read / 01 / 01.04` | `to_read / 01 / 01.02` | 收紧二级类 | 根据 primary abstract，论文核心对象是 AI model discovery、reproduction、iterative improvement，本体已是具体计算研究对象，不宜继续留在通用 `01.04`。 |
| `ASD-0850` | `OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery` | `to_read / 01 / 01.04` | `to_read / 01 / 01.02` | 收紧二级类 | 根据 primary abstract，论文核心对象是 automated algorithm discovery in formal-computational research，实验也落在 combinatorial optimization 与 cooperative-driving 环境，较适合 `01.02`。 |
| `ASD-0844` | `Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery` | `to_read / 01 / 01.04` | `to_read / 01 / 01.04` | 不改类，补强备注 | 重新核对摘要后确认，物理与单细胞只是跨域 demo；论文主语仍是 runtime / protocol / scientific operating system，本体不是具体单一科学对象。 |
| `ASD-0737` | `ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence Verification` | `to_read / 01 / 01.04` | `to_read / 01 / 01.04` | 不改类，补强备注 | 当前证据更支持其为带可验证性机制的通用 autonomous-research workflow；虽与 `11.07` 接壤，但摘要层证据还不足以改到 scientific knowledge production 对象。 |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前分类 | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| `ASD-0844` | `Science Earth` | `01 / 01.04` | 你提出的质疑是合理的，但摘要已明确它把跨学科案例作为 runtime 验证，而不是把 physics 或 single-cell biology 作为主对象。 | 是，若后续拿到全文可再核 EACN / runtime 部分与 case-study 权重。 |
| `ASD-0737` | `ScientistOne` | `01 / 01.04` | `01.04 / 11.07` 边界压力仍高，但现有证据更像“让通用 research agent 变得可验证”，还不是直接研究科学知识生产制度本身。 | 是，优先补全文 note。 |
| `ASD-0528` | `AutoSciLab` | `01 / 01.04` | 虽有 projectile motion、Ising、nanophotonics 等案例，但摘要主语仍是 interpretable self-driving laboratory framework；跨域 demo 不足以推出 `01.04`。 | 是。 |
| `ASD-0811` | `Closed-Loop Molecular Design with Calibrated Deference` | `04 / 04.04` | 仍是 `03 / 04` 高压样本，但当前证据更支持 energy-materials / battery-negolyte 对象，而不是一般分子反应路线优化。 | 是。 |
| `ASD-0112` | `CSSTep` | `07 / 07.04` | 仍是 `03 / 07` 边界样本；当前记录更偏 drug-like molecules / therapeutic target 叙事，暂保留 `07.04`。 | 是。 |
| `ASD-0695` | `FoodPuzzle` | `08 / 08.05` | `08` 稀缺不等于放宽标准；当前摘要足以支持 food/flavor science object，但 core-strength 仍偏 abstract / benchmark 侧。 | 是。 |
| `ASD-0510` | `A conversational multi-agent AI system for automated plant phenotyping` | `08 / 08.01` | 当前证据仍支持农业生产对象而非一般植物生命机制，适合作为 confirmed `08` 保守样本继续保留。 | 是。 |

## 4. 本轮边界问题清单

### 4.1 `01.04 / 01.02`

这一轮最明确的发现不是一级类错误，而是部分 `01` 类记录在二级类上被写得过泛。像 `AutoSOTA`、`OR-Agent` 这类论文虽然也有 workflow / multi-agent / automated research 叙事，但其最终对象已经收敛到 AI model discovery 或 algorithm discovery，本质上是具体的 formal-computational research object，不宜继续占用通用 `01.04`。

### 4.2 `01.04 / 11.07`

`ScientistOne` 说明这个边界依然有压力。只要论文是在“增强一般 research agent 的可验证性、可追溯性、可靠性”，它仍可能属于 `01.04`；只有当研究对象真正转向 scientific peer review、scientific publishing、scientific evaluation、scientific knowledge production itself 时，才应稳定落到 `11.07`。

### 4.3 `Science Earth` 的用户质疑与当前裁决

关于 `Science Earth`，这次复核明确承认你的担心有道理，因为它确实用了物理和生物相关案例。  
但按项目的对象优先规则，本轮仍不改主类：摘要主语是 planet-scale AI-native scientific operating system、heterogeneous runtime、EACN protocol；跨学科案例更像“证明这个 runtime 能跨域工作”，而不是把论文主对象改成物理学或生命科学本身。

### 4.4 `08` 类仍应维持保守口径

`FoodPuzzle`、`PhenoAssistant` 这类样本对 `08` 很重要，但这轮没有发现足够证据支持放宽 `08`。  
当前更合理的做法仍是：把 `08` 当作稀缺但真实存在的类别，宁可少、不要虚胖。

## 5. 本轮后统计

- confirmed included + classified count：`478`
- needs_review count：`0`
- confirmed `08` count：`3`
- confirmed class 分布：
  - `01`: `47`
  - `02`: `31`
  - `03`: `73`
  - `04`: `99`
  - `05`: `25`
  - `06`: `58`
  - `07`: `53`
  - `08`: `3`
  - `09`: `34`
  - `10`: `23`
  - `11`: `32`
- 本轮 note 目标批次 `51 / 51` 已全部具备 `Note path`
- 当前 confirmed core 中仍缺 `Note path`：`350`
- 当前主要边界压力点：
  - `01.04 / 01.02`
  - `01.04 / 11.07`
  - `03 / 04`
  - `07 / 01.04`
  - `08` 的稀缺样本强度核实

## 6. 结论

这一轮最重要的收获，不是推翻一级类，而是把“高风险缺 note 批次”真正从无本地证据状态拉回到可追溯状态，并据此收紧了少数 `01` 类内部过泛的二级分类。

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
