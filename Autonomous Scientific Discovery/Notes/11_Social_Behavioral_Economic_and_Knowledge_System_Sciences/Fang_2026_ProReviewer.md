# Fang et al. 2026 - From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent

**论文信息**
- 标题：From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent
- 作者：Haishuo Fang; Yue Feng; Iryna Gurevych
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2606.13349
- PDF / 本地文件路径：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Fang_2026_ProReviewer.pdf`
- 论文类型：系统论文 / scientific peer-review agent paper
- 当前状态：`to_read`
- 阅读日期：2026-07-05
- 笔记作者：Codex

## Phase6FollowupR21 Frozen Adjudication

- Frozen paper id: `ASD-0626`
- Final adjudicated modules: `11`
- `general_method_bucket`: `none`
- Primary module for filing: `11`
- Filing note: 当前目录位置仅用于归档便利，不构成分类依据。
- First-hand source state: 本轮已按本地归档 PDF `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Fang_2026_ProReviewer.pdf` 进行一手来源确认，不再保留“非全文 / 仅摘要级 / 无本地 PDF”表述。
- Frozen judgment: 该文稳定归入 `11`，对象是 investigative scientific peer review 与 evidence-grounded critique；可在展示时放入 `11.07` 语境，但模块事实保持 `11`。

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 本地归档 PDF | 系统围绕 scientific peer review 执行多步主动调查流程 | 高 |
| 科学对象归类 | `11` | 本地归档 PDF | 对象是 scientific peer review 这一知识生产与质量控制机制本身 | 高 |
| 方法流程 | 主动调查式审稿流程成立 | 本地归档 PDF | Agent 维护 structured review log，围绕 claims、questions 和 notes 主动导航论文并核对证据 | 高 |
| 实验验证 | 五维质量评测 + human evaluation | 本地归档 PDF | ProReviewer 在多项质量维度和人工对比中表现强 | 高 |
| 边界判断 | 稳定 `11`，不属于 `01.04` | 本地归档 PDF；对象优先规则 | 核心贡献是 evidence-grounded review generation，而不是通用科研平台 | 高 |
| 本地 PDF 状态 | 已确认 | 本地归档路径 | R21 冻结写回包已确认本地归档 PDF | 高 |

## 0. 摘要翻译

本文提出 ProReviewer，把 automated scientific peer review 从被动生成评论推进到主动调查证据。作者将审稿过程形式化为 MDP，并让 agent 维护一个 structured review log，用于持续记录 claims、questions 和 notes，再据此决定下一步检查论文的哪个部分、是否回看前文以及如何形成最终 critique。实验显示，ProReviewer 在多个质量维度上表现突出，说明其对象稳定属于 scientific knowledge production 中的 peer review 环节。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕自动 scientific peer review 执行多步主动调查流程，具备规划、证据记录、反馈迭代和策略决策等 Agent 特征
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：计划生成、工具调用、反馈迭代、自主决策、多 Agent 协作
- 在科研流程中承担的明确角色：evidence_assessment_and_validation; literature_search_and_reading; feedback_iteration; result_interpretation

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 当前排除结论：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`11`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`11`
- Primary module for filing 说明：仅用于归档和展示，不覆盖对象模块事实
- 主展示模块一级类：`11` 社会、行为、经济与知识系统科学
- 主展示语境：`11.07` investigative scientific peer review
- 其他覆盖模块及对应层级路径：无
- 每个模块的对象实验证据：scientific peer review 中的 claim checking、review log、evidence-grounded critique 与评测结果均围绕 knowledge production 审稿机制
- 归类理由：研究对象是 investigative scientific peer review，本质上属于科学知识生产系统
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：investigative scientific peer review
- 最终科学问题：如何让 review agent 像人类 reviewer 一样主动核查可疑 claims，并据此生成更扎实的 critique
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：项目规则要求按最终研究对象而非模型实现细节归类

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `11`
- 判定理由：研究对象就是 scientific peer review 行为本身，而不是无具体对象的通用 research-agent platform
- 01.04 判定说明：已有明确知识生产对象、任务与结果，因此 `general_method_bucket=none`
- 是否需要二次复核：当前分类无需二次复核

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent; Planning Agent; Hybrid Agent
- 科研流程角色：evidence_assessment_and_validation; literature_search_and_reading; feedback_iteration; result_interpretation
- 自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
- 交叉属性：computation_driven; benchmark_driven

## 4. 方法设计

### 4.1 方法动机

- 作者希望让自动审稿从被动生成一般性评论，转向主动调查论文中的可疑 claim 与证据链
- 既有自动审稿常缺少跨 section 的证据核查与一致性判断

### 4.2 系统流程

1. 读入待审 scientific paper。
2. Agent 根据当前证据决定下一步检查哪个 section、提取哪个 claim、提出哪个 question。
3. 系统在论文内部导航，并维护 structured review log。
4. 新读内容用于核对旧 claim、解决未决问题或记录新的 inconsistency。
5. 聚合证据并生成 evidence-grounded review comments。

## 5. 实验与验证

- 验证方式：benchmark; expert_evaluation
- 数据 / 对象：version-matched paper-review pairs；peer-review benchmark setting
- 任务设置：在 scientific paper 审稿中主动调查 claim、维护 review log、生成 evidence-grounded review
- 关键结果：论文报告在多项质量维度和人工比较中表现较强
- 证据强度判断：当前已是本地 PDF 支撑下的对象分类证据，不再是 non-full-text state

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：本文直接研究 scientific peer review，而不是自然科学对象上的发现或预测
- 与已有 Agent / 科研智能系统的区别：它把自动审稿推进到可学习的主动调查策略，并强调 evidence-grounded critique
- 与同一科学领域其他 Agent 文献的关系：可作为 `11` 下偏 investigation / evidence-tracking 的 peer-review agent 代表样本
- 主要创新点：peer review 的 MDP 形式化、structured review log 与主动调查式审稿策略

## 7. 局限性与风险

- 当前评测仍集中在 peer-review benchmark 场景，跨 venue 与跨学科泛化仍需细看全文细节
- 若做正文精细引文，后续仍可补页码级摘录
- 当前主要风险是系统强度和外推性展开，而不是 `11` 分类风险

## 8. 对综述写作的价值

- 可放入章节：`11` 社会、行为、经济与知识系统科学中的 investigative peer-review agents
- 可支撑论点：Agent 已能直接介入 scientific peer review 的证据核查与 critique 生成，而不只是输出一般性评论
- 可用于表格或图：主类代表作表、边界样本表、验证方式对比表
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

把自动审稿推进到主动调查证据的 scientific peer-review agent。

### 9.2 速记版 pipeline

1. 读入待审论文。
2. 维护 review log 并跟踪 claims。
3. 主动导航 section 核查证据。
4. 迭代更新 questions / notes。
5. 生成有证据支撑的 review。

### 9.3 标注字段汇总

```text
paper_id: ASD-0626
scientific_object_modules: 11
object_coverage_mode: single_module
primary_module_for_filing: 11
general_method_bucket: none
classification_confidence: high
source_limited: no
safety_access_status: none
first_hand_sources_checked: local archived PDF (`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Fang_2026_ProReviewer.pdf`); official arXiv record (`https://arxiv.org/abs/2606.13349`)
pdf_archive_status: local archived PDF confirmed
canonical_local_pdf_path: Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Fang_2026_ProReviewer.pdf
official_pdf_url: https://arxiv.org/pdf/2606.13349
```
