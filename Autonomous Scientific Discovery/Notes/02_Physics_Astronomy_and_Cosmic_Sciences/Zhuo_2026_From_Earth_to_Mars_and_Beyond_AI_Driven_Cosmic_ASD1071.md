# From Earth to Mars and Beyond: AI-Driven Cosmic-Ray Validation and Prediction with CorsikaAgent

**论文信息**

- ID：ASD-1071
- 标题：From Earth to Mars and Beyond: AI-Driven Cosmic-Ray Validation and Prediction with CorsikaAgent
- 作者：Chen, Zhuo; Zhao, Zhizheng; Shen, Jinhong; Gao, Leyun; Liu, Cheng-en; Li, Qite; Wang, Zijian; Li, Qiang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.16607
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1071.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Zhuo_2026_From_Earth_to_Mars_and_Beyond_AI_Driven_Cosmic_ASD1071.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象和目标 | 计算海平面宇宙线缪子通量。 | TXT lines 223-225；核验TXT行号 223 | We calculate the sea-level cosmic-ray muon flux with CORSIKA and develop CorsikaAgent, an auditable large-language-model-based system for configuring, executing, and validating air-shower simulations, | 高（一手正文；非独立复现） |
| 验证数据 | 与实验测量和常用解析参数化比较。 | TXT lines 230-232；核验TXT行号 230 | energies. The predicted momentum spectra at approximately 0∘0^{\circ} and 75∘75^{\circ} are compared with experimental measurements of the atmospheric muon flux and with commonly used analytic parametrizations. The two | 高（一手正文；非独立复现） |
| 独立重建 | Agent以不同采样策略复算同一可观测量。 | TXT lines 234-236；核验TXT行号 234 | principal momentum and zenith-angle dependences of the data. The agent independently reconstructs the same observable through a different sampling strategy and keeps every steering card, executable, seed, log, and | 高（一手正文；非独立复现） |
| 新环境预测 | 迁移到火星复现基准，金星给出无测量环境预测。 | TXT lines 239-241；核验TXT行号 239 | Transferred to Mars, the workflow reproduces the CORSIKA 8 benchmark, and transferred to Venus it produces the first prediction of the surface muon flux, an environment for which no measurement exists. The agent | 高（一手正文；非独立复现） |
| 局限 | 质子初级粒子假设和系统不确定性限制精度。 | TXT lines 244-247；核验TXT行号 244 | magnetic field, electric field—for new environments, while the proton-only primary model, limited high-momentum statistics, and an incomplete systematic-uncertainty treatment bound the physical precision that can currently be claimed. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

CorsikaAgent为CORSIKA空气簇射模拟提供可审计的配置、执行和验证工作流。论文计算海平面宇宙线缪子通量，并与实验测量和解析参数化比较；Agent以不同采样策略独立重建可观测量。迁移到火星可复现基准，迁移到金星则给出无测量环境的通量预测，同时明确物理精度受初级粒子假设、统计量和系统误差处理限制。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。计算并验证宇宙线缪子通量，外推至行星环境。
  - 原文位置：TXT lines 223-225；核验TXT行号 223；引文：We calculate the sea-level cosmic-ray muon flux with CORSIKA and develop CorsikaAgent, an auditable large-language-model-based system for configuring, executing, and validating air-shower simulations,
- 多步行动过程：yes。配置、运行、验证模拟并迁移环境参数。
  - 原文位置：TXT lines 224-226；核验TXT行号 224；引文：develop CorsikaAgent, an auditable large-language-model-based system for configuring, executing, and validating air-shower simulations, and for predicting particle fluxes in unexplored environments. The
- 至少一种Agent能力：yes。自主重配大气、磁场和电场以适配新环境。
  - 原文位置：TXT lines 241-244；核验TXT行号 241；引文：surface muon flux, an environment for which no measurement exists. The agent thus extends the workflow from auditable reproduction to first-principles prediction: it autonomously reconfigures the simulation—atmosphere, magnetic field, electric field—for new environments, while the proton-only
- 明确科研流程角色：yes。保存模拟输入、执行文件、随机种子和分析脚本以保证审计。
  - 原文位置：TXT lines 235-238；核验TXT行号 235；引文：independently reconstructs the same observable through a different sampling strategy and keeps every steering card, executable, seed, log, and analysis script bound to the result it produced; its output is consistent with the direct calculation at the level resolved by the present comparison.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02 物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为宇宙线空气簇射及行星通量，属02物理科学。

### 2.3 容易混淆的边界

对象为宇宙线空气簇射及行星通量，属02物理科学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

llm_simulation_agent

### 3.2 科研流程角色

simulation_setup；validation；prediction

LLM Agent配置和执行CORSIKA，保存steering卡、可执行文件、随机种子、日志和分析脚本以供审计。

### 3.3 自主能力

自主重配大气、磁场和电场以适配新环境。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是行星环境宇宙线通量计算及金星预测；系统贡献是可审计模拟配置与执行Agent。

### 4.2 系统流程与组件

输入环境条件和目标通量；Agent设定初级粒子与相互作用模型，配置空气簇射模拟并执行，分析海平面谱并与测量/解析模型比较；再替换大气、磁场和电场参数迁移至火星和金星，输出可复现基准及新预测。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

海平面通量与实验测量、解析参数化比较；不同采样方式独立复算；火星案例复现CORSIKA 8基准。

### 5.2 基线、指标与结果

作者报告两种相互作用模型谱线相似并描述主要趋势；火星复现基准，金星得到首个表面缪子通量预测。

### 5.3 科学贡献与证据强度

科学贡献是行星环境宇宙线通量计算及金星预测；系统贡献是可审计模拟配置与执行Agent。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

从可复现地球环境计算扩展到行星环境模拟，并以独立采样核查同一可观测量。

## 7. 局限性与风险

- author_stated：质子初级粒子模型、高动量统计不足及系统误差处理不完整限制精度。
- reviewer_inference：金星没有测量，预测的准确度无法由当前案例直接验证。

## 8. 对综述写作的价值

体现可审计科学模拟Agent如何区分基准复现与无测量环境预测。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

CorsikaAgent验证地球缪子通量并将CORSIKA工作流迁移到行星环境。

### 9.2 速记版 pipeline

输入环境条件和目标通量；Agent设定初级粒子与相互作用模型，配置空气簇射模拟并执行，分析海平面谱并与测量/解析模型比较；再替换大气、磁场和电场参数迁移至火星和金星，输出可复现基准及新预测。

### 9.3 标注字段汇总

```text
paper_id=ASD-1071
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.14` 粒子物理学；二级：`02.02`。
- 原文位置：PDF p.1。
- 判定：宇宙线μ子通量及强子相互作用模型，归粒子物理。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
