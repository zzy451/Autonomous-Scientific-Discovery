# Large-Scale Autonomous Discovery of Kissing Number Constructions

**论文信息**

- ID：ASD-0973
- 标题：Large-Scale Autonomous Discovery of Kissing Number Constructions
- 作者：Yang, Shuxing; Zhao, Rui; Wu, Junyao; Wang, Yize; Chen, Fujia; Zhu, Kaihao; Li, Wenhao; Li, Zichen; Li, Yaqi; Hong, Shenzhan; Pan, Yuang; Yang, Junjie; Deng, Taowen; Mi, Jincheng; Chen, Hongsheng; Yang, Yihao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.35051
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0973.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Shuxing_2026_Large_Scale_Autonomous_Discovery_of_Kissing_Number_Constructions_ASD0973.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 研究对象为离散几何中的接吻数构造及其下界。 | 本地原文 TXT 第486行；核验TXT行号 486 | The kissing-number problem is one of the oldest problems in discrete geometry. In 1694, Isaac Newton and David Gregory discussed whether 12 or 13 equal spheres could simultaneously touch a central sphere in three dimensions. The answer, 12, was proved more than two centuries later [27]. Yet the apparent simplicity of the question is deceptive. More than three hundred years after its formulation, exact kissing numbers are known only in dimensions 1,2,3,4,81,2,3,4,8 and 2424. In the exceptional dimensions 88 and 2424, the optimal configurations arise from the E8E_{8} and Leech lattices, with 240 and 196560 contacts, respectively [10, 27]. In most other dimensions, substantial gaps remain between the best constructions and known upper bounds. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | 自主系统通过改变表示和几何结构发现多个构造机制。 | 本地原文 TXT 第565行；核验TXT行号 565 | Autonomous scientific research systems provide a possible route towards this broader form of discovery. Recent large-language-model-based agents can carry out extended sequences of reasoning, computation and tool use, while revising research strategies in response to intermediate evidence. Qiushi Engine was previously used for end-to-end autonomous scientific discovery on a physical optical platform [41], where it conducted long-horizon investigations that combined theoretical reasoning, computation and experiment. Here we ask whether the same paradigm can be extended to open mathematical research: can an autonomous research system move beyond optimizing a fixed mathematical formulation and instead discover new representations, constructions and proofs? | 高（一手正文；非独立复现） |
| 实验任务与验证 | 文中列出接触层移动、标记提升及联合选择等具体构造路径。 | 本地原文 TXT 第623行；核验TXT行号 623 | Rather than arising from a single optimization procedure, these improvements were obtained through a sequence of distinct structural discoveries. They include coordinated motions of complete contact layers, labelled liftings that separate direction deletion from reuse, joint support exchanges that exploit shared deletion costs, signed-code replacements generated through Hadamard transfers, compatible directions drawn from a different lattice shell, enlarged lattice-line classes combined through low-overlap isometric images, and spherical-design moment identities and inequalities that determine or bound large lattice sections without enumerating the ambient shell. | 高（一手正文；非独立复现） |
| 主要结果 | 维度25和27的实例说明整体几何自由度可扩充已知构造。 | 本地原文 TXT 第639行；核验TXT行号 639 | A common pattern connects these apparently different constructions. Configurations that appear saturated in one representation retain exploitable freedom in another. In dimension 25, moving an entire 552-point contact layer while preserving its internal Gram matrix creates room for an additional point. In dimension 27, labelled lifting separates direction reuse from deletion; with the first layer fixed, jointly selecting second-layer directions and labels enlarges the final two-layer construction. In dimensions 32–37 and 39, optimizing collective exchanges and individual sign patterns exposes improvements hidden by separate support-insertion scores and complete sign bundles. In dimension 38, changing the search from the minimal Leech shell to a second lattice shell produces 288 additional points. In dimensions 43 and 45, counting millions of minimal lattice vectors reduces to a finite space of projection signatures whose multiplicities satisfy exact spherical-design moments. A single enlarged line class in dimension 48, combined with low-overlap isometric images, similarly generates new constructions throughout dimensions 49–55. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 每项报告界均由有限证书及精确或严格数值核验支撑。 | 本地原文 TXT 第662行；核验TXT行号 662 | Qiushi Engine carried out the construction searches, mathematical analysis and computational verification. Each discovered mechanism is expressed through explicit geometric or combinatorial conditions. Each reported bound is supported by finite witnesses checked using exact integer and rational arithmetic, lattice and code identities, rigorous interval arithmetic, and finite combinatorial verification. In dimension 25, outward-rounded interval arithmetic certifies the remaining strict inequalities [17]. These mathematical arguments and reproducible certificates make the constructions independently checkable. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文展示Qiushi Engine自主发现 kissing number 构造的数学研究案例。多Agent系统提出组合几何构造，通过提升、分层码、局部替换和壳层补全等步骤改进多个维度的下界，并生成可检查证书。数学对象与证明结果属于01.01；主要贡献是新的构造及界，而非仅展示Agent平台。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。Qiushi Engine研究接吻数问题，并在十九个维度给出新的下界构造。
  - 原文位置：TXT 第444行；原文引文；核验TXT行号 444；引文：we use Qiushi Engine, an autonomous multi-agent research system, to investigate kissing numbers and obtain new lower bounds in nineteen dimensions: 2525, 2727, 3232–3939, 4343, 4545, and 4949–5555.
- 多步行动过程：yes。自主科研系统会依据中间证据修订研究策略，推进多轮数学探索。
  - 原文位置：TXT 第568行；原文引文；核验TXT行号 568；引文：while revising research strategies in response to intermediate evidence.
- 至少一种Agent能力：yes。Qiushi Engine自主开展接吻数构造搜索，并报告多个维度的新下界。
  - 原文位置：TXT 第444行；原文引文；核验TXT行号 444；引文：autonomous multi-agent research system, to investigate kissing numbers and obtain new lower bounds in nineteen dimensions: 2525, 2727, 3232–3939, 4343, 4545, and 4949–5555.
- 明确科研流程角色：yes。工作产出包括由不同结构机制支持的数学构造，而非单一优化器给出的数值候选。
  - 原文位置：TXT 第447行；原文引文；核验TXT行号 447；引文：The resulting constructions arise from distinct structural mechanisms, including coordinated motions of contact layers, labelled direction reuse, joint support exchanges, signed-code replacements, cross-shell lattice constructions

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01 数学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- Formal mathematical research Agent: Qiushi Engine multi-agent autonomous research discovers kissing-number constructions and lower bounds with checkable certificates.

### 2.3 容易混淆的边界

01.01数学对象明确；包括组合、离散几何和编码构造。现有证据足以01.01，不需把通用Agent方法单独作为科研对象。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

多Agent/科研工作流Agent

### 3.2 科研流程角色

科学问题提出；实验设计；工具调用与代码执行；结果分析与验证

Qiushi Engine由协调的数学研究Agent组成，生成构造方案、分工探索证明/计算子任务、检查候选配置并整合可验证证书。

### 3.3 自主能力

Qiushi Engine自主开展接吻数构造搜索，并报告多个维度的新下界。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

产生组合几何构造和数学下界，属直接数学知识贡献；系统贡献是大规模自主构造搜索与验证。

### 4.2 系统流程与组件

从已有 kissing number 构造和界出发；搜索方向复用、Leech提升、分层二进制码及壳层补全等构造；用组合计数和程序检查点对点距离/证书；将可行构造纳入新下界。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

形式化/程序化构造核验及可检查证书；与已知下界比较。主要是数学证明和计算检查，不是实验室验证。

### 5.2 基线、指标与结果

论文报告多个维度的 kissing number 下界提升，例如K(25)≥197580及其他维度构造；数字应按原文定理和证书分别引用。

### 5.3 科学贡献与证据强度

产生组合几何构造和数学下界，属直接数学知识贡献；系统贡献是大规模自主构造搜索与验证。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

建立在球面码、Leech格提升及既有 kissing number 构造之上，通过方向复用和联合替换扩展已知下界。

## 7. 局限性与风险

下界构造不等于最优 kissing number；部分高维结果依赖复杂证书及程序核验；数学子领域交叉，暂不细化至更具体代码。

## 8. 对综述写作的价值

可作为Agent产生可验证纯数学新构造和下界的强代表案例。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

多Agent系统自主生成并验证多个维度的 kissing number 新下界。

### 9.2 速记版 pipeline

从已有 kissing number 构造和界出发；搜索方向复用、Leech提升、分层二进制码及壳层补全等构造；用组合计数和程序检查点对点距离/证书；将可行构造纳入新下界。

### 9.3 标注字段汇总

```text
paper_id=ASD-0973
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O5 开放数学 | kissing number构造为开放数学问题，超越已知下界 | “论文报告多个维度的 kissing number 下界提升” · L105 |
| 验证强度 | V2 计算/仿真/回顾性 | 精确算术和可检查证书验证构造，无独立复现 | “形式化/程序化构造核验及可检查证书；与已知下界比较” · L101 |
| 系统自主性 | L2 闭环执行者 | 系统自主发现构造机制并改变表示 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
