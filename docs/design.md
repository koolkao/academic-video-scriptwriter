# Design: academic-video-scriptwriter

Date: 2026-11-17. Builds on `docs/construction-plan.md`; where they differ, this document wins.

## Why

Explainer videos produced with existing faceless-explainer workflows looked impressive but were
hard to follow. Reviewing that workflow suggested why: frames were the only unit (no topic layer,
no roadmap or recap), each frame chose a fresh visual surface, the structure came from marketing
(hook, pain point, call to action), and density rules favored spectacle over a single focus. This
skill keeps the striking visuals but subordinates them to orientation.

## Goals

- Viewers always know what they are learning, where it sits, what they just learned, and why the
  next part follows.
- Scientific-looking visuals built from the project's own data, including the complex figures
  of academic papers (heat maps, contour, radar, 3D reconstructions), made readable by building
  them step by step.
- Narration ready for TTS that does not sound generated.
- Output that any production tool can build from.

## Non-goals

Rendering, TTS execution, media generation, publishing; choosing a visual style; research beyond
the supplied materials.

## Anti-goals

The skill has failed, even if every file is produced, if: a number does not come from the
project's data; a claim's meaning has shifted; the narration carries disclaimers or stock
qualifiers; a viewer could freeze any frame and not know what topic they are in or where to look.

## Decisions made with the user

| Topic | Decision |
| --- | --- |
| Data | Numbers come only from the respective project's data. Never make up data. This replaces the construction plan's allowance for labeled illustrative data. |
| Computation | The skill uses only numbers and figures the project already produced. It does not compute new statistics; it proposes them. |
| Narration voice | No disclaimers or qualifier sentences. Scope and uncertainty become concrete facts inside the claim; full statistics go on screen. |
| Focus | Every scene has one focus of attention, led by the figure or by a large cursor. |
| Pacing | Deliberate pauses with defined purposes (beat, look, break). |
| Voice | TTS by default; markup stays provider-neutral. |
| Visual taste | Scientific graphics, graphs, numbers, statistics; complex academic figure types welcome. |
| Approach | Text-only skill plus a small standard-library checker (adapted in spirit from the user's academic-humanizer preservation check); review in a fresh sub-agent when the host has one. |
| Distribution | Public GitHub repository. |
| Engagement (v0.2) | Built into the default workflow: opening puzzle answered at the end, predictions with thinking time and withheld answers, reasoning out loud, conversational register, plainly stated unknowns. Explaining before naming is optional. Techniques modeled on teachers such as Feynman, never an imitation of a person. A formal talk may set `Engagement: reduced` with a reason. |

## Approaches considered

1. **Text-only skill.** Simplest and most portable, but the two hardest rules (no made-up data,
   no hedging) would rest on agent self-review.
2. **Text-only skill plus a checker script (chosen).** Same portability (Python standard
   library), and the hardest rules get a check that actually runs: every on-screen number traced
   to a claim's values, banned phrasings, TTS-hostile text, required structure, timing.
3. **Plus a mandatory separate reviewer.** Better comprehension review, but depends on host
   sub-agent support. Folded into option 2 as "use a fresh sub-agent if available".

For engagement (v0.2) the options were: built into the default workflow (chosen); an on/off
switch in the teaching plan (rejected: the user wants these by default); a rewrite pass after
drafting (rejected: the puzzle and predictions have to shape the outline and storyboard).

## Calls made by the builder

- Fixed markup (`references/output-format.md`) so the checker can parse outputs; IDs O, T, S, F,
  C, D.
- Topic titles are spoken labels and must appear word for word in the roadmap and announcement.
- `On screen` (data, checked) is separate from `Orientation text` (labels, not checked).
- Five-step figure build: frame, anchor, fill, pattern, takeaway.
- Two FAIL/WARN tiers, exit code 1 on FAIL, as in the humanizer.
- Worked examples use Palmer Penguins (CC0) with a stand-in project analysis, so every example
  number is real and reproducible.
- MIT license. All text is original; source licenses are recorded in `docs/source-review.md`.
