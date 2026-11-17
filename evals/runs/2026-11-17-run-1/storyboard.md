# Storyboard: One trend pooled, another within species

## Figures

### F01 · Pooled bill length against bill depth

- Type: scatter plot, all birds in one color
- Data: D01, columns bill_length_mm, bill_depth_mm (342 rows with both values; 2 rows with NA left out)
- Encodings: x = bill length (mm); y = bill depth (mm); one dot = one bird; color = muted context (species not shown)
- Colormap: none; single muted color
- Reading steps: frame — axes, units, "one dot = one bird"; anchor — none needed for this familiar figure type, the axes are read in full at frame; fill — all 342 dots appear; pattern — the cloud's gentle downward tilt and the r readout; takeaway — hold with readout "r = −0.24"
- Claims: C01

### F02 · Bill length against bill depth by species

- Type: scatter plot recolored by species, then split into three small-multiple panels on identical axes; large species-mean markers
- Data: D01, columns bill_length_mm, bill_depth_mm, species; D03, species means of bill_length_mm and bill_depth_mm; D02, within-species r
- Encodings: x = bill length (mm); y = bill depth (mm); color + shape = species (Adelie circle, Chinstrap triangle, Gentoo square); enlarged outlined marker = species mean
- Colormap: qualitative, color-blind safe, each species also has its own shape
- Reading steps: frame — same axes as F01, legend of three species; anchor — the Adelie panel with its readout; fill — Chinstrap and Gentoo panels; pattern — each panel's upward tilt, then the three species means on one shared plot; takeaway — means highlighted on the pooled cloud, showing the between-species gap that makes the pooled tilt negative
- Claims: C02, C03, C04, C05

### F03 · Mean body mass, Gentoo and Chinstrap

- Type: bar chart with SD whiskers, two bars
- Data: D03, rows body_mass_g for Gentoo and Chinstrap
- Encodings: x = species; y = mean body mass (g), axis starting at zero; whisker = ±1 SD; label = mean, SD, n
- Colormap: species C and species B colors from F02
- Reading steps: frame — axis "mean body mass (g)" from zero; anchor — Gentoo bar with its label; fill — Chinstrap bar; pattern — compare heights; takeaway — hold both labels
- Claims: C06

## Scenes

### S01 · opening

- Narration: goal, roadmap
- Look at: the outline strip
- Focus by: figure
- Stays: title card
- Changes: outline strip builds its two items as the roadmap names them
- Orientation text: "1 · The pooled trend" · "2 · Within each species"
- Motion: build
- Intensity: calm
- Hold: 1s
- Duration: 17s

### S02 · T1

- Narration: announce, introduce
- Topic change: outline highlight lights item 1; chapter heading "The pooled trend"
- Look at: the sample line under the heading
- Focus by: figure
- Stays: outline strip with item 1 lit
- Changes: sample line appears
- On screen: "342 penguins · 3 species · 3 islands, Palmer Archipelago · 2007–2009"
- Orientation text: "1 · The pooled trend"
- Motion: reveal
- Intensity: calm
- Hold: 2s
- Duration: 20s
- Claims: C07

### S03 · T1

- Narration: explain
- Look at: each axis as it is named, then the dots
- Focus by: figure + cursor
- Stays: outline strip with item 1 lit
- Changes: axes draw, then all dots fade in gray (cursor points to x axis, then y axis, then leaves)
- Figure: F01, steps frame and fill
- On screen: "bill length (mm)" · "bill depth (mm)"
- Orientation text: "1 · The pooled trend"
- Motion: draw
- Intensity: calm
- Hold: 1s
- Duration: 15s
- Claims: C01

### S04 · T1

- Narration: explain
- Look at: the overall tilt of the cloud, then the r readout
- Focus by: figure
- Stays: axes, all gray dots, outline strip with item 1 lit
- Changes: r readout appears in the top-right corner
- Figure: F01, step pattern
- On screen: "r = −0.24 · n = 342 · p = 1.1 × 10⁻⁵"
- Orientation text: "1 · The pooled trend"
- Motion: reveal
- Intensity: build
- Hold: 2s
- Duration: 9s
- Claims: C01

### S05 · T1

- Narration: wrap-up, bridge
- Look at: the r readout
- Focus by: figure
- Stays: axes, gray dots, readout, outline strip with item 1 lit
- Changes: takeaway heading "Pooled: longer bills, slightly shallower" appears
- Figure: F01, step takeaway
- On screen: "r = −0.24"
- Orientation text: "1 · The pooled trend"
- Motion: hold
- Intensity: calm
- Hold: 1s
- Duration: 13s
- Claims: C01

### S06 · T2

- Narration: announce, introduce
- Topic change: outline highlight slides to item 2; chapter heading "Within each species"; the same scatter stays on screen
- Look at: the dots as they take species color and shape
- Focus by: figure
- Stays: axes, all dots, outline strip
- Changes: dots recolor by species and the legend appears
- Figure: F02, step frame
- On screen: "Adelie · Chinstrap · Gentoo"
- Orientation text: "2 · Within each species"
- Motion: transform
- Intensity: build
- Hold: 1s
- Duration: 10s

### S07 · T2

- Narration: explain
- Look at: the Adelie panel and its readout
- Focus by: figure
- Stays: axes, legend, outline strip with item 2 lit
- Changes: the cloud splits into three panels; Adelie panel is lit, the other two dimmed; Adelie readout appears
- Figure: F02, step anchor
- On screen: "Adelie · r = 0.39 · n = 151 · p = 6.7 × 10⁻⁷"
- Orientation text: "2 · Within each species"
- Motion: split
- Intensity: build
- Hold: 2s
- Duration: 9s
- Claims: C02

### S08 · T2

- Narration: explain
- Look at: each remaining panel's readout as it is named
- Focus by: figure
- Stays: three panels on identical axes, Adelie readout, legend, outline strip with item 2 lit
- Changes: Chinstrap then Gentoo panels light with their readouts
- Figure: F02, step fill
- On screen: "Chinstrap · r = 0.65 · n = 68 · p = 1.5 × 10⁻⁹" · "Gentoo · r = 0.64 · n = 123 · p = 1.0 × 10⁻¹⁵"
- Orientation text: "2 · Within each species"
- Motion: highlight
- Intensity: build
- Hold: 2s
- Duration: 9s
- Claims: C03, C04

### S09 · T2

- Narration: explain
- Look at: the three positive readouts side by side
- Focus by: figure
- Stays: three panels, all readouts, outline strip with item 2 lit
- Changes: small heading "within: r > 0 in every species" appears, with the pooled readout "r = −0.24" shown faded beside it for contrast
- Figure: F02, step pattern
- On screen: "r = 0.39" · "r = 0.65" · "r = 0.64" · "pooled r = −0.24"
- Orientation text: "2 · Within each species"
- Motion: compare
- Intensity: build
- Hold: 1s
- Duration: 7s
- Claims: C01, C02, C03, C04

### S10 · T2

- Narration: explain
- Look at: the three species-mean markers, one at a time as each is named
- Focus by: figure + cursor
- Stays: axes, legend, outline strip with item 2 lit
- Changes: panels merge back into one colored plot; each species mean marker appears with its label as named; the dots dim to 30 percent so the markers carry the scene
- Figure: F02, step takeaway
- On screen: "Adelie mean · 38.8 mm, 18.3 mm" · "Gentoo mean · 47.5 mm, 15.0 mm" · "Chinstrap mean · 48.8 mm, 18.4 mm"
- Orientation text: "2 · Within each species"
- Motion: merge
- Intensity: peak
- Hold: 2s
- Duration: 30s
- Claims: C05

### S11 · T2

- Narration: explain
- Look at: the Gentoo bar, then the Chinstrap bar
- Focus by: figure
- Stays: species colors and shapes, outline strip with item 2 lit
- Changes: bar chart replaces the scatter
- Figure: F03, steps anchor, fill, pattern
- On screen: "Gentoo · 5076.0 g · SD 504.1 · n = 123" · "Chinstrap · 3733.1 g · SD 384.3 · n = 68"
- Orientation text: "2 · Within each species"
- Motion: compare
- Intensity: calm
- Hold: 2s
- Duration: 13s
- Claims: C06

### S12 · T2

- Narration: wrap-up, bridge
- Look at: the takeaway heading over the scatter
- Focus by: figure
- Stays: the merged species scatter with means, outline strip with item 2 lit
- Changes: scatter returns; heading "Within each species, the trend reverses" appears, then the term "Simpson's paradox" below it
- Figure: F02, step takeaway
- On screen: "r = 0.39 · 0.65 · 0.64" · "pooled r = −0.24"
- Orientation text: "2 · Within each species"
- Motion: reveal
- Intensity: calm
- Hold: 2s
- Duration: 24s
- Claims: C01, C02, C03, C04

### S13 · conclusion

- Narration: synthesis
- Topic change: outline strip lights both items together; chapter heading "Conclusion"
- Look at: the two readouts, pooled and within, side by side
- Focus by: figure
- Stays: outline strip, both items lit
- Changes: F01 (gray) and F02 (colored, merged) sit side by side on matched axes
- Figure: F01, step takeaway; F02, step takeaway
- On screen: "pooled r = −0.24" · "within r = 0.39 · 0.65 · 0.64"
- Orientation text: "1 · The pooled trend" · "2 · Within each species"
- Motion: compare
- Intensity: calm
- Hold: 2s
- Duration: 21s
- Claims: C01, C02, C03, C04
