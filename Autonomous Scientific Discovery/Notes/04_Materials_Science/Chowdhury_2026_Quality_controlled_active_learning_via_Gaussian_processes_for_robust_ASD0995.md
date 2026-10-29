# Quality-controlled active learning via Gaussian processes for robust structure–property learning in autonomous microscopy

**论文信息**

- ID：ASD-0995
- 标题：Quality-controlled active learning via Gaussian processes for robust structure–property learning in autonomous microscopy
- 作者：Jawad Chowdhury; Ganesh Narasimha; Jan-Chi Yang; Hiroshi Funakubo; Yoshitaka Ehara; Yongtao Liu; Rama Vasudevan
- 年份：2026
- 来源 / venue：npj Computational Materials
- DOI / arXiv / URL：https://www.nature.com/articles/s41524-026-02248-x
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0995.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Chowdhury_2026_Quality_controlled_active_learning_via_Gaussian_processes_for_robust_ASD0995.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | 论文提出质量控制主动学习框架，用简谐振子模型拟合评估测量质量，并在数据获取时自动排除低保真数据，结合高斯过程进行结构—性质学习。先在含空间局部噪声的PbTiO3薄膜BEPS既有数据集评估，再在具有异质畴结构的独立薄膜样品上实时部署。 | 摘要；TXT第13行；核验TXT行号 13 | Autonomous experimental systems are increasingly used in materials research to accelerate scientiﬁc discovery, but their performance is often limited by low-quality, noisy data. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第17行；核验TXT行号 17 | We introduce a gated active learning framework that combines curiosity driven sampling with a physics-informed quality control ﬁlter based on Simple Harmonic Oscillator model ﬁts, allowing the system to automatically exclude low ﬁdelity data during acquisition. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Quality-controlled active learning via Gaussian processes for robust structure–property learning in autonomous microscopy。系统角色与能力：系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第27行；核验TXT行号 27 | Autonomous experimentation platforms are transforming the landscape of materials research by enabling rapid, closed-loop discovery cycles that combine physical instrumentation with machine learning (ML)1–4. | 高（一手正文；非独立复现） |
| 验证与结果 | 在预采集PbTiO3数据上与随机采样、标准主动学习和多任务学习比较；随后于不同PbTiO3样品开展实时显微实验。摘要报告质量门控框架优于比较方法，但具体指标需结果段补录。 | 摘要；TXT第22行；核验TXT行号 22 | We further deployed the framework in real-time experiments on a separate PbTiO3 thin-ﬁlm sample with heterogeneous domain structures, demonstrating its effectiveness in autonomous microscopy experiments. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可支持综述讨论物理知识质量门控与主动学习结合的混合自主实验。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第20行；核验TXT行号 20 | Evaluations on a pre-acquired dataset of band-excitation piezoresponse spectroscopy (BEPS) data from PbTiO3 thin ﬁlms with spatially localized noise show that the proposed method outperforms random sampling, standard active learning, and multitask learning strategies. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出质量控制主动学习框架，用简谐振子模型拟合评估测量质量，并在数据获取时自动排除低保真数据，结合高斯过程进行结构—性质学习。先在含空间局部噪声的PbTiO3薄膜BEPS既有数据集评估，再在具有异质畴结构的独立薄膜样品上实时部署。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文提出质量控制主动学习框架，用简谐振子模型拟合评估测量质量，并在数据获取时自动排除低保真数据，结合高斯过程进行结构—性质学习。先在含空间局部噪声的PbTiO3薄膜BEPS既有数据集评估，再在具有异质畴结构的独立薄膜样品上实时部署。
  - 原文位置：摘要；TXT第13行；核验TXT行号 13；引文：Autonomous experimental systems are increasingly used in materials research to accelerate scientiﬁc discovery, but their performance is often limited by low-quality, noisy data.
- 多步行动过程：yes。系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第17行；核验TXT行号 17；引文：We introduce a gated active learning framework that combines curiosity driven sampling with a physics-informed quality control ﬁlter based on Simple Harmonic Oscillator model ﬁts, allowing the system to automatically exclude low ﬁdelity data during acquisition.
- 至少一种Agent能力：yes。Quality-controlled active learning via Gaussian processes for robust structure–property learning in autonomous microscopy。系统角色与能力：系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第18行；核验TXT行号 18；引文：physics-informed quality control ﬁlter based on Simple Harmonic Oscillator model ﬁts, allowing the system to automatically exclude low ﬁdelity data during
- 明确科研流程角色：yes。在预采集PbTiO3数据上与随机采样、标准主动学习和多任务学习比较；随后于不同PbTiO3样品开展实时显微实验。摘要报告质量门控框架优于比较方法，但具体指标需结果段补录。
  - 原文位置：摘要；TXT第22行；核验TXT行号 22；引文：We further deployed the framework in real-time experiments on a separate PbTiO3 thin-ﬁlm sample with heterogeneous domain structures, demonstrating its effectiveness in autonomous microscopy experiments.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.03 软物质与功能材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为PbTiO3铁电薄膜畴结构与压电响应关系，归04.03实验设计/主动采样。核心贡献为质量控制和学习策略，不是语言模型Agent。

### 2.3 容易混淆的边界

对象为PbTiO3铁电薄膜畴结构与压电响应关系，归04.03实验设计/主动采样。核心贡献为质量控制和学习策略，不是语言模型Agent。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

实验设计与执行

Quality-controlled active learning via Gaussian processes for robust structure–property learning in autonomous microscopy。系统角色与能力：系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Quality-controlled active learning via Gaussian processes for robust structure–property learning in autonomous microscopy。系统角色与能力：系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述讨论物理知识质量门控与主动学习结合的混合自主实验。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

在预采集PbTiO3数据上与随机采样、标准主动学习和多任务学习比较；随后于不同PbTiO3样品开展实时显微实验。摘要报告质量门控框架优于比较方法，但具体指标需结果段补录。

### 5.2 基线、指标与结果

在预采集PbTiO3数据上与随机采样、标准主动学习和多任务学习比较；随后于不同PbTiO3样品开展实时显微实验。摘要报告质量门控框架优于比较方法，但具体指标需结果段补录。

### 5.3 科学贡献与证据强度

可支持综述讨论物理知识质量门控与主动学习结合的混合自主实验。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文在 curiosity-driven主动学习和高斯过程结构—性质学习基础上增加物理模型质量门控，针对噪声数据会被误判为高信息量的问题。

## 7. 局限性与风险

作者及读者可确认的适用边界：评估限于PbTiO3薄膜BEPS数据及相关显微结构—性质任务；其他材料、噪声类型和仪器上仍需重新检验质量门控。

## 8. 对综述写作的价值

可支持综述讨论物理知识质量门控与主动学习结合的混合自主实验。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出质量控制主动学习框架，用简谐振子模型拟合评估测量质量，并在数据获取时自动排除低保真数据，结合高斯过程进行结构—性质学习。

### 9.2 速记版 pipeline

系统在显微实验中持续采集BEPS数据，以简谐振子拟合估计数据质量；质量门控过滤低保真测量，高斯过程和主动学习策略根据合格样本选择下一测点。新测量更新结构—性质模型并影响后续采样。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0995
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.03
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.03` 材料表征；二级：`04.01`。
- 原文位置：PDF p.1。
- 判定：First-hand evidence supports 04.01.03; valuations on a pre-acquired dataset of band-excitation piezoresponse spectroscopy (BEPS) data from PbTiO3 thin ﬁlms with spatially localized noise show that the proposed method outperforms random sampling, standard active learning, and multitask learning strategies. We further deployed the framework in real-time experiments on a separate PbTiO3 thin-ﬁlm sample with heterogeneous domain structures, demonstrating its
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
