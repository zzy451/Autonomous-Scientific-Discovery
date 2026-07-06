# Reference_PDF

## 这个目录是做什么的

`Reference_PDF/` 用来保存本项目已经拿到本地的论文主文 PDF。

当前 GitHub 公开版本中，这个目录对应的是已经收录并且已经拿到本地 PDF 的文献资料库。目录仍按学科对象分层，便于直接浏览、人工抽查和后续写综述时回到原文。

## 这套数据化文献管理怎么理解

当前 GitHub 上保留的是一套面向公开使用的最小化文献管理结果，核心由三部分组成：

1. `Reference_PDF/`
   已有本地 PDF 的文献原文库。
2. `Data/`
   文献的结构化结果层，包括论文结构化记录、PDF 清单、缺 PDF 清单、分类索引和稳定管理码账本。
3. `scripts/`
   用来读取、检查、构建和查询这些结构化结果的脚本。

一句话：

> `Reference_PDF` 管原文，`Data` 管结构化字段，`scripts` 管处理和查询。

## 有 PDF 和没有 PDF 时分别怎么看

### 1. 已有本地 PDF 的论文

直接在本目录下按学科进入对应子目录查找 PDF。

同时可以配合下面两个结构化文件使用：

- `Data/pdf_manifest.json`
  列出哪些论文已经有本地 PDF，以及对应 `paper_id`、标题、PDF 路径、分类信息和证据状态。
- `Data/papers.jsonl`
  给出每篇已公开论文的完整结构化记录。

### 2. 没有本地 PDF 的论文

这类论文不在 `Reference_PDF/` 里找，而是看：

- `Data/missing_pdf_manifest.json`

这个文件记录当前没有本地主文 PDF、但仍然可以通过 DOI、HTML、publisher page、official page、abstract、supplementary 等路径建立证据链的论文。

## 最常用的几个文件

- `Data/papers.jsonl`
  当前公开论文结构化总表。
- `Data/papers.sqlite`
  当前公开论文查询数据库。
- `Data/classification_code_index.json`
  分类码和分类词表。
- `Data/discipline_code_assignments.jsonl`
  稳定管理码账本。
- `Data/discipline_local_code_registry.jsonl`
  当前论文与稳定管理码的映射快照。
- `Data/pdf_manifest.json`
  已有本地 PDF 的论文清单。
- `Data/missing_pdf_manifest.json`
  没有本地 PDF 但已有替代证据的论文清单。

## 最常用的查询方式

先看整体摘要：

```powershell
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
```

如果想直接读取结构化总表，可查看：

- `Data/papers.jsonl`
- `Data/papers.sqlite`

如果想知道当前公开集里哪些论文已经有本地 PDF，可查看：

- `Data/pdf_manifest.json`

如果想知道哪些论文没有本地 PDF，但仍然已经被记录和管理，可查看：

- `Data/missing_pdf_manifest.json`

## 当前 GitHub 公开集的边界

当前 GitHub 公开版本是一个面向文献资料和结构化结果展示的最小子集，不等于本地完整生产环境。

因此：

- GitHub 上保留了 `Reference_PDF + Data + scripts`
- 公开结构化记录当前收缩为已收录的 `447` 篇 confirmed-core 子集
- 本地完整维护环境中的更多内部过程文件、工作日志和全库中间层并未全部公开

## 如果后续继续维护

这套管理方式的基本逻辑是：

1. 先确认论文是否已有本地 PDF。
2. 有 PDF 的，归入 `Reference_PDF/` 并在结构化层登记。
3. 没有 PDF 的，至少保留 DOI / HTML / official page / abstract 等证据，并登记到 `Data/missing_pdf_manifest.json` 所对应的结构化链路中。
4. 后续统一通过 `Data/` 和 `scripts/` 做查询、筛选和统计，而不是只靠人工翻目录。
