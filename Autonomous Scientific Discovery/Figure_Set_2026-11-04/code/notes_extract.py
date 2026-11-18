"""Extract auditable signals from the 662 papercard notes (Notes/**.md, commit 60f8bad).

Per paper: the problem statement (section 2.2 '最终科学问题'), verbatim, and the Evidence-Log validation row.
Regex flags for uncertainty, replication, demos and code release were tried and dropped after an audit:
they matched template and process text (e.g. 'needs more external validation'), so they would invert
meaning. Only verbatim extraction is kept.
Writes derived/note_signals.csv and derived/leaderboard.csv. Usage: python3 notes_extract.py
"""
import csv, re, collections as C
from pathlib import Path
import style as S, proxies as X

NOTES = S.SRC / "notes" / "Autonomous Scientific Discovery"
STOP = {"PDF", "LLM", "LLMs", "AI", "API", "GPT", "DOI", "URL", "Sec", "Fig", "Table", "Tables", "Appendix", "Agent",
        "Agents", "Level", "HTML", "PMC", "Abstract", "RAG", "ML", "DL", "RL", "CI", "OK", "QA", "NLP"}
BENCH = re.compile(r"\b([A-Z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*(?:Bench|bench|QA|-\d+)[A-Za-z0-9-]*|"
                   r"[A-Z][A-Za-z]*Bench[A-Za-z0-9-]*|[A-Z]{2,}[A-Za-z0-9]*-?(?:Bench|QA|\d{2,}))\b")


def row(text, key):
    m = re.search(r"^\|\s*" + key + r"\s*\|(.+)$", text, re.M)
    return " ".join(c.strip() for c in m.group(1).split("|") if c.strip()) if m else ""


def main():
    cards = S.papercards(); px = X.load()
    sig, rows = [], []
    for c in cards:
        p = NOTES / c["note_path"]
        text = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
        prob = re.search(r"最终科学问题[：:]\s*(.+)", text)
        val = row(text, "实验验证")
        out = dict(paper_id=c["paper_id"], note_found=bool(text), problem=prob.group(1).strip() if prob else "",
                   validation_row=val[:400])
        out["benchmarks"] = ";".join(sorted({b for b in BENCH.findall(val) if b not in STOP}))
        sig.append(out)
        E, L = px[c["paper_id"]]
        rows.append(dict(field=";".join(c["fields"]), paper_id=c["paper_id"], year=c["year"],
                         system=c["title"].split(":")[0].strip()[:60], problem=out["problem"],
                         evidence_tier="" if E is None else f"E{E}", loop_reach="" if L is None else f"L{L}",
                         mechanism=c["decision_class"], venue=c["source"], link=c["doi_or_url"]))
    with open(S.DER / "note_signals.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(sig[0])); w.writeheader(); w.writerows(sig)
    rows.sort(key=lambda r: (r["field"].split(";")[0] if r["field"] else "99", -(int(r["evidence_tier"][1:]) if r["evidence_tier"] else -1),
                             -(int(r["loop_reach"][1:]) if r["loop_reach"] else -1), r["year"], r["paper_id"]))
    with open(S.DER / "leaderboard.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    n = len(sig)
    print("notes found", sum(s["note_found"] for s in sig), "/", n, "problem", sum(bool(s["problem"]) for s in sig))
    bc = C.Counter(b for s in sig for b in s["benchmarks"].split(";") if b)
    print("named suites in validation rows", len(bc))
    write_md(rows)


def write_md(rows):
    """Full leaderboard as Markdown: one ranked table per field, verbatim problem statement, live link."""
    key = lambda r: (-(int(r["evidence_tier"][1:]) if r["evidence_tier"] else -1),
                     -(int(r["loop_reach"][1:]) if r["loop_reach"] else -1), int(r["year"]), r["paper_id"])
    status = {"E3": "strong (V3–V4)", "E2": "computed (V2)", "E1": "benchmark (V1)",
              "E0": "claim (V0)", "": "not coded"}
    out = ["# Leaderboard of closed loops\n",
           "Within each field, papers are ranked by verification strength (V3–V4 > V2 > V1 > V0), then system autonomy "
           "(L3 first), then the earliest year. The problem column quotes the papercard's 最终科学问题 verbatim; it "
           "is empty where the note has no such line. Snapshot 2026-11-01, commit 60f8bad.\n"]
    for f in S.FIELDS:
        ent = sorted([r for r in rows if f in r["field"].split(";")], key=key)
        out += [f"\n## {f} · {S.FNAME[f]} ({len(ent)} papers)\n",
                "| # | ID | System | Year | Status | Reach | Mechanism | Problem | Link |", "|---|---|---|---|---|---|---|---|---|"]
        for i, r in enumerate(ent, 1):
            prob = r["problem"].replace("|", "/")
            prob = prob if len(prob) <= 90 else prob[:89] + "…"
            out.append(f"| {i} | {r['paper_id']} | {r['system'].replace('|', '/')} | {r['year']} | "
                       f"{status[r['evidence_tier']]} | {r['loop_reach'] or '–'} | {r['mechanism']} | {prob} | "
                       f"[link]({r['link']}) |")
    (S.DER / "LEADERBOARD.md").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
