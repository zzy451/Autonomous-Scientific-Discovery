# Coder brief: O / V / A coding of agent-for-science papers

You code papers on three axes defined in `classification_protocol.md` (same folder): read it first, fully. It is in Chinese; the level tables and boundaries are the rules.

For each paper id you are given, read `packets/<paper_id>.txt`. Each packet line is `L<n>: <text>`, where `<n>` is the line number in the original papercard note. Code only from what the packet says. Do not use outside knowledge of the paper, and do not guess beyond the text.

Write one JSON object per line (JSONL) to the output file you are given, with exactly these keys:

```
{"paper_id": "ASD-0010",
 "openness": "O1".."O6", "openness_rationale_zh": "<one sentence>",
 "openness_quote": "<verbatim text copied from ONE packet line>", "openness_line": <that line's n>,
 "verification": "V0".."V4", "verification_rationale_zh": "<one sentence>",
 "verification_quote": "<verbatim text copied from ONE packet line>", "verification_line": <n>,
 "autonomy": "A0".."A3", "autonomy_rationale_zh": "<one sentence>",
 "contested": false, "contested_quote": "",
 "confidence": "high" | "medium" | "low", "needs_fulltext_review": true | false}
```

Hard rules:
- Each quote must be ONE contiguous substring copied character for character from the packet line whose number you give, with the `L<n>: ` prefix removed. Never join fragments, drop words in the middle, or translate. Keep each quote short, 8–60 characters. A quote that does not appear verbatim on that line is rejected automatically.
- Code the most open problem the paper actually attempted **with reported results**. Code V for that problem's result, not the strongest result anywhere in the paper.
- V3 needs a physical or prospective experiment, or a machine-checked proof, that covers the core scientific claim. V4 needs explicit independent or third-party replication. A note saying such validation is missing or still needed is evidence **against** V3/V4.
- When evidence is thin, give your best code, set confidence to low and needs_fulltext_review to true. Never invent a level outside the tables.
- `contested` is true only when the packet records that the result was challenged, retracted or refuted; then quote it.
- Write only your own output file. Do not read or write any other coder's output.

When finished, reply with one line: how many papers you coded and how many you marked low confidence.
