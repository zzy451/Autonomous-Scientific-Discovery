"""Shared tokens, names and the papercard loader for the figure set."""
import csv, json, collections as C
from pathlib import Path
import matplotlib as mpl
import numpy as np

ROOT = Path(__file__).parent
SRC, DER, OUT = ROOT / "source_data", ROOT / "derived", ROOT / "out"
PT = 72 / 25.4

mpl.rcParams.update({
    "font.family": ["Arial", "Arial Unicode MS"], "font.size": 6, "pdf.fonttype": 42,
    "svg.fonttype": "none", "axes.linewidth": 0.4, "xtick.major.width": 0.4,
    "ytick.major.width": 0.4, "xtick.major.size": 2, "ytick.major.size": 2,
    "xtick.labelsize": 5.5, "ytick.labelsize": 5.5,
})

INK, INK2, INK3, RULE, SURF = "#1d1d1b", "#55524c", "#8a857c", "#d9d4cb", "#ffffff"
# validate_palette.js --pairs all: light ALL PASS; dark set validated separately (see README)
MECH = {"classical": "#a8326e", "optimization": "#d9622b", "hybrid": "#1a9b74", "llm": "#2f5fb3"}
MECH_DARK = {"classical": "#b8396f", "optimization": "#e2682a", "hybrid": "#22a884", "llm": "#4a86e8"}
MECH_ORDER = ["classical", "optimization", "hybrid", "llm"]
MECH_LABEL = {"classical": "Symbolic / planning / learned policy (D1, D2, D4)",
              "optimization": "Optimization / probabilistic (D3)", "hybrid": "Hybrid (D6)",
              "llm": "LLM-driven (D5)"}

FIELDS = [f"{i:02d}" for i in range(1, 12)]
FNAME = {"01": "Formal & computational", "02": "Physics & astronomy", "03": "Chemistry",
         "04": "Materials", "05": "Earth & environment", "06": "Life sciences",
         "07": "Medicine & health", "08": "Agriculture & food", "09": "Engineering & industry",
         "10": "Aerospace, marine & transport", "11": "Social & knowledge systems"}
FSHORT = {"01": "Formal", "02": "Physics", "03": "Chemistry", "04": "Materials", "05": "Earth",
          "06": "Life", "07": "Medicine", "08": "Agriculture", "09": "Engineering",
          "10": "Aerospace", "11": "Social"}
# second-level names, from science_domain_taxonomy.md section headings
SECNAME = {
    "01.01": "Mathematics", "01.02": "Computer science", "01.03": "Systems & complexity",
    "02.01": "Astronomy & astrophysics", "02.02": "Physics",
    "03.01": "General chemistry & methods", "03.02": "Fundamental chemistry",
    "03.03": "Synthesis & catalysis", "03.04": "Molecular design",
    "04.01": "Materials fundamentals", "04.02": "Structural & inorganic",
    "04.03": "Soft & functional", "04.04": "Energy & device materials",
    "05.01": "Earth-science fundamentals", "05.02": "Atmosphere, ocean & water",
    "05.03": "Environmental science", "05.04": "Geography & spatial info.",
    "06.01": "Biological fundamentals", "06.02": "Organisms", "06.03": "Biotechnology",
    "07.01": "Medical fundamentals", "07.02": "Clinical medicine", "07.03": "Public health",
    "07.04": "Pharmacy & biomedicine",
    "08.01": "Agronomy", "08.02": "Forestry", "08.03": "Animal science", "08.04": "Aquatic science",
    "08.05": "Food science",
    "09.01": "Engineering fundamentals", "09.02": "Mechanical & manufacturing",
    "09.03": "Electrical & information", "09.04": "Chemical & process", "09.05": "Civil & hydraulic",
    "09.06": "Energy engineering", "09.07": "Biomedical engineering", "09.08": "Materials & devices",
    "10.01": "Aeronautics", "10.02": "Astronautics", "10.03": "Ocean engineering",
    "10.04": "Transportation",
    "11.01": "Economics", "11.02": "Sociology & population", "11.03": "Politics & administration",
    "11.04": "Psychology & cognition", "11.05": "Education & learning",
    "11.06": "Anthropology & archaeology", "11.07": "Science & knowledge systems",
}


def mix(a, b, t):
    ca, cb = np.array(mpl.colors.to_rgb(a)), np.array(mpl.colors.to_rgb(b))
    return mpl.colors.to_hex((1 - t) * ca + t * cb)


def papercards():
    """One record per core paper with every field-level code and its provenance trail."""
    man = {r["paper_id"]: r for r in csv.DictReader(open(SRC / "core_corpus_manifest.csv", encoding="utf-8-sig"))}
    dm = {r["paper_id"]: r for r in csv.DictReader(open(SRC / "classification_results_662.csv", encoding="utf-8-sig"))}
    pap = {r["paper_id"]: r for r in csv.DictReader(open(DER / "papers.csv", encoding="utf-8"))}
    codes = C.defaultdict(list)
    for line in open(SRC / "paper_module_taxonomy_assignments.jsonl"):
        a = json.loads(line)
        codes[a["paper_id"]].append((a["module_context"], a["secondary_taxonomy_code"] or "",
                                     a["tertiary_taxonomy_code"] or ""))
    tree = set(l.rstrip("\n") for l in open(SRC / "repo_tree_60f8bad.txt", encoding="utf-8"))
    pre = "Autonomous Scientific Discovery/"
    cards = []
    for pid, p in pap.items():
        m, d = man[pid], dm[pid]
        cards.append(dict(
            paper_id=pid, title=p["title"], year=int(p["year"]), era=p["era"],
            fields=[f for f in p["modules"].split(";") if f],
            codes=sorted(codes[pid]), mechanism=p["mechanism"], decision_class=p["decision_class"],
            confidence=d["confidence"], provisional=d["provisional"] == "True",
            mech_basis=d["source_basis"], venue_class=p["venue_class"], source=p["source"],
            note_path=m["note_path"], pdf_exists=m["pdf_exists"] == "True", pdf_path=m["pdf_path"],
            evidence_status=m["evidence_status"], source_checked_at=m["source_checked_at"],
            doi_or_url=m["doi_or_url"],
            note_in_repo=pre + m["note_path"] in tree,
            pdf_in_repo=bool(m["pdf_path"]) and pre + m["pdf_path"] in tree))
    return cards


def export_ledger(cards):
    with open(DER / "papercards.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["paper_id", "title", "year", "k_fields", "fields", "field_codes", "decision_class",
                    "confidence", "provisional", "mechanism_basis", "venue_class", "source",
                    "note_path", "pdf_exists", "pdf_path", "evidence_status", "source_checked_at",
                    "doi_or_url", "note_in_repo", "pdf_in_repo"])
        for c in cards:
            w.writerow([c["paper_id"], c["title"], c["year"], len(c["fields"]), ";".join(c["fields"]),
                        ";".join("/".join(x) for x in c["codes"]), c["decision_class"], c["confidence"],
                        c["provisional"], c["mech_basis"], c["venue_class"], c["source"], c["note_path"],
                        c["pdf_exists"], c["pdf_path"], c["evidence_status"], c["source_checked_at"],
                        c["doi_or_url"], c["note_in_repo"], c["pdf_in_repo"]])


def save(fig, name, dark=False):
    OUT.mkdir(exist_ok=True)
    bg = fig.get_facecolor()
    for ext, kw in [("pdf", {}), ("png", {"dpi": 600})]:
        fig.savefig(OUT / f"{name}.{ext}", facecolor=bg, **kw)


if __name__ == "__main__":
    cards = papercards()
    export_ledger(cards)
    k = C.Counter(len(c["fields"]) for c in cards)
    print(len(cards), "cards;", "k:", sorted(k.items()),
          "pairs:", sum(len(c["fields"]) * (len(c["fields"]) - 1) // 2 for c in cards))
    print("codes per card match fields:", all(len(c["codes"]) == len(c["fields"]) for c in cards))


def wilson(k, n, z=1.96):
    """Wilson score 95% interval for a proportion k/n."""
    if n == 0:
        return (float("nan"),) * 3
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return p, max(0.0, c - h), min(1.0, c + h)


TIER_FILL = {3: INK, 2: "#8f877a", 1: "#c9c2b6", 0: "#efebe4"}
TIER_NAME = {3: "V3–V4 experiment, proof or replication", 2: "V2 computational / simulation",
             1: "V1 benchmark / internal evaluation", 0: "V0 claim only"}
