# priority core refinement 跟进复核报告

> Historical note 2026-06-20：本报告形成于当前“放松领域实验覆盖”口径完全固化之前。报告中关于 `cross-domain demo`、`主对象`、`核心贡献`、`暂保持 01.04` 的判断只作为历史背景；本轮 451 篇多模块复核必须以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准，逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。只要对象层证据可识别，即可记录对应 `01–11` 模块，不要求该模块构成论文核心贡献。

生成日期：`2026-06-18`  
审计目标：对 confirmed core refinement queue 中当前最优先的四条记录做更强证据复核，重点确认 `Science Earth`、`SciDER`、`ASD-0811`、`ASD-0855` 是否需要改主类或改 status。

## 1. 当前权威基线

- total records：`871`
- confirmed included + classified count：`478`
- needs_review count：`0`
- confirmed `08` count：`3`
- 当前主要边界压力点：
  - `01.04 / 具体科学对象`
  - `01.04 / 11.07`
  - `03 / 04`
  - `08 / 06`

## 2. 本轮处理结论

本轮未对 `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 落地主类或 status 改动。  
原因不是“没有问题”，而是这四条记录在补充摘要级与本地 follow-up 证据后，当前都更支持保留原判。

### 2.1 `ASD-0844` `Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery`

- 当前记录：`to_read / 01.04`
- 本轮结论：**保留 `01.04`**

补强证据：

- 论文自我定义更接近 `planet-scale operating system`、`scientific-agent runtime`、`coordination substrate`，而不是单一学科发现论文。
- 当前可见摘要与 HTML 证据强调其核心是 protocol、capability discovery、task ownership negotiation、cross-regime adjudication。
- 虽然文中有 physics 与 biology case study，但 companion papers 承载具体 scientific results，本论文承载的是通用 scientific runtime。

主控判断：

- 用户指出它做了物理和生物实验，这个质疑是成立的边界压力。
- 但按本项目“主类看最终 scientific object，而不看跨域 demo 数量”的规则，`Science Earth` 当前更像通用科研基础设施，因此仍应留在 `01.04`。

一句话理由：

> `Science Earth` 的主对象仍是通用 scientific coordination runtime，而不是物理或生物某一具体 scientific object。

### 2.2 `ASD-0845` `SciDER: Scientific Data-centric End-to-end Researcher`

- 当前记录：`to_read / 01.04`
- 本轮结论：**保留 `01.04`**

补强证据：

- 摘要强调的是 adaptability、domain generalization、multimodal scalability。
- 系统由多个 specialized sub-agents 组成，目标是自动化整个 research lifecycle。
- 当前证据主要指向 benchmark / workflow / end-to-end scientific researcher framing，而不是稳定单一具体学科对象。

主控判断：

- `SciDER` 比 `Science Earth` 更像需要后续全文继续盯的高风险 `01.04` 样本。
- 但在现阶段，仍没有足够证据把它稳定迁移到 `06`、`07`、`03` 或其他具体学科类。

一句话理由：

> `SciDER` 当前更像通用 data-centric scientific researcher，而不是已经稳定落在某个 concrete scientific object 上的领域论文。

### 2.3 `ASD-0811` `Closed-Loop Molecular Design with Calibrated Deference`

- 当前记录：`to_read / 04.04`
- 本轮结论：**保留 `04.04`**

补强证据：

- 当前摘要级证据显示系统面向 `aqueous organic redox flow battery (AORFB) negolyte` 设计。
- 评价终点集中在 `redox potential`、`electrochemical reversibility` 等电池相关性能。
- 流程是 synthesize / characterize / redesign 闭环，而不是以 reaction planning 或 synthesis route discovery 为核心对象。

主控判断：

- 这是一个真实存在的 `03 / 04` 高压边界样本。
- 虽然标题中有 `molecular design`，但按本项目规则，若最终被直接优化和评估的是 energy-materials object，则仍应优先放在 `04`。
- 现有证据还不足以把它改回 `03`。

一句话理由：

> 该论文直接优化的终点是 battery negolyte 的材料性能，而不是一般分子反应或合成路线本体。

### 2.4 `ASD-0855` `Automating Scientific Evaluation: A Multi-Agent Framework for Transparent and Trustworthy Peer Review`

- 当前记录：`to_read / 11.07`
- 本轮结论：**保留 `11.07`**

补强证据：

- 题名已经直接指向 `scientific evaluation` 与 `peer review`。
- 当前主列表备注与多份本地 follow-up 报告都稳定指向：研究对象是 scientific peer review itself。
- 该论文的剩余不确定性主要在 “framework-heavy 程度是否偏强”，而不是主类方向。

主控判断：

- 这不是 `01.04` 的 general scientific workflow platform。
- 其 primary object 明确属于 scientific knowledge production / scientific evaluation process itself，应稳定落在 `11.07`。

一句话理由：

> 这篇论文研究的对象是 scientific peer review 本身，而不是通用科研能力平台。

## 3. 本轮后的边界判断

### 3.1 `01.04 / 具体科学对象`

本轮继续支持已采用的硬规则：

- 只要论文主对象仍是通用 scientific runtime、research workflow substrate、protocol layer、data-centric end-to-end researcher 或 research-team infrastructure，即使出现 physics、biology、chemistry 等 case study，也不应仅凭 demo 把它移出 `01.04`。
- 但这类样本应持续列为高风险边界样本，后续若 companion papers 或全文证据显示 concrete object 已成为真正主对象，再重开改类讨论。

### 3.2 `03 / 04`

本轮继续支持：

- 若系统最终直接优化的是材料性能、energy-materials behavior、器件相关材料对象，应优先归 `04`。
- 若系统直接优化的是分子、反应、合成路线、催化条件本体，则应优先归 `03`。

`ASD-0811` 当前仍更靠 `04` 一侧。

### 3.3 `01.04 / 11.07`

本轮继续支持：

- 通用科研能力平台、general scientific-agent workflow、domain-general substrate -> `01.04`
- scientific peer review、scientific evaluation、scientific knowledge production itself -> `11.07`

`ASD-0855` 当前是这条边界上的稳定样本。

## 4. 本轮未落地修改的原因

本轮没有改主列表，不是因为这些样本“完全没有风险”，而是因为：

- `ASD-0844` 与 `ASD-0845` 在更强摘要级证据下仍更支持 `01.04`
- `ASD-0811` 仍更支持 `04.04`
- `ASD-0855` 仍更支持 `11.07`

因此，如果现在强行改写主类，反而会削弱主列表的一致性。

## 5. 当前阶段结论

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

本轮之后的最新状态仍为：

- confirmed included + classified count：`478`
- needs_review count：`0`
- confirmed `08` count：`3`

当前最主要边界压力点仍然是：

- `01.04 / 具体科学对象`
- `01.04 / 11.07`
- `03 / 04`
- `08 / 06`
