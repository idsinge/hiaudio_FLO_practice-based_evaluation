# AGENTS.md — Hi-AUDiO FLO Practice-Based Evaluation

Working instructions for AI coding agents (Codex and others). Read this file before making any changes. For full project background, read [CONTEXT.md](CONTEXT.md). For the statistical analysis plan, read [docs/ANALYSIS_PLAN.md](docs/ANALYSIS_PLAN.md).

---

## Project Summary

This repository publishes a practice-based evaluation of the Hi-Audio web audio platform (hiaudio.fr), conducted by the Female Laptop Orchestra (FLO) for Télécom Paris / Institut Mines-Télécom. The work is funded by the European Research Council under Horizon Europe (grant No. 101052978, project: "Hybrid and Interpretable Deep Neural Audio Machines"). The repository is public and served via GitHub Pages at https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/.

---

## File Inventory — What You Can and Cannot Touch

| File | Edit? | Commit? | Purpose |
|---|---|---|---|
| README.md | Yes | Yes | Main evaluation report — primary public document |
| CONTEXT.md | Yes | Yes | LLM/collaborator context — keep it current |
| docs/ANALYSIS_PLAN.md | Yes | Yes | Statistical analysis plan — data collection closed, cleared for publication |
| docs/participant_survey.md | Yes | Yes | Survey working copy — data collection closed, cleared for publication |
| docs/output.md | **Never** | Already published | Original Pandoc conversion — historical record only |
| docs/participant_survey_responses.csv / .xlsx | No | Yes | Raw response data, no PII columns — cleared for publication |
| docs/individual_participant_responses/P01–P09.pdf | No | Yes | Per-respondent submissions, anonymised as P01–P09 |
| docs/response_id_mapping.md | Yes | Yes | Maps PID ↔ original JotForm submission ID |
| docs/Practice-Based Evaluation...pdf | No | No | Original PDF memo |
| CITATION.cff | Yes | Yes | Structured citation for GitHub |
| _config.yml | Only if asked | Only if asked | Jekyll theme config |
| images/ | No | No | Static images — do not add, remove, rename |

`invitation_message.md` has been removed from the repository entirely — do not recreate it without instruction.

---

## Rules — Read These Before Doing Anything

### Rule 1: docs/output.md is read-only
`docs/output.md` is the original Pandoc conversion of the evaluation memo from .docx. It is kept for the historical record. Do not edit, overwrite, or delete its content. Ever. Exception already used once: when the file was relocated from repo root into `docs/`, its 8 relative image paths (`./images/imageN.png`) were updated to `../images/imageN.png` so they keep resolving from the new location — a path fix required by the move, not a content edit. Do not make further changes.

### Rule 2: docs/participant_survey.md, docs/ANALYSIS_PLAN.md, and the response data are cleared for publication
Data collection from participants is complete, so the risk that motivated withholding these files — contaminating participant responses before they replied — no longer applies. `invitation_message.md` was removed from the repo entirely (not published, not withheld pending approval — simply gone).

### Rule 3: Acknowledgements is always last in README.md
The Acknowledgements section must remain the final section of README.md, after any appendices. Do not move it.

### Rule 4: No personal identifiers in any file
Do not add email addresses, phone numbers, or full names to any file beyond what already exists. The institutional email is written as `[available on request]` in docs/participant_survey.md. Keep it that way. One accepted exception: P09's Q7 response names Nela Brown in a track filename — left as-is given her dual role as questionnaire designer/respondent (see Rule 8 below and CONTEXT.md).

### Rule 5: Use careful framework language for Q18–Q20
The survey items in Q18–Q20 were developed specifically for this study. They are informed by established usability and technology acceptance literature, but they are not reproductions of standardised instruments. When writing about these items, always say "informed by" or "adapts constructs from". Never describe them as directly applying named instruments such as USE Questionnaire, AttrakDiff, UEQ, or TAM.

### Rule 6: Small sample — descriptive statistics only
The expected participant count is approximately 9 FLO performers. This is a small expert sample. Do not apply inferential statistics (t-tests, ANOVA, regressions, confidence intervals) unless explicitly instructed. Report means, medians, and ranges. Frame all findings as exploratory and descriptive. Scope every claim to "FLO participants in this study" — never generalise.

### Rule 7: No remote pushes without instruction
Stage and commit locally only when asked. Never force-push.

### Rule 8: Respondent overlap — Nela Brown is P09
Nela Brown designed this questionnaire and authored the evaluation memo, and is also P09 in the response dataset. Before computing or reporting any aggregate statistic or thematic summary, read "Researcher Positionality" in `docs/ANALYSIS_PLAN.md` — it specifies reporting n=9 as primary but also computing n=8 (P09 excluded) for headline metrics, and flagging P09-sourced excerpts in thematic coding.

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
- Rename columns to Q1, Q2, ... Q23 for consistency. JotForm may export verbose column names — map them to Q-labels based on question order.
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
- **Q3, Q4, Q6, Q7** use configurable list or multiple-entry widgets. JotForm may export these as lists or repeated columns. Treat them descriptively — summarise common entries in prose rather than forcing frequency counts.

Produce a short narrative summary of the sample covering: musical roles, prior tool experience, recording methods, latency measurement behaviour, session structure, time spent, OS and browser, headphone type.

### Step 3 — Q16 and Q17: Suitability and Artistic-Intent Ratings

```python
for q in ['Q16', 'Q17']:
    print(df[q].describe())
```

- **Q16** (suitability for professional/artistic use) is the **headline metric**. Report it first and prominently.
- **Q17** (artistic intention support) is a supporting metric.
- Both are single 7-point questions on the live form — confirmed directly in the JotForm builder, which shows each has exactly one matrix row with a blank row-name field (JotForm's own "Type Row Name" placeholder, not a real label). An earlier JotForm export defect split them into 4 bogus sub-columns (suffixed `>> Service Quality`, `>> Cleanliness`, `>> Responsiveness`, `>> Friendliness` — never real form content); `docs/participant_survey_responses.csv`/`.xlsx` have already been corrected to one clean column per question, so no further preprocessing is needed here.
- **Respondent overlap:** Nela Brown (questionnaire designer, memo author, evaluator) is also P09 in the response dataset. Before computing or reporting any aggregate statistic or thematic summary, read the "Researcher Positionality" section in `docs/ANALYSIS_PLAN.md` — it specifies reporting n=9 as primary but also computing n=8 (P09 excluded) for headline metrics, and flagging P09-sourced excerpts in thematic coding.
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

The deductive frames come from the evaluation report (README.md). Use these as your starting categories:

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
Apply both frames above and remain open to themes that do not fit either.

#### Inductive Coding

When a participant response raises a theme that does not fit the deductive frames, flag it explicitly as a new inductive theme. These are potentially new findings.

#### Output per Question

For each of Q21, Q22, Q23, produce:
1. A list of identified themes, each with a short description (1–2 sentences).
2. One or two representative anonymised excerpts per theme.
3. A note for each theme indicating whether it **confirms**, **nuances**, **contradicts**, or **extends** findings already present in the practice-based memo (README.md).

### Step 8 — Triangulation With the Memo

Compare survey findings against the following sections of README.md:

| README section | Survey questions to compare |
|---|---|
| §4 Platform Strengths | Q21 thematic results |
| §5 Workflow Challenges | Q22 thematic results |
| §6 Design Implications | Q22 and Q23 thematic results |
| §7 Platform Fit and Future Use | Q16, Q17, Q20 quantitative results |

Produce a triangulation table or short narrative identifying:
- **Confirmation** — survey finding agrees with the memo
- **Nuance** — survey finding qualifies or adds context to the memo
- **Contradiction** — survey finding conflicts with the memo
- **New finding** — survey finding raises something not addressed in the memo

### Step 9 — Deliverables

Produce a file named `analysis_summary.md` containing:
- Sample description (from Q1–Q15)
- Quantitative summary tables (Q16–Q20)
- Thematic summaries (Q21–Q23)
- Triangulation section

Do not commit `analysis_summary.md` until reviewed and approved. Keep it local until instructed.

---

## Privacy and Anonymity Constraints

- Never commit participant response data to the repo without explicit instruction.
- Before any commit of response-related files, verify that all names, emails, and identifiers have been removed.
- Participant responses, when referenced in write-ups, must be anonymised (e.g. "Participant 3 noted that...").
- The Lead Software Engineer is referred to by role only in public documents — not by name.

---

## Reporting Conventions

- Use academic, professional tone throughout.
- Scope every claim: "among FLO participants in this study..." — never generalise to broader populations.
- Scale midpoint is 4.0. Contextualise means relative to this midpoint.
- When discussing Q18–Q20, note that the instrument was developed for this study and informed by established approaches — not a validated standardised scale.
- Distinguish clearly between what the data shows (descriptive) and what it might mean (interpretive). Keep these separate.
