# Andy: A Mathematical Agent for Rigorous Proof and Autonomous Research

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`09`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;09`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 09 | 09.01 工程基础 | 09.01.04 控制科学 | 已落地 |
| 01 | 01.01 数学 | 01.01.07 动力系统与遍历理论 | 已落地 |

- 模块09：混合控制和时滞网络同步，定理加数值验证；建议主归档09。
  - 证据：PDF 第 [7, 15, 16] 页；原文：The control-theoretic contribution is the recovery-window design.

- 模块01：数学动力系统对象可新增01；撤回离散数学码，主归档09。
  - 证据：PDF 第 [7, 9, 15] 页；原文：This case study considers a class of leader-follower heterogeneous networks with switching communication topologies, time-varying delays, and impulse execution delays.

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0976
- 标题：Andy: A Mathematical Agent for Rigorous Proof and Autonomous Research
- 作者：Wang, Zi'an
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.15052
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0976.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Zian_2026_Andy_A_Mathematical_Agent_for_Rigorous_Proof_and_Autonomous_ASD0976.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 研究对象是数学问题生成、定理证明和可审计验证流程。 | 本地原文 TXT 第232行；核验TXT行号 232 | Andy is an autonomous mathematical research agent that turns a mathematical problem into a traceable proof. It solves or verifies a submitted problem, formulates a literature-grounded new problem through a research-value gate, and carries it through proof construction and final verification. It organizes proof steps in an executable DAG, verifies each step independently and binds the result to a certificate, retains verified work whose interfaces remain unchanged during local repair, and records the full path from problem formulation to final proof. The system separates proof generation from correctness evaluation and can acquire, retain, retrieve, and reuse knowledge from existing results. Starting from a self-triggered impulsive consensus result [1], Andy formulates a global exponential leader-follower synchronization problem for delayed heterogeneous networks with switching communication topologies. The proposed hybrid control combines self-triggered impulses with execution delay and continuous feedback over a recovery window. After each delayed impulse, the feedback cancels the delayed error channel until the pre-impulse history leaves the active delay interval. Sufficient conditions for global exponential synchronization are established, Zeno behavior is excluded for both timing sequences, and a numerical example illustrates the result. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | 系统分离求解器与评估器，并以DAG组织逐节点证明及核验。 | 本地原文 TXT 第763行；核验TXT行号 763 | Andy uses a dual-model architecture that separates the roles of solver and evaluator. The main solver uses DeepSeek V4 Pro. It is responsible for solving the original problem, generating proofs, generating new problems, and revising proofs. The mathematical correctness evaluator uses Claude Sonnet 5. It reviews answers and proofs along three dimensions: use of premises, correctness of calculations, and logical completeness. The evaluator cannot directly modify a proof. It can only provide structured verification conclusions, error locations, and revision suggestions. The main solver then completes the revisions. This separation of roles prevents the solver model from approving its own answer without external review. | 高（一手正文；非独立复现） |
| 实验任务与验证 | DAG流程与普通流程在一个代表性案例中作耗时比较。 | 本地原文 TXT 第968行；核验TXT行号 968 | Andy adapts this dependency structure to proof construction. The rigorous DAG proof route first generates only a proof outline, necessary definitions, and lemmas. Andy then represents the proof as a directed acyclic graph. Each node corresponds to a lemma or proof step with explicit inputs, assumptions, and a conclusion. Directed edges represent logical dependencies between nodes. The system first checks node identifiers, dependency relations, and reachability of the target. It then executes the nodes one by one in topological order. | 高（一手正文；非独立复现） |
| 主要结果 | 该案例报告DAG执行耗时降低，但作者指出差值不能全归因于DAG。 | 本地原文 TXT 第1162行；核验TXT行号 1162 | We used Andy twice to process the problem “Study the zeros and monotonicity of the function x3−xx^{3}-x.” An ordinary proof attempt and verification process serves as the baseline. It took 11 hour, 2222 minutes, and 1212 seconds. The DAG process took approximately 3737 minutes and 59.759.7 seconds. The time decreased by approximately 53.8%53.8\%. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 数学案例从已有自触发一致性结果扩展到更复杂的网络控制问题。 | 本地原文 TXT 第1415行；核验TXT行号 1415 | The verified source problem is the self-triggered impulsive consensus problem of Hong and Zhang [1]. It studies switched delay multi-agent systems under self-triggered impulsive control. Andy uses this result as a starting point and asks how its scheduling and impulsive-control structure can be extended to a heterogeneous leader-follower network with switching topology and impulse execution delay. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Andy是一种数学Agent，尝试从已有结果提出有研究价值的新问题，并以引理依赖DAG组织证明步骤。案例研究从自触发脉冲一致性结果出发，提出时滞异质网络切换拓扑下的领导者—跟随者同步问题，构造混合控制充分条件并进行数值验证。主要对象是数学定理和证明，归01.01。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。Andy从既有结果提出新的同步问题，并研究其充分数学条件。
  - 原文位置：TXT 第232行；原文引文；核验TXT行号 232；引文：Starting from a self-triggered impulsive consensus result [1], Andy formulates a global exponential leader-follower synchronization problem for delayed heterogeneous networks with switching communication topologies.
- 多步行动过程：yes。Andy以文献为依据提出新问题，经研究价值门筛选后继续构造证明并完成最终核验。
  - 原文位置：TXT 第232行；原文引文；核验TXT行号 232；引文：formulates a literature-grounded new problem through a research-value gate, and carries it through proof construction and final verification.
- 至少一种Agent能力：yes。系统将引理组织为显式依赖的DAG，逐节点执行、核验、冻结或局部修复，最后组装证明。
  - 原文位置：TXT 第734行；原文引文；核验TXT行号 734；引文：Build a lemma DAG with explicit dependencies Execute, verify, freeze, or locally repair each node Assemble the complete proof and perform final verification Deliver the proof, certificates, literature links, and research
- 明确科研流程角色：yes。系统完整承担数学问题形成、证明构造与验证工作，并允许局部修订失败节点。
  - 原文位置：TXT 第252行；原文引文；核验TXT行号 252；引文：A research system must identify a meaningful question, ground it in relevant literature, construct a long proof, distinguish generation from correctness evaluation, and revise local failures without discarding verified work.

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

- 时滞异质网络在切换拓扑与脉冲控制下的同步定理及其严格证明

### 2.3 容易混淆的边界

01.01为数学研究对象，主要落在控制理论/网络同步。可由数学分类人员复核是否加列01.03系统科学，但目前01.01证据充分。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

单Agent

### 3.2 科研流程角色

科学问题提出；实验设计；工具调用与代码执行；结果分析与验证

Andy采用Solver–Evaluator分离；检索文献形成问题候选，经研究价值门控后拆成引理DAG，由求解器证明节点、验证器检查并进行定向修复，记忆模块保存可复用知识。

### 3.3 自主能力

系统将引理组织为显式依赖的DAG，逐节点执行、核验、冻结或局部修复，最后组装证明。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献为数学控制定理和证明路线；系统贡献为问题生成、价值筛选、分层证明与验证修复工作流。

### 4.2 系统流程与组件

以既有自触发脉冲一致性定理为输入；生成文献扎根的问题；评估原创性/价值；构造恢复窗口并推导充分条件；探索证明路线、执行引理DAG、逐节点形式验证与失败分支修复；最后进行数值模拟。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

数学证明节点由Lean/符号工具核验；通过数值仿真检查所提条件下网络同步行为；另在附录展示失败路线和修复轨迹。

### 5.2 基线、指标与结果

作者报告一个时滞异质网络在切换通信拓扑和混合控制下的全局指数领导者—跟随者同步充分条件；数值验证与定理证明支持该案例。

### 5.3 科学贡献与证据强度

科学贡献为数学控制定理和证明路线；系统贡献为问题生成、价值筛选、分层证明与验证修复工作流。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

区别于只做已有定理证明的自动定理证明器，增加文献扎根问题生成与研究价值门控；承接网络同步和脉冲控制理论。

## 7. 局限性与风险

论文主要展示单个深入案例，研究价值门控和原创性判断仍需专家复核；数值例证不能替代定理假设验证。

## 8. 对综述写作的价值

适合作为Agent从文献问题提出走到严格证明、数值验证的端到端数学研究案例。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Andy提出并证明切换时滞网络同步的新充分条件。

### 9.2 速记版 pipeline

以既有自触发脉冲一致性定理为输入；生成文献扎根的问题；评估原创性/价值；构造恢复窗口并推导充分条件；探索证明路线、执行引理DAG、逐节点形式验证与失败分支修复；最后进行数值模拟。

### 9.3 标注字段汇总

```text
paper_id=ASD-0976
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
