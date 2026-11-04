# Dr. Claw: An AI Scientist Workspace for Vibe Research

**论文信息**

- ID：ASD-0950
- 标题：Dr. Claw: An AI Scientist Workspace for Vibe Research
- 作者：Song, Dingjie; Zhang, Hanrong; Liu, Dawei; Liu, Yixin; Li, Zongxia; Yuan, Zhengqing; Zhang, Siqi; Zou, Henry Peng; Yan, Zhiling; Zhang, Yuxuan; Ye, Yanfang; Yu, Philip S.; Sun, Lichao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.00365
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0950.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Dingjie_2026_Dr_Claw_An_AI_Scientist_Workspace_for_Vibe_Research_ASD0950.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断依据：目标是研究而非通用产品应用。 | 纳入判断依据：目标是研究而非通用产品应用。 | TXT line 332；核验TXT行号 332 | Command-line coding agents (e.g., Claude Code, Gemini CLI) can already read and write files and sustain long sessions, yet end-to-end research still fragments across chat tools, IDEs, terminals, and writing environments, and the decisions that make it auditable are rarely preserved. | 高（一手正文；非独立复现） |
| 科学对象或研究任务由正文明确指出。 | 科学对象或研究任务由正文明确指出。 | TXT line 925；核验TXT行号 925 | instruction (“conduct a rigorous, publication-quality study…”) across three medical problems: | 高（一手正文；非独立复现） |
| 方法包含任务路由、执行和结果处理。 | 方法包含任务路由、执行和结果处理。 | TXT line 1022；核验TXT行号 1022 | We run one coherent Derm7pt mini-project through Dr. Claw and recover it from an induced failure, on the same backend executor (codex/gpt-5.4). The advantage on display is not speed or accuracy but the auditable, structured artifact trail the orchestration layer maintains: when a step fails, the captured execution trace and preserved prior state let the project recover in place rather than restart. | 高（一手正文；非独立复现） |
| 作者设置了对照或独立验证。 | 作者设置了对照或独立验证。 | TXT line 1036；核验TXT行号 1036 | The same project also shows what happens when a step fails (Figure 7). Halting on an induced wrong-path error rather than silently self-correcting, then recovering to a real result (accuracy 0.8920.892) with all 55 pre-existing files retained (2323 tool events), the workspace adds the corrected artifacts rather than wiping the failed attempt—the prior pipeline state survives the fix. We report this as a single-condition design demonstration, without a matched bare-agent recovery run. | 高（一手正文；非独立复现） |
| 正文报告可核对的结果或系统贡献。 | 正文报告可核对的结果或系统贡献。 | TXT line 1077；核验TXT行号 1077 | We presented Dr. Claw, an integrated system for end-to-end AI research that unifies state-object management and skill-based execution in one workspace to reduce cross-tool orchestration costs and improve workflow continuity. Evaluated with the same backend executor run inside versus outside Dr. Claw, which compares the whole orchestration layer against the agent it wraps rather than ablating its parts, the layer preserves the measured completeness of the output (a count of which research components are present, not a correctness check) while producing a more auditable, better-structured artifact trail, as shown through a persisted-process-model analysis and a non-destructive failure-recovery walkthrough; a retrospective human study over three stages provides complementary evidence on time, output quality, and integrated experience. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出Dr. Claw工作空间，将编码Agent等现有执行器组织为可审计的人机协作流程，用持久化任务图、产物存储、决策日志和执行轨迹支持研究过程。作者以皮肤病变分类和临床笔记风险基线三个医学任务测试完整性、故障恢复和用户体验。结果提示它增强过程完整性与可追溯性，但实验规模较小。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文设定了可检验的科研目标或学术问题。
  - 原文位置：TXT line 925；核验TXT行号 925；引文：instruction (“conduct a rigorous, publication-quality study…”) across three medical problems:
- 多步行动过程：yes。正文实例显示Agent进行了多步任务路径。
  - 原文位置：TXT line 1036；核验TXT行号 1036；引文：The same project also shows what happens when a step fails (Figure 7). Halting on an induced wrong-path error rather than silently self-correcting, then recovering to a real result (accuracy 0.8920.892) with all 55 pre-existing files retained (2323 tool events), the workspace adds the corrected artifacts rather than wiping the failed attempt—the prior pipeline state survives the fix. We report this as a single-condition design demonstration, without a matched bare-agent recovery run.
- 至少一种Agent能力：yes。系统使用工具、计划、反馈或多Agent中明确能力。
  - 原文位置：TXT line 332；核验TXT行号 332；引文：Command-line coding agents (e.g., Claude Code, Gemini CLI) can already read and write files and sustain long sessions, yet end-to-end research still fragments across chat tools, IDEs, terminals, and writing environments, and the decisions that make it auditable are rarely preserved.
- 明确科研流程角色：yes。系统在科研流程中承担研究者、执行者或审查者角色。
  - 原文位置：TXT line 334；核验TXT行号 334；引文：We demonstrate Dr. Claw through an interactive three-view scenario and a failure-recovery walkthrough, and evaluate it against a bare command-line agent sharing the same backend executor, so the comparison contrasts the whole orchestration layer (task graph, state objects, and skill library) with the agent it wraps. Holding the executor fixed, Dr. Claw scores higher on research completeness while persisting an auditable, recoverable process trail. Demo access: repository https://github.com/OpenLAIR/dr-claw, released under AGPL-3.0 with GPL-3.0 upstream components.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.02.05 肿瘤学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

医学数据实验支持07模块；系统也对研究软件结构和人机交互有方法贡献，但对象证据当前以医学任务为主，保留07。

### 2.3 容易混淆的边界

医学数据实验支持07模块；系统也对研究软件结构和人机交互有方法贡献，但对象证据当前以医学任务为主，保留07。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM research agent

### 3.2 科研流程角色

研究协调；实验执行

系统中的Agent角色为 Dr. Claw: An AI Scientist Workspace for Vibe Research; 输入是人类提供的研究目标和约束；协调层构造依赖感知的任务计划，调用编码Agent或其他执行器完成代码、分析和写作；执行结果回写任务图和工作区，人类可检查、接管或修订后继续迭代。

### 3.3 自主能力

系统使用工具、计划、反馈或多Agent中明确能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是在三种医学数据任务上观察研究要素和任务完整性；主要系统贡献是轨迹管理、恢复和可控执行的工作空间。

### 4.2 系统流程与组件

输入是人类提供的研究目标和约束；协调层构造依赖感知的任务计划，调用编码Agent或其他执行器完成代码、分析和写作；执行结果回写任务图和工作区，人类可检查、接管或修订后继续迭代。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以三项医学问题比较工作空间与裸编码Agent，评分研究完整性要素；另运行Derm7pt项目人为注入路径错误来检查是否保留失败状态并恢复，人研另含7名AI博士研究者。

### 5.2 基线、指标与结果

作者报告三项任务的池化完整性得分为0.952，裸编码Agent为0.873；单个任务重复为每项一次，bootstrap置信区间包含0，故属探索性先导结果。

### 5.3 科学贡献与证据强度

科学贡献是在三种医学数据任务上观察研究要素和任务完整性；主要系统贡献是轨迹管理、恢复和可控执行的工作空间。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

正文在相关工作中将本系统放入自动研究Agent及其评测背景；与相邻自动化研究工作相比，本文主要增加了对应方法或监督机制。

## 7. 局限性与风险

作者限制或讨论中明示的证据见原文结论；阅读者推断是评测任务较窄或规模有限，不宜外推至广泛自主科学发现。

## 8. 对综述写作的价值

科学贡献是在三种医学数据任务上观察研究要素和任务完整性；主要系统贡献是轨迹管理、恢复和可控执行的工作空间。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出Dr. Claw工作空间，将编码Agent等现有执行器组织为可审计的人机协作流程，用持久化任务图、产物存储、决策日志和执行轨迹支持研究过程。作者以皮肤病变分类和临床笔记风险基线三个医学任务测试完整性、故障恢复和用户体验。结果提示它增强过程完整性与可追溯性，但实验规模较小。

### 9.2 速记版 pipeline

输入是人类提供的研究目标和约束；协调层构造依赖感知的任务计划，调用编码Agent或其他执行器完成代码、分析和写作；执行结果回写任务图和工作区，人类可检查、接管或修订后继续迭代。

### 9.3 标注字段汇总

```text
paper_id=ASD-0950
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.02.05
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在既定医学数据集上执行分析 | “three medical problems” · L36 |
| 验证强度 | V1 基准/内部评测 | 基准完整性评分无物理验证 | “the measured completeness of the output” · L25 |
| 系统自主性 | L2 闭环执行者 | 系统自主执行研究流程并恢复失败 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
