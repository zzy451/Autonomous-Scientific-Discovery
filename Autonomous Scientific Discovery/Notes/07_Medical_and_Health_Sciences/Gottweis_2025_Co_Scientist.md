# Gottweis et al. 2025 - Towards an AI co-scientist

**论文信息**
- 标题：Towards an AI co-scientist
- 作者：Juraj Gottweis et al.
- 年份：2025
- 来源 / venue：arXiv；Nature preview / landing page
- DOI / arXiv / URL：https://arxiv.org/abs/2502.18864；https://doi.org/10.48550/arXiv.2502.18864
- PDF / 本地文件路径：`Reference_PDF/07_Medical_and_Health_Sciences/Gottweis_2025_Co_Scientist.pdf`
- First-hand source checked：项目树外本地归档 arXiv PDF 全文；Nature 落地页摘要
- PDF version：local arXiv PDF canonical copy
- Source-limited：no
- 当前状态：confirmed core；当前落地为 relaxed multi-module `06;07`，主归档模块为 `07`

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| PDF 归档与来源核对 | 已完成 | 本地 arXiv PDF；Nature 落地页摘要 | 当前使用的规范版本是本地 canonical arXiv PDF，足以支持全文级复核 | 高 |
| Agent 纳入 | 是 | arXiv PDF 全文；Nature 摘要 | 系统是 multi-agent AI co-scientist，执行 hypothesis generation、debate、refinement 与迭代筛选 | 高 |
| 医学与健康科学覆盖 | `07` | 本地 PDF 全文 | 论文包含 AML drug repurposing、疾病相关靶点 / 治疗导向验证等明确 biomedical discovery 任务 | 高 |
| 生命科学覆盖 | `06` | 本地 PDF 全文 | 论文同时包含 liver-fibrosis target-discovery 与 AMR 机制解释等生命机制 / 靶点 / 分子生物学对象证据 | 高 |
| `01.04` 存放区判断 | `none` | 本地 PDF 全文 | 虽有 co-scientist 平台外观，但全文提供了具体生物医学与生命科学对象验证，不属于独立通用方法存放区 | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- 判断依据：系统围绕科学家提出的研究目标进行多步假设生成、批评辩论、迭代演化与候选筛选。
- 纳入置信度：高。
- 当前口径说明：本 note 不再保留旧的 `07 / 01.04` 拉扯表述，也不再把该文写成“泛化 co-scientist 压力待定”的未落地案例。

## 2. 科学领域归类

- scientific_object_modules：`06;07`
- object_coverage_mode：`multi_module`
- general_method_bucket：`none`
- primary_module_for_filing：`07`
- 归类理由：
  - `07`：AML drug repurposing 与疾病导向验证使医学与健康科学覆盖稳定成立。
  - `06`：liver-fibrosis target-discovery 与 AMR-related mechanism explanation 提供明确生命科学对象证据。
- 边界说明：其平台化 co-scientist 叙事不能覆盖掉已出现的 concrete object-level evidence，因此不应退回独立 `01.04`。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Planning Agent；Retrieval-augmented Agent；Multi-Agent System；Human-in-the-loop Agent；Hybrid Agent。
- 科研流程角色：科学问题提出；假设生成；证据评估与验证；结果解释；部分实验设计。
- 自主能力：任务分解；计划生成；反馈迭代；自主决策；多 Agent 协作。

## 4. 方法设计

1. 输入科学家目标、约束与先验证据。
2. 多 Agent 生成候选 hypotheses。
3. 通过 debate / critique / refine 迭代改写候选。
4. 借助 tournament evolution 机制筛选更强假设。
5. 输出面向生物医学与生命科学验证的研究建议。

## 5. 实验与验证

- 医学对象证据：AML drug repurposing 候选与相关验证。
- 生命科学对象证据：liver-fibrosis 靶点发现、AMR 相关机制解释。
- 验证方式：benchmark；wet_lab / in-vitro-oriented validation；expert_evaluation。
- 证据强度：experimentally_validated。

## 6. 与已有工作的关系

- 与一般通用 research-agent 系统相比，这篇的关键价值不只是平台架构，而是已经落到具体 biomedical 与 life-science 对象。
- 可与 `Biomni`、`Robin`、`HealthFlow` 等生物医学 Agent 对照，也可与更泛化的 co-scientist / AI Scientist 类系统比较对象覆盖边界。

## 7. 局限性与风险

- 仍依赖 scientist-provided objectives and guidance。
- 平台泛化叙事强，但当前已不构成把记录退回 `01.04` 的充分理由。
- 主要残余风险是模块内细粒度叙述，而不是 `06;07` 的主模块落地。

## 8. 对综述写作的价值

- 适合放入医学与健康科学主节，并在生命科学交叉覆盖处点明其 `06;07` 双模块属性。
- 可支撑“co-scientist 系统已从抽象假设生成走向具体生物医学 / 生命科学对象验证”的论点。
- 推荐引用强度：core。

## 9. 总结

### 9.1 一句话概括

多 Agent co-scientist 系统已在 AML 药物再利用、肝纤维化靶点发现与 AMR 机制解释等具体生命医学对象上落地验证。

### 9.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：06;07
object_coverage_mode：multi_module
general_method_bucket：none
primary_module_for_filing：07
Agent 类型：LLM Agent; Planning Agent; Retrieval-augmented Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：scientific_question_formulation; hypothesis_generation; evidence_assessment_and_validation; result_interpretation; experimental_design
验证方式：benchmark; wet_lab_experiment; expert_evaluation
科学贡献类型：hypothesis; system_platform
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
