"""Proxy coding for the proposal's axes, derived from existing per-paper labels.

The corpus has no O1-O6 (openness) or V0-V4 (verification) coding. Two proxies are built
from labels already in Data/papers.jsonl, with explicit keyword rules; ambiguous values
fall to the lower level (conservative).

  E0-E3  evidence endpoint (from validation_type; max over a paper's values)
         E0 benchmark / ablation only      E1 expert or case evaluation
         E2 computational or simulation    E3 physical experiment, clinical data,
                                              field deployment or formal proof (self-reported);
                                              a computational "controlled experiment" is E2
  L1-L4  research-loop reach (from research_workflow_role; max over values)
         L1 analysis, tools, orchestration L2 designs / runs experiments, optimises
         L3 generates hypotheses           L4 formulates questions / end-to-end autonomy

Writes derived/proxies.csv. Usage: python3 proxies.py
"""
import csv, json, collections as C
from style import SRC, DER

E_RULES = [  # (tier, keywords) - checked from the highest tier down
    (3, ["wet_lab", "robotic_experiment", "closed_loop_experiment", "high_throughput_experiment",
         "experimental_validated", "clinical_data", "real_world_deployment", "mission_operation",
         "lean_kernel_check", "形式化验"]),
    # "对照实验" (controlled comparison) in these records is computational - always paired with benchmark
    (2, ["对照实验"]),
    (2, ["computational_validation", "computationally_validated", "simulation_validation",
         "high_throughput_computation", "计算验证", "实验或"]),
    (1, ["expert_evaluation", "case_study", "对照评估", "匹配对照", "反事实"]),
    (0, ["benchmark", "基准", "消融", "故障测试", "压力测试", "留出验证", "全文实验"]),
]
L_RULES = [
    (4, ["scientific_question_formulation", "end_to_end_research_automation", "科提出", "研究项目规划",
         "科规划"]),
    (3, ["hypothesis_generation"]),
    # in-loop choices (e.g. a rover selecting targets) are L2, not question formulation
    (2, ["experimental_design", "experiment_execution", "optimization", "feedback_iteration",
         "autonomous_decision_making", "molecular_design", "实验", "科研执"]),
    (1, [""]),     # anything else that is present
]
E_NAME = {0: "Benchmark only", 1: "Expert or case evaluation", 2: "Computational / simulation",
          3: "Physical, clinical, deployed or formal"}
L_NAME = {1: "Analysis & execution", 2: "Experiment design & optimisation", 3: "Hypothesis generation",
          4: "Question formulation & end-to-end"}


def fix(s):
    """Undo UTF-8-read-as-GBK mojibake present in a few records."""
    try:
        return s.encode("gbk").decode("utf-8")
    except UnicodeError:
        try:
            return s.encode("gbk", errors="ignore").decode("utf-8", errors="ignore")
        except UnicodeError:
            return s


def tier(values, rules):
    vals = [fix(v) for v in values]
    for lvl, kws in rules:
        if any(k in v for v in vals for k in kws):
            return lvl
    return None


def main():
    core = {r["paper_id"] for r in csv.DictReader(open(DER / "papers.csv", encoding="utf-8"))}
    rows = []
    for line in open(SRC / "papers.jsonl", encoding="utf-8"):
        p = json.loads(line)
        if p["paper_id"] not in core:
            continue
        rows.append(dict(paper_id=p["paper_id"],
                         evidence_tier=tier(p.get("validation_type") or [], E_RULES),
                         loop_reach=tier(p.get("research_workflow_role") or [], L_RULES),
                         validation_type=";".join(fix(v) for v in p.get("validation_type") or []),
                         workflow_role=";".join(fix(v) for v in p.get("research_workflow_role") or [])))
    with open(DER / "proxies.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(len(rows), "E:", sorted(C.Counter(r["evidence_tier"] for r in rows).items(), key=str),
          "L:", sorted(C.Counter(r["loop_reach"] for r in rows).items(), key=str))


CODED = DER.parent / "ov_coding" / "increment" / "classification_results_662.jsonl"
# Figures now read the coded axes (RUBRIC.md, proposal scales). Tier = verification with V3/V4 merged as the
# strong tier: 0 = V0 claim, 1 = V1 benchmark/internal, 2 = V2 computational/simulation/retrospective,
# 3 = V3-V4 physical experiment, proof or replication. Level = system autonomy L1-L3.
E_NAME = {0: "Claim only (V0)", 1: "Benchmark / internal (V1)", 2: "Computational / simulation (V2)",
          3: "Strong: experiment, proof or replication (V3–V4)"}
L_NAME = {0: "Tool (L0)", 1: "Task assistant (L1)", 2: "Closed-loop executor (L2)", 3: "Autonomous researcher (L3)"}
O_NAME = {1: "Rule world (O1)", 2: "Fixed benchmark (O2)", 3: "New instance (O3)", 4: "Needs physical test (O4)",
          5: "Open mathematics (O5)", 6: "Open science (O6)"}


def load_ov():
    """paper_id -> (O 1-6, V 0-4, L 0-3) from the coded increment."""
    out = {}
    for line in open(CODED, encoding="utf-8"):
        r = json.loads(line)
        if r["coded"]:
            out[r["paper_id"]] = (int(r["openness"][1]), int(r["verification"][1]), int(r["autonomy"][1]))
    return out


def load():
    """paper_id -> (evidence tier 0-3, autonomy level 1-3), from the coded axes."""
    return {pid: (min(v, 3), L) for pid, (o, v, L) in load_ov().items()}


def load_proxy():
    """The earlier label-derived proxies (E0-E3 from validation_type, reach L1-L4), kept for comparison."""
    out = {}
    for r in csv.DictReader(open(DER / "proxies.csv", encoding="utf-8")):
        out[r["paper_id"]] = (int(r["evidence_tier"]) if r["evidence_tier"] else None,
                              int(r["loop_reach"]) if r["loop_reach"] else None)
    return out


if __name__ == "__main__":
    main()
