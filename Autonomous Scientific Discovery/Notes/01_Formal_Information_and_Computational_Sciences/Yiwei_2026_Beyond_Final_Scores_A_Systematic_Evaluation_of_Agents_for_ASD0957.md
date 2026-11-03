# Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development

**论文信息**

- ID：ASD-0957
- 标题：Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development
- 作者：Li, Yiwei; Yang, Wanli; Tan, Hexiang; Huang, Xiangzhou; Chen, Zhengyu; Li, Ziran; Chen, Borun; Lei, Shanglin; Zhu, Huaisheng; Tian, Hao; Sun, Fei; Cai, Xunliang; Wang, Jingang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.13417
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0957.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Yiwei_2026_Beyond_Final_Scores_A_Systematic_Evaluation_of_Agents_for_ASD0957.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入核查：文章直接研究自动研究Agent或其基准。 | 纳入核查：文章直接研究自动研究Agent或其基准。 | TXT line 560；核验TXT行号 560 | Our evaluation focuses on four workload families that capture distinct demands of automated research: Model Development, System Optimization, Puzzle & Challenge, and CUDA. | 高（一手正文；非独立复现） |
| 研究对象由正文任务或数据明确界定。 | 研究对象由正文任务或数据明确界定。 | TXT line 562；核验TXT行号 562 | Each task provides an objective, a correct but deliberately suboptimal starting artifact, an expert-written reference solution, a wall-clock budget, and an automated verifier. | 高（一手正文；非独立复现） |
| 方法证据包括任务输入与迭代操作。 | 方法证据包括任务输入与迭代操作。 | TXT line 581；核验TXT行号 581 | For the main cross-model comparison, all models use Claude Code (v2.1.152) as a practical shared harness, thereby holding the tool interface and iteration policy fixed. | 高（一手正文；非独立复现） |
| 验证设计含有对照、多次执行或独立评分。 | 验证设计含有对照、多次执行或独立评分。 | TXT line 695；核验TXT行号 695 | Unlike conventional one-shot tasks that provide feedback only on the final output, the iterative research tasks studied here expose explicit verifier feedback at each evaluated checkpoint. These step-level signals provide direct evidence of progress and failure, allowing us to evaluate the research process without relying on subjective model judgments. We therefore compute all three scores deterministically from recorded evaluation signals, as detailed below. The resulting metrics are reproducible and auditable. | 高（一手正文；非独立复现） |
| 正文报告了可核对结果或系统贡献。 | 正文报告了可核对结果或系统贡献。 | TXT line 715；核验TXT行号 715 | At each non-initial evaluated checkpoint, a delivery gate first checks whether the artifact runs and, when the task provides a correctness verdict, whether it is correct. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文用四个工作负载族、36项专家编制任务系统比较多个最新模型执行长程自动研究的能力。分析不止结果分数，还评估方法定义、执行可靠性、进度反馈、经验利用和系统工具层。作者结论称当前系统已实现部分研究闭环，而不是稳健的自我提升研究者。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文设定了明确的科学目标或评测问题。
  - 原文位置：TXT line 563；核验TXT行号 563；引文：Within the allotted budget, the agent iteratively improves the artifact, and the verifier scores the final submission relative to the starting artifact and expert reference on a normalized scale from 00 to 11.
- 多步行动过程：yes。方法需要反复提案、执行和判读结果。
  - 原文位置：TXT line 695；核验TXT行号 695；引文：Unlike conventional one-shot tasks that provide feedback only on the final output, the iterative research tasks studied here expose explicit verifier feedback at each evaluated checkpoint. These step-level signals provide direct evidence of progress and failure, allowing us to evaluate the research process without relying on subjective model judgments. We therefore compute all three scores deterministically from recorded evaluation signals, as detailed below. The resulting metrics are reproducible and auditable.
- 至少一种Agent能力：yes。系统具有调用工具并根据反馈继续的Agent能力。
  - 原文位置：TXT line 761；核验TXT行号 761；引文：Opus-4.7 leads outcome at 0.739, C1 at 0.612, and C2 at 0.967, while also placing third on C3 at 0.920. C2 is the most compressed dimension, ranging from 0.880 to 0.967, because successful delivery is common across the evaluated models. C1 ranges from 0.473 to 0.612, while C3 ranges from 0.772 to 0.928. The broader variation in C1 and C3 reveals differences that delivery success alone cannot explain.
- 明确科研流程角色：yes。系统在文中承担科研Agent的实验、研发或评价角色。
  - 原文位置：TXT line 769；核验TXT行号 769；引文：GPT-5.5 and Gemini-3.1-Pro provide the clearest comparison between models with similar outcomes. Their outcomes are 0.663 and 0.652, and both score 0.555 on C1, indicating nearly identical observed progress in solution framing. Their later capabilities differ sharply. GPT-5.5 reaches 0.958 on C2 but 0.858 on C3, whereas Gemini-3.1-Pro reaches 0.889 on C2 but 0.920 on C3. Similar outcomes and framing quality can therefore arise from different balances between reliable implementation and feedback control.

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

任务覆盖AI工程、挑战和CUDA算法，但本文是对AI科研Agent的通用评估，没有专业领域科学结果，归入01.02。

### 2.3 容易混淆的边界

任务覆盖AI工程、挑战和CUDA算法，但本文是对AI科研Agent的通用评估，没有专业领域科学结果，归入01.02。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

语言模型Agent

### 3.2 科研流程角色

科研执行；实验评估

Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development?每任务给定一个正确但次优的起始产物、参考解和运行预算，Agent在共同Claude Code工具环境中修改并执行多次。评估器通过验证器对每个提交点评分，并分析规划、结果执行、反馈控制和回退。三次独立运行测个任务，亦使用重启对比检查系统是否从旧经验获益。

### 3.3 自主能力

系统具有调用工具并根据反馈继续的Agent能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

### 4.2 系统流程与组件

每任务给定一个正确但次优的起始产物、参考解和运行预算，Agent在共同Claude Code工具环境中修改并执行多次。评估器通过验证器对每个提交点评分，并分析规划、结果执行、反馈控制和回退。三次独立运行测个任务，亦使用重启对比检查系统是否从旧经验获益。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

在36个AutoLab任务和7个前沿模型上测评，每任务每模型3次轨迹；主度量为评分器打分、执行产物正确性、失败恢复和经验保留后提交表现。

### 5.2 基线、指标与结果

作者报告Claude Opus 4.7总体结果0.739；不同模型在规划、执行和反馈控制上有分别优势，经验复用提升不一致，真正新颖方法仍不常见。

### 5.3 科学贡献与证据强度

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文在自动研究Agent及长程轨迹研究的背景下与已有系统和评测基准比较，具体差异体现于上文所述的新监督、证据记忆或任务评价策略。

## 7. 局限性与风险

作者承认的局限以全文limitations段为准；读者风险：任务集和评分器不能代表全部真实研究环境，结果需按作者所设定的任务范围解读。

## 8. 对综述写作的价值

任务覆盖AI工程、挑战和CUDA算法，但本文是对AI科研Agent的通用评估，没有专业领域科学结果，归入01.02。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文用四个工作负载族、36项专家编制任务系统比较多个最新模型执行长程自动研究的能力。分析不止结果分数，还评估方法定义、执行可靠性、进度反馈、经验利用和系统工具层。作者结论称当前系统已实现部分研究闭环，而不是稳健的自我提升研究者。

### 9.2 速记版 pipeline

每任务给定一个正确但次优的起始产物、参考解和运行预算，Agent在共同Claude Code工具环境中修改并执行多次。评估器通过验证器对每个提交点评分，并分析规划、结果执行、反馈控制和回退。三次独立运行测个任务，亦使用重启对比检查系统是否从旧经验获益。

### 9.3 标注字段汇总

```text
paper_id=ASD-0957
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
| 问题开放度 | O2 既定基准 | 36个AutoLab任务为预定义评测基准 | “在36个AutoLab任务和7个前沿模型上测评” · L101 |
| 验证强度 | V1 基准/内部评测 | 自动评分器打分及执行产物正确性检查，无独立复现 | “每任务每模型3次轨迹；主度量为评分器打分、执行产物正确性” · L101 |
| 系统自主性 | L2 闭环执行者 | Agent在给定任务内自主迭代研究和修正 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
