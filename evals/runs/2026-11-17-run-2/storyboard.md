# Storyboard: Longer bills, shallower bills?

## Figures

### F01 · Bill length against bill depth

- Type: scatter plot with least-squares trend lines (pooled, then one per species)
- Data: D01, columns bill_length_mm, bill_depth_mm, species; rows missing either bill measure dropped (342 rows, matching D02). Trend lines are ordinary least squares drawn while plotting; no slope or intercept is printed or spoken. Their directions match the reported signs of r (pooled negative, each species positive).
- Encodings: x = bill length (mm); y = bill depth (mm); color + marker shape = species (circle Adelie, triangle Chinstrap, square Gentoo); thick neutral line = pooled trend; thin species-colored lines = within-species trends
- Colormap: qualitative, color-blind safe, each species paired with a marker shape; muted context color for unsorted dots
- Reading steps: frame — axes "Bill length (mm)" across and "Bill depth (mm)" up, no data; anchor — one gray dot lights, read as "one bird"; fill — all 342 gray dots, then the pooled line draws; pattern — dots split into species colors and three species lines draw; takeaway — cluster centers labeled, pooled and species lines held together
- Claims: C01, C02, C04, C05, C06, C07, C08, C09

## Scenes

### S01 · opening

- Narration: puzzle, hook, goal
- Look at: the downward pooled line
- Focus by: figure
- Stays: nothing yet (first scene)
- Changes: labeled axes and gray dots fade in together (a preview; S03 deliberately clears and rebuilds the figure step by step); then the pooled line draws, tilting down
- Figure: F01, step fill
- Withheld: species colors and species lines (the answer to the opening puzzle)
- On screen: "n = 342"
- Orientation text: "Longer bills, shallower bills?" · "Bill length (mm)" · "Bill depth (mm)"
- Motion: draw
- Intensity: build
- Hold: 1s
- Duration: 18s
- Claims: C01, C02

### S02 · opening

- Narration: roadmap
- Look at: the outline strip
- Focus by: figure
- Stays: F01 dimmed to muted context in the background
- Changes: outline strip builds at the top, one item per spoken title
- Orientation text: "1 · The pooled trend" · "2 · Within each species"
- Motion: build
- Intensity: calm
- Hold: 1s
- Duration: 6s

### S03 · T1

- Narration: announce, introduce, explain
- Topic change: outline highlight slides onto item 1; chapter heading reads "The pooled trend"
- Look at: the two axes, then one lit dot
- Focus by: figure
- Stays: outline strip with item 1 lit
- Changes: dots and line clear; axes draw on cue ("bill length", then "bill depth"); then one gray dot appears and lights
- Figure: F01, steps frame and anchor
- On screen: "Palmer Archipelago · 2007–2009"
- Orientation text: "1 · The pooled trend"
- Motion: build
- Intensity: calm
- Hold: 2s
- Duration: 20s
- Claims: C10

### S04 · T1

- Narration: explain
- Topic change: no
- Look at: the pooled trend line
- Focus by: figure
- Stays: axes, axis labels, outline strip with item 1 lit
- Changes: all gray dots fill in; then the pooled line draws; then the statistics block appears
- Figure: F01, step fill
- On screen: "r = −0.24" · "n = 342" · "p = 1.1e-05"
- Orientation text: "1 · The pooled trend"
- Motion: build
- Intensity: build
- Hold: 2s
- Duration: 15s
- Claims: C01, C02

### S05 · T1

- Narration: wrap-up, bridge
- Topic change: no
- Look at: the pooled line
- Focus by: figure
- Stays: axes, gray dots, pooled line, statistics block, outline strip with item 1 lit
- Changes: dots dim slightly so the line stands alone; takeaway heading appears
- Figure: F01, step takeaway (for T1)
- On screen: "r = −0.24" · "n = 342"
- Orientation text: "Pooled: longer bills, shallower bills"
- Motion: highlight
- Intensity: peak
- Hold: 2s
- Duration: 14s
- Claims: C01, C02

### S06 · T2

- Narration: announce, introduce, explain, predict
- Topic change: outline highlight slides to item 2; chapter heading reads "Within each species"; figure stays
- Look at: the two hypothesis arrows, then the gray dot cloud during the thinking pause
- Focus by: figure
- Stays: axes, gray dots, pooled line, outline strip with item 2 lit
- Changes: two short labeled arrows appear beside the plot on cue, "trade-off → down" then "bigger is bigger → up"; then the figure holds still through the thinking pause
- Figure: F01, step fill
- Withheld: species colors and species lines; dots stay gray
- On screen: "Adelie · Chinstrap · Gentoo"
- Orientation text: "2 · Within each species"
- Motion: build
- Intensity: build
- Hold: 4s
- Duration: 28s
- Claims: C03

### S07 · T2

- Narration: reveal, explain
- Topic change: no
- Look at: the three species lines
- Focus by: figure
- Stays: axes, pooled line (dimmed), outline strip with item 2 lit
- Changes: gray dots split into the three species colors; then each species line draws, tilting up, with its r label
- Figure: F01, step pattern
- On screen: "Adelie r = 0.39 · n = 151" · "Chinstrap r = 0.65 · n = 68" · "Gentoo r = 0.64 · n = 123"
- Orientation text: "2 · Within each species"
- Motion: split
- Intensity: peak
- Hold: 3s
- Duration: 15s
- Claims: C04, C05, C06

### S08 · T2

- Narration: explain
- Topic change: no
- Look at: each species cluster in turn, then the pooled line
- Focus by: figure + cursor
- Stays: axes, species-colored dots, species lines, pooled line, outline strip with item 2 lit
- Changes: cursor moves to the Adelie cluster and its mean label appears; then Chinstrap; then Gentoo; then cursor traces the pooled line from upper left to lower right and leaves
- Figure: F01, step takeaway
- On screen: "Adelie 38.8 mm · 18.3 mm" · "Chinstrap 48.8 mm · 18.4 mm" · "Gentoo 47.5 mm · 15.0 mm"
- Orientation text: "2 · Within each species"
- Motion: trace
- Intensity: build
- Hold: 2s
- Duration: 26s
- Claims: C07, C08, C09

### S09 · T2

- Narration: wrap-up, bridge
- Topic change: no
- Look at: the takeaway heading over the held figure
- Focus by: figure
- Stays: full F01 with species colors, all lines, outline strip with item 2 lit
- Changes: takeaway heading appears, then the term "Simpson's paradox" beneath it
- Figure: F01, step takeaway
- Orientation text: "Within each species, the trend reverses" · "Simpson's paradox"
- Motion: hold
- Intensity: calm
- Hold: 2s
- Duration: 17s
- Claims: C04, C05, C06

### S10 · conclusion

- Narration: synthesis, reveal, unknown
- Topic change: both outline items light together; heading reads "Both are true"
- Look at: pooled line and species lines side by side
- Focus by: figure
- Stays: full F01, outline strip fully lit
- Changes: pooled line and the three species lines brighten together; then the Gentoo cluster highlights on "Gentoos"
- Figure: F01, step takeaway
- On screen: "pooled r = −0.24" · "within species r = 0.39 · 0.65 · 0.64" · "Gentoo bill depth 15.0 mm"
- Orientation text: "1 · The pooled trend" · "2 · Within each species"
- Motion: highlight
- Intensity: calm
- Hold: 3s
- Duration: 29s
- Claims: C01, C04, C05, C06, C08
