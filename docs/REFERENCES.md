# References

Sources referenced by this repository. The list is deliberately minimal: every entry
supports a claim, method, or design decision that is actually stated somewhere in
[`README.md`](../README.md), [`ANALYSIS_PLAN.md`](ANALYSIS_PLAN.md),
[`analysis_summary.md`](analysis_summary.md), or the participant questionnaire. It is not
a literature review of the field.

All citations follow APA 7th style, matching the companion repository
[`hiaudio_user_evaluation_results`](https://github.com/idsinge/hiaudio_user_evaluation_results).

---

## 1. The platform under evaluation

- Gil Panal, J. M., David, A., & Richard, G. (2026). The Hi-Audio online platform for recording and distributing multi-track music datasets. *Journal on Audio, Speech, and Music Processing, 2026*(26). https://doi.org/10.1186/s13636-026-00459-0
  - Preprint: https://hal.science/hal-05153739
  - The primary description of the platform evaluated in this report: its browser-based architecture, multi-track recording and sharing model, automatic analysis features, and built-in latency-estimation method (the method referred to in **Q9** of the participant questionnaire). Also reports the 22-participant task-based usability study that this practice-based evaluation complements.

- Gil Panal, J. M., David, A., & Richard, G. (2026). *Hi-Audio user evaluation results* [Data repository]. GitHub. https://github.com/idsinge/hiaudio_user_evaluation_results
  - The companion task-based study referenced in the Summary of `README.md`, using SUS and NASA-TLX. Read alongside this repository, it provides the controlled-task counterpart to the practice-based evaluation reported here.

---

## 2. Constructs informing the participant questionnaire (Q16–Q20)

> **Important framing note — corrected 2026-08-20.**
>
> An earlier version of this repository described the questionnaire as adapting *constructs*
> without reproducing any published instrument. **That was inaccurate**, and item-level
> comparison against the primary sources shows why:
>
> | Survey block | Relationship to source |
> |---|---|
> | **Q18** (4 items) | The four-item **Perceived Ease of Use** scale as worded in Venkatesh (2000, Appendix 1), reproduced with the verb tense changed present→past and the platform named in place of "the system" |
> | **Q19** (3 items) | The three-item **Perceived Enjoyment** scale from the same appendix, same treatment |
> | **Q20_2** | Davis's (1989) perceived-usefulness item, with the domain changed from "in my job" to "for recording music" |
> | **Q20_1, Q20_3** | Attitude and behavioural-intention items in the TAM tradition. **Direct wording source not established** — in particular *not* attributable to Davis (1989), which developed the usefulness and ease-of-use scales only |
> | **Q20_4** | A recommendation item, not part of any of these scales |
> | **Q16, Q17** | Single items written for this study |
>
> So the correct statement is **not** "no items are reproduced." It is that the items *are*
> largely drawn from published scales, but the **instrument as assembled** is not a
> standardised questionnaire and was **not re-validated** for this population or this
> retrospective framing.
>
> What follows from that, and still holds:
> - Q16–Q20 results are descriptive and must **not** be compared against published norms for
>   any source scale.
> - They must not be treated as validated subscale scores: items were recombined across
>   sources, their verb tense was changed from present to past, the framing moved from a
>   system in current use to one recalled months later, and n = 9 is far too small to
>   establish reliability.
> - Practically: **neither SUS nor NASA-TLX was administered in this study, and no items from
>   either are reproduced** — that claim remains true and is separate from the TAM-derived
>   items above. Their reuse terms differ and should not be described together: NASA states
>   that TLX is open source and that no permission is needed to use or modify it, whereas
>   SUS reuse conventionally carries an attribution expectation.

- Venkatesh, V. (2000). Determinants of perceived ease of use: Integrating control, intrinsic motivation, and emotion into the technology acceptance model. *Information Systems Research, 11*(4), 342–365. https://doi.org/10.1287/isre.11.4.342.11872
  - **The earliest published source whose item wording matches Q18 and Q19.** Note what this does and does not establish: the match is textual. It shows the lineage of the wording, not which document the questionnaire's co-designers actually had in front of them — neither co-designer recalls, so the repository claims textual correspondence only. Appendix 1 gives Perceived Ease of Use as four items — "My interaction with the system is clear and understandable," "Interacting with the system does not require a lot of my mental effort," "I find the system to be easy to use," "I find it easy to get the system to do what I want it to do" — which is Q18 with the tense shifted and the platform named. The same appendix gives Perceived Enjoyment as "I find using the system to be enjoyable," "The actual process of using the system is pleasant," "I have fun using the system," which is Q19 under the same treatment. The paper's Measurement section states its TAM scales were "adapted from Davis (1989) and Davis et al. (1989)," and its enjoyment scale "adapted from Davis et al. (1992)" — so Venkatesh (2000) is the immediate source of the wording, and Davis is the upstream origin of the constructs. **Cite this paper for the items; cite Davis for the constructs.**

- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340. https://doi.org/10.2307/249008
  - Origin of the *perceived usefulness* and *perceived ease of use* constructs and scales, and the upstream source Venkatesh (2000) adapts. Directly relevant to **Q20**: Davis's six-item usefulness scale ends with "I would find [this product] useful in my job," which is **Q20_2** with the domain changed to "for recording music." Note the limit of this attribution: Davis (1989) developed the usefulness and ease-of-use scales only — not attitude or behavioural-intention scales — so it is **not** the source of Q20_1 or Q20_3, whose direct wording source remains unestablished.

- Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1992). Extrinsic and intrinsic motivation to use computers in the workplace. *Journal of Applied Social Psychology, 22*(14), 1111–1132. https://doi.org/10.1111/j.1559-1816.1992.tb00945.x
  - The upstream origin of the perceived-enjoyment items that Venkatesh (2000) adapts into the wording used in **Q19**. Cited for completeness of the attribution chain. Note: the item text of this paper could not be read directly (no open-access copy is indexed); the attribution above rests on Venkatesh's own statement of adaptation, not on inspection of the 1992 items.

- Hassenzahl, M. (2004). The interplay of beauty, goodness, and usability in interactive products. *Human–Computer Interaction, 19*(4), 319–349. https://doi.org/10.1207/s15327051hci1904_2
  - The pragmatic-quality / hedonic-quality distinction that justifies reporting **Q18** (clarity, mental effort, ease, controllability) separately from **Q19** (enjoyment, pleasantness, fun) rather than pooling them. Cited for the *reporting structure*, not as a source of item wording — the items come from Venkatesh (2000).

- Lund, A. M. (2001). Measuring usability with the USE questionnaire. *Usability Interface, 8*(2), 3–6.
  - Cited only as a parallel example of a usefulness / ease-of-use / satisfaction item set in practitioner use. **USE was not administered in this study and was not a source of any item in this questionnaire.** Whether USE was consulted is not something this repository can establish either way — neither co-designer recalls — so the statement above is about sourcing as far as it can be reconstructed, not a documented negative. There is in any case real wording overlap: USE contains "It is easy to use", "I would recommend it to a friend", "It is fun to use" and "It is pleasant to use", which are close to Q18_3, Q20_4, Q19_3 and Q19_2 — so no categorical "no USE item appears" claim should be made. Lund does not state a derivation from TAM, so that resemblance is best described as a shared construct vocabulary rather than a common ancestry. Published in a professional-society newsletter, not a peer-reviewed venue; the original STC URL is no longer live and no DOI exists.

- Brooke, J. (1996). SUS: A "quick and dirty" usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Eds.), *Usability evaluation in industry* (pp. 189–194). Taylor & Francis. https://doi.org/10.1201/9781498710411-35
  - Cited because SUS is named in the Summary of `README.md` as an instrument used in the **companion** 22-participant study. **SUS was not administered in this evaluation.** Two citation details: the DOI given is the *chapter* DOI (`…-35`), not the whole-book DOI, which an earlier version used; and the pages are the widely cited 189–194 from the 1996 printing, whereas Taylor & Francis' current record for the chapter gives 207–212. Both ranges refer to the same chapter.

- Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. In P. A. Hancock & N. Meshkati (Eds.), *Human mental workload* (pp. 139–183). North-Holland. https://doi.org/10.1016/S0166-4115(08)62386-9
  - Cited for the same reason as Brooke (1996): named in the Summary as part of the companion study. **NASA-TLX was not administered in this evaluation.** Note that **Q18_2** ("did not require a lot of mental effort") concerns perceived effort but is *not* a NASA-TLX workload measure and is not scored as one.

---

## 3. Rating-scale design

- Rohrmann, B. (2007). *Verbal qualifiers for rating scales: Sociolinguistic considerations and psychometric data* (Project report). University of Melbourne. https://www.rohrmannresearch.net/pdfs/rohrmann-vqs-report.pdf
  - Empirically calibrated scale values for English verbal qualifiers. Supports the use of a fully labelled verbal scale ("Strongly disagree" … "Strongly agree") with approximately equidistant anchors, rather than labelling only the endpoints. Relevant to the decision, stated in `AGENTS.md`, to recode the labels to 1–7 and treat the midpoint as 4.0. Self-published project report; no DOI.

- Preston, C. C., & Colman, A. M. (2000). Optimal number of response categories in rating scales: Reliability, validity, discriminating power, and respondent preferences. *Acta Psychologica, 104*(1), 1–15. https://doi.org/10.1016/S0001-6918(99)00050-5
  - Supports the choice of a 7-point rather than a shorter scale: reliability and validity are poorest with 2–4 categories and plateau from roughly 7 points upward. Note the paper does **not** identify 7 as uniquely optimal — 7, 9 and 10 all performed well — so it should be cited as a justification for "at least 7," not for "7 is best."

---

## 4. Evaluation methodology

- Candy, L. (2006). *Practice based research: A guide* (CCS Report 2006-V1.0). Creativity & Cognition Studios, University of Technology, Sydney. https://www.creativityandcognition.com/wp-content/uploads/2011/04/PBR-Guide-1.1-2006.pdf
  - The practice-based / practice-led distinction underpinning §3 of `README.md`, where the evaluation is described as following "a practice-based research methodology grounded in real creative activity" rather than controlled usability tasks.

- Schmuckler, M. A. (2001). What is ecological validity? A dimensional analysis. *Infancy, 2*(4), 419–436. https://doi.org/10.1207/S15327078IN0204_02
  - Supports the claim in §3 of `README.md` that the approach "prioritises ecological validity." Argues ecological validity is dimensional rather than binary — varying by setting, stimuli, and response — which is the more defensible reading given that this evaluation was conducted inside a real festival production rather than a laboratory.

- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77–101. https://doi.org/10.1191/1478088706qp063oa
  - The foundational account of thematic analysis, and the basis for the coding procedure described under "Qualitative Analysis" in `ANALYSIS_PLAN.md`.

- Fereday, J., & Muir-Cochrane, E. (2006). Demonstrating rigor using thematic analysis: A hybrid approach of inductive and deductive coding and theme development. *International Journal of Qualitative Methods, 5*(1), 80–92. https://doi.org/10.1177/160940690600500107
  - The specific warrant for the **hybrid** approach this study uses: an a priori code manual drawn from §4–§6 of the evaluation report, applied deductively to Q21–Q23, with inductive codes added for material the existing frame does not capture. (Several citation aggregators give the pages as 1–11; the publisher of record gives 80–92.)

---

## 5. Researcher positionality

- Brannick, T., & Coghlan, D. (2007). In defense of being "native": The case for insider academic research. *Organizational Research Methods, 10*(1), 59–74. https://doi.org/10.1177/1094428106289253
  - Supports the position taken in the "Positionality note" in §3 of `README.md` and in "Researcher Positionality" in `ANALYSIS_PLAN.md`: that a practitioner-researcher embedded in the activity under study is an asset to be disclosed and accounted for, rather than a contamination to be removed. This is the basis for retaining P09 in the primary n = 9 results while additionally reporting n = 8.
  - Note that the §3 Positionality note makes **two** disclosures, and this source speaks to the first (the FLO Lab director as both memo author and respondent). The second — that the questionnaire was co-designed in part by the platform's own development side — is a conflict-of-interest disclosure rather than an insider-research one, and is addressed in the report by publishing the instrument, the response data, and the analysis for independent inspection rather than by appeal to method literature.

- Berger, R. (2015). Now I see it, now I don't: Researcher's position and reflexivity in qualitative research. *Qualitative Research, 15*(2), 219–234. https://doi.org/10.1177/1468794112468475
  - Reflexivity as a trustworthiness mechanism, and the specific case of a researcher who shares the participants' experience — the situation of this evaluation, where the memo's author was also one of the nine performers.

---

## Verification note

Every DOI and URL above was resolved and confirmed against a publisher or primary record. Where a publisher's current record disagrees with the commonly cited pagination, both are noted in the entry (Brooke, 1996; Fereday & Muir-Cochrane, 2006).
Two entries have no DOI because none exists: Rohrmann (2007), a self-published project
report, and Lund (2001), a professional-society newsletter article whose original host URL
is dead. Both are cited in the form their authors use.
