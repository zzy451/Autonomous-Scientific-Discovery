# ASD 结构化数据 baseline 更新规则

日期：2026-07-02

本文档用于把 Phase 5 中的 baseline 变更纪律写成一套可执行、可审计、可在 PR 中落地的规则。

对应文件：

- `Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md`
- `Coverage_Check/structured_data_authoritative_acceptance_snapshot_2026-07-02.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/structured-data-guard.yml`

## 1. 什么是 baseline

当前结构化数据 baseline 至少包括以下内容：

1. active confirmed-core 数量
2. active local PDF 数量
3. active no-local-PDF 数量
4. active no-local-PDF 的 ID 集
5. 当前 canonical classification 规则
6. 当前快照身份
   - `schema_version`
   - `papers_jsonl_sha256`
7. 当前 workflow mirror drift 状态

当前已验收 baseline 的代表性例子：

- `447 / 421 / 26`

## 2. 什么算 baseline 更新

以下情况属于 baseline 更新：

1. `447 / 421 / 26` 中任一数字发生变化
2. active confirmed-core 集合或 active no-local-PDF ID 集发生变化
3. canonical classification 规则发生变化，导致正式统计口径变化
4. authoritative pair 的语义变化导致重新生成的快照身份发生实质变化
5. `workflow mirror drift` 不再只是清理顺序问题，而是伴随 canonical / authoritative 语义变化

以下情况通常不算 baseline 更新：

1. 纯文档润色
2. 纯 CLI 帮助文本调整
3. 纯 CI 文案说明更新
4. workflow mirror 的顺序清理，且不影响 authoritative baseline 数字
5. 仅仅把已有 canonical 事实更清晰地展示出来，但不改变 baseline 结果

## 3. baseline 更新的权限与角色

baseline 更新必须由 Main Controller 收口。

角色边界：

- Main Controller
  - 唯一可以最终落地 baseline 更新
  - 唯一可以修改 authoritative pair 并宣布 baseline 已更新
  - 唯一可以决定本次变更是否属于 baseline 更新

- 子 Agent
  - 只读审查
  - 只读取证
  - 只读 spot-check
  - 不直接改 master / progress / baseline 文档

## 4. baseline 更新必须从哪里发起

baseline 更新只能从 authoritative pair 发起：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

不得从以下位置反推修复 baseline：

- `Data/papers.jsonl`
- `Data/*.csv`
- `Data/*.sqlite`
- registry 层
- manifest 层

一句话：

> baseline 只能先改事实层，不能先改派生层。

## 5. baseline 更新的固定流程

如果你确认这次改动属于 baseline 更新，固定流程如下：

1. 先在 authoritative pair 中落地事实变化。
2. 运行：
   - `python "Autonomous Scientific Discovery/scripts/export_structured_data.py"`
   - `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
   - `python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"`
3. 运行：
   - `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary`
4. 生成或更新相应的 baseline / acceptance 记录。
5. 在 PR 中显式说明这是 baseline 更新。

## 6. baseline 更新 PR 必须附带的证据包

每次 baseline 更新 PR，至少要附带以下信息：

1. `old baseline`
2. `new baseline`
3. 变更原因
4. 受影响的 authoritative 字段
5. `check_data_consistency.py` 关键输出
6. `query_analysis_db.py summary` 关键输出
7. 新快照身份：
   - `schema_version`
   - `papers_jsonl_sha256`
8. `workflow mirror drift` 是否为 `0`
   - 若不为 `0`，必须解释
9. 谁批准本次 baseline 更新

## 7. baseline 更新时必须同步的文档

baseline 更新不应只改数据，不改说明。

至少要同步检查以下文档是否需要更新：

1. 最新 acceptance / baseline 记录
2. 与 baseline 数字直接绑定的治理文档
3. 若规则变化，相关 SOP / 规则文档

如果 baseline 已变，但说明文档还停留在旧值，则该 PR 不算完成。

## 8. baseline 更新 PR 的范围要求

baseline 更新 PR 应尽量保持单主题。

推荐做法：

- 只做 baseline 更新及其必要再生
- 同步更新必要验收记录
- 不把无关脚本重构、样式调整、治理文档杂项和 baseline 更新混提

如果一个 PR 同时包含：

- baseline 更新
- 无关 CLI 大改
- 无关文档重写

则审查风险会显著上升，不推荐。

## 9. 审查重点

baseline 更新 PR 的 reviewer 至少应检查：

1. 是否从 authoritative pair 发起
2. 是否误把派生层当事实层
3. canonical / mirror 边界是否仍然正确
4. `01.04` 是否仍独立，不并入 formal `01-11`
5. PDF 证据口径是否仍与本地真实文件一致
6. active 集合变化是否合理
7. baseline 数字变化是否有足够证据支持

## 10. 不完整 baseline PR 的处理

如果 CI 通过，但以下内容缺失：

- baseline 旧值 / 新值说明
- 批准人
- 快照身份
- drift 状态解释

则该 PR 仍视为流程不完整，不应合并。

## 11. 回滚规则

如果 baseline 更新已合并后发现口径错误：

1. 回滚仍应从 authoritative pair 发起
2. 重新执行 `export -> check -> build`
3. 留下新的日期化回滚 / 更正记录

不要直接手改 `Data/` 来“补救”。

## 12. 记录规则

每次 baseline 更新，都应留下一个可追溯的日期化记录，至少回答：

1. 谁批准
2. 为什么改
3. 改了什么
4. 旧 baseline 是什么
5. 新 baseline 是什么
6. 快照身份是什么
7. drift 状态是什么

## 13. 一句话纪律

> baseline 更新必须从 authoritative pair 发起，由 Main Controller 收口，并带着完整证据包进入 PR。
