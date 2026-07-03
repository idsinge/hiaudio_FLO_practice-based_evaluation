# CLAUDE.md — Hi-AUDiO FLO Practice-Based Evaluation

Working instructions for Claude Code. Read alongside [CONTEXT.md](CONTEXT.md) (full project background) and [docs/ANALYSIS_PLAN.md](docs/ANALYSIS_PLAN.md) (statistical methodology).

---

## What This Repo Is

A public academic repository publishing a practice-based evaluation of the Hi-Audio web audio platform (hiaudio.fr), conducted by the Female Laptop Orchestra (FLO) for Télécom Paris / Institut Mines-Télécom under ERC Horizon Europe grant No. 101052978. Served via GitHub Pages. All public-facing content must remain professional and consistent with academic report conventions.

---

## File Inventory

| File | Status | Rule |
|---|---|---|
| README.md | Published | Primary public document — edits go here, not docs/output.md |
| CONTEXT.md | Published | LLM/collaborator reference — keep current |
| docs/ANALYSIS_PLAN.md | Published | Data collection is complete — cleared for publication |
| docs/participant_survey.md | Published | Data collection is complete — cleared for publication |
| docs/output.md | Published | Read-only historical record — never edit or delete |
| docs/participant_survey_responses.csv / .xlsx | Published | Raw response data (no PII columns) — cleared for publication |
| docs/individual_participant_responses/P01–P09.pdf | Published | Per-respondent submissions, anonymised as P01–P09 — cleared for publication |
| docs/response_id_mapping.md | Published | Maps PID ↔ original JotForm submission ID |
| docs/Practice-Based Evaluation...pdf | Published | Original PDF memo — do not modify |
| CITATION.cff | Published | Structured citation |
| _config.yml | Published | Jekyll config — only change if explicitly asked |
| images/ | Published | Static assets — do not modify |

`invitation_message.md` has been removed from the repository entirely (not moved) — it is no longer part of this project's files.

---

## Hard Rules

- **docs/output.md is untouchable.** Never edit, overwrite, or delete its content. Exception already used once: when the file was relocated from repo root into `docs/`, its 8 relative image paths (`./images/imageN.png`) were updated to `../images/imageN.png` so they keep resolving from the new location — a path fix required by the move, not a content edit. Do not make further changes.
- **docs/participant_survey.md, docs/ANALYSIS_PLAN.md, and the response data files are cleared for publication.** Data collection is complete, so the contamination risk that motivated withholding them no longer applies. `invitation_message.md` was removed from the repo entirely (not published).
- **Acknowledgements is always the last section in README.md**, after any appendices. Never reorder it.
- **No personal identifiers.** Do not add email addresses, phone numbers, or names beyond what already exists. The institutional email appears as `[available on request]` in docs/participant_survey.md. One exception is already present and accepted: P09's Q7 answer names Nela Brown in a track filename — left as-is per her dual role as questionnaire designer/respondent (see "Respondent overlap" below and CONTEXT.md).
- **Framework language.** Q18–Q20 were designed for this study and are informed by established usability and technology acceptance literature. Always say "informed by" or "adapts constructs from" — never name or "use"/"apply" specific named instruments (USE, AttrakDiff, UEQ, TAM).
- **Q16/Q17 are single 7-point questions**, confirmed in the JotForm builder (one matrix row each, blank row-name field). An earlier JotForm export defect split them into 4 bogus sub-columns (`>> Service Quality` etc. — never real form content); `docs/participant_survey_responses.csv`/`.xlsx` have already been corrected to one clean column per question. Usable as the intended headline suitability/artistic-fit metrics with no further preprocessing. See `docs/ANALYSIS_PLAN.md`.
- **Respondent overlap.** Nela Brown (questionnaire designer, memo author) is also P09 in the response dataset. See "Researcher Positionality" in `docs/ANALYSIS_PLAN.md` before computing or reporting aggregate stats.
- **No inferential statistics** unless sample size clearly justifies it. Expected ~9 participants. Report means, medians, ranges. Scope all claims to this small expert cohort.
- **Do not push to remote without explicit instruction.**

---

## Statistical Analysis Workflow

Activates when JotForm CSV response data is available. Expected: ~9 rows (one per FLO participant).

### Data Preparation

1. Import CSV; confirm row count.
2. Rename columns to Q1–Q23 (JotForm headers may differ).
3. Remove any name, email, IP, or identifier column before any further step.
4. The response data (`docs/participant_survey_responses.csv`/`.xlsx`, individual PDFs) is already committed and cleared for publication — no further raw-data commit decision needed. Any *new*/derived working file (e.g. a numeric-recoded copy for computing means) is local-only; only commit `analysis_summary.md` once reviewed and approved.

### Quantitative

**Before computing any mean/median for Q16–Q20:** the CSV stores these as text labels ("Strongly disagree" ... "Strongly agree"), not numbers 1–7. Recode to numeric first (see AGENTS.md Step 1b for the exact mapping) — this recoded copy is a local working file, not something to commit; the published CSV/XLSX intentionally keep the original text labels.

**Q1–Q15** — frequency counts and percentages per option; narrative sample description.
- Q8 is multiple-choice (select all that apply) — count options independently.
- Q10 is conditional on Q9 = "No" — use only those rows as denominator.

**Q16 (headline metric) and Q17** are single 7-point rating questions — mean, median, range. Q16 (suitability for professional/artistic use) is reported first and prominently.

**Q18 — Pragmatic Usability (4 items, 7-point matrix)** — mean per item:

| Column | Statement |
|---|---|
| Q18_1 | Interaction was clear and understandable |
| Q18_2 | Did not require a lot of mental effort |
| Q18_3 | Easy to use |
| Q18_4 | Easy to get it to do what I wanted |

**Q19 — Hedonic/Experiential Quality (3 items, 7-point matrix)** — mean per item:

| Column | Statement |
|---|---|
| Q19_1 | Enjoyable |
| Q19_2 | Process was pleasant |
| Q19_3 | Had fun |

**Q20 — Future Use Intent and Perceived Usefulness (4 items, 7-point matrix)** — mean per item:

| Column | Statement |
|---|---|
| Q20_1 | Would be a good idea to use for recording music |
| Q20_2 | Would find it useful for recording music |
| Q20_3 | Would plan to use in a future project |
| Q20_4 | Would recommend to colleagues |

Scale midpoint is 4.0 — reference it when interpreting means.

### Qualitative

Open-text Q21, Q22, Q23 — thematic coding, hybrid deductive/inductive.

**Deductive frames (from README.md):**

| Question | Coding frame source |
|---|---|
| Q22 (challenges) | §5 challenge taxonomy: visual feedback, transport controls, editing, file format, latency, browser/network compatibility, workflow integration |
| Q21 (strengths) | §4 Platform Strengths: browser access, no install, multi-track, collaboration, sharing ease |
| Q23 (use cases) | §7 Platform Fit — also open inductive |

**Inductive:** flag themes not covered by deductive frames — these are potential new findings.

**Per-question output:** theme list with short descriptions, anonymised example excerpts, note whether each theme confirms / nuances / contradicts / extends the practice-based memo.

### Triangulation

Compare survey findings against README.md §4–§7:
- §4 Platform Strengths ↔ Q21
- §5 Workflow Challenges ↔ Q22
- §6 Design Implications ↔ Q22, Q23
- §7 Platform Fit and Future Use ↔ Q16, Q17, Q20

Output: triangulation table or narrative noting confirmation, nuance, contradiction, new findings.

### Deliverables

Produce `analysis_summary.md` (full write-up: sample description, quantitative tables, thematic summaries, triangulation). Do not commit until reviewed and approved.

---

## Reporting Conventions

- Academic, professional tone.
- Scope claims: "among FLO participants in this study..." — never generalise beyond this sample.
- For Q18–Q20, note they are study-specific items informed by established approaches, not a validated standardised scale.
- Separate descriptive findings from interpretation.
