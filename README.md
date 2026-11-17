# academic-video-scriptwriter

An agent skill that writes scripts for academic and scientific videos that viewers can actually
follow. You give it your project's data and results; it gives you a teaching plan, TTS-ready
narration, a visual storyboard with figure specs, and an evidence record in which every number
traces back to your data.

It writes for any production tool (slides, an animation library, an HTML video engine, a video
editor) and does not render anything itself.

## Why

AI explainer pipelines produce videos that look impressive and lose the viewer by the second
minute: no outline, no recap, a new visual style every cut, and a complex figure dumped on screen
all at once. This skill keeps the scientific visuals and adds what makes a lecture by a good
teacher easy to follow:

- **An outline you can hear and see.** A spoken roadmap; each topic announced by name,
  introduced, explained, wrapped up, and bridged to the next; a synthesis at the end. The outline
  stays on screen and lights up as the video moves.
- **One focus of attention at a time.** Every scene names the one thing to look at, led by the
  figure itself or by a large cursor.
- **Complex figures built the way experts read them.** Heat maps, contour plots, radar plots, 3D
  reconstructions, interval plots: frame (axes and encodings) → anchor (one element read in full)
  → fill → pattern → takeaway.
- **Real data only.** Numbers come from data and results your project already produced. The
  skill never makes up data and never computes new statistics; it proposes them for you to add.
- **Narration that does not sound generated.** No disclaimers or stock qualifiers ("it's
  important to note", "results may vary"). Scope and uncertainty are stated as facts; full
  statistics go on screen. Text is prepared for TTS: no digits or symbols, a pronunciation table,
  purposeful pauses.

## Use it

Point your agent (Claude Code, Codex, Cursor, or similar) at this repository and give it a brief:

```
Use the skill at https://github.com/koolkao/academic-video-scriptwriter.
Write a four-minute video for first-year biology students from the results in ./analysis/results.
```

The agent reads `SKILL.md` and follows it. To install it as a Claude Code skill, clone it into
your skills folder:

```
git clone https://github.com/koolkao/academic-video-scriptwriter ~/.claude/skills/academic-video-scriptwriter
```

## What you get

| File | Contents |
| --- | --- |
| `teaching-plan.md` | Audience, objectives, topics in prerequisite order, figure inventory, visual vocabulary and brief, pronunciation, scope, timing. |
| `script.md` | Every spoken word, by topic, with scene, role, claim, and pause marks. |
| `storyboard.md` | Figure specs (type, data, encodings, colormap, reading steps) and scenes (focus, what stays, what changes, on-screen values, motion, hold, duration). |
| `evidence-and-review.md` | Data sources, claims with exact values and verification status, gaps, proposed changes, review results. |

A line of narration:

```
[S10] [explain] Within Adelies, the correlation is point three nine. Within Chinstraps, point six five. Within Gentoos, point six four. {C03} {C04} {C05} {beat}
```

The scene it plays over:

```
### S10 · T3
- Look at: each upward trend line in turn
- Focus by: figure
- Stays: outline strip, three islands, faint pooled line
- Changes: three within-species trend lines draw upward, one per island, each with its r label
- Figure: F02, step pattern
- On screen: "Adelie r = 0.39 · n = 151" · "Chinstrap r = 0.65 · n = 68" · "Gentoo r = 0.64 · n = 123" · "each p < 0.001"
- Motion: draw
- Duration: 17s
- Claims: C03, C04, C05
```

## The checker

```
python3 scripts/check_outputs.py path/to/output-folder
```

Standard library only. It reads the four files and reports:

- **FAIL** (exit code 1): an on-screen number not found in the values of a listed claim; a claim
  without a data source; a gap claim used; a digit, symbol, or banned phrase in the narration; a
  topic missing its announcement, introduction, explanation, wrap-up, or bridge; a roadmap or
  announcement that does not say the topic title; a new topic with no visible marker; broken IDs.
- **WARN**: unverified claims, acronyms with no pronunciation, quantities without a claim tag,
  long sentences, scenes too short for their narration, runtime over target.

It checks structure, tracing, and TTS-readiness. It cannot tell whether a claim is true or a
transition is good; `references/review-rubric.md` covers that, ideally in a fresh agent.

Tests: `python3 -m unittest discover tests`.

## Examples

Both are built from the real [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins)
data (CC0). `examples/penguin-project/` stands in for a research project: raw data, the analysis
script, and its results tables.

- [`examples/short-body-mass/`](examples/short-body-mass/): which species is the heavy one;
  about a minute and a half, two topics, a strip plot and an interval plot.
- [`examples/bill-paradox/`](examples/bill-paradox/): Simpson's paradox in bill shape; about six
  minutes, five topics, a contour plot that splits by species, a radar plot, and correlation heat
  maps. Includes a topic change over the same figure, a gap (diet), and an analogy with its limit.

## Layout

```
SKILL.md                  entry point for the agent
references/               structure, evidence, narration and TTS, visuals and figures, rubric, format
templates/                the four output files
scripts/                  check_outputs.py, banned_phrases.txt
tests/                    checker tests
examples/                 penguin project and two worked examples
evals/                    evaluation cases and recorded runs
docs/                     design, construction plan, source and license review
```

## Limits

- An agent's review is not a subject-matter review and not a test with real viewers. The outputs
  say which of these have happened.
- Timing is an estimate from word counts until real TTS audio exists.
- The checker's quantity-word warning has false positives (for example "near zero" in a legend).

## Credits

The design draws on ideas from
[Educational Video Creator](https://github.com/skindhu/skind-skills/tree/main/skills/educational-video-creator)
(MIT), [Academic Presentations](https://github.com/yigityildiz0/scientific-agent-skills/tree/main/skills/codex/academic-presentations),
and OpenMontage's [Script Director](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/pipelines/explainer/script-director.md)
and [Storytelling](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/creative/storytelling.md)
skills. No text was copied from them; the license review is in `docs/source-review.md`.

Example data: Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago
(Antarctica) penguin data. Collected by Dr. Kristen Gorman with the Palmer Station, Antarctica
LTER. CC0-1.0.

## License

MIT
