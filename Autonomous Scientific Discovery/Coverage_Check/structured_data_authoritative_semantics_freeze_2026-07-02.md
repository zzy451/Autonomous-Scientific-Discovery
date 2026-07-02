# ASD structured-data authoritative semantics freeze

日期：2026-07-02

本文档对应 [structured_data_post_phase2_execution_plan_2026-07-02.md](/abs/path/C:/Users/20683/Desktop/综述/Autonomous%20Scientific%20Discovery/Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md) 中的 `Phase 3A`，用于把当前结构化体系从“能导出”推进到“正式可依赖”。

## 1. 冻结范围

本轮冻结的是结构化层的 authoritative 语义，而不是新增分类规则。分类规则本身仍以项目既有文档为准；这里解决的是：

1. 哪些字段属于 master ownership，哪些属于 progress ownership。
2. 哪些字段虽然 ownership 已明，但当前导出仍带有兼容性 fallback。
3. canonical classification 与 workflow mirror 的边界。
4. `pdf_status` / `pdf_path` / `evidence_status` / `source_limited` 这类工作流字段的正式解释。
5. 后续协作者遇到改类、补 PDF、改 note path、做统计时，第一落点到底在哪一层。

## 2. 冻结时点

当前冻结时点以 `Phase6FollowupR5` 结束后的机器可验证状态为准：

- active confirmed-core: `447`
- active local PDF: `421`
- active no-local-PDF: `26`
- canonical active `01.04` bucket: `9`
- workflow mirror semantic drift: `0`
- workflow mirror order drift: `0`

说明：

- 上面这组数字是本文件冻结字段语义时对应的历史时点，不是后续 live baseline 的唯一维护入口。
- 当前 live accepted baseline 应以 `structured_data_authoritative_acceptance_checklist_447_2026-07-02.md` 或其后继 dated acceptance checklist 为准。

## 3. Authoritative pair

当前结构化事实层只有两份文件：

1. `Paper_Lists/agent_master_paper_list.md`
2. `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

任何 `Data/`、CSV、SQLite、manifest、registry 文件都不是第三事实源。

## 4. Ownership and export-resolution freeze

这里冻结的不只是“谁拥有哪个字段”，还包括当前脚本真实执行时的导出优先级。因为在 row-level schema 还没完全迁移完成之前，少数字段是“主 ownership 明确，但导出允许回退”的状态。

| 字段 | 主 ownership | 当前导出解析规则 | 说明 |
|---|---|---|---|
| `paper_id` / 标题 / 作者 / 年份 / 来源 / DOI / URL | master | 直接读 master | 永久身份与元信息主记录 |
| `inclusion_status` | master | 直接读 master | confirmed-core 主线判断从这里起步 |
| `legacy_main_class` / `legacy_secondary_class` | master | 直接读 master | 只作 legacy filing / fallback lead |
| `note_path` | master 主 ownership | `progress.note_path or master.Note path` | 当前脚本允许 progress 临时覆盖；正式修改默认仍应先改 master |
| `pdf_path` | progress 主 ownership | `progress.pdf_path or master.PDF path` | 当前脚本允许从 master 旧列回退；正式修改默认先改 progress |
| `pdf_status` / `evidence_status` / `note_status` / `master_status` / `source_limited` / `batch` / `closed` | progress | 直接读 progress | workflow 状态字段 |
| `final_modules_or_bucket` | progress | 直接读 progress，再按分号拆分 | workflow mirror，不是 canonical fact |
| `scientific_object_modules` / `general_method_bucket` / `object_coverage_mode` / `primary_module_for_filing` | master remarks overlay | remarks 结构化 token 优先，再按 legacy fallback 归一化 | canonical structured classification |

### 4.1 Canonical classification derivation rule

当前 canonical classification 不是直接读单一列，而是按以下顺序导出：

1. 优先解析 master `Remarks` 中的结构化 token：
   - `scientific_object_modules=...`
   - `general_method_bucket=...`
   - `object_coverage_mode=...`
   - `primary_module_for_filing=...`
2. 若 remarks 未给出 `general_method_bucket`，且 legacy 行仍是 `Main class = 01` 且 `Secondary class = 01.04`，则把该记录归一化解释为独立 `01.04` bucket。
3. 若 remarks 未给出 formal modules，且当前 general bucket 为 `none`，再回退到 legacy `Main class` 作为 formal-module fallback。
4. `object_coverage_mode` 和 `primary_module_for_filing` 也按 remarks 优先、legacy/fact fallback 的顺序归一化。

这意味着：

- 协作者做正式分类修正时，默认应先改 master remarks overlay。
- legacy `Main class / Secondary class` 只是在 schema migration 未完成阶段保留的 fallback lead，不是默认 canonical 编辑入口。

### 4.2 Derived-only fields

以下属于派生解释，不能直接手改来“修事实”：

- `pdf_exists`
- `note_exists`
- `active_confirmed_core`
- registry assignments
- CSV / SQLite aggregates
- manifest counts

## 5. Canonical vs mirror freeze

### 5.1 Canonical classification

当前默认正式分类只认：

- `scientific_object_modules`
- `general_method_bucket`

也就是说：

- formal `01-11` 模块来自 `scientific_object_modules`
- 独立 `01.04` bucket 来自 `general_method_bucket`

### 5.2 Workflow mirror

`final_modules_or_bucket` 是 reaudit 过程中的 workflow mirror。

它的用途是：

- 记录当轮工作流收口状态
- 做 canonical-vs-mirror drift 审计
- 支撑 progress 追踪与 round closeout

它**不是** canonical classification fact source。

当前 mirror 语法冻结为：

- 底层来源：progress `final_modules_or_bucket`
- 解析方式：分号分隔列表
- 允许成员：formal `01-11`，以及可选的 `01.04`
- 顺序含义：保留并参与 `order_drift` 审计
- 默认统计规则：除非命令明确标为 audit / mirror，否则不得把它当 canonical source

### 5.3 `01.04` freeze

`01.04` 的正式冻结解释是：

- 可以出现在 `general_method_bucket`
- 可以出现在 taxonomy registry / index
- 不能进入 `scientific_object_modules`
- 在 canonical formal-module 统计里，不并入 `01-11`

## 6. Field semantics freeze

### 6.1 `scientific_object_modules`

- 类型：formal module array
- 合法值：`01-11`
- 允许多值
- 不允许出现 `01.04`

### 6.2 `general_method_bucket`

当前只允许：

- `none`
- `01.04_general_asd_methods_without_concrete_object_experiments`

输入归一化规则：

- bare `01.04` 可以作为输入写法被归一化接受
- 结构化导出层的 canonical 字面值统一写成 `01.04_general_asd_methods_without_concrete_object_experiments`

该字段非 `none` 时，`scientific_object_modules` 必须为空。

### 6.3 `object_coverage_mode`

当前只允许：

- `single_module`
- `multi_module`
- `general_method_without_concrete_object_experiments`

### 6.4 `primary_module_for_filing`

- 只用于 filing / display / directory convenience
- 不能压扁多模块 canonical fact
- 不能替代 `scientific_object_modules`
- 在当前 schema migration 未完成阶段，checker 允许它等于 canonical modules 之一，或等于 legacy `Main class`
- 上述宽松校验只反映迁移现实，不改变其“非 canonical fact”的角色

### 6.5 `final_modules_or_bucket`

- progress workflow mirror
- 用于 drift 审计和 round closeout
- 默认统计不得把它当 canonical fact source
- drift 审计需区分：
  - `semantic_drift`
  - `order_drift`
  - 可接受的 `01.04` mirror 保留

### 6.6 `pdf_path`

- 它只是 authoritative pair 中的路径字段
- `pdf_path` 非空不自动等于“本地真 PDF 已验证存在”
- 本地 PDF 真值必须结合：
  - `pdf_exists`
  - `pdf_manifest.json`
  - 实际文件可读取验证

### 6.7 `pdf_status`

- 这是 PDF 工作流状态字段
- 它描述的是归档/访问状态，不是单独的文件真值判定器
- 是否计入“active local PDF”最终仍以导出后真实文件存在且可读为准
- 当前冻结为 workflow label 字段，而不是正式闭集枚举规范

### 6.8 `evidence_status`

- 这是来源层级/取证路径字段
- 它描述一手来源到底到了全文、HTML、摘要、landing page、repo 还是其它受限来源
- 它不是简单的强弱分数，也不自动等于“本地 PDF 已有”
- 当前冻结为 workflow label 字段，而不是正式闭集枚举规范

### 6.9 `source_limited`

当前冻结为三态解释：

- `yes`：当前条目仍受来源或全文可得性限制
- `no`：当前条目不受此限制
- 空字符串：当前没有进入 progress 驱动工作流，不能对 active confirmed-core 作积极解释

当前导出会把该字段归一化为小写字符串：`yes` / `no` / `""`

## 7. 常见操作的第一落点

### 改分类

先改 master remarks 中的 canonical classification overlay，再重建派生层。

### 补 PDF

默认先改 progress 的 `pdf_status` / `pdf_path` / `evidence_status`，再重建派生层。

若旧 master `PDF path` 仍在回退链路中，不应把这种兼容性回退误解为 master 重新拥有 `pdf_path`。

### 改 note path

默认先改 master 中的 `Note path`，再重建派生层。

若当前 round 需要临时 workflow override，脚本允许 `progress.note_path` 覆盖导出；但这不改变 master 仍是 note path 的主 ownership。

### 做统计

默认从 canonical classification 出发，不默认从 `final_modules_or_bucket` 出发。

## 8. 本轮结论

自本文件起，项目内部关于 structured-data 的默认解释正式冻结为：

1. authoritative pair only
2. canonical classification 由 master remarks overlay 优先导出，legacy class 只作 fallback lead
3. `note_path` / `pdf_path` 当前要按 export-resolution 规则解释，而不是机械理解成单列硬 ownership
4. progress 写 PDF/evidence/workflow state
5. `01.04` 只在独立 bucket 中存在
6. `primary_module_for_filing` 只做 filing
7. `final_modules_or_bucket` 只做 mirror
8. `pdf_path` 非空不等于本地真 PDF
