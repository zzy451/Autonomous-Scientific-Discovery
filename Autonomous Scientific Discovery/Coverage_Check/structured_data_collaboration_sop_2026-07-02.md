# ASD 结构化数据协作简明 SOP

日期：2026-07-02

本文档面向会直接修改 `Autonomous Scientific Discovery` 仓库的协作者。目标不是重复讲治理原则，而是回答一个更具体的问题：

> 我现在要改一条记录，第一步改哪里，改完跑什么，哪些文件绝不能直接改？

本 SOP 对应：

- `Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md`
- `Coverage_Check/structured_data_baseline_update_rules_2026-07-02.md`
- `Data/README.md`
- `Data/field_dictionary.md`

## 1. 适用范围与红线

本 SOP 适用于以下协作动作：

1. 新增论文
2. 改分类
3. 改 PDF 状态
4. 改 `note_path`
5. 重建 `Data/`
6. 提交 PR

绝对红线：

1. 不要把 `Data/*.json*`、`*.csv`、`*.sqlite` 当事实层直接修改。
2. 不要把 `final_modules_or_bucket` 当正式分类事实。
3. 不要把 `primary_module_for_filing` 当完整分类事实。
4. 不要把 `pdf_path` 非空、note 写了“已核对”、或“看过全文”直接等同于“本地真 PDF 存在”。
5. 不要跳过 `export -> check -> build` 的再生顺序。

## 2. 先判断你在改哪一层

开始前，先判断你的动作属于哪一层：

- `agent_master_paper_list.md`
  负责 paper identity、inclusion status、canonical classification、`note_path`、remarks 等主数据。

- `multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
  负责 `pdf_status`、`pdf_path`、`evidence_status`、`note_status`、`master_status`、`final_modules_or_bucket`、`source_limited` 等 workflow / evidence 字段。

- `Data/`
  全部是派生层。只能通过脚本重建，不能反向充当事实层。

- `Notes/` / `Reference_PDF/`
  是 support / evidence 层，不是 authoritative pair。

一句话判断：

- 改 canonical classification、paper identity、note path：先看 master。
- 改 PDF / evidence / workflow 状态：先看 progress。
- 改统计、manifest、CSV、SQLite：先修 authoritative pair，再重建。

## 3. 六类高频动作速查表

| 动作 | 第一落点 | 常见伴随动作 | 禁止直接改 |
|---|---|---|---|
| 新增论文 | master | 视情况补 progress，再重建 Data | 直接手加 `papers.jsonl` / SQLite |
| 改分类 | master | 必要时同步 progress mirror，再重建 Data | 直接改 `paper_modules.csv` / SQLite |
| 改 PDF 状态 | progress | 必要时补本地 PDF 文件，再重建 Data | 直接改 `pdf_manifest.json` |
| 改 `note_path` | master | 真正移动 note 文件，再重建 Data | 只改 `note_manifest.json` |
| 重建 Data | 脚本链路 | `export -> check -> build` | 只跑 `build` |
| 提交 PR | git + PR 模板 | 填清 source-of-truth / baseline 影响 | 空着 baseline 说明硬提 |

## 4. 动作 A：新增论文

适用场景：

- 新增一篇尚未进入主表的 ASD 论文

执行顺序：

1. 在 `Paper_Lists/agent_master_paper_list.md` 中新增记录。
2. 分配新的稳定 `ASD-xxxx`。
3. 填入主数据字段：
   - `Paper title`
   - `DOI / arXiv / URL`
   - `Inclusion status`
   - canonical classification 相关字段
   - `Note path`
4. 如果已有 PDF / workflow 证据，再补 progress 行。
5. 运行：
   - `python "Autonomous Scientific Discovery/scripts/export_structured_data.py"`
   - `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
   - `python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"`

禁止做法：

- 先往 `Data/papers.jsonl` 里手加一条
- 先往 SQLite 里插一条

## 5. 动作 B：改分类

适用场景：

- 从单模块改为多模块
- 从多模块收回单模块
- 调整 `01.04` / formal module 边界

执行顺序：

1. 先改 `agent_master_paper_list.md` 中的 canonical classification 相关字段与 remarks。
2. 如果 progress 中的 `final_modules_or_bucket` 需要保留为 workflow mirror，则再判断是否应同步收平。
3. 运行：
   - `export`
   - `check`
   - `build`
4. 用以下命令 spot-check：
   - `query_analysis_db.py paper ASD-xxxx`
   - `query_analysis_db.py boundary-cases --limit 10`

判断提醒：

- `scientific_object_modules` / `general_method_bucket` 才是 canonical。
- `final_modules_or_bucket` 是 workflow mirror。
- `primary_module_for_filing` 只用于 filing / display。

## 6. 动作 C：改 PDF 状态

适用场景：

- 补到本地 PDF
- 发现原 PDF 丢失或不可读
- 更新 `evidence_status`
- 更新 `source_limited`

执行顺序：

1. 先改 progress 文件中的：
   - `pdf_status`
   - `pdf_path`
   - `evidence_status`
   - `source_limited`
2. 若新增本地 PDF，确保真实文件已放到对应路径。
3. 运行：
   - `export`
   - `check`
   - `build`
4. 用以下命令 spot-check：
   - `query_analysis_db.py missing-pdf`
   - `query_analysis_db.py module-pdf-coverage`

判断提醒：

- “本地真 PDF”必须同时满足：
  - progress 口径允许
  - 本地文件真实存在且可读

## 7. 动作 D：改 `note_path`

适用场景：

- note 改目录
- note 文件名调整

执行顺序：

1. 真正移动 note 文件。
2. 在 master 中更新 `Note path`。
3. 运行：
   - `export`
   - `check`
   - `build`
4. 用以下命令 spot-check：
   - `query_analysis_db.py paper ASD-xxxx`

禁止做法：

- 只改 `note_manifest.json`
- 只移动文件，不改 master

## 8. 动作 E：重建 `Data/`

固定顺序：

```text
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

不要只跑：

```text
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

最低通过标准：

- `check_data_consistency.py` 严格通过
- `workflow mirror drift count = 0`，或者若不为 `0`，必须在 PR 中明确解释

## 9. 动作 F：提交 PR

提交前必须确认：

1. 你改的是 authoritative pair，还是只改派生层 / 文档层。
2. 如果改了 authoritative pair，是否已完成 `export -> check -> build`。
3. 是否需要把这次改动声明为 baseline 更新。
4. PR 模板中的 source-of-truth、baseline、再生步骤、验证输出是否已填清。

如果这次改动涉及：

- `447 / 421 / 26`
- active ID 集
- `papers_jsonl_sha256`
- canonical classification 规则

则必须同时遵守：

- `structured_data_baseline_update_rules_2026-07-02.md`

## 10. 提交前 30 秒检查清单

提交前快速自检：

1. 我改的是 master、progress，还是只是派生层？
2. 我有没有误把 mirror 当 canonical？
3. 我有没有误把 `primary_module_for_filing` 当完整分类？
4. 我有没有误把 `pdf_path` 非空当真 PDF？
5. 我有没有按 `export -> check -> build` 顺序跑？
6. `check_data_consistency.py` 是否通过？
7. `git diff` 里有没有只改 `Data/` 却没改 authoritative pair 的奇怪情况？
8. PR 模板里是否明确写清了 source-of-truth / baseline 影响？

## 11. 常见误操作与纠正方式

误操作 1：
直接改 `Data/papers.jsonl`

纠正：
回到 master / progress 修事实层，再重建。

误操作 2：
把 `final_modules_or_bucket` 当正式分类

纠正：
先核对 master 中的 canonical classification 与 remarks，再决定是否同步收平 progress mirror。

误操作 3：
只跑 `build_analysis_db.py`

纠正：
重新按 `export -> check -> build` 完整跑一遍。

误操作 4：
只移动 note 文件，不改 master 的 `Note path`

纠正：
更新 master，再重建。

误操作 5：
补了 PDF 文件，但只改 manifest 没改 progress

纠正：
更新 progress 的 PDF / evidence 字段，再重建。

## 12. 一句话工作法

> 先改 authoritative pair，再重建 Data；先分清 canonical 和 mirror，再做统计和审计。
