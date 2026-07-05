# ASD 下一步数据编码方案复核

日期：2026-07-05  
执行方式：controller-executed approximate multi-agent review  
说明：当前会话未暴露真实子 Agent 启动接口，因此本次为诚实的近似多 Agent 方案复核，而非真实外部 Agent 讨论回包。

## 1. 复核目标

复核“下一步是否需要把论文分类进一步形式化为可长期维护、可分析、可增删改查的层级数据结构”，并回答：

1. 现有仓库是否已经具备数据库化基础；
2. 学长提出的“分类数组 + 唯一身份号 + 分类 index 对应 + GitHub 管理”里，哪些已经完成；
3. 下一步最值得做的具体动作是什么；
4. 哪些设计如果直接硬改，会引入不必要返工。

## 2. 近似多 Agent 角色

### `Architecture-Reviewer`

关注主键设计、层级编码、数据模型稳定性。

结论：

- 当前永久主键已经存在：`ASD-xxxx`
- 当前主键已贯穿：
  - `agent_master_paper_list.md`
  - `multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
  - `Notes/`
  - `Data/papers.jsonl`
  - `Data/papers.sqlite`
  - `Data/registry/*`
- 因此**不应**把现有永久主键整体替换成类似 `0101abc` 的学科编码主键
- 更稳妥的方案是：
  - 保留 `ASD-xxxx` 作为永久 paper identity
  - 新增一个“学科排架 / 管理码”作为二级键，例如 `discipline_local_code`
- 这个二级键服务于：
  - GitHub 目录管理
  - 学科顺序展示
  - 表格导出
  - 章节写作排架
- 它不应反过来承担事实层唯一主键职责

### `Data-Governance-Reviewer`

关注 authoritative pair、派生层纪律、字段 ownership。

结论：

- 现有 structured-data 底座已经满足“形式化保存分类”的主体要求：
  - `scientific_object_modules` 已是数组
  - `general_method_bucket` 已单独结构化
  - `primary_module_for_filing` 已单独结构化
  - `classification_assignments.jsonl` 已是 exploded assignment 表
  - `papers.sqlite` 已支持数据库查询
- 当前已存在的 index / registry 包括：
  - `Data/taxonomy_index.json`
  - `Data/registry/paper_registry.jsonl`
  - `Data/registry/classification_assignments.jsonl`
  - `Data/registry/paper_identifier_aliases.jsonl`
- 因此下一步**不是重建数据库**，而是**在现有底座上补一层更显式的层级学科编码导出**
- 这层新增内容必须继续保持：
  - authoritative facts 仍只来自 master + progress
  - 新编码文件属于 derived layer
  - 不能反向手改编码导出层来修事实

### `Analysis-Reviewer`

关注后续统计、图表、SQL、数组查询和二级学科分析。

结论：

- 学长的需求里，真正对后续分析最有价值的，不是“重新命名主 ID”，而是：
  1. 给每篇论文一个稳定的层级学科管理码；
  2. 给一级 / 二级分类建立正式 code-to-label index；
  3. 让 SQLite / JSONL / CSV 都能直接导出这一层；
  4. 让后续统计能区分：
     - 永久主键 `ASD-xxxx`
     - 一级 formal module 数组
     - 二级学科排架码
- 当前最明显的空缺是：
  - 现有 `scientific_object_modules` 只显式结构化到一级 `01-11`
  - 二级层目前主要还体现在 legacy `Main class / Secondary class` 和 note 语义里
- 因此下一步最值得做的是：
  - 把“二级学科排架层”从隐含状态变成正式导出层

## 3. 当前已完成的部分

下面这些，其实已经有了：

### 3.1 唯一身份号

- 已完成：`ASD-xxxx`
- 这是永久 paper ID
- 适合继续作为数据库主键

### 3.2 分类数组保存

- 已完成：`scientific_object_modules`
- 已保存于：
  - `Data/papers.jsonl`
  - `Data/registry/paper_registry.jsonl`
  - `Data/registry/classification_assignments.jsonl`
  - `Data/papers.sqlite`

### 3.3 数据库 / 可查询层

- 已完成：`Data/papers.sqlite`
- 已具备查询脚本：`scripts/query_analysis_db.py`

### 3.4 一级分类 index

- 已基本完成：`Data/taxonomy_index.json`
- 但它目前主要覆盖：
  - formal `01-11`
  - separate `01.04`
- 还没有把“一级 + 二级学科排架映射”完整单独抽出来

## 4. 当前真正缺的部分

### 4.1 显式二级学科编码层

目前缺：

- 一个正式的“二级学科 code registry”
- 一个正式的“每篇论文对应哪个二级学科排架码”的导出表

### 4.2 学科管理码

目前缺：

- 类似 `04-03-001` 这种“排架 / 管理用二级码”

建议不要直接使用 `0101abc` 这种不带分隔的紧凑串作为唯一设计，因为：

- 可读性差
- 多模块论文会立刻出现歧义
- 与现有 `ASD-xxxx` 主键体系冲突
- 后续改类时迁移成本高

更好的形式是：

- `discipline_local_code = 04-03-001`
- 含义：
  - `04`：一级正式模块
  - `03`：二级学科排架位
  - `001`：该排架位下的顺序号

### 4.3 二级 index 对应表

目前缺：

- “数字到分类名”的一级+二级双层对应
- “分类名到数字”的逆向对应

## 5. 推荐的下一步方案

## 5.1 总原则

下一步不是重建系统，而是给现有系统**补一层层级学科排架编码导出层**。

保持三层分离：

1. 永久事实主键：`ASD-xxxx`
2. 正式对象分类事实：`scientific_object_modules` / `general_method_bucket`
3. 排架 / 管理 / 展示编码：`discipline_local_code`

## 5.2 建议新增字段

建议新增 derived 字段：

- `primary_taxonomy_code_2lvl`
  - 示例：`04.03`
- `discipline_local_code`
  - 示例：`04-03-001`
- `discipline_local_rank`
  - 示例：`001`

说明：

- `primary_taxonomy_code_2lvl` 是学科位
- `discipline_local_code` 是面向管理和排架的组合码
- 它们都不替代 `ASD-xxxx`

## 5.3 建议新增导出文件

建议新增：

- `Data/classification_code_index.json`
  - 保存一级、二级 code-to-label / label-to-code 对应
- `Data/discipline_local_code_registry.jsonl`
  - 每篇论文一行，保存 `paper_id` 与 `discipline_local_code` 对应
- `Data/discipline_local_code_registry.csv`
  - 方便人工审查和表格使用

## 5.4 建议新增 SQLite 表 / 视图

建议在 `papers.sqlite` 中新增：

- `discipline_local_code_registry`
- 或等价 view

最少字段：

- `paper_id`
- `discipline_local_code`
- `primary_module_for_filing`
- `legacy_secondary_class`
- `title`
- `note_path`
- `pdf_path`
- `active_confirmed_core`

## 5.5 编码生成规则建议

推荐规则：

1. 继续用 `ASD-xxxx` 作为永久主键
2. 用 `primary_module_for_filing` 作为一级排架主入口
3. 用 `legacy_secondary_class` 作为当前二级位的初始来源
4. 在每个二级位内部按当前稳定行序分配 `001`、`002`、`003`……

例如：

- `04` + `04.03` + 本位第 `001` 篇
- 导出为：`04-03-001`

注意：

- 多模块论文只生成一个排架管理码
- 这个排架管理码跟随 `primary_module_for_filing` 走
- 多模块事实仍然只保留在 canonical 数组里，不要被管理码覆盖

## 6. 当前不建议立刻做的事

### 6.1 不建议重写全部 PDF / note 文件名

原因：

- 风险高
- Git 历史会变脏
- 当前主线收益低

### 6.2 不建议废弃 `ASD-xxxx`

原因：

- 已经是稳定永久主键
- 重构成本极高
- 没有分析收益

### 6.3 不建议现在就把二级分类事实全面 canonical 化进 authoritative pair

原因：

- 当前 authoritative pair 的 canonical 层已经围绕一级 formal module + `01.04` 稳定
- 二级层可以先作为 derived registry / analysis layer 落地
- 等写作和分析真正需要时，再决定是否升级为更强事实层字段

## 7. 下一步最具体的动作

下一步最值得做的是一个小而稳的实现轮：

1. 设计并冻结 `discipline_local_code` 规则
2. 从现有 `primary_module_for_filing + legacy_secondary_class` 生成二级排架码
3. 新增：
   - `classification_code_index.json`
   - `discipline_local_code_registry.jsonl`
   - `discipline_local_code_registry.csv`
4. 把这层接入 `papers.sqlite`
5. 跑：
   - `export`
   - `check`
   - `build`
6. 提交 git

## 8. 一句话结论

**我们下一步不该重建数据库；我们该在现有 `ASD-xxxx + classification arrays + SQLite` 底座上，补一层“一级/二级学科排架编码层”，把学长想要的分类管理逻辑正式导出成 index + registry。**
