# Evidence and review: Which penguin is the heavy one?

## Data sources

| ID | Location | Produced by | Version |
| --- | --- | --- | --- |
| D01 | examples/penguin-project/results/species_summary.csv | analysis.py | sha256 44ac13cc…b45d |
| D02 | examples/penguin-project/results/body_mass_tests.csv | analysis.py | sha256 f09ce2de…1a7f |
| D03 | examples/penguin-project/results/correlations.csv | analysis.py | sha256 adea0068…a73f |
| D04 | examples/penguin-project/data/penguins.csv | Palmer Station LTER, via palmerpenguins | commit 8957207b, sha256 f204db2c…7a93 |
| D05 | palmerpenguins README, https://github.com/allisonhorst/palmerpenguins/blob/8957207b78d6ccd1b4654a9dd9c9041b657478ab/README.md | Horst, Hill and Gorman 2020 | commit 8957207b |

## Claims

| ID | Claim | Values | Source | Location | Status |
| --- | --- | --- | --- | --- | --- |
| C01 | Adelie mean body mass | 3700.7 g; SD 458.6; n = 151 | D01 | species Adelie, body_mass_g | verified |
| C02 | Chinstrap mean body mass | 3733.1 g; SD 384.3; n = 68 | D01 | species Chinstrap, body_mass_g | verified |
| C03 | Gentoo mean body mass | 5076.0 g; SD 504.1; n = 123 | D01 | species Gentoo, body_mass_g | verified |
| C05 | Gentoo minus Adelie mean body mass, Welch | +1375 g; 95% CI 1260 to 1491 g | D02 | row "Welch difference", columns estimate, ci95 | verified |
| C06 | 342 penguins with body mass, three species, 2007 to 2009, Palmer Archipelago, Palmer Station LTER | n = 342; 2007–2009 | D03, D04, D05 | D03 row all/flipper_length_mm/body_mass_g n; D04 year column; D05 lines 39 and 89 | verified |

## Simplifications and analogies

- "Each dot is one bird": exact. Jitter on the horizontal axis is for visibility only and is
  stated in F01's spec.
- The interval is introduced as "the range the true difference plausibly sits in". That is the
  usual plain reading of a ninety-five percent confidence interval; it is looser than the
  frequentist definition. Acceptable for this audience.

## Gaps

- None. The brief asked only for what the results tables contain.

## Proposed substantive changes

- A Gentoo-versus-Chinstrap interval would make T2 symmetric. The project did not report it, so
  the video compares with Adelie only. Adding it needs a new row in body_mass_tests.csv.

## Review

### Checker

`python3 scripts/check_outputs.py examples/short-body-mass`: FAIL 0, WARN 0.

### Rubric

| Dimension | Score (1–3) | Evidence |
| --- | --- | --- |
| Scientific fidelity | 3 | Every number from D01 or D02; interval shown with its level. |
| Objective coverage | 3 | O1 in S04 wrap-up, O2 in S06 wrap-up. |
| Prerequisite order | 3 | The interval is framed on screen before it is read. |
| Orientation | 3 | Two-item roadmap; both titles spoken in roadmap and announcements. |
| Transition quality | 2 | T1 to T2 is a natural question; the bridge to the conclusion is plain. |
| Terminology | 3 | "Gentoo gap" kept throughout. |
| Focus | 3 | One focus per scene; cursor only on the interval ends. |
| Figure building | 3 | Both figures use frame, anchor, fill, pattern, takeaway. |
| Narration voice | 3 | No hedging; contractions and direct address; scope stated as fact. |
| Engagement | 3 | Opening puzzle answered in the conclusion; one prediction with a three-second pause and the dots withheld. |
| Timing | 3 | First draft ran 1:38 against 1:15; target reset to 1:45, then 2:00 after v0.2 added the puzzle and prediction. |
| Technology independence | 3 | No tool-specific instructions. |

Scored by the drafting agent; not a fresh-context review.

### Not yet done

- Subject-matter review by an expert: not done
- Testing with target viewers: not done
