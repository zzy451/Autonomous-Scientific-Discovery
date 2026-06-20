# 多 Agent 全库分类审计 Skill 预览稿

生成日期：`2026-06-18`  
用途：把本轮已经验证有效的全库分类复核流程沉淀为可复用 skill 预览稿，供后续正式写入本地 skill 时直接采用。

## 1. skill 目标

用于以下任务：

- 对 `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 做全库或大批次分类复核
- 系统性核查当前 confirmed core 是否存在误分类、误保留、误降级
- 重点清理：
  - `01.04 / 具体学科对象`
  - `01.04 / 11.07`
  - `03 / 04`
  - `05 / 10`
  - `06 / 07`
  - `08 / 06`
  - review / roadmap / benchmark / orchestration / protocol / copilot / AaaS / infrastructure-heavy records

## 2. 推荐 skill 名称

- `asd-full-library-classification-audit-workflow`

如果保留一个更简短的别名，也可以同时维护：

- `asd-batch-classification-audit`

## 3. 核心执行模式

### 3.1 默认不是一次把全库硬分给 4 个 Agent

已验证更合适的模式是：

- 以 `200` 条为一个 audit round
- 每个 round 由 `4` 个只读 reviewer 并行复核
- 主控代理统一裁决、改主列表、重算计数、写中文报告

### 3.2 推荐批次切法

- Round 1：`0001–0200`
- Round 2：`0201–0400`
- Round 3：`0401–0600`
- Round 4：`0601–0800`
- Round 5：`0801–end`

### 3.3 round 内 reviewer 切片

- `Reviewer-A`：前 `50`
- `Reviewer-B`：第二个 `50`
- `Reviewer-C`：第三个 `50`
- `Reviewer-D`：第四个 `50`

## 4. 子 Agent 硬规则

- 子 Agent 只读
- 子 Agent 不编辑 `agent_master_paper_list.md`
- 子 Agent 不写最终主列表结论
- 子 Agent 必须使用统一输出 schema
- 子 Agent 只负责自己负责的非重叠 ID 区间

## 5. reviewer 统一输出 schema

每条记录必须输出：

- `paper ID`
- `title`
- `current status`
- `current main class`
- `suggested status`
- `suggested main class`
- `Agent-inclusion evidence`
- `scientific-object evidence`
- `reason`
- `confidence`
- `full-text review required?`

建议优先用 markdown table；记录很多时可用 TSV。

## 6. 主控代理 merge 规则

### 6.1 可以直接写回主列表的情况

- 证据强
- 分类规则明确
- 与项目规则一致
- reviewer 结论没有实质冲突

### 6.2 不应直接强改主列表的情况

- 证据弱
- reviewer 分歧明显
- 依赖缺失全文
- 问题更像 taxonomy pressure，而不是单条误分

此类样本应进入中文审计报告，而不是直接改 canonical master list。

## 7. 当前已验证有效的高风险优先级

每轮优先看：

1. 当前在 `01.04` 的记录
2. 当前在 `11.07` 的记录
3. remarks 含以下关键词的记录：
   - `Strict review`
   - `moved from`
   - `boundary`
   - `review`
   - `roadmap`
   - `benchmark`
   - `framework`
   - `copilot`
   - `orchestration`
   - `AaaS`
4. 低覆盖与高压边界：
   - `08`
   - `08 / 06`
   - `05 / 10`
   - `03 / 04`
   - `01.04 / domain classes`
   - `01.04 / 11.07`

## 8. 建议固化进 skill 的硬判断句

- classify by final scientific research object, not by model, venue, benchmark framing, or claimed generality
- if a paper has a concrete scientific object, it should usually leave `01.04`
- scientific peer review, scientific publishing, scientific evaluation, and scientific knowledge production itself belong to `11.07`
- do not keep review, roadmap, benchmark, orchestration, protocol, copilot, or infrastructure papers in confirmed core unless they also function as primary Agent-system studies
- Earth-observation natural-process papers on mission platforms belong to `05`
- rover, spacecraft, or mission-science autonomy papers belong to `10`
- do not relax class `08` merely to balance counts
- only the main agent edits `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md`

## 9. 每轮必做输出

### 9.1 主列表侧

- 必要时改 `agent_master_paper_list.md`
- 重算：
  - confirmed included + classified count
  - `needs_review`
  - confirmed `08`
  - confirmed class distribution

### 9.2 报告侧

每轮写一份中文 batch report，至少包含：

- reviewed range
- baseline before the round
- landed master-list changes
- records reviewed but left unchanged
- boundary issue list
- post-round counts
- whether top-level taxonomy adjustment is supported

## 10. 全库复核后的最佳追加产物

除了 batch reports，建议再固定输出两类收口文档：

- 一份全库级总报告
- 一份 skill / workflow 预览稿

本项目当前已经形成这两类成果的实证模板，可直接继续沿用。

## 11. 当前流程结论

本轮实践已经证明，最合适的 Agent 模式不是“4 个 Agent 各管 200+ 篇直到结束”，而是：

- `200` 篇为一个 round
- 每 round `4` 个只读 reviewer
- 主控代理当轮收口
- 每轮结束立即关闭 reviewer
- 下一轮再重新开新 reviewer

这套模式兼顾了：

- 吞吐量
- 口径稳定性
- 可回滚性
- 主控裁决集中
- 对高风险边界进行逐轮复盘的能力
