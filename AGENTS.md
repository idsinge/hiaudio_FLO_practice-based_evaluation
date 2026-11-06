# AGENTS.md — Hi-AUDiO FLO Practice-Based Evaluation

Working instructions for AI coding agents (Codex and others). Read this file before making any changes. For full project background, read [CONTEXT.md](CONTEXT.md). For the statistical analysis plan, read [docs/ANALYSIS_PLAN.md](docs/ANALYSIS_PLAN.md).

---

## Project Summary

This repository publishes a practice-based evaluation of the Hi-Audio web audio platform (hiaudio.fr), conducted by the Female Laptop Orchestra (FLO) for Télécom Paris / Institut Mines-Télécom. The work is funded by the European Research Council under Horizon Europe (grant No. 101052978, project: "Hybrid and Interpretable Deep Neural Audio Machines"). The repository is public and served via GitHub Pages at https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/.

---

## File Inventory — What You Can and Cannot Touch

| File | Edit? | Commit? | Purpose |
|---|---|---|---|
| README.md | Yes | Yes | Repository guide — what the repo is, links to the web pages, contents, positionality, licensing, citation |
| CONTEXT.md | Yes | Yes | LLM/collaborator context — keep it current |
| docs/ANALYSIS_PLAN.md | Yes | Yes | Statistical analysis plan — data collection closed, cleared for publication |
| docs/participant_survey.md | Yes | Yes | Survey working copy — data collection closed, cleared for publication |
| docs/output.md | **Never** | Already published | The memo as delivered (original Pandoc conversion) and the source of docs/memo.html |
| docs/participant_survey_responses.csv / .xlsx | No | Yes | Canonical response data — no PII columns; already corrected (Q16/Q17 collapsed from the bogus 4-column export split), so not a raw JotForm export |
| docs/individual_participant_responses/P01–P09.pdf | No | Yes | Per-respondent submissions, pseudonymised as P01–P09 |
| docs/response_id_mapping.md | Yes | Yes | Maps PID ↔ original JotForm submission ID; also documents the identifier scheme and the reverse-chronological CSV row order |
| docs/analysis_summary.md | Yes | Yes | Survey analysis by Nela Brown and José M. Gil Panal — source of docs/analysis.html; the source of truth for the analysis |
| index.html, docs/memo.html, docs/analysis.html | Via script only | Yes | The website (GitHub Pages). Rebuild with `python3 docs/build_pages.py`; never hand-edit |
| docs/build_pages.py | Yes | Yes | Builds the three web pages — standard library only |
| docs/REFERENCES.md | Yes | Yes | Annotated reference list; the authority for item attribution (see Rule 5) |
| docs/figures/ | Via script only | Yes | Analysis figures (SVG) + `make_figures.py`. Regenerate with the script; never hand-edit an SVG |
| docs/Practice-Based Evaluation...pdf | No | No | The memo as delivered (PDF) |
| CITATION.cff | Yes | Yes | Structured citation for GitHub |
| CLAUDE.md | Yes | Yes | Working instructions for Claude Code — keep aligned with this file |
| docs/DATA_LICENSE.md | Only if asked | Yes | Research-use licence for the response data — legal text |
| LICENSE | Only if asked | Yes | CC BY 4.0, scoped to exclude the response data and the EU/ERC emblem |
| _config.yml | Only if asked | Only if asked | Jekyll theme config |
| images/ | No | No | Static images — do not add, remove, rename |

`invitation_message.md` has been removed from the repository entirely — do not recreate it without instruction.

---

## Rules — Read These Before Doing Anything

### Rule 1: docs/output.md is read-only
`docs/output.md` is the original Pandoc conversion of the evaluation memo from .docx: the memo as delivered, and the source of `docs/memo.html`. Do not edit, overwrite, or delete its content. Ever. Exception already used once: when the file was relocated from repo root into `docs/`, its 8 relative image paths (`./images/imageN.png`) were updated to `../images/imageN.png` so they keep resolving from the new location — a path fix required by the move, not a content edit. Do not make further changes.

### Rule 2: docs/participant_survey.md, docs/ANALYSIS_PLAN.md, and the response data are cleared for publication
Data collection from participants is complete, so the risk that motivated withholding these files — contaminating participant responses before they replied — no longer applies. `invitation_message.md` was removed from the repo entirely (not published, not withheld pending approval — simply gone).

### Rule 3: Acknowledgements is always last in README.md
The Acknowledgements section must remain the final section of README.md, after any appendices. Do not move it.

### Rule 4: No personal identifiers in any file
Do not add email addresses, phone numbers, or full names to any file beyond what already exists. The institutional email is written as `[available on request]` in docs/participant_survey.md. Keep it that way. One accepted exception: P09's Q7 response names Nela Brown in a track filename — left as-is given her dual role as questionnaire co-designer/respondent (see Rule 8 below and CONTEXT.md).

### Rule 5: Attribute the Q18–Q20 items correctly
**Corrected 2026-08-20 — an earlier version of this rule said the opposite and is superseded.** Item-level comparison against the primary sources shows that Q18 and Q19 *do* reproduce published scales:

- **Q18** = Venkatesh (2000, Appendix 1) four-item **Perceived Ease of Use** scale, verbatim except the tense is shifted present→past, "the system" becomes "the Hi-Audio platform", and Q18_2 drops "my" ("a lot of my mental effort" → "a lot of mental effort").
- **Q19** = the three-item **Perceived Enjoyment** scale from the same appendix, same treatment.
- **Q20_2** = Davis (1989) perceived-usefulness item, domain changed from "in my job" to "for recording music". **Q20_4** (recommendation), **Q16** and **Q17** were written for this study.
- **Q20_1 / Q20_3** are attitude and behavioural-intention items in the technology-acceptance tradition, but **their direct wording source has not been established.** Do not attribute them to Davis (1989): that paper developed the perceived-usefulness and perceived-ease-of-use scales, not attitude or intention scales. Either leave their provenance explicitly open, or establish it against a primary source first.

Cite **Venkatesh (2000)** for the Q18/Q19 item wording, **Davis (1989)** for perceived usefulness and perceived ease of use, and **Davis, Bagozzi & Warshaw (1992)** as the upstream origin of the enjoyment items. Do **not** write that no items are reproduced — that is a false attribution claim, and a worse error than overclaiming.

What still holds, and must be stated wherever results are reported: the instrument **as assembled** is not a standardised questionnaire and was never re-validated for this population. Items were recombined across sources and n = 9 cannot establish reliability. So: no comparison against published norms for any source scale, and no treating block means as validated subscale scores. Note two distinct things here and do not merge them — the **verb tense** was changed present→past, and the **framing** moved from a system in current use to one recalled months later.

**SUS and NASA-TLX were not administered in this study and none of their items appear.** That claim is safe: their items are distinctive, and both belong to the companion 22-participant study, not this one.

**USE, AttrakDiff and UEQ were likewise not administered and were not used as sources** — but do not extend the "none of their items appear" wording to them. Lund's USE questionnaire contains "It is easy to use", "I would recommend it to a friend", "It is fun to use" and "It is pleasant to use", which resemble Q18_3, Q20_4, Q19_3 and Q19_2 closely enough that a categorical no-overlap claim is indefensible. The resemblance reflects a shared construct vocabulary, not derivation from USE.

Full attribution table: [`docs/REFERENCES.md`](docs/REFERENCES.md).

### Rule 6: Small sample — descriptive statistics only
The expected participant count is approximately 9 FLO performers. This is a small expert sample. Do not apply inferential statistics (t-tests, ANOVA, regressions, confidence intervals) unless explicitly instructed. Report means, medians, and ranges. Frame all findings as exploratory and descriptive. Scope every claim to "FLO participants in this study" — never generalise.

### Rule 7: No remote pushes without instruction
Stage and commit locally only when asked. Never force-push.

### Rule 8: Respondent overlap — Nela Brown is P09
Nela Brown co-designed this questionnaire (with José M. Gil Panal, the Hi-AUDiO lead software engineer), authored the evaluation memo, co-authored the survey analysis, and is also P09 in the response dataset. Before computing or reporting any aggregate statistic or thematic summary, read "Researcher Positionality" in `docs/ANALYSIS_PLAN.md` — it specifies reporting n=9 as primary but also computing n=8 (P09 excluded) for headline metrics, and flagging P09-sourced excerpts in thematic coding.

---

## Statistical Analysis Workflow

This section applies when JotForm survey response data has been received. Data will arrive as a CSV file exported from JotForm (one row per participant, columns are question responses).

### Step 1 — Ingest and Clean Data

```python
import pandas as pd

df = pd.read_csv('responses.csv')
print(f"Rows: {len(df)}")  # Expected: ~9
print(df.columns.tolist())  # Review JotForm column names
```

- Confirm row count matches the expected number of participants.
- Rename columns to Q1, Q2, ... Q23 for consistency. JotForm exports verbose column names — **match them by header text (each begins with its question number), never by column order or position.** A raw JotForm export and the published CSV do not share a column count or ordering, so positional addressing silently produces wrong results.
- **Remove immediately:** any column containing participant names, email addresses, IP addresses, or submission metadata that could identify individuals.
- The response data is already committed at `docs/participant_survey_responses.csv`/`.xlsx` — it was screened for PII and cleared for publication (see CONTEXT.md). Do not commit any *further* raw data (e.g. a fresh JotForm export) without the same screening.

### Step 1b — Recode 7-Point Scale Columns to Numeric

The CSV stores Q16, Q17, and the Q18–Q20 matrix items as text labels ("Strongly disagree" ... "Strongly agree"), not numbers. Recode before computing any mean/median/describe — calling those directly on the text columns will fail or silently produce nonsense.

```python
scale_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Somewhat disagree': 3,
    'Neither disagree nor agree': 4,
    'Somewhat agree': 5,
    'Agree': 6,
    'Strongly agree': 7,
}
scale_cols = ['Q16', 'Q17',
              'Q18_1', 'Q18_2', 'Q18_3', 'Q18_4',
              'Q19_1', 'Q19_2', 'Q19_3',
              'Q20_1', 'Q20_2', 'Q20_3', 'Q20_4']
for col in scale_cols:
    df[col] = df[col].map(scale_map)
    assert df[col].notna().all(), f'{col} has an unmapped value — check for typos/variants in the raw text'
```

This recoded `df` is a local working copy for analysis only — do not commit it. The published `docs/participant_survey_responses.csv`/`.xlsx` intentionally keep the original text labels (more legible/self-explanatory for anyone opening the raw file directly).

### Step 2 — Q1–Q15: Background and Setup (Frequency Counts)

For each closed question in Q1–Q15, compute frequency counts and percentages per response option.

```python
for col in ['Q1', 'Q2', 'Q5', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15']:
    print(df[col].value_counts())
    print(df[col].value_counts(normalize=True).mul(100).round(1))
```

**Special cases:**
- **Q1 and Q8** are multiple-choice (select all that apply). Each option is counted independently — not as mutually exclusive. JotForm may export these as comma-separated strings in one column; parse accordingly.
- **Q10** is conditional — shown only when Q9 = "No". When computing Q10 frequencies, use only the rows where Q9 = "No" as the denominator.
- **Q3, Q4, Q6, Q7** use configurable list or multiple-entry widgets. JotForm may export these as lists or repeated columns. **Q3 and Q4** collect tool names, so entries can be categorised by hand and then counted, which is what the published analysis does — state in the write-up that the categorisation was manual. **Q6 and Q7** collect instruments and track content, which do not reduce to comparable categories; summarise those in prose without counts.

Produce a short narrative summary of the sample covering: musical roles, prior tool experience, recording methods, latency measurement behaviour, session structure, time spent, OS and browser, headphone type.

### Step 3 — Q16 and Q17: Suitability and Artistic-Intent Ratings

```python
for q in ['Q16', 'Q17']:
    print(df[q].describe())
```

- **Q16** (meets the necessary standards as a professional audio recording application) is the **headline metric**. Report it first and prominently. Its construct is professional standards only — artistic-intention support is Q17; do not merge them.
- **Q17** (artistic intention support) is a supporting metric.
- Both are single 7-point questions on the live form — confirmed directly in the JotForm builder, which shows each has exactly one matrix row with a blank row-name field (JotForm's own "Type Row Name" placeholder, not a real label). An earlier JotForm export defect split them into 4 bogus sub-columns (suffixed `>> Service Quality`, `>> Cleanliness`, `>> Responsiveness`, `>> Friendliness` — never real form content); `docs/participant_survey_responses.csv`/`.xlsx` have already been corrected to one clean column per question, so no further preprocessing is needed here.
- **Respondent overlap:** Nela Brown (questionnaire co-designer, memo author, evaluator) is also P09 in the response dataset. Before computing or reporting any aggregate statistic or thematic summary, read the "Researcher Positionality" section in `docs/ANALYSIS_PLAN.md` — it specifies reporting n=9 as primary but also computing n=8 (P09 excluded) for headline metrics, and flagging P09-sourced excerpts in thematic coding.
- Scale: 1–7, "Strongly disagree → Strongly agree". Scale midpoint is 4.0.

### Step 4 — Q18: Pragmatic Usability Matrix (4 Items, 7-Point)

JotForm exports matrix rows as separate columns. Map them as follows:

| Column name | Statement |
|---|---|
| Q18_1 | My interaction with the Hi-Audio platform was clear and understandable |
| Q18_2 | Interacting with the Hi-Audio platform did not require a lot of mental effort |
| Q18_3 | I found the Hi-Audio platform to be easy to use |
| Q18_4 | I found it easy to get the Hi-Audio platform to do what I wanted it to do |

```python
q18_cols = ['Q18_1', 'Q18_2', 'Q18_3', 'Q18_4']
print(df[q18_cols].mean())
print(df[q18_cols].median())
```

Compute mean, median, and range per item. Note: Q18_2 is worded so that higher scores indicate lower mental effort — this is intentional. Do not reverse-code unless explicitly asked.

### Step 5 — Q19: Hedonic/Experiential Quality Matrix (3 Items, 7-Point)

| Column name | Statement |
|---|---|
| Q19_1 | I found using the Hi-Audio platform to be enjoyable |
| Q19_2 | The actual process of using the Hi-Audio platform was pleasant |
| Q19_3 | I had fun using the Hi-Audio platform |

```python
q19_cols = ['Q19_1', 'Q19_2', 'Q19_3']
print(df[q19_cols].mean())
```

Compute mean, median, and range per item.

### Step 6 — Q20: Future Use Intent and Perceived Usefulness Matrix (4 Items, 7-Point)

| Column name | Statement |
|---|---|
| Q20_1 | Using the Hi-Audio platform for recording music would be a good idea |
| Q20_2 | I would find the Hi-Audio platform useful for recording music |
| Q20_3 | I would plan to use the Hi-Audio platform in my next music project |
| Q20_4 | I would recommend the Hi-Audio platform to music colleagues |

```python
q20_cols = ['Q20_1', 'Q20_2', 'Q20_3', 'Q20_4']
print(df[q20_cols].mean())
```

Compute mean, median, and range per item.

### Step 7 — Q21, Q22, Q23: Qualitative Thematic Coding

These are open-text responses. Do not run sentiment analysis or automated classifiers without explicit instruction. Analyse them through thematic coding using a hybrid deductive/inductive approach.

#### Deductive Coding Frames

The deductive frames come from the evaluation memo (`docs/output.md`, published as `docs/memo.html`). Use these as your starting categories:

**For Q22 — Challenges encountered:**
- Visual feedback (waveform display, level meters, VU meters)
- Transport controls (play, stop, record behaviour)
- Editing capabilities (trimming, naming, organising tracks)
- File format compatibility
- Latency and synchronisation
- Browser or network compatibility issues
- Workflow integration with external tools (DAWs, routing software)

**For Q21 — Most useful or effective aspects:**
- Browser-based accessibility (no download or installation required)
- Multi-track recording support
- Real-time or asynchronous collaboration features
- Ease of sharing recorded tracks
- Platform simplicity and low barrier to entry

**For Q23 — Use cases:**
Apply §7 (Assessment of Platform Fit for Professional Creative Workflows) as the primary frame, plus both frames above, and remain open to themes that do not fit any of them.

#### Inductive Coding

When a participant response raises a theme that does not fit the deductive frames, flag it explicitly as a new inductive theme. These are potentially new findings.

#### Output per Question

For each of Q21, Q22, Q23, produce:
1. A list of identified themes, each with a short description (1–2 sentences).
2. One or two representative pseudonymised excerpts per theme (attributed by participant ID only).
3. A note for each theme indicating whether it **confirms**, **nuances**, **contradicts**, or **extends** findings already present in the practice-based memo (`docs/output.md`).

### Step 8 — Triangulation With the Memo

Compare survey findings against the following sections of the memo (`docs/output.md`):

| Memo section | Survey questions to compare |
|---|---|
| §4 Platform Strengths | Q21 thematic results |
| §5 Workflow Challenges | Q22 thematic results |
| §6 Design Implications | Q22 and Q23 thematic results |
| §7 Assessment of Platform Fit | Q16, Q17, Q20 quantitative results |
| §8 Key Findings and Next Steps | Which §8 development priorities the survey does and does not independently corroborate |

Produce a triangulation table or short narrative identifying:
- **Confirmation** — survey finding agrees with the memo
- **Nuance** — survey finding qualifies or adds context to the memo
- **Contradiction** — survey finding conflicts with the memo
- **New finding** — survey finding raises something not addressed in the memo

### Step 9 — Deliverables

Produce a file named `docs/analysis_summary.md` containing:
- Sample description (from Q1–Q15)
- Quantitative summary tables (Q16–Q20)
- Thematic summaries (Q21–Q23)
- Triangulation section

Do not commit `docs/analysis_summary.md` until reviewed and approved. Keep it local until instructed.

---

## Privacy and Anonymity Constraints

- Never commit participant response data to the repo without explicit instruction.
- Before any commit of response-related files, verify that no **new** names, emails, phone numbers or IP addresses have entered them. This is not a blanket instruction to strip identifiers: the repository deliberately publishes the pseudonymous PIDs, submission dates and PDF ordinals in the response data, and the JotForm submission IDs in `docs/response_id_mapping.md`. Do not remove those, and do not treat their presence as a failed check. The one accepted name is P09's, in her own Q7 answer (Rule 4).
- Participant responses, when referenced in write-ups, are attributed by participant ID only — pseudonymised, never by name (e.g. "P03 noted that...").
- The Hi-AUDiO lead software engineer is named (José M. Gil Panal) only as co-author of the survey analysis and in README's Positionality section — owner decision, 2026-11-06. Do not add other personal identifiers.

---

## Reporting Conventions

- Use academic, professional tone throughout.
- Scope every claim: "among FLO participants in this study..." — never generalise to broader populations.
- Scale midpoint is 4.0. Contextualise means relative to this midpoint.
- When discussing Q18–Q20, cite Venkatesh (2000) for the Q18/Q19 item wording and note that the instrument *as assembled* was never re-validated (Rule 5) — do not present the items as original to this study.
- Distinguish clearly between what the data shows (descriptive) and what it might mean (interpretive). Keep these separate.
