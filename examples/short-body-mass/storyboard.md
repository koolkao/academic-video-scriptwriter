# Storyboard: Which penguin is the heavy one?

## Figures

### F01 · Body mass by species

- Type: strip plot, one dot per bird, with a mean marker per species
- Data: D04, columns species, body_mass_g; means from D01
- Encodings: x = species (horizontal jitter for visibility only); y = body mass (g); color = species
- Colormap: qualitative, color-blind safe, three species roles
- Reading steps: frame — y axis "Body mass (g)" and three empty species columns; anchor — one Adelie dot lights up with its weight; fill — all dots fall into place column by column; pattern — Gentoo column highlights, other two dim; takeaway — mean markers with values hold
- Claims: C01, C02, C03

### F02 · The Gentoo gap

- Type: interval plot, one estimate with its 95% confidence interval
- Data: D02, row "Welch difference", columns estimate and ci95
- Encodings: x = difference in mean body mass, Gentoo minus Adelie (g); dot = estimate; bar = 95% CI; dashed line = zero difference
- Colormap: estimate in Gentoo color; zero line neutral
- Reading steps: frame — axis and dashed zero line; anchor — the estimate dot; fill — the interval bar grows out from the dot; pattern — cursor visits both ends of the bar, then the zero line; takeaway — the gap between bar and zero holds
- Claims: C05

## Scenes

### S01 · opening

- Narration: puzzle, roadmap
- Look at: the title, then the outline strip
- Focus by: figure
- Stays: nothing yet
- Changes: title fades to the top edge and becomes the outline strip with two items
- Orientation text: "Which penguin is the heavy one?" · "Weight by species" · "The Gentoo gap"
- Motion: build
- Intensity: calm
- Hold: 1s
- Duration: 19s

### S02 · T1

- Narration: announce, introduce, predict
- Topic change: outline item one lights up
- Look at: the empty axes
- Focus by: figure
- Stays: outline strip
- Changes: F01 frame appears: body mass axis and three labeled species columns
- Figure: F01, step frame
- Withheld: every dot; the three species columns stay empty through the guess
- On screen: "n = 342 · 2007–2009"
- Orientation text: "Weight by species"
- Motion: reveal
- Intensity: calm
- Hold: 1s
- Duration: 20s
- Claims: C06

### S03 · T1

- Narration: reveal, explain
- Look at: the dots as they land, then the Gentoo column
- Focus by: figure
- Stays: outline strip, axes, species labels
- Changes: one Adelie dot first, then all dots fill in; Gentoo column then lifts in brightness
- Figure: F01, steps anchor, fill, pattern
- On screen: "Adelie 3700.7 g" · "Chinstrap 3733.1 g" · "Gentoo 5076.0 g"
- Orientation text: "Weight by species"
- Motion: build, highlight
- Intensity: build
- Hold: 1s
- Duration: 16s
- Claims: C01, C02, C03

### S04 · T1

- Narration: wrap-up, bridge
- Look at: the empty space between the Gentoo column and the other two
- Focus by: figure
- Stays: the full F01 plot, outline strip
- Changes: a bracket draws between the Adelie mean and the Gentoo mean
- Figure: F01, step takeaway
- On screen: "Adelie 3700.7 g" · "Gentoo 5076.0 g"
- Orientation text: "Weight by species"
- Motion: draw
- Intensity: peak
- Hold: 2s
- Duration: 11s
- Claims: C01, C03

### S05 · T2

- Narration: announce, introduce, explain
- Topic change: outline highlight slides to item two; the bracket from S04 carries over and turns into F02's estimate
- Look at: the estimate dot
- Focus by: figure
- Stays: outline strip
- Changes: the bracket rotates to horizontal and becomes the estimate on F02's axis; dashed zero line appears
- Figure: F02, steps frame, anchor
- On screen: "+1375 g"
- Orientation text: "The Gentoo gap"
- Motion: transform
- Intensity: build
- Hold: 1s
- Duration: 15s
- Claims: C05

### S06 · T2

- Narration: explain, wrap-up, bridge
- Look at: the low end of the interval and its distance from zero
- Focus by: figure + cursor
- Stays: outline strip, estimate dot, zero line
- Changes: the interval bar grows out from the dot; cursor moves to the low end, then to the zero line
- Figure: F02, steps fill, pattern, takeaway
- On screen: "+1375 g" · "95% CI 1260 to 1491 g"
- Orientation text: "The Gentoo gap"
- Motion: build, move
- Intensity: peak
- Hold: 3s
- Duration: 21s
- Claims: C05

### S07 · conclusion

- Narration: synthesis, reveal
- Topic change: both outline items lit; F01 and F02 side by side
- Look at: the two figures together
- Focus by: figure
- Stays: outline strip with both items lit
- Changes: F01 shrinks to the left and F02 sits beside it
- Figure: F01, F02, step takeaway
- On screen: "Adelie 3700.7 g" · "Chinstrap 3733.1 g" · "+1375 g, 95% CI 1260 to 1491 g"
- Orientation text: "Weight by species" · "The Gentoo gap"
- Motion: compare
- Intensity: calm
- Hold: 2s
- Duration: 13s
- Claims: C01, C02, C05
