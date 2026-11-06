# Hi-Audio Platform: Practice-Based Evaluation by FLO Lab

This repository publishes a practice-based evaluation of the [Hi-Audio](https://hiaudio.fr) web platform. Between 13 February and 13 March 2026, nine performers from the [Female Laptop Orchestra (FLO)](https://femalelaptoporchestra.org/) used the platform to record the source tracks of a collaborative composition, which was then mixed offline for the Radiophrenia 2026 festival broadcast. The FLO Lab director reported the evaluation in a memo, and a follow-up participant survey was analysed afterwards. Both documents, the survey instrument and the pseudonymised response data are published here.

The platform itself is described in Gil Panal, David and Richard (2026). A complementary task-based usability study of the platform, conducted with 22 participants using the System Usability Scale (SUS; Brooke, 1996) and the NASA Task Load Index (NASA-TLX; Hart & Staveland, 1988), is available at [hiaudio_user_evaluation_results](https://github.com/idsinge/hiaudio_user_evaluation_results).

## Read online

**https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/**

| Document | Authors | Read | Source in this repository |
|---|---|---|---|
| Practice-based evaluation memo, 22 March 2026, reproduced as delivered | Nela Brown | [Web page](https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/docs/memo.html) · [original PDF](./docs/Practice-Based%20Evaluation%20of%20the%20Hi-AUDiO%20platform%20by%20FLO%20Lab%20.pdf) | [`docs/output.md`](./docs/output.md) |
| Participant survey analysis | Nela Brown, José M. Gil Panal | [Web page](https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/docs/analysis.html) | [`docs/analysis_summary.md`](./docs/analysis_summary.md) |

The web pages are generated from those sources by [`docs/build_pages.py`](./docs/build_pages.py). Edit the sources, never the HTML, and rebuild with `python3 docs/build_pages.py`.

## Repository contents

The table below lists everything published in the repository.

| Category | File / folder | What it is |
|---|---|---|
| Web pages | [`index.html`](./index.html) | Landing page of the website, linking the memo and the analysis |
| Web pages | [`docs/memo.html`](./docs/memo.html) | The memo as a web page, built from `docs/output.md` |
| Web pages | [`docs/analysis.html`](./docs/analysis.html) | The survey analysis as a web page, built from `docs/analysis_summary.md` |
| Web pages | [`docs/build_pages.py`](./docs/build_pages.py) | Builds the three pages above (standard-library Python) |
| Memo | [`docs/Practice-Based Evaluation of the Hi-AUDiO platform by FLO Lab .pdf`](./docs/Practice-Based%20Evaluation%20of%20the%20Hi-AUDiO%20platform%20by%20FLO%20Lab%20.pdf) | The memo as delivered, as a PDF |
| Memo | [`docs/output.md`](./docs/output.md) | The Pandoc conversion of the memo's original `.docx`, kept unchanged except for 8 relative image paths updated when the file moved into `docs/` |
| Memo | `images/` | The memo's Appendix B screenshots (`image1.png`–`image8.png`) and the EU/ERC emblem (`ERC_logo.png`) |
| Survey | [`docs/participant_survey.md`](./docs/participant_survey.md) | The participant questionnaire, as administered via JotForm (23 questions, three sections) |
| Survey | [`docs/ANALYSIS_PLAN.md`](./docs/ANALYSIS_PLAN.md) | The planned approach for analysing the survey responses: quantitative and thematic-coding methodology, triangulation against the memo |
| Survey | [`docs/analysis_summary.md`](./docs/analysis_summary.md) | The survey analysis: sample description, quantitative results, thematic coding of the open questions, and triangulation against the memo |
| Survey | [`docs/figures/`](https://github.com/idsinge/hiaudio_FLO_practice-based_evaluation/tree/main/docs/figures) | The analysis figures (SVG), plus `make_figures.py`, which regenerates them from the published response data |
| Survey | [`docs/REFERENCES.md`](./docs/REFERENCES.md) | Annotated reference list for the sources cited in this repository |
| Response data | [`docs/participant_survey_responses.csv`](./docs/participant_survey_responses.csv) / [`.xlsx`](./docs/participant_survey_responses.xlsx) | Pseudonymised respondent-level responses from all 9 participants, one row per respondent. Rows carry a submission date, not a participant ID; use `docs/response_id_mapping.md` to link a row to its P01–P09 identifier |
| Response data | [`docs/individual_participant_responses/`](https://github.com/idsinge/hiaudio_FLO_practice-based_evaluation/tree/main/docs/individual_participant_responses) | Per-respondent submission exports (`P01.pdf`–`P09.pdf`), pseudonymised by participant ID |
| Response data | [`docs/response_id_mapping.md`](./docs/response_id_mapping.md) | Maps each participant ID (P01–P09) to its original JotForm submission identifier, for cross-referencing the CSV/XLSX rows against the individual PDFs |
| About the repository | [`CITATION.cff`](CITATION.cff) | Structured citation metadata (also powers GitHub's "Cite this repository" button) |
| About the repository | [`LICENSE`](LICENSE) | CC BY 4.0 — covers everything **except** the participant response data |
| About the repository | [`docs/DATA_LICENSE.md`](./docs/DATA_LICENSE.md) | Research-use licence governing the participant response data (CSV/XLSX, individual PDFs, ID mapping) |
| About the repository | [`CONTEXT.md`](CONTEXT.md) | Project background and working notes for collaborators |
| About the repository | [`AGENTS.md`](AGENTS.md) / [`CLAUDE.md`](CLAUDE.md) | Working instructions for AI coding assistants and collaborators working in this repository |
| About the repository | [`_config.yml`](https://github.com/idsinge/hiaudio_FLO_practice-based_evaluation/blob/main/_config.yml) | Jekyll configuration for GitHub Pages (Jekyll does not copy underscore-prefixed files into the published site, so this link points at the repository) |

All response data was screened for personally identifiable information before publication; see [Positionality](#positionality) below for the one disclosed exception.

The response data is **pseudonymised rather than anonymised**: each row is one respondent, carrying a submission date that links to a stable participant identifier through `docs/response_id_mapping.md`. Because the cohort is small and the festival's published programme names the performers of this piece, readers should treat these records as re-identifiable and use them accordingly.

## Positionality

The participant questionnaire was designed collaboratively by Nela Brown, FLO Lab director, and José M. Gil Panal, lead software engineer of the Hi-AUDiO project, who also co-authored the survey analysis. Two aspects of that arrangement are disclosed here for transparency.

First, Nela Brown, who wrote the memo, also completed the questionnaire as one of the nine respondents (participant P09 in the published response data). Her response is retained in the dataset rather than excluded, consistent with the practice-based, practitioner-embedded nature of this evaluation (Brannick & Coghlan, 2007; Berger, 2015), and the analysis reports every rating both with and without it. One consequence of this disclosed dual role: her name appears once in the response data itself, in a track filename she references in her own answer — left unredacted, since she is the memo's named author.

Second, José M. Gil Panal is a member of the Hi-AUDiO team that develops the platform under evaluation, so the questionnaire and the analysis come in part from the platform's own development side. He did not complete the questionnaire and is not among the nine respondents. This is disclosed so that readers can weigh it: the questionnaire as administered, the full pseudonymised response data, and the analysis of those responses are all published in this repository and can be examined independently.

## Licensing

**Licensing is split.** The memo, the survey instrument, the analysis, the web pages, and the images are licensed [CC BY 4.0](LICENSE), except the EU/ERC emblem, whose use follows the EU's and the ERC's own rules. The participant response data — the CSV/XLSX, the individual respondent PDFs, and the ID mapping — is released under a more restrictive [research-use licence](./docs/DATA_LICENSE.md): non-commercial academic research and educational use only, no redistribution, and no attempted re-identification.

## References

Sources cited in this file. The complete annotated list, including the sources behind the survey items and the analysis methods, is in [`docs/REFERENCES.md`](./docs/REFERENCES.md).

- Berger, R. (2015). Now I see it, now I don't: Researcher's position and reflexivity in qualitative research. *Qualitative Research, 15*(2), 219–234. https://doi.org/10.1177/1468794112468475
- Brannick, T., & Coghlan, D. (2007). In defense of being "native": The case for insider academic research. *Organizational Research Methods, 10*(1), 59–74. https://doi.org/10.1177/1094428106289253
- Brooke, J. (1996). SUS: A "quick and dirty" usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Eds.), *Usability evaluation in industry* (pp. 189–194). Taylor & Francis. https://doi.org/10.1201/9781498710411-35
- Gil Panal, J. M., David, A., & Richard, G. (2026). The Hi-Audio online platform for recording and distributing multi-track music datasets. *Journal on Audio, Speech, and Music Processing, 2026*, Article 26. https://doi.org/10.1186/s13636-026-00459-0
- Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. In P. A. Hancock & N. Meshkati (Eds.), *Human mental workload* (pp. 139–183). North-Holland. https://doi.org/10.1016/S0166-4115(08)62386-9

## Citation

This repository contains three citable components. Cite whichever matches what you actually used. A structured [CITATION.cff](CITATION.cff) is also included, which GitHub uses to generate a "Cite this repository" option automatically.

**To cite the evaluation memo:**

> Brown, N. (2026). *Practice-Based Evaluation: Hi-AUDiO* [Evaluation memo, 22 March 2026]. FLO Lab, Female Laptop Orchestra. https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/docs/memo.html

**To cite the survey analysis** — including any specific survey finding, figure, or theme:

> Brown, N., & Gil Panal, J. M. (2026). *Hi-AUDiO FLO Participant Survey — Analysis Summary*. FLO Lab, Female Laptop Orchestra / Hi-AUDiO, Télécom Paris. https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/docs/analysis.html

**To cite the full repository** — the memo together with the participant survey, the pseudonymised response data, and the survey analysis:

> Brown, N., & Hi-AUDiO (2026). *Hi-AUDiO: Practice-Based Evaluation — Report, Participant Survey, and Response Analysis*. FLO Lab, Female Laptop Orchestra / Hi-AUDiO, Télécom Paris. https://github.com/idsinge/hiaudio_FLO_practice-based_evaluation

**BibTeX:**

```bibtex
@techreport{Brown2026hiaudio,
  author      = {Brown, Nela},
  title       = {Practice-Based Evaluation: Hi-{AUDiO}},
  type        = {Evaluation memo},
  institution = {FLO Lab, Female Laptop Orchestra},
  year        = {2026},
  month       = mar,
  url         = {https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/docs/memo.html}
}

@techreport{BrownGilPanal2026survey,
  author      = {Brown, Nela and Gil Panal, Jos{\'e} M.},
  title       = {Hi-{AUDiO} {FLO} Participant Survey --- Analysis Summary},
  institution = {FLO Lab, Female Laptop Orchestra / Hi-AUDiO, T{\'e}l{\'e}com Paris},
  year        = {2026},
  url         = {https://idsinge.github.io/hiaudio_FLO_practice-based_evaluation/docs/analysis.html}
}

@misc{Brown2026hiaudiorepo,
  author       = {Brown, Nela and {Hi-AUDiO}},
  title        = {Hi-AUDiO: Practice-Based Evaluation --- Report, Participant Survey,
                  and Response Analysis},
  year         = {2026},
  howpublished = {GitHub repository, FLO Lab, Female Laptop Orchestra /
                  Hi-AUDiO, T{\'e}l{\'e}com Paris},
  url          = {https://github.com/idsinge/hiaudio_FLO_practice-based_evaluation}
}
```

## Acknowledgements

The Hi-Audio platform is developed as part of the project *Hybrid and Interpretable Deep Neural Audio Machines*, funded by the European Research Council (ERC) under the European Union's Horizon Europe research and innovation programme (grant agreement No. 101052978).

Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.

<img src="./images/ERC_logo.png" alt="Emblem of the European Union and logo of the European Research Council" width="250"/>
