"""Derive tidy tables for the main figure from the 2026-11-01 core snapshot
and the 2026-11-03 decision-mechanism increment (repo commit 60f8bad).

Outputs (derived/):
  papers.csv       one row per core paper: year, era, venue class, mechanism
  assignments.csv  one row per paper-field assignment (935)
  cooccur.csv      field-pair counts among cross-field papers
"""
import csv, json, re, itertools, collections as C
from pathlib import Path

ROOT = Path(__file__).parent
SRC, OUT = ROOT / "source_data", ROOT / "derived"

# Venue class from the manifest `source` string. Order matters: a record that
# names both a preprint server and a venue (e.g. "arXiv / ICML 2025") is
# classed by the peer-reviewed venue it names.
CONF = re.compile(r"conference|proceedings|workshop|symposium|\bICLR\b|\bICML\b|NeurIPS|\bAAAI\b|\bIJCAI\b|\bACL\b|EMNLP|\bKDD\b|ICRA|i-SAIRAS|SpaceOps|PMLR|\bWWW\b|\bCAI\b|ICOSST|Moriond|GN&C|IEEE Aerospace|Findings of|OpenReview|Poster", re.I)
PREPRINT = re.compile(r"arxiv|rxiv|preprint|research square|ssrn", re.I)
# Journals that a record co-lists with an arXiv copy; PMC mirrors of
# bio/medRxiv and "SSRN Electronic Journal" remain preprints.
JOURNAL_HINT = re.compile(r"Journal of Chemical Information|Science China", re.I)


def venue_class(s):
    s = s.strip()
    if s.lower() in ("", "unknown"):
        return "unknown"
    if CONF.search(s):
        # "arXiv / OpenReview" alone is a submission platform, not acceptance
        return "preprint" if re.fullmatch(r"arXiv / OpenReview", s) else "conference"
    if PREPRINT.search(s) and not JOURNAL_HINT.search(s):
        return "preprint"
    return "journal"


def era(y):
    y = int(y)
    return ("2004–2019" if y <= 2019 else "2020–2023" if y <= 2023 else str(y))


MECH = {"D1": "classical", "D2": "classical", "D4": "classical",
        "D3": "optimization", "D6": "hybrid", "D5": "llm"}


def main():
    OUT.mkdir(exist_ok=True)
    man = {r["paper_id"]: r for r in csv.DictReader(open(SRC / "core_corpus_manifest.csv", encoding="utf-8-sig"))}
    dm = {r["paper_id"]: r for r in csv.DictReader(open(SRC / "classification_results_662.csv", encoding="utf-8-sig"))}
    assert len(man) == len(dm) == 662 and man.keys() == dm.keys()

    papers = []
    for pid, r in man.items():
        mods = json.loads(r["scientific_object_modules"] or "[]")
        d = dm[pid]
        assert d["year"] == r["year"], pid
        papers.append(dict(
            paper_id=pid, title=r["title"], year=int(r["year"]), era=era(r["year"]),
            source=r["source"], venue_class=venue_class(r["source"]),
            decision_class=d["decision_class"], mechanism=MECH[d["decision_class"]],
            confidence=d["confidence"], modules=";".join(mods), n_modules=len(mods),
            general_method=r["general_method_bucket"]))
    write(OUT / "papers.csv", papers)

    sec = C.defaultdict(list)
    for line in open(SRC / "paper_module_taxonomy_assignments.jsonl"):
        a = json.loads(line)
        sec[(a["paper_id"], a["module_context"])].append(a["secondary_taxonomy_code"] or "")
    rows = [dict(paper_id=p["paper_id"], field=m, secondary=sec.get((p["paper_id"], m), [""])[0],
                 year=p["year"], era=p["era"], venue_class=p["venue_class"],
                 mechanism=p["mechanism"], decision_class=p["decision_class"])
            for p in papers for m in p["modules"].split(";") if m]
    write(OUT / "assignments.csv", rows)

    co = C.Counter()
    for p in papers:
        ms = sorted(p["modules"].split(";")) if p["modules"] else []
        for a, b in itertools.combinations(ms, 2):
            co[(a, b)] += 1
    write(OUT / "cooccur.csv", [dict(a=a, b=b, n=n) for (a, b), n in sorted(co.items())])

    print("papers", len(papers), "assignments", len(rows), "cross-field", sum(p["n_modules"] > 1 for p in papers))
    print("venue", C.Counter(p["venue_class"] for p in papers))
    print("mechanism", C.Counter(p["decision_class"] for p in papers))
    print("era", sorted(C.Counter(p["era"] for p in papers).items()))


def write(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)


if __name__ == "__main__":
    main()
