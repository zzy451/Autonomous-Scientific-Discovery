# 数据要求、来源与版本

## 复现当前图实际需要什么

不需要下载论文全文，不需要 API Key，也不需要重新检索、用关键词分类或调用 LLM。本目录已经包含全部必需的最小输入。

| 文件 | 内容与去重单位 | 用途 |
|---|---|---|
| `data/population.csv` | 1,492个唯一记录编号、记录类型及来源语料 | 固定取样范围：1,114研究论文＋378其他条目 |
| `data/field_memberships.csv` | 1,981个唯一“记录编号—一级领域”对 | 重算11领域显示数量及精确领域组合 |
| `data/tertiary_memberships.csv` | 2,073个唯一“记录编号—正式三级代码”对 | 重算三级类记录数及研究论文数 |
| `data/tertiary_vocabulary.csv` | 350个正式三级类及其父类、中文名 | 校验标签与类别层级 |
| `inputs/fields.csv` | 11领域中英文名称、显示数量、历史版式参考数量、色值 | 固定领域标注和已有版式 |
| `inputs/themes.csv` | 每领域前四类，共44行，含中英文名称和计数 | 主题峰和标签 |
| `inputs/selected_seas.csv` | 11个选定精确组合、数量及几何参数 | 共享海域 |
| `inputs/parameters.json` | 随机种子、板块中心、网格数和主题峰偏移 | 确定性空间布局 |

`recount.py` 从记录级数据重新计算领域数量、全部三级类频次、每领域前四及11个海域，逐项核验与绘图输入一致。排序依据：全部记录数降序；并列时研究论文数降序；再次并列时三级代码升序。同一记录在同一类别仅计一次，但可有多个类别。

三条记录位于独立通用方法桶，不进入11个正式领域；有正式领域标签的记录为1,489条。只有明确登记的有效三级标签才计入主题峰；不把父类展开为子类，不补猜缺失标签。三级层级的缺失情况见 `data/field_tertiary_coverage.csv`。

## 原始资料在仓库中的位置

仓库是 [zzy451/Autonomous-Scientific-Discovery](https://github.com/zzy451/Autonomous-Scientific-Discovery)。以下为原始数据的逻辑路径：

| 原始资料 | 路径 |
|---|---|
| 广义 AI4S 主表 | `AI_Science_Literature/Paper_Lists/ai_science_master_paper_list.md` |
| Agent 主表 | `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` |
| 各模块的正式分类登记 | `Autonomous Scientific Discovery/Data/paper_module_taxonomy_assignments.jsonl` |
| 分类代码索引 | `Autonomous Scientific Discovery/Data/classification_code_index.json` |
| 正式领域分类树 | `Autonomous Scientific Discovery/science_domain_taxonomy.md` |

**不能把当前远程主分支当成这张图的完整历史输入。** 打包时远程主分支基点为 `60f8bad0e5f9be96fc24ae75f0cfdbbe26a51cc8`；本图采用本地2026-11-17的1,492条快照，两者存在版本差异。其中广义 AI4S 主表不在该远程基点中，其余相关文件也不与本图来源哈希相同。本包因此附带最小的冻结记录—分类快照，避免依赖失效链接或尚未同步的工作区。

逐文件来源 SHA-256、逻辑路径以及是否存在/匹配远程基点，见 `data/source_provenance.json`。其中本地历史提交编号只作来源追踪，**不是下载依赖**；无需取得该提交即可复现。

完整题名、正文、笔记和引用元数据不参与本图渲染，不重复附在本包。如果将来需要重新判断分类，应回到原始主表和分类登记；不能把这个绘图快照反向当成新的分类事实所有者。

## 11个精确共享海域

| 成员领域 | 去重记录数 |
|---|---:|
| 生命科学—医学健康 | 100 |
| 化学—材料 | 39 |
| 化学—医学健康 | 35 |
| 材料—工程制造 | 14 |
| 地球与环境—航空交通 | 14 |
| 物理与天文—工程制造 | 13 |
| 形式与计算—物理与天文 | 12 |
| 形式与计算—工程制造 | 11 |
| 形式与计算—社会知识 | 11 |
| 形式与计算—物理与天文—工程制造 | 6 |
| 化学—材料—生命科学 | 5 |

“精确”指完整的一级标签集合恰好等于表中成员；同时拥有第三领域标签的记录不会再进入二领域海域。这里只展示选定的11种组合，并非全部跨领域组合。

## 图形计数与布局参数分离

`display_records` 是2026-11-17实际重算的领域数量；`layout_reference_records` 是为保留已定稿地形和海域位置而冻结的旧版布局参考量。两者用途不同，不能直接互相替换。板块采用面积响应指数0.35并有定向边界修形，因此面积用于表现相对规模，不是严格线性面积统计图。详见 `METHODS.md`。
