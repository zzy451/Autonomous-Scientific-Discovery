# round 2 priority batch 2 跟进复核报告

> Historical note 2026-06-20：本报告形成于当前“放松领域实验覆盖”口径完全固化之前。报告中关于 `cross-domain demo`、`主对象`、`核心贡献`、`暂保持 01.04` 的判断只作为历史背景；本轮 451 篇多模块复核必须以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准，逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。只要对象层证据可识别，即可记录对应 `01–11` 模块，不要求该模块构成论文核心贡献。

生成日期：`2026-06-18`  
复核范围：`ASD-0053`、`ASD-0062`、`ASD-0079`、`ASD-0115`  
复核目标：对第二轮高风险 confirmed core 队列的第二批样本做更强证据复核，并区分“可以直接落地主列表收口”的 metadata / evidence-strength 问题与“仍需全文补证”的真实边界问题。

## 1. 本轮前基线

- total records：`871`
- confirmed included + classified count：`478`
- needs_review count：`0`
- confirmed `08` count：`3`

主要边界压力点：

- `01.04 / 具体科学对象`
- `01.04 / 11.07`
- `03 / 04`
- `06 / 07`
- `07 / 01.04`

## 2. 本轮已落地主列表修改

### 2.1 `ASD-0053` `Towards autonomous hypothesis verification via language models with minimal guidance`

- 当前记录保持：`to_read / 01.04`
- 本轮落地内容：
  - 去掉标题末尾误残留的年份字符串
  - `Evidence strength` 从 `low_metadata_only` 收口为 `benchmark_only`
  - 备注补入 round-2 结论

主控判断：

- 该论文的主对象仍是通用科研假设生成/验证能力，而不是具体学科对象，因此 `01.04` 不变。
- 真正的风险不是主类错误，而是 confirmed-core 强度偏弱。
- 全文本地 note 已经足够支持我们把“旧的 metadata-only 判断”升级为“benchmark-level evidence”。

一句话理由：

> `ASD-0053` 的问题不在错类，而在它更像早期 toy-problem capability probe，而不是成熟 scientific discovery core paper。

### 2.2 `ASD-0062` `Empowering scientific workflows with federated agents`

- 当前记录保持：`to_read / 01.04`
- 本轮落地内容：
  - 补齐 Agent type / workflow role / validation / contribution / evidence-strength 字段
  - 备注补入 round-2 结论

主控判断：

- 基于本地 full-text note，`ASD-0062` 继续支持留在 `01.04`，而不是回调到 `09`。
- 原因是论文主对象是 domain-general scientific workflow substrate / federated research-agent infrastructure，而不是某个具体 engineering object。
- 但它确实 infrastructure-heavy，因此仍应留在高风险 confirmed-core 队列中。

一句话理由：

> `ASD-0062` 的剩余风险是 confirmed-core 强度，而不是主类方向。

### 2.3 `ASD-0079` `DrugAgent`

- 当前记录保持：`to_read / 07.04`
- 本轮落地内容：
  - 标题更正为 note 与 arXiv v4 对应的 canonical task/title
  - 补齐 Agent type / workflow role / validation / contribution / evidence-strength
  - 备注明确这次处理的是 metadata correction，而不是主类改动

主控判断：

- 本地 full-text note 已经足够高置信表明该论文是 `drug-target interaction prediction` paper，而不是稳定意义上的 `drug repurposing` paper。
- 主类仍然稳定归 `07.04`，因为最终 scientific object 仍是 drug discovery / biomedical prediction task。

一句话理由：

> `ASD-0079` 的核心问题是 title/task metadata 漂移，不是 `07` 主类方向错误。

## 3. 本轮复核但暂不改主列表的记录

### 3.1 `ASD-0115` `Towards an AI co-scientist`

- 当前记录：`to_read / 07.04`
- 本轮结论：**暂不改主列表**

当前证据情况：

- 本地主列表已有 journal-upgrade 备注，但仍没有独立本地 full note。
- 题名与 paper framing 都明显具有通用 `co-scientist` / `general scientific workflow` 色彩。
- 支撑其暂留 `07.04` 的核心依据仍是现有 biomedical validation framing，而不是已经充分展开的全文证据。

主控判断：

- 这是一条真实的 `07 / 01.04` 高压边界样本。
- 当前还不适合只凭题名 general 就直接回调 `01.04`。
- 但同样也不能把它当成已经完全稳固的 biomedical core sample。

当前建议：

- 保持 `to_read / 07.04`
- 继续留在高优先级全文补证与 note-first 队列

一句话理由：

> `ASD-0115` 现在最缺的不是再做一轮摘要判断，而是需要全文级 note 来确认 biomedical object 是否真的是 primary object。

## 4. 本轮后的整体判断

### 4.1 哪些问题已经收口

- `ASD-0079`：已确认是 metadata correction，不是主类错误
- `ASD-0053`：已确认主类方向稳定，风险集中在 confirmed-core 强度
- `ASD-0062`：已确认主类方向稳定，风险集中在 infrastructure-heavy 的 confirmed-core 强度

### 4.2 哪些问题仍未收口

- `ASD-0115`：仍是高优先级 `07 / 01.04` 边界样本
- 更广义上，`01.04` confirmed core 里仍有一批 records 的主要问题不是“错类”，而是“是否保留在 confirmed core 的阈值偏宽”

## 5. 本轮 reviewer 交叉意见摘要

- `ASD-0053`：reviewer 与主控一致认为 `01.04` 方向稳定，但 confirmed-core 强度偏弱
- `ASD-0062`：reviewer 与主控一致认为 `01.04` 方向较稳，剩余风险是 infrastructure-heavy
- `ASD-0079`：reviewer 与主控一致认为应保留 `07.04`，并优先做 title/task metadata cleanup
- `ASD-0115`：reviewer 与主控一致认为当前不宜强改，但应继续保留在高优先级全文复核队列

## 6. 本轮后基线

- confirmed included + classified count：`478`
- needs_review count：`0`
- confirmed `08` count：`3`

本轮只落地了 metadata / evidence-strength / remarks 收口，没有改变 confirmed count。

## 7. 当前阶段结论

这批第二优先级样本继续支持我们当前的总体判断：

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
