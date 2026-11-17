# Evidence and review: One trend pooled, another within species

## Data sources

| ID | Location | Produced by | Version |
| --- | --- | --- | --- |
| D01 | examples/penguin-project/data/penguins.csv | Horst, Hill & Gorman (2020), palmerpenguins, CC0; copied per README.md | sha256 f204db2c…7a93 (matches README) |
| D02 | examples/penguin-project/results/correlations.csv | project analysis.py, section 2 (Pearson r, pooled and within species) | sha256 adea0068…a73f (matches README) |
| D03 | examples/penguin-project/results/species_summary.csv | project analysis.py, section 1 (n, mean, SD per species) | sha256 44ac13cc…b45d (matches README) |
| D04 | examples/penguin-project/README.md | project README (provenance) | read in this run |

## Claims

Values are the exact strings shown on screen. Status: verified (checked against the source in
this run), unverified, or gap.

| ID | Claim | Values | Source | Location | Status |
| --- | --- | --- | --- | --- | --- |
| C01 | Pooled across species, bill length and bill depth have a weak negative correlation. | r = −0.24; n = 342; p = 1.1 × 10⁻⁵ | D02 | row group=all, x=bill_length_mm, y=bill_depth_mm (r −0.24, n 342, p 1.1e-05) | verified |
| C02 | Within Adelie, the correlation is positive. | r = 0.39; n = 151; p = 6.7 × 10⁻⁷ | D02 | row group=Adelie, bill_length_mm × bill_depth_mm | verified |
| C03 | Within Chinstrap, the correlation is positive. | r = 0.65; n = 68; p = 1.5 × 10⁻⁹ | D02 | row group=Chinstrap, bill_length_mm × bill_depth_mm | verified |
| C04 | Within Gentoo, the correlation is positive. | r = 0.64; n = 123; p = 1.0 × 10⁻¹⁵ | D02 | row group=Gentoo, bill_length_mm × bill_depth_mm | verified |
| C05 | Species mean bill length and depth: Adelie short and deep, Gentoo long and shallow, Chinstrap long and deep. | 38.8 mm, 18.3 mm; 47.5 mm, 15.0 mm; 48.8 mm, 18.4 mm | D03 | rows measure=bill_length_mm and bill_depth_mm for Adelie, Gentoo, Chinstrap, column mean | verified |
| C06 | Gentoo mean body mass is larger than Chinstrap mean body mass. | 5076.0 g; SD 504.1; n = 123; 3733.1 g; SD 384.3; n = 68 | D03 | rows species=Gentoo and Chinstrap, measure=body_mass_g, columns mean, sd, n | verified |
| C07 | The sample: 342 penguins with both bill measures, 3 species, measured on 3 islands of the Palmer Archipelago, Antarctica, 2007–2009. | 342; 3 species; 3 islands; 2007–2009 | D01, D02, D04 | D02 n column for group=all (342); D01 columns species (Adelie, Chinstrap, Gentoo), island (Biscoe, Dream, Torgersen), year (2007, 2008, 2009 only); D04 for "Palmer Archipelago (Antarctica)" | verified |
| C08 | Diet shapes each species' bill. | none | D01 | no diet, prey, or feeding variable in D01–D04 | gap |
| C09 | Gentoos are some percent heavier than Chinstraps. | none | D03 | ratio not reported in any results file | gap |

Note on C07: the counts of species, islands, and the year range are read from the distinct values of three raw columns, not computed statistics. I treated them as reported. If the author considers distinct-value counts "computed," confirm them.

## Simplifications and analogies

- Bill depth is described as "the height of the bill from top to bottom." This is the standard meaning of the measure; the project files name the column but do not define it.
- The explanation of the reversal (S10) is an interpretation of reported species means, not a separate result: short, deep Adelies and long, shallow Gentoos sit on opposite corners of the plot, so the between-species difference dominates the pooled correlation. It holds as a description of the reported means; it does not say why species differ. Chinstraps (long and deep) pull against the falling diagonal, and the narration says so ("so they pull against the tilt").
- "Tilts upward / downward" stands for the sign of r. No fitted line is drawn because the project did not report slopes.
- No analogies used.

## Gaps

- C08, diet: the brief asked to explain how diet shapes each species' bill. No diet data exist in the project, and outside research was not requested. Left out of the narration. Replacement: S12 states that the correlations describe how the measures go together, not what shaped them. To restore the point, the author can supply a cited diet source or diet data, and the claim would be added with that source, worded as the source supports (likely "is linked to," not "shapes," unless the source shows mechanism).
- C09, percent heavier: not reported by the project; left out. Replacement: both reported means, with SD and n, on screen in S11 and spoken rounded.

## Proposed substantive changes

- Add the Gentoo versus Chinstrap body mass ratio to the project's results if the author wants the percent spoken. Arithmetic from D03 means, for the author to confirm and add to the results, not for use in the video as is: 5076.0 / 3733.1 = 1.360, so about 36 percent heavier (difference 1342.9 g). A Welch interval for the Gentoo minus Chinstrap difference, like the one the project already reports for Gentoo minus Adelie, would let the video show uncertainty with it. Not in the script until the author adds it.
- Add least-squares slopes, pooled and per species, for bill depth on bill length. That would allow fitted lines on F01 and F02, which make the tilt much easier to see than r = −0.24 alone.
- The user's requested sentence "the results should be interpreted with caution" was not used: it is a banned stock disclaimer. Its content is carried by C07 (who, where, when) in T1 and by the association-not-cause sentence in T2. If the author has a specific limitation in mind (for example, sexes pooled, or island confounded with species), name it and it can be stated concretely.

## Review

### Checker

Final run: FAIL 0 · WARN 0. Earlier runs: first draft FAIL 1 (conclusion scene S13 lacked a `Topic change` marker; added) and 11 WARN (scene durations shorter than narration; narration 3:35 against a 3:00 target). Fixed by cutting narration from 473 to about 405 words and resetting durations, not by raising the speech rate. Summary notes C08 and C09 as unused: expected, they are gap claims kept for the record. Storyboard total 3:17 against 3:00 (within the checker's 10 percent tolerance); see Timing in the teaching plan for the S11 cut option.

### Rubric

Run by a fresh sub-agent that received the four files, the rubric, the references, and the project data, but not the drafting notes. It re-ran the checker and checked every number against the CSVs. Tests run by that sub-agent: narration only (pass), freeze frame on S04, S08, S11 (S11 weak: the body-mass chart had no reason to be there), two renderers (pass), listener's ear (flagged "r is" being heard as "are"; relies on the Pronunciation table; and "Gentoos sit low and to the right" was misleading because Chinstrap bills are longer). No blocking failures.

| Dimension | Score (1–3) | Evidence |
| --- | --- | --- |
| Scientific fidelity | 2 → fixed | All values trace; S10 "to the right" and missing Chinstrap caveat were corrected after review |
| Objective coverage | 3 | O1–O3 taught and wrapped in S05, S12, S13 |
| Prerequisite order | 3 | Axes framed in S03; Simpson's paradox named after it is explained |
| Orientation | 3 | Roadmap, outline strip in every scene, announcements, synthesis |
| Transition quality | 2 → fixed | S12 bridge was thin; now names the between-species versus within relationship; S11 given a lead-in |
| Terminology | 3 | One name per concept; pronunciations listed |
| Focus | 2 | S10 is long (five lines, 30 s) but keeps one marker at a time; S11 is an aside the user requested |
| Figure building | 3 | F02 frame → anchor → fill → pattern → takeaway |
| Narration voice | 3 | Caution sentence replaced with concrete scope and association facts; no filler |
| Timing | 2 | 3:17 storyboard against 3:00 target; S11 is the offered cut |
| Technology independence | 3 | No tool or provider named |

Fixes applied after review: S10 wording ("Gentoos sit low"; Chinstraps "pull against the tilt"), S11 lead-in ("Gentoos also differ in size"), S12 bridge ("one trend runs between species, and another runs within them"), the percent arithmetic labeled as author-only. Not applied: removing `{C07}` from the S05 bridge, because the line says "three species" and the checker asks for a claim tag on any spoken quantity. Not re-reviewed after the fixes; the drafting agent re-ran the checker only.

### Not yet done

- Subject-matter review by an expert: not done
- Testing with target viewers: not done
