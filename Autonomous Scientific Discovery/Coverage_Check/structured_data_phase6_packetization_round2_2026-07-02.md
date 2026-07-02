# ASD 结构化数据 Phase 6 第二轮执行记录

日期：2026-07-02

对应方案：

- `Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md`

本轮目标：

- 把上一轮生成的 Phase 6 队列进一步切成可直接分发的首轮任务包
- 同时给写作支持侧确定首轮优先模块包

## 1. 本轮新增产物

### 1.1 follow-up 首轮切片

新增：

- `Coverage_Check/structured_data_phase6_followup_round1_slice_A_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_slice_B_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_slice_C_447_2026-07-02.tsv`

这三份 slice 都来自：

- `structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`

并按首轮 `3 x 10` 的 evidence-agent 切片结构生成。

### 1.2 写作支持首轮包

新增：

- `Coverage_Check/structured_data_phase6_writing_support_round1_modules_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_writing_support_round1_representatives_447_2026-07-02.tsv`

当前首轮写作支持优先模块为：

- `04`
- `03`
- `07`
- `09`
- `02`

### 1.3 packet 计划文档

新增：

- `Coverage_Check/structured_data_phase6_followup_round1_plan_447_2026-07-02.md`

该文档说明了：

1. 为什么首轮先取 `30` 篇而不是全量 `137` 篇
2. A / B / C 三个 evidence slice 的任务定位
3. 为什么写作支持先聚焦 `04/03/07/06/05`

### 1.4 packet 生成脚本

新增：

- `scripts/generate_phase6_round1_packets.py`

该脚本将队列层进一步转换为：

1. 可分发的 follow-up slice
2. 可分发的写作支持模块包

## 2. 本轮切片策略

### 2.1 follow-up 首轮为什么先做 30 篇

首轮不做全量 `137` 条 follow-up，而只取前 `30` 条，原因是：

1. 前 `30` 条已经覆盖了最高压力区域
   - `no local PDF`
   - `source_limited=yes`
   - non-full-text evidence
2. 这 `30` 条里包含了整个 `26` 条无本地 PDF 前沿，以及最先进入的 `4` 条本地有 PDF 但仍强 source-limited 的记录
3. 这样既能高效并行，又不会把 Main Controller 的合并审查压力一次性推得过大

### 2.2 A / B / C 三个 slice 的定位

- `A`
  - 最前沿高压 mixed chemistry / materials / bio 记录
- `B`
  - 剩余 no-local-PDF 前沿，延伸到 `05/06/07/10/11`
- `C`
  - no-local-PDF 尾部加首批 local-PDF 但 source-limited 的记录，兼顾 `01.04 / 01 / 02 / 03` 边界

## 3. 本轮写作支持侧结论

首轮写作支持不追求模块全覆盖，而优先服务正文主体和交叉边界：

- `04 Materials Science`
- `03 Chemical Sciences`
- `07 Medical and Health Sciences`
- `09 Engineering and Industrial Technology Sciences`
- `02 Physics, Astronomy and Cosmic Sciences`

原因是：

1. `04/03/07` 体量大，且 representative candidates 已经足够稳定
2. `09/02` 虽然体量略小，但 PDF 覆盖 `100%`，source-limited 压力很低，更适合首轮快速形成“可直接落稿”的模块包模板
3. `06/05` 依然重要，但 source-limited 压力更高，更适合作为后续第二波写作支持包

## 4. 本轮的性质

本轮仍属于 Phase 6 的准备与 packetization，不属于：

- authoritative pair 改写
- note writeback
- master/progress closeout

也就是说，本轮产物是：

- coordination assets
- launch packets
- writing-support packets

而不是最终事实更新。

## 5. 下一步建议

按当前阶段，下一步最合适有两个方向：

1. 真的发出 `Phase6FollowupR1` 的 Evidence-Agent A/B/C 任务包，开始首轮并行收证
2. 将 `writing_support_round1` 中的 `04/03/07/06/05` 模块进一步拆成章节写作支持包
