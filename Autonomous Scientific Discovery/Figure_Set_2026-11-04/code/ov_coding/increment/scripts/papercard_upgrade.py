"""Upgrade the existing papercards (Notes/**.md) with the O / V / L section, in place and idempotently.

Appends (or replaces) a final section "## 10. 问题开放度 · 验证强度 · 系统自主性" built from
increment/classification_results_662.jsonl. Existing lines are untouched, so every quoted line number
in the section still points at the same text. Usage:
  python3 papercard_upgrade.py <repo_root>        # e.g. ../../asd_pr
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
HEAD = "## 10. 问题开放度 · 验证强度 · 系统自主性"
INC_DIR = "Coverage_Check/openness_verification_increment_2026-11-04"
O_NAME = {"O1": "规则世界", "O2": "既定基准", "O3": "新实例", "O4": "需物理检验", "O5": "开放数学", "O6": "开放科学"}
V_NAME = {"V0": "声明", "V1": "基准/内部评测", "V2": "计算/仿真/回顾性", "V3": "物理实验", "V4": "证明/复现"}
L_NAME = {"L0": "工具", "L1": "任务助手", "L2": "闭环执行者", "L3": "自主研究者"}


def cell(s):
    return str(s or "").replace("|", "／").replace("\n", " ").strip()


AX_ZH = {"openness": "开放度", "verification": "验证强度", "autonomy": "自主性"}


def review_zh(reasons):
    out = []
    for part in [p.strip() for p in str(reasons or "").split(";") if p.strip()]:
        if part.startswith("coders disagree:"):
            axes = [AX_ZH.get(a.strip(), a.strip()) for a in part.split(":", 1)[1].split(",")]
            out.append("双编码不一致（" + "、".join(axes) + "）")
        else:
            out.append({"low confidence": "低置信度", "needs full-text review": "需全文复核", "contested": "有争议记录",
                        "primary missing or invalid": "主编码缺失"}.get(part, part))
    return "待专家复核：" + "；".join(out) if out else "无需复核"


def section(r):
    strong = r["verification"] in ("V3", "V4")
    review = review_zh(r["review_reasons"])
    lines = [
        HEAD,
        "",
        f"编码日期：2026-11-04；依据：`{INC_DIR}/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。"
        "引文均为本笔记原文，已用脚本逐字核对行号。",
        "",
        "| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |",
        "|---|---|---|---|",
        f"| 问题开放度 | {r['openness']} {O_NAME[r['openness']]} | {cell(r['openness_rationale_zh'])} | "
        f"“{cell(r['openness_quote'])}” · L{r['openness_line']} |",
        f"| 验证强度 | {r['verification']} {V_NAME[r['verification']]} | {cell(r['verification_rationale_zh'])} | "
        f"“{cell(r['verification_quote'])}” · L{r['verification_line']} |",
        f"| 系统自主性 | {r['autonomy']} {L_NAME[r['autonomy']]} | {cell(r['autonomy_rationale_zh'])} | — |",
        "",
        f"- 强验证（V3–V4）：{'是' if strong else '否'}",
        f"- 置信度：{r['confidence']}；需全文复核：{'是' if r['needs_fulltext_review'] else '否'}；"
        f"争议记录：{'有 · “' + cell(r['contested_quote']) + '”' if r['contested'] else '无'}",
        f"- 复核状态：{review}",
        "",
    ]
    return "\n".join(lines)


def main(repo):
    root = Path(repo) / "Autonomous Scientific Discovery"
    rows = [json.loads(l) for l in open(HERE / "increment" / "classification_results_662.jsonl", encoding="utf-8")]
    import csv
    man = {r["paper_id"]: r for r in csv.DictReader(open(HERE.parent / "source_data" / "core_corpus_manifest.csv",
                                                         encoding="utf-8-sig"))}
    done = skipped = 0
    for r in rows:
        if not r["coded"]:
            skipped += 1; continue
        p = root / man[r["paper_id"]]["note_path"]
        if not p.exists():
            skipped += 1; continue
        text = p.read_text(encoding="utf-8")
        i = text.find("\n" + HEAD)
        base = text[:i] if i >= 0 else text.rstrip("\n")
        p.write_text(base.rstrip("\n") + "\n\n" + section(r), encoding="utf-8")
        done += 1
    print("upgraded", done, "papercards; skipped", skipped)


if __name__ == "__main__":
    main(sys.argv[1])
