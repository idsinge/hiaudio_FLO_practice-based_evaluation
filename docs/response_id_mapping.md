# Response ID Mapping

Maps the anonymised participant IDs used throughout the repository to the original JotForm submission identifiers, for cross-referencing `participant_survey_responses.csv`/`.xlsx` rows against the individual PDFs in `individual_participant_responses/`.

Derived from the unique submission date on each row/PDF (no two respondents submitted on the same day, so the join is unambiguous) and verified against matching free-text content (DAW list, instrument list) between the CSV rows and the corresponding PDFs.

| PID | Submission date | CSV row (0-indexed) | Original JotForm submission ID |
|---|---|---|---|
| P01 | 2026-05-20 | 8 | 6551092545111428004 |
| P02 | 2026-05-22 | 7 | 6552583811463246351 |
| P03 | 2026-05-24 | 6 | 6554391233514452682 |
| P04 | 2026-05-27 | 5 | 6557039847815884318 |
| P05 | 2026-05-29 | 4 | 6558610039983730983 |
| P06 | 2026-05-30 | 3 | 6559377660628523792 |
| P07 | 2026-05-31 | 2 | 6560534866918408872 |
| P08 | 2026-06-01 | 1 | 6561152523719202448 |
| P09 | 2026-07-03 | 0 | 6588874506099281851 |

**Note:** P09 is Nela Brown, who designed the questionnaire and authored the evaluation memo — see "Researcher Positionality" in `ANALYSIS_PLAN.md` (same directory) and the note in `../CONTEXT.md` §Key People.

**History note:** an earlier set of individual PDFs (same 9 submission IDs, different export/render) had stale question labels and was missing several *answered* questions entirely (Q9, Q12, Q16–Q20 absent even where the CSV shows a value). That set was replaced on 2026-07-03 with the current PDFs (4–5 pages each), correctly labeled "Q1."–"Q23." for every answered question, and verified consistent with the CSV. No PDF-label caveat applies to the current set. Note: the current PDFs (correctly) omit optional/conditional questions that were left blank — e.g. P05.pdf and P07.pdf show no Q21–Q23 section at all, and P08.pdf omits Q23, because those CSV cells are empty for those respondents. This is expected rendering behaviour, not a data gap — always check the CSV cell, not just PDF page count, to confirm whether a question was actually left unanswered.

**Q16/Q17 note:** the PDFs render Q16 and Q17 as a single unlabeled matrix row each (one selection) — this matches the live form. The original JotForm CSV export had incorrectly split these into 4 bogus sub-columns (never real form content); `participant_survey_responses.csv`/`.xlsx` have already been corrected to one clean column per question. See "Q16/Q17 data correction" in `../CONTEXT.md` and in `ANALYSIS_PLAN.md` for the full history.
