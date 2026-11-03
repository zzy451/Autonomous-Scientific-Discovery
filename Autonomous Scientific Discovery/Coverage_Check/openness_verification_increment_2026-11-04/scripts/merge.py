"""Merge the two independent coders into the openness / verification / autonomy increment.

Reads full/sonnet/*.jsonl (primary, Claude Sonnet 5.5) and full/codex/*.jsonl (second coder, Codex gpt-6.1-sol), rejects any record that fails
ov_tools.check (level out of range, quote not verbatim on the cited note line), and writes to
increment/:
  coder_codex.jsonl, coder_sonnet.jsonl         raw, as coded (valid records only)
  invalid_records.jsonl                         rejected records with reasons
  classification_results_662.jsonl / .csv      final codes (primary coder) + second-coder codes + agreement
  expert_review_queue.csv                       disagreement, low confidence, full-text review or contested
  classification_summary.json                   counts, agreement (exact, within-one, weighted kappa)
Usage: python3 merge.py
"""
import csv, json, collections as C
from pathlib import Path
import ov_tools as T

HERE = Path(__file__).parent
INC = HERE / "increment"
AX = list(T.LEVELS)
LV = T.PLEVELS


BROKEN = []                                            # (coder, paper_id) of lines that are not valid JSON


def read_dir(d):
    import re
    recs = {}
    for p in sorted((HERE / "full" / d).glob("*.jsonl")):   # b* first, then r* repairs override
        for line in open(p, encoding="utf-8"):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                m_ = re.search(r'"paper_id"\s*:\s*"(ASD-\d+)"', line)
                BROKEN.append((d, m_.group(1) if m_ else "?"))
                continue
            recs[r.get("paper_id")] = r            # a later duplicate replaces an earlier one
    return recs


def fix_lines(r, cards):
    """If a quote is verbatim on a different note line, correct the line number and record it."""
    c = cards.get(r.get("paper_id"))
    if not c:
        return r
    lines = T.note_lines(c)
    for ax in ("openness", "verification"):
        q = str(r.get(f"{ax}_quote", "")).strip()
        try:
            n = int(r.get(f"{ax}_line"))
        except (TypeError, ValueError):
            n = 0
        if q and not (1 <= n <= len(lines) and q in lines[n - 1]):
            hits = [i for i, ln in enumerate(lines, 1) if q in ln]
            if hits:
                r[f"{ax}_line"] = min(hits, key=lambda i: abs(i - n))
                r.setdefault("line_corrected", []).append(ax)
    return r


PROOF = ("形式化", "Lean", "lean", "proof", "Proof", "证明", "theorem prover", "kernel")


def to_proposal(r):
    """Map coded levels onto the proposal's scales: A0-A3 -> L0-L3; a V3 whose evidence is a machine-checked
    formal proof -> V4 ("V4 证明/复现"). Each change is recorded in `mapping`."""
    r = dict(r)
    notes = []
    if str(r.get("autonomy", "")).startswith("A"):
        r["autonomy"] = "L" + r["autonomy"][1:]
    text = r.get("verification_quote", "") + " " + r.get("verification_rationale_zh", "")
    if r.get("verification") == "V3" and any(k in text for k in PROOF) and "实验" not in text:
        r["verification"] = "V4"; notes.append("V3->V4 formal proof")
    r["mapping"] = notes
    return r


def main():
    cards = {c["paper_id"]: c for c in T.S.papercards()}
    INC.mkdir(exist_ok=True)
    coders, invalid = {}, []
    for name in ("codex", "sonnet"):
        good = {}
        for pid, r in read_dir(name).items():
            r = fix_lines(r, cards)
            errs = T.check(r, cards)
            if errs:
                invalid.append(dict(coder=name, paper_id=pid, errors=errs))
            else:
                good[pid] = to_proposal(r)
        coders[name] = good
        with open(INC / f"coder_{name}.jsonl", "w", encoding="utf-8") as f:
            for pid in sorted(good):
                f.write(json.dumps(good[pid], ensure_ascii=False) + "\n")
    invalid += [dict(coder=c, paper_id=pid, errors=["line is not valid JSON"]) for c, pid in BROKEN]
    invalid = [r for r in invalid if r["paper_id"] not in coders.get(r["coder"], {})]   # superseded by a repair
    with open(INC / "invalid_records.jsonl", "w", encoding="utf-8") as f:
        for r in invalid:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    P, Q = coders["sonnet"], coders["codex"]
    rows = []
    for pid in sorted(cards):
        p, q = P.get(pid), Q.get(pid)
        row = dict(paper_id=pid, title=cards[pid]["title"], year=cards[pid]["year"],
                   scientific_object_modules=";".join(cards[pid]["fields"]), coded=bool(p))
        for ax in AX:
            row[ax] = p[ax] if p else ""
            row[ax + "_second"] = q[ax] if q else ""
            row[ax + "_agree"] = bool(p and q and p[ax] == q[ax])
        for k in ("openness_rationale_zh", "openness_quote", "openness_line", "verification_rationale_zh",
                  "verification_quote", "verification_line", "autonomy_rationale_zh", "contested",
                  "contested_quote", "confidence", "needs_fulltext_review"):
            row[k] = p.get(k, "") if p else ""
        reasons = []
        if not p:
            reasons.append("primary missing or invalid")
        if p and q and any(p[ax] != q[ax] for ax in AX):
            reasons.append("coders disagree: " + ",".join(ax for ax in AX if p[ax] != q[ax]))
        if p and p.get("confidence") == "low":
            reasons.append("low confidence")
        if p and p.get("needs_fulltext_review"):
            reasons.append("needs full-text review")
        if p and p.get("contested"):
            reasons.append("contested")
        row["review_reasons"] = "; ".join(reasons)
        row["corpus_snapshot"] = "2026-11-01"
        row["classification_date"] = "2026-11-04"
        rows.append(row)
    with open(INC / "classification_results_662.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(INC / "classification_results_662.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    queue = [r for r in rows if r["review_reasons"]]
    with open(INC / "expert_review_queue.csv", "w", newline="", encoding="utf-8-sig") as f:
        cols = ["paper_id", "title", "scientific_object_modules", "openness", "openness_second", "verification",
                "verification_second", "autonomy", "autonomy_second", "confidence", "review_reasons"]
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        w.writerows({k: r[k] for k in cols} for r in queue)
    both = [pid for pid in cards if pid in P and pid in Q]
    agree = {}
    if not both:
        both = []
    for ax, lv in LV.items():
        a = [P[i][ax] for i in both]; b = [Q[i][ax] for i in both]
        if not a:
            continue
        agree[ax] = dict(exact=round(sum(x == y for x, y in zip(a, b)) / len(a), 3),
                         within_one=round(sum(abs(lv.index(x) - lv.index(y)) <= 1 for x, y in zip(a, b)) / len(a), 3),
                         weighted_kappa=round(T.wkappa(a, b, lv), 3))
    summary = dict(
        corpus_snapshot="2026-11-01", classification_date="2026-11-04", papers=len(cards),
        coded_primary=len(P), coded_second=len(Q), coded_both=len(both), invalid_records=len(invalid),
        primary_coder="Claude Sonnet 5.5 (claude-sonnet-5-5, via Claude Code on H20)", second_coder="Codex gpt-6.1-sol (high effort, on H20)",
        distribution={ax: dict(sorted(C.Counter(P[i][ax] for i in P).items())) for ax in AX},
        confidence=dict(C.Counter(P[i]["confidence"] for i in P)),
        needs_fulltext_review=sum(bool(P[i].get("needs_fulltext_review")) for i in P),
        contested=sum(bool(P[i].get("contested")) for i in P),
        agreement=agree, expert_review_queue=len(queue))
    (INC / "classification_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
