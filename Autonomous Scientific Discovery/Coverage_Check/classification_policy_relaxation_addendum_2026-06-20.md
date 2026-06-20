# 多模块分类口径放松备忘（2026-06-20）

## 结论

从本备忘起，项目分类采用更宽松的“领域实验覆盖”口径：只要一篇纳入文献在某一科学领域中做了可识别的实验、验证、benchmark task、case study 或结果报告，就可以归入该领域模块。

这意味着多模块归类不再要求每个模块都构成论文的核心科学贡献，也不再要求每个领域实验都是同等重要的主线贡献。分类依据仍然不是 Agent 技术、系统名称或论文自称的通用性，而是论文实际做了哪些具体科学对象相关实验。

## 对 `01.04` 的影响

`01.04` 继续保留，但只作为独立的 ASD/general 方法存放区，不再作为正式科学对象主类。只有同时满足以下条件的文献才应进入 `01.04`：

1. 提出 ASD / general research-agent / general scientific workflow / general benchmark；
2. 没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告；
3. 其验证停留在通用能力、抽象任务、流程框架或领域无关评测层面。

如果论文既提出通用 ASD 方法，又在生物、物理、化学、材料、医学、地球环境、工程等领域做了具体实验或案例验证，应优先进入对应具体模块；`01.04` 可作为方法属性或存放区标签记录，但不能替代具体模块。

## 对已完成 451 篇审计的影响

此前 `multi_module_reclassification_*_2026-06-20.md` 系列审计采用的是较保守口径：多模块归入需要较强对象层面贡献证据。现在该轮结果应视为“保守基线”，不能直接代表新口径下的最终多模块分布。

后续应重开以下类型文献：

- 原归入 `01.04`，但论文中出现了具体学科实验、benchmark task 或 case study 的文献；
- 通用科研 Agent / AI co-scientist / scientific workflow 论文中包含多领域 demo 的文献；
- benchmark 或平台论文中每个任务可明确对应科学对象模块的文献；
- 综述笔记或主列表备注中出现 “biology / physics / chemistry / materials / medicine / earth / engineering experiments” 等跨领域实验线索的文献。

## 典型边界样本

`ASD-0844 Science Earth` 不应再仅因其是通用 ASD 方法或平台型论文而停留在 `01.04`。如果已确认其包含生命科学实验和物理/复杂系统实验，则新口径下应至少记录对应具体模块，例如：

- `06`：生命科学实验，例如 pan-cancer single-cell / biological data analysis 相关验证；
- `01.03` 或 `02`：若实验对象是复杂系统、动力系统、Kuramoto / nonlinear system 等一般系统规律，优先 `01.03`；若实验对象是明确物理系统或物理过程，则进入 `02`。

最终以论文笔记和原文证据为准，但原则上不能只保留 `01.04`。

## 主列表 schema 建议

现有 `Main class / Secondary class` schema 不足以稳定表达多模块归类。建议下一轮迁移时新增或统一以下字段：

- `scientific_object_modules`
- `object_coverage_mode`
- `has_concrete_object_experiments`
- `general_method_bucket`
- `module_assignment_evidence`
- `primary_module_for_filing`
- `multi_module_object_coverage_note`

在 schema 迁移完成前，不建议直接用旧 `Main class` 字段覆盖多模块事实；可以先在审计报告中记录建议模块，再集中迁移主列表。
