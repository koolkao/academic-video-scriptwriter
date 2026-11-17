# Teaching plan: Longer bills, shallower bills?

## Brief

- Audience: first-year undergraduate biology students
- Prior knowledge: scatter plots, the idea of a correlation coefficient from minus one to one; not contour plots, radar plots, or correlation heat maps
- Purpose: students can read the three figure types and explain how a trend can reverse when groups are pooled, using real field data
- Target duration: 6:30
- Speech rate: 150 wpm
- Language: English
- Materials: examples/penguin-project (raw data, results tables, dataset README)
- Requested by the brief but not supported: "explain that diet causes the different bill shapes" (see evidence file, Gaps)
- Assumptions: classroom use, landscape, captions on; students can pause

## Objectives

| ID | Viewers can … | Topic |
| --- | --- | --- |
| O1 | read a contour plot as a map of where observations are common | T1 |
| O2 | state the pooled relationship between bill length and depth, with its size and sign | T2 |
| O3 | explain why the relationship reverses within species | T3 |
| O4 | read a radar plot of standardized measurements and say which profile drives the pooled trend | T4 |
| O5 | read a correlation heat map and spot the same reversal for bill depth | T5 |

## Topics

| ID | Title | Prerequisites | Takeaway |
| --- | --- | --- | --- |
| T1 | Reading a contour plot | scatter plots | Rings mark equal density; peaks are where birds are common. |
| T2 | The pooled trend | T1, correlation | Pooled, longer bills go with shallower bills: r = −0.24. |
| T3 | Splitting by species | T2 | Within every species the trend is positive; pooling reversed it. |
| T4 | Species profiles | T3 | Gentoos pair long bills with shallow ones; that placement tilts the pooled trend. |
| T5 | Every pair of measurements | T4, correlation | Pooled, bill depth runs negative with everything; within Gentoos every pair is positive. |

## Figure-reading prerequisites

- Contour plot: its own topic (T1), because T2 and T3 argue with it.
- Radar plot and heat map: taught inside T4 and T5 with a full frame step, because each is used
  once and the frame takes one or two sentences.

## Figure inventory

| ID | Existing artifact or data | Decision | Notes |
| --- | --- | --- | --- |
| F01 | raw bill measurements (D04) | new plot from project data | pooled 2D density contour |
| F02 | raw bill measurements (D04); r values (D03); species means (D01) | new plot from project data | same axes as F01, one contour set per species |
| F03 | species_profiles_z.csv (D06) | new plot from project data | radar of z-scores |
| F04 | correlations.csv (D03) | new plot from project data | two heat maps, pooled and Gentoo |

## Visual vocabulary

| Concept | Shape and color role | Used in |
| --- | --- | --- |
| Pooled data | neutral gray contours | F01 |
| Adelie | species 1 color, everywhere | F02, F03 |
| Chinstrap | species 2 color, everywhere | F02, F03 |
| Gentoo | species 3 color, everywhere | F02, F03, F04 label |
| Trend line | thin line in the color of its group; gray when pooled | F01, F02 |
| Negative and positive correlation | cool and warm ends of one diverging scale, pale at zero | F04 |

## Visual brief

- Mood: clean scientific; dark ground; restrained color that is saved for species
- Home visual: a five-item outline strip along the top edge
- Metaphor family: maps and terrain (contour rings as height lines), only where it helps
- Color roles: three species colors, color-blind safe; neutral gray for pooled; one diverging scale
- Topic transition gesture: the outline highlight slides right to the next item

## Pronunciation

| Term | Say as | Note |
| --- | --- | --- |
| Adelie | uh-DAY-lee | |
| Adelies | uh-DAY-leez | plural |
| Gentoo | JEN-too | |
| Gentoos | JEN-tooz | plural |
| Chinstraps | CHIN-straps | |
| Simpson's paradox | SIMP-sunz PARE-uh-docks | |

## Scope exclusions

- Diet, ecology, or evolution as causes of bill shape: no such data in the project (gap).
- Sex differences: in the data, but a second grouping would double the figures.
- Statistical adjustment (for example regression with species as a covariate): not reported by the project.

## Timing

The first draft targeted 5:00. The checker estimated the narration at 746 words, about 5:42
with pauses, and the storyboard at 6:16 once figure holds were added. Options: drop T5 (the heat
map), fold T1 into T2, or extend. T1 is a prerequisite for T2 and T3, and T5 is the only heat
map, so the runtime was extended to 6:30; the audience is a class that can pause. If a hard
five-minute limit applies, cut T5 and keep O1 to O4.
