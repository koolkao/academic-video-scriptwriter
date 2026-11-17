# Evidence and review: Longer bills, shallower bills?

## Data sources

| ID | Location | Produced by | Version |
| --- | --- | --- | --- |
| D01 | examples/penguin-project/data/penguins.csv | Horst, Hill & Gorman (2020), palmerpenguins; Palmer Station LTER | sha256 f204db2c… (per README); commit 8957207b |
| D02 | examples/penguin-project/results/correlations.csv | project analysis.py, section 2 | sha256 adea0068… (per README) |
| D03 | examples/penguin-project/results/species_summary.csv | project analysis.py, section 1 | sha256 44ac13cc… (per README) |
| D04 | examples/penguin-project/README.md | project | as supplied |

## Claims

Values are the exact strings shown on screen. Status: verified (checked against the source in
this run), unverified, or gap.

| ID | Claim | Values | Source | Location | Status |
| --- | --- | --- | --- | --- | --- |
| C01 | Pooled across species, bill length and bill depth are weakly negatively correlated | r = −0.24; p = 1.1e-05 | D02 | row group=all, x=bill_length_mm, y=bill_depth_mm | verified |
| C02 | 342 birds have both bill measures | n = 342 | D02 | same row, column n | verified |
| C03 | The birds belong to three species: Adelie, Chinstrap, Gentoo | Adelie; Chinstrap; Gentoo | D03 | species column | verified |
| C04 | Within Adelie, the correlation is positive | Adelie r = 0.39; n = 151; 0.39 | D02 | row group=Adelie, bill_length_mm, bill_depth_mm | verified |
| C05 | Within Chinstrap, the correlation is positive | Chinstrap r = 0.65; n = 68; 0.65 | D02 | row group=Chinstrap, bill_length_mm, bill_depth_mm | verified |
| C06 | Within Gentoo, the correlation is positive | Gentoo r = 0.64; n = 123; 0.64 | D02 | row group=Gentoo, bill_length_mm, bill_depth_mm | verified |
| C07 | Adelie bills are short and deep on average | 38.8 mm; 18.3 mm | D03 | Adelie rows bill_length_mm, bill_depth_mm, mean | verified |
| C08 | Gentoo bills are long but the shallowest on average | 47.5 mm; 15.0 mm | D03 | Gentoo rows bill_length_mm, bill_depth_mm, mean | verified |
| C09 | Chinstrap bills are long and deep on average | 48.8 mm; 18.4 mm | D03 | Chinstrap rows bill_length_mm, bill_depth_mm, mean | verified |
| C10 | Birds were measured on three islands of the Palmer Archipelago, 2007 to 2009 | Palmer Archipelago; 2007–2009 | D01 | island column (Biscoe, Dream, Torgersen) and year column read from data; archipelago name from D04 citation | verified |
| C11 | Diet was not measured, so the data cannot explain why bills differ | none | — | no diet variable in D01 columns; none in D02, D03 | gap |

## Simplifications and analogies

- "Bill depth, how tall the bill is": plain-language gloss of the bill_depth_mm column. Holds for the measurement's meaning; does not say exactly where on the bill it is taken.
- "One line through every bird has to run from the short, deep bills down to the long, shallow Gentoo bills": a verbal description of the plotted pooled line relative to the reported species means (C07–C09). It explains the reversal qualitatively. It is not a reported decomposition of the pooled correlation; no between-group statistic was computed or spoken.
- "Weak, but not noise: the p-value is far below point zero five": p = 1.1e-05 is shown on screen. "Not noise" is a plain reading of a small p-value; it does not mean the effect is large or causal.
- "Each species trend is stronger than the pooled one, and opposite in sign": comparison of reported |r| values (0.39, 0.65, 0.64 versus 0.24); no new statistic.
- "Inside a species, longer bills do tend to be deeper": plain restatement of moderate positive within-species correlations (0.39 to 0.65). Earlier draft said "bigger every way" and "bigger birds have bigger bills"; both widened the claim (only two bill measures; body size not used) and were removed after review.
- "Gentoos pair long bills with shallow ones, and that tilts the pooled line down": a description of the plotted structure (species means C07–C09 against the pooled line), not a biological mechanism and not a reported decomposition.

## Gaps

- C11: the brief asked to explain how diet shapes each species' bill. The project has no diet data, and the skill does not bring in outside literature unless asked. Replaced by one `[unknown]` line in the conclusion. To restore it: supply a published source on these species' diets; it would be added as a new data source and claim.

## Proposed substantive changes

- **Percent heavier, Gentoo versus Chinstrap (requested by the brief; not reported, for the author to confirm).** From D03 body_mass_g means: 5076.0 g (Gentoo, n = 123) and 3733.1 g (Chinstrap, n = 68). (5076.0 − 3733.1) / 3733.1 = 0.3597, about 36 percent. No interval or test for this comparison exists in the project (body_mass_tests.csv compares Gentoo with Adelie only). Not in the script or storyboard. If the author adds it to the results, ideally with an interval, it fits a third topic on body size; that would need about one more minute.
- **Optional, for a stronger T2:** a reported between-species summary (for example the correlation of species means, or a regression of depth on length with species as a covariate) would let the video put a number on the explanation in S08. Not computed here.
- **Caution request:** rendered as concrete scope facts (C10, plus "these are correlations" and the diet gap in the conclusion) instead of the requested stock sentence, which is on the banned-phrase list. Author may prefer a different concrete limitation.

## Review

### Checker

- First draft: FAIL 1 · WARN 12. FAIL: gap claim C11 listed in scene S10's Claims (fixed by removing it; C11 stays only on the `[unknown]` line). WARNs: two untagged quantity lines (a general statement about the range of r, and "both halves"; both cut or reworded) and ten timing WARNs. The narration was 530 words, about 4:02, against a 3:00 target, so it was cut to about 360 words.
- After cutting and rebalancing: FAIL 0 · WARN 0.
- After the review fixes below: FAIL 0 · WARN 0. Narration about 375 words ≈ 2:56 including pauses; storyboard 3:08 (eight seconds over target, accepted as within tolerance; trim S08's cluster tour if a hard 3:00 is needed).

### Rubric

Fresh sub-agent review (it received the four files, the rubric and the source data, but none of the drafting notes). Its scores were for the pre-fix draft; the third column shows what changed afterward.

| Dimension | Score (1–3) | Evidence |
| --- | --- | --- |
| Scientific fidelity | 1 → fixed | All numbers trace; "bigger birds just have bigger bills" and "bigger every way" widened the claim (blocking). Both lines rewritten. |
| Objective coverage | 3 | O1 S04–S05, O2 S07, O3 S08, each wrapped up |
| Prerequisite order | 2 | S01 previewed dots before axes (axis labels added to S01); r refresher promised but cut (plan corrected) |
| Orientation | 3 | Roadmap, word-for-word announcements, outline strip in every topic scene, synthesis |
| Transition quality | 2 → revised | S09 bridge was generic; now names the puzzle question |
| Terminology | 2 | "trend", "tilt", "line" overlap; not fully unified (open) |
| Focus | 2 → revised | S06 Look at now sequenced: arrows, then cloud during the pause |
| Figure building | 2 | Frame → anchor → fill → pattern → takeaway in T1/T2; S01 is an explicit preview |
| Narration voice | 2 → revised | "nobody here" made unambiguous; "That's strange." filler merged |
| Engagement | 2 → revised | Goal line spoiled the prediction; rewritten so it doesn't |
| Timing | 3 | Within tolerance |
| Technology independence | 3 | No tool-specific effects |

Tests run by the sub-agent: checker, narration-only (pass), freeze frame (pass S03–S10; S01 fixed), listener's ear (pass on three lines). Not changed: full terminology unification (tilt vs trend vs line).

### Not yet done

- Subject-matter review by an expert: not done
- Testing with target viewers: not done
- Re-review of the post-fix draft by a fresh reviewer: not done
