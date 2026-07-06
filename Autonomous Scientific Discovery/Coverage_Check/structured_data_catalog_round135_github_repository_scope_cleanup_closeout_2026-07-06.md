# structured_data_catalog_round135_github_repository_scope_cleanup_closeout_2026-07-06

## 本轮目标

按用户要求清理 GitHub 仓库范围，只保留学长那套逻辑整理后的 `Autonomous Scientific Discovery` 项目主体，不再把其他无关项目或仓库级协作配置一起公开到远端主分支。

## 本轮修改

### 1. 收紧仓库公开范围

更新仓库根目录 `.gitignore`，把以下非 ASD 主体目录或仓库级协作文件明确列为本地保留、GitHub 不再继续跟踪：

- `.github/`
- `CODEOWNERS`
- `LLM Survey/`
- `Scientific Discovery by Agents/`
- `codex_agents_sdk_demo/`

### 2. 从版本库中移除非 ASD 主体内容

对以下已跟踪内容执行 `git rm --cached`，仅从 Git 历史的当前快照中删除，不删除本地工作副本：

- `.github/`
- `CODEOWNERS`
- `LLM Survey/`
- `Scientific Discovery by Agents/`

这样 GitHub `main` 在本轮提交后将只保留：

- `Autonomous Scientific Discovery/` 主体
- 必要的根目录 Git 配置文件（如 `.gitattributes`、`.gitignore`）

## 验证

运行：

```powershell
python "Autonomous Scientific Discovery/scripts/run_structured_data_pipeline.py" --with-execution-audit
```

预期验证点：

- ASD 主体结构化流程仍然可以正常执行
- `export -> check -> build -> execution-audit` 不受仓库范围清理影响
- 本轮清理不触碰四类 owner fact source 的事实内容

## 结果定义

当本轮提交并推送后，GitHub 仓库公开范围将收缩为以 `Autonomous Scientific Discovery/` 为中心的项目主体，不再混入其他综述项目、Agent 资料库或仓库级协作模板文件。
