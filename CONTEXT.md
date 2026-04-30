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

- **Nela Brown** — FLO Lab director, lead evaluator, author of the evaluation memo
- **Lead Software Engineer** — Hi-Audio platform developer, involved in onboarding and technical support (name not disclosed in public documents)
- **FLO participants** — nine performers from the Female Laptop Orchestra

Do not add names, email addresses, or personal identifiers to any file in this repository beyond what is already present.

---

## Repository Files

| File | Status | Purpose |
|---|---|---|
| README.md | Published | Main evaluation report, converted and edited from original .docx memo |
| docs/Practice-Based Evaluation of the Hi-Audio platform by FLO Lab .pdf | Published | Original evaluation memo in PDF format |
| output.md | Published | Original Pandoc conversion from .docx — kept as historical reference, do not edit or delete |
| participant_survey.md | NOT YET COMMITTED | Working copy of the JotForm survey — commit only after data collection is complete |
| ANALYSIS_PLAN.md | NOT YET COMMITTED | Planned approach for processing and analysing survey responses |
| invitation_message.md | NOT YET COMMITTED | Draft invitation message to be sent to FLO participants |
| CONTEXT.md | This file | Context for LLMs and collaborators |
| CITATION.cff | Published | Structured citation for GitHub's "Cite this repository" button |
| LICENSE | Published | CC BY 4.0 |
| _config.yml | Published | Jekyll Cayman theme for GitHub Pages |
| images/ | Published | Screenshots (image1–8.png) and ERC_logo.png |

**Important:** `participant_survey.md` must not be committed to the repo until data collection is complete. `ANALYSIS_PLAN.md` documents the coding frame and analytical mapping — publishing either file before participants respond could contaminate their answers.

---

## The Survey

The participant survey complements the practice-based evaluation memo. It will be administered via JotForm:
https://eu.jotform.com/form/260613043838354

The survey title is: **FLO Lab Hi-Audio Evaluation — Participant Survey**

The `.md` file is a working copy that mirrors the live JotForm. Any changes agreed in review must be applied to both. The `.md` version uses `[available on request]` in place of the institutional email address to avoid publishing contact details in the public repo.

### Survey Structure (JotForm Q1–Q24)

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
- Q8: Recording/upload method — direct recording, routed recording, upload-only, or other (single choice)
- Q9: Latency measurement (frequency/applicability)
- Q10: If no, why not (conditional single choice — shown only if Q9 = No)
- Q11: Session structure — one or multiple sessions (single choice)
- Q12: Total time spent on Hi-Audio (single choice)
- Q13: Operating system (single choice)
- Q14: Web browser (single choice)
- Q15: Headphones — wired or wireless (single choice)

**Section 3: Exploring Usability and Usefulness (Q16–Q24)**
- Q16: Suitability for professional/artistic use — **headline metric** (7-point rating)
- Q17: Artistic intentions support (7-point rating)
- Q18: Challenges encountered (open text)
- Q19: Relevant use cases (open text)
- Q20: Most useful or effective aspects (open text — complements Q18)
- Q21: First-time experience matrix (7-point, 4 items — pragmatic usability dimensions)
- Q22: Recording experience matrix (7-point, 3 items — hedonic/experiential quality)
- Q23: Future use matrix (7-point, 4 items — perceived usefulness and behavioural intention)
- Q24: Additional comments (open text)

### Widget Questions (not rendered in JotForm PDF export)
Q3, Q4, Q6, Q7 use configurable list or multiple entry widgets. They are present and active in JotForm but do not appear in the PDF export. They are confirmed present in the live form.

---

## Key Design Decisions

### Framework language
The survey items for Q21–Q23 were designed for this study, informed by established usability and technology acceptance evaluation approaches. They adapt common constructs (pragmatic usability, hedonic quality, perceived usefulness, behavioural intention) to the specific context of collaborative online audio recording.

Do not describe the survey as directly reproducing or formally applying named instruments such as USE Questionnaire, AttrakDiff, UEQ, or TAM. The correct framing is "informed by" or "adapts constructs from." This applies to all public-facing documents including README.md, participant_survey.md, and CONTEXT.md.

### Scale
All rating items (Q16, Q17) and matrix items (Q21–Q23) use a 7-point scale. Q16 uses "Not suitable at all → Highly suitable." Q17 and Q21–Q23 use "Strongly disagree → Strongly agree."

### Headline metric
Q16 (overall suitability for professional/artistic use) is the primary headline metric. Q17, Q21, Q22, Q23 are supporting evaluative items.

### Sections and ordering
The Acknowledgements section is always last in README.md — after appendices. Do not move it.

### output.md
This file is the original Pandoc conversion from the .docx memo. It is kept as a historical reference. Do not edit, overwrite, or delete it.

---

## Analysis Approach

The analysis is exploratory and descriptive. Inferential statistics are not planned given the expected small sample size.

- **Q1–Q15:** frequency counts, percentages, narrative sample description
- **Q16, Q17, Q21–Q23:** item-level means, medians, range
- **Q18–Q20, Q24:** thematic coding — hybrid deductive/inductive approach
  - Deductive frame: §4 (Platform Strengths) and §5 (Workflow Challenges) of README.md
  - Inductive: open to new themes not in the existing framework
- **Triangulation:** survey findings compared against the practice-based memo to identify confirmation, nuance, contradiction, and new issues

Q17 sits at the boundary — report its mean alongside Q21–Q23, but also read it qualitatively alongside Q18 and Q20 when interpreting artistic fit.

---

## Privacy and Anonymity Constraints

- Do not add email addresses, phone numbers, or personal identifiers to any file
- The institutional email is replaced with `[available on request]` in participant_survey.md
- Participant responses, when collected, should not be committed to the public repo without anonymisation
- The FLO Lead Software Engineer is referred to by role only in public documents

---

## What Comes Next

1. FLO director reviews and approves the survey
2. Invitation message is sent to FLO participants with the JotForm link and a deadline
3. Responses are collected
4. participant_survey.md, ANALYSIS_PLAN.md, invitation_message.md, and CONTEXT.md are updated accordingly and committed to the repo
5. Data is processed and analysed per ANALYSIS_PLAN.md
6. Findings are documented and added to the repository

---

## Current Session Status

This section captures the latest working state so the project can be resumed easily in a later session.

### Completed in the latest review cycle

- Reviewed the updated survey structure and confirmed that it works well as a companion instrument to the practice-based memo
- Added Q20 as a strengths-focused open question, improving balance with Q18 on challenges
- Clarified the methodological framing in `participant_survey.md` and `README.md` so the questionnaire is described as developed for this study and informed by established approaches, rather than presented as a direct reuse of standardised instruments
- Added `ANALYSIS_PLAN.md` to document the intended descriptive and thematic analysis approach
- Added `invitation_message.md` as a draft participant invitation

### Decisions made

- Skip further work for now on the anonymity/copy-of-answers issue (Q25)
- Skip further work for now on publishing a direct contact email in the public repo
- Keep the survey framed as a study-specific instrument informed by prior usability and technology acceptance work
- Treat Q16 as the headline evaluative metric, with Q17 and Q21-Q23 as supporting items

### Recommended next actions for the next session

1. Do one final freeze pass on `participant_survey.md`
2. Add a visible version/date line to the survey file
3. Refine `invitation_message.md` with the real deadline, sender name, and preferred tone
4. Decide how raw and processed response data will be organised locally once collection starts
5. After survey launch, keep the analysis aligned with `ANALYSIS_PLAN.md` and avoid expanding claims beyond the small expert sample
