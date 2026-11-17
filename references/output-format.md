# Output format

The four output files use a small, fixed markup so that a person can read them and
`scripts/check_outputs.py` can check them. Copy the files in `templates/` and keep their
headings and field names exactly. Everything else is free prose.

## Identifiers

| Prefix | Meaning | Example | Defined in |
| --- | --- | --- | --- |
| `O` | Learning objective | `O2` | teaching-plan.md, Objectives table |
| `T` | Topic (a stable outline item) | `T3` | teaching-plan.md, Topics table |
| `S` | Scene (a visual unit) | `S07` | storyboard.md, `### S07 · …` |
| `F` | Figure | `F02` | storyboard.md, `### F02 · …` |
| `C` | Claim (anything factual, including every number) | `C05` | evidence-and-review.md, Claims table |
| `D` | Data source (a file the project already produced) | `D01` | evidence-and-review.md, Data sources table |

`opening` and `conclusion` are reserved topic values for the first and last sections.

## teaching-plan.md

- `## Brief` holds `- Key: value` lines. The checker reads `Target duration` (`m:ss` or `Ns`),
  `Speech rate` (`N wpm`; default 150), and `Engagement` (default full; `reduced, because …`).
- `## Puzzle`: the opening question, the claims it rests on, and where the conclusion answers it.
- `## Objectives` table: `| ID | Viewers can … | Topic |`.
- `## Topics` table: `| ID | Title | Prerequisites | Takeaway |`, in outline order. The
  Title is the spoken label. It must appear word for word in the roadmap and in the topic's
  announcement, so keep it short (two to five words).
- `## Pronunciation` table: `| Term | Say as | Note |`. Every acronym and every unusual word
  the narration contains goes here.
- Other sections (audience, visual vocabulary, figure inventory, visual brief, scope) are
  prose or tables the checker does not parse.

## script.md

Sections are `## Opening`, then one `## T1 · Title` per topic in outline order, then
`## Conclusion`. A topic heading is the topic-boundary marker.

Each spoken segment is one line:

```
[S04] [explain] Gentoo penguins average *about five thousand* grams. {C02} {beat}
```

- `[S04]` is the scene the segment plays over. Several lines may share a scene, and a scene
  may hold lines of only one topic.
- `[explain]` is the role: `goal`, `hook`, `puzzle`, `roadmap`, `announce`, `introduce`,
  `explain`, `predict`, `reveal`, `unknown`, `wrap-up`, `bridge`, `synthesis`. Join roles with
  `+` when one sentence does both (`[announce+introduce]`), which is normal in short videos.
- `{C02}` attaches a claim. Put it on every line that states a fact from the data, including
  counts that are facts about the data ("three hundred and forty two birds", "three species").
  Counts about the video itself ("two parts") are not claims; reword them if the checker warns.
- Pause marks: `{beat}` (about 0.75 s, after a key number), `{break}` (about 1.5 s, at a topic
  boundary), `{look:3}` (hold N seconds so viewers can read a figure).
- `*word*` marks spoken emphasis. Use it rarely.
- Spoken text is what remains after removing `[...]`, `{...}`, and `*`. It must contain no
  digits and no symbols such as `%`, `<`, `=`, `±`, `/`, `&`.

Required per topic: `announce`, `introduce`, `explain`, `wrap-up`, `bridge`. The opening needs
`goal` and `roadmap`; the conclusion needs `synthesis`. The last topic's bridge leads into the
conclusion.

Engagement roles (`references/engagement.md`):

- `puzzle` in the opening poses a question from the data. The conclusion must then contain a
  `reveal` that answers it.
- `predict` asks the viewer to commit to an answer. The line needs at least two seconds of
  pause (`{look:3}`), and a later `reveal` in the same section. Its scene needs a `Withheld`
  field. A prediction and its reveal never share a line.
- `unknown` states plainly what the data cannot answer. It is the only role in which a `gap`
  claim may be tagged.
- The checker warns when a video has no puzzle or no prediction, unless the Brief says
  `Engagement: reduced, because …`.

## storyboard.md

`## Figures` comes first, then `## Scenes`.

```
### F01 · Bill length against bill depth
- Type: filled contour plot (2D kernel density) with species overlay
- Data: D02, columns bill_length_mm, bill_depth_mm, species
- Encodings: x = bill length (mm); y = bill depth (mm); contour = how many birds; color = species
- Colormap: sequential, perceptually uniform, light = few birds
- Reading steps: frame → anchor → fill → pattern → takeaway (one line each, see visuals guide)
- Claims: C03, C04
```

```
### S05 · T2
- Narration: explain, wrap-up
- Topic change: no
- Look at: the single darkest contour peak
- Focus by: figure
- Stays: axes, axis labels, outline strip with T2 lit
- Changes: all contours except the peak dim to 20 percent
- Figure: F01, step pattern
- On screen: "r = −0.24" · "n = 342"
- Orientation text: "2 · The pooled trend"
- Motion: highlight
- Intensity: build
- Hold: 2s
- Duration: 11s
- Claims: C04
```

- Required fields: `Topic` (in the heading after `·`), `Look at`, `Focus by`, `Stays`,
  `Changes`, `Duration`. `Focus by` is `figure`, `cursor`, or `figure + cursor`.
- `Topic change` is required, and must describe the visible marker, on the first scene of each
  new topic and on the first scene of the conclusion (for example: every outline item lights).
- `On screen` lists the exact data-bearing strings shown, quoted and separated by `·`. Every
  number in them must appear in the `Values` of a claim the scene lists.
- `Orientation text` holds topic labels, chapter headings, and roadmap items. Numbers there
  are not data and are not checked.
- `Narration: none (silent)` marks a scene with no speech.
- `Withheld` is required on a scene that carries a `[predict]` line: what stays off screen
  until the reveal ("species colors; dots stay gray").
- `Motion` uses the verbs in `references/visuals-and-figures.md`.
- `Changes` may list several changes in the order they happen, each on its own narration cue
  ("axes appear; then one dot lights; then all dots fill"). Never two at the same moment.

### Timing rule the checker uses

A scene needs its narration time (words ÷ speech rate) plus its pause marks plus half its `Hold`
(the other half overlaps the narration). The checker warns when `Duration` is shorter. Count
words while drafting: a budget of about `target minutes × speech rate × 0.8` spoken words leaves
room for holds and pauses.

## evidence-and-review.md

- `## Data sources` table: `| ID | Location | Produced by | Version |`. Location is a path or
  a citation of a results table or figure the project already produced.
- `## Claims` table: `| ID | Claim | Values | Source | Location | Status |`. `Values` holds the
  exact strings as displayed (for example `5076 g; SD 504 g; n = 123`). `Source` is a `D` ID.
  `Status` is `verified` (checked against the source file in this run), `unverified`, or `gap`.
- Then prose sections: `## Simplifications and analogies`, `## Gaps`,
  `## Proposed substantive changes`, `## Review`.
