# ASD 结构化数据 Phase 5 第一轮执行记录

日期：2026-07-02

对应方案：

- `Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md`

本轮目标：

- 把面向协作者的简明 SOP 正式写入仓库
- 把 baseline 更新纪律正式写成可执行规则
- 对 PR 模板做最小但关键的 baseline 说明补强

## 1. 本轮新增产物

### 1.1 协作 SOP

新增：

- `Coverage_Check/structured_data_collaboration_sop_2026-07-02.md`

该文档面向实际协作者，按动作组织，而不是按原则组织。重点覆盖：

1. 新增论文
2. 改分类
3. 改 PDF 状态
4. 改 `note_path`
5. 重建 `Data/`
6. 提交 PR

### 1.2 baseline 更新规则

新增：

- `Coverage_Check/structured_data_baseline_update_rules_2026-07-02.md`

该文档把 baseline 更新从“原则要求”推进成“可执行规则”，明确了：

1. 什么算 baseline 更新
2. 什么不算 baseline 更新
3. baseline 更新只能从 authoritative pair 发起
4. baseline 更新必须由 Main Controller 收口
5. baseline 更新 PR 必须附带哪些证据包

### 1.3 PR 模板最小补强

更新：

- `.github/PULL_REQUEST_TEMPLATE.md`

本轮补入了：

1. `Baseline Impact` 区块
2. baseline 变更专用字段：
   - `old baseline`
   - `new baseline`
   - `approval by`
   - `snapshot id`
   - `canonical-only semantics reconfirmed`
3. `check_data_consistency.py` 输出模板中的：
   - `workflow mirror drift count`
   - `workflow mirror semantic drift count`
   - `workflow mirror order drift count`

## 2. 本轮解决的问题

在本轮之前，项目已经具备：

- authoritative pair 边界
- `export -> check -> build`
- CI guard
- PR 模板基础骨架

但仍缺少：

1. 新协作者可以直接照着操作的简明流程
2. baseline 更新何时成立、谁批准、要附什么证据的独立规则

本轮完成后，这两个缺口都已由正式文档覆盖。

## 3. 本轮形成的协作纪律

### 3.1 协作者的一句话工作法

> 先改 authoritative pair，再重建 Data；先分清 canonical 和 mirror，再做统计和审计。

### 3.2 baseline 更新的一句话纪律

> baseline 更新必须从 authoritative pair 发起，由 Main Controller 收口，并带着完整证据包进入 PR。

## 4. 本轮的最小治理增强

本轮没有新增复杂 CI 逻辑，也没有扩大 CODEOWNERS 范围。

原因是当前主缺口不在自动化守卫不足，而在：

1. 协作者如何判断自己在改哪一层
2. 协作者如何申报 baseline 更新
3. reviewer 如何快速看懂一次 baseline 变更

因此本轮采用的是：

- 文档先行
- PR 模板最小增强

而不是先加更复杂的 CI 阻断逻辑。

## 5. 本轮后的状态

到本轮结束时，Phase 5 已经完成了第一批正式产物：

1. 面向协作者的简明 SOP
2. baseline 更新规则
3. PR 模板中 baseline 影响的显式化

这意味着：

- 结构化数据协作已不再只依赖“知道原则的人”
- baseline 变更已经有了明确的申报与审查入口

## 6. 下一步建议

按当前总方案，下一步最合适继续推进的是：

1. 若需要，再给协作者补一份更短的“一页速查版”
2. 在协作规则稳定后，进入 Phase 6 的准备：
   - `note_revision_queue`
   - `full_text_followup_queue`
   - `representative_paper_pool`
   - `module_coverage_pool`
