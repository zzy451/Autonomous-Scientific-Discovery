"""O/V/A coding tools: build per-paper evidence packets, pick the pilot sample, verify coder output.

  python3 ov_tools.py packets            # packets/<paper_id>.txt for all 662 core papers
  python3 ov_tools.py pilot [n]          # pilot_ids.txt: stratified sample (default 30)
  python3 ov_tools.py verify FILE.jsonl  # schema + verbatim-quote check against the original note
  python3 ov_tools.py agree A.jsonl B.jsonl   # per-axis exact agreement and linearly weighted kappa
"""
import json, re, sys, random, collections as C
from pathlib import Path

HERE = Path(__file__).parent
MF = HERE.parent
sys.path.insert(0, str(MF))
import style as S, proxies as X  # noqa: E402

NOTES = S.SRC / "notes" / "Autonomous Scientific Discovery"
PK = HERE / "packets"
KEEP = ("## Evidence Log", "## 0. 摘要翻译", "## 5. 实验与验证", "## 7. 局限性与风险")
LEVELS = {"openness": [f"O{i}" for i in range(1, 7)], "verification": [f"V{i}" for i in range(0, 5)],
          "autonomy": [f"A{i}" for i in range(0, 4)]}
PLEVELS = {"openness": LEVELS["openness"], "verification": LEVELS["verification"],
           "autonomy": [f"L{i}" for i in range(0, 4)]}   # proposal scales, after merge.to_proposal
CAP = 11000                                         # characters per packet


def note_lines(card):
    p = NOTES / card["note_path"]
    return p.read_text(encoding="utf-8", errors="ignore").splitlines() if p.exists() else []


def packet(card):
    lines = note_lines(card)
    keep, on = [], False
    for i, ln in enumerate(lines, 1):
        if i <= 14:                                 # title / year / venue / link block
            keep.append((i, ln)); continue
        if ln.startswith("## "):
            on = ln.startswith(KEEP)
        if on or "最终科学问题" in ln:
            keep.append((i, ln))
    out, n = [f"PAPER {card['paper_id']} | {card['title']} | {card['year']} | fields {';'.join(card['fields'])}"], 0
    for i, ln in keep:
        if not ln.strip():
            continue
        s = f"L{i}: {ln}"
        if n + len(s) > CAP:
            out.append("[packet truncated]"); break
        out.append(s); n += len(s)
    return "\n".join(out)


def cmd_packets():
    PK.mkdir(exist_ok=True)
    cards = S.papercards()
    for c in cards:
        (PK / f"{c['paper_id']}.txt").write_text(packet(c), encoding="utf-8")
    sizes = [len((PK / f"{c['paper_id']}.txt").read_text(encoding="utf-8")) for c in cards]
    print(len(cards), "packets; chars min/mean/max", min(sizes), sum(sizes) // len(sizes), max(sizes))


def cmd_pilot(n=30):
    cards = S.papercards(); px = X.load()
    strata = C.defaultdict(list)                    # era x proxy evidence tier
    for c in cards:
        strata[(c["era"], px[c["paper_id"]][0])].append(c["paper_id"])
    rng = random.Random(20261104)
    keys = sorted(strata, key=str)
    picks = []
    while len(picks) < n:
        for k in keys:
            pool = [p for p in strata[k] if p not in picks]
            if pool and len(picks) < n:
                picks.append(rng.choice(pool))
    (HERE / "pilot_ids.txt").write_text("\n".join(sorted(picks)) + "\n")
    print(len(picks), "pilot ids across", len(keys), "strata")


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def check(rec, cards):
    errs = []
    c = cards.get(rec.get("paper_id"))
    if not c:
        return ["unknown paper_id"]
    for ax, lv in LEVELS.items():
        if rec.get(ax) not in lv:
            errs.append(f"{ax}={rec.get(ax)!r} not in {lv[0]}..{lv[-1]}")
    lines = note_lines(c)
    for ax in ("openness", "verification"):
        q, ln = str(rec.get(f"{ax}_quote", "")).strip(), rec.get(f"{ax}_line")
        try:
            ln = int(ln)
        except (TypeError, ValueError):
            errs.append(f"{ax}_line not an integer"); continue
        if not q:
            errs.append(f"{ax}_quote empty")
        elif not (1 <= ln <= len(lines)) or q not in lines[ln - 1]:
            errs.append(f"{ax}_quote not verbatim on note line {ln}")
    if rec.get("confidence") not in ("high", "medium", "low"):
        errs.append("confidence invalid")
    return errs


def cmd_verify(path):
    cards = {c["paper_id"]: c for c in S.papercards()}
    recs = load(path)
    bad = {r.get("paper_id"): check(r, cards) for r in recs}
    bad = {k: v for k, v in bad.items() if v}
    print(f"{path}: {len(recs)} records, {len(recs) - len(bad)} valid, {len(bad)} invalid")
    for k, v in list(bad.items())[:20]:
        print(" ", k, "; ".join(v))
    return bad


def wkappa(a, b, levels):
    idx = {l: i for i, l in enumerate(levels)}
    k = len(levels)
    pairs = [(idx[x], idx[y]) for x, y in zip(a, b)]
    if not pairs:
        return float("nan")
    w = lambda i, j: 1 - abs(i - j) / (k - 1)
    po = sum(w(i, j) for i, j in pairs) / len(pairs)
    pa = C.Counter(i for i, _ in pairs); pb = C.Counter(j for _, j in pairs)
    n = len(pairs)
    pe = sum(w(i, j) * pa[i] / n * pb[j] / n for i in range(k) for j in range(k))
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def cmd_agree(pa, pb):
    A = {r["paper_id"]: r for r in load(pa)}; B = {r["paper_id"]: r for r in load(pb)}
    ids = sorted(set(A) & set(B))
    print(f"{len(ids)} papers coded by both")
    for ax, lv in LEVELS.items():
        a = [A[i][ax] for i in ids if A[i].get(ax) in lv and B[i].get(ax) in lv]
        b = [B[i][ax] for i in ids if A[i].get(ax) in lv and B[i].get(ax) in lv]
        exact = sum(x == y for x, y in zip(a, b)) / len(a)
        within1 = sum(abs(lv.index(x) - lv.index(y)) <= 1 for x, y in zip(a, b)) / len(a)
        print(f"  {ax:12s} exact {exact:.0%}  within-one {within1:.0%}  weighted kappa {wkappa(a, b, lv):.2f}")
    dis = [i for i in ids if any(A[i].get(ax) != B[i].get(ax) for ax in LEVELS)]
    print("  disagreements:", len(dis), dis[:12])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "packets":
        cmd_packets()
    elif cmd == "pilot":
        cmd_pilot(int(sys.argv[2]) if len(sys.argv) > 2 else 30)
    elif cmd == "verify":
        cmd_verify(sys.argv[2])
    elif cmd == "agree":
        cmd_agree(sys.argv[2], sys.argv[3])
