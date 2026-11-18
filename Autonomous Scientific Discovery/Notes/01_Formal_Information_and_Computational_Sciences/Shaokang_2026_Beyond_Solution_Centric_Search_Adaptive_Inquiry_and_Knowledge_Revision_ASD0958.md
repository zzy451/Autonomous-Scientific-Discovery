# Beyond Solution-Centric Search: Adaptive Inquiry and Knowledge Revision for Autonomous ML Engineering

**论文信息**

- ID：ASD-0958
- 标题：Beyond Solution-Centric Search: Adaptive Inquiry and Knowledge Revision for Autonomous ML Engineering
- 作者：Fu, Shaokang; Tao, Yulong; Jin, Linbo; Zhao, Jiarong; Shi, Qiming; Pan, Tianjun; Li, Haonan; Wang, Chengyu; Wu, Jia; Huo, Chengfu
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.02143
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0958.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Shaokang_2026_Beyond_Solution_Centric_Search_Adaptive_Inquiry_and_Knowledge_Revision_ASD0958.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入核查：文章直接研究自动研究Agent或其基准。 | 纳入核查：文章直接研究自动研究Agent或其基准。 | TXT line 295；核验TXT行号 295 | Iris synthesizes observations across experiments into task knowledge composed | 高（一手正文；非独立复现） |
| 研究对象由正文任务或数据明确界定。 | 研究对象由正文任务或数据明确界定。 | TXT line 300；核验TXT行号 300 | 12-hour budget, the highest among compared systems. Across four tasks spanning | 高（一手正文；非独立复现） |
| 方法证据包括任务输入与迭代操作。 | 方法证据包括任务输入与迭代操作。 | TXT line 393；核验TXT行号 393 | preserve experiment records or validated successes for later use (Ji et al. 2026). Yet | 高（一手正文；非独立复现） |
| 验证设计含有对照、多次执行或独立评分。 | 验证设计含有对照、多次执行或独立评分。 | TXT line 443；核验TXT行号 443 | limitations in information acquisition and management. | 高（一手正文；非独立复现） |
| 正文报告了可核对结果或系统贡献。 | 正文报告了可核对结果或系统贡献。 | TXT line 556；核验TXT行号 556 | represent evidence across experiments as revisable task-level claims with | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出Iris，为多实验自动研究保留可修订的任务级知识，使过程持续通过信息获取和知识修订发展研究。它不将单次最高分当作唯一目标，而是基于连续实验建立跨实验主张和正反证据。实验在78项MLE-Bench任务外加四个其他研究任务。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文设定了明确的科学目标或评测问题。
  - 原文位置：TXT line 295；核验TXT行号 295；引文：Iris synthesizes observations across experiments into task knowledge composed
- 多步行动过程：yes。方法需要反复提案、执行和判读结果。
  - 原文位置：TXT line 412；核验TXT行号 412；引文：information management, Iris synthesizes observations from multiple experiments
- 至少一种Agent能力：yes。系统具有调用工具并根据反馈继续的Agent能力。
  - 原文位置：TXT line 443；核验TXT行号 443；引文：limitations in information acquisition and management.
- 明确科研流程角色：yes。系统在文中承担科研Agent的实验、研发或评价角色。
  - 原文位置：TXT line 1066；核验TXT行号 1066；引文：Once the evidence and summary sets have been extended, cross-experiment

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

论文任务包含ML工程实验，但研究中心是使Agent形成可更新的跨实验任务知识，仍为计算科学方法对01.02。

### 2.3 容易混淆的边界

论文任务包含ML工程实验，但研究中心是使Agent形成可更新的跨实验任务知识，仍为计算科学方法对01.02。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

语言模型Agent

### 3.2 科研流程角色

科研执行；实验评估

Beyond Solution-Centric Search: Adaptive Inquiry and Knowledge Revision for Autonomous ML Engineering?每次实验后提取观测、记录和验证成功形式的结果，组合为带范围和负面证据的任务知识；计划器在后续搜索时用知识选择有价值的实验或自适应信息采集，新证据反过来修订知识与正反向关系。

### 3.3 自主能力

系统具有调用工具并根据反馈继续的Agent能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

### 4.2 系统流程与组件

每次实验后提取观测、记录和验证成功形式的结果，组合为带范围和负面证据的任务知识；计划器在后续搜索时用知识选择有价值的实验或自适应信息采集，新证据反过来修订知识与正反向关系。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者在75项MLE-Bench任务、四个其他跨域任务上评测，包含用户独立任务和中间实验反馈；测量包含任务奖牌率和跨实验迁移表现。

### 5.2 基线、指标与结果

作者报告Iris在75件MLE-Bench任务的gold medal率为39.1%，高于比较系统；实验外任务也测试其知识是否转移。

### 5.3 科学贡献与证据强度

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文在自动研究Agent及长程轨迹研究的背景下与已有系统和评测基准比较，具体差异体现于上文所述的新监督、证据记忆或任务评价策略。

## 7. 局限性与风险

作者承认的局限以全文limitations段为准；读者风险：任务集和评分器不能代表全部真实研究环境，结果需按作者所设定的任务范围解读。

## 8. 对综述写作的价值

论文任务包含ML工程实验，但研究中心是使Agent形成可更新的跨实验任务知识，仍为计算科学方法对01.02。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出Iris，为多实验自动研究保留可修订的任务级知识，使过程持续通过信息获取和知识修订发展研究。它不将单次最高分当作唯一目标，而是基于连续实验建立跨实验主张和正反证据。实验在78项MLE-Bench任务外加四个其他研究任务。

### 9.2 速记版 pipeline

每次实验后提取观测、记录和验证成功形式的结果，组合为带范围和负面证据的任务知识；计划器在后续搜索时用知识选择有价值的实验或自适应信息采集，新证据反过来修订知识与正反向关系。

### 9.3 标注字段汇总

```text
paper_id=ASD-0958
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | MLE-Bench及其他跨域任务为预定义基准集合 | “在75项MLE-Bench任务、四个其他跨域任务上评测” · L101 |
| 验证强度 | V1 基准/内部评测 | 基准得分和gold medal率评估，无独立复现 | “包含用户独立任务和中间实验反馈；测量包含任务奖牌率和跨实验迁移表现” · L101 |
| 系统自主性 | L2 闭环执行者 | 系统自主保留和修订跨实验知识并迭代多次实验 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
