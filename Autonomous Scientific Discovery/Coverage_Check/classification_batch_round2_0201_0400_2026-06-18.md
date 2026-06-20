# 第 2 轮全库分类复核报告：`ASD-0201`–`ASD-0400`

生成日期：`2026-06-18`  
审计模式：全库分类复核，第 2 轮，`200` 篇一批，`4 x 50` 只读 reviewer，由主控代理统一裁决并修改主列表。  
审计范围：`Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 中 `ASD-0201`–`ASD-0400`

## 1. 本轮开始前基线

- confirmed included + classified count：`476`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 主要边界压力点：
  - `01.04 / 具体领域`
  - `01.04 / 11.07`
  - `03 / 04`
  - `06 / 07`
  - SDL platform / orchestration / methodology 是否被过宽保留为 confirmed core

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0212 | Control Risk for Potential Misuse of Artificial Intelligence in Science | `background_only / 11.03` | `background_only / 11.07` | 主类细化修正 | 研究对象是 scientific knowledge production and governance，而不是一般公共管理。 |
| ASD-0232 | MDAgents: An adaptive collaboration of LLMs for medical decision-making | `background_only / 07.04` | `background_only / 07.02` | 二级类修正 | 当前证据只支持 clinical decision-making，不支持 drug discovery。 |
| ASD-0268 | Quantum many-body physics calculations with large language models | `background_only / 02.01` | `background_only / 02.02` | 二级类修正 | 对象是 quantum many-body physics，不是 astronomy。 |
| ASD-0276 | Automating exploratory multiomics research via language models | `background_only / 06` | `to_read / 06` | 欠纳入上调 | reviewer 共识与公开摘要证据均支持其为自动化、迭代式 multiomics research Agent。 |
| ASD-0281 | Accelerated end-to-end chemical synthesis development with large language models | `background_only / 03` | `excluded / 03` | duplicate / preprint cleanup | 作为 `ASD-0280` 的 preprint / duplicate 处理更稳妥。 |
| ASD-0290 | ChemReasoner: Heuristic search over a large language model’s knowledge space using quantum-chemical feedback | `background_only / 03` | `to_read / 03` | 欠纳入上调 | 公开摘要已明确 heuristic search、反馈迭代、quantum-chemical feedback，满足当前 Agent 纳入口径。 |
| ASD-0300 | MuJoCo: A physics engine for model-based control | `background_only / 09` | `excluded / 09` | 移出背景池 | 通用仿真/控制引擎，不属于本项目有效科学 Agent 背景。 |
| ASD-0333 | Moose-chem: Large language models for rediscovering unseen chemistry scientific hypotheses | `background_only / 03` | `to_read / 03` | 欠纳入上调 | reviewer 复核与公开摘要一致支持其为 chemistry hypothesis rediscovery 的多阶段 Agent 框架。 |
| ASD-0355 | Transformer quantum state: A multipurpose model for quantum many-body problems | `background_only / 02.01` | `background_only / 02.02` | 二级类修正 | 量子多体对象应归 physics。 |
| ASD-0386 | What is a minimal working example for a self-driving laboratory? | `to_read / 01.04` | `background_only / 01.04` | 从 confirmed core 降回 background | 更像 SDL methodology / commentary，而不是 primary Agent-system study。 |
| ASD-0399 | The physics and chemistry of the Schottky barrier height | `background_only / 02` | `background_only / 04` | 主类修正 | Schottky barrier 更稳定地落在 materials / interface science，而不是 physics-cosmos 口径。 |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前主类 | 暂不改动原因 | 是否建议后续继续复核 |
|---|---|---|---|---|
| ASD-0207 | DS-Agent: Automated data science by empowering large language models with case-based reasoning | `01 / 01.04` background | 更像 research-adjacent data-science automation；当前不足以直接上调，也不足以强行改出 `01.04`。 | 是 |
| ASD-0263 | ArxivDigestables: Synthesizing scientific literature into tables using language models | `01 / 01.04` background | 有 `01.04 / 11.07` 压力，但当前更像 literature tooling / synthesis assistance，证据还不够强。 | 是 |
| ASD-0347 | The evolving role of large language models in scientific innovation: Evaluator, collaborator, and scientist | `11 / 11.07` background | reviewer 提醒其可能是 `01.04 / 11.07` 边界样本，但目前没有必要改动。 | 是 |
| ASD-0357 | Origene: A self-evolving virtual disease biologist automating therapeutic target discovery | `07 / 07.04` core | 当前 disease / therapeutic target framing更支持 `07`，但仍是 `06 / 07` 的高风险边界样本。 | 是 |
| ASD-0372 | Data-Centric Architecture for Self-Driving Laboratories with Autonomous Discovery of New Nanomaterials | `04 / 04.04` core | 有 architecture/core 边界压力，但题名与现有备注仍支持 concrete nanomaterials object。 | 是 |
| ASD-0382 | Toward autonomous design and synthesis of novel inorganic materials | `04 / 04.04` core | 带有路线宣言色彩，但当前仍可维持 concrete materials object。 | 是 |
| ASD-0383 | Universal self-driving laboratory for accelerated discovery of materials and molecules | `04 / 04.04` core | 这是本轮最强的 `03 / 04` 兼 `01.04 / 具体领域` 边界样本；“universal” 压力存在，但当前尚不足以直接改到 `01.04`。 | 是 |
| ASD-0388 | Crystallography companion agent for high-throughput materials discovery | `04 / 04.04` core | companion-agent / copilot 边界明显，但现有证据仍偏向 concrete materials-discovery workflow。 | 是 |

## 4. 边界问题清单

### 4.1 `01.04 / 具体领域`

- 本轮最重要的正向修复不是“把更多东西赶出 `01.04`”，而是避免把真正已有科学对象与 Agent 闭环的论文长期压在 `background_only`。
- `ASD-0276`、`ASD-0290`、`ASD-0333` 都说明此前确实存在少量欠纳入样本。
- 但 `ASD-0207`、`ASD-0263`、`ASD-0373`、`ASD-0384` 这类基础设施/工作流/工具化条目，仍然是 `01.04` 压力的主要来源。

### 4.2 `01.04 / 11.07`

- `ASD-0212` 的修正进一步支持既有规则：如果对象是 scientific knowledge production / governance，本轮应优先收口到 `11.07`。
- `ASD-0263` 仍是值得继续盯住的边界样本，但当前证据不足以仅凭题名把 literature synthesis tooling 直接改成 `11.07`。

### 4.3 `03 / 04`

- 本轮最敏感样本仍是 `ASD-0383`。它跨 materials 与 molecules，确实带来 `03 / 04` 与 “是否仍算具体领域对象” 的双重压力。
- 在没有更强全文证据前，当前先维持 `04`，但应继续作为后续复核优先样本。
- `ASD-0399` 的修正则属于较清晰的历史误挂，不影响总体类框架稳定性。

### 4.4 `06 / 07`

- `ASD-0357` 仍是本轮最重要的 `06 / 07` 样本。
- 当前 disease biologist / therapeutic target discovery 的对象表述仍更支持 `07`，但是否存在更深的机制研究导向，仍需全文确认。

### 4.5 SDL core / background 边界

- `ASD-0386` 的降级说明：当前 confirmed core 里最需要警惕的，不只是错类，还有 methodology / commentary / minimal example 被过宽保留的问题。
- 这一边界在 `ASD-0372`、`ASD-0383`、`ASD-0388` 上仍未完全消失，但本轮没有足够证据支持继续大规模下调。

## 5. 本轮后统计

- confirmed included + classified count：`479`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 47`
  - `02: 31`
  - `03: 73`
  - `04: 100`
  - `05: 25`
  - `06: 58`
  - `07: 51`
  - `08: 3`
  - `09: 35`
  - `10: 24`
  - `11: 32`
- 当前主要边界压力点：
  - `01.04 / 具体领域`
  - `01.04 / 11.07`
  - `03 / 04`
  - `06 / 07`
  - SDL platform / orchestration / companion-agent 是否应继续计入 confirmed core

## 6. 结论

- 本轮最有价值的发现不是一级类大面积失稳，而是确认了少数此前被保守压低的 core 候选确实应进入 confirmed core。
- 与此同时，Round 2 也再次说明真正持续施压的仍是边界解释，尤其是 `01.04`、`11.07` 与 SDL 平台类样本的收口。
- 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 7. 下一轮建议

- 下一轮范围：`ASD-0401`–`ASD-0600`
- 继续沿用 `200` 篇一轮、`4 x 50` 只读 reviewer 的组织方式。
- 主控优先继续抓三类问题：
  - `01.04` 中可能被过宽保留的 SDL / orchestration / workflow / instrumentation 论文
  - `03 / 04` 与 `06 / 07` 的高风险 core 样本
  - duplicate / preprint / roadmap / methodology 清理
