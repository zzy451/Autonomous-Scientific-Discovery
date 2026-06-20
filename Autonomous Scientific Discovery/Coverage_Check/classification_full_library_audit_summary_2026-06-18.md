# 全库分类复核总报告：`ASD-0001`–`ASD-0871`

生成日期：`2026-06-18`  
审计模式：全库分类复核总收口  
审计范围：`Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 当前全部 `871` 条记录  
执行依据：

- `asd-literature-search-workflow`
- `asd-full-library-classification-audit-workflow`
- `Autonomous Scientific Discovery/review_scope_and_classification_policy.md`
- `Autonomous Scientific Discovery/domain_classification_rules.md`
- `Autonomous Scientific Discovery/science_domain_taxonomy.md`

说明：本报告不是替代 Round 1–5 的逐批次报告，而是把全库复核已经落地的结果、当前权威计数、主要边界压力点和后续建议统一收束到一个总入口，方便后续继续推进 confirmed core 精修与 skill 沉淀。

## 1. 当前主列表权威状态

- total records：`871`
- `to_read`：`478`
- `background_only`：`347`
- `excluded`：`46`
- `needs_review`：`0`
- confirmed included + classified：`478`
- confirmed `08` count：`3`

当前 confirmed class 分布：

- `01: 48`
- `02: 31`
- `03: 73`
- `04: 99`
- `05: 25`
- `06: 58`
- `07: 52`
- `08: 3`
- `09: 34`
- `10: 23`
- `11: 32`

## 2. 本轮全库复核已经完成的工作

### 2.1 批次复核已覆盖全库

已完成 5 轮批次复核并写出中文报告：

- [classification_batch_round1_0001_0200_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_batch_round1_0001_0200_2026-06-18.md>)
- [classification_batch_round2_0201_0400_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_batch_round2_0201_0400_2026-06-18.md>)
- [classification_batch_round3_0401_0600_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_batch_round3_0401_0600_2026-06-18.md>)
- [classification_batch_round4_0601_0800_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_batch_round4_0601_0800_2026-06-18.md>)
- [classification_batch_round5_0801_end_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_batch_round5_0801_end_2026-06-18.md>)

### 2.2 高风险 follow-up 已经完成多轮收口

本轮已额外完成若干专项 follow-up，重点压测：

- `01.04 / 11.07`
- `01.04 / 具体学科对象`
- `05 / 10`
- `08 / 06`
- SDL / orchestration / copilot / data-workflow / AaaS 类记录是否被误保留在 confirmed core

对应报告包括：

- [classification_followup_01dot04_and_11dot07_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_followup_01dot04_and_11dot07_2026-06-18.md>)
- [classification_followup_class10_lineage_cleanup_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_followup_class10_lineage_cleanup_2026-06-18.md>)
- [classification_followup_vesta_scider_2026-06-18.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_followup_vesta_scider_2026-06-18.md>)
- [classification_correction_round_2026-06-18_scienceearth_and_01dot04.md](</c:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Coverage_Check/classification_correction_round_2026-06-18_scienceearth_and_01dot04.md>)

## 3. 全库复核后的总体判断

### 3.1 一级类整体仍然稳定

经过全库 5 轮批次复核和多轮边界 follow-up，当前没有出现大规模“无法安放”的 confirmed core 样本，也没有出现明显要求重写 `01–11` 顶层主类的系统性反例。

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

### 3.2 当前最真实的问题不是顶层分类失效，而是 confirmed core 口径曾经偏宽

全库复核反复指向同一个问题：此前有一批 records 因为带有 Agent、workflow、orchestration、copilot、protocol、benchmark、scientific platform 等表述，被偏宽地保留在 confirmed core 中；但继续复核后发现，其中相当一部分更适合作为：

- `background_only`
- `11.07` 边界背景样本
- `01.04` 的 infrastructure / protocol / workflow substrate 边界样本

也就是说，问题主要不是“一级类设计错了”，而是“confirmed core 的收口需要更严”。

### 3.3 同时也存在少量被低估的真实 core paper

全库复核也发现了少量此前被保守放在 `background_only` 的记录，后续经过更强证据复核后被提升进 confirmed core。  
这说明当前系统不只是单向“过宽”，也有少量“过保守”的情况，但数量明显少于“偏宽保留”的情况。

## 4. 当前主要边界压力点

### 4.1 `01.04 / 具体学科对象`

这是当前最核心的压力源。  
硬规则仍然成立：

- 如果 paper 的 primary object 是 concrete scientific object，应优先离开 `01.04`
- 如果 paper 的 primary object 仍是 general scientific runtime、workflow substrate、protocol、research-team infrastructure、benchmark、domain-general scientific capability，则保留 `01.04`

当前最值得继续盯住的代表样本：

- `ASD-0844` `Science Earth`
- `ASD-0845` `SciDER`
- 若干 general research-team / protocol / orchestration / data-centric 系列 paper

### 4.2 `01.04 / 11.07`

当前规则已经比较稳定：

- general scientific capability platform / workflow / domain-general research agent -> `01.04`
- scientific peer review / publishing / scientific evaluation / scientific knowledge production itself -> `11.07`

当前代表样本：

- 稳定落在 `11.07`：`PaperOrchestra`、`Automating Scientific Evaluation`
- 已从 `01.04` 收口到 `11.07`：`OmniScientist`
- 稳定留在 `01.04`：`Science Earth`、`SciDER`

### 4.3 `03 / 04`

当前规则仍然有效，但仍需逐样本谨慎裁决：

- molecules / reactions / synthesis routes / catalysts -> `03`
- material composition / structure / phase / performance / device materials -> `04`

高压样本集中在：

- battery-materials / molecular-design
- MOF / COF / heterogeneous catalyst
- nanomaterials / chemistry synthesis vs materials object

### 4.4 `05 / 10`

当前硬规则已经在尾段样本中得到再次验证：

- mission-borne Earth natural-process monitoring -> `05`
- rover / spacecraft / mission-science autonomy -> `10`

当前最稳的验证组：

- `ASD-0852`–`ASD-0854`、`ASD-0858` -> `10`
- `ASD-0859`–`ASD-0861` -> `05`

### 4.5 `08 / 06`

这是低覆盖类最敏感的压力点。  
当前 confirmed `08` 只有 `3`，但复核后的判断是：

- 这更像真实稀缺，而不是一级类设计失败
- 不能因为 `08` 数量少就放宽标准

当前最稳的结论是：

- crop / breeding / food-science / agricultural production objects 才稳定归 `08`
- general plant / genomics / basic biological mechanism 不应为了补 `08` 被硬拉进去
- `ASD-0836` 这类 plant genomics agenda / review-style sample 保持 `background_only` 更稳

## 5. 本轮全库复核已经带来的净效果

### 5.1 `needs_review` 已清零

此前剩余的 `needs_review` 样本已经完成收口。当前主列表 `needs_review = 0`。

### 5.2 confirmed core 已从先前的 500 压缩到更可信的 478

这次全库复核没有追求数量维持，而是优先追求口径收紧与对象一致性。  
当前 `478` 更接近“经过结构化复核后仍能站住”的 confirmed core。

### 5.3 `08` 低覆盖被证实为真实稀缺，而不是简单漏分

多轮边界复核后，`08` 仍然只有 `3`。这不是坏结果，反而说明：

- 当前 Agent-only 纳入口径是严格且一致的
- 农业 / 食品方向真正满足当前标准的 core paper 目前确实少

## 6. 接下来的优先任务

### 6.1 继续做 confirmed core 的精修，而不是重新扩量

当前更优先的不是继续往上加 paper 数，而是继续精修现有 `478` 条 confirmed core，尤其是：

- `01.04` confirmed core 的高风险样本
- `03 / 04` 高压边界样本
- `11.07` 中 framework-heavy / evaluation-heavy 样本

### 6.2 为 confirmed core 补齐 note 覆盖与强证据复核

下一阶段可以把“分类正确但证据仍偏摘要级”的样本优先进入全文 note 阶段，尤其是：

- `Science Earth`
- `SciDER`
- `ASD-0811`
- 若干 `01.03 / 01.04` equation-discovery 邻近样本

### 6.3 把多 Agent 审计流程正式沉淀为可复用 skill

当前这套 `200` 篇一轮、`4` 个只读 reviewer、主控代理统一裁决的模式已经被验证可用，适合正式沉淀为项目内 skill。

## 7. 结论

当前全库复核已经完成了一个重要阶段性目标：  
不是单纯“看过了 871 条”，而是已经把主列表推进到一个更可信的、规则更一致的、边界解释更清楚的状态。

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
