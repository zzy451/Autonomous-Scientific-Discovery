> Historical note 2026-06-20: 本文件是旧口径 / 过渡口径下的历史审计记录，仅可作为背景线索。本轮 451 篇 confirmed 文献的多模块分类以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准；不得用本文中的 legacy single-primary、primary object 或 core-contribution 判断覆盖当前“可识别具体科学对象实验 / 验证 / benchmark task / case study / reported result 即可入对应模块”的规则。

# 第 1 轮全库分类复核报告：`ASD-0001`–`ASD-0200`

生成日期：`2026-06-18`  
审计模式：全库分类复核，第 1 轮，`200` 篇一批，`4 x 50` 只读 reviewer，并由主控代理收口裁决。  
审计范围：`Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 中 `ASD-0001`–`ASD-0200`

## 1. 本轮开始前基线

- confirmed included + classified count：`475`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 主要边界压力点：
  - `01.04 / 具体领域`
  - `01.04 / 11.07`
  - `06 / 07`
  - `03 / 04`
  - workflow / benchmark / infrastructure 是否被过宽保留为 core

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0062 | Empowering scientific workflows with federated agents | `to_read / 09` | `to_read / 01` | 主类修正 | 多位 reviewer 倾向将其视为通用 scientific workflow infrastructure；主控复核本地 full-text note 后，认为其主要对象是跨 federated research environment 的 domain-general scientific workflow substrate，而不是具体工程系统。故从 `09` 收口到 `01.04`。 |
| ASD-0189 | Automating exploratory proteomics research via language models | `background_only / 06` | `to_read / 06` | 状态提升 | reviewer-D 补充的 arXiv 摘要证据表明该文已有 hierarchical planning、tool execution、iterative refinement 与 autonomous hypothesis generation，且对象是 exploratory proteomics research，满足 Agent 纳入并应进入 confirmed core。 |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前主类 | 暂不改动原因 | 是否建议后续继续复核 |
|---|---|---|---|---|
| ASD-0006 | Dora AI Scientist | `06` | `01 / 06 / 07` 三方边界仍不稳，但现有证据仍不足以高置信改类。 | 是 |
| ASD-0009 | Agent-based learning of materials datasets from the scientific literature | `04` | reviewer 认为材料对象仍可成立，但其 discovery contribution 与 core 强度仍偏弱。 | 是 |
| ASD-0025 | CACTUS: Chemistry agent connecting tool usage to science | `03` | chemistry object 成立，但有较强 tool/benchmark assistant 压力，现阶段不直接降级。 | 是 |
| ASD-0045 | Honeycomb: A flexible LLM-based agent system for materials science | `04` | concrete materials object 仍在，但更像 materials workflow / QA system，需后续继续看 core 强度。 | 是 |
| ASD-0100 | SciReplicate-Bench | `01` | benchmark framing 很强，但本地 full-text note 支持其 dual-agent scientific reproduction 角色；本轮不直接降级。 | 是 |
| ASD-0115 | Towards an AI co-scientist | `07` | biomedical / general co-scientist 双重 framing 仍在；当前先不把它从 `07` 拉回 `01.04`。 | 是 |
| ASD-0140 | Large language models for automated open-domain scientific hypotheses discovery | `11` | `11.07 / 01.04` 边界真实存在，但当前仍可支持其 knowledge-production 对象。 | 是 |
| ASD-0151 | Self-driving lab discovers principles for steering spontaneous emission beyond conventional Fourier optics | `04` | reviewer-D 提醒其可能更接近 `02/光学物理`，但现有证据不足以在本轮强改。 | 是 |
| ASD-0200 | Rapid and automated alloy design with graph neural network-powered LLM-driven multi-agent systems | `04` `background_only` | 看起来像可升 core，但大概率与 `ASD-0084 / ASD-0086` 属 alloy-design 同一谱系；在版本映射未完成前暂不提升。 | 是 |

## 4. 边界问题清单

### 4.1 `01.04 / 具体领域`

- 本轮最重要的新收口案例是 `ASD-0062`。它虽然带有 strong engineering / infrastructure 语言，但主对象不是某个具体工程系统，而是 scientific workflow infrastructure itself，因此应回到 `01.04`。
- 相反，`ASD-0001`、`ASD-0007`、`ASD-0016`、`ASD-0031`、`ASD-0044`、`ASD-0046` 等记录都显示：只要研究对象稳定落在 materials / astronomy / chemistry，就不应因为系统“很通用”而误送回 `01.04`。

### 4.2 `06 / 07`

- `ASD-0006`、`ASD-0033`、`ASD-0077`、`ASD-0115` 是这一批最典型的 biomedical / omics 摇摆样本。
- 当前可继续沿用的实操口径仍然是：若核心对象是 gene / protein / single-cell / omics / cellular mechanism，则优先 `06`；若疾病、治疗、药物转化、患者对象更强，则优先 `07`。
- 本轮没有足够证据支持对这一组做大范围重分。

### 4.3 `03 / 04`

- 本轮没有新增必须立刻落地的 `03 / 04` 主类修正，但压力仍存在于 `ASD-0056`、`ASD-0151` 一类“功能材料 / 光学规律 / 物理机制”混合对象。
- 当前保持的硬规则仍有效：
  - 直接搜索分子、反应、催化位点、OSDA、合成路线时，优先 `03`
  - 直接搜索材料组成、结构、性能、alloy、MOF、metamaterial、device material 时，优先 `04`

### 4.4 `01.04 / 11.07`

- `ASD-0186` 是这一批最稳定的正例：scientific peer review / review generation 对象应留在 `11.07`。
- `ASD-0140` 仍是边界样本，但当前还没有足够强的证据把它回退为一般 research automation。

### 4.5 低估 core 的补升压力

- `ASD-0189` 是本轮最明确的“此前保守过头”样本：原先放成 `background_only`，但补看摘要后足以进入 core。
- 这说明当前问题并不只是“core 保留过宽”，也存在少数真实 Agent paper 被低估的情况，但数量明显更少。

## 5. 本轮后统计

- confirmed included + classified count：`476`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 47`
  - `02: 31`
  - `03: 71`
  - `04: 100`
  - `05: 25`
  - `06: 57`
  - `07: 51`
  - `08: 3`
  - `09: 35`
  - `10: 24`
  - `11: 32`
- 当前主要边界压力点：
  - `01.04 / 具体领域`
  - `01.04 / 11.07`
  - `06 / 07`
  - `03 / 04`
  - workflow / benchmark / infrastructure 是否被过宽保留为 core

## 6. 结论

- 本轮复核显示，`0001–0200` 中真正需要立即修改主列表的高置信记录并不多，说明这一批整体主类稳定性高于“需要大规模推倒重来”的水平。
- 当前更突出的不是一级类框架失效，而是少数边界样本的解释口径仍需继续收紧，尤其是：
  - 通用 scientific workflow / infrastructure 是否应留 `01.04`
  - biomedical / omics 边界是否应留 `06` 还是进 `07`
  - benchmark / assistant / framework 是否被过宽保留为 confirmed core
- 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
