# Relaxed multi-module round-2 skip list

> Date: 2026-06-21  
> Purpose: provide a practical skip list for the next manual review restart.  
> Rule: records in the skip list already have high-confidence classification closure plus synchronized note revision or an explicitly closed keep-as-is boundary decision. Records still listed in `multi_module_reclassification_relaxed_round2_fulltext_boundary_queue_2026-06-20.md` as open follow-up items should not be skipped.

## 1. 可直接绕过的已收口记录

以下 `89` 篇记录已经完成本轮可操作意义上的分类收口，可在下一轮人工复核中先跳过：

```text
ASD-0003 ASD-0004 ASD-0006 ASD-0008 ASD-0013 ASD-0014 ASD-0032 ASD-0033 ASD-0035
ASD-0048 ASD-0054 ASD-0055 ASD-0056 ASD-0060 ASD-0062 ASD-0064 ASD-0069 ASD-0096
ASD-0100 ASD-0141 ASD-0151 ASD-0254 ASD-0276 ASD-0290 ASD-0385 ASD-0447 ASD-0510
ASD-0520 ASD-0522 ASD-0523 ASD-0525 ASD-0531 ASD-0537 ASD-0539 ASD-0540 ASD-0543
ASD-0545 ASD-0547 ASD-0548 ASD-0553 ASD-0554 ASD-0564 ASD-0609 ASD-0651 ASD-0660
ASD-0662 ASD-0663 ASD-0664 ASD-0669 ASD-0671 ASD-0673 ASD-0676 ASD-0693 ASD-0696
ASD-0697 ASD-0702 ASD-0703 ASD-0709 ASD-0710 ASD-0711 ASD-0712 ASD-0713 ASD-0715
ASD-0719 ASD-0721 ASD-0722 ASD-0731 ASD-0736 ASD-0739 ASD-0740 ASD-0742 ASD-0743
ASD-0744 ASD-0745 ASD-0773 ASD-0782 ASD-0787 ASD-0790 ASD-0792 ASD-0811 ASD-0820
ASD-0844 ASD-0845 ASD-0856 ASD-0866 ASD-0868 ASD-0869 ASD-0870 ASD-0871
```

## 2. 暂时不要绕过的继续审记录

以下 `34` 篇仍保留 open boundary / full-text / core-strength follow-up 压力，下一轮不建议跳过：

```text
ASD-0034 ASD-0037 ASD-0049 ASD-0070 ASD-0466 ASD-0478 ASD-0519 ASD-0541 ASD-0544
ASD-0587 ASD-0596 ASD-0599 ASD-0659 ASD-0665 ASD-0668 ASD-0682 ASD-0700 ASD-0737
ASD-0751 ASD-0752 ASD-0759 ASD-0761 ASD-0766 ASD-0768 ASD-0769 ASD-0775 ASD-0793
ASD-0797 ASD-0803 ASD-0810 ASD-0817 ASD-0818 ASD-0838 ASD-0850
```

## 3. 使用说明

- 本文件是“下一轮人工重开时的操作跳表”，不是新的分类结论源文件。
- 真正的分类事实仍以：
  - `Paper_Lists/agent_master_paper_list.md`
  - `Coverage_Check/multi_module_reclassification_relaxed_round2_fulltext_boundary_queue_2026-06-20.md`
  - 各 `round2_p*` 审计报告
  为准。
- `ASD-0737` 特别保留在继续审集合中。虽然它已经从 independent `01.04` 迁到 `01`，但当前仍挂着是否额外触发 `07/09` 的 follow-up 压力，因此不放入 skip list。
