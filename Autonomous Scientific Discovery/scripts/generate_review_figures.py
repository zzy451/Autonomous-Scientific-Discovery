from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data"
SQLITE_PATH = DATA_DIR / "papers.sqlite"
DEFAULT_OUTPUT_DIR = DATA_DIR / "figures" / "review_charts"

MODULE_CODES = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
MODULE_LABELS = {
    "01": "01  Formal / Info / Comp",
    "02": "02  Physics / Astro",
    "03": "03  Chemistry",
    "04": "04  Materials",
    "05": "05  Earth / Environment",
    "06": "06  Life Sciences",
    "07": "07  Medical / Health",
    "08": "08  Agriculture",
    "09": "09  Engineering",
    "10": "10  Aerospace / Marine / Transport",
    "11": "11  Social / Behavioral / Econ",
}

COLORS = {
    "ink": "#243b53",
    "teal": "#2a9d8f",
    "sand": "#e9c46a",
    "rust": "#e76f51",
    "slate": "#577590",
    "cloud": "#d9e2ec",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate review-ready bar/line charts from Data/papers.sqlite."
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=SQLITE_PATH,
        help="Path to papers.sqlite",
    )
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


def export_year_trend(conn: sqlite3.Connection, output_dir: Path) -> None:
    rows = fetch_rows(
        conn,
        """
        SELECT
            CAST(year AS INTEGER) AS year,
            COUNT(*) AS total_records,
            SUM(CASE WHEN active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_confirmed_core_records
        FROM papers
        WHERE year GLOB '[0-9][0-9][0-9][0-9]'
        GROUP BY CAST(year AS INTEGER)
        ORDER BY CAST(year AS INTEGER)
        """,
    )
    csv_rows = [dict(row) for row in rows]
    write_csv(
        output_dir / "year_trend_records.csv",
        ["year", "total_records", "active_confirmed_core_records"],
        csv_rows,
    )

    years = [row["year"] for row in rows]
    all_records = [row["total_records"] for row in rows]
    active_core = [row["active_confirmed_core_records"] for row in rows]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(years, all_records, color=COLORS["slate"], marker="o", linewidth=2.2, label="All records")
    ax.plot(
        years,
        active_core,
        color=COLORS["teal"],
        marker="o",
        linewidth=2.6,
        label="Active confirmed core",
    )
    ax.fill_between(years, active_core, color=COLORS["teal"], alpha=0.10)
    ax.set_title("ASD Corpus Growth by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Paper count")
    ax.grid(axis="y", linestyle="--", alpha=0.8)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output_dir / "year_trend_records.png", bbox_inches="tight")
    plt.close(fig)


def export_formal_module_bar(conn: sqlite3.Connection, output_dir: Path) -> None:
    rows = fetch_rows(
        conn,
        """
        SELECT
            pm.module_code,
            COUNT(DISTINCT pm.paper_id) AS active_assigned_paper_count
        FROM paper_modules pm
        JOIN papers p ON p.paper_id = pm.paper_id
        WHERE p.active_confirmed_core = 1
          AND pm.assignment_scope = 'scientific_object_modules'
          AND pm.module_kind = 'formal_module'
        GROUP BY pm.module_code
        ORDER BY pm.module_code
        """,
    )
    csv_rows = [dict(row) for row in rows]
    write_csv(
        output_dir / "formal_module_assignment_counts.csv",
        ["module_code", "active_assigned_paper_count"],
        csv_rows,
    )

    codes = [row["module_code"] for row in rows]
    values = [row["active_assigned_paper_count"] for row in rows]
    labels = [MODULE_LABELS.get(code, code) for code in codes]

    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    bars = ax.barh(labels, values, color=COLORS["rust"], height=0.72)
    ax.set_title("Formal Module Assignment Counts")
    ax.set_xlabel("Expanded active-paper assignments")
    ax.grid(axis="x", linestyle="--", alpha=0.8)
    ax.set_axisbelow(True)
    for bar, value in zip(bars, values):
        ax.text(value + 1, bar.get_y() + bar.get_height() / 2, str(value), va="center", fontsize=9)
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(output_dir / "formal_module_assignment_counts.png", bbox_inches="tight")
    plt.close(fig)


def export_primary_filing_bar(conn: sqlite3.Connection, output_dir: Path) -> None:
    rows = fetch_rows(
        conn,
        """
        SELECT
            primary_module_for_filing AS module_code,
            COUNT(*) AS active_confirmed_core_count
        FROM papers
        WHERE active_confirmed_core = 1
          AND primary_module_for_filing IN ('01','02','03','04','05','06','07','08','09','10','11')
        GROUP BY primary_module_for_filing
        ORDER BY primary_module_for_filing
        """,
    )
    csv_rows = [dict(row) for row in rows]
    write_csv(
        output_dir / "primary_filing_counts.csv",
        ["module_code", "active_confirmed_core_count"],
        csv_rows,
    )

    codes = [row["module_code"] for row in rows]
    values = [row["active_confirmed_core_count"] for row in rows]
    labels = [MODULE_LABELS.get(code, code) for code in codes]

    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    bars = ax.barh(labels, values, color=COLORS["ink"], height=0.72)
    ax.set_title("Primary Filing Counts by Module")
    ax.set_xlabel("Unique active confirmed-core papers")
    ax.grid(axis="x", linestyle="--", alpha=0.8)
    ax.set_axisbelow(True)
    for bar, value in zip(bars, values):
        ax.text(value + 1, bar.get_y() + bar.get_height() / 2, str(value), va="center", fontsize=9)
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(output_dir / "primary_filing_counts.png", bbox_inches="tight")
    plt.close(fig)


def export_pdf_coverage_bar(conn: sqlite3.Connection, output_dir: Path) -> None:
    rows = fetch_rows(
        conn,
        """
        SELECT
            primary_module_for_filing AS module_code,
            SUM(CASE WHEN pdf_exists = 1 THEN 1 ELSE 0 END) AS with_local_pdf,
            SUM(CASE WHEN pdf_exists = 0 THEN 1 ELSE 0 END) AS without_local_pdf
        FROM papers
        WHERE active_confirmed_core = 1
          AND primary_module_for_filing IN ('01','02','03','04','05','06','07','08','09','10','11')
        GROUP BY primary_module_for_filing
        ORDER BY primary_module_for_filing
        """,
    )
    csv_rows = [dict(row) for row in rows]
    write_csv(
        output_dir / "primary_filing_pdf_coverage.csv",
        ["module_code", "with_local_pdf", "without_local_pdf"],
        csv_rows,
    )

    codes = [row["module_code"] for row in rows]
    with_pdf = [row["with_local_pdf"] for row in rows]
    without_pdf = [row["without_local_pdf"] for row in rows]
    labels = [MODULE_LABELS.get(code, code) for code in codes]

    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    ax.barh(labels, with_pdf, color=COLORS["teal"], height=0.72, label="Has local PDF")
    ax.barh(labels, without_pdf, left=with_pdf, color=COLORS["sand"], height=0.72, label="No local PDF")
    totals = [a + b for a, b in zip(with_pdf, without_pdf)]
    for bar, total in zip(ax.patches[-len(labels):], totals):
        ax.text(total + 1, bar.get_y() + bar.get_height() / 2, str(total), va="center", fontsize=9)
    ax.set_title("Primary Filing PDF Coverage")
    ax.set_xlabel("Unique active confirmed-core papers")
    ax.grid(axis="x", linestyle="--", alpha=0.8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False)
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(output_dir / "primary_filing_pdf_coverage.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    apply_chart_style()
    ensure_output_dir(args.output_dir)
    with sqlite3.connect(args.db) as conn:
        export_year_trend(conn, args.output_dir)
        export_formal_module_bar(conn, args.output_dir)
        export_primary_filing_bar(conn, args.output_dir)
        export_pdf_coverage_bar(conn, args.output_dir)
    print(f"Generated review charts in {args.output_dir}")


if __name__ == "__main__":
    main()
