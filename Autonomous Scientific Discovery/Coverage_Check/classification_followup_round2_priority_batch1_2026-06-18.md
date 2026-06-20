# round 2 priority batch 1 跟进复核报告

生成日期：`2026-06-18`  
复核范围：`ASD-0004`、`ASD-0006`、`ASD-0009`、`ASD-0033`  
复核目标：对第二轮高风险 confirmed core 队列的第一批样本做更强证据复核，并决定是否需要主列表改动。

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
- `08 / 06`

## 2. 本轮已落地主列表修改

### 2.1 `ASD-0004`

- 原记录标题：`Novelseek: When agent becomes the scientist...`
- 当前更正后：`InternAgent: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification`
- 当前主类保持：`to_read / 01.04`

结论：

- 本轮对 `ASD-0004` 落地的是 **metadata correction**，不是分类改动。
- 当前已可高置信确认：对应 `arXiv:2505.16938` 的 canonical title / author line 应以 `InternAgent` 为准，而不是 `NovelSeek`。

## 3. 本轮复核但暂不改主列表的记录

### 3.1 `ASD-0006` `DORA AI Scientist`

- 当前记录：`to_read / 06.03`
- 本轮结论：**暂不改主列表**

当前更强证据显示：

- 现有本地 note 仍主要基于 abstract + metadata，全文证据仍弱。
- 题名中的 `multi-agent virtual research team` 与 `automated report generation` 会把它往 `01.04` 拉。
- 但现有整理材料又持续提示其 biomedical / drug-discovery research 语境，因此当前也不能高置信改去 `01.04`。

主控判断：

- 这是一个真实的 `06 / 07 / 01.04` 三向压力样本。
- 在没有更强全文证据前，当前仍不适合强改主类。

当前建议：

- 保持 `to_read / 06.03`
- 继续作为高优先级全文补证样本

补充说明：

- 本轮 reviewer 只读意见中，有一方明确认为当前公开证据更像 `01.04` 通用 scientific research / reporting workflow，而不是稳定生命科学对象。
- 主控代理这次仍未直接改类，原因不是因为 `06.03` 证据更强，而是因为全文仍不可得，当前更适合先把风险写清楚而不是强行改写主列表。

### 3.2 `ASD-0009` `Agent-based learning of materials datasets from the scientific literature`

- 当前记录：`to_read / 04.04`
- 本轮结论：**暂不改主列表**

当前更强证据显示：

- 这篇文章的 Agent 纳入和材料对象方向都成立。
- 但其直接贡献更偏向 materials literature extraction / ML-ready dataset construction。
- 风险不在主类方向，而在它是否足够强到继续保留在 confirmed core。

主控判断：

- 目前还没有足够证据把它直接降为 `background_only`。
- 但它属于 confirmed-core 强度偏弱的样本，应继续列为高风险精修对象。

当前建议：

- 保持 `to_read / 04.04`
- 后续全文再核其 “core system paper” 强度是否足够

补充说明：

- 本轮 reviewer 只读意见与主控判断一致：`ASD-0009` 的主要风险不在主类方向，而在它是否更接近 materials data-construction support paper，从而使 confirmed-core 强度偏弱。

### 3.3 `ASD-0033` `OmniCellAgent`

- 当前记录：`to_read / 06.03`
- 本轮结论：**暂不改主列表**

当前更强证据显示：

- 现有 PMC 全文证据明确表明系统核心围绕 `single-cell RNA-seq`、omics 数据分析、DEGs、通路富集和 disease-mechanism exploration。
- 尽管题名中有 `precision medicine`，但当前 primary object 仍更靠 omics / cell-state discovery，而不是临床治疗决策或患者级医学转化。

主控判断：

- `06 / 07` 边界压力存在，但现阶段保留在 `06.03` 更稳。
- 若后续发现更强的 clinical validation / therapeutic decision / patient-centered evidence，再重开 `07` 侧调整讨论。

当前建议：

- 保持 `to_read / 06.03`

补充说明：

- 本轮 reviewer 只读意见与主控判断一致：尽管题名带有 `precision medicine`，当前更强全文证据仍表明系统直接工作对象主要是 single-cell / omics / disease-mechanism discovery。

## 4. 本轮后对第一批样本的整体判断

### 4.1 当前最稳的结论

- `ASD-0004`：metadata 需要纠正，但主类 `01.04` 方向稳定
- `ASD-0033`：当前仍更稳在 `06.03`

### 4.2 当前仍最需要继续补强的结论

- `ASD-0006`：仍是 `06 / 07 / 01.04` 三向高压样本
- `ASD-0009`：方向不一定错，但 confirmed-core 强度仍偏弱

## 5.1 本轮 reviewer 交叉意见摘要

- `ASD-0004`：两侧意见一致支持保留 `01.04`，并优先做 canonical title / identity cleanup
- `ASD-0006`：reviewer 倾向更靠 `01.04`，但主控因全文仍不可得，暂不强改
- `ASD-0009`：reviewer 与主控一致，保留 `04.04`，但继续标记为 confirmed-core 强度偏弱
- `ASD-0033`：reviewer 与主控一致，当前继续保留 `06.03`

## 6. 本轮后基线

- confirmed included + classified count：`478`
- needs_review count：`0`
- confirmed `08` count：`3`

本轮没有因为 metadata 更正而改变 confirmed count。

## 7. 当前阶段结论

这批第一优先级样本并没有暴露出新的大规模一级类失稳问题。  
它们继续支持我们当前的总体判断：

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
