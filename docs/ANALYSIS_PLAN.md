# Analysis Plan

## Purpose

This document outlines the planned approach for processing and analysing responses to the Hi-AUDiO participant survey. The survey is designed as a companion instrument to the practice-based evaluation report and is intended to complement, refine, and contextualise the findings already presented in the repository.

The analysis is exploratory and descriptive in nature. It is not intended to validate a standardised instrument or support broad generalisation beyond the present study context.

## Study Context

- Population: FLO participants involved in the Hi-AUDiO evaluation activity
- Likely sample: small, expert, practice-based cohort
- Study role of survey: companion instrument to the evaluation memo/report
- Main analytic strategy: descriptive summary of closed questions plus thematic coding of open-text responses

## Researcher Positionality — Respondent Overlap

Nela Brown, who designed this questionnaire and authored the practice-based evaluation memo (README.md) against which survey findings are triangulated, is also a respondent in the dataset: she is **P09** (submitted 2026-07-03). This is disclosed for transparency and is not treated as disqualifying — practice-based research expects the lead researcher to be embedded in the activity under study — but it has concrete implications for this analysis:

- **Do not silently exclude P09.** Report the full n=9 sample as the primary result.
- For headline quantitative metrics (Q16–Q20), additionally compute the same means/medians with P09 excluded (n=8) and note whether her response is an outlier that shifts the result. Report both if they diverge meaningfully.
- For thematic coding of Q21–Q23, flag which excerpts originate from P09 when citing them, so a reader can judge whether a theme is corroborated by independent respondents or partly reflects the instrument designer's own view.
- When triangulating survey findings against the memo (§4–§7), be aware that P09's survey response and the memo's authorial voice are not independent sources — agreement between them is expected and should not be over-read as independent corroboration.

## Analysis Goals

The survey analysis will be used to:

- document participant background and technical setup
- characterise first-use usability and experiential impressions
- assess perceived artistic/professional fit and future use intention
- identify recurring strengths, challenges, and suggested use cases
- compare participant survey feedback with the themes identified in the practice-based memo

## Quantitative Analysis

Closed questions will be analysed descriptively.

### Background and Context

These items provide sample/context description rather than evaluative outcomes:

- Q1-Q6: participant background, prior experience, DAW literacy, interface use, instruments
- Q7-Q15: contribution type, recording method, latency measurement, session structure, duration, OS/browser, headphones

Planned outputs:

- frequency counts
- simple percentages
- short narrative summary of sample/context

### Core Evaluative Items

These items provide the main evaluative indicators:

- Q16: overall suitability / platform fit — **headline metric**
- Q17: artistic intention support — supporting metric
- Q18: first-use usability dimensions
- Q19: hedonic / experiential quality
- Q20: future use intention and perceived usefulness

Planned outputs:

- item-level means
- medians where useful
- minimum/maximum or range where informative
- response distributions when useful for interpretation

Note: the published CSV/XLSX store these items as text ("Strongly disagree" ... "Strongly agree"), not numbers — recode to 1–7 in a local working copy before computing means (see AGENTS.md Step 1b for the exact mapping). The published files intentionally keep the text labels for legibility; the recoded numeric copy is not committed.

Because the sample is expected to be small, interpretation will remain descriptive and cautious. Inferential statistics are not planned unless a later sample size clearly justifies them.

**Q16/Q17 data correction (already applied to the hosted CSV/XLSX).** The raw JotForm export originally split Q16 and Q17 into 4 sub-columns each, suffixed `>> Service Quality`, `>> Cleanliness`, `>> Responsiveness`, `>> Friendliness`. This text was never part of the actual form — confirmed directly in the live JotForm builder, which shows Q16 and Q17 each have exactly one matrix row with a blank row-name field (JotForm's own "Type Row Name" placeholder hint, not real content). The 4-way split was a JotForm export defect. Before correction, all 4 sub-column values were identical for every one of the 9 respondents (e.g. P01: Q16 = "Strongly disagree" ×4), confirming no information was lost by collapsing them.

`docs/participant_survey_responses.csv` and `.xlsx` have already been corrected: each of Q16/Q17 is now a single column with the plain question title as its header, holding the one real value per respondent. No preprocessing is needed — treat Q16/Q17 exactly like any other single 7-point rating column (e.g. alongside Q18–Q20). Q16 is the headline suitability metric, Q17 the supporting artistic-intention metric.

## Qualitative Analysis

Open-text responses will be analysed through thematic coding.

### Open Questions

- Q21: most useful or effective aspects
- Q22: challenges encountered
- Q23: relevant use cases / applicability

Note: Q17 sits at the boundary between quantitative and qualitative analysis. Its mean should be reported alongside Q16 and Q18–Q20, and responses should also be read in conjunction with Q21 and Q22 when interpreting artistic fit findings.

### Coding Approach

Coding will begin with a hybrid approach:

- deductive coding using themes already present in the report
- inductive coding for new themes not captured by the existing framework

Initial deductive frames:

- report strengths in `README.md` section 4
- workflow challenges in `README.md` section 5
- design implications in `README.md` section 6

Planned outputs:

- recurring themes with short descriptions
- example excerpts where appropriate
- note of confirmatory themes, new themes, and contradictory themes

## Triangulation With the Memo

The survey findings will be compared against the practice-based evaluation memo in order to identify:

- confirmation of memo findings
- nuance or qualification of memo findings
- contradictions or areas of disagreement
- new issues or opportunities not captured in the memo

This triangulation is central to the study. The survey is not a separate standalone evaluation, but a secondary layer of evidence that helps interpret the memo findings.

## Reporting Principles

When writing up results:

- keep claims appropriately scoped to a small expert sample
- avoid presenting adapted questionnaire items as validated scales
- distinguish clearly between descriptive findings and interpretation
- state when findings reflect expert-practitioner context rather than general end-user behaviour

## Survey Item Mapping

The table below maps each survey item to the corresponding section of the evaluation report and the type of metric it produces.

| Survey item(s) | Report section | Metric |
|---|---|---|
| Q1 | §2.1 User Profile | Primary musical role — characterises evaluator perspective |
| Q2 | §2.1 User Profile | Prior browser-based tool experience — contextualises adoption findings |
| Q3 | §7 Platform Fit | Competitive awareness — qualitative context |
| Q4 | §2.1 User Profile | DAW/software literacy — contextualises technical findings |
| Q5 | §2.2 Use Case | Audio interface usage — contextualises recording quality findings |
| Q6 | §2.1 User Profile | Instruments and proficiency level — characterises performer expertise |
| Q7 | §3 Methodology | Track/instrument contribution — connects survey to broadcast deliverable |
| Q8 | §3 Methodology | Recording/upload method distribution — frequency counts |
| Q9, Q10 | §3 Methodology | Latency measurement frequency/applicability and reasons for skipping |
| Q11, Q12 | §3 Methodology | Session structure and duration distribution |
| Q13, Q14 | §2.2 Use Case | OS and browser distribution — frequency counts |
| Q15 | §2.2 Use Case | Headphone type breakdown |
| Q16 | §7 Platform Fit | Overall professional/artistic suitability — headline metric; mean |
| Q17 | §7 Artistic Fit | Artistic intention support — mean |
| Q18 | §4.2 Ease of Use | First-use usability dimensions (clarity, effort, ease, control) — mean per item |
| Q19 | §7 Artistic Fit | Hedonic/experiential quality (enjoyment, pleasantness, fun) — mean per item |
| Q20 | §7 Platform Fit | Future use intent and perceived usefulness — mean per item |
| Q21 | §4 Platform Strengths / §7 Platform Fit | Participant-reported strengths — thematic coding; complements Q22 challenge taxonomy |
| Q22 | §5, §6 Design Implications | Challenges — thematic coding against report challenge taxonomy |
| Q23 | §7 Platform Fit | Applicability scenarios — thematic coding |

**Matrix scales Q18–Q20:** This questionnaire was developed for the present study and informed by established technology acceptance and usability evaluation approaches. Q18 adapts pragmatic usability dimensions (clarity, mental effort, ease, controllability) commonly used in usability questionnaires. Q19 captures hedonic/experiential quality (enjoyment, pleasantness, fun) using common UX evaluation dimensions. Q20 adapts perceived usefulness and behavioural intention constructs commonly associated with technology acceptance literature.

**Open-text questions (Q21–Q23)** are suited for thematic coding. Q22 (challenges) and Q21 (strengths) form a complementary pair — the challenge areas identified in §5 of the evaluation report (visual feedback, transport controls, editing, file format, etc.) can serve as the coding frame for Q22, while §4 (Platform Strengths) provides the frame for Q21.

---

## Planned Deliverables

- a numeric-recoded working copy of the response data for computing statistics (see Step 1b in AGENTS.md) — local only, not committed; the published `docs/participant_survey_responses.csv`/`.xlsx` already serve as the canonical hosted dataset and are not replaced by it
- descriptive summary of closed questions
- thematic summary of open questions
- integrated interpretation aligned with the report
- follow-up documentation or appendix for the repository
