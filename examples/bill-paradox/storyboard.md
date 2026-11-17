# Storyboard: Longer bills, shallower bills?

## Figures

### F01 · Pooled bill length against bill depth

- Type: filled contour plot, 2D kernel density of all birds
- Data: D04, columns bill_length_mm, bill_depth_mm (rows with both present)
- Encodings: x = bill length (mm); y = bill depth (mm); ring = equal density; darker fill = more birds; gray line = least-squares trend line drawn by the plotting step (no slope printed; its downward direction matches C02)
- Colormap: sequential, perceptually uniform, single neutral hue
- Reading steps: frame — axes with units, no data; anchor — one ring drawn alone and traced by the cursor; fill — all rings fill in; pattern — gray trend line draws left to right, downward; takeaway — r label holds beside the line
- Claims: C02

### F02 · The same axes, split by species

- Type: three filled contour sets on F01's axes, same density levels, one per species, each with its own trend line
- Data: D04, columns species, bill_length_mm, bill_depth_mm; r from D03; centers from D01
- Encodings: as F01; color = species; colored line = within-species least-squares trend line (no slope printed; upward, matching C03 to C05)
- Colormap: qualitative, color-blind safe, the three species roles
- Reading steps: frame — F01 stays, gray contours ready to split; anchor — one species island lit; fill — all three islands in their colors; pattern — three upward trend lines draw, the gray pooled line remains faintly; takeaway — three r labels beside three upward lines, the faint downward line between them
- Claims: C03, C04, C05, C11

### F03 · Species profiles

- Type: radar plot, four spokes, three overlaid profiles
- Data: D06, all rows
- Encodings: spoke = measurement (bill length, bill depth, flipper length, body mass, fixed order); distance from center = z-score against the pooled mean and SD; middle ring = 0; color = species
- Colormap: the three species roles
- Reading steps: frame — empty spokes, labeled, with rings at minus one, zero, and plus one SD; anchor — Gentoo profile alone; fill — Adelie and Chinstrap profiles join; pattern — Gentoo bill depth spoke highlighted against Adelie bill depth; takeaway — the two opposed bill profiles hold
- Claims: C06, C07, C08

### F04 · Correlation heat maps, pooled and Gentoo

- Type: two 4 × 4 correlation heat maps side by side, lower triangle only, values printed in cells
- Data: D03, rows group = all and group = Gentoo
- Encodings: row and column = measurement, same order as F03; cell color = Pearson r on a diverging scale from −1 to 1, pale at 0
- Colormap: diverging, cool for negative, warm for positive, color-blind safe
- Reading steps: frame — empty pooled grid with row and column labels and the color scale; anchor — flipper length × body mass cell; fill — all pooled cells; pattern — the bill depth row highlighted; takeaway — the Gentoo grid slides in beside it, every cell warm
- Claims: C09, C10

## Scenes

### S01 · opening

- Narration: hook, goal, roadmap
- Look at: the gray contour plot, then the outline strip
- Focus by: figure
- Stays: nothing yet
- Changes: F01 appears faintly behind the title, then the title moves up and becomes the five-item outline strip
- On screen: "n = 342"
- Orientation text: "Longer bills, shallower bills?" · "Reading a contour plot" · "The pooled trend" · "Splitting by species" · "Species profiles" · "Every pair of measurements"
- Motion: build
- Intensity: calm
- Hold: 1s
- Duration: 36s
- Claims: C01

### S02 · T1

- Narration: announce, introduce
- Topic change: outline item one lights up; F01 clears to empty axes
- Look at: the empty axes
- Focus by: figure
- Stays: outline strip
- Changes: F01 clears to its frame
- Figure: F01, step frame
- Orientation text: "1 · Reading a contour plot"
- Motion: reveal
- Intensity: calm
- Hold: 1s
- Duration: 15s

### S03 · T1

- Narration: explain
- Look at: the axis labels, then one ring
- Focus by: figure + cursor
- Stays: outline strip, axes, axis labels
- Changes: axis labels light in turn; one ring draws; the cursor traces it; then all rings fill
- Figure: F01, steps frame, anchor, fill
- Orientation text: "1 · Reading a contour plot"
- Motion: highlight, trace, build
- Intensity: build
- Hold: 2s
- Duration: 26s

### S04 · T1

- Narration: wrap-up, bridge
- Look at: the tallest peak
- Focus by: figure
- Stays: outline strip, the full contour plot
- Changes: the peak brightens; the rest dims slightly
- Figure: F01, step fill
- Orientation text: "1 · Reading a contour plot"
- Motion: highlight
- Intensity: calm
- Hold: 2s
- Duration: 23s

### S05 · T2

- Narration: announce, introduce
- Topic change: outline highlight slides to item two; the plot stays
- Look at: the outline strip, then the whole plot
- Focus by: figure
- Stays: outline strip, F01
- Changes: chapter heading changes
- Figure: F01, step fill
- Orientation text: "2 · The pooled trend"
- Motion: hold
- Intensity: calm
- Hold: 1s
- Duration: 9s

### S06 · T2

- Narration: explain
- Look at: the gray trend line as it draws
- Focus by: figure
- Stays: outline strip, F01
- Changes: the pooled trend line draws left to right, downward; the r label appears
- Figure: F01, step pattern
- On screen: "r = −0.24 · n = 342 · p < 0.001"
- Orientation text: "2 · The pooled trend"
- Motion: draw
- Intensity: build
- Hold: 2s
- Duration: 20s
- Claims: C02

### S07 · T2

- Narration: wrap-up, bridge
- Look at: the downward line
- Focus by: figure
- Stays: outline strip, F01, r label
- Changes: everything but the line and label dims
- Figure: F01, step takeaway
- On screen: "r = −0.24"
- Orientation text: "2 · The pooled trend"
- Motion: dim
- Intensity: calm
- Hold: 2s
- Duration: 18s
- Claims: C02

### S08 · T3

- Narration: announce, introduce, explain, predict
- Topic change: outline highlight slides to item three; the same axes stay, and the chapter heading changes
- Look at: the gray contours, about to split
- Focus by: figure
- Stays: outline strip, axes, faint pooled line
- Changes: chapter heading changes; the gray contours shimmer once to signal the split
- Figure: F02, step frame
- Withheld: species colors and the within-species trend lines; the contours stay gray and still through the question
- Orientation text: "3 · Splitting by species"
- Motion: hold
- Intensity: calm
- Hold: 1s
- Duration: 34s

### S09 · T3

- Narration: reveal, explain
- Look at: each island as it is named
- Focus by: figure
- Stays: outline strip, axes, faint pooled line
- Changes: the gray landscape splits into three colored islands, lit one at a time as each is named
- Figure: F02, steps anchor, fill
- On screen: "Adelie 38.8 mm, 18.3 mm" · "Chinstrap 48.8 mm, 18.4 mm" · "Gentoo 47.5 mm, 15.0 mm"
- Orientation text: "3 · Splitting by species"
- Motion: split
- Intensity: peak
- Hold: 2s
- Duration: 19s
- Claims: C11

### S10 · T3

- Narration: reveal, explain
- Look at: each upward trend line in turn
- Focus by: figure
- Stays: outline strip, three islands, faint pooled line
- Changes: three within-species trend lines draw upward, one per island, each with its r label
- Figure: F02, step pattern
- On screen: "Adelie r = 0.39 · n = 151" · "Chinstrap r = 0.65 · n = 68" · "Gentoo r = 0.64 · n = 123" · "each p < 0.001"
- Orientation text: "3 · Splitting by species"
- Motion: draw
- Intensity: build
- Hold: 2s
- Duration: 20s
- Claims: C03, C04, C05

### S11 · T3

- Narration: wrap-up, bridge
- Look at: three upward lines against the one faint downward line
- Focus by: figure
- Stays: outline strip, F02 with all labels
- Changes: the faint pooled line brightens briefly so both directions show at once; the name appears
- Figure: F02, step takeaway
- On screen: "r = 0.39" · "r = 0.65" · "r = 0.64"
- Orientation text: "3 · Splitting by species" · "Simpson's paradox"
- Motion: highlight
- Intensity: peak
- Hold: 2s
- Duration: 23s
- Claims: C03, C04, C05

### S12 · T4

- Narration: announce, introduce, explain
- Topic change: outline highlight slides to item four; F02 pulls back and the radar frame replaces it
- Look at: each spoke as it is named, then the middle ring
- Focus by: figure + cursor
- Stays: outline strip
- Changes: the empty radar draws spoke by spoke; the cursor visits the middle ring
- Figure: F03, step frame
- Orientation text: "4 · Species profiles"
- Motion: pull back, build
- Intensity: calm
- Hold: 3s
- Duration: 28s

### S13 · T4

- Narration: explain
- Look at: the Gentoo bill depth spoke, then the other profiles
- Focus by: figure + cursor
- Stays: outline strip, radar frame
- Changes: Gentoo profile draws; cursor moves to its bill depth point; Adelie and Chinstrap profiles join
- Figure: F03, steps anchor, fill
- On screen: "Gentoo bill depth −1.1 SD" · "flipper +1.16" · "mass +1.09"
- Orientation text: "4 · Species profiles"
- Motion: draw, move
- Intensity: build
- Hold: 2s
- Duration: 22s
- Claims: C06, C07, C08

### S14 · T4

- Narration: wrap-up, bridge
- Look at: the Gentoo and Adelie bill points, opposite each other
- Focus by: figure
- Stays: outline strip, all three profiles
- Changes: Chinstrap profile dims; Gentoo and Adelie bill-depth points pulse once
- Figure: F03, steps pattern, takeaway
- On screen: "Gentoo bill depth −1.1" · "Adelie bill depth 0.61"
- Orientation text: "4 · Species profiles"
- Motion: highlight
- Intensity: peak
- Hold: 2s
- Duration: 24s
- Claims: C06, C08

### S15 · T5

- Narration: announce, introduce, explain
- Topic change: outline highlight slides to item five; the radar pulls back and the pooled grid frame appears
- Look at: the color scale, then the empty grid
- Focus by: figure
- Stays: outline strip
- Changes: empty pooled grid with labels and the diverging color scale appears
- Figure: F04, step frame
- Orientation text: "5 · Every pair of measurements"
- Motion: reveal
- Intensity: calm
- Hold: 2s
- Duration: 18s
- Claims: C09

### S16 · T5

- Narration: explain, predict
- Look at: the flipper length by body mass cell, then the bill depth row
- Focus by: figure + cursor
- Stays: outline strip, pooled grid, color scale
- Changes: the cursor lands on one cell, which fills; all cells fill; the bill depth row highlights
- Figure: F04, steps anchor, fill, pattern
- Withheld: the Gentoo grid; the pooled grid holds still with the bill depth row lit through the question
- On screen: "0.87" · "−0.24" · "−0.58" · "−0.47" · "0.66" · "0.6"
- Orientation text: "5 · Every pair of measurements"
- Motion: move, build, highlight
- Intensity: build
- Hold: 2s
- Duration: 29s
- Claims: C09

### S17 · T5

- Narration: reveal, wrap-up, bridge
- Look at: the Gentoo grid, all warm
- Focus by: figure
- Stays: outline strip, pooled grid
- Changes: the Gentoo grid slides in beside the pooled grid and its cells fill warm
- Figure: F04, step takeaway
- On screen: "Gentoo only" · "0.64 to 0.72"
- Orientation text: "5 · Every pair of measurements"
- Motion: compare
- Intensity: peak
- Hold: 3s
- Duration: 28s
- Claims: C10

### S18 · conclusion

- Narration: synthesis, reveal, unknown
- Topic change: all five outline items light; one small panel per topic lines up beneath them
- Look at: each panel as the narration reaches it
- Focus by: figure
- Stays: outline strip, fully lit
- Changes: the five panels light in turn, from left to right; on the unknown line, an empty sixth slot labeled "diet: not measured" appears and stays
- Figure: F01, F02, F03, F04, step takeaway
- On screen: "pooled r = −0.24" · "within species r = 0.39, 0.65, 0.64" · "n = 342 · 2007–2009"
- Orientation text: "Reading a contour plot" · "The pooled trend" · "Splitting by species" · "Species profiles" · "Every pair of measurements" · "diet: not measured"
- Motion: build
- Intensity: calm
- Hold: 3s
- Duration: 56s
- Claims: C01, C02, C03, C04, C05, C08, C10
