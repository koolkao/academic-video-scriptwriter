# Teaching plan: Longer bills, shallower bills?

## Brief

- Audience: second-year biology majors
- Prior knowledge: can read a scatter plot; have met the correlation coefficient r and p-values in an introductory statistics course; have not necessarily met Simpson's paradox; know nothing specific about these penguins
- Purpose: viewers can explain how a pooled correlation can point the opposite way from the correlation inside every group, and so check group structure before trusting a pooled trend in their own lab data
- Target duration: 3:00
- Speech rate: 150 wpm
- Language: English
- Materials: examples/penguin-project/data/penguins.csv; results/correlations.csv; results/species_summary.csv; README.md (data provenance). analysis.py read only to understand how the results were made; not run. body_mass_tests.csv and species_profiles_z.csv read, not used.
- Engagement: full
- Assumptions: "three-minute" is a target of 3:00 with some tolerance; "use TTS" means TTS-ready narration only, no audio is generated; topic titles shortened to "The pooled trend" and "Within each species"; the diet, percent-heavier, and caution requests are handled as described under Scope exclusions rather than as written, because each conflicts with a hard rule (see that section).

## Puzzle

- Question: across three hundred and forty two penguins, birds with longer bills tend to have shallower bills. But a bigger bill should be bigger in every direction. Why does length go with shallowness?
- Rests on: C01, C02
- Answered in: conclusion; the key step is T2, where the species colors reveal that every species tilts up and the groups sit in different places.
- Predictions: one, in T2 (S06): "Inside each species, will the trend tilt up, or down?" Species colors and per-species lines are withheld; dots stay gray with only the pooled line until S07.

## Objectives

| ID | Viewers can … | Topic |
| --- | --- | --- |
| O1 | state the direction and rough strength of the pooled bill length–bill depth correlation | T1 |
| O2 | state that the correlation is positive inside each of the three species | T2 |
| O3 | explain, pointing at the species clusters, why the pooled trend tilts down when each species tilts up | T2 |

## Topics

Outline order. The title is the spoken label: two to five words, used word for word in the
roadmap and the announcement.

| ID | Title | Prerequisites | Takeaway |
| --- | --- | --- | --- |
| T1 | The pooled trend | reading a scatter plot; what r measures (assumed known; no refresher, cut for time) | Pooled across all birds, longer bills go with shallower bills, weakly. |
| T2 | Within each species | T1; the idea of a group | Inside every species, longer bills are deeper; the pooled downward tilt comes from where the species sit. |

## Figure-reading prerequisites

Scatter plot with a least-squares trend line: second-year biology majors read these; T1 still frames axes before data. The correlation coefficient is assumed known from intro statistics; the refresher sentence was cut for time. If the audience is shakier, restore it in S04 (about four seconds).

## Figure inventory

| ID | Existing artifact or data | Decision | Notes |
| --- | --- | --- | --- |
| F01 | data/penguins.csv (raw rows); no existing figure in the project | new plot from project data | scatter, bill length vs bill depth; pooled least-squares line, then species colors and per-species least-squares lines. Rows with missing bill measures are dropped, matching the 342 complete pairs in correlations.csv. |
| — | results/correlations.csv | values printed on F01 | pooled and within-species r, n, p |
| — | results/species_summary.csv | values printed on F01 at species cluster centers | bill length and depth means |

## Visual vocabulary

| Concept | Shape and color role | Used in |
| --- | --- | --- |
| unsorted bird | dot, muted context color | F01 |
| Adelie | dot, species A color, circle marker | F01 |
| Chinstrap | dot, species B color, triangle marker | F01 |
| Gentoo | dot, species C color, square marker | F01 |
| pooled trend | thick line, neutral dark | F01 |
| within-species trend | thin line in the species color | F01 |
| statistics | small label block, same corner and format every time | F01 |

## Visual brief

- Mood: clean scientific, light ground, restrained color; one plot that stays on screen and changes meaning
- Home visual: an outline strip along the top with two items, "1 · The pooled trend" and "2 · Within each species"
- Metaphor family: none needed; the figure is the explanation
- Color roles: muted context (unsorted dots, dimmed elements); species A, B, C (color-blind-safe qualitative palette, each paired with a marker shape); highlight (the element being discussed)
- Topic transition gesture: the outline highlight slides to the next item; the chapter heading under it changes

## Pronunciation

| Term | Say as | Note |
| --- | --- | --- |
| Adelie | uh-DAY-lee | species name; one word |
| Gentoo | JEN-too | species name |
| Chinstrap | CHIN-strap | species name |
| Palmer Archipelago | PAH-mer ar-kih-PEL-uh-go | place |
| p-value | PEE value | letter, then word |
| Simpson's paradox | SIMP-sunz PAIR-uh-docks | term |
| twenty oh seven, twenty oh nine | as written | years, not counts |

## Scope exclusions

- **"Explain how diet shapes each species' bill."** The project has no diet variable (D01 columns: species, island, bill length, bill depth, flipper length, body mass, sex, year). Explaining diet would mean bringing in claims from outside the supplied materials, which the skill does not do unless asked. Instead, one `[unknown]` line (C11) says plainly that diet was not measured, so these data cannot say why the bills differ. If you want the diet explanation, supply a source (a paper on Pygoscelis diets) and it can become a cited claim.
- **"Say what percent heavier Gentoos are than Chinstraps."** The project has not reported this percentage; the skill may not compute new statistics. The arithmetic from reported means is under *Proposed substantive changes* in evidence-and-review.md. It is also off-topic: body mass belongs to neither requested topic, and a third topic would not fit three minutes (see Timing). Options: add the percentage to the project's results and make it a third topic in a longer video, or drop it.
- **"Add a sentence saying the results should be interpreted with caution."** That exact phrasing is a banned stock disclaimer. Its content is delivered as concrete facts instead: where and when the birds were measured (C10, in T1), that these are correlations among measurements that cannot say what causes the bill shapes, and that diet was not measured (C11, conclusion).
- Flipper length, body mass, sex, island differences, and the ANOVA results are left out: they belong to no requested topic.

## Timing

Budget: 3 min × 150 wpm × 0.8 = 360 spoken words. The first draft ran 530 words (checker estimate 4:02), well over budget, so it was cut to about 360 words: shorter reasoning lines, one refresher sentence on r removed, fewer spoken numbers. Final estimate after review fixes: about 375 words plus 26 s of pause marks ≈ 2:56 of narration; storyboard scene durations, including holds, total 3:08. That is within a reasonable tolerance of 3:00. No topic was cut. A third topic (body mass) would need about one more minute.
