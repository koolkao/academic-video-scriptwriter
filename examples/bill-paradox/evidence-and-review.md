# Evidence and review: Longer bills, shallower bills?

## Data sources

| ID | Location | Produced by | Version |
| --- | --- | --- | --- |
| D01 | examples/penguin-project/results/species_summary.csv | analysis.py | sha256 44ac13cc…b45d |
| D03 | examples/penguin-project/results/correlations.csv | analysis.py | sha256 adea0068…a73f |
| D04 | examples/penguin-project/data/penguins.csv | Palmer Station LTER, via palmerpenguins | commit 8957207b, sha256 f204db2c…7a93 |
| D05 | palmerpenguins README, https://github.com/allisonhorst/palmerpenguins/blob/8957207b78d6ccd1b4654a9dd9c9041b657478ab/README.md | Horst, Hill and Gorman 2020 | commit 8957207b |
| D06 | examples/penguin-project/results/species_profiles_z.csv | analysis.py | sha256 2bd621ff…703b |

## Claims

| ID | Claim | Values | Source | Location | Status |
| --- | --- | --- | --- | --- | --- |
| C01 | 342 penguins with both bill measurements, three species, 2007 to 2009, Palmer Archipelago | n = 342; 2007–2009 | D03, D04, D05 | D03 row all/bill_length_mm/bill_depth_mm; D04 year; D05 line 89 | verified |
| C02 | Pooled correlation of bill length and bill depth | r = −0.24; n = 342; p = 1.1e-05; p < 0.001 | D03 | row all, bill_length_mm, bill_depth_mm | verified |
| C03 | Adelie within-species correlation | r = 0.39; n = 151; p = 6.7e-07; p < 0.001 | D03 | row Adelie, bill_length_mm, bill_depth_mm | verified |
| C04 | Chinstrap within-species correlation | r = 0.65; n = 68; p = 1.5e-09; p < 0.001 | D03 | row Chinstrap, bill_length_mm, bill_depth_mm | verified |
| C05 | Gentoo within-species correlation | r = 0.64; n = 123; p = 1.0e-15; p < 0.001 | D03 | row Gentoo, bill_length_mm, bill_depth_mm | verified |
| C06 | Adelie profile, z-scores against pooled mean and SD | bill length −0.94; bill depth 0.61; flipper −0.78; mass −0.62 | D06 | row Adelie | verified |
| C07 | Chinstrap profile | bill length 0.9; bill depth 0.64; flipper −0.36; mass −0.58 | D06 | row Chinstrap | verified |
| C08 | Gentoo profile | bill length 0.66; bill depth −1.1; flipper 1.16; mass 1.09 | D06 | row Gentoo | verified |
| C09 | Pooled correlations among the four measurements, six pairs | −0.24; 0.66; 0.6; −0.58; −0.47; 0.87; 6 pairs | D03 | rows group = all | verified |
| C10 | Gentoo correlations among the four measurements, all positive | 0.64; 0.66; 0.67; 0.71; 0.72; 0.7; 0.64 to 0.72 | D03 | rows group = Gentoo | verified |
| C11 | Species mean bill length and depth | Adelie 38.8 mm, 18.3 mm; Chinstrap 48.8 mm, 18.4 mm; Gentoo 47.5 mm, 15.0 mm | D01 | bill_length_mm and bill_depth_mm rows | verified |
| C12 | Diet causes the species' bill shapes | — | D04 | no diet variable in the data | gap |

## Simplifications and analogies

- **Contour rings as hiking-map height lines (T1).** Holds: a ring joins points of equal value,
  and stacked rings mark a peak. Breaks: on a hiking map the value is ground height; here it is
  how many birds have those measurements. The wrap-up says this in one sentence. Contour levels
  come from a kernel density estimate, a smoothing choice the renderer makes; levels must be
  identical in F01 and F02.
- **"The negative trend came from where the islands sit" (T3) and "that placement tilts the
  pooled trend" (T4).** Interpretation of the figures, not a reported statistic. It is the
  standard reading of Simpson's paradox with these data. No number is attached to it.
- **"The middle ring is the average penguin" (T4).** Exact for z = 0 against the pooled mean.

## Gaps

- **C12, diet as cause of bill shape.** The brief asked for it; the project has no diet data.
  Left out of the script. Replacement: T4 describes how the species differ, without saying why.

## Proposed substantive changes

- A pooled regression with species as a covariate would put a single number on "the trend
  within species". The project has not reported one, so the video uses the three within-species
  correlations instead.

## Review

### Checker

`python3 scripts/check_outputs.py examples/bill-paradox`: FAIL 0, WARN 1.

- WARN script.md:50 ("pale cells are near zero"): the heat map legend, not a data claim. Left as is.
- First run had 15 WARN: three structural counts ("four measurements") rephrased or tagged, eleven
  scenes too short for their narration lengthened, and the 5:00 target extended to 6:30 (see
  the teaching plan, Timing).
- Note: claim C12 is a gap and is correctly unused.

### Rubric

| Dimension | Score (1–3) | Evidence |
| --- | --- | --- |
| Scientific fidelity | 3 | All numbers from D01, D03, D06; no causal claim about diet; interpretation labeled above. |
| Objective coverage | 3 | Each objective has a wrap-up line in its topic. |
| Prerequisite order | 3 | Contour reading is T1; radar and heat map get frame steps before data. |
| Orientation | 3 | Five-item roadmap; T3 changes topic over the same axes with a spoken and visible marker. |
| Transition quality | 3 | Prerequisite, cause, and generalization bridges; none forced. |
| Terminology | 3 | "pooled", "within species", "profile" kept fixed. |
| Focus | 3 | Cursor used for single heat-map cells and radar spokes; figure-led elsewhere. |
| Figure building | 3 | All four figures follow frame, anchor, fill, pattern, takeaway. |
| Narration voice | 3 | No hedging; the scope is stated as fact in the conclusion. |
| Timing | 2 | First draft ran 5:42 against 5:00; runtime extended to 6:30 rather than compressing T1 or dropping T5. |
| Technology independence | 3 | No tool-specific instructions. |

Scored by the drafting agent; not a fresh-context review.

### Not yet done

- Subject-matter review by an expert: not done
- Testing with target viewers: not done
