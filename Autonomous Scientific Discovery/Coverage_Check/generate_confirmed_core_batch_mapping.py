from __future__ import annotations

import re
from pathlib import Path


MASTER_PATH = Path("Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md")

DOMAIN_DIR_MAP = {
    "01": "01_Formal_Information_and_Computational_Sciences",
    "02": "02_Physics_Astronomy_and_Cosmic_Sciences",
    "03": "03_Chemical_Sciences",
    "04": "04_Materials_Science",
    "05": "05_Earth_and_Environmental_Sciences",
    "06": "06_Life_Sciences",
    "07": "07_Medical_and_Health_Sciences",
    "08": "08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences",
    "09": "09_Engineering_and_Industrial_Technology_Sciences",
    "10": "10_Aerospace_Marine_and_Transportation_Sciences",
    "11": "11_Social_Behavioral_Economic_and_Knowledge_System_Sciences",
}


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("’", "'").replace("‘", "'").replace("–", "-").replace("—", "-")
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text[:80] or "Untitled"


def guess_filename(authors: str, year: str, title: str) -> str:
    first_author = authors.split(";")[0].split(",")[0].strip() if authors.strip() else "Unknown"
    first_author = re.sub(r"[^A-Za-z0-9]+", "", first_author) or "Unknown"
    return f"{first_author}_{year}_{slugify(title)}.md"


def parse_master() -> dict[str, dict[str, str]]:
    data: dict[str, dict[str, str]] = {}
    for line in MASTER_PATH.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ASD-"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 23:
            continue
        paper_id = parts[0]
        data[paper_id] = {
            "title": parts[1],
            "authors": parts[2],
            "year": parts[3],
            "source": parts[4],
            "url": parts[5],
            "status": parts[8],
            "main_class": parts[10],
            "secondary_class": parts[11],
            "evidence": parts[19],
            "citation": parts[20],
            "note_path": parts[21],
        }
    return data


def parse_manifest_ids(manifest_path: Path) -> list[str]:
    ids: list[str] = []
    seen: set[str] = set()
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if "|" not in line:
            continue
        match = re.search(r"ASD-\d{4}", line)
        if not match:
            continue
        paper_id = match.group(0)
        if paper_id not in seen:
            ids.append(paper_id)
            seen.add(paper_id)
    return ids


def main() -> None:
    manifest_path = Path(
        "Autonomous Scientific Discovery/Coverage_Check/confirmed_core_missing_note_batch1_manifest_2026-06-19.md"
    )
    master = parse_master()
    ids = parse_manifest_ids(manifest_path)

    print("ID\tMainClass\tYear\tExistingNote\tSuggestedNotePath\tEvidence\tTitle")
    for paper_id in ids:
        row = master[paper_id]
        main_class = row["main_class"]
        domain_dir = DOMAIN_DIR_MAP.get(main_class, "00_MISC")
        suggested = f"Notes/{domain_dir}/{guess_filename(row['authors'], row['year'], row['title'])}"
        print(
            "\t".join(
                [
                    paper_id,
                    main_class,
                    row["year"],
                    row["note_path"],
                    suggested,
                    row["evidence"],
                    row["title"],
                ]
            )
        )


if __name__ == "__main__":
    main()
