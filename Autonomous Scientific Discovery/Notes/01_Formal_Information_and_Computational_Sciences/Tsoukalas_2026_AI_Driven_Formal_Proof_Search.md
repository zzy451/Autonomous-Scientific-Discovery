# Advancing mathematics research with AI-driven formal proof search

**论文信息**

- ID：ASD-0906
- 标题：Advancing mathematics research with AI-driven formal proof search
- 作者：George Tsoukalas; Anton Kovsharov; Sergey Shirobokov; Anja Surina; Moritz Firsching; Gergely Bérczi; Francisco J. R. Ruiz; Arun Suggala; Adam Zsolt Wagner; Eric Wieser; Lei Yu; Aja Huang; Miklós Z. Horváth; Andrew Ferraiuolo; Henryk Michalewski; Codrut Grosu; Edward Lockhart; Thomas Hubert; Matej Balog; Pushmeet Kohli; Swarat Chaudhuri
- 年份：2026
- 来源 / venue：Science
- DOI / arXiv / URL：https://doi.org/10.1126/science.aej2213
- 一手阅读来源：https://ar5iv.labs.arxiv.org/html/2605.22763
- 来源层级：全文
- 阅读版本：arXiv submitted manuscript 2605.22763 (ar5iv HTML full-text mirror); OpenAlex links this submitted version to Science DOI 10.1126/science.aej2213. PDF endpoint was inaccessible, so source is HTML.
- 阅读版本题名：Advancing mathematics research with AI-driven formal proof search
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_rescue/0906_ar5iv.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 版本身份与题名对应 | 页面标题为[2605.22763] Advancing Mathematics Research with AI-Driven Formal Proof Search，题名与Science DOI 10.1126/science.aej2213相同；OpenAlex将arXiv submitted version链接到该Science论文。当前读取的是arXiv/HTML镜像。 | ar5iv页标题、摘要首段 | high |
| 系统组成与两个Agent变体 | 提出AlphaProof Nexus；basic agent由使用Lean compiler反馈的prover subagents搜索，full-featured版本以evolutionary algorithm协调子Agent并可使用AlphaProof。 | Abstract；Introduction / AlphaProof Nexus architecture section | high |
| Basic prover subagent的循环步骤 | 每个subagent与Gemini 3.1 Pro交互，查看Lean文件并对proof进行search-replace编辑；每次修改后Lean compiler提供编译错误等反馈；多个subagent独立并行，发现有效证明即停止其他进程。 | Materials and Methods, Appendix A.1 “Further Details on AlphaProof Nexus Agents”, Figure 4 discussion | high |
| Lean形式验证参与每步迭代 | 独立subagents从相同初始proof sketch出发，Ralph loop连续执行证明草稿编辑、Lean编译和错误反馈，完成后检查最终sketch完整性。 | Materials and Methods, Appendix A.1, “Basic Agent” | high |
| Full-featured agent使用进化协调和AlphaProof | 完整Agent通过进化算法协调prover agents，使用AlphaProof作为专门Lean theorem-proving工具；不同配置在9个已解Erdős题上比较。 | Main text, AlphaProof Nexus agents description; Materials and Methods Appendix | high |
| 开放问题求解规模和成本 | full-featured Agent自主解决353个开放Erdős问题中的9个，每题成本约数百美元；基础LLM+Lean Agent在难题上成本更高但复现这9题。 | Abstract | high |
| 独立猜想证明结果 | 在492个OEIS conjectures中证明44个，提供形式证明搜索在Erdős问题外的数量级结果。 | Abstract | high |
| 结果配置比较及实际验证产物 | basic agent可复现full-featured agent的9个Erdős成功，但较难问题代价较高；Lean proof文件和部分自然语言证明公开在AlphaProof Nexus results repository。 | Main text, results discussion following problem-level analysis | high |
| 量子光学并非本文展示的对象级实验 | 量子光学仅和组合数学、优化、图论、代数几何并列于“being deployed”方向；全文未发现单独量子光学任务/方法/结果，故不以该应用列表增加02。 | Abstract领域列表及全文搜索 quantum optics | high |
| 证据与版本边界 | 获取的是与Science工作对应的arXiv HTML全文，不是Science出版PDF；主文与Materials and Methods附录可检索、可定位。 | ar5iv / arXiv metadata; Methods appendix | high |

## 0. 摘要翻译

全文介绍AlphaProof Nexus形式证明搜索系统，以LLM提出Lean证明步骤、Lean编译器逐步验证；full-featured Agent由多个prover subagents并行搜索，并用进化算法协调，且可调用AlphaProof专门证明工具。报告在353个开放Erdős问题中解决9个，平均每题成本数百美元；在492个OEIS猜想中证明44个。basic Agent以LLM生成与Lean验证交替，也复现9个Erdős解，但较难问题成本更高。正文给出Lean文件编辑、编译反馈、并行子Agent及代理配置的细节。量子光学仅在潜在部署/研究领域列表中提及，未发现量子光学具体任务或结果。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Agent承担具体开放数学问题求解：多个prover subagents读取并编辑Lean证明文件，调用Lean编译器反馈并循环修订；full-featured版本还进行进化协调及AlphaProof调用，成功结果经形式验证。该工作直接执行数学研究中的形式证明搜索而非一般数学问答，满足科学Agent的多步任务和科研角色标准。

### 1.2 排除风险检查

归01.01.12数学/形式数学（沿用原记录的组合数学细分标注）；核心对象是Lean形式证明和开放数学命题。量子光学只在摘要中作为部署/应用领域提及，正文未见可定位的物理对象任务、实验或结果，故不增加02。Lean是证明验证工具，不改变数学对象归属。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不替代多模块事实）
- 模块内分类路径：01.01.12
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

Full-featured系统解决353个开放Erdős问题中的9个，平均每题成本数百美元，并证明492个OEIS conjectures中的44个。Basic LLM+Lean循环复现full-featured agent解决的9个Erdős问题，但在较难问题上成本更高；全文还对这9题比较basic、AlphaProof辅助、进化组件及full agent配置。论文提及系统正在组合数学、优化、图论、代数几何、量子光学等方向部署，但本次审阅未发现量子光学对象级案例/结果；不据此增加02分类。

### 2.3 容易混淆的边界

归01.01.12数学/形式数学（沿用原记录的组合数学细分标注）；核心对象是Lean形式证明和开放数学命题。量子光学只在摘要中作为部署/应用领域提及，正文未见可定位的物理对象任务、实验或结果，故不增加02。Lean是证明验证工具，不改变数学对象归属。

## 3. Agent 系统与科研流程角色

Agent承担具体开放数学问题求解：多个prover subagents读取并编辑Lean证明文件，调用Lean编译器反馈并循环修订；full-featured版本还进行进化协调及AlphaProof调用，成功结果经形式验证。该工作直接执行数学研究中的形式证明搜索而非一般数学问答，满足科学Agent的多步任务和科研角色标准。

科研流程与自主能力以本文实际行动和工具调用为依据：

研究构建basic与full-featured形式证明搜索Agent。Basic由N个相互独立、共享同一初始Lean proof sketch的prover subagents并行运行Ralph式循环；每轮LLM（Gemini 3.1 Pro）阅读Lean文件、在限定区域进行文本编辑，Lean compiler对每次改动编译并提供错误反馈，subagent据此继续修订；任一子Agent找到有效证明即终止其余搜索。full-featured版本使用进化算法协调prover subagents，保留/比较候选sketch，并可调用AlphaProof作为聚焦证明工具；最终对proof sketch和编译结果做完整性检查。评估开放Erdős问题、OEIS猜想及其他数学任务，比较不同功能配置的证明数量与成本。

## 4. 方法设计

### 4.1 方法动机与设计

将Lean形式化证明、编译器机器反馈和并行LLM搜索组成可扩展的数学研究Agent，展示其对开放Erdős问题及OEIS猜想的实际求解能力，并比较简化循环与带进化协调/专门证明器的成本和效果。

### 4.2 系统流程与组件

研究构建basic与full-featured形式证明搜索Agent。Basic由N个相互独立、共享同一初始Lean proof sketch的prover subagents并行运行Ralph式循环；每轮LLM（Gemini 3.1 Pro）阅读Lean文件、在限定区域进行文本编辑，Lean compiler对每次改动编译并提供错误反馈，subagent据此继续修订；任一子Agent找到有效证明即终止其余搜索。full-featured版本使用进化算法协调prover subagents，保留/比较候选sketch，并可调用AlphaProof作为聚焦证明工具；最终对proof sketch和编译结果做完整性检查。评估开放Erdős问题、OEIS猜想及其他数学任务，比较不同功能配置的证明数量与成本。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

Full-featured系统解决353个开放Erdős问题中的9个，平均每题成本数百美元，并证明492个OEIS conjectures中的44个。Basic LLM+Lean循环复现full-featured agent解决的9个Erdős问题，但在较难问题上成本更高；全文还对这9题比较basic、AlphaProof辅助、进化组件及full agent配置。论文提及系统正在组合数学、优化、图论、代数几何、量子光学等方向部署，但本次审阅未发现量子光学对象级案例/结果；不据此增加02分类。

### 5.2 基线、指标与结果

Full-featured系统解决353个开放Erdős问题中的9个，平均每题成本数百美元，并证明492个OEIS conjectures中的44个。Basic LLM+Lean循环复现full-featured agent解决的9个Erdős问题，但在较难问题上成本更高；全文还对这9题比较basic、AlphaProof辅助、进化组件及full agent配置。论文提及系统正在组合数学、优化、图论、代数几何、量子光学等方向部署，但本次审阅未发现量子光学对象级案例/结果；不据此增加02分类。

### 5.3 科学贡献与证据强度

将Lean形式化证明、编译器机器反馈和并行LLM搜索组成可扩展的数学研究Agent，展示其对开放Erdős问题及OEIS猜想的实际求解能力，并比较简化循环与带进化协调/专门证明器的成本和效果。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

沿用Lean形式证明助手约束LLM推理，并将AlphaProof作为专用证明工具；在开放问题上比较基础生成/验证循环与带进化协调的并行搜索。

## 7. 局限性与风险

ar5iv所载为对应Science工作的arXiv提交版，并非期刊最终PDF；本次arXiv PDF直链因SSL失败，使用完整HTML正文。大规模求解结果集中于可形式化且被纳入基准的问题集；full-featured成功率伴随每题数百美元成本，basic虽复现9题但难题成本更高。部署领域列表不等于各领域均有本文实证结果；特别是没有足够量子光学对象实验支持02。

## 8. 对综述写作的价值

形式数学 Agent 代表，可说明形式验证作为科研 Agent 证据约束的作用。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以形式验证约束数学证明搜索

### 9.2 速记版 pipeline

研究构建basic与full-featured形式证明搜索Agent。Basic由N个相互独立、共享同一初始Lean proof sketch的prover subagents并行运行Ralph式循环；每轮LLM（Gemini 3.1 Pro）阅读Lean文件、在限定区域进行文本编辑，Lean compiler对每次改动编译并提供错误反馈，subagent据此继续修订；任一子Agent找到有效证明即终止其余搜索。full-featured版本使用进化算法协调prover subagents，保留/比较候选sketch，并可调用AlphaProof作为聚焦证明工具；最终对proof sketch和编译结果做完整性检查。评估开放Erdős问题、OEIS猜想及其他数学任务，比较不同功能配置的证明数量与成本。

### 9.3 标注字段汇总

```text
paper_id=ASD-0906
inclusion_status=included
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01.12
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O5 开放数学 | 解决开放Erdős问题和OEIS猜想，答案事先未知但可由Lean形式化证明严格检验 | “full-featured Agent自主解决353个开放Erdős问题中的9个” · L30 |
| 验证强度 | V4 证明/复现 | 每个证明由Lean编译器逐步机器检验，Lean proof文件公开，属机器可检验的形式化证明 | “Lean形式验证参与每步迭代” · L28 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：是
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
