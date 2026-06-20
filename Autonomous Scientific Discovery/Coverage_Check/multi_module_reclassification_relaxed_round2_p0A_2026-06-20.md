# 451 confirmed 文献 relaxed multi-module round 2 / P0-A 审计报告

> 日期：2026-06-20  
> 范围：Round 2 full-text boundary queue 中首批 P0 `01.04` / general-agent boundary 记录。  
> 本批复核记录：`ASD-0004`, `ASD-0006`, `ASD-0013`, `ASD-0032`。  
> 执行口径：优先使用论文原文 / arXiv / DOI landing page 等一手来源；旧 Notes 只作为定位线索。高置信变更同步写入 master list remarks 与对应 Note。

## 一、结论摘要

本批 4 条记录中，3 条可高置信退出 independent `01.04` only treatment，并写入 relaxed overlay：

| Paper ID | 处理结果 | relaxed scientific_object_modules | general_method_bucket | Note 是否已同步 |
|---|---|---|---|---|
| `ASD-0004` | 从 independent `01.04` 改为多模块对象覆盖 | `01;03;06;09;10` | `none` | yes |
| `ASD-0006` | 暂不改；继续全文复核 | uncertain | uncertain | yes, source-limited block only |
| `ASD-0013` | 从 independent `01.04` 改为正式对象模块 | `01` | `none` | yes |
| `ASD-0032` | 从 independent `01.04` 改为正式对象模块 | `01` | `none` | yes |

## 二、逐条判定

### `ASD-0004` InternAgent

- 一手来源：arXiv abstract `https://arxiv.org/abs/2505.16938`；ar5iv HTML `https://ar5iv.org/html/2505.16938v3`。
- 复核结论：不再保留为 independent `01.04` only。
- 依据：论文/HTML 中列出的 12 个任务不只是抽象 workflow demo，而是包含可识别对象层实验或 benchmark task。AI/CV/NLP/geometric-VLM 任务支持 `01`；reaction yield prediction 与 molecular dynamics 支持 `03`；transcription perturbation 与 enhancer activity prediction 支持 `06`；power-flow / transformer-temperature 工程数据支持 `09`；autonomous-driving point-cloud detection 支持 `10`。
- 本轮动作：master list remarks 增加 `RelaxedRound2P0A2026-06-20`；Note 顶部加入 relaxed round-2 revision block。

### `ASD-0006` DORA AI Scientist

- 一手来源尝试：DOI / bioRxiv `https://doi.org/10.1101/2025.03.06.641840`；直接 bioRxiv 页面仍无法通过当前路径稳定读取。
- 复核结论：不直接改分类。
- 依据：现有可读证据仍不足以判断 DORA 是否有具体生命科学 / 生物医学对象实验，也不足以高置信从 `06` 移入 independent `01.04`。
- 本轮动作：master list 不变；Note 顶部加入 source-limited revision block；继续留在 Round 2 full-text boundary queue。

### `ASD-0013` The AI Scientist-v2

- 一手来源：arXiv abstract `https://arxiv.org/abs/2504.08066`。
- 复核结论：从 independent `01.04` only 迁出，记录为 `scientific_object_modules=01`。
- 依据：论文报告的对象层验证是 AI/ML 研究本身，包括 ML hypothesis generation、code experiment execution、data analysis、paper generation，以及 AI 生成 ML 论文的 workshop peer review。按当前规则，AI/ML 计算研究对象属于 `01`，不是无对象 general-method bucket。
- 本轮动作：master list remarks 增加 `RelaxedRound2P0A2026-06-20`；Note 顶部加入 relaxed round-2 revision block。

### `ASD-0032` CodeScientist

- 一手来源：arXiv abstract `https://arxiv.org/abs/2503.22708`。
- 复核结论：从 independent `01.04` only 迁出，记录为 `scientific_object_modules=01`。
- 依据：论文报告的实验对象包括 software artifacts、agent / virtual-environment tasks、code experiments、candidate tasks / agents / metrics / data、code review 与 replication attempts，属于形式、信息与计算科学中的具体计算研究对象。
- 本轮动作：master list remarks 增加 `RelaxedRound2P0A2026-06-20`；Note 顶部加入 relaxed round-2 revision block。

## 三、计数更新

本轮前 relaxed overlay：

- `01:47, 02:33, 03:73, 04:103, 05:34, 06:66, 07:64, 08:3, 09:35, 10:23, 11:31`
- Expanded module assignment count: `512`
- Independent `01.04` general-method bucket count: `32`

本轮后 relaxed overlay：

- `01:50, 02:33, 03:74, 04:103, 05:34, 06:67, 07:64, 08:3, 09:36, 10:24, 11:31`
- Expanded module assignment count: `519`
- Independent `01.04` general-method bucket count: `29`

变化说明：

- `ASD-0004` 从 independent `01.04` only 变为 `01;03;06;09;10`，expanded assignment `+5`，independent `01.04` `-1`。
- `ASD-0013` 从 independent `01.04` only 变为 `01`，expanded assignment `+1`，independent `01.04` `-1`。
- `ASD-0032` 从 independent `01.04` only 变为 `01`，expanded assignment `+1`，independent `01.04` `-1`。
- `ASD-0006` 未改计数。

## 四、剩余风险

- `ASD-0006` 仍是 source-limited 边界项，不能用现有 note 或第三方摘要作高置信迁移。
- `ASD-0004` 的 relaxed 多模块覆盖比较宽，但每个模块都来自任务清单中的可识别对象层实验；后续若做全文页码级证据表，可进一步细分到 task-level evidence。
- 本批不改变 legacy `Main class` / `Secondary class` 字段，等待后续 schema migration。
