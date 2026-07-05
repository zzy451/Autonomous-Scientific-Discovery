#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parent.parent
MASTER_PATH = ROOT / "Paper_Lists" / "agent_master_paper_list.md"
PROGRESS_PATH = (
    ROOT
    / "Coverage_Check"
    / "multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md"
)
DATA_DIR = ROOT / "Data"
REGISTRY_DIR = DATA_DIR / "registry"
CLASSIFICATION_CODE_INDEX_PATH = DATA_DIR / "classification_code_index.json"
DISCIPLINE_CODE_ASSIGNMENTS_PATH = DATA_DIR / "discipline_code_assignments.jsonl"
CHANGE_LOG_PATH = DATA_DIR / "change_log.jsonl"
DISCIPLINE_CODE_INITIAL_ASSIGNMENT_PREVIEW_PATH = (
    DATA_DIR / "discipline_code_initial_assignment_preview.csv"
)
DISCIPLINE_LOCAL_CODE_REGISTRY_PATH = DATA_DIR / "discipline_local_code_registry.jsonl"

MASTER_HEADER = [
    "ID",
    "Paper title",
    "Authors",
    "Year",
    "Source",
    "DOI / arXiv / URL",
    "PDF path",
    "Is Agent",
    "Inclusion status",
    "Exclusion reason",
    "Main class",
    "Secondary class",
    "Tertiary class",
    "Fourth-level topic",
    "New fourth-level",
    "Agent type",
    "Research workflow role",
    "Validation type",
    "Scientific contribution type",
    "Evidence strength",
    "Citation priority",
    "Note path",
    "Remarks",
]

PROGRESS_HEADER = [
    "paper_id",
    "title",
    "note_path",
    "pdf_status",
    "pdf_path",
    "evidence_status",
    "note_status",
    "master_status",
    "final_modules_or_bucket",
    "source_limited",
    "batch",
    "closed",
]

FORMAL_MODULES = {f"{idx:02d}" for idx in range(1, 12)}
GENERAL_BUCKET_CANONICAL = (
    "01.04_general_asd_methods_without_concrete_object_experiments"
)
OBJECT_COVERAGE_MODES = {
    "single_module",
    "multi_module",
    "general_method_without_concrete_object_experiments",
}
PRIMARY_MODULE_CONFIDENCE_VALUES = {"high", "medium", "low"}
SECONDARY_CLASS_SOURCE_VALUES = {"legacy", "normalized", "manual_override"}

TAXONOMY_CODE_TO_LABEL = {
    "01": "Formal, Information and Computational Sciences",
    "01.04": "General ASD Methods without Concrete Object Experiments",
    "02": "Physics, Astronomy and Cosmic Sciences",
    "03": "Chemical Sciences",
    "04": "Materials Science",
    "05": "Earth and Environmental Sciences",
    "06": "Life Sciences",
    "07": "Medical and Health Sciences",
    "08": "Agricultural, Food, Forestry, Animal and Fishery Sciences",
    "09": "Engineering and Industrial Technology Sciences",
    "10": "Aerospace, Marine and Transportation Sciences",
    "11": "Social, Behavioral, Economic and Knowledge System Sciences",
}

TAXONOMY_CODE_TO_ZH_LABEL = {
    "01": "形式、信息与计算科学",
    "01.04": "无具体科学对象实验的通用 ASD 方法",
    "02": "物理学、天文学与宇宙科学",
    "03": "化学科学",
    "04": "材料科学",
    "05": "地球与环境科学",
    "06": "生命科学",
    "07": "医学与健康科学",
    "08": "农业、食品、林业、畜牧与渔业科学",
    "09": "工程与工业技术科学",
    "10": "航空、航天、海洋与交通科学",
    "11": "社会、行为、经济与知识系统科学",
}

TAXONOMY_DIR_NAMES = {
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
    "01.04": "01_04_General_Method_Bucket",
}

TAXONOMY_SORT_ORDER = {
    "01": 10,
    "01.04": 14,
    "02": 20,
    "03": 30,
    "04": 40,
    "05": 50,
    "06": 60,
    "07": 70,
    "08": 80,
    "09": 90,
    "10": 100,
    "11": 110,
}

REMARK_KEYS = [
    "scientific_object_modules",
    "object_coverage_mode",
    "primary_module_for_filing",
    "general_method_bucket",
    "first_hand_sources_checked",
]

REMARK_VALUE_PATTERNS = {
    "scientific_object_modules": re.compile(
        r"(?<![A-Za-z0-9_])scientific_object_modules\s*=\s*`?([0-9]{2}(?:\s*;\s*[0-9]{2})*)`?",
        re.IGNORECASE,
    ),
    "object_coverage_mode": re.compile(
        r"(?<![A-Za-z0-9_])object_coverage_mode\s*=\s*`?(single_module|multi_module|general_method_without_concrete_object_experiments)`?",
        re.IGNORECASE,
    ),
    "primary_module_for_filing": re.compile(
        r"(?<![A-Za-z0-9_])primary_module_for_filing\s*=\s*`?([0-9]{2})`?",
        re.IGNORECASE,
    ),
    "general_method_bucket": re.compile(
        r"(?<![A-Za-z0-9_])general_method_bucket\s*=\s*`?(none|01\.04(?:_general_asd_methods_without_concrete_object_experiments)?)`?",
        re.IGNORECASE,
    ),
    "first_hand_sources_checked": re.compile(
        r"(?<![A-Za-z0-9_])first_hand_sources_checked\s*=\s*",
        re.IGNORECASE,
    ),
}
FIRST_HAND_CONTINUATION_PREFIXES = (
    "official",
    "arxiv",
    "ar5iv",
    "crossref",
    "doi",
    "publisher",
    "pmc",
    "pubmed",
    "amazon",
    "science",
    "nature",
    "zenodo",
    "github",
    "repo",
    "project",
    "landing",
    "html",
    "pdf",
    "preprint",
    "canonical",
    "full paper",
    "full text",
    "biorxiv",
    "ssrn",
    "api",
    "dataset",
    "jpl",
)
FIRST_HAND_STOP_PREFIXES = (
    "evidence",
    "the ",
    "this ",
    "current ",
    "keep ",
    "note ",
    "prior ",
    "independent ",
    "legacy ",
    "stale ",
    "reviewer",
    "scientific_object_modules",
    "object_coverage_mode",
    "primary_module_for_filing",
    "general_method_bucket",
    "source_limited",
)
SECONDARY_CODE_PATTERN = re.compile(r"^(0[1-9]|1[0-1])\.(\d{2})$")
SOURCE_CHECK_DATE_PATTERN = re.compile(r"20[0-9]{2}-[0-9]{2}-[0-9]{2}")
PAPER_ID_PATTERN = re.compile(r"ASD-\d{4}")
SOURCE_CHECK_CONTEXT_KEYWORDS = (
    "checked",
    "rechecked",
    "text-checked",
    "full text",
    "full-text",
    "html full text",
    "html",
    "pdf",
    "archived",
    "landing page",
    "landing",
    "official",
    "supporting-information",
    "supporting information",
    "supplementary",
    "first-hand",
    "first hand",
    "reopened",
    "readme",
    "repo",
    "blog",
    "page",
    "xml",
)
PREVIEW_FIELDNAMES = [
    "paper_id",
    "title",
    "active_confirmed_core",
    "inclusion_status",
    "scientific_object_modules",
    "general_method_bucket",
    "object_coverage_mode",
    "primary_module_for_filing",
    "primary_module_label",
    "legacy_main_class",
    "legacy_secondary_class",
    "proposed_primary_taxonomy_code_2lvl",
    "secondary_term_in_index",
    "secondary_term_label",
    "secondary_term_status",
    "secondary_term_review_status",
    "proposed_assignment_status",
    "pending_reason",
    "proposed_discipline_local_code",
    "discipline_local_rank",
    "source_limited",
    "pdf_status",
    "evidence_status",
    "note_path",
    "pdf_path",
    "review_flags",
]
DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDNAMES = [
    "paper_id",
    "assignment_id",
    "discipline_local_code",
    "discipline_local_rank",
    "discipline_display_order",
    "assignment_status",
    "assigned_at",
    "assigned_by",
    "retired_at",
    "redirected_to_code",
    "assignment_reason",
    "pending_reason",
    "primary_module_for_filing",
    "primary_module_confidence",
    "primary_module_assignment_rule",
    "primary_module_override_reason",
    "primary_taxonomy_code_2lvl",
    "legacy_secondary_class",
    "scientific_object_modules",
    "general_method_bucket",
    "title",
    "note_path",
    "pdf_path",
    "active_confirmed_core",
    "is_derived_snapshot",
    "generated_at",
    "generated_by",
    "source_commit",
    "worktree_dirty",
]


@dataclass
class MarkdownTable:
    header: List[str]
    rows: List[Dict[str, str]]


def split_markdown_row(line: str, expected_cols: int) -> List[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        raise ValueError(f"Not a markdown row: {line!r}")
    parts = [part.strip() for part in stripped[1:-1].split("|")]
    if len(parts) > expected_cols:
        merged = parts[: expected_cols - 1] + ["|".join(parts[expected_cols - 1 :]).strip()]
        parts = merged
    if len(parts) < expected_cols:
        parts.extend([""] * (expected_cols - len(parts)))
    return parts


def is_markdown_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return False
    cells = [cell.strip() for cell in stripped[1:-1].split("|")]
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_markdown_table(
    path: Path, header_marker: str, expected_header: List[str], data_prefix: str
) -> MarkdownTable:
    lines = read_text_lossy(path).splitlines()
    start_index = None
    for idx, line in enumerate(lines):
        if line.strip() == header_marker:
            start_index = idx
            break
    if start_index is None:
        raise ValueError(f"Header marker not found in {path}: {header_marker}")

    header = split_markdown_row(lines[start_index], len(expected_header))
    if header != expected_header:
        raise ValueError(f"Unexpected header in {path}: {header}")

    rows: List[Dict[str, str]] = []
    data_start = start_index + 1
    if data_start < len(lines) and is_markdown_separator(lines[data_start]):
        data_start += 1

    for line in lines[data_start:]:
        if not line.startswith(data_prefix):
            if rows:
                continue
            continue
        parts = split_markdown_row(line, len(expected_header))
        rows.append(dict(zip(expected_header, parts)))
    return MarkdownTable(header=header, rows=rows)


def read_text_lossy(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "gb18030"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def split_semicolon_list(value: str) -> List[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def parse_doi_and_arxiv(value: str) -> Tuple[str, str, str]:
    doi = ""
    arxiv_id = ""
    url = value.strip()
    doi_match = re.search(r"(10\.\d{4,9}/\S+)", value)
    if doi_match:
        doi = doi_match.group(1).rstrip(".,;")
    arxiv_match = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)", value, re.I)
    if arxiv_match:
        arxiv_id = arxiv_match.group(1)
    return doi, arxiv_id, url


def extract_urls(value: str) -> List[str]:
    urls = [
        normalize_extracted_remark_value(match.group(0))
        for match in re.finditer(r"https?://\S+", value, re.IGNORECASE)
    ]
    return list(dict.fromkeys(url for url in urls if url))


def normalize_extracted_remark_value(raw_value: str) -> str:
    value = raw_value.strip()
    while value and value[0] in "'\"([{":
        value = value[1:].lstrip()
    while value and value[-1] in "'\".,;)]}":
        value = value[:-1].rstrip()
    return value


def is_likely_first_hand_continuation(clause: str) -> bool:
    lowered = clause.strip().lower()
    if not lowered:
        return False
    if "=" in lowered:
        return False
    if lowered.startswith(FIRST_HAND_STOP_PREFIXES):
        return False
    if lowered.startswith(FIRST_HAND_CONTINUATION_PREFIXES):
        return True
    return any(
        marker in lowered
        for marker in (" github", " ar5iv", " doi", " pdf", " html", " repo", " api")
    )


def extract_first_hand_sources_checked(remarks: str) -> str:
    matches = list(REMARK_VALUE_PATTERNS["first_hand_sources_checked"].finditer(remarks))
    if not matches:
        return ""
    tail = remarks[matches[-1].end() :]
    next_assignment = re.search(r"[;,]\s*[a-z_]+\s*=", tail, re.IGNORECASE)
    candidate = tail[: next_assignment.start()] if next_assignment else tail
    parts = [part.strip() for part in candidate.split(";") if part.strip()]
    if not parts:
        return ""
    kept_parts = [parts[0]]
    for part in parts[1:]:
        if not is_likely_first_hand_continuation(part):
            break
        kept_parts.append(part)
    return normalize_extracted_remark_value("; ".join(kept_parts))


def extract_remark_value(remarks: str, key: str) -> str:
    if not remarks:
        return ""
    if key == "first_hand_sources_checked":
        return extract_first_hand_sources_checked(remarks)
    pattern = REMARK_VALUE_PATTERNS[key]
    matches = list(pattern.finditer(remarks))
    if not matches:
        return ""
    return normalize_extracted_remark_value(matches[-1].group(1))


def extract_structured_remark_fields(remarks: str) -> Dict[str, str]:
    return {key: extract_remark_value(remarks, key) for key in REMARK_KEYS}


def normalize_general_method_bucket(raw_value: str, legacy_main: str, legacy_secondary: str) -> str:
    raw = raw_value.strip()
    if not raw and legacy_main == "01" and legacy_secondary == "01.04":
        raw = "01.04"
    raw_lower = raw.lower()
    if raw_lower in {"", "none"}:
        return "none"
    if raw_lower.startswith("01.04"):
        return GENERAL_BUCKET_CANONICAL
    return raw


def normalize_modules(raw_value: str, legacy_main: str, general_bucket: str) -> List[str]:
    modules = [code for code in split_semicolon_list(raw_value) if code in FORMAL_MODULES]
    if modules:
        return list(dict.fromkeys(modules))
    if general_bucket != "none":
        return []
    if legacy_main in FORMAL_MODULES:
        return [legacy_main]
    return []


def normalize_object_coverage_mode(raw_value: str, modules: List[str], general_bucket: str) -> str:
    raw = raw_value.strip()
    if raw in OBJECT_COVERAGE_MODES:
        return raw
    if general_bucket != "none":
        return "general_method_without_concrete_object_experiments"
    if len(modules) > 1:
        return "multi_module"
    if len(modules) == 1:
        return "single_module"
    return ""


def normalize_primary_module(raw_value: str, legacy_main: str, modules: List[str]) -> str:
    raw = raw_value.strip()
    if raw in FORMAL_MODULES:
        return raw
    if legacy_main in FORMAL_MODULES:
        return legacy_main
    return modules[0] if modules else ""


def normalize_primary_module_for_export(
    raw_value: str,
    legacy_main: str,
    modules: List[str],
    general_method_bucket: str,
) -> str:
    if general_method_bucket != "none":
        return ""
    return normalize_primary_module(raw_value, legacy_main, modules)


def derive_classification_trace(
    *,
    raw_modules: str,
    raw_object_coverage_mode: str,
    raw_primary_module: str,
    raw_general_bucket: str,
    legacy_main: str,
    legacy_secondary: str,
) -> Tuple[str, str, str]:
    if any(
        value.strip()
        for value in (
            raw_modules,
            raw_object_coverage_mode,
            raw_primary_module,
            raw_general_bucket,
        )
    ):
        return ("Remarks", "high", "structured_remark_token")
    if legacy_main == "01" and legacy_secondary == "01.04":
        return (
            "Main class;Secondary class",
            "medium",
            "legacy_general_method_fallback",
        )
    if legacy_main in FORMAL_MODULES:
        return ("Main class", "medium", "legacy_main_class_fallback")
    return ("", "low", "needs_review")


def derive_primary_filing_trace(
    *,
    raw_primary_module: str,
    legacy_main: str,
    scientific_object_modules: List[str],
    general_method_bucket: str,
    primary_module_for_filing: str,
) -> Tuple[str, str, str]:
    if general_method_bucket != "none" or not primary_module_for_filing:
        return ("", "", "")
    if len(scientific_object_modules) == 1 and primary_module_for_filing == scientific_object_modules[0]:
        return ("high", "main_scientific_object", "")
    if len(scientific_object_modules) > 1:
        raw_primary = raw_primary_module.strip()
        if raw_primary and raw_primary == primary_module_for_filing and raw_primary in scientific_object_modules:
            return (
                "medium",
                "manual_override",
                "structured_remark_primary_module_for_filing",
            )
        if legacy_main == primary_module_for_filing and legacy_main in scientific_object_modules:
            return (
                "low",
                "manual_override",
                "legacy_main_class_fallback_for_multi_module",
            )
        if primary_module_for_filing in scientific_object_modules:
            return (
                "low",
                "manual_override",
                "derived_primary_module_without_explicit_trace",
            )
    return ("low", "manual_override", "needs_primary_module_review")


def derive_secondary_class_source(term: Dict[str, object] | None, legacy_secondary_class: str) -> str:
    if not legacy_secondary_class.strip():
        return ""
    if term is None:
        return "legacy"
    source_value = str(term.get("source", "")).strip().lower()
    if "manual_override" in source_value:
        return "manual_override"
    if "normalized" in source_value:
        return "normalized"
    return "legacy"


def derive_secondary_class_confidence(term: Dict[str, object] | None, legacy_secondary_class: str) -> str:
    if not legacy_secondary_class.strip():
        return ""
    if term is None:
        return "low"
    status = str(term.get("status", "")).strip()
    review_status = str(term.get("review_status", "")).strip()
    if status == "active" and review_status == "reviewed":
        return "high"
    if status == "needs_review" or review_status in {"unreviewed", "needs_split", "needs_merge"}:
        return "low"
    return "medium"


def derive_secondary_class_review_status(term: Dict[str, object] | None, legacy_secondary_class: str) -> str:
    if not legacy_secondary_class.strip():
        return ""
    if term is None:
        return "unreviewed"
    return str(term.get("review_status", "")).strip() or "unreviewed"


def derive_record_status(inclusion_status: str, active_confirmed_core: bool) -> str:
    normalized = inclusion_status.strip().lower()
    if active_confirmed_core:
        return "active_confirmed_core"
    if normalized == "excluded":
        return "excluded"
    if normalized in {"duplicate", "duplicated"}:
        return "duplicate"
    if normalized in {"retired", "retire"}:
        return "retired"
    if normalized in {"background_only", "background"}:
        return "background_only"
    if normalized in {"candidate", "pending", "to_read"}:
        return "candidate"
    return "candidate"


def derive_duplicate_of(exclusion_reason: str) -> str:
    if "duplicate" not in exclusion_reason.strip().lower():
        return ""
    matches = PAPER_ID_PATTERN.findall(exclusion_reason)
    return matches[0] if matches else ""


def adjust_record_status_for_duplicate(
    *,
    inclusion_status: str,
    active_confirmed_core: bool,
    duplicate_of: str,
) -> str:
    if duplicate_of and not active_confirmed_core:
        return "duplicate"
    return derive_record_status(inclusion_status, active_confirmed_core)


def derive_inclusion_decision(
    inclusion_status: str, active_confirmed_core: bool, duplicate_of: str = ""
) -> str:
    if duplicate_of and not active_confirmed_core:
        return "duplicate"
    normalized = inclusion_status.strip().lower()
    if active_confirmed_core:
        return "confirmed_core"
    if normalized == "background_only":
        return "background_only"
    if normalized == "excluded":
        return "excluded"
    if normalized in {"duplicate", "duplicated"}:
        return "duplicate"
    if normalized in {"retired", "retire"}:
        return "retired"
    return normalized or "candidate"


def build_classification_display_code(
    scientific_object_modules: List[str], general_method_bucket: str
) -> str:
    if general_method_bucket != "none":
        return "01.04"
    if scientific_object_modules:
        return ";".join(scientific_object_modules)
    return ""


def path_exists(repo_relative_path: str) -> bool:
    if not repo_relative_path:
        return False
    return (ROOT / repo_relative_path).exists()


def load_classification_code_index() -> Dict[str, object]:
    payload = json.loads(CLASSIFICATION_CODE_INDEX_PATH.read_text(encoding="utf-8"))
    required_keys = (
        "primary_code_to_label",
        "secondary_code_to_label",
        "primary_terms",
        "secondary_terms",
    )
    missing = [key for key in required_keys if key not in payload]
    if missing:
        raise ValueError(
            "classification_code_index.json missing required keys: "
            + ", ".join(missing)
        )
    return payload


def load_jsonl_rows(path: Path) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def build_latest_change_log_index(
    change_log_rows: List[Dict[str, object]],
) -> Dict[str, Dict[str, str]]:
    latest: Dict[str, Dict[str, str]] = {}
    for row in change_log_rows:
        paper_id = str(row.get("paper_id") or "").strip()
        changed_at = str(row.get("changed_at") or "").strip()
        changed_by = str(row.get("changed_by") or "").strip()
        if not paper_id or not changed_at:
            continue
        current = latest.get(paper_id)
        if current is None or changed_at >= current["changed_at"]:
            latest[paper_id] = {
                "changed_at": changed_at,
                "changed_by": changed_by,
            }
    return latest


def derive_source_checked_at(
    *,
    remarks: str,
    first_hand_sources_checked: str,
    pdf_status: str,
    evidence_status: str,
    latest_change: Dict[str, str],
) -> str:
    candidate_dates: List[str] = []
    for match in SOURCE_CHECK_DATE_PATTERN.finditer(remarks):
        snippet_start = max(0, match.start() - 120)
        snippet_end = min(len(remarks), match.end() + 160)
        snippet = remarks[snippet_start:snippet_end].lower()
        if any(keyword in snippet for keyword in SOURCE_CHECK_CONTEXT_KEYWORDS):
            candidate_dates.append(match.group(0))
    if candidate_dates:
        return max(candidate_dates)

    if first_hand_sources_checked.strip():
        all_dates = SOURCE_CHECK_DATE_PATTERN.findall(remarks)
        if all_dates:
            return max(all_dates)

    latest_change_date = str(latest_change.get("changed_at") or "").strip()
    if latest_change_date and (
        first_hand_sources_checked.strip()
        or pdf_status.strip()
        or evidence_status.strip()
    ):
        return latest_change_date
    return ""


def is_yes_like(value: str) -> bool:
    return value.strip().lower().startswith("yes")


def stringify_list(values: List[str]) -> str:
    return ";".join(values)


def parse_discipline_local_rank(discipline_local_code: object) -> str:
    if not discipline_local_code:
        return ""
    return str(discipline_local_code).rsplit("-", 1)[-1]


def build_discipline_display_order(
    *,
    assignment_status: str,
    discipline_local_code: object,
    primary_module_for_filing: object,
    primary_taxonomy_code_2lvl: object,
    paper_id: object,
) -> str:
    discipline_local_code_str = str(discipline_local_code or "").strip()
    if assignment_status == "active_code" and discipline_local_code_str:
        return discipline_local_code_str

    primary_module = str(primary_module_for_filing or "").strip() or "ZZ"
    secondary_code = str(primary_taxonomy_code_2lvl or "").strip()
    secondary_rank = "ZZ"
    secondary_match = SECONDARY_CODE_PATTERN.fullmatch(secondary_code)
    if secondary_match:
        secondary_rank = secondary_match.group(2)
    paper_id_str = str(paper_id or "").strip()

    if assignment_status == "pending_secondary":
        return f"{primary_module}-{secondary_rank}-PENDING-{paper_id_str}"
    if assignment_status == "non_discipline_general_method":
        return f"GM-PENDING-{paper_id_str}"
    return f"UNSORTED-{paper_id_str}"


def get_git_export_metadata() -> Tuple[str, bool]:
    try:
        source_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
        ).strip()
    except Exception:
        source_commit = ""
    try:
        worktree_status = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
        )
        worktree_dirty = bool(worktree_status.strip())
    except Exception:
        worktree_dirty = False
    return source_commit, worktree_dirty


def build_discipline_initial_assignment_preview(
    papers: Iterable[Dict[str, object]],
    classification_code_index: Dict[str, object],
) -> List[Dict[str, object]]:
    primary_code_to_label = {
        str(code): str(label)
        for code, label in dict(classification_code_index["primary_code_to_label"]).items()
    }
    secondary_code_to_label = {
        str(code): str(label)
        for code, label in dict(classification_code_index["secondary_code_to_label"]).items()
    }
    secondary_terms_by_code = {
        str(term["secondary_code"]): term
        for term in classification_code_index["secondary_terms"]
        if isinstance(term, dict) and term.get("secondary_code")
    }
    preview_rows: List[Dict[str, object]] = []
    active_code_groups: Dict[str, List[Dict[str, object]]] = {}

    for paper in sorted(
        (paper for paper in papers if bool(paper["active_confirmed_core"])),
        key=lambda item: str(item["paper_id"]),
    ):
        scientific_object_modules = [str(code) for code in paper["scientific_object_modules"]]
        general_method_bucket = str(paper["general_method_bucket"])
        primary_module_for_filing = str(paper["primary_module_for_filing"])
        legacy_secondary_class = str(paper["legacy_secondary_class"]).strip()
        legacy_secondary_match = SECONDARY_CODE_PATTERN.fullmatch(legacy_secondary_class)
        secondary_term = secondary_terms_by_code.get(legacy_secondary_class)
        review_flags: List[str] = []
        if len(scientific_object_modules) > 1:
            review_flags.append("multi_module")
        if is_yes_like(str(paper["source_limited"])):
            review_flags.append("source_limited")
        if (
            primary_module_for_filing
            and scientific_object_modules
            and primary_module_for_filing not in scientific_object_modules
        ):
            review_flags.append("primary_module_outside_scientific_object_modules")
        if legacy_secondary_class and secondary_term is None:
            review_flags.append("secondary_not_in_taxonomy_index")
        if secondary_term is not None and secondary_term.get("status") != "active":
            review_flags.append(
                f"secondary_term_status_{str(secondary_term.get('status', '')).strip() or 'unknown'}"
            )
        if secondary_term is not None and secondary_term.get("review_status") != "reviewed":
            review_flags.append(
                "secondary_term_review_"
                f"{str(secondary_term.get('review_status', '')).strip() or 'unknown'}"
            )

        preview_row: Dict[str, object] = {
            "paper_id": paper["paper_id"],
            "title": paper["title"],
            "active_confirmed_core": bool(paper["active_confirmed_core"]),
            "inclusion_status": paper["inclusion_status"],
            "scientific_object_modules": stringify_list(scientific_object_modules),
            "general_method_bucket": general_method_bucket,
            "object_coverage_mode": paper["object_coverage_mode"],
            "primary_module_for_filing": primary_module_for_filing,
            "primary_module_label": primary_code_to_label.get(primary_module_for_filing, ""),
            "legacy_main_class": paper["legacy_main_class"],
            "legacy_secondary_class": legacy_secondary_class,
            "proposed_primary_taxonomy_code_2lvl": "",
            "secondary_term_in_index": secondary_term is not None,
            "secondary_term_label": (
                str(secondary_term.get("label", ""))
                if secondary_term is not None
                else secondary_code_to_label.get(legacy_secondary_class, "")
            ),
            "secondary_term_status": (
                str(secondary_term.get("status", "")) if secondary_term is not None else ""
            ),
            "secondary_term_review_status": (
                str(secondary_term.get("review_status", ""))
                if secondary_term is not None
                else ""
            ),
            "proposed_assignment_status": "",
            "pending_reason": "",
            "proposed_discipline_local_code": "",
            "discipline_local_rank": "",
            "source_limited": paper["source_limited"],
            "pdf_status": paper["pdf_status"],
            "evidence_status": paper["evidence_status"],
            "note_path": paper["note_path"],
            "pdf_path": paper["pdf_path"],
            "review_flags": "",
        }

        is_pure_general_method = (
            general_method_bucket != "none" and not scientific_object_modules
        )
        if is_pure_general_method:
            preview_row["proposed_assignment_status"] = "non_discipline_general_method"
            if legacy_secondary_class and legacy_secondary_class != "01.04":
                review_flags.append("general_method_secondary_not_01_04")
        elif not primary_module_for_filing:
            preview_row["proposed_assignment_status"] = "pending_secondary"
            preview_row["pending_reason"] = "missing_primary_module_for_filing"
            review_flags.append("missing_primary_module_for_filing")
        elif legacy_secondary_match is None:
            preview_row["proposed_assignment_status"] = "pending_secondary"
            preview_row["pending_reason"] = "missing_or_uncertain_secondary_class"
            review_flags.append("missing_or_uncertain_secondary_class")
        elif legacy_secondary_match.group(1) != primary_module_for_filing:
            preview_row["proposed_assignment_status"] = "pending_secondary"
            preview_row["pending_reason"] = "secondary_primary_mismatch"
            review_flags.append("secondary_primary_mismatch")
        else:
            preview_row["proposed_assignment_status"] = "active_code"
            preview_row["proposed_primary_taxonomy_code_2lvl"] = legacy_secondary_class
            active_code_groups.setdefault(legacy_secondary_class, []).append(preview_row)

        preview_row["review_flags"] = stringify_list(review_flags)
        preview_rows.append(preview_row)

    for secondary_code, rows in sorted(active_code_groups.items()):
        primary_code, secondary_rank = secondary_code.split(".")
        for index, row in enumerate(sorted(rows, key=lambda item: str(item["paper_id"])), start=1):
            row["proposed_discipline_local_code"] = (
                f"{primary_code}-{secondary_rank}-{index:03d}"
            )
            row["discipline_local_rank"] = f"{index:03d}"

    return preview_rows


def build_discipline_local_code_registry(
    papers: Iterable[Dict[str, object]],
    discipline_code_assignments: List[Dict[str, object]],
    generated_at: str,
    generated_by: str,
    source_commit: str,
    worktree_dirty: bool,
) -> List[Dict[str, object]]:
    papers_by_id = {str(paper["paper_id"]): paper for paper in papers}
    registry_rows: List[Dict[str, object]] = []
    current_statuses = {
        "active_code",
        "pending_secondary",
        "non_discipline_general_method",
    }
    assignments_by_paper_id: Dict[str, List[Dict[str, object]]] = {}

    for assignment in discipline_code_assignments:
        paper_id = str(assignment["paper_id"])
        assignments_by_paper_id.setdefault(paper_id, []).append(assignment)

    for paper_id, assignments in sorted(assignments_by_paper_id.items()):
        paper = papers_by_id.get(paper_id)
        if paper is None:
            raise ValueError(
                f"discipline_code_assignments.jsonl references unknown paper_id during registry export: {paper_id}"
            )
        current_assignments = [
            assignment
            for assignment in assignments
            if str(assignment["assignment_status"]) in current_statuses
        ]
        if len(current_assignments) != 1:
            raise ValueError(
                "discipline_code_assignments.jsonl must provide exactly one current "
                f"snapshot row per paper for registry export: {paper_id} -> {len(current_assignments)}"
            )
        assignment = current_assignments[0]

        discipline_local_code = assignment.get("discipline_local_code")
        registry_rows.append(
            {
                "paper_id": paper_id,
                "assignment_id": assignment["assignment_id"],
                "discipline_local_code": discipline_local_code,
                "discipline_local_rank": parse_discipline_local_rank(discipline_local_code),
                "discipline_display_order": build_discipline_display_order(
                    assignment_status=str(assignment["assignment_status"]),
                    discipline_local_code=discipline_local_code,
                    primary_module_for_filing=paper["primary_module_for_filing"],
                    primary_taxonomy_code_2lvl=assignment["primary_taxonomy_code_2lvl"],
                    paper_id=paper_id,
                ),
                "assignment_status": assignment["assignment_status"],
                "assigned_at": assignment["assigned_at"],
                "assigned_by": assignment["assigned_by"],
                "retired_at": assignment["retired_at"],
                "redirected_to_code": assignment["redirected_to_code"],
                "assignment_reason": assignment["assignment_reason"],
                "pending_reason": assignment["pending_reason"],
                "primary_module_for_filing": paper["primary_module_for_filing"],
                "primary_module_confidence": paper["primary_module_confidence"],
                "primary_module_assignment_rule": paper["primary_module_assignment_rule"],
                "primary_module_override_reason": paper["primary_module_override_reason"],
                "primary_taxonomy_code_2lvl": assignment["primary_taxonomy_code_2lvl"],
                "legacy_secondary_class": paper["legacy_secondary_class"],
                "secondary_class_source": paper["secondary_class_source"],
                "secondary_class_confidence": paper["secondary_class_confidence"],
                "secondary_class_review_status": paper["secondary_class_review_status"],
                "scientific_object_modules": paper["scientific_object_modules"],
                "general_method_bucket": paper["general_method_bucket"],
                "title": paper["title"],
                "note_path": paper["note_path"],
                "pdf_path": paper["pdf_path"],
                "active_confirmed_core": paper["active_confirmed_core"],
                "is_derived_snapshot": True,
                "generated_at": generated_at,
                "generated_by": generated_by,
                "source_commit": source_commit,
                "worktree_dirty": worktree_dirty,
            }
        )

    return registry_rows


def build_papers(
    master_rows: Iterable[Dict[str, str]],
    progress_rows: Dict[str, Dict[str, str]],
    latest_change_log_by_paper_id: Dict[str, Dict[str, str]],
    classification_code_index: Dict[str, object],
) -> List[Dict[str, object]]:
    exported_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    papers: List[Dict[str, object]] = []
    secondary_terms_by_code = {
        str(term.get("secondary_code")): term
        for term in classification_code_index.get("secondary_terms", [])
        if isinstance(term, dict) and term.get("secondary_code")
    }

    for row in master_rows:
        paper_id = row["ID"]
        progress = progress_rows.get(paper_id, {})
        remarks = row["Remarks"]

        structured_remarks = extract_structured_remark_fields(remarks)
        raw_modules = structured_remarks["scientific_object_modules"]
        raw_object_coverage_mode = structured_remarks["object_coverage_mode"]
        raw_primary_module = structured_remarks["primary_module_for_filing"]
        raw_general_bucket = structured_remarks["general_method_bucket"]
        first_hand_sources_checked = structured_remarks["first_hand_sources_checked"]

        general_method_bucket = normalize_general_method_bucket(
            raw_general_bucket, row["Main class"], row["Secondary class"]
        )
        scientific_object_modules = normalize_modules(
            raw_modules, row["Main class"], general_method_bucket
        )
        object_coverage_mode = normalize_object_coverage_mode(
            raw_object_coverage_mode, scientific_object_modules, general_method_bucket
        )
        primary_module_for_filing = normalize_primary_module_for_export(
            raw_primary_module,
            row["Main class"],
            scientific_object_modules,
            general_method_bucket,
        )
        (
            classification_source_field,
            classification_source_confidence,
            classification_parser_rule,
        ) = derive_classification_trace(
            raw_modules=raw_modules,
            raw_object_coverage_mode=raw_object_coverage_mode,
            raw_primary_module=raw_primary_module,
            raw_general_bucket=raw_general_bucket,
            legacy_main=row["Main class"],
            legacy_secondary=row["Secondary class"],
        )
        (
            primary_module_confidence,
            primary_module_assignment_rule,
            primary_module_override_reason,
        ) = derive_primary_filing_trace(
            raw_primary_module=raw_primary_module,
            legacy_main=row["Main class"],
            scientific_object_modules=scientific_object_modules,
            general_method_bucket=general_method_bucket,
            primary_module_for_filing=primary_module_for_filing,
        )
        legacy_secondary_class = row["Secondary class"]
        secondary_term = secondary_terms_by_code.get(legacy_secondary_class)
        secondary_class_source = derive_secondary_class_source(
            term=secondary_term,
            legacy_secondary_class=legacy_secondary_class,
        )
        secondary_class_confidence = derive_secondary_class_confidence(
            term=secondary_term,
            legacy_secondary_class=legacy_secondary_class,
        )
        secondary_class_review_status = derive_secondary_class_review_status(
            term=secondary_term,
            legacy_secondary_class=legacy_secondary_class,
        )

        doi, arxiv_id, url = parse_doi_and_arxiv(row["DOI / arXiv / URL"])
        note_path = progress.get("note_path") or row["Note path"]
        pdf_path = progress.get("pdf_path") or row["PDF path"]
        pdf_exists = path_exists(pdf_path)
        note_exists = path_exists(note_path)
        source_limited = (progress.get("source_limited") or "").strip().lower()
        is_active_confirmed_core = (
            row["Inclusion status"] in {"to_read", "included"}
            and (bool(scientific_object_modules) or general_method_bucket != "none")
        )
        duplicate_of = derive_duplicate_of(row["Exclusion reason"])
        record_status = adjust_record_status_for_duplicate(
            inclusion_status=row["Inclusion status"],
            active_confirmed_core=is_active_confirmed_core,
            duplicate_of=duplicate_of,
        )
        inclusion_decision = derive_inclusion_decision(
            row["Inclusion status"], is_active_confirmed_core, duplicate_of
        )
        latest_change = latest_change_log_by_paper_id.get(paper_id, {})
        pdf_status = progress.get("pdf_status", "")
        evidence_status = progress.get("evidence_status", "")
        source_checked_at = derive_source_checked_at(
            remarks=remarks,
            first_hand_sources_checked=first_hand_sources_checked,
            pdf_status=pdf_status,
            evidence_status=evidence_status,
            latest_change=latest_change,
        )

        papers.append(
            {
                "paper_id": paper_id,
                "title": row["Paper title"],
                "authors": row["Authors"],
                "year": row["Year"],
                "source": row["Source"],
                "doi_or_url": row["DOI / arXiv / URL"],
                "doi": doi,
                "url": url,
                "arxiv_id": arxiv_id,
                "pdf_path": pdf_path,
                "pdf_exists": pdf_exists,
                "note_path": note_path,
                "note_exists": note_exists,
                "is_agent": row["Is Agent"],
                "inclusion_status": row["Inclusion status"],
                "exclusion_reason": row["Exclusion reason"],
                "legacy_main_class": row["Main class"],
                "legacy_secondary_class": legacy_secondary_class,
                "legacy_tertiary_class": row["Tertiary class"],
                "secondary_class_source": secondary_class_source,
                "secondary_class_confidence": secondary_class_confidence,
                "secondary_class_review_status": secondary_class_review_status,
                "fourth_level_topic": row["Fourth-level topic"],
                "new_fourth_level": row["New fourth-level"],
                "agent_type_raw": row["Agent type"],
                "agent_type": split_semicolon_list(row["Agent type"]),
                "research_workflow_role_raw": row["Research workflow role"],
                "research_workflow_role": split_semicolon_list(row["Research workflow role"]),
                "validation_type_raw": row["Validation type"],
                "validation_type": split_semicolon_list(row["Validation type"]),
                "scientific_contribution_type_raw": row["Scientific contribution type"],
                "scientific_contribution_type": split_semicolon_list(
                    row["Scientific contribution type"]
                ),
                "evidence_strength": row["Evidence strength"],
                "citation_priority": row["Citation priority"],
                "remarks": remarks,
                "scientific_object_modules": scientific_object_modules,
                "general_method_bucket": general_method_bucket,
                "object_coverage_mode": object_coverage_mode,
                "primary_module_for_filing": primary_module_for_filing,
                "primary_module_confidence": primary_module_confidence,
                "primary_module_assignment_rule": primary_module_assignment_rule,
                "primary_module_override_reason": primary_module_override_reason,
                "classification_source_field": classification_source_field,
                "classification_source_confidence": classification_source_confidence,
                "classification_parser_rule": classification_parser_rule,
                "first_hand_sources_checked": first_hand_sources_checked,
                "source_checked_at": source_checked_at,
                "progress_title": progress.get("title", ""),
                "pdf_status": pdf_status,
                "evidence_status": evidence_status,
                "note_status": progress.get("note_status", ""),
                "master_status": progress.get("master_status", ""),
                "final_modules_or_bucket_raw": progress.get("final_modules_or_bucket", ""),
                "final_modules_or_bucket": split_semicolon_list(
                    progress.get("final_modules_or_bucket", "")
                ),
                "source_limited": source_limited,
                "batch": progress.get("batch", ""),
                "closed": progress.get("closed", ""),
                "active_confirmed_core": is_active_confirmed_core,
                "record_status": record_status,
                "inclusion_decision": inclusion_decision,
                "duplicate_of": duplicate_of,
                "last_reviewed_at": latest_change.get("changed_at", ""),
                "last_reviewed_by": latest_change.get("changed_by", ""),
                "exported_at": exported_at,
            }
        )
    return papers


def build_taxonomy_index() -> Dict[str, Dict[str, str]]:
    label_to_code = {label: code for code, label in TAXONOMY_CODE_TO_LABEL.items()}
    return {"code_to_label": TAXONOMY_CODE_TO_LABEL, "label_to_code": label_to_code}


def compute_sha256(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compute_repo_relative_sha256(
    repo_relative_path: str, sha256_cache: Dict[str, str]
) -> str:
    if not repo_relative_path:
        return ""
    cached = sha256_cache.get(repo_relative_path)
    if cached is not None:
        return cached
    repo_path = ROOT / repo_relative_path
    if not repo_path.exists():
        return ""
    sha256 = compute_sha256(repo_path)
    sha256_cache[repo_relative_path] = sha256
    return sha256


def compute_repo_relative_size_bytes(repo_relative_path: str) -> int | None:
    if not repo_relative_path:
        return None
    repo_path = ROOT / repo_relative_path
    if not repo_path.exists() or not repo_path.is_file():
        return None
    return repo_path.stat().st_size


def derive_pdf_evidence_type(
    *,
    pdf_exists: bool,
    pdf_status: str,
    evidence_status: str,
) -> str:
    pdf_status_lower = pdf_status.strip().lower()
    evidence_status_lower = evidence_status.strip().lower()
    combined = f"{pdf_status_lower} {evidence_status_lower}"
    if "supplement" in combined:
        return "supplementary_pdf"
    if pdf_exists:
        return "main_pdf"
    if any(
        token in combined
        for token in ("html_full_text", "pmc_full_text", "public_full_text", "article_page")
    ):
        return "html_full_text"
    if any(token in combined for token in ("project_page", "repo", "preview_repo")):
        return "project_page"
    if any(token in combined for token in ("official", "page", "doi", "metadata", "promptbio")):
        return "official_page"
    return "abstract"


def derive_pdf_check_status(
    *,
    pdf_evidence_type: str,
    pdf_exists: bool,
    evidence_status: str,
    source_limited: str,
) -> str:
    evidence_status_lower = evidence_status.strip().lower()
    source_limited_lower = source_limited.strip().lower()
    if pdf_evidence_type == "main_pdf" and pdf_exists:
        return "full_text_checked"
    if pdf_evidence_type == "html_full_text":
        return "full_text_checked"
    if pdf_evidence_type == "supplementary_pdf" and "full_text" in evidence_status_lower:
        return "full_text_checked"
    if source_limited_lower.startswith("yes") or pdf_evidence_type == "supplementary_pdf":
        return "source_limited"
    return "metadata_only"


def build_paper_registry(papers: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    registry: List[Dict[str, object]] = []
    for paper in papers:
        registry.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "authors": paper["authors"],
                "year": paper["year"],
                "source": paper["source"],
                "source_locator_raw": paper["doi_or_url"],
                "is_agent": paper["is_agent"],
                "inclusion_status": paper["inclusion_status"],
                "exclusion_reason": paper["exclusion_reason"],
                "note_path": paper["note_path"],
                "note_exists": paper["note_exists"],
                "pdf_path": paper["pdf_path"],
                "pdf_exists": paper["pdf_exists"],
                "legacy_main_class": paper["legacy_main_class"],
                "legacy_secondary_class": paper["legacy_secondary_class"],
                "legacy_tertiary_class": paper["legacy_tertiary_class"],
                "fourth_level_topic": paper["fourth_level_topic"],
                "new_fourth_level": paper["new_fourth_level"],
                "scientific_object_modules": paper["scientific_object_modules"],
                "general_method_bucket": paper["general_method_bucket"],
                "object_coverage_mode": paper["object_coverage_mode"],
                "primary_module_for_filing": paper["primary_module_for_filing"],
                "classification_display_code": build_classification_display_code(
                    paper["scientific_object_modules"], paper["general_method_bucket"]
                ),
                "active_confirmed_core": paper["active_confirmed_core"],
                "first_hand_sources_checked": paper["first_hand_sources_checked"],
                "pdf_status": paper["pdf_status"],
                "evidence_status": paper["evidence_status"],
                "note_status": paper["note_status"],
                "master_status": paper["master_status"],
                "source_limited": paper["source_limited"],
                "batch": paper["batch"],
                "closed": paper["closed"],
                "exported_at": paper["exported_at"],
            }
        )
    return registry


def build_paper_identifier_aliases(
    papers: Iterable[Dict[str, object]]
) -> List[Dict[str, object]]:
    aliases: List[Dict[str, object]] = []
    seen = set()

    def append_alias(
        paper_id: str,
        alias_scheme: str,
        alias_value: str,
        exported_at: str,
    ) -> None:
        value = alias_value.strip()
        if not value:
            return
        key = (paper_id, alias_scheme, value)
        if key in seen:
            return
        seen.add(key)
        aliases.append(
            {
                "paper_id": paper_id,
                "alias_scheme": alias_scheme,
                "alias_value": value,
                "is_primary_key": False,
                "exported_at": exported_at,
            }
        )

    for paper in papers:
        paper_id = str(paper["paper_id"])
        exported_at = str(paper["exported_at"])
        append_alias(paper_id, "doi", str(paper["doi"]), exported_at)
        append_alias(paper_id, "arxiv_id", str(paper["arxiv_id"]), exported_at)
        for url in extract_urls(str(paper["doi_or_url"])):
            append_alias(paper_id, "url", url, exported_at)

    return aliases


def build_taxonomy_registry(exported_at: str) -> Dict[str, object]:
    terms: List[Dict[str, object]] = []
    for code in TAXONOMY_CODE_TO_LABEL:
        kind = "general_bucket" if code == "01.04" else "formal_module"
        terms.append(
            {
                "taxonomy_code": code,
                "kind": kind,
                "labels": {"display": TAXONOMY_CODE_TO_LABEL[code]},
                "zh_label": TAXONOMY_CODE_TO_ZH_LABEL[code],
                "en_label": TAXONOMY_CODE_TO_LABEL[code],
                "sort_order": TAXONOMY_SORT_ORDER[code],
                "dir_name": TAXONOMY_DIR_NAMES[code],
                "parent_module_code": "01" if code == "01.04" else "",
            }
        )
    return {"exported_at": exported_at, "taxonomy_terms": terms}


def build_classification_assignments(
    papers: Iterable[Dict[str, object]]
) -> List[Dict[str, object]]:
    assignments: List[Dict[str, object]] = []
    for paper in papers:
        exported_at = paper["exported_at"]
        primary_module_for_filing = paper["primary_module_for_filing"]
        modules = list(paper["scientific_object_modules"])
        for index, module_code in enumerate(modules, start=1):
            assignments.append(
                {
                    "paper_id": paper["paper_id"],
                    "taxonomy_code": module_code,
                    "assignment_kind": "formal_module",
                    "assignment_source": "scientific_object_modules",
                    "assignment_order": index,
                    "is_primary_filing": module_code == primary_module_for_filing,
                    "primary_module_for_filing": primary_module_for_filing,
                    "object_coverage_mode": paper["object_coverage_mode"],
                    "active_confirmed_core": paper["active_confirmed_core"],
                    "exported_at": exported_at,
                }
            )

        general_bucket = str(paper["general_method_bucket"])
        if general_bucket != "none":
            assignments.append(
                {
                    "paper_id": paper["paper_id"],
                    "taxonomy_code": "01.04",
                    "assignment_kind": "general_bucket",
                    "assignment_source": "general_method_bucket",
                    "assignment_order": 1,
                    "is_primary_filing": False,
                    "primary_module_for_filing": primary_module_for_filing,
                    "object_coverage_mode": paper["object_coverage_mode"],
                    "active_confirmed_core": paper["active_confirmed_core"],
                    "exported_at": exported_at,
                }
            )
    return assignments


def build_pdf_archive_registry(
    papers: Iterable[Dict[str, object]], sha256_cache: Dict[str, str]
) -> List[Dict[str, object]]:
    registry: List[Dict[str, object]] = []
    for paper in papers:
        pdf_path = str(paper["pdf_path"])
        pdf_exists = bool(paper["pdf_exists"])
        pdf_status = str(paper["pdf_status"])
        evidence_status = str(paper["evidence_status"])
        source_limited = str(paper["source_limited"])
        pdf_evidence_type = derive_pdf_evidence_type(
            pdf_exists=pdf_exists,
            pdf_status=pdf_status,
            evidence_status=evidence_status,
        )
        pdf_check_status = derive_pdf_check_status(
            pdf_evidence_type=pdf_evidence_type,
            pdf_exists=pdf_exists,
            evidence_status=evidence_status,
            source_limited=source_limited,
        )
        registry.append(
            {
                "asset_id": f"{paper['paper_id']}:primary_pdf",
                "paper_id": paper["paper_id"],
                "asset_role": "primary_pdf",
                "title": paper["title"],
                "pdf_path": pdf_path,
                "pdf_exists": pdf_exists,
                "sha256": compute_repo_relative_sha256(pdf_path, sha256_cache),
                "asset_size_bytes": compute_repo_relative_size_bytes(pdf_path),
                "pdf_status": pdf_status,
                "evidence_status": evidence_status,
                "pdf_evidence_type": pdf_evidence_type,
                "pdf_check_status": pdf_check_status,
                "is_main_text": pdf_evidence_type == "main_pdf",
                "is_supplementary": pdf_evidence_type == "supplementary_pdf",
                "source_limited": source_limited,
                "source_checked_at": paper["source_checked_at"],
                "primary_module_for_filing": paper["primary_module_for_filing"],
                "scientific_object_modules": paper["scientific_object_modules"],
                "general_method_bucket": paper["general_method_bucket"],
                "active_confirmed_core": paper["active_confirmed_core"],
                "exported_at": paper["exported_at"],
            }
        )
    return registry


def build_asset_manifest(
    papers: Iterable[Dict[str, object]], sha256_cache: Dict[str, str]
) -> List[Dict[str, object]]:
    manifest: List[Dict[str, object]] = []
    for paper in papers:
        note_path = str(paper["note_path"])
        pdf_path = str(paper["pdf_path"])
        manifest.append(
            {
                "asset_id": f"{paper['paper_id']}:note",
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "asset_type": "note",
                "path": note_path,
                "exists": paper["note_exists"],
                "sha256": compute_repo_relative_sha256(note_path, sha256_cache),
                "asset_size_bytes": compute_repo_relative_size_bytes(note_path),
                "asset_status": paper["note_status"],
                "is_main_text": False,
                "is_supplementary": False,
                "source_limited": paper["source_limited"],
                "source_checked_at": "",
                "exported_at": paper["exported_at"],
            }
        )
        pdf_exists = bool(paper["pdf_exists"])
        pdf_evidence_type = derive_pdf_evidence_type(
            pdf_exists=pdf_exists,
            pdf_status=str(paper["pdf_status"]),
            evidence_status=str(paper["evidence_status"]),
        )
        manifest.append(
            {
                "asset_id": f"{paper['paper_id']}:primary_pdf",
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "asset_type": "primary_pdf",
                "path": pdf_path,
                "exists": pdf_exists,
                "sha256": compute_repo_relative_sha256(pdf_path, sha256_cache),
                "asset_size_bytes": compute_repo_relative_size_bytes(pdf_path),
                "asset_status": paper["pdf_status"],
                "is_main_text": pdf_evidence_type == "main_pdf",
                "is_supplementary": pdf_evidence_type == "supplementary_pdf",
                "source_limited": paper["source_limited"],
                "source_checked_at": paper["source_checked_at"],
                "exported_at": paper["exported_at"],
            }
        )
    return manifest


def build_pdf_manifest(
    papers: Iterable[Dict[str, object]], sha256_cache: Dict[str, str]
) -> List[Dict[str, object]]:
    manifest: List[Dict[str, object]] = []
    for paper in papers:
        pdf_path = str(paper["pdf_path"])
        if not pdf_path or not bool(paper["pdf_exists"]):
            continue
        manifest.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "pdf_path": pdf_path,
                "sha256": compute_repo_relative_sha256(pdf_path, sha256_cache),
                "primary_module_for_filing": paper["primary_module_for_filing"],
                "scientific_object_modules": paper["scientific_object_modules"],
                "pdf_status": paper["pdf_status"],
                "evidence_status": paper["evidence_status"],
                "active_confirmed_core": paper["active_confirmed_core"],
            }
        )
    return manifest


def build_missing_pdf_manifest(papers: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    manifest: List[Dict[str, object]] = []
    for paper in papers:
        if not bool(paper["active_confirmed_core"]):
            continue
        if bool(paper["pdf_exists"]):
            continue
        manifest.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "doi": paper["doi"],
                "url": paper["url"],
                "pdf_status": paper["pdf_status"],
                "evidence_status": paper["evidence_status"],
                "source_limited": paper["source_limited"],
                "access_note": paper["remarks"],
            }
        )
    return manifest


def build_note_manifest(papers: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    manifest: List[Dict[str, object]] = []
    for paper in papers:
        manifest.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "note_path": paper["note_path"],
                "note_exists": paper["note_exists"],
                "active_confirmed_core": paper["active_confirmed_core"],
                "inclusion_status": paper["inclusion_status"],
            }
        )
    return manifest


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[Dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: Iterable[Dict[str, object]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    classification_code_index = load_classification_code_index()

    master_table = parse_markdown_table(
        MASTER_PATH,
        header_marker="| " + " | ".join(MASTER_HEADER) + " |",
        expected_header=MASTER_HEADER,
        data_prefix="| ASD-",
    )
    progress_table = parse_markdown_table(
        PROGRESS_PATH,
        header_marker="| " + " | ".join(PROGRESS_HEADER) + " |",
        expected_header=PROGRESS_HEADER,
        data_prefix="| ASD-",
    )
    progress_rows = {row["paper_id"]: row for row in progress_table.rows}

    change_log_rows = (
        load_jsonl_rows(CHANGE_LOG_PATH) if CHANGE_LOG_PATH.exists() else []
    )
    latest_change_log_by_paper_id = build_latest_change_log_index(change_log_rows)
    papers = build_papers(
        master_table.rows,
        progress_rows,
        latest_change_log_by_paper_id,
        classification_code_index,
    )
    discipline_code_assignments = (
        load_jsonl_rows(DISCIPLINE_CODE_ASSIGNMENTS_PATH)
        if DISCIPLINE_CODE_ASSIGNMENTS_PATH.exists()
        else []
    )
    sha256_cache: Dict[str, str] = {}
    taxonomy_index = build_taxonomy_index()
    source_commit, worktree_dirty = get_git_export_metadata()
    generated_at = str(papers[0]["exported_at"]) if papers else ""
    paper_registry = build_paper_registry(papers)
    paper_identifier_aliases = build_paper_identifier_aliases(papers)
    taxonomy_registry = build_taxonomy_registry(generated_at)
    classification_assignments = build_classification_assignments(papers)
    pdf_archive_registry = build_pdf_archive_registry(papers, sha256_cache)
    asset_manifest = build_asset_manifest(papers, sha256_cache)
    pdf_manifest = build_pdf_manifest(papers, sha256_cache)
    missing_pdf_manifest = build_missing_pdf_manifest(papers)
    note_manifest = build_note_manifest(papers)
    discipline_local_code_registry = build_discipline_local_code_registry(
        papers=papers,
        discipline_code_assignments=discipline_code_assignments,
        generated_at=generated_at,
        generated_by="export_structured_data.py",
        source_commit=source_commit,
        worktree_dirty=worktree_dirty,
    )
    discipline_code_initial_assignment_preview = build_discipline_initial_assignment_preview(
        papers, classification_code_index
    )

    write_jsonl(DATA_DIR / "papers.jsonl", papers)
    write_json(DATA_DIR / "taxonomy_index.json", taxonomy_index)
    write_json(DATA_DIR / "pdf_manifest.json", pdf_manifest)
    write_json(DATA_DIR / "missing_pdf_manifest.json", missing_pdf_manifest)
    write_json(DATA_DIR / "note_manifest.json", note_manifest)
    write_csv(
        DISCIPLINE_CODE_INITIAL_ASSIGNMENT_PREVIEW_PATH,
        discipline_code_initial_assignment_preview,
        PREVIEW_FIELDNAMES,
    )
    write_jsonl(DISCIPLINE_LOCAL_CODE_REGISTRY_PATH, discipline_local_code_registry)
    write_jsonl(REGISTRY_DIR / "paper_registry.jsonl", paper_registry)
    write_jsonl(REGISTRY_DIR / "paper_identifier_aliases.jsonl", paper_identifier_aliases)
    write_json(REGISTRY_DIR / "taxonomy_registry.json", taxonomy_registry)
    write_jsonl(
        REGISTRY_DIR / "classification_assignments.jsonl", classification_assignments
    )
    write_jsonl(REGISTRY_DIR / "pdf_archive_registry.jsonl", pdf_archive_registry)
    write_jsonl(REGISTRY_DIR / "asset_manifest.jsonl", asset_manifest)

    print(f"Exported {len(papers)} paper records to {DATA_DIR}")
    print(f"Exported {len(pdf_manifest)} local PDF manifest rows")
    print(f"Exported {len(missing_pdf_manifest)} missing PDF manifest rows")
    print(f"Exported {len(note_manifest)} note manifest rows")
    print(
        "Exported "
        f"{len(discipline_code_initial_assignment_preview)} initial discipline-code preview rows"
    )
    print(
        "Exported "
        f"{len(discipline_local_code_registry)} discipline local code registry rows"
    )
    print(f"Exported {len(paper_registry)} paper registry rows")
    print(f"Exported {len(paper_identifier_aliases)} paper identifier alias rows")
    print(f"Exported {len(classification_assignments)} classification assignment rows")
    print(f"Exported {len(pdf_archive_registry)} PDF archive registry rows")
    print(f"Exported {len(asset_manifest)} asset manifest rows")


if __name__ == "__main__":
    main()
