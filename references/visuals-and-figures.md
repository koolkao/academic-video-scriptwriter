# Visuals and figures

The aim is visuals that look like serious science and still never leave the viewer lost. The
storyboard describes what the viewer should see and understand, and leaves the implementation
to whichever tool produces the video. Name intent and observable behavior; do not write code,
pixel coordinates, easing curves, or tool names unless the user asks.

## One focus of attention, always

Every scene names exactly one thing the eye should be on (`Look at`) and how the viewer is led
there (`Focus by`).

- **`figure`**: the visual itself leads. The target is highlighted, enlarged, or animated while
  everything else dims, desaturates, or holds still. This is the default.
- **`cursor`**: a large, high-contrast pointer moves to the target. Use it when the target is
  small, when several similar elements compete (one cell in a heat map, one contour line), or
  when the figure must stay unaltered (a published figure reused as-is).
- **`figure + cursor`**: both, for dense figures.

Cursor rules:

1. It moves to the target just before the narration names it, so the eye arrives as the word
   does.
2. It holds still while the narration talks about that target.
3. It takes direct paths and never drifts, circles, or idles on screen.
4. It leaves, or fades, when the scene's focus moves to the whole figure.

If you cannot name one focus for a scene, the scene is doing two things. Split it.

## Orientation on screen

- **Home visual.** Pick one visual that stands for the whole outline: an outline strip, a map,
  or a master diagram whose regions are the topics. Each topic zooms into its region; each
  wrap-up pulls back out. The roadmap becomes something to look at, not a list.
- **Persistent context.** `Stays` lists what remains on screen through a scene: axes, legend,
  outline strip, the previous step of a build. Removing context the viewer still needs is a
  defect, even if it looks cleaner.
- **One change at a time.** `Changes` lists the single thing that moves or appears. Two
  simultaneous changes split attention.
- **Topic transitions look the same every time.** Use one recognizable gesture for every topic
  change (the outline highlight slides to the next item, the heading changes). Consistency is
  what makes it readable. Save spectacle for the content.

## Holding back the answer

When the narration asks the viewer to predict, the screen must not give the answer away. The
scene's `Withheld` field says what stays hidden (the species colors, the last row of the heat
map, the trend line), and the figure holds still through the thinking pause. The reveal is
the next change, and often the topic's showpiece.

## Visual vocabulary

The teaching plan fixes, for the whole video, the shape and color role of each recurring
concept: "each species has one color, used in every figure"; "the outline strip is always at the
top." A viewer who learns an encoding once should never have to relearn it. Color roles are
named (`species A`, `highlight`, `muted context`), not given as hex values; the production tool
chooses the palette.

## Impressive, placed on the insight

Each topic gets at most one showpiece: the moment where the figure does something striking
because the idea just clicked. The contour plot splits into three islands that each tilt
upward; the 3D reconstruction rotates to reveal the structure the narration just described. Put
it at the wrap-up or at the turn of the explanation, never on an announcement or a transition.
Mark it `Intensity: peak`. Most scenes are `calm` or `build`.

## Motion verbs

The storyboard names what a change means, not how it is animated. Each tool draws it its own
way.

| Verb | Meaning |
| --- | --- |
| `build` | Add the next piece to something already on screen. |
| `reveal` | Show something that was hidden. |
| `highlight` / `dim` | Raise one element, lower the rest. |
| `trace` | Follow a path, line, or contour with the eye. |
| `split` / `merge` | One group becomes several, or several become one. |
| `transform` | One representation becomes another (scatter to density, raw to normalized). |
| `compare` | Place two things side by side, aligned on the same scale. |
| `zoom in` / `pull back` | Move into a region of the home visual, or back out to the whole. |
| `rotate` | Turn a 3D view about one axis. |
| `draw` | A line, arrow, or annotation appears stroke by stroke. |
| `move` | The cursor or an element travels to a new place. |
| `fade` / `cut` / `hold` | Leave gradually, change instantly, stay still. |

## Building a complex figure

Experts read a complex figure in a fixed order. Build it on screen in that order, one step per
narration beat. Each figure's `Reading steps` lists all five; each scene names which step it shows.

1. **frame**: axes, units, and what each encoding means (color, size, height, contour level),
   before any data. "Across: bill length. Up: bill depth. Darker means more birds."
2. **anchor**: one concrete element, read in full. "This cell is Gentoo flipper length against
   body mass: point seven."
3. **fill**: the rest of the data arrives.
4. **pattern**: the structure that matters is highlighted; everything else dims.
5. **takeaway**: the figure holds while the conclusion is spoken. The showpiece goes here.

An expert audience may combine frame and anchor in one beat. A novice audience may need a short
figure-reading topic first (see `instructional-structure.md`).

## Figure families

Use the figure the data and the claim call for. Academic figures are welcome; each needs the
build order above.

| Family | Good for | Watch for |
| --- | --- | --- |
| Heat map, correlation matrix | Many pairwise values at once | Diverging colormap centered on zero for signed values; label the scale; anchor one cell first. |
| Contour plot, 2D density | Where observations concentrate in two variables | Explain what a contour line means before the data arrive; keep the levels the same across panels. |
| Radar (spider) plot | Profiles across several standardized measures | Axes must share a scale (state it, for example z-scores); keep axis order fixed; at most three or four profiles. |
| 3D reconstruction, surface | Spatial structure | See *3D* below. |
| Violin, box, strip plot | Distributions by group | Show the points when n is small; say what the box or width means. |
| Forest plot, interval plot | Estimates with confidence intervals | Mark the no-effect line; read one row in full first. |
| Survival or cumulative curve | Time to event | Say what a drop means; show numbers at risk if the project reported them. |
| Volcano, Manhattan plot | Many tests at once | Explain both axes and the threshold lines before highlighting hits. |
| Network, pathway | Relationships | Build node by node; fix positions so nodes do not jump. |
| Scatter, line, bar | Simple relationships | Fine when they fit; do not upgrade a figure just to look advanced. |

### Colormaps and encodings

- Sequential data: a perceptually uniform colormap (viridis, cividis, or similar). Never
  rainbow or "jet," which invents boundaries.
- Signed data: a diverging colormap with its neutral color at zero.
- Categories: a color-blind-safe qualitative palette; never rely on red versus green alone.
- Keep each encoding the same across all figures in the video.

### 3D

A rotating 3D view is the fastest way to lose a viewer. To keep it readable:

- Keep a small orientation marker (x, y, z axes or anatomical directions) in one corner.
- One camera move at a time, about one axis, followed by a hold.
- Say where we are looking from before moving ("from above," "now from the side").
- Return to a home view between explorations.

## Showing statistics

On screen, a statistic carries its context: estimate, interval, sample size, and test where the
project reported them. Keep each in the same place and format throughout. Spoken form is
covered in `narration-and-tts.md`.

## Pacing the visuals

- Visual stability serves comprehension. Do not change the picture every few seconds for
  novelty; change it when the explanation moves.
- Allow reading time: `Hold` gives the seconds a scene must stay still after its last change.
  Dense figures need more.
- Reveal each piece when the narration reaches it, not before. A full figure dumped on screen
  ahead of the narration makes viewers read instead of listen.

## Accessibility

- Captions for all narration (the production handoff notes this).
- Text large enough to read on a phone; avoid text blocks that compete with speech.
- Color-blind-safe palettes, and a second cue (shape, position, label) for every color
  distinction that matters.
- Essential visual relationships are also spoken.
- Note any remaining accessibility needs in the handoff.

## The visual brief

The teaching plan's visual brief sets mood ("clean scientific, dark background, restrained
color"), the family of metaphors to draw from, and the meaning of each color role. It does not
pick fonts, hex values, or a tool. Two different tools should be able to produce recognizably
the same video from it.
