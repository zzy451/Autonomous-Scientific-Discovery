# 451 confirmed 文献 relaxed multi-module round 2 / P0-B 审计报告

> 日期：2026-06-20
> 范围：Round 2 full-text boundary queue 中第二批 P0 `01.04` / general-agent boundary 记录。
> 本批复核记录：`ASD-0048`, `ASD-0060`, `ASD-0062`。
> 执行口径：优先使用论文原文 / arXiv / PDF 文本等一手来源；旧 Notes 只作为定位线索。高置信变更同步写入 master list remarks 与对应 Note。

## 一、结论摘要

本批 3 条记录均可高置信退出 independent `01.04` only treatment，并写入 relaxed overlay：

| Paper ID | 处理结果 | relaxed scientific_object_modules | general_method_bucket | Note 是否已同步 |
|---|---|---|---|---|
| `ASD-0048` | 从 independent `01.04` 改为正式对象模块 | `01` | `none` | yes |
| `ASD-0060` | 从 independent `01.04` 改为多模块对象覆盖 | `03;04;07` | `none` | yes |
| `ASD-0062` | 从 independent `01.04` 改为多模块对象覆盖 | `01;02;04` | `none` | yes |

## 二、逐条判定

### `ASD-0048` Dolphin

- 一手来源：arXiv abstract / PDF `https://arxiv.org/abs/2501.03916`。
- 复核结论：不再保留为 independent `01.04` only，记录为 `scientific_object_modules=01`。
- 依据：论文的 closed-loop auto-research 验证对象是可识别的形式 / 计算研究任务，包括 ModelNet40 3D classification、CIFAR-100 image classification、SST-2 sentiment classification、MLE-bench ML-engineering tasks 与代码实验结果。按当前规则，这些 AI/ML/计算任务构成 `01` 对象层实验，而不是无对象 general-method demo。
- 本轮动作：master list remarks 增加 `RelaxedRound2P0B2026-06-20`；补齐 arXiv URL；Note 顶部加入 relaxed round-2 revision block。

### `ASD-0060` PiFlow

- 一手来源：arXiv abstract / PDF `https://arxiv.org/abs/2505.15047`。
- 复核结论：不再保留为 independent `01.04` only，记录为 `scientific_object_modules=03;04;07`。
- 依据：PiFlow 虽是 principle-aware multi-agent 方法论文，但其验证任务不是抽象 workflow 测试。Nanohelix Optimization 与 Superconductor Optimization 支持 `04`；Molecular Bio-activity Optimization 使用 ChEMBL molecules、chemical space 与 pChEMBL 支持 `03`；同一任务明确以 lead compound / drug-discovery bioactivity 为目标，支持 `07`。
- 未记录 `06`：PDF 中 MBO 的对象是 chemical compounds / molecules 与 drug-discovery bioactivity，而不是蛋白质、细胞、基因或生命机制本身；因此不把旧候选 `06` 作为本轮高置信模块。
- 本轮动作：master list remarks 增加 `RelaxedRound2P0B2026-06-20`；Note 顶部加入 relaxed round-2 revision block。

### `ASD-0062` Empowering Scientific Workflows with Federated Agents

- 一手来源：arXiv abstract / PDF `https://arxiv.org/abs/2505.05428`。
- 复核结论：不再保留为 independent `01.04` only，记录为 `scientific_object_modules=01;02;04`。
- 依据：论文确实 infrastructure-heavy，但 full text 中的 case studies 具有可识别对象层任务。middleware / microbenchmark / decentralized-learning evaluations 支持 `01`；astronomy instrument-calibration、telescope optical-parameter estimation 与 sky-image alignment 支持 `02`；MOF ligand assembly、molecular dynamics screening 与 CO2 adsorption materials workflow 支持 `04`。
- 未记录 `09`：HPC / federated infrastructure 是执行 substrate，不是本轮的最终工程对象；不因系统部署在工程基础设施上而归入 `09`。
- 本轮动作：master list remarks 增加 `RelaxedRound2P0B2026-06-20`；Note 顶部加入 relaxed round-2 revision block。

## 三、计数更新

本轮前 relaxed overlay：

- `01:50, 02:33, 03:74, 04:103, 05:34, 06:67, 07:64, 08:3, 09:36, 10:24, 11:31`
- Expanded module assignment count: `519`
- Independent `01.04` general-method bucket count: `29`

本轮后 relaxed overlay：

- `01:52, 02:34, 03:75, 04:105, 05:34, 06:67, 07:65, 08:3, 09:36, 10:24, 11:31`
- Expanded module assignment count: `526`
- Independent `01.04` general-method bucket count: `26`

变化说明：

- `ASD-0048` 从 independent `01.04` only 变为 `01`，expanded assignment `+1`，independent `01.04` `-1`。
- `ASD-0060` 从 independent `01.04` only 变为 `03;04;07`，expanded assignment `+3`，independent `01.04` `-1`。
- `ASD-0062` 从 independent `01.04` only 变为 `01;02;04`，expanded assignment `+3`，independent `01.04` `-1`。

## 四、剩余风险

- `ASD-0062` 仍应在正文中作为 infrastructure-heavy case 谨慎表述：它的科学对象覆盖来自 case studies，不表示论文主贡献等同于材料发现或天文学发现。
- `ASD-0060` 的 `03/07` 边界来自同一 MBO 任务；后续表格若只展示 primary filing，可用 `04`，但 relaxed overlay 应保留 `03;04;07`。
- 本批不改变 legacy `Main class` / `Secondary class` 字段，等待后续 schema migration。
