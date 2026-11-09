# CLAUDE.md — Hi-AUDiO FLO Practice-Based Evaluation

Working instructions for Claude Code. Read alongside [CONTEXT.md](CONTEXT.md) (full project background) and [docs/ANALYSIS_PLAN.md](docs/ANALYSIS_PLAN.md) (statistical methodology).

---

## What This Repo Is

A public academic repository publishing a practice-based evaluation of the Hi-Audio web audio platform (hiaudio.fr), conducted by the Female Laptop Orchestra (FLO) for Télécom Paris / Institut Mines-Télécom under ERC Horizon Europe grant No. 101052978. Served via GitHub Pages. All public-facing content must remain professional and consistent with academic report conventions.

---

## File Inventory

| File | Status | Rule |
|---|---|---|
| README.md | Published | Repository guide: what the repo is, links to the web pages, contents, positionality, licensing, citation. It no longer contains the memo |
| CONTEXT.md | Published | LLM/collaborator reference — keep current |
| docs/ANALYSIS_PLAN.md | Published | Data collection is complete — cleared for publication |
| docs/participant_survey.md | Published | Data collection is complete — cleared for publication |
| docs/output.md | Published | The memo as delivered (Pandoc conversion of the original .docx, with the author's one-word amendment of 2026-11-09 — see Hard Rules) and the source of docs/memo.html — never edit or delete |
| docs/participant_survey_responses.csv / .xlsx | Published | Canonical response data (no PII columns) — already corrected (Q16/Q17 collapsed), not a raw JotForm export |
| docs/individual_participant_responses/P01–P09.pdf | Published | Per-respondent submissions, pseudonymised as P01–P09 — cleared for publication |
| docs/response_id_mapping.md | Published | Maps PID ↔ original JotForm submission ID; also documents the identifier scheme and the reverse-chronological CSV row order |
| docs/analysis_summary.md | Approved by the owner, 2026-11-06 | Survey analysis by Nela Brown and José M. Gil Panal — source of docs/analysis.html and the source of truth for the analysis |
| index.html, docs/memo.html, docs/analysis.html | Generated | The website (GitHub Pages): landing page, memo page, analysis page. Rebuild with `python3 docs/build_pages.py` after any edit to their sources; never hand-edit |
| docs/build_pages.py | Published | Builds the three web pages from docs/output.md and docs/analysis_summary.md — standard library only |
| docs/REFERENCES.md | Published | Annotated reference list; the authority for item attribution (see "Item attribution" under Hard Rules) |
| docs/figures/ | Published | Analysis figures (SVG) + `make_figures.py`. Regenerate with the script; never hand-edit an SVG — the figures must stay reproducible from the CSV |
| docs/Practice-Based Evaluation...pdf | Published | The memo as delivered (PDF); replaced on 2026-11-09 by the author's amended version (§3) — do not modify |
| CITATION.cff | Published | Structured citation |
| AGENTS.md | Published | Working instructions for other AI agents — keep aligned with this file |
| docs/DATA_LICENSE.md | Published | Research-use licence for the response data — legal text, change only on explicit instruction |
| LICENSE | Published | CC BY 4.0, scoped to exclude the response data and the EU/ERC emblem — change only on explicit instruction |
| _config.yml | Published | Jekyll config — only change if explicitly asked |
| images/ | Published | Static assets — do not modify |

`invitation_message.md` has been removed from the repository entirely (not moved) — it is no longer part of this project's files.

---

## Hard Rules

- **docs/output.md is untouchable.** Never edit, overwrite, or delete its content. Exceptions used so far: first, when the file was relocated from repo root into `docs/`, its 8 relative image paths (`./images/imageN.png`) were updated to `../images/imageN.png` so they keep resolving from the new location — a path fix required by the move, not a content edit. Second exception, 2026-11-09, at the author's request and authorised by the repo owner: Nela Brown amended her memo, so §3's "across two separate two-hour sessions" now reads "across three separate two-hour sessions", as in her amended PDF (Appendix A lists three onboarding sessions led by the Lead Software Engineer). Do not make further changes unless the author amends the memo again and the owner authorises it.
- **docs/participant_survey.md, docs/ANALYSIS_PLAN.md, and the response data files are cleared for publication.** Data collection is complete, so the contamination risk that motivated withholding them no longer applies. `invitation_message.md` was removed from the repo entirely (not published).
- **Acknowledgements is always the last section in README.md**, after any appendices. Never reorder it.
- **No personal identifiers.** Do not add email addresses, phone numbers, or names beyond what already exists. The institutional email appears as `[available on request]` in docs/participant_survey.md. One exception is already present and accepted: P09's Q7 answer names Nela Brown in a track filename — left as-is per her dual role as questionnaire co-designer/respondent (see "Respondent overlap" below and CONTEXT.md).
- **Item attribution (corrected 2026-08-20 — the earlier "never name TAM" rule is superseded).** Q18 reproduces Venkatesh's (2000, Appendix 1) four-item Perceived Ease of Use scale and Q19 the three-item Perceived Enjoyment scale from the same appendix, both with the verb tense changed present→past and "the Hi-Audio platform" in place of "the system" (Q18_2 also drops "my"); Q20_2 is Davis's (1989) usefulness item with the domain changed; Q20_4, Q16 and Q17 were written for this study. **Q20_1/Q20_3 are attitude and behavioural-intention items whose direct wording source has not been established — do not attribute them to Davis (1989)**, which developed the usefulness and ease-of-use scales only. Cite Venkatesh (2000) for the Q18/Q19 wording; never write that no items are reproduced. Still required: the instrument **as assembled** is not standardised and was never re-validated, so no comparison against published norms and no treating block means as validated subscale scores. **SUS and NASA-TLX were not administered here and none of their items appear** — that claim is safe. **USE, AttrakDiff and UEQ were also not administered and not used as sources, but do not claim zero item overlap for them**: Lund's USE contains close variants of "easy to use", "recommend it to a friend", "fun to use" and "pleasant to use". See `docs/REFERENCES.md` and AGENTS.md Rule 5.
- **Q16/Q17 are single 7-point questions**, confirmed in the JotForm builder (one matrix row each, blank row-name field). An earlier JotForm export defect split them into 4 bogus sub-columns (`>> Service Quality` etc. — never real form content); `docs/participant_survey_responses.csv`/`.xlsx` have already been corrected to one clean column per question. Usable as the intended headline suitability/artistic-fit metrics with no further preprocessing. See `docs/ANALYSIS_PLAN.md`.
- **Respondent overlap.** Nela Brown (questionnaire co-designer, memo author) is also P09 in the response dataset. See "Researcher Positionality" in `docs/ANALYSIS_PLAN.md` before computing or reporting aggregate stats.
- **No inferential statistics** (t-tests, ANOVA, regressions, confidence intervals) unless explicitly instructed. Expected ~9 participants — a sample this small does not justify them on its own, so do not make that judgement call independently. Report means, medians, ranges. Frame all findings as exploratory and descriptive. Scope all claims to this small expert cohort.
- **Do not push to remote without explicit instruction.**

---

## Statistical Analysis Workflow

Activates when JotForm CSV response data is available. Expected: ~9 rows (one per FLO participant).

### Data Preparation

1. Import CSV; confirm row count.
2. Rename columns to Q1–Q23 (JotForm headers may differ).
3. Remove any name, email, IP, or identifier column before any further step.
4. The response data (`docs/participant_survey_responses.csv`/`.xlsx`, individual PDFs) is already committed and cleared for publication — no further raw-data commit decision needed. Any *new*/derived working file (e.g. a numeric-recoded copy for computing means) is local-only; only commit `docs/analysis_summary.md` once reviewed and approved.

### Quantitative

**Before computing any mean/median for Q16–Q20:** the CSV stores these as text labels ("Strongly disagree" ... "Strongly agree"), not numbers 1–7. Recode to numeric first (see AGENTS.md Step 1b for the exact mapping) — this recoded copy is a local working file, not something to commit; the published CSV/XLSX intentionally keep the original text labels.

**Q1–Q15** — frequency counts and percentages per option; narrative sample description.
- **Q1 and Q8** are multiple-choice (select all that apply) — count each option independently, not as mutually exclusive.
- **Q3, Q4, Q6, Q7** use configurable list or multiple-entry widgets. **Q3/Q4** collect tool names and are hand-categorised then counted in the published analysis (say so in the write-up); **Q6/Q7** collect instruments and track content and stay prose-only, without counts.
- **Map columns by header text, never by position.** A raw JotForm export and the published CSV do not share a column count or ordering, so positional addressing silently produces wrong results.
- **Never edit the raw response files.** `docs/participant_survey_responses.csv`/`.xlsx` and the individual PDFs are read-only inputs. Derived working copies stay local.
- Q10 is conditional on Q9 = "No" — use only those rows as denominator.

**Q16 (headline metric) and Q17** are single 7-point rating questions — mean, median, range. Q16 (meets the necessary standards as a professional audio recording application) is reported first and prominently. Its construct is professional standards only — artistic-intention support is Q17; do not merge the two into a "professional/artistic" judgement.

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

**Do not reverse-code Q18_2.** It is worded so that a higher score indicates *lower* mental effort, which is intentional and already consistent in direction with the other Q18 items. Reverse-coding it would silently change every Q18 figure. Do not reverse-code it unless explicitly asked.

### Qualitative

Open-text Q21, Q22, Q23 — thematic coding, hybrid deductive/inductive.

**Deductive frames (from the memo — `docs/output.md`, published as `docs/memo.html`; same section numbers):**

| Question | Coding frame source |
|---|---|
| Q22 (challenges) | §5 challenge taxonomy: visual feedback, transport controls, editing, file format, latency, browser/network compatibility, workflow integration |
| Q21 (strengths) | §4 Platform Strengths: browser access, no install, multi-track, collaboration, sharing ease |
| Q23 (use cases) | §7 Assessment of Platform Fit as the primary frame, **plus** both the §4 strengths and §5 challenges frames above — and remain open to inductive themes fitting none of them |

**Inductive:** flag themes not covered by deductive frames — these are potential new findings.

**Per-question output:** theme list with a short description each (1–2 sentences), **one or two** representative pseudonymised excerpts per theme — never more — and a note on whether each theme confirms / nuances / contradicts / extends the practice-based memo.

### Triangulation

Compare survey findings against the memo's §4–§8 (`docs/output.md`):
- §4 Platform Strengths ↔ Q21
- §5 Workflow Challenges ↔ Q22
- §6 Design Implications ↔ Q22, Q23
- §7 Assessment of Platform Fit ↔ Q16, Q17, Q20
- §8 Key Findings ↔ which §8 priorities the survey does and does not independently corroborate

Output: triangulation table or narrative noting confirmation, nuance, contradiction, new findings.

### Deliverables

Produce `docs/analysis_summary.md` (full write-up: sample description, quantitative tables, thematic summaries, triangulation). Do not commit until reviewed and approved.

---

## Reporting Conventions

- Academic, professional tone.
- Scope claims: "among FLO participants in this study..." — never generalise beyond this sample.
- For Q18–Q20, cite Venkatesh (2000) for the Q18/Q19 item wording and state that the assembled instrument was never re-validated — not that the items were written for this study.
- Separate descriptive findings from interpretation.
