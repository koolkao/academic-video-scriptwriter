# Teaching plan: One trend pooled, another within species

## Brief

- Audience: second-year biology majors
- Prior knowledge: scatter plots, the idea of a correlation coefficient r and its sign, basic penguin biology; not assumed: Simpson's paradox, how pooling groups can reverse a trend
- Purpose: read a correlation in pooled data and within groups, and explain why the two can point in opposite directions; this matters whenever they pool measurements from groups that differ
- Target duration: 3:00
- Speech rate: 150 wpm
- Language: English, read by a TTS voice
- Materials: examples/penguin-project/data/penguins.csv; results/correlations.csv; results/species_summary.csv; results/body_mass_tests.csv and results/species_profiles_z.csv (read, not used); README.md (provenance and checksums); analysis.py (read to confirm how results were produced)
- Assumptions: second-year majors already know what r is and what its sign means, so no separate figure-reading topic; scatter plots need only a short frame step. The user's two topics are kept as the whole outline. The species-mean explanation of the reversal sits inside topic two. Body mass is a short aside in topic two because the user asked for the Gentoo versus Chinstrap comparison. The diet explanation, the percent figure, and the caution sentence are handled as described in Scope exclusions and in evidence-and-review.md. TTS voice and provider are left to production.

## Objectives

| ID | Viewers can … | Topic |
| --- | --- | --- |
| O1 | state the direction and strength of the pooled bill length to bill depth correlation, and the sample it comes from | T1 |
| O2 | state the direction of the correlation within each of the three species | T2 |
| O3 | explain, using where each species sits on the plot, why the pooled and within-species correlations have opposite signs | T2 |

## Topics

Outline order. The title is the spoken label: two to five words, used word for word in the
roadmap and the announcement.

| ID | Title | Prerequisites | Takeaway |
| --- | --- | --- | --- |
| T1 | The pooled trend | scatter plot; sign of r | Across all 342 birds, longer bills go with slightly shallower bills (r = −0.24). |
| T2 | Within each species | T1; species colors | Inside every species, longer bills go with deeper bills; the pooled negative sign comes from where the species sit relative to each other (Simpson's paradox). |

## Figure-reading prerequisites

Scatter plots are familiar to this audience. The video frames the axes once in T1 (what across and up mean, one dot is one bird) and reuses the same axes in T2, so no extra topic is needed. Species mean markers are introduced in T2 as "the center of each species."

## Figure inventory

| ID | Existing artifact or data | Decision | Notes |
| --- | --- | --- | --- |
| F01 | data/penguins.csv (raw rows); results/correlations.csv | new plot from project data | Pooled scatter, all points in one neutral color; no fitted line (the project did not report slopes) |
| F02 | data/penguins.csv; results/correlations.csv; results/species_summary.csv | new plot from project data | Same scatter recolored by species, then split into three panels on identical axes; species means as large markers |
| F03 | results/species_summary.csv (body_mass_g rows) | new plot from project data | Two bars, Gentoo and Chinstrap mean body mass with SD whiskers |

The project has no existing figures; all three are drawn from project data.

## Visual vocabulary

| Concept | Shape and color role | Used in |
| --- | --- | --- |
| Pooled data (species not shown) | small dots, muted context color | F01 |
| Adelie | color role species A, circle | F02, F03 legend order |
| Chinstrap | color role species B, triangle | F02, F03 |
| Gentoo | color role species C, square | F02, F03 |
| Species mean | the species' shape, enlarged, with outline | F02 |
| Correlation readout | "r = … · n = … · p = …" in one fixed corner of each panel | F01, F02 |
| Outline strip | two items across the top: "1 · The pooled trend", "2 · Within each species"; current item lit | all scenes |

## Visual brief

- Mood: clean scientific, light ground, restrained color; data in color, everything else gray
- Home visual: the outline strip plus the bill length by bill depth axes, which stay the same across the whole video
- Metaphor family: none needed; the plot itself carries the idea
- Color roles: muted context; species A, B, C (color-blind-safe qualitative, each with its own shape); highlight
- Topic transition gesture: the outline strip highlight slides to the next item and the chapter heading changes

## Pronunciation

| Term | Say as | Note |
| --- | --- | --- |
| Adelie | uh-DAY-lee | word; plural Adelies, uh-DAY-leez |
| Gentoo | JEN-too | word; plural Gentoos |
| Chinstrap | CHIN-strap | word |
| Palmer Archipelago | PAH-mer ar-kih-PEL-uh-go | word |
| r | ar | single letter, the correlation coefficient |
| Simpson's paradox | SIMP-sunz PAIR-uh-docks | word |

## Scope exclusions

- How diet shapes each species' bill: the project contains no diet data, and the brief limits me to the supplied materials. Left out of the narration and recorded as a gap. The video says plainly that these are correlations in measured birds and do not show what shaped the bills.
- Percent by which Gentoos are heavier than Chinstraps: the project does not report this ratio. The skill forbids computing it. The video shows the two reported means instead; the arithmetic is offered under Proposed substantive changes.
- "Results should be interpreted with caution": this exact sentence is a banned stock disclaimer. Its content is stated as concrete facts instead: the sample (342 birds, three islands, 2007 to 2009) in T1, and association versus cause in T2.
- Flipper length, sex, island differences, the body mass ANOVA, and z-score profiles: not needed for the two topics.

## Timing

Narration is about 400 words at 150 wpm (about 2:40) plus about 19 s of marked pauses, about 3:00 of audio. Scene durations add half of each reading hold on top, giving a storyboard total of about 3:17, just under 10 percent over the 3:00 target. A first draft ran 473 words (3:35) and was cut by trimming sentences, not by raising the speech rate. If 3:00 is a hard limit, the cleanest cut is the body-mass aside (S11, about 12 s), which is not needed for either topic's argument.
