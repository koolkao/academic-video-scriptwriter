# Review rubric

Review the complete output documents, not just their headings. Run the checker first, then
read with this rubric. If your host can start a sub-agent, run this review in a fresh one that
receives the four files and this rubric but not your drafting notes; a reviewer who did not
write the script finds more.

## Blocking failures

Any one of these means the outputs are not ready, whatever else scores well:

1. A number, result, citation, or quotation in the script or storyboard that does not trace to
   the project's data. (Arithmetic offered under *Proposed substantive changes* for the author
   to confirm is not a violation.)
2. A claim whose meaning changed: causation from association, a dropped comparator, a lost
   interval, a null turned into a trend, a narrowed or widened population.
3. A missing major topic from the brief, or a topic missing its announcement, explanation,
   wrap-up, or bridge.
4. A prerequisite jump: a term, figure type, or idea used before it is explained.
5. A `gap` claim narrated as if supported.

## Tests

- **Checker.** `python3 scripts/check_outputs.py OUTPUT_DIR`. Zero FAIL lines required. Read
  every WARN and either fix it or say why it stands.
- **Narration only.** Read `script.md` aloud (or have it read) without the storyboard. Can a
  listener name the outline, say what each topic was about, and say why the next one followed?
  This tests orientation, not whether visuals are needed.
- **Freeze frame.** Pick any scene in the storyboard at random. From that scene alone, can a
  viewer tell which topic they are in and where to look? If not, the scene lacks an outline
  marker in `Stays` or a clear `Look at`.
- **Two renderers.** Could two different tools (say, slides and an animation library) produce
  recognizably the same video from the storyboard without rewriting the teaching structure? If
  the storyboard relies on tool-specific effects or skips intent, it fails.
- **Listener's ear.** Read three random narration lines as a TTS voice would. Any symbol,
  ambiguous abbreviation, or sentence you had to reread?

## Dimensions

Score each 1–3 (1 = problem, 2 = acceptable, 3 = strong) and write one line of evidence. A high
total does not offset a blocking failure.

| Dimension | Question |
| --- | --- |
| Scientific fidelity | Do the script and figures say exactly what the data say? |
| Objective coverage | Is every learning objective taught and wrapped up? |
| Prerequisite order | Is every idea and figure type explained before it is used? |
| Orientation | Roadmap, announcements, wrap-ups, visible topic markers, synthesis? |
| Transition quality | Does each bridge state a real relationship? |
| Terminology | One name per concept; acronyms defined and pronounced? |
| Focus | One `Look at` per scene, led by figure or cursor, on time with the narration? |
| Figure building | Complex figures built frame → anchor → fill → pattern → takeaway? |
| Narration voice | No hedging, disclaimers, filler, or inflated words; reads naturally aloud? |
| Engagement | Puzzle from the data answered at the end; predictions the viewer can reason toward, with time to think; reasoning out loud; conversational register; unknowns stated plainly? |
| Timing | Narration, holds, and figure reading fit the target? |
| Technology independence | Nothing tied to one tool, provider, or library? |

## Reporting

Write the results in `evidence-and-review.md` under `## Review`:

- checker result (FAIL and WARN counts, and what you did about each WARN)
- the rubric table with scores and evidence
- which tests were actually run, and by whom (drafting agent, fresh sub-agent, person)
- what has not been done: subject-matter review by an expert, testing with real viewers

Never report agent review as evidence that viewers learn better.
