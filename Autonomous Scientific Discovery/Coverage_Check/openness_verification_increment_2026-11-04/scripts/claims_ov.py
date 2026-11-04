"""Re-test the proposal's §2 claims on the coded O / V / A axes (primary coder; both-coder agreement subset).

Reads increment/classification_results_662.jsonl, writes increment/claims_analysis.json and prints a summary.
Claims (proposal §2(2)): autonomy and verification run opposite (L3: 0/12 strong; L1: 24/59 strong);
evidence thins over time (weak V0-V1 by era 0/1/4/13; strong V3-V4 share 5/7 -> 12/41); and §2(3)(i) a
frontier: per field and era, the highest openness held by at least one strongly verified (V>=3) paper.
Usage: python3 claims_ov.py
"""
import json, sys, collections as C
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
import style as S  # noqa: E402

INC = HERE / "increment"
ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
lv = lambda code: int(code[1:]) if code else None


def wilson(k, n):
    p, lo, hi = S.wilson(k, n)
    return dict(k=k, n=n, share=round(p, 3) if n else None, ci95=[round(lo, 3), round(hi, 3)] if n else None)


def main():
    rows = [json.loads(l) for l in open(INC / "classification_results_662.jsonl", encoding="utf-8")]
    era = {c["paper_id"]: c["era"] for c in S.papercards()}
    coded = [r for r in rows if r["coded"]]
    agreed = [r for r in coded if r["verification_agree"] and r["autonomy_agree"]]
    out = {}
    for name, sub in (("primary", coded), ("both_coders_agree_on_V_and_A", agreed)):
        res = {}
        res["strong_V_by_autonomy"] = {f"L{a}": wilson(sum(lv(r["verification"]) >= 3 for r in sub if lv(r["autonomy"]) == a),
                                                       sum(lv(r["autonomy"]) == a for r in sub)) for a in range(4)}
        res["by_era"] = {}
        for e in ERAS:
            s = [r for r in sub if era[r["paper_id"]] == e]
            res["by_era"][e] = dict(n=len(s), weak_V0_V1=sum(lv(r["verification"]) <= 1 for r in s),
                                    strong_V3_V4=wilson(sum(lv(r["verification"]) >= 3 for r in s), len(s)),
                                    openness=dict(sorted(C.Counter(r["openness"] for r in s).items())))
        out[name] = res
    # frontier on the primary codes: highest O per field with >= 1 V>=3 paper, cumulative by era
    front = {}
    for f in S.FIELDS:
        front[f] = {}
        for k, e in enumerate(ERAS):
            upto = set(ERAS[:k + 1])
            os_ = [lv(r["openness"]) for r in coded if f in r["scientific_object_modules"].split(";")
                   and era[r["paper_id"]] in upto and lv(r["verification"]) >= 3]
            front[f][e] = f"O{max(os_)}" if os_ else None
        att = [lv(r["openness"]) for r in coded if f in r["scientific_object_modules"].split(";")]
        front[f]["highest_attempted"] = f"O{max(att)}" if att else None
    out["frontier_primary"] = front
    out["proposal_reference"] = {"strong_at_L3": "0/12", "strong_at_L1": "24/59", "weak_by_era": "0/1/4/13",
                                 "strong_share_first_last_era": "5/7 -> 12/41",
                                 "note": "84 hand-coded chronicle cases; eras and autonomy scale differ from this corpus"}
    (INC / "claims_analysis.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    p = out["primary"]
    print("strong V>=3 by autonomy:", {a: f"{v['k']}/{v['n']}" for a, v in p["strong_V_by_autonomy"].items()})
    print("weak V0-V1 by era:", [p["by_era"][e]["weak_V0_V1"] for e in ERAS])
    print("strong share by era:", [f"{p['by_era'][e]['strong_V3_V4']['k']}/{p['by_era'][e]['n']}" for e in ERAS])
    print("frontier 2026:", {f: front[f]["2026"] for f in S.FIELDS})


if __name__ == "__main__":
    main()
