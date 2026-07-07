from __future__ import annotations

import argparse
import csv
import sqlite3
import textwrap
from pathlib import Path

import matplotlib
import numpy as np
from scipy.interpolate import PchipInterpolator

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data"
SQLITE_PATH = DATA_DIR / "papers.sqlite"
DEFAULT_OUTPUT_DIR = DATA_DIR / "figures" / "review_charts"

COLORS = {
    "ink": "#243b53",
    "teal": "#2a9d8f",
    "sand": "#e9c46a",
    "rust": "#e76f51",
    "slate": "#577590",
    "cloud": "#d9e2ec",
}

SOURCE_CATEGORY_LABELS = [
    "arXiv-Linked Preprints",
    "Other Preprint Servers",
    "Nature Portfolio",
    "Science Family",
    "Cell Press",
    "ACS and Chemistry Journals",
    "Materials and Advanced Science Journals",
    "AI/ML Conferences and Workshops",
    "IEEE, Robotics, and Aerospace Venues",
    "Other Journals and Venues",
]

SOURCE_CATEGORY_COLORS = {
    "arXiv-Linked Preprints": "#264653",
    "Other Preprint Servers": "#4c78a8",
    "Nature Portfolio": "#e76f51",
    "Science Family": "#d62828",
    "Cell Press": "#8d99ae",
    "ACS and Chemistry Journals": "#f4a261",
    "Materials and Advanced Science Journals": "#2a9d8f",
    "AI/ML Conferences and Workshops": "#7b2cbf",
    "IEEE, Robotics, and Aerospace Venues": "#4361ee",
    "Other Journals and Venues": "#bc6c25",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate review-ready charts from Data/papers.sqlite."
    )
    parser.add_argument("--db", type=Path, default=SQLITE_PATH, help="Path to papers.sqlite")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for PNG and CSV outputs",
    )
    return parser.parse_args()


def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def apply_chart_style() -> None:
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "savefig.dpi": 200,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titleweight": "bold",
            "axes.labelcolor": COLORS["ink"],
            "xtick.color": COLORS["ink"],
            "ytick.color": COLORS["ink"],
            "axes.edgecolor": COLORS["ink"],
            "grid.color": COLORS["cloud"],
            "text.color": COLORS["ink"],
            "font.size": 10,
        }
    )


def fetch_rows(conn: sqlite3.Connection, sql: str, params: tuple[object, ...] = ()) -> list[sqlite3.Row]:
    conn.row_factory = sqlite3.Row
    return conn.execute(sql, params).fetchall()


def wrap_label(label: str, width: int = 18) -> str:
    return "\n".join(textwrap.wrap(label, width=width, break_long_words=False))


def smooth_series(years: list[int], values: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    x = np.array(years, dtype=float)
    y = np.array(values, dtype=float)
    x_dense = np.linspace(x.min(), x.max(), 400)
    y_dense = PchipInterpolator(x, y)(x_dense).clip(min=0)
    return x, y, x_dense, y_dense


def categorize_source(source: str) -> str:
    if (
        source == "arXiv"
        or source.startswith("arXiv /")
        or source.endswith("/ arXiv")
        or " / arXiv" in source
    ):
        return "arXiv-Linked Preprints"

    if (
        source.startswith("bioRxiv")
        or source.startswith("medRxiv")
        or source.startswith("ChemRxiv")
        or source.startswith("Research Square")
        or source == "Preprints.org"
        or source.startswith("SSRN")
    ):
        return "Other Preprint Servers"

    if source.startswith("Nature") or source.startswith("npj "):
        return "Nature Portfolio"

    if (
        source == "Science"
        or source.startswith("Science ")
        or source.startswith("Science Advances")
        or source.startswith("Science Robotics")
        or source.startswith("Science China")
        or source.startswith("Light: Science")
        or source.startswith("Science and Technology of Advanced Materials Methods")
    ):
        return "Science Family"

    if source in {"Cell Reports Physical Science", "Matter", "iScience"}:
        return "Cell Press"

    if (
        source.startswith("ACS")
        or source
        in {
            "JACS",
            "Chemical Science",
            "Digital Discovery",
            "Communications Chemistry",
            "Chemical Communications",
            "Chemical Engineering Journal",
            "Chemical Engineering Science",
            "Chemistry of Materials",
            "Polymer Chemistry",
            "Journal of Chemical Information and Modeling / arXiv",
            "Journal of Pharmaceutical Analysis",
        }
    ):
        return "ACS and Chemistry Journals"

    if (
        source.startswith("Advanced ")
        or source
        in {
            "APL Materials",
            "Extreme Mechanics Letters",
            "Journal of Materials Informatics",
            "MRS Bulletin",
            "MRS Communications",
            "Remote Sensing of Environment",
            "Scientific Reports",
            "Scripta Materialia",
            "Advanced Materials",
            "Advanced Energy Materials",
            "Advanced Science",
            "Advanced Intelligent Systems",
            "npj Computational Materials",
        }
    ):
        return "Materials and Advanced Science Journals"

    if (
        source
        in {
            "AAAI",
            "AAAI 2006",
            "ACL",
            "ACL Findings",
            "KDD '19",
            "Proceedings of the AAAI Conference on Artificial Intelligence",
            "EMNLP 2024",
            "Findings of ACL: EMNLP 2025",
            "Findings of the Association for Computational Linguistics: EMNLP 2025",
            "ICLR",
            "PMLR 311 (Machine Learning in Computational Biology)",
        }
        or source.startswith("NeurIPS")
        or source.startswith("AI for Accelerated Materials Design at ICLR")
        or source.startswith("ACL 2026")
        or source.startswith("IJCAI")
        or source.startswith("arXiv / OpenReview")
        or source.startswith("arXiv / ICLR")
        or source.startswith("arXiv / ICML")
        or source.startswith("arXiv / EMNLP")
    ):
        return "AI/ML Conferences and Workshops"

    if (
        "IEEE" in source
        or source
        in {
            "SpaceOps Conference",
            "Journal of Aerospace Information Systems",
            "Journal of Field Robotics",
            "Journal of Intelligent & Robotic Systems",
            "i-SAIRAS 2014",
            "i-SAIRAS 2024",
            "2nd IEEE International Conference on Space Mission Challenges for Information Technology",
            "AAS Rocky Mountain GN&C Conference preprint",
            "ACM Transactions on Intelligent Systems and Technology",
            "IFAC-PapersOnLine",
        }
    ):
        return "IEEE, Robotics, and Aerospace Venues"

    return "Other Journals and Venues"


def build_source_category_year_rows(conn: sqlite3.Connection) -> tuple[list[int], list[dict[str, object]]]:
    rows = fetch_rows(
        conn,
        """
        SELECT year, source
        FROM papers
        WHERE active_confirmed_core = 1
          AND year GLOB '[0-9][0-9][0-9][0-9]'
        """,
    )
    years_present = sorted({int(row["year"]) for row in rows})
    start_year = min(years_present)
    end_year = 2026
    years = list(range(start_year, end_year + 1))

    count_map: dict[tuple[int, str], int] = {}
    for row in rows:
        year = int(row["year"])
        category = categorize_source(str(row["source"]))
        key = (year, category)
        count_map[key] = count_map.get(key, 0) + 1

    csv_rows: list[dict[str, object]] = []
    for year in years:
        csv_row: dict[str, object] = {"year": year}
        for label in SOURCE_CATEGORY_LABELS:
            csv_row[label] = count_map.get((year, label), 0)
        csv_rows.append(csv_row)
    return years, csv_rows


def export_source_category_year_lines(conn: sqlite3.Connection, output_dir: Path) -> None:
    years, csv_rows = build_source_category_year_rows(conn)
    write_csv(
        output_dir / "source_category_year_trend.csv",
        ["year", *SOURCE_CATEGORY_LABELS],
        csv_rows,
    )

    fig = plt.figure(figsize=(16.2, 8.8))
    ax_main = fig.add_axes([0.07, 0.18, 0.54, 0.60])
    ax_zoom = fig.add_axes([0.66, 0.18, 0.31, 0.60])

    for label in SOURCE_CATEGORY_LABELS:
        values = [int(row[label]) for row in csv_rows]
        x, y, x_dense, y_dense = smooth_series(years, values)
        color = SOURCE_CATEGORY_COLORS[label]

        ax_main.plot(x_dense, y_dense, linewidth=2.1, color=color, label=label)
        ax_main.plot(x, y, linestyle="None", marker="o", markersize=3.0, color=color)

        if label != "arXiv-Linked Preprints":
            ax_zoom.plot(x_dense, y_dense, linewidth=2.1, color=color, label=label)
            ax_zoom.plot(x, y, linestyle="None", marker="o", markersize=3.0, color=color)

    ax_main.set_title("Full scale: all categories", fontsize=16, pad=10)
    ax_main.set_xlabel("Publication Year")
    ax_main.set_ylabel("Number of Publications")
    ax_main.set_xlim(min(years), max(years))
    ax_main.set_xticks(years)
    ax_main.tick_params(axis="x", rotation=45)
    ax_main.grid(axis="y", linestyle="--", alpha=0.8)
    ax_main.set_ylim(0, 125)

    zoom_max = 25
    ax_main.axhline(zoom_max, color=COLORS["slate"], linestyle=(0, (5, 4)), linewidth=1.2)
    ax_main.text(
        min(years) + 0.35,
        zoom_max + 2.0,
        "zoomed range: 0-25",
        color=COLORS["slate"],
        fontsize=9,
        fontweight="bold",
        va="bottom",
    )

    ax_zoom.set_title(
        "Zoomed comparison of smaller categories\n(Excludes arXiv-Linked Preprints)",
        fontsize=15,
        pad=10,
    )
    ax_zoom.set_xlabel("Publication Year")
    ax_zoom.set_ylabel("Number of Publications")
    ax_zoom.set_xlim(min(years) - 0.2, max(years) + 0.2)
    ax_zoom.set_xticks(years[::2])
    ax_zoom.tick_params(axis="x", rotation=35, labelsize=9)
    ax_zoom.grid(axis="y", linestyle="--", alpha=0.8)
    ax_zoom.set_ylim(0, zoom_max)

    connector_x = max(years) - 0.1
    ax_main.plot(
        [connector_x, max(years) + 1.2],
        [zoom_max, 78],
        color=COLORS["slate"],
        linestyle=(0, (5, 4)),
        linewidth=1.2,
        clip_on=False,
    )
    ax_main.plot(
        [min(years), min(years)],
        [0, zoom_max],
        color=COLORS["slate"],
        linestyle=(0, (5, 4)),
        linewidth=1.2,
    )

    fig.suptitle(
        "Annual Distribution of Included Agent Publications Across Source Categories",
        fontsize=18,
        fontweight="bold",
        y=0.97,
    )
    handles, labels = ax_main.get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        title="Source Category",
        ncol=5,
        frameon=False,
        loc="upper center",
        bbox_to_anchor=(0.50, 0.93),
        fontsize=9,
        title_fontsize=10,
        columnspacing=1.4,
        handletextpad=0.6,
    )
    fig.text(
        0.33,
        0.06,
        "Inset magnifies the 0-25 range and excludes the dominant arXiv-linked series; data values are unchanged.",
        fontsize=10,
        style="italic",
        color=COLORS["ink"],
    )
    fig.savefig(output_dir / "source_category_year_trend.png", bbox_inches="tight")
    plt.close(fig)


def export_source_category_bar(conn: sqlite3.Connection, output_dir: Path) -> None:
    rows = fetch_rows(
        conn,
        """
        SELECT source
        FROM papers
        WHERE active_confirmed_core = 1
        """,
    )
    category_counts = {label: 0 for label in SOURCE_CATEGORY_LABELS}
    for row in rows:
        category_counts[categorize_source(str(row["source"]))] += 1

    csv_rows = [
        {"source_category": label, "paper_count": category_counts[label]}
        for label in SOURCE_CATEGORY_LABELS
    ]
    write_csv(
        output_dir / "source_category_counts_bar.csv",
        ["source_category", "paper_count"],
        csv_rows,
    )

    labels = [wrap_label(label, width=16) for label in SOURCE_CATEGORY_LABELS]
    values = [category_counts[label] for label in SOURCE_CATEGORY_LABELS]
    colors = [SOURCE_CATEGORY_COLORS[label] for label in SOURCE_CATEGORY_LABELS]

    fig, ax = plt.subplots(figsize=(14.6, 7.2))
    bars = ax.bar(labels, values, color=colors, width=0.72)
    ax.set_title("Distribution of Included Agent Publications Across Source Categories")
    ax.set_xlabel("Source Category")
    ax.set_ylabel("Number of Publications")
    ax.grid(axis="y", linestyle="--", alpha=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", rotation=18)
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 1,
            str(value),
            ha="center",
            va="bottom",
            fontsize=9,
        )
    fig.tight_layout()
    fig.savefig(output_dir / "source_category_counts_bar.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    apply_chart_style()
    ensure_output_dir(args.output_dir)
    with sqlite3.connect(args.db) as conn:
        export_source_category_year_lines(conn, args.output_dir)
        export_source_category_bar(conn, args.output_dir)
    print(f"Generated review charts in {args.output_dir}")


if __name__ == "__main__":
    main()
