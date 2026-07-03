# Project Context

This file provides context for LLMs or collaborators interacting with this repository. It summarises the project background, current state, key decisions, and working constraints.

---

## What This Repository Is

This repository publishes findings and methodology from a practice-based evaluation of the Hi-Audio web audio platform (hiaudio.fr), conducted by the Female Laptop Orchestra (FLO) between February and March 2026. The evaluation was carried out as part of the Hi-AUDiO research project, funded by the European Research Council (ERC) under Horizon Europe (grant No. 101052978).

The repository is public and hosted on GitHub Pages. It is intended to support open dissemination and reproducibility for other researchers.

**Repo:** https://github.com/idsinge/hiaudio_FLO_practice-based_evaluation
**GitHub Pages:** https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/

---

## Key People

- **Nela Brown** — FLO Lab director, lead evaluator, author of the evaluation memo, and designer of the participant questionnaire. She is also **P09** in the survey response dataset (submitted 2026-07-03) — she completed the questionnaire herself as one of the nine respondents. This dual role (instrument designer + respondent) is disclosed in README.md §3 and should be kept in mind when interpreting aggregate survey results; see docs/ANALYSIS_PLAN.md for how this is handled during analysis.
- **Lead Software Engineer** — Hi-Audio platform developer, involved in onboarding and technical support (name not disclosed in public documents)
- **FLO participants** — nine performers from the Female Laptop Orchestra, including Nela Brown (P09)

Do not add names, email addresses, or personal identifiers to any file in this repository beyond what is already present.

---

## Repository Files

| File | Status | Purpose |
|---|---|---|
| README.md | Published | Main evaluation report, converted and edited from original .docx memo |
| docs/Practice-Based Evaluation of the Hi-Audio platform by FLO Lab .pdf | Published | Original evaluation memo in PDF format |
| docs/output.md | Published | Original Pandoc conversion from .docx — kept as historical reference, do not edit or delete |
| docs/participant_survey.md | Published | Working copy of the JotForm survey — data collection is complete, cleared for publication |
| docs/ANALYSIS_PLAN.md | Published | Planned approach for processing and analysing survey responses — data collection is complete, cleared for publication |
| docs/participant_survey_responses.csv / .xlsx | Published | Raw aggregate response data (9 rows), no name/email/IP columns |
| docs/individual_participant_responses/P01–P09.pdf | Published | Per-respondent submission exports, anonymised as P01–P09 |
| docs/response_id_mapping.md | Published | Maps PID ↔ original JotForm submission ID/date |
| CONTEXT.md | This file | Context for LLMs and collaborators |
| CITATION.cff | Published | Structured citation for GitHub's "Cite this repository" button |
| LICENSE | Published | CC BY 4.0 |
| _config.yml | Published | Jekyll Cayman theme for GitHub Pages |
| images/ | Published | Screenshots (image1–8.png) and ERC_logo.png |

**Data collection status:** data collection closed. `docs/participant_survey.md`, `docs/ANALYSIS_PLAN.md`, and the response data were withheld from the public repo only to avoid contaminating participant responses before they replied; that risk no longer applies, and all are now published, moved into `docs/`. `invitation_message.md` was removed from the repo entirely (not published, not withheld — deleted).

A full PII scan was run across the response CSV (all 39 columns × 9 rows, before the Q16/Q17 column correction below reduced it to 33 columns) and all 9 individual PDFs before publication: no names, emails, phone numbers, or IP addresses were found, with one accepted exception — see "Nela Brown / P09" below.

---

## The Survey

The participant survey complements the practice-based evaluation memo. It was administered via JotForm:
https://form.jotform.com/hiaudioparis/flo-lab-evaluation (Form ID: 261313989509366)

The survey title is: **FLO Lab Hi-Audio Evaluation — Participant Survey**

The `.md` file is a working copy that mirrors the live JotForm. The `.md` version uses `[available on request]` in place of the institutional email address to avoid publishing contact details in the public repo.

### Survey Structure (JotForm Q1–Q23)

**Consent and Ethical Notice** — full GDPR-compliant text, required before proceeding to Section 1

**Section 1: User Profile & Background (Q1–Q6)**
- Q1: Musical activity (multiple choice, select all that apply)
- Q2: Prior browser-based tool experience (yes/no)
- Q3: Known similar platforms (multiple entry)
- Q4: DAWs and software used (multiple entry)
- Q5: External audio interface use (single choice)
- Q6: Instruments and proficiency level (configurable list)

**Section 2: Hi-Audio Recording Technical Setup (Q7–Q15)**
- Q7: Instruments/sounds recorded or uploaded for the Radiophrenia 2026 Jam session (configurable list)
- Q8: Recording/upload method — six options covering browser mic, audio interface, DAW routing, DAW upload, sound-recorder upload, or other (multiple choice)
- Q9: Latency measurement (frequency/applicability)
- Q10: If no, why not (conditional single choice — shown only if Q9 = No)
- Q11: Session structure — one or multiple sessions (single choice)
- Q12: Total time spent on Hi-Audio (single choice)
- Q13: Operating system (single choice)
- Q14: Web browser (single choice)
- Q15: Headphones — wired or wireless (single choice)

**Section 3: Exploring Usability and Usefulness (Q16–Q23)**
- Q16: Suitability for professional/artistic use — single-item 7-point rating, **intended headline metric**, usable
- Q17: Artistic intentions support — single-item 7-point rating, supporting metric
- Q18: First-use experience matrix (7-point, 4 items — pragmatic usability dimensions)
- Q19: Personal-experience matrix (7-point, 3 items — hedonic/experiential quality)
- Q20: Future-use matrix (7-point, 4 items — perceived usefulness and behavioural intention)
- Q21: Most useful or effective aspects (open text)
- Q22: Challenges encountered (open text)
- Q23: Relevant use cases (open text)

### Q16/Q17 data correction (already applied)

Q16 and Q17 are single questions on the live form — confirmed directly in the JotForm builder, where each has exactly one matrix row with a blank row-name field (shown as JotForm's own "Type Row Name" placeholder, not an actual label; text like "Service Quality"/"Cleanliness"/"Responsiveness"/"Friendliness" was never part of the form). The original JotForm CSV export nonetheless split each into 4 sub-columns suffixed with that bogus text — a JotForm export defect, not real data. All 4 sub-column values were identical for every one of the 9 respondents before correction, confirming nothing was lost by collapsing them. `docs/participant_survey_responses.csv`/`.xlsx` have already been corrected to a single clean column per question. See `docs/ANALYSIS_PLAN.md` for the full explanation.

### Widget Questions (not rendered in JotForm PDF export)
Q3, Q4, Q6, Q7 use configurable list or multiple entry widgets. They are present and active in JotForm but do not appear in the PDF export. They are confirmed present in the live form.

---

## Key Design Decisions

### Framework language
The survey items for Q18–Q20 were designed for this study, informed by established usability and technology acceptance evaluation approaches. They adapt common constructs (pragmatic usability, hedonic quality, perceived usefulness, behavioural intention) to the specific context of collaborative online audio recording.

Do not describe the survey as directly reproducing or formally applying named instruments such as USE Questionnaire, AttrakDiff, UEQ, or TAM. The correct framing is "informed by" or "adapts constructs from." This applies to all public-facing documents including README.md, docs/participant_survey.md, and CONTEXT.md.

### Scale
Q16–Q20 all use the same 7-point "Strongly disagree → Strongly agree" scale. Q16 and Q17 are single-item ratings; Q18, Q19, and Q20 are multi-item matrices.

### Headline metric
Q16 (overall suitability for professional/artistic use) is the primary headline metric, with Q17–Q20 as supporting evaluative items — usable as designed.

### Sections and ordering
The Acknowledgements section is always last in README.md — after appendices. Do not move it.

### docs/output.md
This file is the original Pandoc conversion from the .docx memo. It is kept as a historical reference. Do not edit, overwrite, or delete it.

---

## Analysis Approach

The analysis is exploratory and descriptive. Inferential statistics are not planned given the expected small sample size.

- **Q1–Q15:** frequency counts, percentages, narrative sample description
- **Q16–Q20:** means, medians, range
- **Q21–Q23:** thematic coding — hybrid deductive/inductive approach
  - Deductive frame: §4 (Platform Strengths) and §5 (Workflow Challenges) of README.md
  - Inductive: open to new themes not in the existing framework
- **Triangulation:** survey findings compared against the practice-based memo to identify confirmation, nuance, contradiction, and new issues

Q17 sits at the boundary — report its mean alongside Q16, Q18–Q20, but also read it qualitatively alongside Q21 and Q22 when interpreting artistic fit.

---

## Privacy and Anonymity Constraints

- Do not add email addresses, phone numbers, or personal identifiers to any file
- The institutional email is replaced with `[available on request]` in docs/participant_survey.md
- The response CSV, XLSX, and all 9 individual PDFs were scanned for PII before publication (see "Data collection status" above) — one accepted exception: Nela Brown's name appears in P09's Q7 answer (a track filename); left as-is given her dual role, see below
- The FLO Lead Software Engineer is referred to by role only in public documents

### Nela Brown / P09 — dual role disclosure
Nela Brown designed the questionnaire and authored the evaluation memo, and is also **P09** in the response dataset (submitted 2026-07-03). This is disclosed in README.md §3 (Methodological Approach) as a "Positionality note," and in `docs/ANALYSIS_PLAN.md` under "Researcher Positionality," which specifies how to handle her response during analysis (report n=9 as primary, additionally compute n=8 with P09 excluded for headline metrics, flag P09-sourced excerpts in thematic coding). Her name appearing in P09's Q7 free-text answer (a track filename referencing her) is treated as consistent with this disclosure, not as a separate PII leak — she is already the named public author of this report.

---

## What Comes Next

1. Process the response data (`docs/participant_survey_responses.csv`) per `docs/ANALYSIS_PLAN.md`, following the "Researcher Positionality" guidance for P09
2. Produce `analysis_summary.md` (not committed until reviewed and approved)
3. Findings are documented and added to the repository

---

## Current Session Status

This section captures the latest working state so the project can be resumed easily in a later session.

### Completed in the latest review cycle

- Data collection closed; `docs/participant_survey.md`, `docs/ANALYSIS_PLAN.md`, and `docs/output.md` moved from repo root into `docs/`; `invitation_message.md` removed from the repo entirely
- Compared `docs/participant_survey.md` against a JotForm export of the live form and corrected `docs/participant_survey.md`, `docs/ANALYSIS_PLAN.md`, `CONTEXT.md`, `AGENTS.md`, and `CLAUDE.md` to match the live form's actual Q1–Q23 structure (no Q24; Q16–Q20 matrices, Q21–Q23 open text)
- Received and incorporated the actual response data: `participant_survey_responses.csv`/`.xlsx` (9 rows, originally 39 columns before the Q16/Q17 correction below, now 33; no PII columns) and 9 individual PDFs
- Ran a full PII scan across the CSV and all 9 PDFs; found and disclosed one dual-role case: Nela Brown is P09. Documented as a "Positionality note" in README.md §3, a "Researcher Positionality" section in `docs/ANALYSIS_PLAN.md`, and here in CONTEXT.md
- Added a "Citation" section to README.md (before Acknowledgements) naming Nela Brown as author, consistent with CITATION.cff; later added José M. Gil Panal as co-author in both README.md and CITATION.cff
- **Replaced the individual PDF set.** The first batch (renamed P01–P09.pdf) turned out to be incomplete — missing Q9, Q12, and Q16–Q20 even where the CSV shows an answer, on all 9 files, with stale question labels elsewhere. A second batch from the same 9 submission IDs was dropped in, verified complete and correctly labeled ("Q1."–"Q23." for every answered question, 4–5 pages each) against the CSV, PII-scanned (same single accepted exception, Nela Brown/P09), and used to replace the first batch. Mapping in `docs/response_id_mapping.md` updated accordingly (submission IDs unchanged, so the PID mapping itself didn't need to change). Note: the current PDFs correctly omit blank optional/conditional questions (e.g. Q21–Q23 don't appear at all for P05/P07, which left them unanswered) — this is expected, not a defect.
- **Resolved and corrected the Q16/Q17 data quality issue** (previously believed to make them unusable). The CSV's 4 sub-columns per question always held identical values for every respondent, the corrected PDFs render a single row per question, and the user confirmed directly in the JotForm builder that Q16/Q17 each have exactly one matrix row with a blank row-name field — the "Service Quality"/"Cleanliness"/"Responsiveness"/"Friendliness" sub-column text was never part of the actual form, confirmed by the user to be a JotForm export defect. `docs/participant_survey_responses.csv`/`.xlsx` were corrected in place: each of Q16/Q17 collapsed from 4 sub-columns to 1 clean column. Q16 resumes its intended role as the headline suitability metric, Q17 as the supporting artistic-intention metric — both usable with no further preprocessing.

### Decisions made

- Data collection is fully closed — all survey/analysis docs and response data are cleared for publication, committed under `docs/`
- Commit the response data (CSV, XLSX, individual PDFs) as-is rather than keeping it local-only, since it contains no PII beyond the one disclosed/accepted case
- Nela Brown's name appearing in P09's Q7 answer is left unredacted — treated as consistent with her disclosed dual role, not a privacy leak
- Q16/Q17 are usable single-item metrics; the response CSV/XLSX were corrected in place (4 bogus sub-columns collapsed to 1 clean column each) rather than documenting a workaround — not reported as a disqualifying limitation
- For any aggregate statistic, report n=9 as primary and additionally compute n=8 (P09 excluded) for headline metrics — see `docs/ANALYSIS_PLAN.md`

### Recommended next actions for the next session

1. Process the response CSV per `docs/ANALYSIS_PLAN.md`, applying the Researcher Positionality guidance
2. Produce `analysis_summary.md` (descriptive stats, thematic coding, triangulation) — keep local until reviewed and approved
