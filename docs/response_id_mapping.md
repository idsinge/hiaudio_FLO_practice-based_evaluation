# Response ID Mapping

Maps the pseudonymous participant IDs used throughout the repository to the original JotForm submission identifiers, for cross-referencing `participant_survey_responses.csv`/`.xlsx` rows against the individual PDFs in `individual_participant_responses/`.

Originally derived from the unique submission date on each row/PDF (no two respondents submitted on the same day, so the join is unambiguous) and verified against matching free-text content (DAW list, instrument list) between the CSV rows and the corresponding PDFs.

**Confirmed against source data on 2026-08-20** using a JotForm export carrying the platform's own `Submission ID` column: all nine IDs match the rows below exactly, so this mapping is not merely an inference from submission dates. That export is not retained in this repository, so a reader cannot reproduce that particular check — but the mapping stays independently checkable from published material, through the unique submission dates and the `Submission N` ordinal printed in each PDF.

| PID | Submission date | CSV/XLSX data row (0-indexed, header excluded) | PDF `Submission N` header | Original JotForm submission ID |
|---|---|---|---|---|
| P01 | 2026-05-20 | 8 | Submission 1 | 6551092545111428004 |
| P02 | 2026-05-22 | 7 | Submission 2 | 6552583811463246351 |
| P03 | 2026-05-24 | 6 | Submission 3 | 6554391233514452682 |
| P04 | 2026-05-27 | 5 | Submission 4 | 6557039847815884318 |
| P05 | 2026-05-29 | 4 | Submission 5 | 6558610039983730983 |
| P06 | 2026-05-30 | 3 | Submission 6 | 6559377660628523792 |
| P07 | 2026-05-31 | 2 | Submission 7 | 6560534866918408872 |
| P08 | 2026-06-01 | 1 | Submission 8 | 6561152523719202448 |
| P09 | 2026-07-03 | 0 | Submission 9 | 6588874506099281851 |

## Identifier scheme — how to reference a participant

**`PID` (P01–P09) is the canonical identifier.** Use it in all analysis, prose, and published discussion. Every other identifier joins back to it through this table.

Where each identifier lives:

| Artifact | Identifier it carries | Contains the JotForm submission ID? |
|---|---|---|
| `participant_survey_responses.csv` / `.xlsx` | `Submission Date` only (column 0 of 33) | **No** |
| `individual_participant_responses/P0N.pdf` | The PID in the filename; a `Submission N` ordinal inside the document | **No** |
| This file | PID ↔ date ↔ row ↔ ordinal ↔ submission ID | **Yes — the only place in the repository** |

The published CSV/XLSX deliberately carry no submission-ID column: platform identifiers are kept out of the response data for privacy, and the published files are citable artifacts whose schema should stay stable. This file is the intended bridge instead.

**Always map columns by header text, never by position.** The analysis workflow in `AGENTS.md` maps the 7-point items by column name, and any further analysis should do the same — a raw JotForm export and the published CSV do not share a column count or ordering, so positional addressing silently produces wrong results.

### ⚠️ The two orderings run in opposite directions

- **CSV/XLSX rows are reverse-chronological** — row 0 is the *newest* submission (P09), row 8 the oldest (P01).
- **The PDF `Submission N` ordinal is chronological** — Submission 1 is the *oldest* (P01), Submission 9 the newest (P09).

So `PID number = 9 − csv_row_index`, but `PID number = PDF ordinal` directly.

Matching by row position without consulting this table produces an exact mirror image of the correct mapping — a clean, plausible-looking 1-to-1 that is wrong for every respondent except P05. **Always join through this table, never by position.**

### Note on verifying against the PDFs

The PDFs contain real extractable text for questions, option labels, and free-text answers. The Likert *selections* in Q16–Q20 are rendered as radio-button graphics, not text — so text extraction shows all seven option labels but never which one was chosen. Confirming a Likert value from a PDF requires rendering the page as an image and reading it visually.

**Note:** P09 is Nela Brown, who co-designed the questionnaire and authored the evaluation memo — see "Researcher Positionality" in `ANALYSIS_PLAN.md` (same directory) and the note in `../CONTEXT.md` §Key People.

**History note:** an earlier set of individual PDFs (same 9 submission IDs, different export/render) had stale question labels and was missing several *answered* questions entirely (Q9, Q12, Q16–Q20 absent even where the CSV shows a value). That set was replaced on 2026-07-03 with the current PDFs (4–5 pages each), correctly labeled "Q1."–"Q23." for every answered question, and verified consistent with the CSV. No PDF-label caveat applies to the current set. Note: the current PDFs (correctly) omit optional/conditional questions that were left blank — e.g. P05.pdf and P07.pdf show no Q21–Q23 section at all, and P08.pdf omits Q23, because those CSV cells are empty for those respondents. This is expected rendering behaviour, not a data gap — always check the CSV cell, not just PDF page count, to confirm whether a question was actually left unanswered.

**Q16/Q17 note:** the PDFs render Q16 and Q17 as a single unlabeled matrix row each (one selection) — this matches the live form. The original JotForm CSV export had incorrectly split these into 4 bogus sub-columns (never real form content); `participant_survey_responses.csv`/`.xlsx` have already been corrected to one clean column per question. See "Q16/Q17 data correction" in `../CONTEXT.md` and in `ANALYSIS_PLAN.md` for the full history.
