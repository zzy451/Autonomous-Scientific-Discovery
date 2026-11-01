# 综述统一 BibTeX 文献库逐条核查报告

核查日期：2026-10-31。检查范围为 `references.bib` 全部 **1,051 条**，包括 663 篇核心论文、381 条背景文献对应的去重记录，以及综述和分类标准等补充引用。正文当前使用 43 个引用键。

## 本轮结果

| 项目 | 数量 | 含义 |
|---|---:|---|
| 逐条检查的 BibTeX 条目 | 1,051 | 每条有独立审计记录 |
| 按官方标识符元数据确认身份 | 978 | 标题、作者及标识符匹配；改题、作者差异另作裁定 |
| 按已核对的本地版本或原文确认 | 51 | 指定版本优先，避免当前 API 覆盖实际阅读版本 |
| 已取回的网页资源 | 5 | 项目分类文件及分类体系资源 |
| 论文来源仍未确认 | 15 | 均为背景记录；其中 1 条已移除错误标识符 |
| 网页本轮无法取回 | 2 | CLC 索引、LCC 官方网页的访问验证未成功 |
| 有字段变化的条目 | 456 | 包含实质纠错、作者补全、版本统一及格式调整，不能将其全部解释为原条目有实质错误 |
| 字段变化总数 | 1909 | 一条文献可能涉及多个字段 |

上述“确认”首先指书目身份获得支持，**不等于每个字段均已由独立来源双重验证，更不等于论文的科学结论已获验证**。两篇条目的正式卷期信息仍待确认，另有版本与链接限制列在后文，不能宣称整个库已完全准确。

## 主要实质修正

| 引用键 | 问题 | 本轮处理 |
|---|---|---|
| asd0142 / CompBioAgent | 原 DOI 指向无关的前列腺癌研究 | 更正为 `10.1101/2025.03.17.643771`，同步核对标题和完整作者 |
| asd0593 / AutoDSL | 原 arXiv 标识符实际对应 Search-o1 | 移除 DOI、URL 与 arXiv 字段；未找到替代原始来源，保留待核实标记 |
| asd0052 / 有限元多 Agent 系统 | SSRN 元数据与实际阅读的 arXiv 修订版混用 | 固定为 `2408.13406v2`，采用 Tian、Zhang 作者及该版本标题、2025 年份，移除 SSRN DOI |
| asd0736 / AI-Researcher | 原作者名单错误 | 依据本地 v1 首页改为 Jiabin Tang、Lianghao Xia、Zhonghang Li、Chao Huang |
| asd0739 / 微流控自主实验 | 原首作者错误 | 按出版社元数据及本地首页改为 Junbin Li 等完整作者名单 |
| asd0709、asd0710、asd0711 | 火星车论文的作者名单与原文不符 | 按各自 PDF 首页逐人转录；区分论文与扩展摘要 |
| asd0721 / EO-1 Sciencecraft | 多名作者被误写入单作者论文 | 按本地首页修正为 Steve Chien |
| asd0195 / DockingGA | 年份曾为 2041 | 依据 DOI 元数据修正为 2024，并补全正式出版信息 |
| asd0353 / π-PrimeNovo | 标题乱码、年份和正式来源缺失 | 选择 Nature Communications 正式版本，补全 DOI、2025 年份和作者 |
| asd0498 / Automated Machine Learning | 编辑被写为作者、书籍写为期刊文章 | 使用 `@book` 与 `editor`，补齐 Hutter、Kotthoff、Vanschoren 三位编辑及出版社 |
| asd0185、asd0165 | 首次在线年份与正式卷期年份混用 | 根据官方印刷卷期日期改为 2025、2022 |
| asd0137、asd0151、asd0723 | 在线年份 2025 与正式卷期 2026 混用 | 根据本地期刊版首页统一为 2026 |
| asd0250 | 标题中的撇号被编码为乱码 | 修复标题编码；其余书目信息仍待来源核实 |

其他修改包括补全作者、恢复标题大小写与重音、规范会议条目、清理不属于所引用版本的卷期页码、修复机构作者括号，以及移除 bioRxiv DOI 中错误的 `v1` 后缀。每一个字段变化见 `field_changes.csv`。

## 版本与部分字段的限制

- `asd0420`、`asd0521`：官方元数据确认身份及首次在线年份，但本轮未确认正式卷期年份。暂采用首次在线年份并清除尚未确认的卷期页码，在 BibTeX 中注明口径。
- `asd0614`：本地原文支持标题及完整作者；已有标识符的在线落地页本轮未能取回，未将该链接描述为已验证。
- `asd0543`：保留已注册 SSRN 版本，避免将另一标题、作者名单不同的本地 PDF 信息混入。两版本的修订关系仍待确认。
- `asd0537`、`asd0626`、`asd0728`：当前标识符注册的标题或作者与旧归档版本不同；本轮采用同一来源内部一致的注册信息并注明版本差异。引用某一旧版特有结论时仍应指定版本。
- CLC 条目是在线分类索引资源，不能替代中国图书馆分类法某一正式版次的出版物引用。LCC、DDC、UDC 引用的是各体系的官方在线资源。

## 尚未完成来源确认的条目

以下条目未被标记为“完全正确”。当前正文涉及其中的 LCC 官方网页，其链接已改为现行官方入口；其余待核实论文均未被正文引用。

| 引用键 | 标题 | 原因 |
|---|---|---|
| asd0174 | Unveiling phase transitions with machine learning | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0182 | Reactree: Hierarchical task planning with dynamic tree expansion using llm agent nodes | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0213 | LEGO: A multi-agent collaborative framework with role-playing and iterative feedback for causality explanation generation | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0221 | Adaptive iterative feedback prompting for obstacle-aware path planning via llms | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0228 | Massnet: billion-scale ai-friendly mass spectral corpus enables robust de novo peptide sequencing | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0245 | Learning distilled collaboration graph for multi-agent perception | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0250 | Mind鈥檚 eye: Grounded language model reasoning through simulation | Encoding repair only; primary bibliographic metadata still unresolved. |
| asd0252 | A dynamic llm-powered agent network for task-oriented agent collaboration | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0282 | A meta-reinforcement learning algorithm for causal discovery | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0285 | Shortcutsbench: A large-scale real-world benchmark for api-based agents | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0297 | Chain-of-discussion: A multi-model framework for complex evidence-based question answering | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0330 | Rlcd: Reinforcement learning from contrastive distillation for lm alignment | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0335 | Studying and improving reasoning in humans and machines | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| asd0593 | AutoDSL: Automated self-driving laboratory with large language model agents | arXiv 2501.05366 is Search-o1, not AutoDSL. No verified replacement source. |
| asd0594 | LabPilot: an agentic copilot for scientific instrument control | 未取得可唯一确认身份的原始书目信息；参见逐条记录和检索缓存。 |
| clc | Chinese Library Classification | Official/resource URL retained; network retrieval failed. |
| lcc | Library of Congress Classification | Official/resource URL retained; network retrieval failed. |

## 验证与可追溯文件

- `final_entry_audit.csv`：全部 1,051 条的最终裁定、来源、限制与是否在正文引用。
- `field_changes.csv`：逐字段修改前后值及证据来源。
- `unresolved_entries.csv`：尚待来源核实的条目。
- `verified_overrides.json`：本轮经过裁定、可由生成器再次应用的修正。
- `local_pdf_decisions.json`、`unresolved_local_pdf_evidence.json`、`issue_year_pdf_evidence.json`：本地原文补核证据。
- `before/`：修正前的 BibTeX、原覆盖文件及构建统计备份。
- 检索 JSON 保留本轮及前一日官方元数据缓存；不会把访问失败解释为论文不存在。

生成器优先应用本轮修正，再应用指定版本的原文裁定，避免重新生成时恢复旧错误。生产 BibTeX 与 Coverage_Check 中对应副本保持一致。引用键、重复 DOI、编译与再生成稳定性验证结果见 `validation.json`。

本轮仅在本地修改，未推送 GitHub 或 Overleaf。
